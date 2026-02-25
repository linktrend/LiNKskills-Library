# Advanced Execution Logic

## High-Risk Routing Cases
- Cross-lane dependency cycles:
  - Resolve by assigning a single integration owner and explicit handoff checkpoints.
- Ambiguous route ownership in `factory.json`:
  - Mark unresolved packet as blocked and request operator direction before spawn.

## Decomposition Heuristics
- Keep each packet small enough for one worker session.
- Include clear acceptance criteria and rollback instructions per packet.

## Recovery Rules
- If a route target is missing, fallback to the nearest capability lane and label as provisional.
- If spawn budget is exceeded, reprioritize packets by business impact and defer low-value items.
