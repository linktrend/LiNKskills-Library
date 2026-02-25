---
name: task-decomposition
description: "Applies Factored Cognition to decompose complex studio work into atomic, verifiable execution steps."
usage_trigger: "Use when a task is complex, ambiguous, or multi-domain and needs structured decomposition before execution."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [cognition, planning, decomposition]
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
scope_out: ["Do not execute business side effects while decomposing", "Do not skip atomic verification criteria for each subtask"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# task-decomposition

## Decision Tree (Fail-Fast & Persistence)
0. **Resume Check**: If a decomposition task exists in `.workdir/tasks/*/state.jsonl`, resume with same `task_id`.
1. **Complexity Gate**: If task is already atomic and low-risk, return minimal decomposition and stop.
2. **Intelligence Floor Check**: Ensure runtime meets `engine` constraints.
3. **Tooling Protocol Check**: Enforce native cli, cli wrapper, direct api, and mcp policy.
4. **Profile Check**: Classify workload as specialist or generalist.
5. **JIT Check**: If generalist, run `get_tool_details` and cache planning schemas.
6. **Contract Check**: Validate request with `./references/schemas.json#/definitions/input`.

## Rules

### Scope-In
- Break complex objectives into independent atomic subtasks.
- Use Factored Cognition: isolate assumptions, subproblems, dependencies, and verification checks.
- Produce execution-ready decomposition artifacts with explicit ordering.

### Scope-Out
- Do not execute downstream business actions.
- Do not merge unrelated concerns into one atomic step.
- Do not create subtasks without acceptance criteria.

### Tooling Protocol (CLI-First)
1. **Level 1 - Native CLI**: Use native cli for file/context inspection.
2. **Level 2 - CLI Wrapper Scripts**: Use cli wrapper scripts when deterministic transformation is needed.
3. **Level 3 - Direct API**: Use direct api only for approved exception scenarios.
4. **Level 4 - MCP**: Use mcp only for persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Append each phase checkpoint to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Store decomposition graph and dependency matrix as task-local flat files.
- Later phases should seek specific keys rather than loading full artifacts.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for generalist tasks or tool count >10.
- Call `get_tool_details` for capability summaries and cache in task state.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse objective, constraints, and deliverable format.
2. Label scope as specialist or generalist.
3. If generalist, fetch and cache tool details.
4. Validate input contract.
5. Checkpoint with `status: INITIALIZED`.

### Phase 2: Factored Cognition Expansion
6. Create problem tree: objective -> sub-objectives -> atomic subtasks.
7. For each subtask, define inputs, outputs, dependencies, and risk tags.
8. Add verification criteria and failure conditions.
9. Checkpoint with `status: IN_PROGRESS`.

### Phase 3: Draft Plan & Gate
10. Build ordered execution plan with parallelizable segments.
11. If critical ambiguity remains, checkpoint `PENDING_APPROVAL` and stop.

### Phase 4: Finalization
12. Emit final decomposition artifact and dependency map.
13. Validate output contract and checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
14. Append summary to `execution_ledger.jsonl`.
15. Write trace log to `.workdir/tasks/{{task_id}}/trace.log`.
16. Update `references/old-patterns.md` with decomposition mistakes observed.

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `decomposition_request` | `./references/schemas.json#/definitions/input` | Validate scope and constraints. |
| **Output** | `decomposition_plan` | `./references/schemas.json#/definitions/output` | Validate atomic plan completeness. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable checkpoints. |

## Progressive Disclosure References
- Advanced heuristics: `./advanced/advanced.md`
- Validation details: `./references/api-specs.md`
- Historical failures: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
