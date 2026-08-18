# Guía de Auto-Auditoría de Calidad (QA Lead)

Esta guía detalla la lista de verificación que el agente debe ejecutar internamente durante la **FASE 5 (REVISIÓN)** antes de entregar código al usuario.

---

## 1. Lista de Verificación de QA (Checklist)

### A. Lógica y Robustez Funcional
- [ ] **Manejo de Casos Límite (*Edge Cases*):** ¿Se manejan entradas nulas, vacías, valores extremos o respuestas inesperadas de APIs?
- [ ] **Flujo Asíncrono:** ¿Están adecuadamente gestionadas las promesas (`async/await`, `.catch()`, bloques `try/catch`)?
- [ ] **Estados de Carga y Error:** ¿La interfaz muestra indicadores de carga (*skeletons* / *spinners*) y mensajes de error comprensibles para el usuario?

### B. Seguridad del Software
- [ ] **Inyección y Sanitización:** ¿Se validan y sanitizan todos los inputs del usuario para prevenir XSS, SQLi u otras inyecciones?
- [ ] **Manejo de Secretos:** ¿Se evita la exposición de API keys, tokens o credenciales sensibles en el frontend o código cliente?
- [ ] **Autenticación y Autorización:** ¿Las rutas y acciones protegidas verifican los permisos correspondientes?

### C. Rendimiento y Eficiencia
- [ ] **Renderizado Innecesario:** ¿Se previenen re-renders excesivos en React/Next.js mediante memoización o separación de componentes de cliente/servidor (`'use client'` vs Server Components)?
- [ ] **Carga de Recursos:** ¿Las imágenes y fuentes utilizan optimizaciones modernas (`next/image`, `next/font`)?
- [ ] **Tamaño del Bundle:** ¿Se importan únicamente los módulos necesarios en lugar de librerías completas?

### D. Accesibilidad y Estándares Web (a11y)
- [ ] **Jerarquía HTML Semántica:** ¿Se emplean etiquetas correctas (`<main>`, `<section>`, `<article>`, `<button>`, `<a>`)?
- [ ] **Etiquetas ARIA y Contraste:** ¿Los botones sin texto visible tienen `aria-label` y los contrastes de color cumplen con las pautas WCAG?

---

## 2. Formato del Reporte de Auto-Auditoría

El reporte de salida en la **Fase 5** debe estructurarse con la siguiente plantilla:

```markdown
### Reporte de Auto-Auditoría (QA Lead)

- 🔒 **Seguridad:** [Aprobado / Observaciones / Mitigaciones aplicadas]
- ⚡ **Rendimiento:** [Evaluación de complejidad, renderizado y recursos]
- 🧪 **Lógica y Casos Límite:** [Validación de escenarios probados]
- ♿ **Accesibilidad & Estándares:** [Verificación semántica y responsive]
- 📊 **Dictamen Final:** [APROBADO PARA PRODUCCIÓN / REQUIERE REFINAMIENTO EN FASE 6]
```
