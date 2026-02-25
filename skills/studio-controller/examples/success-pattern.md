# Example Trace: Success Pattern

## Scenario
Monthly close requires consolidated reporting across Stripe and expense systems.

## Trace
- Skill reconciles normalized revenue with expense records.
- Produces GAAP bundle and logs canonical transactions in `lsl_finance`.
- Returns successful reconciliation status and report package.
