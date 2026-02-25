---
name: workflow-architect
description: "Designs, creates, activates, and validates n8n workflows from structured task requirements."
usage_trigger: "Use when a user needs to design or update an n8n workflow and activate/test it automatically."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-24
author: LiNKskills Library
tags: [workflow, n8n, automation]
engine:
  min_reasoning_tier: balanced
  preferred_model: gpt-4.1
  context_required: 128000
tooling:
  policy: cli-first
  jit_enabled_if: generalist_or_gt10_tools
  jit_tool_threshold: 10
  require_get_tool_details: true
tools: [write_file, read_file, list_dir, get_tool_details]
dependencies: [n8n]
permissions: [fs_read, fs_write, api_access]
scope_out: ["Do not deploy unreviewed production automations without explicit user consent", "Do not store plaintext secrets in workflow JSON"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-24
---

# workflow-architect

## Decision Tree (Fail-Fast & Persistence)
0. **Resume Check**: Is this request linked to an existing `task_id` in `execution_ledger.jsonl`?
   - YES: Resume from latest checkpoint in `.workdir/tasks/<task_id>/state.jsonl`.
   - NO: Generate a new task id `YYYYMMDD-HHMM-WORKFLOWARCHITECT-<SHORTUNIX>`.
1. **Intelligence Floor Check**: Verify runtime satisfies frontmatter `engine` constraints.
   - FAIL: Stop and report required reasoning/context floor.
2. **Tooling Protocol Check**: Validate plan follows native cli, cli wrapper, direct api, and mcp policy.
   - FAIL: Refactor plan before execution.
3. **Profile Check**: Classify workload as Specialist or Generalist.
   - Specialist: single automation domain and <=10 tools.
   - Generalist: multi-domain automation or >10 tools.
4. **JIT Check**: If Generalist, call `get_tool_details`, cache tool schemas in task state, then continue.
5. **Contract Check**: Validate input against `./references/schemas.json#/definitions/input`.
6. **Pattern Check**: Review `./references/old-patterns.md` before execution.

## Rules

### Scope-In
- Design workflow JSON for n8n based on explicit trigger/action/outcome requirements.
- Create workflow using `/tools/n8n/bin/n8n create`.
- Activate and test workflow using `/tools/n8n/bin/n8n activate` and `/tools/n8n/bin/n8n trigger`.

### Scope-Out
- Do not hardcode secrets in workflow definitions.
- Do not silently modify unrelated workflows.
- Do not skip state checkpointing.

### Tooling Protocol (CLI-First)
1. **Level 1 - Native CLI**: Use native cli for file navigation and JSON sanity checks.
2. **Level 2 - CLI Wrapper**: Prefer CLI wrapper tools (`/tools/n8n/bin/n8n`) for workflow API logic.
3. **Level 3 - Direct API**: Use direct api only if wrapper lacks required endpoint behavior.
4. **Level 4 - MCP**: Use mcp only for persistent session-based workflow operations.

### Internal Persistence (Zero-Copy / Flat-File)
- Append checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl` after each phase.
- Save generated workflow JSON to `.workdir/tasks/{{task_id}}/workflow.json`.
- Future phases must seek specific keys from state artifacts, not reload full context.

### Smart JIT Tool Loading (Mitigated)
- JIT activates only for Generalist or >10 tools.
- When JIT is active, run `get_tool_details` and cache results under task-local state.
- Each cached entry must include a one-sentence capability summary to reduce planning blind spots.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse user requirements: trigger, inputs, actions, outputs, error policy.
2. Determine Specialist vs Generalist profile.
3. If Generalist, fetch tool details with `get_tool_details` and cache schemas.
4. Validate request payload with Input Contract.
5. Checkpoint state with `status: INITIALIZED`.

### Phase 2: Design & Transformation
6. Build canonical n8n workflow JSON skeleton.
7. Add nodes, connections, retries, and failure branches.
8. Validate draft against Output Contract semantics.
9. Save draft to task-local `workflow.json` and checkpoint `status: IN_PROGRESS`.

### Phase 3: Create Workflow
10. Post JSON through `/tools/n8n/bin/n8n create --workflow-json ...`.
11. Persist returned workflow id and API response metadata in `state.jsonl`.
12. If creation fails, checkpoint `FAILED`, log root cause, and stop.

### Phase 4: Activate & Test (Resume Point)
13. Activate workflow using `/tools/n8n/bin/n8n activate --workflow-id ...`.
14. Trigger test payload using `/tools/n8n/bin/n8n trigger --workflow-id ... --payload-json ...`.
15. Validate test result against Output Contract and checkpoint `COMPLETED`.

### Phase 5: Self-Correction & Auditing
16. Append execution summary to `execution_ledger.jsonl`.
17. Save raw API outputs and validation notes to `.workdir/tasks/{{task_id}}/trace.log`.
18. Update `./references/old-patterns.md` with any new known-bad design or activation pattern.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `/tools/n8n/bin/n8n` | Phases 3-4 | Must create before activate; must activate before trigger. |
| `write_file` | All | Required for checkpoints and workflow artifact persistence. |
| `get_tool_details` | Phase 1+ | Mandatory for Generalist/JIT profile and cached locally. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `workflow_request` | `./references/schemas.json#/definitions/input` | Requirement integrity validation. |
| **Output** | `workflow_result` | `./references/schemas.json#/definitions/output` | Creation/activation/test result validation. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Resumable task checkpointing. |

## Progressive Disclosure References
- Advanced edge cases: `./advanced/advanced.md`
- API behavior: `./references/api-specs.md`
- Failure history: `./references/old-patterns.md`
- Change history: `./references/changelog.md`
