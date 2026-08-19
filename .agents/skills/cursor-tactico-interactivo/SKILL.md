---
name: cursor-tactico-interactivo
description: >-
  Diseña, implementa, audita y optimiza cursores tácticos interactivos y retículas de alta precisión estilo HUD/militar (anillo cyan neón con cruz ortogonal y punto central magenta). Úsalo cuando el usuario solicite crear un cursor táctico, implementar un cursor personalizado interactivo, solucionar problemas de retardo (lag), saltos, parpadeos (jitter), o auditar la integración del cursor en cualquier aplicación web.
---

# Cursor Táctico Interactivo & Retícula HUD de Alta Precisión

Esta habilidad proporciona el flujo de trabajo integral, las especificaciones matemáticas de geometría y el motor de renderizado acelerado por hardware para construir, integrar y auditar **cursores tácticos personalizados interactivos** sin fallos, sin lag y con soporte multiplataforma.

---

## 1. Documentación de Referencia y Recursos

- 📐 **[Anatomía de la Retícula Táctica y Fórmulas](./references/anatomia_cursor_tactico.md)**: Geometría, colores neón, anclaje de píxeles pares y estados reactivos.
- 🛡️ **[Guía de Prevención de Bugs y Checklist de Calidad](./references/guia_prevencion_bugs.md)**: Cómo evitar los 10 errores clásicos (conflicto con cursor nativo, parpadeo de subelementos, atrapamiento en iframes, problemas en móviles).
- 📦 **[Plantilla de Componente Listo para Producción](./resources/componente_cursor_tactico.html)**: Código HTML, CSS modular y motor JS en un solo bloque autocontenido.
- 🛠️ **[Script Validador de Calidad](./scripts/verificar_cursor.py)**: Script automatizado en Python para auditar código HTML/CSS/JS y prevenir bugs.

---

## 2. Los 4 Pilares del Cursor Táctico Infalible

Para que un cursor personalizado funcione sin ningún tipo de error, debe cumplir estrictamente 4 reglas de oro:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. ANCLAJE POR HARDWARE (RAF + translate3d)                            │
│    Actualización sincronizada con la tasa de refresco (60/120/144Hz)   │
│    usando requestAnimationFrame y translate3d(clientX, clientY, 0).    │
├────────────────────────────────────────────────────────────────────────┤
│ 2. GEOMETRÍA EN NÚMEROS PARES (0 Subpixel Blur)                       │
│    Diámetro del anillo: 36px/38px. Punto central: 6px.                 │
│    Evita dimensiones impares (5px) que causan desplazamientos 2.5px.   │
├────────────────────────────────────────────────────────────────────────┤
│ 3. DELEGACIÓN DE EVENTOS CON relatedTarget                             │
│    Evita parpadeos (jitter) al moverse entre hijos de botones o cards. │
├────────────────────────────────────────────────────────────────────────┤
│ 4. AISLAMIENTO TOTAL (pointer-events: none)                            │
│    Todos los elementos del cursor deben tener pointer-events: none !important │
│    para no bloquear clics ni capturar eventos del mouse.               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Protocolo de Implementación Paso a Paso

Cuando se solicite implementar o corregir el cursor táctico:

### Paso 1: Estructura HTML Base
Inserta el contenedor del cursor justo antes de la etiqueta de cierre `</body>`:
```html
<!-- TACTICAL RETICLE CURSOR HUD -->
<div id="tacticalCursor" aria-hidden="true">
  <span id="tacticalCursorBadge">[TARGET]</span>
</div>
<div id="tacticalCursorDot" aria-hidden="true"></div>
```

### Paso 2: Estilos CSS de Alta Precisión
- Define el anillo principal `#tacticalCursor` con `position: fixed`, `z-index: 9999999`, `will-change: transform`.
- Usa pseudo-elementos `::before` y `::after` con `box-shadow` simétrico para dibujar las 4 miras ortogonales sin elementos DOM adicionales.
- Define `#tacticalCursorDot` como un círculo central de 6px en `#FF007F` (Magenta Neón).
- Desactiva automáticamente el cursor en pantallas táctiles o móviles con `@media (max-width: 900px), (hover: none)`.

### Paso 3: Motor JavaScript de Renderizado Suave
- Almacena las coordenadas `clientX` y `clientY` en eventos `pointermove` y `mousemove`.
- Ejecuta la traslación dentro de `requestAnimationFrame`.
- Maneja transiciones de estado (`hover`, `active`/clic, `text`) mediante delegación inteligente en `document` verificando `e.target.closest()`.

---

## 4. Matriz de Estados Reactivos

| Estado | Selector / Condición | Apariencia del Cursor | Etiqueta HUD Badge |
|---|---|---|---|
| **Reposo** | Fondo de página | Anillo Cyan `36px`, punto Magenta `6px` | Oculto o `[TARGET]` |
| **Hover Interactivo** | Botones, enlaces, cards | Anillo expandido `scale(1.25)`, color Magenta, punto Cyan | `[ACCEDER]`, `[EXPLORAR]`, `[VER VIDEO]` |
| **Entrada de Texto** | Inputs, textareas | Corchete vertical rectangular | `[ESCRIBIR]` |
| **Disparo / Clic** | `pointerdown` / mousedown | Contracción táctica `scale(0.82)` + destello blanco | Reactivo |
| **Dispositivo Móvil** | `(hover: none)` / touch | Oculto (`display: none !important`) | Oculto |

---

## 5. Checklist de Auto-Auditoría (QA)

Antes de dar por terminada la integración del cursor, verifica:
- [ ] ¿El anillo y el punto central están perfectamente concéntricos en pantallas de 1x, 2x (Retina) y 4K?
- [ ] ¿El cursor tiene `pointer-events: none !important` en todos sus elementos y pseudo-elementos?
- [ ] ¿Al pasar sobre botones con íconos o textos anidados, el cursor se mantiene estable sin parpadear?
- [ ] ¿Al hacer clic sobre cualquier elemento interactivo, el clic se registra de forma instantánea sin bloqueos?
- [ ] ¿En dispositivos móviles o al redimensionar a menos de 900px, el cursor se oculta limpiamente y el touch nativo responde con normalidad?
- [ ] ¿El script está verificado con el script `./scripts/verificar_cursor.py`?
