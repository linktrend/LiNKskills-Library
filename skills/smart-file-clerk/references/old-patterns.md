# Old Patterns & Blacklist

## Deprecated Heuristics
- Storing all docs in one tier regardless of retrieval profile.
  - Reason: cost/performance and retrieval quality issues.
  - New Protocol: hybrid Supabase + GDrive routing.

## Known Failure Modes
- Missing OCR for legal/financial docs in active storage.
  - Resolution: fail-fast until OCR completion status is true.
