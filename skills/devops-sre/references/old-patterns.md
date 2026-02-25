# Old Patterns & Blacklist

## Deprecated Heuristics
- Deploying without explicit rollback path.
  - Reason: high recovery risk during incident.
  - Replacement: mandatory rollback section in output contract.

## Known Failure Modes
- Missing `LSL_MASTER_KEY` in production runtime.
  - Resolution: fail-fast and block release until key injection is verified.
