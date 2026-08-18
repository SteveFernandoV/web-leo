# Next.js SaaS Starter Template

## Stack
- **Framework:** Next.js (App Router) + TypeScript
- **Auth:** Clerk / Supabase Auth
- **Billing & Subscriptions:** Stripe Checkout + Webhooks
- **Database:** PostgreSQL (Neon / Supabase) + Drizzle ORM
- **UI:** Tailwind CSS + Radix UI

## Architecture Highlights
- Protected route groups: `(dashboard)` layout with subscription guard.
- Stripe webhook endpoint: `app/api/webhooks/stripe/route.ts` with signature verification.
- Customer billing portal integration.
