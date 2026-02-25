# Example Trace: Success Pattern

## Scenario
Finance needs one normalized ledger from Stripe and AdSense exports.

## Trace
- Skill ingests both payloads and maps source fields to canonical schema.
- Produces Venture Studio Transaction objects with required fields.
- Final output passes contract validation.
