# Example Trace: Error Recovery

## Scenario
One source feed omits timestamp fields.

## Recovery
- Skill fails fast at canonical validation.
- Writes `PENDING_APPROVAL` with missing-field diagnostics.
- Resumes after corrected source payload is provided.
