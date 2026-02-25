---
name: lead-engineer
description: "Refactored senior execution model for PRD decomposition, factory.json routing, and sub-agent sessions_spawn coordination."
usage_trigger: "Use when a product request must be decomposed into execution lanes and delegated through controlled sub-agent sessions."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [orchestration, prd, routing]
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
dependencies: [factory-json, sessions-spawn]
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not implement feature code directly that belongs to delegated worker sessions", "Do not spawn sessions before route ownership is validated in factory.json"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# lead-engineer

## Decision Tree (Fail-Fast & Persistence)
0. Check for resumable task state in `.workdir/tasks/*/state.jsonl`.
1. Validate PRD payload and objective clarity.
2. Require `factory.json` and route-map parse success.
3. Run intelligence floor check against frontmatter `engine`.
4. Run tooling protocol check: native cli, cli wrapper, direct api, mcp.
5. Classify run as specialist or generalist.
6. If generalist or tool count exceeds 10, call `get_tool_details` and cache schemas in task state.
7. Run the mandatory 10-step orchestration logic before any implementation recommendation.
8. Hard gate: `PLAN.md` and `RISK_MAP.md` must exist before any file modifications are allowed.
9. Validate delegation budget and `sessions_spawn` limits before issuing plan.

## Rules

### Scope-In
- Decompose PRD into atomic work packets with acceptance criteria.
- Route packets using `factory.json` owner and capability data.
- Produce constrained `sessions_spawn` plan for delegated execution.
- Create `PLAN.md` and `RISK_MAP.md` as mandatory pre-modification artifacts.

### Scope-Out
- Do not merge all work into one lane when routing requires specialization.
- Do not bypass pre-spawn risk checks.
- Do not finalize without contract validation.
- Do not modify project files until both `PLAN.md` and `RISK_MAP.md` are written and checkpointed.

### Tooling Protocol (CLI-First)
1. Level 1: native cli for repository and context discovery.
2. Level 2: cli wrapper scripts for deterministic transformations.
3. Level 3: direct api is exception-only for high serialization or real-time constraints.
4. Level 4: mcp only for persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Write phase checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Store decomposition maps, route maps, and spawn plans as task-local flat files.
- Later phases should seek exact keys rather than loading all artifacts.

### Smart JIT Tool Loading (Mitigated)
- Enable JIT only for generalist or >10 tools.
- For JIT runs, call `get_tool_details`, cache schemas, and capture one-line capability summaries.

## 10-Step Orchestration Logic
1. Scope Lock: define objective, out-of-scope, and done-criteria.
2. Inventory Inputs: enumerate PRD sections, constraints, and mandatory dependencies.
3. Inventory Assets: identify existing modules, tools, and ownership signals from `factory.json`.
4. Decompose: split work into atomic packets with explicit acceptance criteria.
5. Route: assign packets to owners/lane targets using `factory.json`.
6. Dependency Map: capture ordering constraints and critical path items.
7. Risk Map: identify technical, schedule, and integration risks with severity/mitigation.
8. Build `PLAN.md`: write execution sequence, packet ownership, and validation gates.
9. Build `RISK_MAP.md`: write ranked risks, triggers, and rollback responses.
10. Pre-Modification Gate: block all file changes until steps 8 and 9 are completed and checkpointed.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Load PRD, constraints, SLA, and dependencies.
2. Load `factory.json` and required lane definitions.
3. Set specialist/generalist profile and initialize JIT cache if needed.
4. Execute 10-step logic steps 1-3 (Scope + Inventory).
5. Validate Input Contract.
6. Append `INITIALIZED` checkpoint.

### Phase 2: Decomposition & Routing
7. Execute 10-step logic steps 4-7 (Decompose + Route + Dependency + Risk).
8. Write `PLAN.md` (step 8) and `RISK_MAP.md` (step 9).
9. Enforce pre-modification gate (step 10): no file modifications until both artifacts exist.
10. Build `sessions_spawn` records with scope, deliverable, and rollback path.
11. Append `IN_PROGRESS` checkpoint.

### Phase 3: Drafting & Asynchronous Gate
12. Generate draft orchestration plan from `PLAN.md` and `RISK_MAP.md`.
13. If delegation risk is high, append `PENDING_APPROVAL` and stop.

### Phase 4: Finalization
14. Finalize route and spawn plan after approval.
15. Validate Output Contract.
16. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
17. Append summary to `execution_ledger.jsonl`.
18. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
19. Update `references/old-patterns.md` with routing/delegation failure lessons.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read `factory.json` and PRD context before planning. |
| `write_file` | All | Required for checkpoints and mandatory `PLAN.md` / `RISK_MAP.md` artifacts. |
| `get_tool_details` | Phase 1+ | Mandatory for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `prd_request` | `./references/schemas.json#/definitions/input` | Validate PRD and routing requirements. |
| **Output** | `orchestration_plan` | `./references/schemas.json#/definitions/output` | Validate packet routing and sessions_spawn data. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable checkpoints. |

## Progressive Disclosure References
- Advanced logic: `./advanced/advanced.md`
- Interfaces: `./references/api-specs.md`
- Regression memory: `./references/old-patterns.md`
- Version log: `./references/changelog.md`
