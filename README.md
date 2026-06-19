# Quarterly Red Flag Scanner

Quarterly Red Flag Scanner is an open-source Codex skill for structured earnings-quality review of listed-company quarterly reports. It helps users identify reporting patterns that may warrant further review across revenue quality, expense timing, asset quality, liability completeness, adjusted metrics, and operating cash-flow quality.

The skill is designed for analysts, investors, credit reviewers, journalists, students, and finance teams who need a disciplined way to read quarterly disclosures. It is most useful when the user supplies current and prior-period filings, earnings releases, interim financial statements, investor presentations, or management commentary.

## What It Does

- Reviews supplied public-company disclosures for earnings-quality red flags.
- Separates factual observations, calculations, interpretation, benign explanations, and missing evidence.
- Triangulates income statement performance against balance sheet movements, cash flow, accounting notes, and management commentary.
- Generates red-flag memos, scorecards, management questions, analyst workpapers, and calm public case-study drafts.
- Applies a legal-safety pass before producing public-facing language.

## What It Does Not Do

- It is not investment advice.
- It is not audit, accounting, tax, or legal advice.
- It is not a fraud detector.
- It does not accuse companies or managers of wrongdoing.
- It does not provide buy, sell, or hold recommendations.
- It does not replace independent verification, professional judgment, or access to complete company records.

## Using It As A Codex Skill

Place the repository where Codex can access it, then ask Codex to use the skill in `skill/SKILL.md`.

Example prompts:

- "Use Quarterly Red Flag Scanner to do a quick scan of this quarterly report."
- "Retrieve the latest 10-Q, latest 10-K, and current earnings release for this ticker, then run all 11 scanners."
- "Create a full earnings-quality memo for this quarter and compare it with the prior-year quarter."
- "Focus only on revenue quality and receivables. I want the evidence table and management questions."
- "Turn this analysis into a public case study. Keep it non-accusatory and avoid investment recommendations."
- "Build a ratio table for profit versus operating cash flow over the last eight quarters."
- "Run all 11 scanner modules and produce a full memo."
- "Run only the Revenue Quality Scanner and Customer Balance Quality Scanner."
- "Run the adjusted metric, income-statement presentation, and cash-flow scanners on this earnings release."

For detailed scanner descriptions, document-upload guidance, and invocation examples, see [docs/using-the-skill.md](docs/using-the-skill.md).

For Codex-native filing retrieval, connector fallback behavior, and SEC EDGAR workflow guidance, see [docs/codex-native-filing-retrieval.md](docs/codex-native-filing-retrieval.md).

## Codex-Native Filing Retrieval

The skill can work from uploaded documents, but a Codex-native workflow can start with a company name or ticker. When retrieval tools are available, Codex should gather primary-source filings first, build a document manifest, then run the scanners.

Preferred retrieval order:

- Use a dedicated SEC, EDGAR, filings, public-equity, or market-disclosure connector if available.
- For U.S. registrants, use official SEC EDGAR public data when no dedicated connector is available.
- Use company investor-relations pages for earnings releases, presentations, and transcripts.
- Fall back to user-uploaded documents when retrieval is unavailable.

Example:

```text
Use Quarterly Red Flag Scanner for AAPL. Retrieve the latest 10-Q, prior-year quarter 10-Q, latest 10-K, and current earnings release from primary sources, then run all 11 scanners and create a red-flag memo.
```

## Recommended Inputs

Minimum useful input:

- One current quarterly report, interim financial statement package, earnings release, or investor presentation.

Best results require:

- Current quarterly report or interim financial statements.
- Prior-year quarter and prior quarter where available.
- Earnings release and investor presentation.
- Cash-flow statement and working-capital detail.
- Segment data, accounting policy notes, and critical estimate disclosures.
- Adjusted metric reconciliations.
- Any restatement, remediation, covenant, or going-concern disclosures.

When documents are incomplete, the skill should run a limited scan and state the limitations.

