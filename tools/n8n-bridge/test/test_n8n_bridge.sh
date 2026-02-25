#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT_DIR/bin/n8n-bridge" --version >/dev/null
"$ROOT_DIR/bin/n8n-bridge" trigger --workflow test --payload '{"ping":true}' --json >/dev/null || true

echo "n8n-bridge smoke test complete"
