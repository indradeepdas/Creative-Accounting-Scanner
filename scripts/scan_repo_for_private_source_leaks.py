from __future__ import annotations

from base64 import b64decode
from pathlib import Path
import os
import sys


ENV_VAR = "PRIVATE_SOURCE_LEAK_TERMS_B64"
LOCAL_TERMS_FILE = ".private_source_leak_terms"
IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".cache",
}
TEXT_SUFFIXES = {
    "",
    ".md",
    ".txt",
    ".py",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".gitignore",
    ".gitattributes",
}


def load_terms(root: Path) -> list[str]:
    encoded = os.environ.get(ENV_VAR, "").strip()
    if encoded:
        try:
            decoded = b64decode(encoded).decode("utf-8")
        except Exception as exc:
            raise SystemExit(f"Failed to decode {ENV_VAR}: {exc}") from exc
        return normalize_terms(decoded.splitlines())

    local_file = root / LOCAL_TERMS_FILE
    if local_file.exists():
        return normalize_terms(local_file.read_text(encoding="utf-8").splitlines())

    return []


def normalize_terms(lines: list[str]) -> list[str]:
    terms = []
    for line in lines:
        term = line.strip()
        if term and not term.startswith("#"):
            terms.append(term)
    return terms


def should_scan(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if any(part in IGNORED_DIRS for part in relative.parts):
        return False
    if path.name == LOCAL_TERMS_FILE:
        return False
    if path.suffix.lower() in TEXT_SUFFIXES:
        return True
    return path.name in {".gitignore", ".gitattributes", "LICENSE"}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and should_scan(path, root):
            yield path


def main() -> int:
    root = Path.cwd()
    terms = load_terms(root)
    if not terms:
        print("Warning: no private-source leak terms provided; leak scanning skipped.")
        return 0

    lowered_terms = [(term, term.lower()) for term in terms]
    hits: list[tuple[Path, int, str]] = []

    for path in iter_text_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(lines, start=1):
            lowered_line = line.lower()
            for original, lowered in lowered_terms:
                if lowered in lowered_line:
                    hits.append((path.relative_to(root), line_no, original))

    if hits:
        print("Potential private-source leaks found:")
        for rel_path, line_no, term in hits:
            print(f"{rel_path}:{line_no}: {term}")
        return 1

    print(f"Private-source leak scan passed with {len(terms)} terms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
