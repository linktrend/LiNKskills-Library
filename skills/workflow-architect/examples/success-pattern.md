# Success Pattern

1. User requests a lead-routing workflow.
2. Agent writes normalized workflow JSON to task-local artifact.
3. Agent creates workflow via `/tools/n8n/bin/n8n create`.
4. Agent activates and triggers with test payload.
5. Agent logs completion in ledger and updates trace.
