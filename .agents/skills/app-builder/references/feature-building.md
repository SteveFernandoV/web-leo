# Feature Building & Incremental Enhancement

Workflow for adding new features or refactoring existing codebases.

---

## 1. Feature Analysis Process

When modifying or expanding an existing project:

1. **Context Discovery:** Read existing `package.json`, project layout, and ORM schemas before modifying anything.
2. **Impact Assessment:**
   - Database schema changes needed? (Create migration / model updates)
   - API endpoints required? (Design contract and route handlers)
   - UI views / components? (Design responsive layouts, loading states, error states)
3. **Incremental Implementation:**
   - Update database model and run migration.
   - Build API handler or Server Action with validation.
   - Wire UI component to API endpoint with optimistic updates and error toasts.

---

## 2. Error Handling & Defensive Patterns

- **Input Validation:** Always validate incoming payloads at API boundaries using Zod (TypeScript) or Pydantic (Python).
- **Graceful UI Errors:** Show friendly error toasts, empty states, and fallback illustrations instead of unhandled crashes.
- **Transactional Safety:** Wrap multi-step database mutations inside database transactions.
