# Sample Input Requirements

The skill can run with a minimal document set, but confidence improves when documents allow period comparison and cross-statement triangulation.

Codex-native option:

- Instead of uploading documents, provide a company name, ticker, or CIK and ask Codex to retrieve public filings from primary sources before running the scanners.
- Example: "Retrieve the latest 10-Q, latest 10-K, current earnings release, and prior-year quarter filing for MSFT, then run all 11 scanners."
- If retrieval tools or web access are unavailable, upload the document package below.

For a strong review, provide:

- Company name and ticker.
- Reporting period.
- Quarterly report or interim financial statements.
- Earnings release.
- Investor presentation.
- Prior-year quarter and prior quarter if available.
- Latest annual report if quarterly notes are condensed.
- Any earnings call transcript or management commentary you want considered.

Minimum useful input:

- One quarterly report, one interim financial statement package, one earnings release, or one investor presentation.

If only minimum input is available, the skill should run a limited scan and explain that confidence is lower because prior periods, notes, or cash-flow detail may be missing.

Best full-memo package:

- Current quarter report.
- Prior quarter report.
- Prior-year quarter report.
- Latest annual report.
- Earnings release.
- Investor presentation.
- Adjusted metric reconciliations.
- Earnings call transcript or prepared remarks.
- Segment tables and KPI schedules.
- Covenant, liquidity, restatement, impairment, restructuring, or remediation disclosures when relevant.

Scanner invocation examples:

- "Run all 11 scanners and create a full memo."
- "Run only the Revenue Quality Scanner."
- "Run revenue quality, customer balance quality, working-capital quality, and cash-flow quality."
- "Run a limited scan because I only have the earnings release."
- "Run disclosure change detection against the prior quarter."
