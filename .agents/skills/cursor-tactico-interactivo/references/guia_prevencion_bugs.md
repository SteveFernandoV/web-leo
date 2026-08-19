# Guía de Prevención de Errores y Diagnóstico de Bugs en Cursores

Esta guía enumera los 10 errores más comunes al implementar cursores personalizados interactivos en el navegador y las soluciones definitivas para cada uno.

---

## Catálogo de los 10 Errores Críticos

### 1. El Desastre de `cursor: none !important` en Todo el Documento
- **Síntoma:** El puntero del ratón desaparece completamente de la página web si el script JS se demora en cargar o si el elemento `#tacticalCursor` está con `opacity: 0`.
- **Causa:** Aplicar `cursor: none !important` a nivel global (`*, *::before, *::after`) sin garantizar que el script de dibujo esté corriendo.
- **Solución Correcta:** Solo aplicar `cursor: none` condicionado dentro de una clase activa en el `body` (ej. `body.custom-cursor-active`) una vez que el primer evento de movimiento del mouse haya posicionado el cursor con éxito, o mantener el cursor nativo y hacer del retículo un acompañante de precisión.

### 2. Parpadeo y Temblor al pasar sobre Elementos con Hijos (Jittering)
- **Síntoma:** Cuando el usuario pasa el mouse sobre un botón con un ícono (`<button><svg>...</svg><span>Texto</span></button>`), el cursor parpadea y tiembla frenéticamente.
- **Causa:** El evento `mouseout`/`pointerout` se dispara cada vez que el puntero se mueve del `<button>` al `<svg>` o al `<span>`, eliminando y re-agregando la clase `.cursor-hover` decenas de veces por segundo.
- **Solución Correcta:** Utilizar `e.relatedTarget.closest(selector)` en el listener de salida para verificar si el puntero sigue dentro del elemento interactivo antes de remover la clase de hover.

### 3. Falta de `pointer-events: none` (Bloqueo de Clics)
- **Síntoma:** El usuario intenta hacer clic en un botón o enlace, pero nada ocurre; o el cursor se "traba" sobre el elemento.
- **Causa:** El elemento `#tacticalCursorBadge` o `#tacticalCursor` carece de `pointer-events: none !important` y captura el clic en lugar del botón subyacente.
- **Solución Correcta:** Asegurar que `#tacticalCursor`, `#tacticalCursorDot`, `#tacticalCursorBadge` y todos sus pseudo-elementos (`::before`, `::after`) tengan `pointer-events: none !important` y `user-select: none !important`.

### 4. Retardo Elástico Molesto (Lag por Lerp Inadecuado)
- **Síntoma:** El usuario mueve el mouse rápido y el cursor personalizado se queda atrás como si flotara en gelatina o estuviera desfasado.
- **Causa:** Usar un factor de interpolación lineal (*lerp*) demasiado bajo (`0.1` o `0.2`) sin actualización instantánea de coordenadas.
- **Solución Correcta:** Actualizar las coordenadas directamente mediante `translate3d(clientX, clientY, 0)` dentro de un bucle `requestAnimationFrame` sin desfase de coordenadas.

### 5. Aberración de Subpíxeles y Desalineación del Punto
- **Síntoma:** El punto central rosa aparece ligeramente hacia la izquierda o borroso respecto a la cruz cyan.
- **Causa:** Tamaños de píxeles impares (ej. 5px), donde `translate(-50%, -50%)` calcula `2.5px`, obligando al motor gráfico a interpolar medios píxeles.
- **Solución Correcta:** Utilizar exclusivamente dimensiones en números pares (`36px`, `38px` para el anillo; `6px` para el punto).

### 6. Desaparición al pasar sobre Iframes / Videos
- **Síntoma:** Al pasar el cursor sobre un video de YouTube integrado (`<iframe>`) o un mapa, el cursor desaparece o se congela en el borde.
- **Causa:** Los `iframes` son contextos de navegación aislados y el documento principal deja de recibir eventos de mouse.
- **Solución Correcta:** Al detectar `mouseover` sobre un contenedor de iframe, permitir que el cursor nativo tome el control o superponer un overlay transparente si solo se requiere previsualización.

### 7. Comportamiento Roto en Pantallas Táctiles / Móviles
- **Síntoma:** En celulares o tablets, aparece un círculo fijo congelado en la esquina o persiguiendo los toques con parpadeos.
- **Causa:** No deshabilitar el cursor táctico en dispositivos táctiles.
- **Solución Correcta:**
  ```css
  @media (max-width: 900px), (hover: none), (pointer: coarse) {
    #tacticalCursor, #tacticalCursorDot, #tacticalCursorBadge {
      display: none !important;
    }
  }
  ```

### 8. Desplazamiento Fantasma durante el Scroll
- **Síntoma:** El usuario scrollea la página con la rueda del ratón y el cursor se desplaza con el contenido.
- **Causa:** Usar `position: absolute` en lugar de `position: fixed`.
- **Solución Correcta:** Usar siempre `position: fixed; top: 0; left: 0;` con `clientX` y `clientY`.

### 9. Afectación por Contextos de Apilamiento (*Stacking Contexts*)
- **Síntoma:** El cursor queda tapado detrás de modales, headers con `backdrop-filter` o elementos 3D con `perspective`.
- **Causa:** Un `z-index` insuficiente o inserción dentro de un contenedor relativo.
- **Solución Correcta:** Insertar `#tacticalCursor` como hijo directo de `<body>` con `z-index: 9999999`.

### 10. Saturación de Eventos y Caída de FPS
- **Síntoma:** El navegador experimenta tirones al mover el mouse en pantallas de 144Hz o 240Hz.
- **Causa:** Manipular estilos pesados del DOM directamente dentro del listener de `mousemove`.
- **Solución Correcta:** El listener de eventos solo debe guardar las variables `clientX` y `clientY`; la mutación de `style.transform` debe residir exclusivamente en el bucle `requestAnimationFrame`.
