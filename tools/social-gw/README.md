# social-gw

## Capability Summary
Unified social wrapper that routes post and comment retrieval actions across YouTube, TikTok, and X through the `gw` tool, returning deterministic JSON payloads.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/social-gw post --provider youtube --target-id <comment_id> --text "Thanks for your feedback" --json`
- `bin/social-gw fetch-comments --provider youtube --target-id <video_id> --json`
- `bin/social-gw post --provider x --target-id <thread_id> --text "Launch update" --json`

## Notes
- YouTube operations map to `gw youtube` comment commands.
- TikTok/X operations are passed through to `gw social ...` provider routes.
