---
name: creative-qa
description: "High-fidelity creative auditor that validates rendered assets against brand_guidelines.md and PRD, issuing mandatory PASS/FAIL with revision logic."
usage_trigger: "Use when creative outputs must be quality-gated before publication or handoff."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [creative, qa, brand]
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
dependencies: [creative-director, asset-filer]
permissions: [fs_read, fs_write]
scope_out: ["Do not approve assets without brand_guidelines.md and PRD checks", "Do not return rejection without revision logic"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# creative-qa

## Decision Tree (Fail-Fast & Persistence)
0. Load resumable task state from `.workdir/tasks/*/state.jsonl`.
1. Require access to rendered assets, `brand_guidelines.md`, and PRD.
2. Validate intelligence floor from `engine`.
3. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
4. Classify audit mode as specialist or generalist.
5. If generalist or >10 tools, call `get_tool_details` and cache schemas.
6. Evaluate every asset for brand and PRD compliance.
7. Output must include mandatory `PASS` or `FAIL`.
8. If `FAIL`, include explicit Revision Logic for Creative Director.

## Rules

### Scope-In
- Audit n8n-generated assets for fidelity and requirements fit.
- Compare outputs against `brand_guidelines.md` and PRD.
- Emit PASS/FAIL with revision directives when required.

### Scope-Out
- Do not issue ambiguous statuses.
- Do not skip brand/PRD comparison steps.
- Do not finalize without output contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: collect assets and reference docs.
2. Level 2 - CLI Wrapper Scripts: deterministic QA scoring/checklists.
3. Level 3 - Direct API: exception-only for high-volume asset retrieval.
4. Level 4 - MCP: persistent review sessions only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save audit matrices and revision directives as task-local files.
- Use seek-based reads for per-asset criteria evaluation.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for `Generalist` or >10 tools.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Collect rendered assets and reference docs (`brand_guidelines.md`, PRD).
2. Build asset-level quality checklist.
3. Determine specialist/generalist mode and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Score each asset against brand standards and PRD requirements.
7. Identify critical violations and remediation needs.
8. Generate PASS/FAIL decision with evidence.
9. Build Revision Logic block when failures exist.

### Phase 3: Drafting & Asynchronous Gate
10. Draft QA report with decision and revision logic.
11. If major ambiguity remains, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize QA gate output.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with recurring quality failures.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read PRD and `brand_guidelines.md` before scoring. |
| `write_file` | All | Persist PASS/FAIL report and revision logic artifacts. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `creative_output_set` | `./references/schemas.json#/definitions/input` | Validate assets and reference docs are present. |
| **Output** | `qa_gate_result` | `./references/schemas.json#/definitions/output` | Validate PASS/FAIL and required revision logic. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable quality audit state. |

## Progressive Disclosure References
- Advanced scoring patterns: `./advanced/advanced.md`
- QA rule specs: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
