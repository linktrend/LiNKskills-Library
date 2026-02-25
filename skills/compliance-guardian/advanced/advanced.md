# Advanced Execution Logic

## Policy Drift Handling
- If policy snapshot appears stale, downgrade confidence and request refresh before pass.
- Track high-risk policy classes separately (medical, finance, political).

## Disclosure Placement
- Enforce platform-appropriate disclosure locations (title/description/overlay).
- Reject ambiguous disclosure wording.
