#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/research" --help >/dev/null
"$(dirname "$0")/../bin/research" --version >/dev/null
