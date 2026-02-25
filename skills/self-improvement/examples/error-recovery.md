# Error Recovery Pattern

Scenario: agent proposes upgrade without sufficient evidence.

1. Agent fails evidence sufficiency gate.
2. Agent checkpoints `PENDING_APPROVAL` and requests missing execution data.
3. After additional data, agent recalculates trend confidence.
4. Agent updates `references/old-patterns.md` with "speculative proposal" anti-pattern.
