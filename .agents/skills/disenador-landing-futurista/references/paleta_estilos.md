# Paleta de Colores, Gradientes y Efectos de Iluminación

Esta guía técnica define los tokens de diseño, gradientes CSS, animaciones de cielo nocturno y efectos de resplandor neón para la estética futurista oscura en Tailwind CSS y Next.js.

---

## 1. Paleta Cromática Central

| Rol | Código Hex | Variable / Clase Tailwind | Uso |
| :--- | :--- | :--- | :--- |
| **Fondo Profundo** | `#030014` / `#050515` | `bg-[#030014]` o `bg-slate-950` | Lienzo espacial nocturno |
| **Púrpura Neón Principal** | `#A855F7` / `#C084FC` | `text-purple-400` / `bg-purple-600` | Botones primarios, brillos, texto destacado |
| **Fucsia Eléctrico** | `#E879F9` / `#D946EF` | `text-fuchsia-400` / `via-fuchsia-500` | Punto medio de degradados de texto y arcos |
| **Azul Profundo / Índigo** | `#3B82F6` / `#1E1B4B` | `text-indigo-400` / `to-indigo-600` | Base del arco de luz y sombras ambientales |
| **Texto Principal** | `#F8FAFC` | `text-white` / `text-slate-100` | Encabezados y títulos principales |
| **Texto Secundario** | `#94A3B8` | `text-slate-400` / `text-zinc-400` | Subtítulos y párrafos descriptivos |
| **Logos e Iconos** | `#FFFFFF` (opacidad 70-90%) | `text-white/80` / `opacity-80` | Logotipos de partners y símbolos |

---

## 2. Definición del Gran Arco de Luz Degradada

El arco de luz enmarca la parte superior y central del Hero, generando profundidad atmosférica.

```css
/* Utilidad CSS para el resplandor ambiental */
.glow-arc-gradient {
  background: radial-gradient(
    ellipse 80% 50% at 50% -20%,
    rgba(168, 85, 247, 0.45),
    rgba(99, 102, 241, 0.25) 45%,
    rgba(3, 0, 20, 0) 80%
  );
}

/* Efecto de arco de luz nítido */
.arc-border-light {
  background: linear-gradient(
    90deg,
    rgba(168, 85, 247, 0) 0%,
    rgba(192, 132, 252, 0.8) 50%,
    rgba(99, 102, 241, 0) 100%
  );
}
```

---

## 3. Fondo de Cielo Espacial Estrellado (*Starfield*)

Para lograr un cielo nocturno vivo con estrellas brillantes sin cargar librerías pesadas:

```css
/* Animación de titileo sutil */
@keyframes twinkle {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.1); }
}

.star {
  position: absolute;
  background-color: white;
  border-radius: 9999px;
  animation: twinkle 3s infinite ease-in-out;
}
```

---

## 4. Efectos de Botones e Interacciones

### Botón Primario (Púrpura Neón Relleno):
```html
<button class="relative px-7 py-3 rounded-full font-medium text-white bg-gradient-to-r from-purple-600 via-fuchsia-500 to-indigo-600 shadow-[0_0_25px_rgba(168,85,247,0.5)] hover:shadow-[0_0_35px_rgba(168,85,247,0.75)] hover:scale-[1.02] active:scale-[0.98] transition-all duration-300">
  Comenzar Ahora
</button>
```

### Botón Secundario (Contorno / Outlined con Glassmorphism):
```html
<button class="px-7 py-3 rounded-full font-medium text-slate-200 border border-purple-500/30 bg-purple-950/20 backdrop-blur-md hover:bg-purple-900/30 hover:border-purple-400/60 hover:text-white transition-all duration-300">
  Ver Demostración
</button>
```
