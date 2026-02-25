# API & Tool Technical Specifications

## Supported Sources
- YouTube views monetization extracts.
- AdSense revenue extracts.
- Stripe billing/transaction exports.

## Canonical Output
- Venture Studio Transaction format fields:
  - `transaction_id`
  - `source`
  - `amount`
  - `currency`
  - `timestamp`
  - `reference`

## Rule
- Final output must only include canonical transaction objects, with source traceability.
