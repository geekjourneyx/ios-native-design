# ios-native-design

A reusable **iOS Design + Runtime QA Harness** for AI coding agents.

The Skill combines:

- Apple HIG
- native-component-first SwiftUI
- semantic design tokens
- accessibility
- agent-operated runtime exploration
- Xcode 27 Device Hub
- Computer Use fallback
- full-resolution screenshot review
- environment/device test matrices
- Explore → XCUI regression
- static design guardrails

## Install

```bash
npx skills add geekjourneyx/ios-native-design
```

## Main workflow

```text
Design → Implement → Build → Operate app → Collect runtime evidence
                                      ↓
                          Screenshot + accessibility
                                      ↓
                              Review → Fix → Rerun
                                      ↓
                            Stable path → XCUI
```

## Start here

- `SKILL.md` — required workflow and hard constraints
- `references/agent-device-testing.md` — P0 runtime loop
- `references/device-hub.md` — Xcode 27 Device Hub usage
- `references/computer-use-testing.md` — semantic-tool vs GUI automation boundary
- `templates/AGENT_UI_TEST_PROMPT.md` — ready-to-use runtime QA prompt
- `templates/DEVICE_TEST_MATRIX.md` — environment coverage
- `DESIGN_DOD.md` — final release gate
- `VERIFIER_RULES.md` — static/render/interaction/judgment rule taxonomy

The static verifier is intentionally a guardrail, not the definition of design quality.
