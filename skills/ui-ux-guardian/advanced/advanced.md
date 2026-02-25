# Advanced Execution Logic

## Visual Drift Classes
- Token drift: color/spacing/typography values diverge from design system constants.
- Component drift: layout structure matches, but state styling diverges.
- Responsive drift: mobile/tablet breakpoints introduce off-grid behavior.

## Audit Escalation
- If diff exceeds threshold and touches core layout primitives, mark critical and require approval.
- If only cosmetic and isolated, provide fix list and keep execution in-progress.

## Resilience
- When screenshot capture fails, retry once with stable viewport and network-idle wait.
