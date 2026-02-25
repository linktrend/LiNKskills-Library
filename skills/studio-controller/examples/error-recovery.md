# Example Trace: Error Recovery

## Scenario
Expense feed contains unmatched records outside expected window.

## Recovery
- Skill marks mismatch and sets `PENDING_APPROVAL`.
- Generates variance table and requested data corrections.
- Resumes close only after corrected inputs are confirmed.
