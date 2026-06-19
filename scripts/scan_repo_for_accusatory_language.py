from __future__ import annotations

from pathlib import Path
import re
import sys


IGNORED_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".pytest_cache"}
ALLOWED_FILES = {
    Path("scripts/scan_repo_for_accusatory_language.py"),
    Path("evals/test_prompts.yaml"),
    Path("evals/legal_safety_tests.md"),
}
TEXT_SUFFIXES = {"", ".md", ".py", ".yml", ".yaml", ".txt", ".json"}

RISKY_PATTERNS = [
    re.compile(r"\bcooked the books\b", re.IGNORECASE),
    re.compile(r"\bcommitted fraud\b", re.IGNORECASE),
    re.compile(r"\bfraudulent\b", re.IGNORECASE),
    re.compile(r"\billegal\b", re.IGNORECASE),
    re.compile(r"\bdeceived investors\b", re.IGNORECASE),
    re.compile(r"\bmisled investors\b", re.IGNORECASE),
    re.compile(r"\bcover(?:ed)? up\b", re.IGNORECASE),
    re.compile(r"\bscam\b", re.IGNORECASE),
    re.compile(r"\bcriminal\b", re.IGNORECASE),
    re.compile(r"\bfake revenue\b", re.IGNORECASE),
    re.compile(r"\bfalsif(?:y|ied|ies)\b", re.IGNORECASE),
    re.compile(r"\bshort the stock\b", re.IGNORECASE),
    re.compile(r"\bbuy the stock\b", re.IGNORECASE),
    re.compile(r"\bsell the stock\b", re.IGNORECASE),
    re.compile(r"\bhold the stock\b", re.IGNORECASE),
    re.compile(r"\bprice target\b", re.IGNORECASE),
]

SAFE_CONTEXT_PATTERNS = [
    re.compile(r"\bdo not\b", re.IGNORECASE),
    re.compile(r"\bdoes not\b", re.IGNORECASE),
    re.compile(r"\bnot\b.{0,40}\b(fraud|fraudulent|wrongdoing|illegal|accus)", re.IGNORECASE),
    re.compile(r"\bno\b.{0,40}\b(accusation|legal conclusion|investment recommendation)", re.IGNORECASE),
    re.compile(r"\bavoid(?:s|ing)?\b", re.IGNORECASE),
    re.compile(r"\brefus(?:e|al|ing)\b", re.IGNORECASE),
    re.compile(r"\bprohibit(?:s|ed)?\b", re.IGNORECASE),
    re.compile(r"\bshould not\b", re.IGNORECASE),
    re.compile(r"\bcannot\b", re.IGNORECASE),
    re.compile(r"\bnot evidence of wrongdoing\b", re.IGNORECASE),
    re.compile(r"\bnot a fraud detector\b", re.IGNORECASE),
]


def should_scan(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if relative in ALLOWED_FILES:
        return False
    if any(part in IGNORED_DIRS for part in relative.parts):
        return False
    if path.name in {".gitignore", ".gitattributes", "LICENSE"}:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def is_safe_context(line: str) -> bool:
    return any(pattern.search(line) for pattern in SAFE_CONTEXT_PATTERNS)


def main() -> int:
    root = Path.cwd()
    hits: list[tuple[Path, int, str]] = []

    for path in root.rglob("*"):
        if not path.is_file() or not should_scan(path, root):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(lines, start=1):
            if is_safe_context(line):
                continue
            for pattern in RISKY_PATTERNS:
                if pattern.search(line):
                    hits.append((path.relative_to(root), line_no, pattern.pattern))

    if hits:
        print("Accusatory or investment-recommendation language found:")
        for rel_path, line_no, pattern in hits:
            print(f"{rel_path}:{line_no}: matched {pattern}")
        return 1

    print("Accusatory-language scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
