# Error Recovery Pattern

Scenario: critique detects factual contradiction that cannot be resolved from current context.

1. Agent marks issue as high severity.
2. Agent checkpoints `PENDING_APPROVAL` with clarification request.
3. After clarification, agent revises draft and re-checks.
4. Agent logs contradiction pattern in `references/old-patterns.md`.
