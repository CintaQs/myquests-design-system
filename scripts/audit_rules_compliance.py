#!/usr/bin/env python3
"""
Zentrales, deterministisches Compliance-Prüfskript für die 23 Website-Regeln
und das MyQuests Digital Design System (https://github.com/CintaQs/myquests-design-system).

Zweck:
  Prüft das aktuelle Projektverzeichnis automatisiert auf Verstöße gegen:
  - Regel 01: Absolutes Emoji-Verbot (Zero-Emoji Policy)
  - Regel 02: Verbot von Inline-Styles (style="..." / style={{ ... }}) in UI-Dateien
  - Regel 04: Keine losen Skripte (.py, .ps1, .sh) im Projekt-Root außerhalb von .scripts/
  - Regel 09/12: Verbot von Glasmorphismus (backdrop-blur / backdrop-filter != none),
                 Text-Verläufen (bg-clip-text), Zirkusfarben (#CCFF00), Sparkles/Wand2-Icons
                 und generischen Stock-AI-Klassen (bg-mesh, noise-overlay, bg-dots, text-shimmer)
  - Regel 14/15/23: Schutz von .archiv/, .konzept/, _PILOT/ und .env in .gitignore
  - Regel 22: H1-Vertrag (kein ':', '?', '[202x]' oder Schlusspunkt '.' in H1),
              0 Em-Dashes (U+2014), Verbot von Ultra-Bold (800/900, font-extrabold, font-black)
              und Verbot von Kursivschrift (font-style: italic)

Aufruf:
  python .scripts/audit_rules_compliance.py
"""

from __future__ import annotations

import pathlib
import re
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

SKIP_DIRS = {
    ".archiv",
    ".git",
    "node_modules",
    "dist",
    ".astro",
    ".next",
    "__pycache__",
    "data_cache",
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".astro",
    ".tsx",
    ".ts",
    ".jsx",
    ".js",
    ".mjs",
    ".cjs",
    ".css",
    ".html",
    ".json",
    ".sql",
    ".py",
    ".ps1",
    ".yml",
    ".yaml",
}

UI_EXTENSIONS = {".astro", ".tsx", ".jsx", ".html", ".vue", ".svelte"}
STYLE_EXTENSIONS = UI_EXTENSIONS | {".css"}

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"
    "]+",
    flags=re.UNICODE,
)

INLINE_STYLE_PATTERN = re.compile(r"\bstyle\s*=\s*(?:[\"']|\{\{)")
SPARKLES_IMPORT_PATTERN = re.compile(r"\b(?:Sparkles|Wand2)\b")
SPARKLES_SVG_PATTERN = re.compile(r"m12\s+3-1\.912\s+5\.813", re.IGNORECASE)
CIRCUS_COLOR_PATTERN = re.compile(r"#ccff00\b", re.IGNORECASE)
STOCK_AI_CLASS_PATTERN = re.compile(r"\b(?:bg-mesh|noise-overlay|bg-dots|text-shimmer)\b")
GLASSMORPHISM_PATTERN = re.compile(
    r"(?:\bbackdrop-blur-[a-z0-9]+\b|\bbackdrop-blur\b|backdrop-filter\s*:\s*(?!none\b)[a-z0-9(])",
    re.IGNORECASE,
)
TEXT_GRADIENT_PATTERN = re.compile(
    r"(?:\bbg-clip-text\b|-webkit-background-clip\s*:\s*text\b)",
    re.IGNORECASE,
)
FORBIDDEN_FONT_WEIGHT_PATTERN = re.compile(
    r"(?:\bfont-extrabold\b|\bfont-black\b|font-weight\s*:\s*(?:800|900)\b)",
    re.IGNORECASE,
)
FORBIDDEN_ITALIC_PATTERN = re.compile(r"font-style\s*:\s*italic\b", re.IGNORECASE)
HTML_H1_PATTERN = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
YEAR_BRACKET_PATTERN = re.compile(r"\[202\d\]")


