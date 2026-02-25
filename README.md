# LiNKskills Library

LiNKskills Library is the Venture Studio's agent operating system.

For all operating procedures, security rules, execution standards, and full catalog coverage, use the master manual:

- **Source of Truth SOP:** [`SOP.md`](./SOP.md)

## Quick Links
- Operator guide: [`OPERATOR_BRIEFING.md`](./OPERATOR_BRIEFING.md)
- Agent conventions: [`AGENT.md`](./AGENT.md)
- Machine SOP: [`SOP_MACHINE.md`](./SOP_MACHINE.md)
- Human SOP: [`SOP_HUMAN.md`](./SOP_HUMAN.md)
- Command manual: [`COMMAND_REFERENCE.md`](./COMMAND_REFERENCE.md)
- Skills/tools catalog: [`SKILLS_CATALOGUE.md`](./SKILLS_CATALOGUE.md)
- Finance templates: [`shared/templates/MASTER_FINANCE_TEMPLATES.md`](./shared/templates/MASTER_FINANCE_TEMPLATES.md)
- Catalog and versions: [`manifest.json`](./manifest.json)
- Full validation: [`validator.py`](./validator.py)
- Health analytics: [`global_evaluator.py`](./global_evaluator.py)

## Core Commands
- Validate registry:
  - `python3 validator.py --repo-root . --scan-all`
- Validate one target:
  - `python3 validator.py --repo-root . --path skills/<skill-name>`

## Security Prerequisite
- `export LSL_MASTER_KEY="<your-master-key>"`
