# API & Tool Technical Specifications

## Inputs
- `PROGRESS.md` files from active lead-engineer and QA streams.
- `lsl_memory.audit_logs` slice for report window.

## Output
- Venture Studio Health Report (Markdown) with:
  - Delivery velocity indicators
  - Quality and blocker trends
  - Risk summary and recommended actions

## Data Rule
- Every reported claim must map to at least one source record.
