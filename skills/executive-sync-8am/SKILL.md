---
name: executive-sync-8am
description: "Executive sync orchestration skill that starts data collection at 06:00 Taipei, queries department leads, and consolidates Wins, Blockers, and Financial Health into the 08:00 AM briefing."
usage_trigger: "Use for daily executive standup preparation and structured morning briefing consolidation for studio leadership."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [executive, standup, briefing]
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
dependencies: [department-head, studio-controller, studio-health-reporting]
permissions: [fs_read, fs_write]
scope_out: ["Do not publish briefing without lead updates", "Do not omit financial health section from 08:00 briefing"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# executive-sync-8am

## Decision Tree (Fail-Fast & Persistence)
0. Resume from `.workdir/tasks/*/state.jsonl` for daily run continuation.
1. Trigger preparation workflow at 06:00 Taipei local time.
2. Query all department-lead updates and required status sources.
3. Validate intelligence floor from `engine`.
4. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
5. Classify sync mode as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Require briefing sections: Wins, Blockers, Financial Health.
8. Final output must be ready for 08:00 AM user briefing.

## Rules

### Scope-In
- Collect departmental status updates in early sync window.
- Consolidate cross-team wins/blockers plus financial health.
- Produce final executive briefing package for 08:00 delivery.

### Scope-Out
- Do not fabricate missing updates.
- Do not skip financial health inclusion.
- Do not finalize without output contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: collect local status artifacts.
2. Level 2 - CLI Wrapper Scripts: deterministic briefing synthesis.
3. Level 3 - Direct API: exception-only for high-frequency status pulls.
4. Level 4 - MCP: persistent morning sync sessions only.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save lead summaries and briefing drafts as task-local files.
- Use seek-based reads for section-level update refreshes.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for `Generalist` or >10 tools.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. At 06:00 Taipei, collect all department lead inputs.
2. Load prior-day briefing and outstanding blocker context.
3. Determine specialist/generalist mode and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Aggregate and deduplicate wins and blockers.
7. Pull financial health summary from controller outputs.
8. Rank issues by urgency and owner accountability.
9. Draft briefing narrative with clear action points.

### Phase 3: Drafting & Asynchronous Gate
10. Draft 08:00 AM executive briefing.
11. If critical data is missing, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize briefing package for user delivery.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with briefing-quality failures.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Read lead reports and controller outputs before synthesis. |
| `write_file` | All | Persist briefing drafts, checkpoints, and final package. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `executive_sync_input` | `./references/schemas.json#/definitions/input` | Validate lead-update and financial-source readiness. |
| **Output** | `executive_briefing` | `./references/schemas.json#/definitions/output` | Validate Wins/Blockers/Financial Health completeness. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable morning sync workflow. |

## Progressive Disclosure References
- Advanced synthesis logic: `./advanced/advanced.md`
- Briefing interfaces: `./references/api-specs.md`
- Known anti-patterns: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
