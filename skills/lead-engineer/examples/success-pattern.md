# Example Trace: Success Pattern

## Scenario
A PRD for onboarding automation must be split across API, UI, and QA lanes.

## Trace
- Input validated with `factory.json` and route definitions.
- Skill classifies run as `Generalist`, calls `get_tool_details`, and caches lane schemas.
- PRD decomposed into six packets with owners and acceptance criteria.
- `sessions_spawn` plan generated with limits and rollback plan.
- Output contract validated and execution logged.
