# Example Trace: Error Recovery

## Scenario
Playwright snapshot command fails on first attempt.

## Recovery
- Skill logs failure and retries with stable viewport settings.
- Retry succeeds; audit continues.
- State checkpoint reflects recovery path and retains trace for review.
