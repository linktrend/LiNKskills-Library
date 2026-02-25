#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/vault" --help >/dev/null
"$(dirname "$0")/../bin/vault" --version >/dev/null
