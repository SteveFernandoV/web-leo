# Next.js Full-Stack Starter Template

## Stack
- **Framework:** Next.js 15 (App Router)
- **Database:** PostgreSQL + Prisma ORM
- **Styling:** Tailwind CSS + Shadcn UI
- **Authentication:** Auth.js (NextAuth v5)

## Quick Start
1. Initialize: `npx -y create-next-app@latest ./ --typescript --tailwind --eslint --app`
2. Install Prisma: `npm install @prisma/client && npm install -D prisma`
3. Initialize schema: `npx prisma init`
4. Run migrations: `npx prisma migrate dev --name init`
5. Dev server: `npm run dev`
