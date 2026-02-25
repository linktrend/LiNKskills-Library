---
name: studio-architect
description: "Template-first architecture skill that enforces factory.json discovery and initialization from approved starter kits before custom development."
usage_trigger: "Use when defining a new studio build and selecting a baseline from SaaS Starter Kit or Website Template before any custom coding."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [architecture, templates, bootstrap]
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
dependencies: [factory-json, saas-starter-kit, website-template]
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not begin custom development before template selection", "Do not bypass factory.json discovery checks"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# studio-architect

## Decision Tree (Fail-Fast & Persistence)
0. Seek resumable task in `.workdir/tasks/*/state.jsonl`.
1. Require readable root `factory.json`.
2. Validate required keys in `factory.json`: `saas_starter_kit`, `website_factory`, `skill_factory`.
3. Require explicit template choice: SaaS Starter Kit or Website Template.
4. Validate intelligence floor from `engine`.
5. Validate tooling policy: native cli, cli wrapper, direct api, mcp.
6. Classify specialist or generalist planning mode.
7. If generalist or >10 tools, call `get_tool_details` and cache tool schemas.
8. Stop if custom implementation starts before baseline initialization from `factory.json`.

## Rules

### Scope-In
- Discover project intent and architecture constraints.
- Select and initialize approved template baseline from root `factory.json`.
- Produce implementation blueprint derived from template-first strategy.

### Scope-Out
- Do not invent greenfield scaffolds when approved templates apply.
- Do not skip baseline comparison and rationale.
- Do not approve custom modules before contract alignment.
- Do not proceed when any required `factory.json` key is missing or empty.

### Tooling Protocol (CLI-First)
1. Level 1: native cli for file and environment discovery.
2. Level 2: cli wrapper scripts for deterministic scaffold generation.
3. Level 3: direct api only for exceptional provider constraints.
4. Level 4: mcp reserved for persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Save all phase snapshots to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Persist template comparison matrices as task-local flat files.
- Use seek-based reads for targeted context reloads.

### Smart JIT Tool Loading (Mitigated)
- Activate only for generalist plans or when tool count >10.
- Use `get_tool_details` and cache schemas for planning visibility.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse request type, business model, and deployment constraints.
2. Read root `factory.json` and validate `saas_starter_kit`, `website_factory`, and `skill_factory`.
3. Resolve initialization source paths from `factory.json` and record selected baseline candidate.
4. Determine specialist/generalist profile.
5. Validate Input Contract.
6. Checkpoint `INITIALIZED`.

### Phase 2: Template-First Planning
7. Evaluate SaaS Starter Kit and Website Template fit using `factory.json` paths.
8. Select baseline with explicit scoring rationale.
9. Define custom deltas only after baseline lock.
10. Checkpoint `IN_PROGRESS`.

### Phase 3: Drafting & Asynchronous Gate
11. Produce architecture blueprint and initialization plan tied to selected `factory.json` source path.
12. If template choice is ambiguous or risky, mark `PENDING_APPROVAL`.

### Phase 4: Finalization
13. Finalize baseline + delta implementation map.
14. Validate Output Contract.
15. Checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
16. Log run into `execution_ledger.jsonl`.
17. Save trace payloads to task `trace.log`.
18. Add template-selection failures to `references/old-patterns.md`.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Must read root `factory.json` and validate required keys before selecting a template. |
| `write_file` | All | Writes checkpoints and architecture artifacts. |
| `get_tool_details` | Phase 1+ | Required in generalist/JIT planning. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `architecture_request` | `./references/schemas.json#/definitions/input` | Validate intent and baseline constraints. |
| **Output** | `baseline_plan` | `./references/schemas.json#/definitions/output` | Validate template choice and custom delta map. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable architectural flow. |

## Progressive Disclosure References
- Advanced heuristics: `./advanced/advanced.md`
- Template policy: `./references/api-specs.md`
- Learned regressions: `./references/old-patterns.md`
- Version record: `./references/changelog.md`
