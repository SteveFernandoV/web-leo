# Componentes Modulares en React Three Fiber (R3F)

Plantillas de componentes listas para producción en Next.js / React con `@react-three/fiber` y `@react-three/drei`.

---

## 1. Escena Base con Loader y Fallback (`SceneCanvas.tsx`)

```tsx
'use client';

import React, { Suspense, useState, useEffect } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Html, useProgress, Environment } from '@react-three/drei';

function CanvasLoader() {
  const { progress } = useProgress();
  return (
    <Html center>
      <div className="flex flex-col items-center justify-center p-4 rounded-xl bg-black/80 backdrop-blur-md border border-white/10 text-white">
        <div className="w-8 h-8 border-2 border-purple-500 border-t-transparent rounded-full animate-spin mb-2" />
        <span className="text-xs font-mono tracking-wider">{progress.toFixed(0)}%</span>
      </div>
    </Html>
  );
}

export function SceneCanvas({ children }: { children: React.ReactNode }) {
  const [isSupported, setIsSupported] = useState(true);

  useEffect(() => {
    try {
      const canvas = document.createElement('canvas');
      const supported = !!(window.WebGLRenderingContext && (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
      setIsSupported(supported);
    } catch {
      setIsSupported(false);
    }
  }, []);

  if (!isSupported) {
    return (
      <div className="w-full h-full flex items-center justify-center bg-[#030014] text-slate-400 text-sm">
        <span>Tu navegador no soporta aceleración 3D WebGL.</span>
      </div>
    );
  }

  return (
    <Canvas
      dpr={[1, 2]}
      camera={{ position: [0, 0, 5], fov: 45 }}
      gl={{ antialias: true, alpha: true, powerPreference: 'high-performance' }}
      className="w-full h-full"
    >
      <ambientLight intensity={0.6} />
      <directionalLight position={[10, 10, 5]} intensity={1} />
      <Environment preset="city" />
      <Suspense fallback={<CanvasLoader />}>
        {children}
      </Suspense>
      <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={0.8} />
    </Canvas>
  );
}
```

---

## 2. Configurador de Producto Interactivo (`ProductConfigurator.tsx`)

```tsx
'use client';

import React, { useState } from 'react';
import { useGLTF } from '@react-three/drei';

interface ConfiguratorProps {
  modelUrl: string;
}

export function ProductModel({ modelUrl, activeColor }: { modelUrl: string; activeColor: string }) {
  const { scene, materials } = useGLTF(modelUrl) as any;

  // Actualizar material reactivamente
  if (materials && materials.MainMaterial) {
    materials.MainMaterial.color.set(activeColor);
  }

  return <primitive object={scene} scale={1.5} />;
}
```
