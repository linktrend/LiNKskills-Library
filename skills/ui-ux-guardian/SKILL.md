---
name: ui-ux-guardian
description: "Design system guardian skill for enforcing Studio CSS standards and Playwright-based visual regression controls."
usage_trigger: "Use when auditing UI changes for consistency with the Studio design system and preventing visual drift."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [design-system, ux, regression]
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
dependencies: [playwright-cli, fast-playwright]
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not approve visual changes without baseline diff", "Do not modify design tokens without explicit policy update"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# ui-ux-guardian

## Decision Tree (Fail-Fast & Persistence)
0. Attempt resume from `.workdir/tasks/*/state.jsonl` when task exists.
1. Confirm target screens, baseline images, and Studio CSS source are available.
2. Validate runtime intelligence floor.
3. Validate tooling protocol order: native cli, cli wrapper, direct api, mcp.
4. Classify specialist or generalist audit profile.
5. If generalist or >10 tools, call `get_tool_details` and cache capabilities.
6. Block approval if visual diff exceeds policy tolerance.

## Rules

### Scope-In
- Run visual regression comparisons using Playwright tools.
- Detect deviations from design tokens, spacing, typography, and component states.
- Produce actionable remediation guidance.

### Scope-Out
- Do not pass UI changes without evidence artifacts.
- Do not accept one-off CSS overrides that bypass tokens.
- Do not skip accessibility and responsive checks.

### Tooling Protocol (CLI-First)
1. Level 1: native cli for file and artifact checks.
2. Level 2: cli wrapper scripts (`playwright-cli`) for deterministic snapshots.
3. Level 3: direct api only when wrapper output is insufficient.
4. Level 4: mcp for persistent interactive sessions (`fast-playwright`) when needed.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoint lines to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save screenshots and diff metadata as task-local files.
- Use seek-based reads to fetch only failing selectors or pages.

### Smart JIT Tool Loading (Mitigated)
- Enable only for generalist/multi-surface audits or >10 tools.
- `get_tool_details` is required to load tool schemas and capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Gather changed routes/pages and expected design tokens.
2. Load baseline image references and threshold policy.
3. Determine specialist/generalist mode and initialize JIT cache if required.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Visual Audit Logic
6. Capture fresh screenshots with Playwright.
7. Run visual and token-level diffs.
8. Classify deltas as pass/warn/fail and prepare remediation list.
9. Append `IN_PROGRESS` checkpoint.

### Phase 3: Drafting & Asynchronous Gate
10. Draft audit report with failing selectors/pages.
11. If critical visual regression appears, mark `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize audit report and gating recommendation.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Log run summary to `execution_ledger.jsonl`.
16. Save traces and screenshots index to task trace files.
17. Update `references/old-patterns.md` with recurring UI drift patterns.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `playwright-cli` | Phases 1-4 | Required for deterministic screenshot and PDF artifacts. |
| `fast-playwright` | Phases 2-3 | Use for interactive debugging when static snapshots are insufficient. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT audits. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `ui_audit_request` | `./references/schemas.json#/definitions/input` | Validate target pages, baselines, and thresholds. |
| **Output** | `ui_audit_report` | `./references/schemas.json#/definitions/output` | Validate diff results and pass/fail decision. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable audit checkpoints. |

## Progressive Disclosure References
- Audit edge cases: `./advanced/advanced.md`
- Tool usage notes: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version notes: `./references/changelog.md`
