# Old Patterns & Blacklist

## Deprecated Heuristics
- Manual visual review without baseline screenshots.
  - Reason: subjective and inconsistent.
  - Replacement: deterministic Playwright capture plus diff scoring.

## Known Failure Modes
- Ignoring token drift when pixel diff is small.
  - Resolution: always run token-level checks in addition to screenshot diffs.
