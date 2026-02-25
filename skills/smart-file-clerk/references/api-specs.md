# API & Tool Technical Specifications

## Hybrid Storage Model
- Active retrieval (RAG): Supabase Buckets.
- Deep archive: Google Drive.

## OCR Requirement
- Financial and legal documents in Supabase must pass OCR indexing.
- Financial document extraction should align to `/shared/templates/MASTER_FINANCE_TEMPLATES.md`.

## Output
- Storage action summary plus OCR index metadata for retrieval.
