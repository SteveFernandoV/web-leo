# Ejemplo Completo de Habilidad en Español: `auditor-accesibilidad-web`

Este es un ejemplo representativo de cómo debe verse una habilidad completa y bien documentada en idioma español.

---

```markdown
---
name: auditor-accesibilidad-web
description: >-
  Audita y corrige problemas de accesibilidad (a11y) en componentes frontend HTML/CSS/React según las pautas WCAG 2.1 AA.
  Úsalo cuando el usuario pida evaluar contrastes, navegación por teclado, roles ARIA o soporte para lectores de pantalla.
---

# Auditor de Accesibilidad Web (WCAG 2.1 AA)

Esta habilidad proporciona un marco de trabajo paso a paso para identificar y corregir barreras de accesibilidad en aplicaciones web modernas.

## 1. Alcance y Cobertura
- Estructura semántica de etiquetas HTML5 (`<main>`, `<nav>`, `<header>`, `<article>`).
- Atributos y roles ARIA (`aria-label`, `aria-expanded`, `aria-live`).
- Contraste cromático mínimo de 4.5:1 para texto normal y 3:1 para texto grande.
- Navegación y foco accesible por teclado (`tabindex`, `:focus-visible`).

## 2. Flujo de Auditoría

### Paso 1: Análisis Semántico
1. Revisa el archivo HTML/JSX y verifica la jerarquía de encabezados (`<h1>` a `<h6>`). Asegúrate de que solo exista un `<h1>` por página.
2. Comprueba que todos los elementos interactivos (`<button>`, `<a>`) utilicen etiquetas nativas en lugar de `<div>` con manejadores `onClick`.

### Paso 2: Evaluación de Atributos ARIA
1. Verifica que todas las imágenes posean el atributo `alt` (o `alt=""` si son puramente decorativas).
2. Si existen modales o menús desplegables, comprueba el estado `aria-expanded="true/false"` y el atrapado de foco (*focus trap*).

### Paso 3: Propuesta y Aplicación de Correcciones
1. Genera un reporte conciso con los hallazgos categorizados por severidad (Crítica, Moderada, Leve).
2. Aplica las correcciones en el código fuente manteniendo la estética y funcionalidad original.

## 3. Criterios de Verificación
- Confirmar que ningún elemento interactivo sea inaccesible mediante la tecla `Tab`.
- Validar contraste de colores utilizando paletas accesibles.
```
