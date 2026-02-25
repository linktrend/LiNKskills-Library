# Error Recovery Pattern

1. Create call succeeds but activation fails.
2. Agent reads workflow details to identify invalid nodes.
3. Agent patches JSON and re-runs create/activate on replacement workflow.
4. Agent records failure mode in `references/old-patterns.md`.
5. Agent emits actionable remediation summary with next-step command.
