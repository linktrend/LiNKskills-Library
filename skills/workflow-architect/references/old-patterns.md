# Old Patterns (Known-Bad)

- Creating workflows without prior contract validation causes malformed nodes.
- Triggering before activation produces false negatives in deployment tests.
- Embedding credentials in node JSON is forbidden; use vault-managed secrets.
