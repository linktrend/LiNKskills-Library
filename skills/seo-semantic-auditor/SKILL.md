---
name: seo-semantic-auditor
description: "Reverse-engineers competitor keyword strategies using research tiers (Brave/Exa) and outputs prioritized content gaps for content operations."
usage_trigger: "Use when SEO strategy requires competitor semantic mapping and a ranked content gap backlog."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [seo, semantic, content]
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
dependencies: [research, search-strategy]
permissions: [fs_read, fs_write, api_access]
scope_out: ["Do not output keyword insights without source support", "Do not skip prioritized content gap ranking"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# seo-semantic-auditor

## Decision Tree (Fail-Fast & Persistence)
0. Resume from `.workdir/tasks/*/state.jsonl` when available.
1. Validate competitor set and domain scope.
2. Require explicit research intent before external retrieval.
3. Validate intelligence floor from `engine`.
4. Validate tooling protocol: native cli, cli wrapper, direct api, mcp.
5. Classify workflow as specialist or generalist.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Start with Brave (`web` tier), escalate to Exa (`neural` tier) when confidence is low.
8. Fail-fast if prioritized content gaps are not produced.

## Rules

### Scope-In
- Reverse-engineer competitor keyword and topic clusters.
- Build prioritized content gaps for content creation teams.
- Provide source-backed strategic rationale for each gap.

### Scope-Out
- Do not produce unsourced rankings.
- Do not skip tiered escalation logic.
- Do not finalize without contract validation.

### Tooling Protocol (CLI-First)
1. Level 1 - Native CLI: prepare competitor/domain input set.
2. Level 2 - CLI Wrapper Scripts: use research wrapper commands by default.
3. Level 3 - Direct API: exception-only for unsupported retrieval behavior.
4. Level 4 - MCP: only for persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save semantic maps and rankings as task-local files.
- Use seek-based reads for targeted cluster lookups.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for `Generalist` or >10 tools.
- Call `get_tool_details` and cache capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse competitor domains, target topics, and geo/language context.
2. Draft research intent with confidence thresholds.
3. Determine specialist/generalist profile and JIT setup.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Logic & Reasoning
6. Query Brave-first for baseline keyword landscape.
7. Escalate to Exa when confidence or coverage is insufficient.
8. Build competitor semantic map and opportunity matrix.
9. Rank content gaps by business impact and ranking difficulty.

### Phase 3: Drafting & Asynchronous Gate
10. Draft prioritized content-gap output for content team.
11. If evidence quality is insufficient, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize ranked gap list and supporting rationale.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Append summary to `execution_ledger.jsonl`.
16. Save trace payloads to `.workdir/tasks/{{task_id}}/trace.log`.
17. Update `references/old-patterns.md` with retrieval/ranking lessons.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `/tools/research/bin/research` | Phases 2-4 | Use Brave first, escalate to Exa when low confidence. |
| `write_file` | All | Persist rankings, checkpoints, and working artifacts. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `seo_audit_request` | `./references/schemas.json#/definitions/input` | Validate competitor and target-topic context. |
| **Output** | `content_gap_report` | `./references/schemas.json#/definitions/output` | Validate prioritized content gaps and evidence mappings. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable SEO audit flow. |

## Progressive Disclosure References
- Advanced heuristics: `./advanced/advanced.md`
- Retrieval specs: `./references/api-specs.md`
- Failure memory: `./references/old-patterns.md`
- Version history: `./references/changelog.md`
