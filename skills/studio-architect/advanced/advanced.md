# Advanced Execution Logic

## Template Selection Matrix
- SaaS Starter Kit priority:
  - Multi-tenant product, auth-heavy workflows, billing/admin requirements.
- Website Template priority:
  - Marketing-first delivery, lower backend complexity, content-driven roadmap.

## Delta-Only Rule
- After selecting baseline, every custom feature must be represented as an explicit delta.
- Reject requests that ask for full custom builds without baseline evaluation.

## Escalations
- If both templates score below threshold, pause and request operator clarification.