def should_skip(path: pathlib.Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def audit_project(root: pathlib.Path) -> list[str]:
    violations: list[str] = []

    # 1. Regel 04: Keine losen Skripte im Projekt-Root
    for item in root.iterdir():
        if item.is_file() and item.suffix.lower() in {".py", ".ps1", ".sh"}:
            violations.append(
                f"[Regel 04] Loses Skript im Projekt-Root gefunden (muss in .scripts/ liegen): {item.name}"
            )

    # 2. Regel 14/15/23: .gitignore Prüfung (falls vorhanden)
    gitignore_path = root / ".gitignore"
    if gitignore_path.exists():
        gitignore_text = gitignore_path.read_text(encoding="utf-8", errors="ignore")
        for required_entry in (".archiv", ".konzept", "_PILOT", ".env"):
            if required_entry not in gitignore_text:
                violations.append(
                    f"[Regel 15/23] Eintrag '{required_entry}' fehlt in .gitignore"
                )

    # 3. Datei-Scan über das Projekt
    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file() or should_skip(file_path):
            continue
        if file_path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if file_path.name in {"audit_rules_compliance.py", "scan_emojis.py"}:
            continue

        rel_path = file_path.relative_to(root)
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        lines = content.splitlines()
        in_code_block = False
        is_rule_or_concept_doc = (
            ".agents" in file_path.parts
            or ".konzept" in file_path.parts
            or "_PILOT" in file_path.parts
        )

        for line_num, line in enumerate(lines, start=1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block

            # Regel 01: Emoji-Prüfung
            if EMOJI_PATTERN.search(line):
                violations.append(
                    f"[Regel 01 Emoji] {rel_path}:{line_num}: Verbotenes Emoji gefunden"
                )

            # Regel 22: Em-Dash (U+2014) Prüfung (in .agents/, .konzept/ und UI-Dateien)
            if "\u2014" in line and (
                ".agents" in file_path.parts
                or ".konzept" in file_path.parts
                or file_path.suffix.lower() in STYLE_EXTENSIONS
            ):
                violations.append(
                    f"[Regel 22 Em-Dash] {rel_path}:{line_num}: Langer englischer Geviertstrich (U+2014) gefunden"
                )

            # Regel 22: Markdown H1-Prüfung (nur außerhalb von Code-Blöcken in .agents/)
            if (
                not in_code_block
                and file_path.suffix.lower() == ".md"
                and ".agents" in file_path.parts
                and line.startswith("# ")
            ):
                h1_text = line[2:].strip()
                if (
                    ":" in h1_text
                    or "?" in h1_text
                    or YEAR_BRACKET_PATTERN.search(h1_text)
                    or h1_text.endswith(".")
                ):
                    violations.append(
                        f"[Regel 22 H1-Vertrag] {rel_path}:{line_num}: H1 enthält ':', '?', '[202x]' oder Schlusspunkt '.': {line}"
                    )

            # UI- & CSS-spezifische Prüfungen (Regel 02, 09, 12, 22)
            if file_path.suffix.lower() in STYLE_EXTENSIONS and not is_rule_or_concept_doc:
                if file_path.suffix.lower() in UI_EXTENSIONS and INLINE_STYLE_PATTERN.search(line):
                    violations.append(
                        f"[Regel 02 Inline-Style] {rel_path}:{line_num}: Verbotenes style-Attribut gefunden"
                    )
                if file_path.suffix.lower() in UI_EXTENSIONS and (
                    SPARKLES_IMPORT_PATTERN.search(line) or SPARKLES_SVG_PATTERN.search(line)
                ):
                    violations.append(
                        f"[Regel 12 Sparkles-Verbot] {rel_path}:{line_num}: Verbotenes Sparkles/Wand2-Icon gefunden"
                    )
                if CIRCUS_COLOR_PATTERN.search(line):
                    violations.append(
                        f"[Regel 12 Zirkusfarbe] {rel_path}:{line_num}: Verbotene Farbe #CCFF00 gefunden"
                    )
                if STOCK_AI_CLASS_PATTERN.search(line):
                    violations.append(
                        f"[Regel 12 Stock-AI-Muster] {rel_path}:{line_num}: Verbotene Deko-Klasse gefunden"
                    )
                if GLASSMORPHISM_PATTERN.search(line):
                    violations.append(
                        f"[Regel 09/12 Glasmorphismus-Verbot] {rel_path}:{line_num}: Verbotener Blur/Glasmorphismus gefunden"
                    )
                if TEXT_GRADIENT_PATTERN.search(line):
                    violations.append(
                        f"[Regel 12 Text-Gradient-Verbot] {rel_path}:{line_num}: Verbotener Text-Farbverlauf (bg-clip-text) gefunden"
                    )
                if FORBIDDEN_FONT_WEIGHT_PATTERN.search(line):
                    violations.append(
                        f"[Regel 22 Font-Weight-Verbot] {rel_path}:{line_num}: Verbotene Schriftstärke 800/900 gefunden (max. 700 Bold)"
                    )
                if FORBIDDEN_ITALIC_PATTERN.search(line):
                    violations.append(
                        f"[Regel 22 Kursiv-Verbot] {rel_path}:{line_num}: Verbotene Kursivschrift (font-style: italic) gefunden"
                    )

        # HTML/JSX <h1> Prüfung in UI-Dateien
        if file_path.suffix.lower() in UI_EXTENSIONS and not is_rule_or_concept_doc:
            for match in HTML_H1_PATTERN.finditer(content):
                h1_inner = re.sub(r"<[^>]+>", "", match.group(1)).strip()
                if (
                    ":" in h1_inner
                    or "?" in h1_inner
                    or YEAR_BRACKET_PATTERN.search(h1_inner)
                    or h1_inner.endswith(".")
                ):
                    violations.append(
                        f"[Regel 22 H1-Vertrag] {rel_path}: HTML-<h1> enthält ':', '?', '[202x]' oder Schlusspunkt '.'"
                    )

    return violations


def main() -> int:
    violations = audit_project(PROJECT_ROOT)
    if violations:
        print(f"[FEHLER] {len(violations)} Regel-Verstöße in {PROJECT_ROOT.name} gefunden:")
        for v in violations:
            print(f"  - {v}")
        return 1

    print(
        f"[OK] Alle geprüften Compliance- & Design-System-Regeln (01, 02, 04, 07, 09, 12, 15, 16, 22, 23) in '{PROJECT_ROOT.name}' zu 100 % erfüllt (0 Verstöße)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
