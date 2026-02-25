# API Specs Reference

## n8n Wrapper Commands
- `n8n create --workflow-json <json>`
- `n8n activate --workflow-id <id>`
- `n8n trigger --workflow-id <id> --payload-json <json>`
- `n8n read --workflow-id <id>`
- `n8n list --limit <n>`

## Validation Expectations
- Create must return workflow identifier.
- Activate must return active=true confirmation.
- Trigger must return execution metadata or explicit error code.
