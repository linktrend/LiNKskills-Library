#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/sandbox-run" --help >/dev/null
"$(dirname "$0")/../bin/sandbox-run" --version >/dev/null