For a full memo, upload the current quarter, prior quarter, prior-year quarter, latest annual report, earnings release, investor presentation, adjusted metric reconciliations, and earnings call transcript where available.

## Scanner Overview

The scanner modules cover:

- Revenue quality: tests whether reported revenue is supported by customer balances, cash conversion, contract disclosures, and management commentary.
- Customer balance quality: reviews receivables, contract assets, deferred revenue, customer advances, allowances, and collection indicators.
- Expense timing and capitalization: assesses whether costs are recognized currently or deferred into assets in a way that affects margins or future expense burden.
- Asset quality: reviews inventory, receivables, contract assets, goodwill, intangibles, deferred tax assets, investments, and recoverability indicators.
- Liability completeness: reviews accruals, provisions, warranties, refunds, deferred revenue, contingencies, leases, debt, and other obligations.
- Income-statement presentation: evaluates classification, labels, subtotals, nonrecurring items, and whether recurring performance is clear.
- Adjusted metric quality: reviews adjusted EBITDA, adjusted EPS, free cash flow, constant-currency metrics, and reconciliation quality.
- Cash-flow quality: tests whether operating cash flow supports reported earnings after working-capital timing and unusual cash items.
- Working-capital quality: reviews receivables, inventory, payables, accruals, contract balances, and cash conversion cycle signals.
- Disclosure change detection: compares current and prior disclosures for definition changes, missing tables, segment changes, and reduced granularity.
- Related-party and off-balance-sheet review: reviews disclosed related-party transactions, guarantees, commitments, receivable sales, leases, supplier financing, and unconsolidated arrangements.

Each scanner defines required inputs, financial statement areas to inspect, red-flag patterns, calculations, cross-statement triangulation, benign explanations, escalation logic, evidence standards, management questions, and output format.

## Invoking Scanners

Run everything:

```text
Use Quarterly Red Flag Scanner on these documents. Run all 11 scanner modules and create a full earnings-quality red-flag memo.
```

Run a focused scanner:

```text
Use only the Revenue Quality Scanner. Compare revenue growth with receivables, contract assets, deferred revenue, and operating cash flow.
```

Run a group:

```text
Run the revenue, customer balance, working-capital, and cash-flow scanners. I want to know whether revenue is converting into cash.
```

Run a limited scan:

```text
I only have the earnings release and investor presentation. Run the relevant limited scan and state missing evidence.
```

## Interpreting Results

The skill uses four judgment dimensions:

- Severity: Low, Medium, or High.
- Evidence strength: Weak, Moderate, or Strong.
- Materiality: Immaterial, Relevant, or Material.
- Recurrence: One-off, Repeated, or Worsening.

Confidence is expressed from 0% to 100%. A high-confidence red flag is still not a conclusion. It means the supplied documents contain enough evidence to ask sharper questions.

## Output Examples

Common outputs include:

- A short red-flag summary.
- A full earnings-quality memo.
- A scorecard by reporting area.
- A table of calculations and missing evidence.
- A list of management questions.
- A public case-study draft with careful language.

## Legal And Ethical Limits

Red flags are questions, not verdicts. The skill must use calm language, avoid claims that exceed the supplied evidence, include possible benign explanations, and state what documents would reduce uncertainty. Public outputs should be especially careful because quarterly information can be incomplete and unaudited.

## Contributing

Contributions are welcome for scanner improvements, ratio definitions, IFRS and US GAAP differences, jurisdiction-specific reporting notes, extraction improvements, legal-safety tests, output templates, and public filing examples.

Do not contribute copied copyrighted material, unsupported public-company accusations, defamatory claims, stock recommendations, sensational writeups, or material that reveals non-public build inputs.

## Roadmap

- Add jurisdiction-specific reporting notes.
- Expand industry-specific working-capital checks.
- Add more sample calculations for quarterly seasonality.
- Improve extraction guidance for messy filings and presentations.
- Add additional eval prompts for public-output safety.
