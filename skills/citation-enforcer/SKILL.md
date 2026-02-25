---
name: citation-enforcer
description: "Enforces evidence-first reasoning by requiring source attribution for every material claim."
usage_trigger: "Use when outputs require high trust and each claim must be linked to Memory, Search, or File evidence."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [reasoning, evidence, citations]
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
dependencies: [memory]
permissions: [fs_read, fs_write]
scope_out: ["Do not emit unsupported claims", "Do not use citation placeholders without source pointers"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# citation-enforcer

## Decision Tree (Fail-Fast & Persistence)
0. Resume any active citation task from `.workdir/tasks/*/state.jsonl`.
1. Identify every material claim in the target output.
2. Intelligence floor check against frontmatter engine.
3. Tooling policy check (native cli, cli wrapper, direct api, mcp).
4. Classify as specialist or generalist and use JIT if generalist.
5. Require citation source type for each claim: Memory, Search, or File.
6. Fail if any claim lacks verifiable evidence pointer.

## Rules

### Scope-In
- Build an evidence ledger for every claim.
- Attach source pointers and confidence labels.
- Block finalization if evidence chain is incomplete.

### Scope-Out
- Do not allow uncited factual statements.
- Do not accept circular citations (claim cites derived summary without base source).
- Do not merge multiple claims into one citation unless all are supported.

### Tooling Protocol (CLI-First)
1. **Level 1 - Native CLI**: Use native cli for file evidence collection.
2. **Level 2 - CLI Wrapper Scripts**: Use cli wrapper scripts for citation extraction and normalization.
3. **Level 3 - Direct API**: Direct api only under exception policy.
4. **Level 4 - MCP**: Use mcp only for persistent background services.

### Internal Persistence (Zero-Copy / Flat-File)
- Save checkpoints in `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save claim ledger to a task-local flat file.
- Use seek-based evidence lookup for updates.

### Smart JIT Tool Loading (Mitigated)
- JIT activates for generalist or >10 tools.
- Call `get_tool_details` and cache schemas + capability summaries.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse draft output and enumerate factual claims.
2. Label profile as specialist or generalist.
3. Load tool details if generalist.
4. Validate input contract.
5. Checkpoint `INITIALIZED`.

### Phase 2: Evidence Mapping
6. For each claim, resolve source type (Memory/Search/File).
7. Create evidence pointer and confidence level.
8. Reject claims with missing or weak evidence.
9. Checkpoint `IN_PROGRESS`.

### Phase 3: Drafting & Gate
10. Produce cited draft with inline or table-form citations.
11. If unresolved claims remain, checkpoint `PENDING_APPROVAL` and stop.

### Phase 4: Finalization
12. Emit final claim-evidence matrix.
13. Validate output contract and checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
14. Append ledger summary.
15. Write trace log and update old-patterns with missed-citation failures.

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `claim_set` | `./references/schemas.json#/definitions/input` | Validate claims requiring citation. |
| **Output** | `citation_report` | `./references/schemas.json#/definitions/output` | Validate coverage of evidence per claim. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist citation progress. |

## Progressive Disclosure References
- Advanced evidence handling: `./advanced/advanced.md`
- Citation schema: `./references/api-specs.md`
- Failure archive: `./references/old-patterns.md`
- Change history: `./references/changelog.md`
