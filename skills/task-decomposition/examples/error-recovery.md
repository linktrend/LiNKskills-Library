# Error Recovery Pattern

Scenario: decomposition merged two unrelated concerns into one task.

1. Agent detects overloaded task with multiple outputs.
2. Agent refactors into two atomic tasks and updates dependencies.
3. Agent rewrites acceptance criteria per new task.
4. Agent logs anti-pattern to `references/old-patterns.md`.
