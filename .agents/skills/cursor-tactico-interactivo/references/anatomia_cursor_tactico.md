# Anatomía y Especificaciones Técnicas de la Retícula Táctica

Este documento detalla los parámetros de diseño, proporciones geométricas y modelos de color para la retícula táctica interactiva.

---

## 1. Esquema Visual de la Retícula

```text
               │ (Eje Vertical Superior: 8px)
               │
          ┌────┴────┐
       ───┤         ├─── (Eje Horizontal: 8px)
          │    ●    │   (Punto Central: 6px)
       ───┤         ├───
          └────┬────┘
               │
               │ (Eje Vertical Inferior: 8px)
          
          [ INSIGNIA HUD ] (Telemetría flotante)
```

---

## 2. Paleta Cromática Neón Táctica

| Parámetro | Token / Variable | Hexadecimal | RGB / Alpha | Rol |
|---|---|---|---|---|
| **Cyan Primario** | `--neon-cyan` | `#00E5FF` | `rgba(0, 229, 255, 1)` | Anillo exterior en reposo, miras y telemetría |
| **Magenta Reactivo** | `--neon-pink` | `#FF007F` | `rgba(255, 0, 127, 1)` | Punto central en reposo / Anillo exterior en hover |
| **Resplandor Glow** | `--glow-cyan` | `#00E5FF` | `rgba(0, 229, 255, 0.35)` | Halo perimetral y sombras de neón |
| **Fondo HUD Badge** | `--bg-hud` | `#03060C` | `rgba(3, 6, 12, 0.94)` | Fondo de alta opacidad para la etiqueta de texto |
| **Flash Activo** | `--flash-white` | `#FFFFFF` | `rgba(255, 255, 255, 0.9)` | Pulso lumínico al hacer clic / disparar |

---

## 3. Dimensiones y Geometría sin Subpíxeles

Para evitar que el motor de renderizado de los navegadores (Blink, WebKit, Gecko) aplique antialiasing borroso al centrar elementos con `translate(-50%, -50%)`, **todas las medidas deben ser números pares**:

1. **Anillo Principal (`#tacticalCursor`):**
   - Diámetro: `36px` x `36px` (o `38px`).
   - Grosor de borde: `1.5px` sólido.
   - Radio de borde: `50%` (círculo perfecto).
   - Box-sizing: `border-box`.

2. **Ejes de la Cruz Ortogonal (`::before` y `::after`):**
   - Eje horizontal (`::before`): Ancho `8px`, alto `2px`.
   - Eje vertical (`::after`): Ancho `2px`, alto `8px`.
   - Proyección opuesta: Utiliza `box-shadow: 30px 0 0 var(--neon-cyan)` para crear el eje opuesto sin generar elementos DOM adicionales.

3. **Punto de Mira Central (`#tacticalCursorDot`):**
   - Diámetro: `6px` x `6px` (par).
   - Radio de borde: `50%`.
   - Sombra: `box-shadow: 0 0 8px var(--neon-pink)`.

4. **Etiqueta HUD (`#tacticalCursorBadge`):**
   - Tipografía: Monospace o fuente táctica condensada (ej. `Rajdhani`, `Orbitron`, `Inter`).
   - Tamaño de fuente: `9px` con `letter-spacing: 0.14em` y `font-weight: 800`.
   - Posicionamiento: `top: 100%`, `transform: translateX(-50%) translateY(8px)`.

---

## 4. Transformaciones y Fórmulas Matemáticas

- **Traslación de hardware:**
  ```javascript
  // Siempre traslada en coordenadas de píxeles enteros utilizando translate3d
  cursor.style.transform = `translate3d(${clientX}px, ${clientY}px, 0) translate(-50%, -50%) scale(${scale})`;
  ```

- **Escalado por estados:**
  - Reposo: `scale(1.0)`
  - Hover en botón/link: `scale(1.25)`
  - Clic presionado: `scale(0.82)`
  - Campo de texto: `scale(1.0)` con morfología a corchete rectangular.
