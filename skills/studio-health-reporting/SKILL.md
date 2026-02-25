---
name: studio-health-reporting
description: "Aggregates lsl_memory.audit_logs and PROGRESS.md streams into a Venture Studio Health Report for COO oversight."
usage_trigger: "Use when Lisa needs a consolidated, evidence-based health report across studio delivery streams."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [reporting, operations, health]
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
dependencies: [memory, department-head]
permissions: [fs_read, fs_write, api_access]
scope_out: ["Do not issue unsupported health claims", "Do not omit source attribution from audit logs or PROGRESS reports"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# studio-health-reporting

## Decision Tree (Fail-Fast & Persistence)
0. Check resumable state in `.workdir/tasks/*/state.jsonl`.
1. Collect `PROGRESS.md` artifacts from active streams.
2. Collect audit events from `lsl_memory.audit_logs`.
3. Validate intelligence floor from `engine`.
4. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
5. Classify report generation as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Fail-fast if source data is missing or stale.

## Rules

### Scope-In
- Aggregate operational data from progress and audit streams.
- Generate a Venture Studio Health Report in Markdown.
- Surface risks, velocity signals, and quality trends for COO review.

### Scope-Out
- Do not infer metrics without source evidence.
- Do not hide unresolved blockers.
- Do not finalize report without output contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: discover and load local progress artifacts.
2. Level 2 - CLI Wrapper Scripts: normalize and summarize records.
3. Level 3 - Direct API: exception-only for memory query calls.
4. Level 4 - MCP: persistent session services only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save extracted metrics and report drafts as task-local flat files.
- Use seek-based reads for targeted sections and indicators.

### Smart JIT Tool Loading (Mitigated)
- Enable JIT only for `Generalist` or >10 tools.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Load `PROGRESS.md` files and parse status, blockers, and handoff notes.
2. Query `lsl_memory.audit_logs` for recent operational events.
3. Determine specialist/generalist profile and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Aggregate delivery, quality, and risk indicators.
7. Compute health categories (green/yellow/red) with source evidence.
8. Draft Markdown report structure for COO consumption.
9. Use embedded schemas for specialist; JIT cache for generalist.

### Phase 3: Drafting & Asynchronous Gate
10. Produce draft Venture Studio Health Report (Markdown).
11. If critical uncertainty exists, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize report with recommendations and owner assignments.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace payloads to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with reporting pitfalls.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read all required `PROGRESS.md` inputs. |
| `write_file` | All | Persist report drafts, checkpoints, and metrics artifacts. |
| `get_tool_details` | Phase 1+ | Mandatory for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `health_inputs` | `./references/schemas.json#/definitions/input` | Validate progress and audit-log input context. |
| **Output** | `health_report` | `./references/schemas.json#/definitions/output` | Validate Markdown report completeness and evidence traceability. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable report generation flow. |

## Progressive Disclosure References
- Advanced analytics: `./advanced/advanced.md`
- Data interface notes: `./references/api-specs.md`
- Anti-pattern catalog: `./references/old-patterns.md`
- Version log: `./references/changelog.md`
