# asset-filer

## Capability Summary
Asset ingestion bridge for creative outputs. Routes `gw asset upload [file]` to Supabase Storage and records metadata in `lsl_memory.assets` for retrieval.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/asset-filer upload ./outputs/thumbnail.png --json`
- `bin/asset-filer upload ./outputs/script.md --asset-type script --project-id launch-q2 --json`

## Notes
- Uses `gw` as the transport layer.
- Expects backend support for asset metadata registration in `lsl_memory.assets`.
