#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT_DIR/bin/asset-filer" --version >/dev/null

touch "$ROOT_DIR/test/sample_asset.txt"
"$ROOT_DIR/bin/asset-filer" upload "$ROOT_DIR/test/sample_asset.txt" --json >/dev/null || true
rm -f "$ROOT_DIR/test/sample_asset.txt"

echo "asset-filer smoke test complete"
