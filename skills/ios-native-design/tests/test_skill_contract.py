#!/usr/bin/env python3
"""Contract tests for the ios-native-design skill documentation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
dod = (ROOT / "DESIGN_DOD.md").read_text(encoding="utf-8")
testing = (ROOT / "references" / "testing.md").read_text(encoding="utf-8")
visual = (ROOT / "references" / "visual-review.md").read_text(encoding="utf-8")
agent_device = (ROOT / "references" / "agent-device-testing.md").read_text(encoding="utf-8")
device_hub = (ROOT / "references" / "device-hub.md").read_text(encoding="utf-8")
computer_use = (ROOT / "references" / "computer-use-testing.md").read_text(encoding="utf-8")

required_files = [
    ROOT / "references" / "agent-device-testing.md",
    ROOT / "references" / "device-hub.md",
    ROOT / "references" / "computer-use-testing.md",
    ROOT / "templates" / "AGENT_UI_TEST_PROMPT.md",
    ROOT / "templates" / "DEVICE_TEST_MATRIX.md",
]

for path in required_files:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"

# Runtime operation is the primary verifier.
assert "Agent-operated runtime verification" in skill
assert "Build and operate the running app — P0" in skill
assert "Runtime verification — P0" in dod
assert "P0  Agent-operated runtime exploration" in testing

# Runtime evidence must include Device Hub-quality screenshots and accessibility semantics.
assert "Device Hub full-resolution screenshots" in skill
assert "accessibility semantics" in skill.lower()
assert "full resolution" in device_hub.lower()
assert "accessibility tree" in agent_device.lower()
assert "Device Hub full-resolution screenshot" in visual
assert "Semantic agreement" in visual

# Capability routing must prefer semantic/native interfaces and keep Computer Use as a GUI fallback.
assert "Xcode native agent" in skill
assert "semantic iOS simulator" in skill
assert "Computer Use" in skill
assert "semantic" in computer_use.lower()
assert "coordinate" in computer_use.lower()

# Exploration should graduate into deterministic regression.
assert "Explore, then codify" in skill
assert "XCUI" in skill
assert "XCUI" in agent_device
assert "stable critical paths" in testing.lower()

# Hardware-specific behavior must escalate to a real device.
assert "physical-device verification" in skill
assert "physical device" in agent_device.lower()

# P0 runtime verification must be described before lower-priority preview/static guardrails.
runtime_pos = skill.index("Agent-operated runtime verification")
preview_pos = skill.index("Preview matrix")
static_pos = skill.index("Static verifier")
assert runtime_pos < preview_pos
assert runtime_pos < static_pos

# Completion requires post-fix runtime evidence, not source-only confidence.
assert "rerun after the final design fix" in dod
assert "post-fix running state is the evidence" in visual

print("ios-native-design skill contract: PASS")
