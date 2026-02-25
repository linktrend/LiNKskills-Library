# Old Patterns & Blacklist

## Deprecated Heuristics
- Waiting indefinitely on blocked workers.
  - Reason: delivery stalls compound across streams.
  - New Protocol: trigger RCA at blocked-turn threshold.

## Known Failure Modes
- RCA generated without actionable owners.
  - Resolution: require owner + due window for every action.
