# Example Trace: Error Recovery

## Scenario
`factory.json` exists but one required lane is missing.

## Recovery
- Phase 1 fails fast at routing check.
- Skill writes a blocked checkpoint in `state.jsonl` and marks packet as unresolved.
- Operator receives a minimal remediation request: add lane mapping or approve fallback owner.
- After update, run resumes from Phase 2 without redoing ingestion.
