# shopify

## Capability Summary
Shopify commerce operations wrapper for LiNKskills. Uses vault-managed credentials to read product catalog data for venture operations.

## Commands
- `list-products`
  - List product records from Shopify Admin API.

## CLI
- `--help`
- `--version`
- `--json`

## Usage
- `bin/shopify list-products --limit 50`

## Vault Keys
- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_STORE_DOMAIN`
