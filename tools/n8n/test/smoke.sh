#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/../bin/n8n" --help >/dev/null
"$(dirname "$0")/../bin/n8n" --version >/dev/null
