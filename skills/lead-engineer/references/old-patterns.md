# Old Patterns & Blacklist

## Deprecated Heuristics
- Single-lane decomposition for multi-domain PRDs.
  - Reason: creates hidden coupling and missed acceptance checks.
  - Replacement: packetized routing with explicit lane ownership.

## Known Failure Modes
- Spawning workers before route validation.
  - Resolution: fail-fast at Decision Tree step 2.
- Missing rollback criteria in packets.
  - Resolution: require rollback field in output plan.
