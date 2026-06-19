from __future__ import annotations

from pathlib import Path
import re
import sys


REQUIRED_SECTIONS = [
    "Purpose",
    "Core Principle",
    "When to Use",
    "Required Inputs",
    "Financial Statement Areas to Inspect",
    "Key Red-Flag Patterns",
    "Suggested Calculations",
    "Cross-Statement Triangulation",
    "Possible Benign Explanations",
    "Escalation Logic",
    "Evidence Standard",
    "Management Questions",
    "Output Format",
]


def section_positions(text: str) -> dict[str, int]:
    positions: dict[str, int] = {}
    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf"^##\s+{re.escape(section)}\s*$", re.MULTILINE)
        match = pattern.search(text)
        if match:
            positions[section] = match.start()
    return positions


def main() -> int:
    root = Path.cwd()
    scanner_dir = root / "scanners"
    failures: list[str] = []

    files = sorted(scanner_dir.glob("*.md"))
    if not files:
        print("No scanner files found.")
        return 1

    for path in files:
        text = path.read_text(encoding="utf-8")
        positions = section_positions(text)
        missing = [section for section in REQUIRED_SECTIONS if section not in positions]
        if missing:
            failures.append(f"{path.relative_to(root)} missing sections: {', '.join(missing)}")
            continue

        ordered_positions = [positions[section] for section in REQUIRED_SECTIONS]
        if ordered_positions != sorted(ordered_positions):
            failures.append(f"{path.relative_to(root)} has sections out of required order")

    if failures:
        print("Scanner structure validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(files)} scanner files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
