#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT_DIR/bin/social-gw" --version >/dev/null
"$ROOT_DIR/bin/social-gw" fetch-comments --provider youtube --target-id dummy --json >/dev/null || true

echo "social-gw smoke test complete"
