# Advanced Execution Logic

## Mapping Edge Cases
- Convert non-currency metrics (e.g., views) using configured monetization rules before normalization.
- Preserve source-native IDs in `reference` for audit traceability.

## Reconciliation Controls
- Detect duplicate transaction IDs across sources.
- Flag outlier amounts for manual finance review.
