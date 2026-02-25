#!/usr/bin/env python3
"""Helper utility for workflow-architect skill."""

from __future__ import annotations

import json
import sys
from typing import Any


def normalize_requirement(raw_json: str) -> dict[str, Any]:
    payload = json.loads(raw_json)
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    normalized = {
        "agent_id": str(payload.get("agent_id", "")).strip(),
        "project_id": str(payload.get("project_id", "")).strip(),
        "workflow_name": str(payload.get("workflow_name", "")).strip(),
        "objective": str(payload.get("objective", "")).strip(),
        "trigger_type": str(payload.get("trigger_type", "manual")).strip(),
        "test_payload": payload.get("test_payload", {}),
    }
    return normalized


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: helper_tool.py '<json_payload>'")
        raise SystemExit(1)
    result = normalize_requirement(sys.argv[1])
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
