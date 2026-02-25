# API & Tool Technical Specifications

## Required Inputs
- `factory.json`: routing table with lane owners and capability tags.
- PRD text/document: objective, constraints, acceptance criteria.

## Required Outputs
- Routed packet list with owner, dependencies, and acceptance criteria.
- `sessions_spawn` list with bounded scope and rollback path.

## Interfaces
- `read_file`: load PRD and route table.
- `write_file`: persist checkpoints and plan artifacts.
- `get_tool_details`: fetch runtime capability schemas for generalist plans.
