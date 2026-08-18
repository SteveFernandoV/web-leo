# Componentes Next.js + Tailwind CSS: Landing Page Futurista

Plantillas de componentes modulares en TypeScript / React listas para usar en proyectos de Next.js (App Router).

---

## 1. Cabecera / Navegación Superior (`Navbar.tsx`)

```tsx
'use client';

import React, { useState } from 'react';
import Link from 'next/link';

export function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 px-6 py-4 bg-[#030014]/70 backdrop-blur-xl border-b border-purple-500/10">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Logotipo tipográfico con icono de red */}
        <Link href="/" className="flex items-center gap-3 group">
          <div className="w-10 h-10 rounded-xl bg-purple-950/60 border border-purple-500/30 flex items-center justify-center shadow-[0_0_15px_rgba(168,85,247,0.3)] group-hover:border-purple-400 group-hover:shadow-[0_0_20px_rgba(168,85,247,0.5)] transition-all">
            {/* Icono de Red / Network SVG */}
            <svg className="w-5 h-5 text-purple-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="3" />
              <circle cx="5" cy="6" r="2" />
              <circle cx="19" cy="6" r="2" />
              <circle cx="5" cy="18" r="2" />
              <circle cx="19" cy="18" r="2" />
              <line x1="7" y1="7" x2="10" y2="10" />
              <line x1="17" y1="7" x2="14" y2="10" />
              <line x1="7" y1="17" x2="10" y2="14" />
              <line x1="17" y1="17" x2="14" y2="14" />
            </svg>
          </div>
          <span className="text-xl font-bold tracking-tight text-white group-hover:text-purple-300 transition-colors">
            NEXUS<span className="text-purple-500">.AI</span>
          </span>
        </Link>

        {/* Navegación Central */}
        <nav className="hidden md:flex items-center gap-8 px-6 py-2 rounded-full bg-white/[0.03] border border-white/[0.08] backdrop-blur-md">
          {['Características', 'Soluciones', 'Ecosistema', 'Precios'].map((item) => (
            <Link key={item} href={`#${item.toLowerCase()}`} className="text-sm text-slate-300 hover:text-white transition-colors">
              {item}
            </Link>
          ))}
        </nav>

        {/* Botón de Acción Destacado a la Derecha */}
        <div className="flex items-center gap-4">
          <Link
            href="/acceso"
            className="px-5 py-2.5 rounded-full text-sm font-semibold text-white bg-gradient-to-r from-purple-600 via-fuchsia-500 to-indigo-600 shadow-[0_0_20px_rgba(168,85,247,0.4)] hover:shadow-[0_0_30px_rgba(168,85,247,0.7)] hover:scale-105 active:scale-95 transition-all"
          >
            Lanzar App
          </Link>
        </div>
      </div>
    </header>
  );
}
```

---

## 2. Gran Arco de Luz y Fondo de Estrellas (`BackgroundSky.tsx`)

```tsx
import React from 'react';

export function BackgroundSky() {
  const stars = Array.from({ length: 45 }, (_, i) => ({
    id: i,
    top: `${Math.random() * 100}%`,
    left: `${Math.random() * 100}%`,
    size: `${Math.random() * 2.5 + 1}px`,
    delay: `${Math.random() * 4}s`,
    opacity: Math.random() * 0.7 + 0.3,
  }));

  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none -z-10">
      {/* Fondo base oscuro */}
      <div className="absolute inset-0 bg-[#030014]" />

      {/* Gran Arco de Luz Degradada Superior */}
      <div className="absolute -top-[250px] left-1/2 -translate-x-1/2 w-[1200px] h-[650px] rounded-[100%] bg-gradient-to-b from-purple-600/40 via-indigo-600/20 to-transparent blur-3xl" />
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[900px] h-[1px] bg-gradient-to-r from-transparent via-purple-400/80 to-transparent shadow-[0_0_40px_rgba(192,132,252,0.8)]" />

      {/* Resplandor secundario azul profundo */}
      <div className="absolute top-1/3 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-indigo-900/15 rounded-full blur-[120px]" />

      {/* Partículas de Estrellas */}
      {stars.map((star) => (
        <div
          key={star.id}
          className="absolute rounded-full bg-white animate-pulse"
          style={{
            top: star.top,
            left: star.left,
            width: star.size,
            height: star.size,
            animationDuration: `${star.delay}`,
            opacity: star.opacity,
          }}
        />
      ))}
    </div>
  );
}
```

---

## 3. Área Principal / Hero Section (`HeroSection.tsx`)

```tsx
import React from 'react';
import Link from 'next/link';

