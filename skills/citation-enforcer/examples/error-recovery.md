# Error Recovery Pattern

Scenario: two claims were cited from a stale summary file.

1. Agent detects missing base evidence pointers.
2. Agent re-queries source records and refreshes citations.
3. Agent downgrades confidence for one claim and flags for review.
4. Agent logs stale-summary anti-pattern in `references/old-patterns.md`.
