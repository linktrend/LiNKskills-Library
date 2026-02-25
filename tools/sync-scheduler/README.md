# sync-scheduler

## Capability Summary
Calendar assistant wrapper that uses `gw` calendar operations to find and suggest Project Review slots with deterministic JSON output for agent workflows.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/sync-scheduler suggest --date 2026-02-25 --duration-minutes 45 --count 3 --json`
- `bin/sync-scheduler suggest --date 2026-02-25 --start-hour 9 --end-hour 18 --json`

## Notes
- Uses `gw` as the primary calendar interface.
- If `gw` event retrieval fails, returns a deterministic JSON error payload.
