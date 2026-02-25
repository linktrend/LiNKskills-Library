---
name: self-critique-loop
description: "Runs a System 2 audit loop that stress-tests draft outputs for correctness, consistency, and risk before release."
usage_trigger: "Use before finalizing high-impact outputs to force structured self-critique and error correction."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [quality, audit, system-2]
engine:
  min_reasoning_tier: high
  preferred_model: gpt-5
  context_required: 128000
tooling:
  policy: cli-first
  jit_enabled_if: generalist_or_gt10_tools
  jit_tool_threshold: 10
  require_get_tool_details: true
tools: [write_file, read_file, list_dir, get_tool_details]
dependencies: []
permissions: [fs_read, fs_write]
scope_out: ["Do not skip critique phase for speed", "Do not suppress detected errors without remediation notes"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# self-critique-loop

## Decision Tree (Fail-Fast & Persistence)
0. Resume from existing `state.jsonl` if critique task is active.
1. Verify draft output exists and is in-scope.
2. Intelligence floor check.
3. Tooling policy check (native cli, cli wrapper, direct api, mcp).
4. Classify as specialist or generalist and fetch JIT details if generalist.
5. Apply System 2 critique checklist.
6. Block finalization if unresolved high-severity issues remain.

## Rules

### Scope-In
- Evaluate drafts for factual, logical, structural, and policy errors.
- Produce issue list, severity, and corrective rewrite suggestions.
- Require at least one explicit re-check pass after corrections.

### Scope-Out
- Do not mark output final without at least one critique pass.
- Do not hide unresolved high-severity findings.
- Do not critique without concrete references to draft segments.

### Tooling Protocol (CLI-First)
1. **Level 1 - Native CLI**: Use native cli for file inspections and diffing.
2. **Level 2 - CLI Wrapper Scripts**: Use cli wrapper scripts for deterministic checks.
3. **Level 3 - Direct API**: Direct api only when exception criteria are met.
4. **Level 4 - MCP**: Use mcp only for persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Write checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save critique matrix and correction diffs as task-local flat files.
- Seek targeted keys for iterative critiques.

### Smart JIT Tool Loading (Mitigated)
- JIT for generalist or >10 tools only.
- Call `get_tool_details` and cache schemas + capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Load draft artifact and intent requirements.
2. Determine specialist/generalist profile.
3. Load JIT tool details if needed.
4. Validate input contract.
5. Checkpoint `INITIALIZED`.

### Phase 2: System 2 Critique
6. Run checks: correctness, consistency, completeness, safety, and style constraints.
7. Score each finding with severity and confidence.
8. Produce correction plan and checkpoint `IN_PROGRESS`.

### Phase 3: Rewrite & Gate
9. Apply corrections and regenerate candidate output.
10. Re-run targeted checks; if unresolved critical issue exists, checkpoint `PENDING_APPROVAL`.

### Phase 4: Finalization
11. Output critique report and corrected artifact.
12. Validate output contract and checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
13. Append run summary to `execution_ledger.jsonl`.
14. Save trace log and add recurring mistakes to `references/old-patterns.md`.

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `draft_artifact` | `./references/schemas.json#/definitions/input` | Validate review context and constraints. |
| **Output** | `critique_report` | `./references/schemas.json#/definitions/output` | Validate findings and corrected output. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist critique checkpoints. |

## Progressive Disclosure References
- Advanced critique methods: `./advanced/advanced.md`
- Checklist details: `./references/api-specs.md`
- Known failure loops: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
