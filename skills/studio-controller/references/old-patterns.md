# Old Patterns & Blacklist

## Deprecated Heuristics
- Reporting without reconciliation controls.
  - Reason: unreliable executive decision signals.
  - New Protocol: mandatory revenue-expense reconciliation before finalization.

## Known Failure Modes
- Missing ledger inserts in `lsl_finance` after report generation.
  - Resolution: fail-fast if `lsl_finance_logged` is false.
