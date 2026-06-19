from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "DISCLAIMER.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    "skill/SKILL.md",
    "skill/workflow.md",
    "skill/operating_principles.md",
    "skill/legal_safety_rules.md",
    "skill/evidence_rules.md",
    "skill/uncertainty_rules.md",
    "skill/output_style.md",
    "principles/earnings_quality_foundations.md",
    "principles/reporting_pressure_and_incentives.md",
    "principles/accounting_judgment_and_flexibility.md",
    "principles/accruals_cash_and_timing.md",
    "principles/classification_and_presentation.md",
    "principles/sustainable_vs_transitory_performance.md",
    "principles/cross_statement_triangulation.md",
    "principles/public_company_review_limitations.md",
    "scanners/revenue_quality.md",
    "scanners/customer_balance_quality.md",
    "scanners/expense_timing_and_capitalization.md",
    "scanners/asset_quality.md",
    "scanners/liability_completeness.md",
    "scanners/income_statement_presentation.md",
    "scanners/adjusted_metric_quality.md",
    "scanners/cash_flow_quality.md",
    "scanners/working_capital_quality.md",
    "scanners/disclosure_change_detection.md",
    "scanners/related_party_and_off_balance_sheet_review.md",
    "templates/red_flag_memo.md",
    "templates/earnings_quality_scorecard.md",
    "templates/management_questions.md",
    "templates/analyst_workpaper.md",
    "templates/public_case_study.md",
    "templates/short_public_summary.md",
    "templates/linkedin_post_template.md",
    "examples/sample_input_requirements.md",
    "examples/sample_red_flag_memo.md",
    "examples/sample_management_questions.md",
    "examples/sample_public_case_study.md",
    "examples/sample_limitations_note.md",
    "evals/test_prompts.yaml",
    "evals/quality_bar.md",
    "evals/legal_safety_tests.md",
    "evals/repo_compliance_tests.md",
    "evals/scanner_coverage_tests.md",
    "scripts/validate_required_files.py",
    "scripts/validate_scanner_structure.py",
    "scripts/scan_repo_for_private_source_leaks.py",
    "scripts/scan_repo_for_accusatory_language.py",
    ".github/workflows/repo_compliance.yml",
    ".gitattributes",
]


def main() -> int:
    root = Path.cwd()
    missing = [path for path in REQUIRED_FILES if not (root / path).is_file()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print(f"All {len(REQUIRED_FILES)} required files are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
