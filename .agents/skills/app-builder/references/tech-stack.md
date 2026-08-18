# Modern Tech Stack Selection Guide

Authoritative technology recommendations and evaluation criteria for modern application building.

---

## 1. Default Stacks (2025/2026 Production Standards)

### Full-Stack Web Applications (Default)
- **Framework:** Next.js (App Router, React 19)
- **Language:** TypeScript
- **Styling:** Tailwind CSS + Shadcn UI / Radix Primitives
- **Database & ORM:** PostgreSQL (Neon / Supabase) with Prisma or Drizzle ORM
- **Authentication:** Clerk / Auth.js (NextAuth v5)
- **State Management:** TanStack Query + Zustand (or Server Actions)

### Backend & APIs
- **Node.js:** Fastify or Express.js with TypeScript & Zod validation
- **Python:** FastAPI with Pydantic v2 & Asyncpg / SQLAlchemy 2.0
- **Documentation:** OpenAPI (Swagger) auto-generation

### Mobile Applications
- **Cross-Platform React:** Expo SDK (Managed Workflow) + React Native + Zustand
- **Cross-Platform Dart:** Flutter 3 + Dart + Flutter Riverpod

---

## 2. Alternatives & When to Pivot

| Requirement | Preferred Option | Alternative & When to Use |
| :--- | :--- | :--- |
| Ultra-lightweight static content | Next.js SSG | **Astro** (zero JS by default, best for content/blogs) |
| High-performance Vue ecosystem | Next.js | **Nuxt 3** (if user explicitly requests Vue 3) |
| Native desktop performance | Electron | **Tauri (Rust + Web)** (smaller binary size & memory footprint) |
| Complex realtime state | WebSockets | **Supabase Realtime / Liveblocks** |
