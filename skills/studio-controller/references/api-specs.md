# API & Tool Technical Specifications

## GAAP Coverage
- Profit & Loss
- Balance Sheet
- Cash Flow
- AR/AP Aging
- Budget vs Actual

## Template Source
- `/shared/templates/MASTER_FINANCE_TEMPLATES.md`

## Source Integration
- Revenue: `revenue-adapter-base` normalized feeds (YouTube/Stripe).
- Expenses: Vault-backed expense extracts.

## Database Requirement
- All financial transaction records must be logged to Supabase `lsl_finance` schema.
