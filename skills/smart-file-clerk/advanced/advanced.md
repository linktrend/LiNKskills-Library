# Advanced Execution Logic

## Routing Priority
- Prioritize active RAG placement for documents accessed within recent windows.
- Relegate stale/low-query documents to deep archive with retrieval pointers.

## OCR Reliability
- Retry OCR on low-confidence scans before archiving final text index.
- Preserve page-level confidence metadata for downstream QA.
