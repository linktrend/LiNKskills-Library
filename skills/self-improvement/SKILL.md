---
name: self-improvement
description: "Analyzes execution_ledger and historical failure patterns to propose versioned upgrades to LiNKskills tools and skills."
usage_trigger: "Use when improving the Library itself based on execution history, failures, regressions, or requested feature upgrades."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [meta, optimization, evolution]
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
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not apply breaking changes without explicit migration path", "Do not change tools or skills without evidence from ledger/patterns/user request"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# self-improvement

## Decision Tree (Fail-Fast & Persistence)
0. Resume active improvement task from `.workdir/tasks/*/state.jsonl` if present.
1. Confirm evidence sources are available: `execution_ledger.jsonl`, `references/old-patterns.md`, user-requested features.
2. Intelligence floor check.
3. Tooling policy check (native cli, cli wrapper, direct api, mcp).
4. Classify specialist or generalist and use JIT if generalist.
5. Build evidence-backed improvement proposals only.
6. Block proposals lacking measurable impact or rollback path.

## Rules

### Scope-In
- Aggregate failure/latency/HITL trends from ledger entries.
- Cross-reference old-patterns and recent user feature requests.
- Produce versioned upgrade proposals for skills/tools with migration notes.

### Scope-Out
- Do not propose speculative changes without evidence.
- Do not remove safety or persistence primitives.
- Do not skip changelog and rollback guidance.

### Tooling Protocol (CLI-First)
1. **Level 1 - Native CLI**: Use native cli to inspect ledger and references.
2. **Level 2 - CLI Wrapper Scripts**: Use cli wrapper scripts for deterministic analytics where available.
3. **Level 3 - Direct API**: Direct api only under exception conditions.
4. **Level 4 - MCP**: Use mcp for persistent session analytics only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save phase snapshots to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save trend tables and proposal diffs as task-local flat files.
- Seek targeted fields for incremental analysis.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT for generalist or >10 tools.
- Use `get_tool_details` and cache capability summaries before proposing cross-tool changes.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Load `execution_ledger.jsonl` and target old-patterns files.
2. Merge with explicit user-requested feature improvements.
3. Determine specialist/generalist profile and load JIT details if needed.
4. Validate input contract and checkpoint `INITIALIZED`.

### Phase 2: Trend Analysis
5. Compute failure clusters, recurring blockers, and HITL bottlenecks.
6. Map trends to candidate interventions (skill rule, schema tightening, tool upgrade).
7. Checkpoint `IN_PROGRESS` with ranked opportunities.

### Phase 3: Proposal Drafting & Gate
8. Draft versioned proposal set with impact, risk, and rollback strategy.
9. If evidence is weak or conflicting, checkpoint `PENDING_APPROVAL`.

### Phase 4: Finalization
10. Emit prioritized improvement roadmap and patch plan.
11. Validate output contract and checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
12. Append summary to `execution_ledger.jsonl`.
13. Save trace log and update old-patterns for analysis mistakes.

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `improvement_context` | `./references/schemas.json#/definitions/input` | Validate available evidence scope. |
| **Output** | `improvement_plan` | `./references/schemas.json#/definitions/output` | Validate versioned proposals with rollback info. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist analytical checkpoints. |

## Progressive Disclosure References
- Advanced trend analysis: `./advanced/advanced.md`
- Proposal rubric: `./references/api-specs.md`
- Historical anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
