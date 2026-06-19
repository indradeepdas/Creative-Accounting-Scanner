# Codex-Native Filing Retrieval

Quarterly Red Flag Scanner should work in two modes:

1. User-supplied documents.
2. Codex-retrieved public filings and related disclosures.

The second mode is more natural for Codex. A user can give a company name, ticker, CIK, or filing period, and Codex can gather public documents before running the scanner modules.

## Recommended Retrieval Order

Use the safest available source in this order:

1. Dedicated filings connector or plugin, if available.
2. Official SEC EDGAR public data endpoints for U.S. issuers.
3. Company investor-relations pages for earnings releases, presentations, and transcripts.
4. User-supplied files or links.
5. General web search only when the user asks for it or when primary sources are not enough.

Do not invent a connector. If no filings tool is available, say so and use the best primary-source fallback.

## Primary Source Preference

Prefer primary sources:

- SEC EDGAR filings.
- Company investor-relations pages.
- Exchange or regulator filings pages for non-U.S. issuers.
- Company-hosted earnings releases and presentations.

Use third-party aggregators only for discovery or convenience, and verify key numbers against primary documents before scoring red flags.

## SEC EDGAR Retrieval Path

For U.S. listed companies, Codex can use official SEC public data when no dedicated connector is available.

Useful official endpoints include:

- Company submissions: `https://data.sec.gov/submissions/CIK##########.json`
- Company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- Filing archive documents: `https://www.sec.gov/Archives/edgar/data/{cik}/{accession_without_dashes}/{primary_document}`

Operational notes:

- Normalize CIKs to 10 digits with leading zeros for `data.sec.gov` URLs.
- Use company name, ticker, or known CIK to identify the registrant.
- Respect SEC fair-access guidance and use an appropriate `User-Agent` header with contact information.
- Retrieve filing metadata first, then fetch only the documents needed for the review.
- Prefer the latest 10-Q for quarterly analysis and the latest 10-K for annual context.
- Also retrieve 8-K earnings releases when the quarterly filing is not yet available.

## What To Retrieve For A U.S. Issuer

For a full quarterly review, gather:

- Current 10-Q.
- Prior quarter 10-Q when available.
- Prior-year quarter 10-Q.
- Latest 10-K.
- Current 8-K earnings release, usually Item 2.02 when available.
- Earnings presentation from investor relations, if available.
- Non-GAAP reconciliation included in the release or presentation.
- Earnings call transcript or prepared remarks, if available from a primary or clearly identified source.

For a limited review, gather:

- Latest 10-Q if filed.
- Latest 8-K earnings release.
- Investor presentation if available.

## Filing Selection Logic

When the user gives only a ticker:

1. Resolve ticker to company name and CIK.
2. Identify the reporting period requested, or use the latest quarter.
3. Retrieve the latest 10-Q.
4. Retrieve the same quarter from the prior year if available.
5. Retrieve the immediately preceding quarter if available.
6. Retrieve the latest 10-K for accounting policy and annual-note context.
7. Retrieve earnings release and presentation when available.
8. Create a document manifest before running scanners.

When the user gives a company name but no ticker:

1. Ask for ticker if the company is ambiguous.
2. If unambiguous, resolve to ticker and CIK.
3. Continue with the ticker workflow.

When the company is not a U.S. SEC registrant:

1. Identify the relevant regulator or exchange filing source.
2. Use primary company and regulator documents where possible.
3. State that SEC-specific retrieval steps do not apply.

## Document Manifest

Before scanning, create a short manifest:

Field | Description
--- | ---
Company | Legal issuer name.
Ticker | Ticker used for retrieval.
CIK or issuer ID | CIK for SEC registrants or equivalent identifier.
Period | Quarter and fiscal year reviewed.
Document type | 10-Q, 10-K, 8-K, presentation, transcript, release, or other.
Filed or published date | Date from the source.
Source URL | Primary-source URL.
Accession number | SEC accession number when applicable.
Primary document | Main HTML, TXT, or PDF document reviewed.
Use in analysis | Which scanner areas the document supports.

## Handoff To Scanners

After retrieval:

1. Extract the income statement, balance sheet, cash-flow statement, notes, segment data, and adjusted metric reconciliations.
2. Normalize current quarter, prior quarter, prior-year quarter, year-to-date, and trailing periods where possible.
3. Run all relevant scanners, or the scanner set requested by the user.
4. State which documents were retrieved by Codex and which were supplied by the user.
5. State which expected documents were not found.

## Scanner Selection After Retrieval

Use all 11 scanners when Codex retrieves a current 10-Q, relevant prior periods, and cash-flow data.

Use a limited scanner set when only an earnings release, presentation, or 8-K is available:

- Revenue quality.
- Adjusted metric quality.
- Income-statement presentation.
- Cash-flow quality if cash flow is disclosed.
- Disclosure change detection if prior releases are available.
- Missing evidence and limitations.

## User Prompts

Full retrieval and review:

```text
Use Quarterly Red Flag Scanner for Microsoft. Retrieve the latest 10-Q, latest 10-K, current earnings release, investor presentation, and prior-period filings from primary sources, then run all 11 scanners.
```

Ticker-only quick scan:

```text
Run a Codex-native quick scan for AAPL. Pull the latest SEC quarterly filing and earnings release, then summarize the top red flags and missing evidence.
```

Specific scanner after retrieval:

```text
For NVDA, retrieve the latest 10-Q and prior-year quarter, then run only the revenue quality and customer balance quality scanners.
```

Limited release review:

```text
The 10-Q is not filed yet. Retrieve the latest earnings release and investor presentation, run a limited scan, and list what the 10-Q should confirm.
```

## Evidence And Safety Rules

- Cite the retrieved document and section used for each finding.
- Treat retrieved documents as public-source evidence, not as proof of intent.
- Do not accuse the company or management.
- Do not give buy, sell, hold, short, or price-target advice.
- Do not overstate confidence when only earnings releases or presentations are available.
- Prefer "not found in retrieved documents" over "not disclosed" unless the expected source was actually reviewed.

## Suggested Codex Behavior

When the user asks for a company review, Codex should ask fewer questions if it can retrieve public filings. A good first response is:

```text
I will retrieve the latest primary-source filings and disclosures, create a document manifest, then run the requested scanner set. If a filing is not yet available, I will run a limited scan and state the missing evidence.
```

If no retrieval tool or web access is available, Codex should say:

```text
I do not have a filings connector or web access in this session. Upload the current quarterly report, prior-period filings, earnings release, and adjusted metric reconciliation, and I will run the scanners from those documents.
```
