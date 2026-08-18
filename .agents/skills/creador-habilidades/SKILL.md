---
name: creador-habilidades
description: >-
  Crea, diseña y estructura nuevas habilidades (skills) personalizadas para Google Antigravity en idioma español.
  Úsalo cuando el usuario pida crear una nueva habilidad, diseñar un SKILL.md, estructurar runbooks o empaquetar flujos de trabajo reutilizables.
---

# Creador de Habilidades para Google Antigravity

Esta habilidad guía al agente en el diseño, estructuración e implementación de nuevas habilidades (*skills*) personalizadas para Google Antigravity en idioma español, siguiendo las especificaciones oficiales de la plataforma ([Documentación oficial de Skills](https://antigravity.google/docs/skills)).

---

## 1. Documentación de Referencia y Recursos

Para profundizar en aspectos específicos durante la creación de una habilidad, consulta los siguientes recursos:

- 📖 **[Convenciones y Estándares de Antigravity](./references/convenciones_antigravity.md)**: Ubicaciones (`.agents/skills/` vs `~/.gemini/config/skills/`), prioridades y reglas YAML.
- 📐 **[Guía de Diseño y Buenas Prácticas](./references/guia_diseno_habilidades.md)**: Divulgación progresiva (*Progressive Disclosure*), modularidad y manejo de contexto.
- 📝 **[Plantilla: Habilidad Instruccional](./resources/plantilla_instruccional.md)**: Para flujos de trabajo paso a paso, guías de estilo y runbooks.
- ⚙️ **[Plantilla: Habilidad con Scripts](./resources/plantilla_con_scripts.md)**: Para habilidades que integran scripts y herramientas en `scripts/`.
- 💡 **[Ejemplo Completo en Español](./examples/ejemplo_habilidad_espanol.md)**: Ejemplo de referencia de una habilidad lista para producción.

---

## 2. Estructura Estándar de una Habilidad

Toda habilidad debe residir en su propio directorio dentro de la carpeta de habilidades:

```text
skills/<nombre-en-kebab-case>/
├── SKILL.md                 # [Obligatorio] Archivo principal con frontmatter YAML
├── references/              # [Opcional] Documentación detallada, manuales o APIs
├── resources/               # [Opcional] Plantillas, prompts, configuraciones base
├── examples/                # [Opcional] Ejemplos de entrada/salida y casos de uso
└── scripts/                 # [Opcional] Scripts ejecutables auxiliares
```

---

## 3. Protocolo de Creación en 4 Fases

Cuando el usuario solicite crear una nueva habilidad, sigue rigurosamente este flujo de trabajo:

### Fase 1: Descubrimiento y Alcance (Interacción con el Usuario)
Antes de generar archivos, aclara los requerimientos clave mediante una conversación concisa:
1. **Objetivo único:** ¿Qué problema o flujo de trabajo específico resolverá la habilidad?
2. **Disparador (*Trigger*):** ¿Con qué frases, palabras clave o contextos debe activarse automáticamente?
3. **Tipo de habilidad:**
   - *Instruccional / Runbook:* Directrices de razonamiento, estándares o procesos paso a paso (sin código adicional).
   - *Técnica / Con Scripts:* Requiere llamadas a APIs, procesamiento de datos o comandos automatizados empaquetados en `scripts/`.
4. **Ámbito de instalación:**
   - *Workspace (Local):* `.agents/skills/<nombre>/` (recomendado para proyectos específicos).
   - *Global:* `~/.gemini/config/skills/<nombre>/` (disponible en todos los proyectos).

### Fase 2: Diseño y Arquitectura
1. **Nombre:** Define un identificador único en minúsculas con guiones (ej. `generador-api-docs`, `auditor-seguridad`).
2. **Descripción YAML:** Redacta una descripción clara y rica en palabras clave contextuales en tercera persona (máx. 1024 caracteres).
3. **Modularidad:** Aplica el principio de *divulgación progresiva*: mantén `SKILL.md` conciso y delega detalles extensos a `references/` o `resources/`.

### Fase 3: Implementación de Archivos
1. Crea el directorio de la habilidad en la ruta seleccionada.
2. Genera el archivo `SKILL.md` con su bloque Frontmatter YAML inicial y las secciones principales:
   - Visión General y Alcance.
   - Enlaces a referencias y recursos secundarios.
   - Flujo de trabajo paso a paso numerado.
   - Árbol de decisiones y manejo de errores.
   - Criterios de verificación concluyentes.
3. Si la habilidad incluye scripts (`scripts/`), asegúrate de que acepten `--help` y dirijan las salidas a archivos (ej. JSON) en lugar de saturar `stdout`.

### Fase 4: Validación y Verificación
1. **Validación YAML:** Verifica que el frontmatter sea sintácticamente válido (sin tabulaciones indebidas ni caracteres inválidos).
2. **Comprobación de Enlaces:** Asegúrate de que todos los enlaces a archivos locales (`./references/...`) sean relativos y correctos.
3. **Prueba de Activación:** Plantea al usuario 2 o 3 ejemplos de preguntas con las que Antigravity activará la nueva habilidad.

---

## 4. Reglas de Oro para Habilidades en Antigravity

- ✅ **Enfocada y Específica:** Cada habilidad debe hacer una sola cosa excepcionalmente bien.
- ✅ **Excelente Descripción:** El enrutador de Antigravity decide activar una habilidad basándose únicamente en su `name` y `description`.
- ✅ **Ahorro de Contexto:** No dupliques conocimientos generales que el modelo ya posee; enfócate en los procedimientos, convenciones y particularidades del proyecto.
- ✅ **Idioma Español:** Toda la documentación, instrucciones y ejemplos deben estar redactados en español claro, profesional y estructurado.
