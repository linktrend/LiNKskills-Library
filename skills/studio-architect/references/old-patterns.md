# Old Patterns & Blacklist

## Deprecated Heuristics
- Starting from scratch without baseline discovery.
  - Reason: produces drift and slower delivery.
  - Replacement: mandatory template-first protocol.

## Known Failure Modes
- Selecting a template without reading `factory.json`.
  - Resolution: block until policy read is confirmed.
