# Multi-Agent Coordination & Execution Pipeline

Guidelines for orchestrating specialized sub-tasks when building applications.

---

## 1. Agent Roles & Responsibilities

```text
┌─────────────────────────────────────────────────────────────┐
│                 App Builder (Orchestrator)                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│ProjectPlanner│        │DatabaseArch. │        │DevOpsEngineer│
│Task Graph    │        │Schema/Migrate│        │Deploy/Preview│
└──────┬───────┘        └──────┬───────┘        └──────────────┘
       │                       │
       ▼                       ▼
┌──────────────┐        ┌──────────────┐
│FrontendSpec. │◄──────►│BackendSpec.  │
│UI/Components │        │API/Services  │
└──────────────┘        └──────────────┘
```

1. **`project-planner`**: Analyzes user prompt, decomposes into dependency graphs, outlines milestone steps.
2. **`database-architect`**: Defines entities, relations, indices, schema files (`schema.prisma`, SQL migrations).
3. **`backend-specialist`**: Implements API endpoints, data validation, business logic, auth middleware.
4. **`frontend-specialist`**: Implements pages, responsive layouts, client state, forms, UI feedback.
5. **`devops-engineer`**: Configures Docker, CI/CD workflows, environment variables, preview servers.

---

## 2. Standard Orchestration Order

1. **Phase 1: Architecture & Planning:** Determine archetype, tech stack, and create project directory layout.
2. **Phase 2: Data Modeling:** Generate schema, models, and type definitions first (data contract).
3. **Phase 3: Backend & API Implementation:** Build core business logic and REST/GraphQL/Server Action handlers.
4. **Phase 4: Frontend & UI Assembly:** Build UI components consuming the data contract with rich aesthetics.
5. **Phase 5: Integration & Verification:** Run unit/integration tests, verify dev server launch, and check responsive layouts.
