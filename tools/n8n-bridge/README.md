# n8n-bridge

## Capability Summary
Webhook trigger bridge for local n8n workflows. Uses `gw n8n trigger` and Vault-backed token retrieval for secure workflow execution.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/n8n-bridge trigger --workflow 123 --payload '{"job":"render"}' --json`
- `bin/n8n-bridge trigger --workflow creative-pipeline --payload-file ./payload.json --json`

## Security
- Reads n8n token from Vault key `N8N_API_KEY` via `gw vault get N8N_API_KEY`.
- Never logs raw token content.
