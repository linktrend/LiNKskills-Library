# Example Trace: Error Recovery

## Scenario
OCR fails on a scanned legal contract.

## Recovery
- Skill records failure and retries OCR pipeline.
- If confidence remains low, sets `PENDING_APPROVAL` with remediation options.
