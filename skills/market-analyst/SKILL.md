---
name: market-analyst
description: "Runs competitor teardown and SWOT analysis workflows using the research tool with confidence-based escalation and cost controls."
usage_trigger: "Use when market intelligence is needed for competitor analysis, positioning, and strategic SWOT synthesis."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [research, competitors, strategy]
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
dependencies: [research, search-strategy]
permissions: [fs_read, fs_write, api_access]
scope_out: ["Do not return claims without source evidence", "Do not run deep research without required HITL controls"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# market-analyst

## Decision Tree (Fail-Fast & Persistence)
0. Load resumable task context from `.workdir/tasks/*/state.jsonl` if available.
1. Validate target market and competitor set.
2. Require explicit research intent before paid API calls.
3. Validate intelligence floor from `engine`.
4. Validate tooling policy: native cli, cli wrapper, direct api, mcp.
5. Classify workload as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. If deep multi-step research is needed, gate with operator approval before execution.

## Rules

### Scope-In
- Execute competitor teardown with evidence-backed findings.
- Produce SWOT with strengths, weaknesses, opportunities, and threats.
- Track confidence levels and escalation path for research tiers.

### Scope-Out
- Do not output unsupported conclusions.
- Do not skip source quality checks.
- Do not bypass deep-research approval controls.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: prepare query context and local references.
2. Level 2 - CLI Wrapper Scripts: use `/tools/research` wrappers by default.
3. Level 3 - Direct API: exception-only for capabilities not exposed by wrappers.
4. Level 4 - MCP: reserved for persistent session-based operations.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints in `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save competitor evidence and SWOT drafts as task-local flat files.
- Use seek-based reads for targeted source recall.

### Smart JIT Tool Loading (Mitigated)
- Enable JIT only when `Generalist` or tool count >10.
- Call `get_tool_details` and cache schemas/capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse objective, market segment, competitors, and decision horizon.
2. Draft research intent and confidence thresholds.
3. Determine specialist/generalist profile and JIT caching needs.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Run tiered research workflow (web then neural, then brief/social if required).
7. Build competitor teardown matrix.
8. Build SWOT from sourced evidence.
9. Keep specialist flows embedded; use JIT schema cache for generalist flows.

### Phase 3: Drafting & Asynchronous Gate
10. Produce draft market intelligence report.
11. If deep-research gate is triggered, set `PENDING_APPROVAL` and pause.

### Phase 4: Finalization
12. Finalize teardown and SWOT recommendations.
13. Validate Output Contract.
14. Append completion checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append run summary to `execution_ledger.jsonl`.
16. Save trace data to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with failed-research heuristics.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `/tools/research/bin/research` | Phases 2-4 | Must follow tier escalation policy and confidence gating. |
| `write_file` | All | Required for checkpointing and report artifacts. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `market_request` | `./references/schemas.json#/definitions/input` | Validate market scope and competitor targets. |
| **Output** | `swot_report` | `./references/schemas.json#/definitions/output` | Validate teardown evidence and SWOT completeness. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persistent resumability and auditability. |

## Progressive Disclosure References
- Advanced teardown patterns: `./advanced/advanced.md`
- Research protocol specs: `./references/api-specs.md`
- Anti-pattern catalog: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
