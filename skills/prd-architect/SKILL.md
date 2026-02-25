---
name: prd-architect
description: "Converts a vibe or rough idea into a professional technical specification with scope, architecture, constraints, and delivery criteria."
usage_trigger: "Use when a project starts from a high-level idea and needs a production-grade technical specification before implementation."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [discovery, strategy, specification]
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
dependencies: [factory-json]
permissions: [fs_read, fs_write]
scope_out: ["Do not start implementation code", "Do not skip ambiguity resolution before spec finalization"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# prd-architect

## Decision Tree (Fail-Fast & Persistence)
0. Check resumable state in `.workdir/tasks/*/state.jsonl`.
1. Confirm the idea/vibe statement is present.
2. Confirm target business outcome and user persona are provided or derivable.
3. Validate intelligence floor from `engine`.
4. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
5. Classify planning mode as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Require `references/MASTER_PRD_TEMPLATE.md` as the mandatory output structure for new project briefings.
8. Fail-fast on unresolved core ambiguity (problem, user, success metric).

## Rules

### Scope-In
- Convert vague intent into formal problem framing.
- Produce a complete technical specification with architecture and contracts.
- Capture delivery phases, assumptions, and acceptance criteria.
- Use `references/MASTER_PRD_TEMPLATE.md` for every new project briefing.

### Scope-Out
- Do not write application code.
- Do not leave risks or assumptions implicit.
- Do not finalize without output contract validation.
- Do not produce ad-hoc PRD formats that diverge from the master template.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: gather local references and context.
2. Level 2 - CLI Wrapper Scripts: use scripts for deterministic formatting/checks.
3. Level 3 - Direct API: exception-only for high-frequency reasoning or high serialization cost.
4. Level 4 - MCP: only for persistent background sessions.

### Internal Persistence (Zero-Copy / Flat-File)
- Write phase checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save working spec drafts as flat files under task folder.
- Subsequent phases should seek precise sections instead of full reload.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only if `Generalist` or tool count >10.
- Call `get_tool_details` and cache capability summaries for planning.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse idea statement, business intent, and target users.
2. Identify unknowns and generate clarification checklist.
3. Determine specialist/generalist profile and load JIT details if needed.
4. Load `references/MASTER_PRD_TEMPLATE.md` and map incoming context to template sections.
5. Validate Input Contract.
6. Append `INITIALIZED` snapshot to `state.jsonl`.

### Phase 2: Logic & Reasoning
7. Convert idea into problem statement, goals, and non-goals.
8. Define architecture outline, core modules, and data flow.
9. Draft constraints, assumptions, and risk list.
10. Populate all required sections in `MASTER_PRD_TEMPLATE.md`, including Venture Thesis, Success Metrics, User Personas, Functional Specs (MoSCoW), and Technical Constraints.
11. For specialist flow use embedded schemas; for generalist use cached JIT schemas.

### Phase 3: Drafting & Asynchronous Gate
12. Produce draft Technical Specification strictly following `MASTER_PRD_TEMPLATE.md`.
13. If unresolved critical ambiguity exists, mark `PENDING_APPROVAL` and pause.

### Phase 4: Finalization
14. Finalize specification with acceptance criteria and rollout phases.
15. Validate Output Contract.
16. Append completion checkpoint to `state.jsonl`.

### Phase 5: Self-Correction & Auditing
17. Append run summary to `execution_ledger.jsonl`.
18. Save trace payloads to `.workdir/tasks/{{task_id}}/trace.log`.
19. Update `references/old-patterns.md` with ambiguity/failure learnings.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Load context artifacts and prior specs when available. |
| `write_file` | All | Required for checkpointing and spec artifact drafting. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `idea_context` | `./references/schemas.json#/definitions/input` | Validate discovery and business context. |
| **Output** | `technical_spec` | `./references/schemas.json#/definitions/output` | Validate professional specification completeness. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persistent resumability and auditability. |

## Progressive Disclosure References
- Advanced edge cases: `./advanced/advanced.md`
- Spec conventions: `./references/api-specs.md`
- Master PRD layout: `./references/MASTER_PRD_TEMPLATE.md`
- Deprecated heuristics: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
