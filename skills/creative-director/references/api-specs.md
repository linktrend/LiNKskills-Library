# API & Tool Technical Specifications

## Inputs
- Marketing brief and campaign objective.
- Target channels and asset formats.
- n8n workflow identifiers.

## Outputs
- Asset order package:
  - Script order
  - Thumbnail order
  - Post order
- Trigger manifest for `n8n-bridge` execution.

## Trigger Rule
- Rendering workflows are invoked through `n8n-bridge` using validated JSON payloads.
