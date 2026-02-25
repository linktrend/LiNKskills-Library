# Example Trace: Error Recovery

## Scenario
One required `PROGRESS.md` file is missing from the QA stream.

## Recovery
- Skill fails fast and marks `PENDING_APPROVAL`.
- Requests missing report before issuing directives.
- Resumes after report is provided and finalizes coordination output.
