# vault

## Capability Summary
Encrypted key/value credential store for LiNKskills. Use to persist sensitive material with `LSL_MASTER_KEY`-protected encryption and retrieve it without committing secrets to the repository.

## Commands
- `set <key> <file_or_string>`
  - Encrypt and store a value from a file path or inline string.
- `get <key>`
  - Decrypt and return a stored value for runtime use.
- `list`
  - Show available key names only.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/vault set google_credentials ./credentials.json`
- `bin/vault get google_credentials`
- `bin/vault list`
