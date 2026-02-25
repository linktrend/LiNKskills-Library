# ad-intel

## Capability Summary
Ad performance monitor for Marketing Strategist workflows. Uses the `gw` bridge for ad-related retrieval and tracks Spend vs. CTR to detect anomalies across Meta/Google campaigns.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/ad-intel monitor --input ./campaign_metrics.json --json`
- `bin/ad-intel monitor --spend-threshold-pct 35 --ctr-threshold-pct 20 --json`
- `bin/ad-intel monitor --bridge-command "gw news search 'meta ads benchmark ctr' --json" --json`

## Notes
- Preferred path is using `gw`-sourced metrics.
- Falls back to local input JSON when bridge retrieval is unavailable.
