---
name: blocker-resolution
description: "Fail-fast escalation protocol for stuck worker agents that triggers Root Cause Analysis when PROGRESS.md remains Blocked for more than two turns."
usage_trigger: "Use when developer or worker streams are repeatedly blocked and require structured diagnosis and recovery actions."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [blockers, escalation, rca]
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
dependencies: [repository-manager]
permissions: [fs_read, fs_write]
scope_out: ["Do not ignore repeated blocked states", "Do not continue execution without RCA after blocked status persists >2 turns"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# blocker-resolution

## Decision Tree (Fail-Fast & Persistence)
0. Resume from `.workdir/tasks/*/state.jsonl` if applicable.
1. Locate worker `PROGRESS.md` files and parse status timeline.
2. Validate intelligence floor from `engine`.
3. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
4. Classify incident handling as specialist or generalist.
5. If generalist or >10 tools, call `get_tool_details` and cache schemas.
6. If status is `Blocked` for more than 2 turns, trigger mandatory RCA.
7. Fail-fast if no unblock action is defined after RCA.

## Rules

### Scope-In
- Detect persistent blocked states in worker streams.
- Trigger Root Cause Analysis (RCA) when blocked threshold is exceeded.
- Produce actionable unblock plan with owners and time bounds.

### Scope-Out
- Do not accept vague blocker descriptions.
- Do not defer RCA when threshold is exceeded.
- Do not close incident without measurable next step.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: parse `PROGRESS.md` histories.
2. Level 2 - CLI Wrapper Scripts: deterministic extraction of status transitions.
3. Level 3 - Direct API: exception-only for external incident systems.
4. Level 4 - MCP: only for persistent incident sessions.

### Internal Persistence (Zero-Copy / Flat-File)
- Write checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Store RCA notes and unblock plans as task-local files.
- Seek specific turn/status records during resume.

### Smart JIT Tool Loading (Mitigated)
- Enable JIT only if `Generalist` or tool count >10.
- Use `get_tool_details` and cache tool schema summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Collect relevant `PROGRESS.md` files and status histories.
2. Count consecutive blocked turns per worker stream.
3. Determine specialist/generalist profile and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Evaluate blocker severity and dependency impact.
7. If blocked >2 turns, execute RCA protocol (root causes, evidence, candidate fixes).
8. Define unblock actions with owner and due window.
9. For specialist use embedded schemas; for generalist use cached JIT schemas.

### Phase 3: Drafting & Asynchronous Gate
10. Draft RCA report and unblock directive set.
11. If decision authority is needed, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize RCA output and next-action checklist.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace data to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with recurring blocker signatures.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Must read worker `PROGRESS.md` and turn histories. |
| `write_file` | All | Persist RCA artifacts, unblock plan, and checkpoints. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `blocker_context` | `./references/schemas.json#/definitions/input` | Validate worker status timeline and constraints. |
| **Output** | `rca_report` | `./references/schemas.json#/definitions/output` | Validate root-cause findings and unblock actions. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumability and escalation history. |

## Progressive Disclosure References
- Advanced RCA logic: `./advanced/advanced.md`
- Protocol details: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
