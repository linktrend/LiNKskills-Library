# Example Trace: Error Recovery

## Scenario
Campaign schedule conflicts with platform blackout window.

## Recovery
- Skill flags conflict and sets `PENDING_APPROVAL`.
- Proposes adjusted schedule and resumes after confirmation.