export function HeroSection() {
  return (
    <section className="relative pt-40 pb-20 px-6 max-w-5xl mx-auto text-center flex flex-col items-center">
      {/* Badge Superior */}
      <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-950/40 border border-purple-500/30 text-purple-300 text-xs font-semibold tracking-wide uppercase mb-8 shadow-[0_0_15px_rgba(168,85,247,0.2)]">
        <span className="w-2 h-2 rounded-full bg-purple-400 animate-ping" />
        Nueva Generación de Inteligencia Digital
      </div>

      {/* Título Principal en Degradado Púrpura */}
      <h1 className="text-5xl md:text-7xl lg:text-8xl font-extrabold tracking-tight text-white leading-[1.1] mb-8">
        El Futuro Conectado en{' '}
        <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-fuchsia-300 to-indigo-400 drop-shadow-[0_0_35px_rgba(168,85,247,0.4)]">
          Una Sola Red
        </span>
      </h1>

      {/* Párrafo Descriptivo */}
      <p className="text-lg md:text-xl text-slate-300/90 max-w-2xl mx-auto mb-10 leading-relaxed font-light">
        Despliega infraestructura descentralizada, orquesta agentes autónomos y escala tus operaciones con la plataforma impulsada por la red neuronal más avanzada.
      </p>

      {/* Botones de Acción Dual */}
      <div className="flex flex-col sm:flex-row items-center gap-4 w-full sm:w-auto">
        {/* Botón Relleno Púrpura Neón */}
        <Link
          href="/comenzar"
          className="w-full sm:w-auto px-8 py-4 rounded-full font-semibold text-white bg-gradient-to-r from-purple-600 via-fuchsia-500 to-indigo-600 shadow-[0_0_30px_rgba(168,85,247,0.5)] hover:shadow-[0_0_45px_rgba(168,85,247,0.8)] hover:scale-105 active:scale-95 transition-all text-base"
        >
          Comenzar Ahora Gratis
        </Link>

        {/* Botón con Contorno / Glassmorphism */}
        <Link
          href="/demo"
          className="w-full sm:w-auto px-8 py-4 rounded-full font-semibold text-slate-200 border border-purple-400/30 bg-purple-950/20 backdrop-blur-md hover:bg-purple-900/30 hover:border-purple-400 hover:text-white transition-all text-base"
        >
          Explorar Documentación
        </Link>
      </div>
    </section>
  );
}
```

---

## 4. Fila de Logotipos Asociados (`PartnerLogos.tsx`)

```tsx
import React from 'react';

const partners = [
  { name: 'HyperScale', label: 'HYPERSCALE' },
  { name: 'NovaCore', label: 'NOVA.CORE' },
  { name: 'VortexAI', label: 'VORTEX' },
  { name: 'AetherFlow', label: 'AETHER' },
  { name: 'OmniGrid', label: 'OMNIGRID' },
];

export function PartnerLogos() {
  return (
    <section className="py-16 px-6 border-t border-purple-500/10 bg-gradient-to-b from-transparent to-purple-950/10">
      <div className="max-w-7xl mx-auto text-center">
        <p className="text-xs uppercase tracking-widest text-slate-400 font-semibold mb-8">
          Con la confianza de los líderes en tecnología espacial y computación cuántica
        </p>

        {/* Fila de logos en blanco monocromático */}
        <div className="flex flex-wrap items-center justify-center gap-10 md:gap-16 opacity-70 hover:opacity-100 transition-opacity">
          {partners.map((partner) => (
            <div key={partner.name} className="flex items-center gap-2 text-white/90 hover:text-white transition-colors cursor-default">
              <div className="w-7 h-7 rounded-lg border border-white/20 flex items-center justify-center bg-white/5">
                <div className="w-2.5 h-2.5 rounded-sm bg-white" />
              </div>
              <span className="text-lg font-bold tracking-widest">{partner.label}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```
