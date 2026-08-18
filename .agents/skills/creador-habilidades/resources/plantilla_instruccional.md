# Plantilla: Habilidad Instruccional / Procedimental (Runbook)

Utiliza esta plantilla cuando la habilidad consista en una serie de directrices, pasos de razonamiento, estándares de código o procedimientos sin necesidad de scripts de soporte.

---

```markdown
---
name: nombre-de-la-habilidad
description: >-
  Describe con precisión qué hace esta habilidad y cuándo debe activarse en tercera persona.
  Ejemplo: "Guía el proceso de revisión de código para pull requests siguiendo los estándares de calidad del equipo."
---

# Título de la Habilidad

## 1. Visión General
Breve descripción del objetivo de esta habilidad, beneficios y contexto de uso.

## 2. Requisitos Previos y Entorno
- Herramientas requeridas o variables de entorno necesarias.
- Referencias a otras habilidades si existe dependencia.

## 3. Flujo de Trabajo Paso a Paso

### Paso 1: [Nombre del Paso]
- Instrucciones detalladas de lo que el agente debe hacer.
- Criterios de validación o decisiones a tomar.

### Paso 2: [Nombre del Paso]
- Acciones a ejecutar.
- Consideraciones especiales o excepciones.

### Paso 3: [Nombre del Paso]
- Consolidación y entrega de resultados al usuario.

## 4. Árbol de Decisión y Manejo de Errores
- **Si ocurre [Situación A]:** Realizar [Acción 1].
- **Si ocurre [Situación B]:** Solicitar aclaración al usuario.

## 5. Criterios de Verificación
Instrucciones para comprobar que el resultado final es correcto antes de dar por terminada la tarea.
```
