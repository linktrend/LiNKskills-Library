# Advanced: workflow-architect

## High-Risk Patterns
- Multi-branch workflows with conditional loops must include explicit termination guards.
- Webhook triggers must define idempotency keys when retries are enabled.
- Fan-out workflows should include per-branch error handling to avoid full-run collapse.

## Recovery Patterns
- If workflow activation fails due to invalid node configuration, capture validation errors and regenerate only the failed nodes.
- If trigger test fails from missing credentials, halt and request vault key setup instead of embedding secrets.
- If n8n API latency causes partial responses, retry read endpoint before deciding failure.
