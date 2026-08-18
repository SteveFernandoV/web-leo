# Project Detection & Classification Matrix

This reference maps natural language keywords and user prompts to project archetypes and optimal starting configurations.

---

## 1. Keyword Matrix

| User Keywords / Concepts | Detected Project Archetype | Primary Stack Recommendation | Template |
| :--- | :--- | :--- | :--- |
| "dashboard", "portal", "SaaS", "auth + billing", "subscription" | **SaaS Application** | Next.js (App Router), Prisma/Drizzle, Stripe, Clerk/NextAuth, Tailwind | `templates/nextjs-saas` |
| "full-stack", "CRUD app", "social network", "marketplace", "e-commerce" | **Full-Stack Web App** | Next.js (App Router), Prisma/PostgreSQL, Tailwind CSS, Shadcn UI | `templates/nextjs-fullstack` |
| "landing page", "portfolio", "marketing site", "showcase", "static" | **Modern Landing Page** | Next.js / Astro, Tailwind CSS, Framer Motion | `templates/nextjs-static` |
| "REST API", "backend service", "microservice", "CRUD API", "Express" | **Node.js REST API** | Express.js / Fastify, TypeScript, Prisma, Zod | `templates/express-api` |
| "Python backend", "AI API", "ML model serving", "FastAPI", "Async API" | **Python FastAPI Service** | Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy/Asyncpg | `templates/python-fastapi` |
| "iOS and Android app", "mobile app", "React Native", "Expo" | **Mobile App (React Native)** | React Native, Expo, Zustand, React Navigation | `templates/react-native-app` |
| "Flutter app", "Dart mobile", "multiplatform mobile" | **Mobile App (Flutter)** | Flutter 3.x, Dart, Riverpod / Bloc | `templates/flutter-app` |
| "desktop app", "Electron", "Windows & Mac tool" | **Desktop App** | Electron + React / Vite, TypeScript, Tailwind | `templates/electron-desktop` |
| "Chrome extension", "browser addon", "Manifest V3" | **Browser Extension** | Manifest V3, TypeScript, Vite / Webpack | `templates/chrome-extension` |
| "CLI tool", "command line utility", "terminal app" | **CLI Utility** | Node.js (Commander.js / Inquirer) or Python (Click / Typer) | `templates/cli-tool` |
| "monorepo", "multi-package", "shared components" | **Monorepo System** | Turborepo, pnpm workspaces, Next.js + Shared Packages | `templates/monorepo-turborepo` |
| "Vue app", "Nuxt", "Pinia store" | **Vue Full-Stack App** | Nuxt 3, Vue 3, Pinia, Tailwind CSS | `templates/nuxt-app` |

---

## 2. Project Detection Decision Tree

1. **Platform Target:** Web, Mobile, Desktop, Extension, or Backend only?
2. **State & Persistence:** Is a database required (PostgreSQL / SQLite) or purely client-side?
3. **Authentication & Payments:** Does the user mention accounts, sign-in, Stripe, or subscriptions?
4. **Rendering Strategy:** Static (SSG), Server-Rendered (SSR), or Single Page App (SPA)?
