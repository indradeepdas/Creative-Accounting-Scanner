# Using Quarterly Red Flag Scanner

This guide explains what to upload, what each scanner module does, and how to ask Codex to run one scanner, a selected group, or the full scanner set.

The skill also supports a Codex-native retrieval flow. If the user gives a ticker or company name instead of uploaded documents, Codex should try to retrieve primary-source filings and disclosures before running scanners. See [codex-native-filing-retrieval.md](codex-native-filing-retrieval.md).

## What To Upload

The scanner can run on a single document, but it becomes much more useful when the user supplies documents that let Codex compare the income statement, balance sheet, cash-flow statement, notes, and management commentary across periods.

## Minimum Useful Package

Upload at least one of the following:

- Current quarterly report or interim financial statements.
- Current earnings release with financial statements.
- Current investor presentation with reported and adjusted metrics.

With only one current-period document, Codex should run a limited scan, state that confidence is lower, and list the missing documents needed for stronger conclusions.

## Recommended Package For A Normal Review

For a practical earnings-quality review, upload:

- Current quarterly report or interim financial statements.
- Current earnings release.
- Current investor presentation, if management uses one.
- Prior-year quarter report.
- Prior quarter report.
- Latest annual report, especially when quarterly notes are condensed.
- Any adjusted metric reconciliation included in releases or presentations.

This package usually supports the full scanner set because it provides current results, comparisons, notes, cash flow, and management's own framing.

## Best Package For A Full Memo

For the strongest analysis, upload:

- Current quarterly report or interim financial statements.
- Prior quarter, prior-year quarter, and latest annual report.
- Earnings release.
- Investor presentation.
- Earnings call transcript or prepared remarks.
- Segment tables and KPI schedules.
- Non-GAAP or adjusted metric reconciliations.
- Debt covenant, liquidity, or refinancing disclosures where relevant.
- Restatement, remediation, impairment, restructuring, or going-concern disclosures where relevant.

## Helpful Documents By Scanner

Scanner | Most Helpful Documents
--- | ---
Revenue quality | Quarterly report, revenue note, segment revenue table, contract asset and deferred revenue note, earnings release, prior periods.
Customer balance quality | Balance sheet, receivables note, allowance rollforward if available, contract asset and liability note, customer concentration disclosure.
Expense timing and capitalization | Cash-flow statement, capitalized cost notes, software or contract cost policy, PP&E and intangible notes, amortization detail.
Asset quality | Balance sheet, inventory note, impairment note, goodwill and intangible note, deferred tax note, segment performance tables.
Liability completeness | Accrued expense detail, provision rollforwards, warranty and return notes, contingency notes, deferred revenue, debt and lease notes.
Income-statement presentation | Current and prior income statements, segment profit tables, line-item notes, restructuring and impairment notes, management commentary.
Adjusted metric quality | Earnings release, investor presentation, non-GAAP reconciliation, adjusted EBITDA or adjusted EPS definitions, prior-period reconciliations.
Cash-flow quality | Cash-flow statement, working-capital lines, capital expenditures, nonrecurring cash items, receivable sale or factoring disclosure.
Working-capital quality | Balance sheet, cash-flow statement, receivables, inventory, payables, accrued expenses, contract balances, prior-period data.
Disclosure change detection | Current and prior filings, prior investor presentation, prior metric definitions, latest annual report, segment disclosures.
Related-party and off-balance-sheet review | Related-party note, commitments and contingencies, guarantees, lease notes, variable interest entity notes, factoring or supplier-finance disclosures.

## Documents That Reduce Common Blind Spots

Upload these when available:

- Prior-period filings, because many red flags require trend comparison.
- Full cash-flow statement, because earnings quality cannot be assessed from income alone.
- Notes to the financial statements, because key risks often sit in accounting policies, estimates, and rollforwards.
- Adjusted metric reconciliations, because headline adjusted metrics can differ materially from GAAP measures and cash flow.
- Segment data, because consolidated results can hide divergent business-unit trends.
- Earnings call transcript, because management questions often come from gaps between commentary and the statements.

## How To Invoke The Skill

Use natural language. Codex should infer the scanner set from the documents and requested output, but explicit scanner names work best when the user wants a targeted review.

If you want Codex to retrieve documents first, say so directly:

```text
Retrieve the latest 10-Q, latest 10-K, current earnings release, and investor presentation for this ticker, then run all 11 scanners.
```

If retrieval is not available in the current Codex session, upload the documents listed above.

## Run All Scanners

Use this when uploading a quarterly report plus prior periods:

```text
Use Quarterly Red Flag Scanner on these documents. Run all 11 scanner modules and produce a full earnings-quality red-flag memo with an evidence table, scorecard, management questions, and limitations.
```

Short version:

```text
Run the full scanner set on this quarter.
```

Codex should run:

