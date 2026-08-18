---
name: uiux-designer
description: "Use this skill when designing UI components, choosing color palettes, implementing responsive layouts, or reviewing code for UX issues. For landing pages, dashboards, e-commerce, SaaS, and mobile apps. Provides 50+ design styles, 97 color palettes, 57 font pairings, and stack-specific guidelines for React, Vue, Next.js, Flutter, SwiftUI, and more."
---

# UIUX Designer - Design Intelligence

Comprehensive design guide for web and mobile applications. Contains 50+ styles, 97 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 12 technology stacks. Searchable database with priority-based recommendations.

---

## 1. Documentación de Referencia y Recursos

- 🎨 **[Catálogo de Estilos de Diseño (50+ Styles)](./references/design_styles_catalog.md)**: Bento Grid, Dark Futurist, Clean SaaS, Neobrutalism, Luxury Minimalist, etc.
- 🌈 **[Paletas de Colores y Tipografías (97 Palettes & 57 Pairings)](./references/color_palettes_typography.md)**: Tokens cromáticos accesibles (WCAG 2.1 AA) y emparejamientos de Google Fonts.
- 📐 **[Heurísticas y Directrices de UX (99 Guidelines)](./references/ux_guidelines_heuristics.md)**: Usabilidad, prevención de errores, tap targets táctiles (44x44px) y micro-interacciones.

---

## 2. Overview

Reference these guidelines when:
- Designing new UI components, landing pages or dashboards
- Choosing harmonious color palettes and typography pairings
- Reviewing code for UX issues, visual balance and accessibility
- Implementing responsive layouts across mobile, tablet and desktop
- Enforcing micro-animations and interactive component states

---

## 3. Protocols & Workflow

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this structured workflow:

### Step 1: Analyze User Requirements
- **Product Type:** SaaS, e-commerce, portfolio, dashboard, landing page, mobile app, etc.
- **Style Keywords:** minimal, dark futurist, bento grid, playful, elegant, clean corporate, etc.
- **Industry:** AI, fintech, healthcare, gaming, education, e-commerce, creative tools.
- **Stack:** Next.js, React, Vue, Flutter, React Native, or default to `html-tailwind`.

### Step 2: Generate Design System (REQUIRED)
Run the search engine to generate a bespoke design system:
```bash
python3 .agents/skills/uiux-designer/scripts/search.py "<keywords>" --design-system -p "Project Name"
```

### Step 3: Supplement with Detailed Searches
Search for specific visual components, color palettes or design patterns:
```bash
python3 .agents/skills/uiux-designer/scripts/search.py "<keyword>" --domain <domain>
```

### Step 4: Apply Stack Guidelines
Retrieve recommendations and optimization rules for your chosen framework:
```bash
python3 .agents/skills/uiux-designer/scripts/search.py "<keyword>" --stack html-tailwind
```
