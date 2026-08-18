# Convenciones y Estándares de Habilidades en Google Antigravity

Este documento detalla las reglas formales, ubicaciones y orden de prioridad para la creación de habilidades (*skills*) en el ecosistema de Google Antigravity.

---

## 1. Ubicaciones de Habilidades

Google Antigravity reconoce habilidades en dos ámbitos principales:

### A. Ámbito de Espacio de Trabajo (Workspace / Local)
- **Ruta estándar:** `<raiz-del-proyecto>/.agents/skills/<nombre-habilidad>/`
- **Rutas alternativas compatibles:** `<raiz-del-proyecto>/skills/<nombre-habilidad>/` o `<raiz-del-proyecto>/.agent/skills/<nombre-habilidad>/`
- **Propósito:** Flujos de trabajo específicos de un proyecto (ej. despliegues, estándares de arquitectura, pruebas locales del repositorio).
- **Control de versiones:** Se recomienda incluirlas en el control de versiones (Git) para compartirlas con el equipo.

### B. Ámbito Global (Usuario / Máquina)
- **Ruta estándar:** `~/.gemini/config/skills/<nombre-habilidad>/`
- **Propósito:** Habilidades transversales disponibles en cualquier proyecto o sesión de trabajo en tu máquina local (ej. formateadores globales, generadores de plantillas, utilidades generales).

---

## 2. Orden de Prioridad y Precedencia

Cuando existen varias habilidades con el mismo nombre o cuando el agente evalúa qué habilidad activar, se sigue el siguiente orden de resolución:

1. **Habilidades del Espacio de Trabajo (`.agents/skills/`)**: Tienen la **máxima prioridad** y sobreescriben cualquier versión global o incorporada.
2. **Habilidades Declaradas Explícitamente (`skills.json`)**: Configuraciones registradas en el proyecto.
3. **Habilidades Globales de Usuario (`~/.gemini/config/skills/`)**: Disponibles para todos los proyectos del usuario.
4. **Habilidades Incorporadas (*Built-in*)**: Habilidades preinstaladas en Antigravity IDE.

---

## 3. Especificación del Frontmatter YAML

El archivo `SKILL.md` debe comenzar obligatoriamente con un bloque Frontmatter YAML delimitado por `---`.

```yaml
---
name: nombre-de-la-habilidad
description: >-
  Descripción precisa y contextual que explica QUÉ hace la habilidad y CUÁNDO debe activarse.
  Escrita preferentemente en tercera persona con palabras clave relevantes.
---
```

### Reglas de los Campos:
| Campo | Tipo | Obligatorio | Restricciones |
| :--- | :--- | :--- | :--- |
| **`name`** | String | Sí | Máximo 64 caracteres. Solo minúsculas, números y guiones (`kebab-case`). Sin espacios ni caracteres especiales. |
| **`description`** | String | Sí | Máximo 1024 caracteres. Define los criterios de activación para el enrutador semántico del agente. |

> [!IMPORTANT]
> El campo `description` es el elemento más crucial: el agente solo lee el nombre y la descripción en el inicio de la sesión. El cuerpo completo de `SKILL.md` solo se carga en el contexto cuando el agente decide activarla (*Progressive Disclosure*).
