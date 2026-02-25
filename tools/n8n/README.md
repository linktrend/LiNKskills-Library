# n8n

## Capability Summary
n8n workflow API wrapper for reading, creating, activating, and triggering automation workflows from agents.

## Commands
- `read`
  - Read a workflow definition by id.
- `list`
  - List workflows from n8n.
- `create`
  - Create a workflow from JSON.
- `activate` / `deactivate`
  - Toggle workflow active status.
- `trigger`
  - Trigger a workflow run with JSON payload.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/n8n list --limit 20`
- `bin/n8n read --workflow-id 123`
- `bin/n8n create --workflow-json '{"name":"Lead Router","nodes":[],"connections":{}}'`
- `bin/n8n activate --workflow-id 123`
- `bin/n8n trigger --workflow-id 123 --payload-json '{"lead_id":"abc"}'`

## Vault Keys
- `N8N_BASE_URL`
- `N8N_API_KEY`
