# Agent Device Loop Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make agent-operated runtime verification with Xcode Device Hub, accessibility semantics, full-resolution screenshots, and explore-to-XCUI regression the highest-priority verification path in `ios-native-design`.

**Architecture:** Keep HIG/native-component/design-token guidance as the design input layer, but move runtime operation to the primary verifier. Route agents to the highest-level available device interface, collect a runtime evidence bundle, use Device Hub captures for final visual evidence, and convert stable critical paths into deterministic XCUI tests.

**Tech Stack:** Markdown Agent Skill, Xcode 27 Device Hub, SwiftUI, XCUI, Computer Use, Python contract tests and static verifier.

**Spec:** Runtime-first direction approved in the conversation on 2026-09-17.

## Global Constraints

- Runtime verification is P0; Preview is P1; static verifier/snapshots are P2.
- Prefer semantic Xcode/simulator tools over coordinate clicking when available.
- Prefer Device Hub device-resolution screenshots over Mac desktop screenshots for final visual evidence.
- Combine screenshots with accessibility semantics and interaction history when available.
- Hardware-dependent behavior requires physical-device verification.
- Stable critical paths should graduate from exploratory agent operation to deterministic XCUI regression.

---

### Task 1: Promote runtime operation into the core Skill

**Files:**
- Modify: `skills/ios-native-design/SKILL.md`
- Modify: `skills/ios-native-design/DESIGN_DOD.md`

- [x] Put agent-operated runtime verification and runtime evidence at P0.
- [x] Add capability routing for Xcode native tools, semantic simulator tools, Computer Use, and fallback paths.
- [x] Require post-fix reruns and physical-device escalation for hardware-dependent behavior.

### Task 2: Add Device Hub and Computer Use reference guidance

**Files:**
- Create: `skills/ios-native-design/references/agent-device-testing.md`
- Create: `skills/ios-native-design/references/device-hub.md`
- Create: `skills/ios-native-design/references/computer-use-testing.md`
- Modify: `skills/ios-native-design/references/testing.md`

- [x] Define runtime exploration and evidence checkpoints.
- [x] Define Device Hub screenshot and environment-matrix rules.
- [x] Define semantic-tool-first / Computer-Use-fallback boundaries.
- [x] Define explore-to-XCUI regression flow.

### Task 3: Add reusable runtime-test templates

**Files:**
- Create: `skills/ios-native-design/templates/AGENT_UI_TEST_PROMPT.md`
- Create: `skills/ios-native-design/templates/DEVICE_TEST_MATRIX.md`

- [x] Add a reusable agent-run UI verification prompt.
- [x] Add a runtime environment coverage matrix.

### Task 4: Upgrade visual review from screenshot-only to runtime evidence

**Files:**
- Modify: `skills/ios-native-design/references/visual-review.md`

- [x] Require interaction history, device-resolution capture, accessibility semantics, and environment state where available.
- [x] Keep visual hierarchy/craft review while adding runtime behavior and semantic mismatch checks.

### Task 5: Enforce the new contract

**Files:**
- Modify: `skills/ios-native-design/tests/test_skill_contract.py`

- [x] Assert runtime verification precedes Preview/static verification.
- [x] Assert Device Hub, accessibility semantics, runtime visual review, physical-device escalation, and explore-to-XCUI references exist.

### Task 6: Update public README

**Files:**
- Modify: `README.md`
- Modify: `skills/ios-native-design/README.md`

- [x] Put `npx skills add geekjourneyx/ios-native-design` first.
- [x] Explain runtime-first Design QA and Device Hub evidence flow.
- [x] Document verification priority and capability routing.

### Verification

- [ ] Run `python3 skills/ios-native-design/tests/test_skill_contract.py` and require exit 0.
- [ ] Run `python3 -m py_compile skills/ios-native-design/verifier/ios_design_verifier.py` and require exit 0.
- [ ] Re-fetch `main` and confirm all runtime-first references/templates/tests are present.
