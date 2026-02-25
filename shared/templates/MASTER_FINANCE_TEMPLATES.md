# MASTER FINANCE TEMPLATES

GAAP-standard reporting templates for the LiNKskills Studio Controller layer.

## 1. Profit & Loss (P&L)
| Period | Revenue | COGS | Gross Profit | Operating Expenses | EBITDA | Net Income |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| YYYY-MM | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## 2. Balance Sheet
### Assets
| Category | Current | Prior |
| :--- | ---: | ---: |
| Cash & Equivalents | 0.00 | 0.00 |
| Accounts Receivable | 0.00 | 0.00 |
| Fixed Assets | 0.00 | 0.00 |
| Total Assets | 0.00 | 0.00 |

### Liabilities & Equity
| Category | Current | Prior |
| :--- | ---: | ---: |
| Accounts Payable | 0.00 | 0.00 |
| Debt | 0.00 | 0.00 |
| Owner Equity | 0.00 | 0.00 |
| Total Liabilities + Equity | 0.00 | 0.00 |

## 3. Cash Flow Statement
| Period | Operating Cash Flow | Investing Cash Flow | Financing Cash Flow | Net Cash Change |
| :--- | ---: | ---: | ---: | ---: |
| YYYY-MM | 0.00 | 0.00 | 0.00 | 0.00 |

## 4. Accounts Receivable (AR) Aging
| Customer | Invoice ID | Amount | Current | 1-30 Days | 31-60 Days | 61+ Days |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Example Co. | INV-001 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## 5. Accounts Payable (AP) Aging
| Vendor | Bill ID | Amount | Current | 1-30 Days | 31-60 Days | 61+ Days |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Example Vendor | BILL-001 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## 6. Budget vs Actual
| Department | Budget | Actual | Variance | Variance % | Owner Action |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Marketing | 0.00 | 0.00 | 0.00 | 0.00% | N/A |

## 7. Transaction Ledger (Canonical)
| transaction_id | source | type | amount | currency | timestamp | counterparty | reference |
| :--- | :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| TXN-0001 | stripe | revenue | 0.00 | USD | YYYY-MM-DDTHH:MM:SSZ | Customer | INV-0001 |

## 8. Report Metadata
| Field | Value |
| :--- | :--- |
| Report Generated At | YYYY-MM-DDTHH:MM:SSZ |
| Prepared By | studio-controller |
| Data Window | YYYY-MM-DD to YYYY-MM-DD |
| Data Sources | revenue-adapter-base, vault_expenses, lsl_finance |
