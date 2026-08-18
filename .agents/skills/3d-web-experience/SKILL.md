---
name: 3d-web-experience
description: Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfolios, immersive websites, and bringing depth to web experiences.
risk: critical
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# 3D Web Experience

Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfolios, immersive websites, and bringing depth to web experiences.

**Role**: 3D Web Experience Architect

You bring the third dimension to the web. You know when 3D enhances and when it's just showing off. You balance visual impact with performance. You make 3D accessible to users who've never touched a 3D app. You create moments of wonder without sacrificing usability.

---

## 1. Documentación de Referencia y Recursos

- ⚡ **[Pipeline de Optimización y Presupuestos 3D](./references/3d_optimization_pipeline.md)**: Compresión Draco con `gltf-transform`, texturas WebP/KTX2 y límites de polígonos (FPS).
- 🔮 **[Recetas de Shaders GLSL](./references/shader_glsl_recipes.md)**: Shaders de resplandor holográfico (Fresnel), partículas y ondas de vértices para WebGL.
- 🧱 **[Plantillas de Componentes React Three Fiber](./resources/componentes_r3f.md)**: Componentes `<SceneCanvas />`, `<ProductConfigurator />` y loaders con `@react-three/drei`.

---

## 2. Capabilities

- Three.js implementation (Vanilla & Modern Modules)
- React Three Fiber (R3F) & `@react-three/drei`
- WebGL & GLSL shader development
- 3D model preparation & Draco compression
- Spline 3D embeds and event bridges
- 3D product configurators with reactive materials
- Scroll-driven 3D camera animations (GSAP ScrollTrigger / R3F ScrollControls)
- Mobile-first 3D performance optimization

---

## 3. Patterns

### 3D Stack Selection Decision Tree

```text
Need quick 3D element / prototype?
└── Yes → Spline
└── No → Continue

Using React / Next.js?
└── Yes → React Three Fiber (R3F)
└── No → Continue

Need max performance / low-level WebGL control?
└── Yes → Three.js vanilla
└── No → Spline or R3F
```

| Tool | Best For | Learning Curve | Control |
| :--- | :--- | :--- | :--- |
| **Spline** | Quick prototypes, visual designers, lightweight embeds | Low | Medium |
| **React Three Fiber** | Next.js/React apps, state-driven 3D, complex interactive scenes | Medium | High |
| **Three.js Vanilla** | Maximum low-level control, canvas libraries, non-React stacks | High | Maximum |
| **Babylon.js** | Complex 3D games, heavy physics, CAD web viewers | High | Maximum |

---

## 4. Code Examples

### Spline Embed (Fastest Start)
```jsx
import Spline from '@splinetool/react-spline';

export default function Scene() {
  return (
    <Spline scene="https://prod.spline.design/xxx/scene.splinecode" />
  );
}
```

### React Three Fiber Scene with Model Loading
```jsx
import React, { Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF, useProgress, Html, Environment } from '@react-three/drei';

function Model({ url }) {
  const { scene } = useGLTF(url);
  return <primitive object={scene} />;
}

function Loader() {
  const { progress } = useProgress();
  return <Html center>{progress.toFixed(0)}%</Html>;
}

export default function Scene() {
  return (
    <Canvas camera={{ position: [0, 2, 5], fov: 45 }} dpr={[1, 1.5]}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} />
      <Environment preset="city" />
      <Suspense fallback={<Loader />}>
        <Model url="/models/product.glb" />
      </Suspense>
      <OrbitControls enableZoom={false} autoRotate />
    </Canvas>
  );
}
```

### Scroll-Driven 3D with R3F ScrollControls
```jsx
import { ScrollControls, useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { useRef } from 'react';

function RotatingModel() {
  const scroll = useScroll();
  const ref = useRef();

  useFrame(() => {
    // Rotar según la posición del scroll
    ref.current.rotation.y = scroll.offset * Math.PI * 2;
  });

  return <mesh ref={ref}>...</mesh>;
}

export default function ScrollScene() {
  return (
    <Canvas>
      <ScrollControls pages={3} damping={0.1}>
        <RotatingModel />
      </ScrollControls>
    </Canvas>
  );
}
```

---

## 5. Validation Checks & Quality Audits

- 🔴 **No 3D Loading Indicator (High Severity):** Always wrap 3D asset loaders inside `<Suspense fallback={<Loader />}>` to avoid jarring blank screens.
- 🟡 **No WebGL Fallback (Medium Severity):** Detect WebGL capability and render a high-quality static preview image if hardware acceleration is unavailable.
- 🟡 **Uncompressed 3D Models (Medium Severity):** Compress all `.glb` assets using `gltf-transform` with Draco geometry compression and WebP textures (target < 3MB).
- 🟡 **OrbitControls Blocking Page Scroll (Medium Severity):** Disable scroll zooming (`enableZoom={false}`) on landing pages to allow normal document scrolling.
- 🟡 **Excessive DPR on Mobile (Medium Severity):** Restrict `dpr={[1, 1.5]}` on mobile devices to maintain 60 FPS and avoid GPU thermal throttling.

---

## 6. Workflows

### A. Product Configurator Workflow
1. Prepare and optimize 3D product model (`gltf-transform`).
2. Set up React Three Fiber canvas with HDR environment lighting.
3. Bind UI color pickers and variant selectors to 3D material properties.
4. Integrate with checkout/cart and add mobile touch controls.
5. Add fallback image for unsupported devices.

### B. Immersive 3D Portfolio Workflow
1. Design 3D scene concept aligned with brand aesthetics.
2. Build scene in Spline or R3F with custom GLSL materials.
3. Sincronize camera and model transformations with GSAP ScrollTrigger.
4. Test frame rates across desktop and mobile devices.
