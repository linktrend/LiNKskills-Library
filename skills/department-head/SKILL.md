---
name: department-head
description: "COO-level coordination skill for managing Lead Engineer and Persistent QA workstreams through PROGRESS.md-driven governance."
usage_trigger: "Use when Lisa needs to supervise delivery status, unblock teams, and align engineering and QA execution via structured progress reports."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [operations, governance, coordination]
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
dependencies: [lead-engineer, persistent-qa]
permissions: [fs_read, fs_write]
scope_out: ["Do not edit implementation files directly", "Do not close items without confirming PROGRESS.md evidence"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# department-head

## Decision Tree (Fail-Fast & Persistence)
0. Load resumable context from `.workdir/tasks/*/state.jsonl` if task exists.
1. Locate and read active `PROGRESS.md` files for Lead Engineer and QA streams.
2. Validate issue status (`Done`, `Blocked`, `In-Progress`) and context handoff quality.
3. Validate intelligence floor from `engine`.
4. Validate tooling policy: native cli, cli wrapper, direct api, mcp.
5. Classify coordination run as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Fail-fast if required `PROGRESS.md` reports are missing.

## Rules

### Scope-In
- Review delivery and QA status through `PROGRESS.md` reports.
- Set COO-level priorities and unblock actions.
- Produce synchronized action directives for Lead Engineer and QA.

### Scope-Out
- Do not execute implementation tasks directly.
- Do not override QA risk flags without explicit rationale.
- Do not finalize status without contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: locate and inspect progress files.
2. Level 2 - CLI Wrapper Scripts: use wrappers for deterministic report synthesis.
3. Level 3 - Direct API: exception-only for high-volume coordination integrations.
4. Level 4 - MCP: only for persistent background management sessions.

### Internal Persistence (Zero-Copy / Flat-File)
- Append phase checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save coordination briefs and assignment matrices as flat files.
- Use seek-based reads for targeted status reloads.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only when `Generalist` or tools >10.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Collect all relevant `PROGRESS.md` files from active streams.
2. Normalize statuses, blockers, and next actions.
3. Determine specialist/generalist mode and JIT need.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Compare engineering progress against QA findings.
7. Identify sequencing conflicts, risk hotspots, and dependency gaps.
8. Build COO directive plan with owner, priority, and due rationale.
9. Use embedded schemas for specialist; cached JIT schemas for generalist.

### Phase 3: Drafting & Asynchronous Gate
10. Draft coordinated update and assignment directives.
11. If critical blocker needs executive decision, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize directive set and updated status matrix.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with coordination failure lessons.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Must read `PROGRESS.md` for Lead Engineer and QA before directives. |
| `write_file` | All | Required for checkpointing and COO directive artifacts. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `ops_context` | `./references/schemas.json#/definitions/input` | Validate progress snapshots and ownership context. |
| **Output** | `coo_directives` | `./references/schemas.json#/definitions/output` | Validate prioritization and assignment clarity. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persistent resumability and auditability. |

## Progressive Disclosure References
- Governance edge cases: `./advanced/advanced.md`
- PROGRESS protocol: `./references/api-specs.md`
- Anti-pattern memory: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
