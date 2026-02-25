---
name: git-safeguard
description: "Applies a mandatory safety checklist before git push operations to prevent accidental or unsafe repository publication."
usage_trigger: "Use when preparing any git push or remote branch publication."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [git, safety, release]
engine:
  min_reasoning_tier: balanced
  preferred_model: gpt-4.1
  context_required: 64000
tooling:
  policy: cli-first
  jit_enabled_if: generalist_or_gt10_tools
  jit_tool_threshold: 10
  require_get_tool_details: true
tools: [write_file, read_file, list_dir, get_tool_details]
dependencies: [git]
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not run git push without checklist completion", "Do not skip staged diff review"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# git-safeguard

## Decision Tree (Fail-Fast & Persistence)
0. Check for existing task in `.workdir/tasks/*/state.jsonl`.
1. Validate frontmatter intelligence floor.
2. Validate tooling policy terms (native cli, cli wrapper, direct api, mcp).
3. Classify Specialist or Generalist; use `get_tool_details` when Generalist.
4. Run safety checklist before any git push.
5. Block push on any unresolved checklist item.

## Safety Checklist (Mandatory Before `git push`)
1. Run `git status` and verify intended branch/files only.
2. Run `git diff --cached` and review exact staged content.
3. Confirm no prohibited artifacts or secrets are staged.
4. Confirm branch naming policy and remote target.
5. Only then permit `git push`.

## Tooling Protocol (CLI-First)
1. Native CLI commands are primary.
2. CLI wrappers may automate checklist execution.
3. Direct API is exception-only.
4. MCP applies only for persistent session operations.

## Internal Persistence (Zero-Copy / Flat-File)
- Append checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save checklist evidence in task-local flat files.
- Seek required checkpoint keys instead of full-file loads.

## Smart JIT Tool Loading (Mitigated)
- Enable JIT only for Generalist or >10 tools.
- Fetch tool details with `get_tool_details` and cache capability summaries.

## Workflow
### Phase 1: Ingestion & Checkpointing
- Capture repo state and intended push target.
- Validate input contract and checkpoint `INITIALIZED`.

### Phase 2: Safety Review
- Execute mandatory commands and capture outputs.
- Validate against policy and checkpoint `IN_PROGRESS`.

### Phase 3: Approval Gate
- If checklist fails, stop with explicit remediation.
- If checklist passes, mark ready for push.

### Phase 4: Finalization
- Record checklist completion in state.
- Output push readiness decision.

### Phase 5: Self-Correction
- Append ledger summary, trace log, and update old-patterns with new failure signals.

## Contracts
- Input: `./references/schemas.json#/definitions/input`
- Output: `./references/schemas.json#/definitions/output`
- State: `./references/schemas.json#/definitions/state`
