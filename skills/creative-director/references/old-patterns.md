# Old Patterns & Blacklist

## Deprecated Heuristics
- Triggering rendering before asset spec definition.
  - Reason: inconsistent outputs and rework loops.
  - New Protocol: schema-validated asset orders first.

## Known Failure Modes
- Missing trigger metadata (workflow id/payload).
  - Resolution: fail-fast before Phase 4 execution.
