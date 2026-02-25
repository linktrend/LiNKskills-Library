---
name: devops-sre
description: "DevOps/SRE persona skill for automated Dockerization, VPS deployment hardening, and secure LSL_MASTER_KEY propagation."
usage_trigger: "Use when packaging services for container deployment, preparing VPS rollout, and validating secure runtime injection policies."
version: 1.0.0
release_tag: v1.0.0
created: 2026-02-25
author: LiNKskills Library
tags: [devops, sre, deployment]
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
dependencies: [docker, vps]
permissions: [fs_read, fs_write, shell_exec]
scope_out: ["Do not ship deployment plans without rollback path", "Do not allow production deployment without LSL_MASTER_KEY verification"]
persistence:
  required: true
  state_path: ".workdir/tasks/{{task_id}}/state.jsonl"
last_updated: 2026-02-25
---

# devops-sre

## Decision Tree (Fail-Fast & Persistence)
0. Resume from `.workdir/tasks/*/state.jsonl` when continuation exists.
1. Validate containerization target and deployment environment metadata.
2. Require explicit `LSL_MASTER_KEY` injection strategy for production.
3. Validate intelligence floor requirements.
4. Validate tooling order: native cli, cli wrapper, direct api, mcp.
5. Classify specialist or generalist deployment mode.
6. If generalist or >10 tools, call `get_tool_details` and cache schemas.
7. Fail fast when rollback or health-check plan is missing.

## Rules

### Scope-In
- Define Docker build/runtime strategy.
- Define VPS deployment sequence with health checks and rollback.
- Verify secure environment variable injection for `LSL_MASTER_KEY`.

### Scope-Out
- Do not approve production rollout without key injection checks.
- Do not omit observability and rollback paths.
- Do not bypass contract validation for deployment artifacts.

### Tooling Protocol (CLI-First)
1. Level 1: native cli for docker/system checks.
2. Level 2: cli wrapper scripts for deterministic deploy steps.
3. Level 3: direct api for exceptional infrastructure constraints only.
4. Level 4: mcp for long-running, persistent session services.

### Internal Persistence (Zero-Copy / Flat-File)
- Persist all checkpoints to `.workdir/tasks/{{task_id}}/state.jsonl`.
- Save deployment manifests and rollback docs as task-local flat files.
- Use seek reads for env injection evidence and health-check logs.

### Smart JIT Tool Loading (Mitigated)
- Activate JIT only for generalist or >10 tools.
- `get_tool_details` required for schema-aware deployment planning.

## Workflow

### Phase 1: Ingestion & Checkpointing
1. Parse service runtime requirements and VPS targets.
2. Load current Docker and deployment configuration.
3. Set specialist/generalist profile and JIT cache if needed.
4. Validate Input Contract.
5. Append `INITIALIZED` checkpoint.

### Phase 2: Container & Deployment Planning
6. Define Dockerfile/runtime profile and resource limits.
7. Define deploy sequence, health checks, and rollback commands.
8. Verify `LSL_MASTER_KEY` injection mechanism and secret handling policy.
9. Append `IN_PROGRESS` checkpoint.

### Phase 3: Drafting & Asynchronous Gate
10. Draft deploy plan and runbook.
11. If production risk remains high, set `PENDING_APPROVAL`.

### Phase 4: Finalization
12. Finalize deployment blueprint and security checks.
13. Validate Output Contract.
14. Append `COMPLETED` checkpoint.

### Phase 5: Self-Correction & Auditing
15. Log run summary to `execution_ledger.jsonl`.
16. Persist trace in task-local `trace.log`.
17. Update `references/old-patterns.md` with deployment failure lessons.

## Tools
| Tool Name | Workflow Scope | Critical Execution Rule |
| :--- | :--- | :--- |
| `read_file` | Phases 1-2 | Load Docker and deployment manifests before planning. |
| `write_file` | All | Save checkpoints and deployment runbooks. |
| `get_tool_details` | Phase 1+ | Required for generalist/JIT profile. |

## Contracts
| Direction | Artifact Name | Schema Reference | Purpose |
| :--- | :--- | :--- | :--- |
| **Input** | `deploy_request` | `./references/schemas.json#/definitions/input` | Validate service and environment requirements. |
| **Output** | `deployment_plan` | `./references/schemas.json#/definitions/output` | Validate rollout, health checks, and key injection policy. |
| **State** | `execution_state` | `./references/schemas.json#/definitions/state` | Persist resumable deployment workflow. |

## Progressive Disclosure References
- Edge-case logic: `./advanced/advanced.md`
- Deployment interfaces: `./references/api-specs.md`
- Failure memory: `./references/old-patterns.md`
- Version timeline: `./references/changelog.md`
