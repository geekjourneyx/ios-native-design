#!/usr/bin/env python3
"""Contract tests for the ios-native-design skill documentation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
dod = (ROOT / "DESIGN_DOD.md").read_text(encoding="utf-8")
testing = (ROOT / "references" / "testing.md").read_text(encoding="utf-8")

required_files = [
    ROOT / "references" / "agent-device-testing.md",
    ROOT / "references" / "device-hub.md",
    ROOT / "references" / "computer-use-testing.md",
    ROOT / "templates" / "AGENT_UI_TEST_PROMPT.md",
    ROOT / "templates" / "DEVICE_TEST_MATRIX.md",
]

for path in required_files:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"

assert "Agent-operated runtime verification" in skill
assert "Build and operate the running app — P0" in skill
assert "explore" in skill.lower() and "XCUI" in skill
assert "Device Hub full-resolution screenshots" in skill
assert "physical-device verification" in skill
assert "Runtime verification — P0" in dod
assert "P0  Agent-operated runtime exploration" in testing

runtime_pos = skill.index("Agent-operated runtime verification")
preview_pos = skill.index("Preview matrix")
static_pos = skill.index("Static verifier")
assert runtime_pos < preview_pos
assert runtime_pos < static_pos

print("ios-native-design skill contract: PASS")
