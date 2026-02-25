#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT_DIR/bin/sync-scheduler" --version >/dev/null
"$ROOT_DIR/bin/sync-scheduler" suggest --date 2026-02-25 --count 1 --json >/dev/null || true

echo "sync-scheduler smoke test complete"
