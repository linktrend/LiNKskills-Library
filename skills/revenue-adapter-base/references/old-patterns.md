# Old Patterns & Blacklist

## Deprecated Heuristics
- Mixing source schemas in final finance payloads.
  - Reason: reconciliation and reporting errors.
  - New Protocol: canonical Venture Studio Transaction normalization.

## Known Failure Modes
- Missing currency or timestamp during mapping.
  - Resolution: fail-fast if required canonical fields are absent.