- Revenue quality.
- Customer balance quality.
- Expense timing and capitalization.
- Asset quality.
- Liability completeness.
- Income-statement presentation.
- Adjusted metric quality.
- Cash-flow quality.
- Working-capital quality.
- Disclosure change detection.
- Related-party and off-balance-sheet review.

## Run A Limited Scan

Use this when only an earnings release or presentation is available:

```text
Run a limited scan using the available earnings release and presentation. Focus on revenue quality, adjusted metric quality, cash-flow quality if cash flow is disclosed, income-statement presentation, and missing evidence.
```

Codex should avoid pretending that unavailable notes, balance-sheet schedules, or prior-period data were reviewed.

## Run A Single Scanner

Use the scanner name directly:

```text
Use only the Revenue Quality Scanner. Compare revenue growth with receivables, contract assets, deferred revenue, cash flow, and management commentary.
```

Other examples:

```text
Use the Adjusted Metric Quality Scanner on this earnings release.
```

```text
Use the Liability Completeness Scanner. Focus on provisions, contingencies, deferred revenue, warranties, and accrued expenses.
```

```text
Use the Disclosure Change Detection Scanner to compare this quarter with the prior quarter.
```

## Run A Scanner Group

Use scanner groups when the question is narrower than a full review but broader than one module.

Revenue and cash group:

```text
Run the revenue, customer balance, working-capital, and cash-flow scanners. I want to know whether reported revenue is converting into cash.
```

Margins and expense group:

```text
Run the expense timing, asset quality, income-statement presentation, and adjusted metric scanners. Focus on whether margin improvement is recurring.
```

Balance-sheet risk group:

```text
Run the asset quality, liability completeness, working-capital, and related-party/off-balance-sheet scanners. Focus on balances that could affect future periods.
```

Public-output group:

```text
Run the relevant scanners and draft a public case study. Keep it calm, evidence-led, non-accusatory, and include possible benign explanations.
```

## Request A Specific Output

Common output requests:

```text
Give me a quick scan with the top five red flags and management questions.
```

```text
Create the full red-flag memo using templates/red_flag_memo.md.
```

```text
Create only a scorecard by scanner module.
```

```text
Create a management-question list from the scanner findings.
```

```text
Create a public LinkedIn-style case study using only supplied public disclosures.
```

```text
Create a ratio table for revenue, receivables, inventory, payables, operating cash flow, adjusted EBITDA, and free cash flow.
```

## What Each Scanner Does

## 1. Revenue Quality

Purpose: Test whether reported revenue is supported by delivery, contract economics, customer demand, cash collection, and disclosures.

It inspects revenue growth, segment revenue, receivables, contract assets, deferred revenue, backlog, remaining performance obligations, return rights, rebates, discounts, customer acceptance, and management commentary.

Typical calculations include revenue growth, DSO, receivables growth minus revenue growth, contract assets as a percentage of revenue, deferred revenue movement, and operating cash flow divided by revenue.

Use it when revenue growth is central to the quarter, revenue recognition is judgment-heavy, or revenue grows faster than cash collection.

## 2. Customer Balance Quality

Purpose: Review receivables, contract assets, unbilled revenue, customer advances, deferred revenue, return obligations, and allowance accounts.

It asks whether customer balances are becoming harder to collect, less transparent, or less aligned with reported revenue. It is especially useful for subscription, reseller, distributor, long-term contract, milestone, and enterprise-sales models.

Typical calculations include DSO, receivables as a percentage of revenue, allowance as a percentage of gross receivables, bad debt expense as a percentage of average receivables, contract assets as a percentage of revenue, and deferred revenue growth versus revenue growth.

## 3. Expense Timing And Capitalization

Purpose: Assess whether costs are recognized currently or deferred into assets in a way that affects margins, operating income, or future expense burden.

It inspects capitalized software, contract acquisition costs, internal-use assets, PP&E, intangibles, amortization, depreciation, impairment, cash capital expenditures, and capitalization policies.

Typical calculations include capitalized costs as a percentage of revenue, amortization divided by average capitalized balance, implied amortization period, operating margin before and after capitalized additions, and free cash flow after capitalized recurring costs.

## 4. Asset Quality

Purpose: Review whether reported assets appear recoverable and supported by operating use or future cash flows.

It inspects receivables, contract assets, inventory, PP&E, goodwill, intangible assets, deferred tax assets, investments, fair value measurements, and other assets.

Typical calculations include asset growth versus revenue growth, inventory days, gross margin trend versus inventory growth, goodwill and intangibles as a percentage of equity or assets, deferred tax assets as a percentage of pre-tax income, and return on assets.

## 5. Liability Completeness

Purpose: Assess whether liabilities, accruals, provisions, deferred revenue, refund obligations, warranties, contingencies, and debt-related obligations appear complete relative to disclosed risks and operating activity.

