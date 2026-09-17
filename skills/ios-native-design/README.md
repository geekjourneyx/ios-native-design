# ios-native-design

A reusable **iOS Design Harness** for AI coding agents.

Goal: make SwiftUI apps feel native to Apple platforms by constraining agent freedom with:

- Apple HIG as the source of truth
- native components first
- semantic design tokens
- accessibility requirements
- motion/material rules
- preview + screenshot review loops
- static verifier rules
- UI / snapshot regression gates

## Structure

```text
ios-native-design/
├── SKILL.md
├── DESIGN_DOD.md
├── VERIFIER_RULES.md
├── references/
│   ├── apple-hig-baseline.md
│   ├── native-components.md
│   ├── design-tokens.md
│   ├── layout-spacing.md
│   ├── typography-color.md
│   ├── motion-materials.md
│   ├── accessibility.md
│   ├── testing.md
│   └── visual-review.md
├── templates/
│   ├── DesignTokens.swift
│   └── SCREENSHOT_REVIEW_PROMPT.md
└── verifier/
    ├── ios_design_verifier.py
    ├── verifier.config.json
    └── README.md
```

## Recommended installation

Cross-runtime:

```bash
mkdir -p ~/.agents/skills
cp -R skills/ios-native-design ~/.agents/skills/ios-native-design
```

Claude Code can also use:

```bash
mkdir -p ~/.claude/skills
cp -R skills/ios-native-design ~/.claude/skills/ios-native-design
```

For a project-specific copy:

```text
<repo>/.agents/skills/ios-native-design/
```

## Recommended agent workflow

```text
Requirement
  ↓
Interaction / navigation model
  ↓
Read relevant Apple HIG
  ↓
Choose native components
  ↓
Apply project tokens
  ↓
Implement SwiftUI
  ↓
Build + Preview matrix
  ↓
Capture screenshots
  ↓
Visual review
  ↓
Accessibility checks
  ↓
Static verifier + UI tests + snapshot tests
  ↓
Design DoD
```

## Key principle

> Agent freedom should be highest in content, illustration, data visualization, and brand moments — and lowest in navigation, controls, typography behavior, accessibility, and platform conventions.

This package intentionally separates:

1. **machine-verifiable constraints** — static verifier / CI
2. **render-verifiable constraints** — previews / screenshots
3. **human/product judgment** — hierarchy, focus, brand expression, delight

Do not convert subjective visual judgment into fake static checks.
