# Document Acquisition

Use this file when the user gives a company name, ticker, CIK, issuer identifier, or asks Codex to find filings before running the scanners.

## Acquisition Policy

Prefer primary-source documents. Use user-uploaded documents when retrieval is unavailable or the user wants a specific local file reviewed.

Retrieval priority:

1. Dedicated SEC, EDGAR, filings, public-equity, or market-disclosure connector if available.
2. Official SEC EDGAR public data for U.S. registrants.
3. Company investor-relations pages for releases, presentations, and transcripts.
4. User-supplied documents or links.
5. General web search only as a fallback or when explicitly requested.

Do not invent a connector. If no connector is available, use official web sources when browsing is available. If neither connector nor browsing is available, ask the user to upload the documents.

## U.S. SEC Retrieval

When using SEC EDGAR:

- Resolve the ticker or company name to a CIK.
- Normalize the CIK to 10 digits with leading zeros.
- Retrieve filing metadata before downloading individual documents.
- Use the latest 10-Q for the current quarter.
- Use the latest 10-K for annual context.
- Use prior quarter and prior-year quarter filings for trend comparison.
- Use 8-K earnings releases and company presentations when the 10-Q is not yet filed.
- Respect SEC fair-access rules and send an appropriate User-Agent header when making direct requests.

Useful endpoint patterns:

- Company submissions: `https://data.sec.gov/submissions/CIK##########.json`
- Company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- Filing archive: `https://www.sec.gov/Archives/edgar/data/{cik}/{accession_without_dashes}/{primary_document}`

## Document Manifest

Before scanning, create a manifest with:

- Company.
- Ticker.
- CIK or issuer identifier.
- Reporting period.
- Document type.
- Filed or published date.
- Source URL.
- Accession number when applicable.
- Primary document reviewed.
- Scanner areas supported by the document.

## Retrieval To Scanner Flow

1. Retrieve or identify documents.
2. Build the document manifest.
3. Extract financial statements, notes, segment data, adjusted metric reconciliations, and management commentary.
4. Normalize the current quarter, prior quarter, prior-year quarter, year-to-date periods, and trailing periods where possible.
5. Run the scanner set requested by the user.
6. If the user did not specify a scanner set, run all scanners when the retrieved data supports them.
7. State skipped scanners and missing documents.

## Limited Retrieval Cases

If only an earnings release or presentation is available:

- Run a limited scan.
- Prioritize revenue quality, adjusted metric quality, income-statement presentation, cash-flow quality if disclosed, and missing evidence.
- Say what the 10-Q or annual report should confirm.

If prior periods are unavailable:

- Avoid trend claims that require prior-period data.
- Lower confidence.
- Ask for or retrieve prior filings before running disclosure change detection.

## User Prompts To Support

- "Retrieve the latest 10-Q and run all scanners."
- "For this ticker, get the latest SEC filings and create a red-flag memo."
- "The 10-Q is not out yet. Use the earnings release and presentation for a limited scan."
- "Find the latest 10-K for policy context, then run the revenue and cash-flow scanners."
- "Create a manifest of the documents you retrieved before scanning."

## Safety

Retrieved filings are still limited public evidence. Do not infer intent. Do not make legal conclusions. Do not give investment recommendations. Treat red flags as follow-up questions.
