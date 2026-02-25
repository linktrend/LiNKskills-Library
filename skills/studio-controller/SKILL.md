---
name: studio-controller
description: "Financial oversight skill implementing GAAP reporting (P&L, Balance Sheet, Cashflow, AR/AP, Budget vs Actual) with Supabase lsl_finance logging and reconciliation controls."
usage_trigger: "Use when executive finance reporting, reconciliation, and transaction oversight are required across revenue and expense systems."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [finance, gaap, controller]
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
dependencies: [revenue-adapter-base, vault, memory]
permissions: [fs_read, fs_write, api_access]
scope_out: ["Do not emit financial reports without GAAP template structure", "Do not finalize unless transactions are logged in lsl_finance schema"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# studio-controller

## Decision Tree (Fail-Fast & Persistence)
0. Resume from `.workdir/tasks/*/state.jsonl` when continuation exists.
1. Validate access to revenue inputs (`revenue-adapter-base`) and expense inputs (Vault-backed).
2. Validate intelligence floor from `engine`.
3. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
4. Classify reporting mode as specialist or generalist.
5. If generalist or >10 tools, call `get_tool_details` and cache schemas.
6. Require GAAP suite outputs: P&L, Balance Sheet, Cashflow, AR/AP, Budget vs Actual.
7. Require transaction logging into Supabase `lsl_finance` schema.
8. Fail-fast on unreconciled mismatches or missing canonical fields.

## Rules

### Scope-In
- Reconcile revenue from YouTube/Stripe normalization against expense streams from Vault-backed systems.
- Produce GAAP-standard reports using `/shared/templates/MASTER_FINANCE_TEMPLATES.md` at repository root.
- Log all transactions into `lsl_finance` schema in Supabase.

### Scope-Out
- Do not publish reports with missing reconciliation status.
- Do not alter source truth without audit trace.
- Do not finalize without output contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: gather and stage finance source inputs.
2. Level 2 - CLI Wrapper Scripts: deterministic transformations and rollups.
3. Level 3 - Direct API: exception-only for high-volume ledger operations.
4. Level 4 - MCP: persistent long-running financial monitors only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save report tables and reconciliation deltas as task-local files.
- Seek specific report sections for targeted reload.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for `Generalist` or >10 tools.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Ingest normalized revenue datasets and expense extracts.
2. Load finance templates from `/shared/templates/MASTER_FINANCE_TEMPLATES.md`.
3. Determine specialist/generalist mode and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Reconcile revenue/expense line items.
7. Build P&L, Balance Sheet, Cashflow, AR/AP, and Budget vs Actual tables.
8. Validate totals and variance thresholds.
9. Prepare canonical transaction records for `lsl_finance`.

### Phase 3: Drafting & Asynchronous Gate
10. Draft financial packet and reconciliation summary.
11. If unresolved mismatch risk is high, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize finance reports and ledger inserts.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with finance control failures.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read normalized revenue and template references before rollup. |
| `write_file` | All | Persist GAAP report artifacts, checkpoint logs, and reconciliation outputs. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `finance_input` | `./references/schemas.json#/definitions/input` | Validate source inputs and reconciliation window. |
| **Output** | `gaap_report_bundle` | `./references/schemas.json#/definitions/output` | Validate GAAP report coverage and lsl_finance logging status. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable finance workflow state. |

## Progressive Disclosure References
- Advanced reconciliation logic: `./advanced/advanced.md`
- Finance interfaces: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
