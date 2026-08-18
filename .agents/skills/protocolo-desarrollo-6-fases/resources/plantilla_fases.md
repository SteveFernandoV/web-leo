# Plantilla de Salida: Protocolo de Desarrollo de 6 Fases

Estructura visual estandarizada para responder al usuario siguiendo las 6 fases del protocolo.

---

```markdown
## FASE 1: INVESTIGACIÓN DEL PROBLEMA (Discovery)
* **Propósito Principal:** [Descripción clara del objetivo de la solución]
* **Público Objetivo y Contexto:** [A quién va dirigido y en qué entorno operará]
* **Requisitos Clave Detectados:**
  - Requisito Funcional 1
  - Requisito Funcional 2
* **Restricciones Técnicas:** [Límites, compatibilidad o reglas del negocio]

---

## FASE 2: PLANIFICACIÓN (Roadmap)
* **Tech Stack Propuesto:**
  - Frontend: [Framework / Librerías]
  - Estilos / UI: [Tailwind CSS / Sistema de Diseño]
  - Backend / Datos: [API / Base de datos / Estado]
* **Estructura de Archivos / Arquitectura:**
  ```text
  directorio/
  ├── archivo_1.tsx
  └── archivo_2.ts
  ```
* **Plan de Acción Paso a Paso:**
  1. [Paso 1: Configuración inicial]
  2. [Paso 2: Implementación de componentes centrales]
  3. [Paso 3: Integración de lógica y datos]

---

## FASE 3: DISEÑO (UI/UX)
* **Concepto Visual & Estética:** [Descripción de la dirección artística, paleta de colores y tipografía]
* **Habilidad de Diseño Aplicada:** [Ej. `disenador-landing-futurista` / Sistema Glassmorphism / Dark Mode]
* **Experiencia de Usuario (UX) y Flujo:**
  - Estado Inicial
  - Micro-interacciones y Estados Hover/Active
  - Adaptabilidad Responsiva (Mobile / Desktop)

---
> [!NOTE]
> *Si la solicitud es compleja, detenerse aquí y solicitar aprobación al usuario antes de avanzar a la Fase 4.*
---

## FASE 4: EJECUCIÓN (Coding)
*Archivos de código modular, limpio, moderno y comentado:*

```tsx
// [Nombre del archivo o componente]
export function MiComponente() {
  // Lógica y marcado
}
```

---

## FASE 5: REVISIÓN (Testing & Debugging)
* **Simulación de Ejecución & Análisis Crítico:**
  - 🔒 Seguridad y Manejo de Datos: [OK / Sin vulnerabilidades]
  - ⚡ Rendimiento y Complejidad: [OK / Optimizado]
  - 🧪 Lógica y Casos Límite: [Validado]
* **Dictamen:** [Código verificado con éxito / Se detectaron ajustes para la Fase 6]

---

## FASE 6: CORRECCIÓN (Refinement & Entrega)
* **Refinamientos Aplicados:** [Correcciones automáticas realizadas o confirmación de código listo]
* **Instrucciones de Despliegue / Pasos Siguientes:**
  1. Comando de instalación o ejecución (`npm run dev`).
  2. Recomendaciones de escalabilidad o mejoras futuras.
```
