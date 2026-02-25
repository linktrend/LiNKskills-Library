# memory

## Capability Summary
Supabase-backed long-term memory tool with strict agent and project isolation. Use to remember and recall notes while keeping Lisa/Bob memories separated by `agent_id` in the same Supabase project.

## Commands
- `remember`
  - Store one memory payload for an `agent_id` and `project_id`.
- `recall`
  - Retrieve memory rows for an `agent_id` and `project_id`, optionally filtered by query.
- `add-note`
  - Store a Markdown note into `lsl_memory.notes` (`agent_id`, `title`, `md_content`).
- `get-note`
  - Retrieve Markdown notes for an `agent_id` with optional id/title filters.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/memory remember --agent-id lisa --project-id growth --content "Launch postmortem: CTA underperformed."`
- `bin/memory recall --agent-id lisa --project-id growth --query "postmortem" --limit 10`
- `bin/memory add-note --agent-id lisa --title "Standup" --md-file ./standup.md`
- `bin/memory get-note --agent-id lisa --title "Standup" --limit 10`

## Vault Keys
- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY`

## Notes Table
- `lsl_memory.notes`
- Columns: `id`, `agent_id`, `title`, `md_content`, `created_at`
- `md_content` is stored as Markdown text.
