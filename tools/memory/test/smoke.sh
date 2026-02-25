#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/memory" --help >/dev/null
"$(dirname "$0")/../bin/memory" --version >/dev/null
