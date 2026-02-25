# Example Trace: Error Recovery

## Scenario
Operator asks for custom development before template selection.

## Recovery
- Skill triggers fail-fast in Decision Tree step 2.
- Writes `PENDING_APPROVAL` state with required baseline options.
- Resumes after operator confirms template choice.
