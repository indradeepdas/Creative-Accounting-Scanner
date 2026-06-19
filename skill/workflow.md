# Workflow

## 1. Frame The Assignment

Identify the company, period, document set, and requested output. If the user provides only one document, state that comparisons will be limited. If the user asks for a public post, apply public-output safeguards from the beginning.

If the user gives a ticker, company name, CIK, or asks Codex to retrieve filings, use `document_acquisition.md` before extraction. Prefer a dedicated filings connector when available, then official SEC EDGAR public data for U.S. registrants, then company investor-relations pages, then user-uploaded files.

Create a document manifest before scanning so the output can distinguish retrieved documents from user-supplied documents.

## 2. Build A Period Table

Create a normalized table for current quarter, prior quarter, prior-year quarter, current year-to-date, prior-year year-to-date, and trailing 12 months where possible.

At minimum, try to capture:

- Revenue.
- Gross profit.
- Operating income.
- Net income.
- Adjusted EBITDA or other adjusted metrics.
- Operating cash flow.
- Capital expenditures.
- Accounts receivable or contract assets.
- Inventory.
- Deferred revenue or contract liabilities.
- Accrued expenses and provisions.
- Debt and covenant metrics when disclosed.

## 3. Run Scanner Modules

Run the modules that match the available evidence. For a full quarterly filing, run every scanner. For an earnings release, prioritize revenue quality, adjusted metric quality, cash-flow quality, and presentation. For an investor presentation, emphasize metric definitions, reconciliation quality, and consistency with filed statements.

If the user requests a named scanner, run that scanner directly and use other modules only when they are necessary to triangulate the finding. If the user requests "all scanners" or "full scan", run all 11 modules and list unavailable tests caused by missing documents.

For common groups:

- Revenue-to-cash: revenue quality, customer balance quality, working-capital quality, cash-flow quality.
- Margin sustainability: expense timing and capitalization, income-statement presentation, adjusted metric quality, asset quality.
- Balance-sheet risk: asset quality, liability completeness, working-capital quality, related-party and off-balance-sheet review.
- Disclosure comparability: disclosure change detection plus any scanner affected by the changed disclosure.

## 4. Triangulate

For each signal, ask:

- Does the income-statement trend agree with cash collection?
- Do balance-sheet movements support the reported performance?
- Do note disclosures explain the movement?
- Does management commentary match the numbers?
- Is the pattern repeated, worsening, or isolated?

## 5. Score And Calibrate

Assign severity, evidence strength, materiality, recurrence, and confidence. Lower confidence when data is missing, seasonality is unresolved, a business-model change is plausible, or only management-adjusted metrics are available.

## 6. Draft The Output

Use the requested template. Keep the writing direct and evidence-led. Avoid legal conclusions and investment language.

## 7. Legal-Safety Pass

Replace loaded language with neutral alternatives:

- "may warrant further review" instead of "shows misconduct"
- "not supported by the documents reviewed" instead of "false"
- "the disclosure does not explain" instead of "management hid"
- "possible reporting pressure" instead of "intent"

Add what evidence would reduce concern.
