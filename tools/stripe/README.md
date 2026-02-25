# stripe

## Capability Summary
Stripe billing operations wrapper for LiNKskills. Uses vault-managed credentials to query invoice activity for venture finance workflows.

## Commands
- `list-invoices`
  - List invoice records with status, amount, currency, and customer fields.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/stripe list-invoices --limit 20`
- `bin/stripe list-invoices --status open --limit 50`

## Vault Keys
- `STRIPE_API_KEY`
