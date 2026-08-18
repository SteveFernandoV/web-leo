# Directrices y Heurísticas de UX (99 UX Guidelines)

Estándares de diseño de interacción, accesibilidad, formularios y micro-animaciones.

---

## 1. Reglas Fundamentales de Usabilidad (Heurísticas Clave)

1. **Visibilidad del Estado del Sistema:** Todo botón o acción asíncrona debe reflejar de inmediato su estado (`loading`, `disabled`, `success`, `error`).
2. **Prevención de Errores en Formularios:**
   - Validación inline en tiempo real tras desenfocar el campo (*on blur*), nunca bloqueando antes de escribir.
   - Mensajes de error específicos indicando exactamente cómo solucionar el problema.
3. **Áreas Táctiles en Móviles (Tap Targets):** Todo elemento clickeable en pantallas táctiles debe medir como mínimo **44x44 px** (o `48x48 dp` en Android).
4. **Jerarquía Visual y Escaneabilidad:**
   - Un solo `<h1>` por página.
   - Proporción de contraste cromático mínima de **4.5:1** para texto normal y **3:1** para texto grande (WCAG 2.1 AA).
   - Uso consistente de espaciados modulares en múltiplos de 4 u 8 px (`gap-2`, `gap-4`, `p-6`).

---

## 2. Micro-Interacciones y Estados de Componentes

- **Botones:** Incluir transiciones suaves (`transition-all duration-200 ease-out`), estados `:hover` con elevación o resplandor sutil, y estado `:active` con escala reducida (`scale-[0.98]`).
- **Cards:** Efecto de borde o iluminación perimetral en hover para denotar interactividad.
- **Skeletons & Shimmers:** Usar marcadores de posición animados durante la carga en lugar de spinners genéricos para reducir la percepción del tiempo de espera.
