# Project Scaffolding & Directory Architecture

Standard directory structures and configuration conventions for generated projects.

---

## 1. Next.js Full-Stack Application Layout

```text
my-app/
├── app/
│   ├── layout.tsx             # Root layout with providers & fonts
│   ├── page.tsx               # Landing / Home page
│   ├── (auth)/                # Route group for sign-in / sign-up
│   ├── (dashboard)/           # Protected dashboard layout & routes
│   └── api/                   # API Route handlers
├── components/
│   ├── ui/                    # Reusable atom components (buttons, inputs, dialogs)
│   ├── forms/                 # Form components with validation
│   └── layout/                # Navbar, Footer, Sidebar
├── lib/
│   ├── db.ts                  # Database client singleton (Prisma / Drizzle)
│   ├── utils.ts               # cn() and helper functions
│   └── auth.ts                # Authentication helpers
├── prisma/
│   └── schema.prisma          # Database schema definition
├── types/
│   └── index.ts               # Shared TypeScript interfaces
├── .env.example               # Environment variables template
├── package.json
└── tailwind.config.ts
```

---

## 2. Python FastAPI Architecture Layout

```text
fastapi-app/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/     # Route handlers per domain
│   │       └── router.py      # Main v1 APIRouter aggregator
│   ├── core/
│   │   ├── config.py          # Pydantic Settings & environment variables
│   │   └── security.py        # Password hashing & JWT tokens
│   ├── db/
│   │   ├── session.py         # Async database engine & session factory
│   │   └── base.py            # Base declarative model
│   ├── models/                # SQLAlchemy database models
│   ├── schemas/               # Pydantic request/response schemas
│   ├── services/              # Business logic & external API clients
│   └── main.py                # FastAPI app initialization & middlewares
├── tests/
├── .env.example
├── pyproject.toml
└── Dockerfile
```
