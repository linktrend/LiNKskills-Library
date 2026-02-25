# Example Trace: Error Recovery

## Scenario
Backlog draft does not include QA sign-off in DoD.

## Recovery
- Skill fails fast at DoD gate.
- Writes `PENDING_APPROVAL` state with required QA criteria.
- Resumes after DoD correction and finalizes output.
