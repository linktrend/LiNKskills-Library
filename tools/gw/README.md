# gw

## Capability Summary
Unified gateway for Google Workspace and external services. Use for Gmail (send/list), Drive (upload/share), Docs (formatting/markdown), Sheets (logging), Calendar (scheduling), Chat, and News (search/trending). Includes `vault` for encrypted secret storage and `sandbox` for ephemeral containerized command execution.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/gw gmail send --to user@example.com --subject "Hello" --body "Test message"`
- `bin/gw drive upload --file-path ./report.pdf`
- `bin/gw docs append --document-id <doc_id> --text "# Update" --markdown`
- `bin/gw tasks list --list-id @default`
- `bin/gw youtube stats`
- `bin/gw news search "artificial intelligence regulation"`
- `bin/gw news trending --limit 10`
- `bin/gw vault set gw.credentials.json ./credentials.json`
- `bin/gw vault get gw.credentials.json`
- `bin/gw sandbox run "python3 -V"`
