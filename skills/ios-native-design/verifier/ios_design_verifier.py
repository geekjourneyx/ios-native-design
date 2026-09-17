#!/usr/bin/env python3
"""Heuristic static verifier for the ios-native-design skill."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

@dataclass
class Finding:
    rule: str
    severity: str
    file: str
    line: int
    message: str
    suggestion: str

RULES = [
    ("IOS-NATIVE-001", "fail", re.compile(r"Color\s*\(\s*hex\s*:|Color\s*\(\s*['\"]#?[0-9A-Fa-f]{6,8}['\"]|Color\s*\(\s*red\s*:"), "Raw color literal in feature UI.", "Use a semantic system color or move an approved brand color into the design system."),
    ("IOS-NATIVE-002", "fail", re.compile(r"\.font\s*\(\s*\.system\s*\(\s*size\s*:"), "Fixed system font size in feature UI.", "Use a Dynamic Type style or an approved typography token."),
    ("IOS-NATIVE-003", "warn", re.compile(r"\.padding\s*\([^)]*\b\d+(?:\.\d+)?\s*\)"), "Raw numeric padding found.", "Prefer system spacing or a semantic spacing token."),
    ("IOS-NATIVE-004", "warn", re.compile(r"\.cornerRadius\s*\([^)]*\b\d+(?:\.\d+)?"), "Raw corner radius found.", "Prefer a system shape or an approved radius token."),
    ("IOS-NATIVE-005", "warn", re.compile(r"\.ignoresSafeArea\s*\("), "Safe area is being ignored.", "Confirm this is intentional full-bleed/background behavior."),
    ("IOS-NATIVE-006", "warn", re.compile(r"\b(?:CustomTabBar|CustomNavigationBar|CustomToggle|CustomSegmentedControl|SegmentedControl)\b"), "Possible recreation of a standard iOS control.", "Confirm a native SwiftUI control cannot express the requirement."),
    ("IOS-NATIVE-007", "warn", re.compile(r"\.glassEffect\s*\("), "Custom Liquid Glass use found.", "Confirm it is functional control/navigation UI, not generic content decoration."),
    ("IOS-NATIVE-008", "warn", re.compile(r"\.bouncy\b"), "Bouncy motion found.", "Reserve expressive bounce for deliberate moments."),
    ("IOS-NATIVE-009", "info", re.compile(r"\.onTapGesture\b"), "Direct tap gesture found.", "If it behaves like a button, prefer Button semantics or verify accessibility and hit target."),
]

DEFAULT_CONFIG = {
    "exclude_paths": [".build", "DerivedData", "Pods", "Carthage", "Packages", "Tests", "UITests"],
    "token_owner_name_fragments": ["DesignToken", "DesignSystem", "Theme", "AppColor", "AppTypography", "AppSpacing"],
    "fail_rules": ["IOS-NATIVE-001", "IOS-NATIVE-002"],
}

def load_config(path: Path | None) -> dict:
    if path is None:
        return DEFAULT_CONFIG
    return {**DEFAULT_CONFIG, **json.loads(path.read_text(encoding="utf-8"))}

def excluded(path: Path, root: Path, config: dict) -> bool:
    parts = path.relative_to(root).parts
    return any(item in parts for item in config["exclude_paths"])

def token_owner(path: Path, config: dict) -> bool:
    stem = path.stem.lower()
    return any(x.lower() in stem for x in config["token_owner_name_fragments"])

def waived(lines: list[str], index: int, rule: str) -> bool:
    for prev in lines[max(0, index - 2):index]:
        if "ios-native-design: allow" in prev and rule in prev and "reason=" in prev:
            return True
    return False

def scan(path: Path, root: Path, config: dict) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    findings: list[Finding] = []
    is_owner = token_owner(path, config)
    for i, line in enumerate(lines):
        for rule, severity, pattern, message, suggestion in RULES:
            if is_owner and rule in {"IOS-NATIVE-001", "IOS-NATIVE-002", "IOS-NATIVE-003", "IOS-NATIVE-004"}:
                continue
            if pattern.search(line) and not waived(lines, i, rule):
                findings.append(Finding(rule, severity, str(path.relative_to(root)), i + 1, message, suggestion))
    if text.count(".glassEffect(") >= 3 and not any(x in path.stem.lower() for x in ("toolbar", "navigation", "tabbar", "control")):
        findings.append(Finding("IOS-NATIVE-007", "warn", str(path.relative_to(root)), 1, "Repeated glassEffect use in one non-control file.", "Review whether glass is being used as generic content decoration."))
    return findings

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.project.resolve()
    if not root.exists():
        print(f"Project path does not exist: {root}", file=sys.stderr)
        return 2
    config = load_config(args.config)
    findings: list[Finding] = []
    for path in root.rglob("*.swift"):
        if not excluded(path, root, config):
            findings.extend(scan(path, root, config))
    gate = "fail" if any(f.severity == "fail" and f.rule in set(config["fail_rules"]) for f in findings) else "pass"
    if args.json:
        print(json.dumps({"gate": gate, "findings": [asdict(x) for x in findings]}, ensure_ascii=False, indent=2))
    else:
        print(f"ios-native-design gate: {gate.upper()}")
        for f in findings:
            print(f"{f.severity.upper():5} {f.rule} {f.file}:{f.line}\n      {f.message}\n      → {f.suggestion}")
    return 1 if gate == "fail" else 0

if __name__ == "__main__":
    raise SystemExit(main())
