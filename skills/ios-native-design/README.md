# ios-native-design

A reusable iOS Design Harness for SwiftUI coding agents.

## Install

```bash
npx skills add geekjourneyx/ios-native-design
```

Explicit skill selection:

```bash
npx skills add geekjourneyx/ios-native-design --skill ios-native-design
```

Global install:

```bash
npx skills add geekjourneyx/ios-native-design -g
```

## What it enforces

- Apple HIG as the primary platform reference
- native SwiftUI components before custom recreations
- Dynamic Type and semantic system colors
- project-owned spacing / radius / brand tokens
- 44×44 pt interaction targets
- deliberate motion and Reduce Motion behavior
- restrained Liquid Glass usage
- screenshot-driven visual review
- accessibility, XCUI, and snapshot verification
- a final Design Definition of Done

## Workflow

```text
Requirement
  ↓
HIG + native component decision
  ↓
Design tokens
  ↓
SwiftUI
  ↓
Render / screenshot
  ↓
Visual + accessibility review
  ↓
Static verifier + UI tests
  ↓
Design DoD
```

See the repository root README for the full overview.
