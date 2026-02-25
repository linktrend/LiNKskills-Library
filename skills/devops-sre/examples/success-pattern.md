# Example Trace: Success Pattern

## Scenario
A service must be dockerized and deployed to VPS with key-managed runtime.

## Trace
- Skill validates runtime needs and container constraints.
- Deployment plan includes health checks and rollback sequence.
- `LSL_MASTER_KEY` injection path is verified before approval.
- Final plan passes contract checks.
