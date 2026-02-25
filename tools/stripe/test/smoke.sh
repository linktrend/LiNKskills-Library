#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/stripe" --help >/dev/null
"$(dirname "$0")/../bin/stripe" --version >/dev/null
