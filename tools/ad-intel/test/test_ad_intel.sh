#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT_DIR/bin/ad-intel" --version >/dev/null

echo '[{"campaign":"A","channel":"meta","spend":200,"baseline_spend":100,"ctr":0.8,"baseline_ctr":1.2}]' > "$ROOT_DIR/test/sample.json"
"$ROOT_DIR/bin/ad-intel" monitor --input "$ROOT_DIR/test/sample.json" --json >/dev/null
rm -f "$ROOT_DIR/test/sample.json"

echo "ad-intel smoke test complete"
