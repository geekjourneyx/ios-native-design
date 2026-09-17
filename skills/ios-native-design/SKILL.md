---
name: ios-native-design
description: Use when designing, implementing, refactoring, or reviewing an iPhone or iPad app whose SwiftUI interface needs to feel Apple-native, consistent, accessible, visually polished, or compliant with Apple Human Interface Guidelines.
---

# iOS Native Design

## Core principle

Build **with the platform, not on top of it**.

Prefer familiar Apple interaction models and system components. Put product identity primarily into content, illustration, data visualization, copy, selective color, and a few deliberate moments — not into reimplementing navigation or basic controls.

A UI task is not complete when it compiles. It is complete only after the rendered result has been inspected.

## Source of truth

In order of authority:

1. Current Apple Human Interface Guidelines and Apple Developer documentation.
2. Current SwiftUI APIs for the project's actual deployment target.
3. The project's approved design tokens and component rules.
4. Existing approved screens in the same product.
5. External inspiration.

When an API, platform behavior, or HIG recommendation may have changed, verify the current Apple documentation before implementing.

Read `references/apple-hig-baseline.md` first for new products or large redesigns.

## Required workflow

### 1. Establish the screen contract

Before writing UI code, identify:

- primary user goal
- primary action
- navigation model
- screen states: loading, empty, populated, error, long-content
- destructive / irreversible actions
- minimum supported iOS version
- whether the screen is content-heavy, task-heavy, or media-heavy

Do not begin by choosing colors or card styles.

### 2. Native-component pass

Read `references/native-components.md`.

For every control or container, ask:

> Does SwiftUI already provide the behavior?

Prefer the native implementation if the answer is yes.

Do not recreate standard navigation, tabs, toggles, segmented controls, search, menus, alerts, sheets, date pickers, progress indicators, or standard buttons merely for visual novelty.

Custom UI requires a concrete product reason.

### 3. Token pass

Read `references/design-tokens.md`, `references/layout-spacing.md`, and `references/typography-color.md`.

Feature views must not invent a parallel design system.

Use semantic tokens for:

- spacing
- content widths
- radii where custom radii are genuinely needed
- brand colors
- semantic status colors
- custom motion values
- custom typography roles

System semantic colors and Dynamic Type styles remain preferable to custom equivalents.

### 4. Motion and material pass

Read `references/motion-materials.md`.

Motion must communicate one of:

- state
- feedback
- continuity
- spatial relationship
- progress

Do not add motion solely to make the UI look "premium".

Use Liquid Glass primarily as the functional layer for controls and navigation. Do not turn content cards into a field of glass surfaces.

### 5. Accessibility pass

Read `references/accessibility.md`.

At minimum verify:

- 44×44 pt interactive hit region
- Dynamic Type
- VoiceOver labels / values / traits where needed
- sufficient contrast
- information is not conveyed by color alone
- Reduce Motion behavior
- logical focus and reading order
- usable layout at accessibility text sizes

### 6. Render before judging

Every material UI change must be rendered in a preview, simulator, or device.

Do not claim visual completion from source inspection alone.

For substantial changes:

1. capture the target screen
2. run `templates/SCREENSHOT_REVIEW_PROMPT.md`
3. fix blocker and major findings
4. render again

Read `references/visual-review.md`.

### 7. Test and verify

Read `references/testing.md`.

Run, as applicable:

- build
- preview matrix
- static design verifier
- accessibility inspection
- critical XCUI flows
- snapshot regression
- screenshot review

Finish with `DESIGN_DOD.md`.

## Hard constraints

Unless the product requirement explicitly justifies an exception:

1. Native component first.
2. Do not redraw system navigation or controls for style alone.
3. Prefer SF Symbols for standard system actions.
4. Prefer semantic system colors for system roles.
5. Do not hard-code a system-role color as RGB/HEX.
6. Prefer Dynamic Type text styles to fixed font sizes.
7. Interactive targets must expose at least a 44×44 pt hit region on iOS/iPadOS.
8. Respect safe areas and system layout behavior.
9. Feature screens may not create arbitrary spacing, radius, color, or animation systems.
10. Use one clear dominant primary action in a normal screen unless the interaction clearly requires otherwise.
11. Liquid Glass belongs primarily to controls/navigation, not ordinary content surfaces.
12. Motion must remain understandable with Reduce Motion enabled.
13. Loading, empty, error, long-content, and populated states must be intentionally designed where applicable.
14. A UI change is incomplete until the rendered output is visually reviewed.
15. Accessibility is part of design quality, not a post-release task.

## Exception protocol

If a rule must be broken:

1. State the user/product reason.
2. Prefer the smallest exception.
3. Preserve accessibility and platform behavior.
4. Document the exception near the implementation.
5. Add a regression test when the exception affects interaction.

For static verifier exceptions:

```swift
// ios-native-design: allow IOS-NATIVE-003 reason=Brand hero typography approved by design
```

Never use an exception merely to silence a warning.

## Agent output format for design reviews

Report findings in this order:

### Blockers
Violations likely to create broken interaction, serious accessibility issues, or strongly non-native behavior.

### Major
Problems that materially reduce consistency, hierarchy, readability, or platform fit.

### Minor
Polish issues that are worth correcting but do not block the screen.

For each finding include:

- rule / principle
- evidence
- affected screen or file
- smallest recommended change

Do not provide a fake numerical "design score".

## Reference routing

| Task | Read |
|---|---|
| New app / redesign | `apple-hig-baseline.md`, then all relevant refs |
| Navigation / controls | `native-components.md` |
| Spacing / layout | `layout-spacing.md`, `design-tokens.md` |
| Typography / color | `typography-color.md` |
| Animation / glass | `motion-materials.md` |
| Accessibility | `accessibility.md` |
| Previews / tests | `testing.md` |
| Screenshot critique | `visual-review.md` |
| Final gate | `DESIGN_DOD.md`, `VERIFIER_RULES.md` |

## Anti-patterns

Reject these defaults:

- card inside card inside card
- every section uses a rounded rectangle
- every surface uses blur/glass
- every button is a large branded capsule
- custom tab bar with manually positioned icons when `TabView` fits
- custom segmented control when `Picker` fits
- multiple unrelated accent colors
- raw numeric spacing scattered across feature views
- fixed font sizes for ordinary UI copy
- icons from a second visual language when SF Symbols already cover the action
- decorative animation on every state change
- hiding core actions to make the screen look "minimal"
- source-only UI review without rendering

## Completion

A feature is design-complete only when the applicable items in `DESIGN_DOD.md` pass.
