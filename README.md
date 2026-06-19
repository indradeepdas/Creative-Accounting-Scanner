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
- "Create a full earnings-quality memo for this quarter and compare it with the prior-year quarter."
- "Focus only on revenue quality and receivables. I want the evidence table and management questions."
- "Turn this analysis into a public case study. Keep it non-accusatory and avoid investment recommendations."
- "Build a ratio table for profit versus operating cash flow over the last eight quarters."

## Recommended Inputs

Best results require:

- Current quarterly report or interim financial statements.
- Prior-year quarter and prior quarter where available.
- Earnings release and investor presentation.
- Cash-flow statement and working-capital detail.
- Segment data, accounting policy notes, and critical estimate disclosures.
- Adjusted metric reconciliations.
- Any restatement, remediation, covenant, or going-concern disclosures.

When documents are incomplete, the skill should run a limited scan and state the limitations.

## Scanner Overview

The scanner modules cover:

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

Each scanner defines required inputs, financial statement areas to inspect, red-flag patterns, calculations, cross-statement triangulation, benign explanations, escalation logic, evidence standards, management questions, and output format.

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
