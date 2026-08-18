---
name: disenador-landing-futurista
description: >-
  Diseña y construye landing pages modernas, responsivas y vanguardistas en Next.js y Tailwind CSS con estética futurista oscura, fondos espaciales con estrellas, arcos de luz degradada en púrpura neón y azul profundo, cabeceras con isotipo de red, sección Hero con títulos en degradado y franjas de logotipos asociados en blanco.
---

# Diseñador de Landing Pages Futuristas (Next.js & Tailwind CSS)

Esta habilidad dota al agente con la experiencia de un diseñador y desarrollador frontend sénior especializado en crear páginas de aterrizaje (*landing pages*) oscuras, inmersivas y ultra-pulidas en **Next.js** y **Tailwind CSS**.

El resultado final combina una dirección de arte vanguardista y espacial con código limpio, modular y 100% responsivo, evitando clichés genéricos para ofrecer una apariencia a medida de máxima calidad.

---

## 1. Documentación de Referencia y Recursos

Consulta los siguientes documentos antes y durante la implementación:

- 🎨 **[Paleta de Colores y Efectos de Iluminación](./references/paleta_estilos.md)**: Tokens cromáticos, sombras de resplandor neón (`#A855F7`, `#3B82F6`), gradientes y estilos de estrellas titilantes.
- 🧩 **[Plantillas de Componentes Next.js + Tailwind](./resources/componentes_tailwind.md)**: Código modular y TypeScript para `<Navbar />`, `<BackgroundSky />`, `<HeroSection />` y `<PartnerLogos />`.

---

## 2. Elementos Clave del Diseño

Toda landing page construida bajo esta habilidad debe incorporar armoniosamente los siguientes 5 pilares visuales:

1. **Fondo de Cielo Espacial Nocturno:**
   - Base oscura profunda (`#030014` / `bg-slate-950`).
   - Campo estelar con partículas de estrellas brillantes distribuidas con opacidad variable y sutil animación de titileo (`twinkle`).
2. **Gran Arco de Luz Degradada:**
   - Un amplio arco lumínico elíptico en tonos púrpura neón (`#A855F7`) y azul profundo / índigo (`#1E1B4B`) que enmarca la parte superior y corona la sección principal.
   - Resplandor atmosférico con efecto `blur-3xl` y línea de horizonte con luz concentrada.
3. **Cabecera Superior Fija (Navbar):**
   - **Izquierda:** Logotipo tipográfico moderno acompañado de un icono de red geométrica (`NetworkIcon` SVG).
   - **Centro:** Navegación minimalista en cápsula de cristal (*glassmorphism*) con enlaces a secciones.
   - **Derecha:** Botón de acción destacado con degradado púrpura-fucsia y micro-animación de escala en hover.
4. **Área Principal (Hero Section):**
   - Título monumental de alto impacto con efecto degradado (*gradient text clip*) de púrpura neón a fucsia y azul.
   - Párrafo descriptivo en tipografía clara y legible (`text-slate-300`).
   - Dos botones de acción:
     - **Botón Primario:** Relleno en degradado púrpura neón con sombra de resplandor (*glow shadow*).
     - **Botón Secundario:** Estilo contorno (*outlined*) con borde translúcido y fondo de cristal (*backdrop-blur*).
5. **Franja de Logotipos Asociados (Social Proof):**
   - Fila de logotipos empresariales y marcas asociadas presentados en blanco monocromático con opacidad equilibrada sobre el fondo oscuro.

---

## 3. Flujo de Trabajo para la Construcción

Cuando se active esta habilidad para crear una landing page, sigue este protocolo:

### Paso 1: Configuración del Lienzo y Tokens de Estilo
1. Configura el fondo base `#030014` en el contenedor principal de la página (`app/page.tsx` o `src/pages/index.tsx`).
2. Importa y aplica la tipografía adecuada (ej. *Inter*, *Outfit* o *Geist Sans* a través de `next/font/google`).

### Paso 2: Implementación de la Atmósfera y Arco de Luz
1. Monta el componente de fondo espacial `<BackgroundSky />` en una capa absoluta (`pointer-events-none -z-10`).
2. Aplica el arco elíptico degradado en la parte superior para crear la ilusión de profundidad y horizonte galáctico.

### Paso 3: Construcción de la Cabecera de Navegación
1. Implementa el `<Navbar />` con soporte de `backdrop-blur-xl` para que se integre elegantemente con el fondo al hacer scroll.
2. Añade el isotipo de red SVG interactivo junto al nombre de la marca.

### Paso 4: Ensamblaje del Hero Section
1. Diseña el encabezado principal garantizando un tamaño tipográfico responsivo (`text-5xl md:text-7xl lg:text-8xl`).
2. Configura los dos botones de llamada a la acción con estados `:hover` y `:active` optimizados.

### Paso 5: Integración de la Fila de Logotipos
1. Ubica la sección de marcas asociadas inmediatamente debajo del Hero.
2. Asegura que los logos usen tonos blancos monocromáticos (`text-white/80` o `fill-white`) con distribución flexible (`flex-wrap`).

---

## 4. Reglas de Excelencia Visual (Anti-Patrones de IA)

Para asegurar que el diseño no parezca una plantilla genérica:

- ❌ **Evitar contrastes pobres:** El texto secundario nunca debe descender de una opacidad legible contra el fondo oscuro.
- ❌ **Evitar bordes toscos:** Utiliza bordes translúcidos con opacidades sutiles (`border-purple-500/20` o `border-white/10`).
- ❌ **Evitar saturación excesiva:** Equilibra los resplandores neón focalizados con amplias áreas de descanso visual en negro espacial.
- ✅ **Micro-interacciones Fluidas:** Aplica transiciones suaves (`transition-all duration-300`, `ease-out`) en botones y enlaces.
- ✅ **Responsividad Perfecta:** Verifica la adaptación fluida en pantallas móviles (375px), tablets (768px) y escritorios amplios (1440px+).
