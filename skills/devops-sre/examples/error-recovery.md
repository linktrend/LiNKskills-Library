# Example Trace: Error Recovery

## Scenario
Production environment lacks `LSL_MASTER_KEY` injection.

## Recovery
- Skill fails fast and records `PENDING_APPROVAL` state.
- Provides exact remediation steps for secure key injection.
- Resumes after operator confirms secure environment update.
