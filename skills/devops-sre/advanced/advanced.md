# Advanced Execution Logic

## Rollout Patterns
- Blue/Green deployment preferred when zero-downtime is required.
- Rolling deployment allowed when service tolerates gradual replacement.

## Security Hardening
- Validate `LSL_MASTER_KEY` exists in deployment environment before release gate clears.
- Disallow plaintext secret storage in repository files.

## Recovery
- If health checks fail post-deploy, auto-select rollback plan and halt further rollout.