It inspects accrued expenses, contract liabilities, warranty obligations, return and rebate reserves, restructuring provisions, litigation contingencies, leases, debt, and tax liabilities.

Typical calculations include accrued expenses as a percentage of operating expenses, warranty liabilities as a percentage of covered revenue, deferred revenue growth versus subscription or service revenue growth, provision releases as a percentage of operating income, and obligations relative to cash flow.

## 6. Income-Statement Presentation

Purpose: Evaluate whether classification, labels, subtotals, and line-item changes make recurring operating performance easier or harder to understand.

It inspects revenue presentation, gross margin, cost of revenue, operating expenses, operating income, other income, discontinued operations, restructuring, impairments, gains, and segment profit definitions.

Typical calculations include gross margin before and after reclassifications, operating margin excluding disclosed gains or recurring charges, other income as a percentage of pre-tax income, restructuring and impairment charges over time, and segment profit bridges.

## 7. Adjusted Metric Quality

Purpose: Review adjusted earnings, adjusted EBITDA, free cash flow, constant-currency metrics, segment measures, and other supplemental metrics for consistency and usefulness.

It inspects non-GAAP reconciliations, metric definitions, recurring exclusions, cash effects of adjustments, definition changes, and prominence of adjusted metrics versus GAAP measures.

Typical calculations include total adjustments as a percentage of GAAP net income or operating income, recurring adjustments over four quarters, adjusted EBITDA to operating cash flow, adjusted net income to GAAP net income, and free cash flow after capitalized recurring costs.

## 8. Cash-Flow Quality

Purpose: Assess whether operating cash flow supports reported earnings after considering working-capital timing, unusual cash items, classification, and capitalized recurring costs.

It inspects operating cash flow, net income, noncash charges, receivables, inventory, payables, accrued expenses, contract balances, investing cash flow, financing cash flow, and free cash flow.

Typical calculations include operating cash flow divided by net income, operating cash flow divided by adjusted EBITDA, adjusted operating cash flow excluding unusual cash items, free cash flow after capital expenditures and capitalized recurring costs, and working-capital contribution to operating cash flow.

## 9. Working-Capital Quality

Purpose: Review current operating accounts to assess whether near-term performance is supported or strained by working-capital timing.

It inspects receivables, inventory, prepaids, payables, accrued expenses, deferred revenue, contract liabilities, and other current accounts.

Typical calculations include DSO, inventory days, days payable outstanding, cash conversion cycle, working capital as a percentage of revenue, change in working capital as a percentage of operating cash flow, and contract liabilities as a percentage of revenue.

## 10. Disclosure Change Detection

Purpose: Identify changes in wording, metric definitions, segment structure, accounting policies, risk language, and table availability that may affect comparability.

It compares current and prior filings, earnings releases, presentations, accounting policies, critical estimates, revenue notes, segment tables, risk factors, liquidity discussion, and non-GAAP definitions.

Typical work includes logging old versus new wording, identifying missing tables, reconstructing trends under old and new definitions where possible, and asking whether the change reduces comparability in a sensitive area.

## 11. Related-Party And Off-Balance-Sheet Review

Purpose: Review disclosed related-party transactions, unconsolidated entities, guarantees, purchase commitments, leases, receivable sales, supplier financing, and other arrangements that may affect earnings quality or risk outside headline metrics.

It inspects related-party notes, variable interests, guarantees, commitments, leases, receivable sales, factoring, securitization, supplier financing, customer concentration, and unusual counterparty arrangements.

Typical calculations include related-party revenue or expense as a percentage of total revenue or expense, related-party receivables as a percentage of total receivables, guarantees and commitments as a percentage of equity and operating cash flow, receivables sold as a percentage of operating cash flow, and supplier-finance balances as a percentage of payables.

## Choosing The Right Scanner Set

Question | Suggested Scanner Set
--- | ---
"Is revenue converting to cash?" | Revenue quality, customer balance quality, working-capital quality, cash-flow quality.
"Are margins sustainable?" | Expense timing and capitalization, income-statement presentation, adjusted metric quality, asset quality.
"Could balance-sheet movements affect future quarters?" | Asset quality, liability completeness, working-capital quality.
"Are management's adjusted numbers helpful?" | Adjusted metric quality, income-statement presentation, cash-flow quality.
"Did the disclosure change?" | Disclosure change detection plus any scanner affected by the changed disclosure.
"Are there hidden obligations or unusual arrangements?" | Related-party and off-balance-sheet review, liability completeness, cash-flow quality.
"I want a full review." | Run all 11 scanners.

## Expected Codex Behavior

Codex should:

- Ask for missing period context when needed.
- Run the selected scanner files directly rather than inventing a new framework.
- State which scanners were run and which were skipped.
- Explain skipped scanners by missing evidence.
- Produce calculations where data permits.
- Separate facts, interpretations, benign explanations, and questions.
- Avoid legal conclusions, accusations, and investment recommendations.
