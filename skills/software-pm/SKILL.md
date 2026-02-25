---
name: software-pm
description: "Software project management orchestrator that converts PRDs into technical backlogs aligned to SaaS/Web factories and enforces QA-backed Definition of Done."
usage_trigger: "Use when a software project needs structured backlog planning, sprint sequencing, and quality-gated completion criteria."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [software-pm, backlog, delivery]
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
dependencies: [prd-architect, lead-engineer, persistent-qa, factory-json]
permissions: [fs_read, fs_write]
scope_out: ["Do not bypass factory alignment when creating backlog items", "Do not mark items Done without QA sign-off evidence"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# software-pm

## Decision Tree (Fail-Fast & Persistence)
0. Check for resumable state in `.workdir/tasks/*/state.jsonl`.
1. Validate PRD and project objective exist.
2. Read `factory.json` and map project to `saas_starter_kit` or `website_factory`.
3. Validate intelligence floor from `engine`.
4. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
5. Classify planning as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Fail-fast if backlog items are not factory-aligned.
8. Fail-fast if Definition of Done omits QA sign-off.

## Rules

### Scope-In
- Decompose PRD into a technical backlog tied to SaaS/Web factories.
- Define sprint-ready sequencing with dependencies and risk labels.
- Enforce Definition of Done including QA sign-off.

### Scope-Out
- Do not write implementation code.
- Do not produce backlog without traceability to PRD and factory.
- Do not close tasks without QA evidence.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: inspect PRD/factory context.
2. Level 2 - CLI Wrapper Scripts: deterministic backlog transformations.
3. Level 3 - Direct API: exception-only for high-serialization workflows.
4. Level 4 - MCP: session-based services only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save phase checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Store backlog tables and DoD matrix as task-local flat files.
- Subsequent phases seek specific sections instead of full reloads.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only if `Generalist` or >10 tools.
- Call `get_tool_details` and cache one-line capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse PRD scope, release intent, and constraints.
2. Load `factory.json` and determine SaaS or Web factory alignment.
3. Set specialist/generalist profile and initialize JIT cache if needed.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Decompose PRD into epics, stories, and technical tasks.
7. Map each backlog item to factory modules and dependencies.
8. Attach DoD checklist, including mandatory QA sign-off.
9. For specialist paths use embedded schema references; for generalist use JIT caches.

### Phase 3: Drafting & Asynchronous Gate
10. Draft Technical Backlog and sprint sequence.
11. If DoD compliance is incomplete, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize backlog, sequencing plan, and DoD gates.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with planning failures.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read PRD and `factory.json` before decomposition. |
| `write_file` | All | Persist backlog, DoD artifacts, and checkpoints. |
| `get_tool_details` | Phase 1+ | Mandatory in generalist/JIT runs. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `pm_input` | `./references/schemas.json#/definitions/input` | Validate PRD and factory context. |
| **Output** | `technical_backlog` | `./references/schemas.json#/definitions/output` | Validate backlog structure and QA-gated DoD. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable progress. |

## Progressive Disclosure References
- Advanced sequencing: `./advanced/advanced.md`
- Interfaces/specs: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
