<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="ios-native-design — an Apple-native design harness for SwiftUI coding agents">
</p>

<p align="center">
  <a href="https://skills.sh/geekjourneyx/ios-native-design"><img src="https://skills.sh/b/geekjourneyx/ios-native-design" alt="skills.sh installs"></a>
</p>

<p align="center">
  <strong>Stop asking coding agents to “make it look more Apple”. Give them constraints they can verify.</strong>
</p>

`ios-native-design` is a reusable design-engineering Skill for building and reviewing SwiftUI apps. It turns Apple HIG, native component choices, semantic tokens, accessibility, screenshot review, and UI regression checks into one repeatable agent workflow.

## Install

```bash
npx skills add geekjourneyx/ios-native-design
```

The repo contains one Skill, so that is the shortest path. To select it explicitly:

```bash
npx skills add geekjourneyx/ios-native-design --skill ios-native-design
```

Install globally when you want it available across projects:

```bash
npx skills add geekjourneyx/ios-native-design -g
```

## Why this exists

AI coding agents can produce SwiftUI that compiles while still feeling visually inconsistent or un-iOS-like:

- every screen invents new spacing and corner radii
- fixed font sizes replace Dynamic Type
- HEX colors replace semantic system colors
- custom tab bars and toggles recreate native controls
- every section becomes a rounded card
- Liquid Glass becomes decoration instead of a functional layer
- UI is considered “done” before anyone looks at the rendered result

The answer is not a longer style prompt. It is a **Design Harness**.

```text
Product requirement
        ↓
Apple HIG + native component decision
        ↓
Semantic design tokens
        ↓
SwiftUI implementation
        ↓
Preview / simulator render
        ↓
Screenshot review
        ↓
Accessibility + interaction checks
        ↓
Static verifier + XCUI + snapshots
        ↓
Design Definition of Done
```

## Four kinds of design rules

A core idea of this Skill is to avoid pretending every design decision can be linted.

| Rule class | What it catches | Example |
|---|---|---|
| **STATIC** | Source-level drift | fixed font size, raw color, magic padding |
| **RENDER** | Problems visible only after rendering | weak hierarchy, card overload, broken Dark Mode |
| **INTERACTION** | Runtime and accessibility behavior | 44×44 hit target, VoiceOver, Reduce Motion |
| **JUDGMENT** | Product/design decisions | familiarity, simplicity, brand restraint, delight |

Static rules should be automated. Visual judgment should be based on screenshots, not regexes.

## Native first

The default rule is simple:

> If SwiftUI already provides the platform behavior, use the native component unless the product has a concrete reason not to.

That means preferring `NavigationStack`, `TabView`, `Toggle`, `Picker`, `.searchable`, `.sheet`, `.alert`, `Menu`, `ProgressView`, `DatePicker`, `Button`, and SF Symbols before rebuilding equivalents from stacks, capsules, offsets, and gestures.

The goal is not “generic Apple UI”. Agent freedom should be **low** in navigation, controls, accessibility, and platform behavior — and **high** in content, illustration, data visualization, editorial composition, and deliberate brand moments.

## What is inside

```text
skills/ios-native-design/
├── SKILL.md                 # agent workflow + hard constraints
├── DESIGN_DOD.md            # final design Definition of Done
├── VERIFIER_RULES.md        # STATIC / RENDER / INTERACTION / JUDGMENT rules
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

## Verifier

The included verifier intentionally checks only source-level signals that are reasonable to automate.

```bash
python3 skills/ios-native-design/verifier/ios_design_verifier.py /path/to/ios-project
```

Example failures:

```swift
Text("Hello")
    .font(.system(size: 15))
    .padding(17)
    .foregroundStyle(Color(hex: "#121212"))
```

Typical findings:

```text
IOS-NATIVE-001  raw RGB / HEX color
IOS-NATIVE-002  fixed system font size
IOS-NATIVE-003  raw numeric padding
```

A legitimate exception must explain itself:

```swift
// ios-native-design: allow IOS-NATIVE-002 reason=Approved brand hero display type
Text(title)
    .font(.system(size: 54, weight: .bold))
```

## Screenshot review loop

Source code cannot tell you whether a screen actually has strong hierarchy or feels visually coherent.

For substantial UI work, the Skill requires this loop:

```text
Implement → Render → Screenshot → Review → Fix → Render again
```

The review prompt explicitly checks for:

- hierarchy and primary focus
- platform familiarity
- spacing and alignment
- typography consistency
- accent-color restraint
- SF Symbols / icon consistency
- nested-card overload
- Liquid Glass misuse
- long-content and localization risk
- accessibility risks visible in the render

No fake “design score” is produced. Findings are classified as **Blocker / Major / Minor**.

## Design Definition of Done

A material UI change is not finished at `BUILD SUCCEEDED`.

The included DoD covers:

- platform fit
- visual hierarchy
- layout and spacing
- typography
- color and materials
- interaction states
- motion and Reduce Motion
- accessibility and VoiceOver
- loading / empty / error / long-content states
- preview, screenshot, XCUI, and snapshot verification

See [`DESIGN_DOD.md`](./skills/ios-native-design/DESIGN_DOD.md).

## Use it with an agent

After installation, ask your coding agent to apply the Skill to new UI or an existing screen, for example:

```text
Use ios-native-design to audit this SwiftUI screen.
Render it first, then report Blocker / Major / Minor findings and fix the highest-leverage issues.
```

Or during implementation:

```text
Implement this screen using ios-native-design.
Prefer native SwiftUI components, use semantic tokens, create the required preview states,
and do not call the UI complete until the rendered screenshot has been reviewed.
```

## Design philosophy

1. **Apple-native, not Apple-looking.** Platform behavior matters more than decorative resemblance.
2. **Native component first.** Custom controls need a product reason.
3. **Semantic over arbitrary.** Prefer Dynamic Type, system colors, SF Symbols, and meaningful tokens.
4. **Accessibility is design quality.** It is part of the default pass, not a release checklist afterthought.
5. **Render before judging.** Source inspection is not visual review.
6. **Automate what is objective.** Leave hierarchy, craft, and brand judgment to rendered review.
7. **Exceptions need evidence.** Deviating from the default path should be explicit and reviewable.

## Primary references

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple Design Resources](https://developer.apple.com/design/resources/)
- [Apple SF Symbols](https://developer.apple.com/sf-symbols/)
- [SwiftUI](https://developer.apple.com/xcode/swiftui/)
- [skills CLI](https://www.skills.sh/docs/cli)

---

<p align="center"><sub>Built as design engineering infrastructure for AI-assisted iOS development.</sub></p>
