# Example Trace: Error Recovery

## Scenario
n8n trigger payload fails schema validation.

## Recovery
- Skill halts before trigger execution.
- Marks `PENDING_APPROVAL` with payload correction notes.
- Resumes after schema-compliant payload update.
