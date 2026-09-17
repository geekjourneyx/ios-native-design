---
name: ios-native-design
description: Use when designing, implementing, refactoring, testing, or reviewing an iPhone or iPad app whose SwiftUI interface needs to feel Apple-native, consistent, accessible, visually polished, or compliant with Apple Human Interface Guidelines.
---

# iOS Native Design

## Core principle

Build **with the platform, then verify in the running app**.

Prefer familiar Apple interaction models and system components. Put product identity primarily into content, illustration, data visualization, copy, selective color, and a few deliberate moments — not into reimplementing navigation or basic controls.

A UI task is not complete when it compiles, previews, or produces a screenshot. It is complete only after an agent or human has operated the rendered app and reviewed runtime evidence.

## Source of truth

In order of authority:

1. Current Apple Human Interface Guidelines and Apple Developer documentation.
2. Current SwiftUI and Xcode behavior for the project's actual deployment target.
3. The project's approved design tokens and component rules.
4. Existing approved screens in the same product.
5. External inspiration.

When an API, Device Hub capability, platform behavior, or HIG recommendation may have changed, verify current Apple documentation before implementing.

Read `references/apple-hig-baseline.md` first for new products or large redesigns.

## Verification priority

Use the highest-fidelity verification available:

1. **P0 — Agent-operated runtime verification**: launch the real app, drive its primary flows, inspect screenshots and accessibility semantics, vary environment settings, fix, and repeat.
2. **P0 — Runtime visual/accessibility evidence**: use Device Hub full-resolution screenshots and accessibility tree/semantics where available.
3. **P1 — Deterministic regression**: convert stable critical flows into XCUI tests; use physical-device smoke tests when hardware matters.
4. **P1 — Preview matrix**: use previews for fast state coverage and component iteration.
5. **P2 — Static verifier and snapshot tests**: prevent drift, but never treat them as proof of visual quality.

If runtime interaction is unavailable, fall back progressively to simulator/CLI/preview evidence and state the limitation.

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

Use semantic tokens for spacing, content widths, custom radii, brand colors, semantic status colors, custom motion values, and justified custom typography roles.

System semantic colors and Dynamic Type styles remain preferable to custom equivalents.

### 4. Motion and material pass

Read `references/motion-materials.md`.

Motion must communicate state, feedback, continuity, spatial relationship, progress, or direct manipulation.

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

### 6. Build and operate the running app — P0

Read `references/agent-device-testing.md`, `references/device-hub.md`, and `references/computer-use-testing.md`.

After a material UI change:

1. build and launch the app
2. choose the best available runtime driver:
   - Xcode agent simulator/device tools
   - a semantic iOS simulator tool such as ZCode `ios-simulator`
   - Computer Use driving Xcode + Device Hub
   - manual Device Hub interaction as fallback
3. execute the primary user flow with realistic tap / swipe / scroll / type interactions
4. inspect accessibility semantics/tree where available
5. capture Device Hub full-resolution screenshots at major checkpoints
6. vary the applicable environment: Light/Dark, Dynamic Type, contrast, screen size, orientation, Reduce Motion, locale/content states
7. review runtime behavior and screenshots
8. fix Blocker and Major findings
9. rerun the affected flow

Use `templates/AGENT_UI_TEST_PROMPT.md` and `templates/DEVICE_TEST_MATRIX.md`.

Do not declare design completion from source inspection, build success, preview success, or a single static screenshot.

### 7. Explore, then codify

Agent exploration is for discovery; regression tests are for repetition.

For new or changed flows:

```text
agent explores runtime
        ↓
finds reliable interaction path
        ↓
fixes product/design issues
        ↓
stable critical path
        ↓
encode as XCUI / deterministic regression
```

Do not require an LLM to rediscover the same stable path on every CI run.

### 8. Fast preview pass

Read `references/testing.md`.

Use previews for rapid state coverage:

- Light / Dark
- default / accessibility text
- empty / populated / long
- loading / error
- small / large layouts

Preview is a fast feedback tool, not runtime truth.

### 9. Static and snapshot guardrails

Run, as applicable:

- static design verifier
- snapshot regression
- shared-component call-site review

These guard against drift. They do not prove that the running app feels correct.

Finish with `DESIGN_DOD.md`.

## Capability routing

Prefer semantic tools over coordinate clicking when they provide equivalent control.

```text
Xcode native agent device/simulator tools available?
  → use them

Else semantic iOS simulator automation available?
  → use it

Else Computer Use available?
  → drive Xcode + Device Hub

Else
  → CLI + previews + manual screenshots
```

Use CLI/API for deterministic operations such as build, install, launch, device discovery, and repeatable test execution when available. Use Computer Use for visual exploration, system UI, and interactions that do not have a better semantic interface.

## Runtime evidence bundle

For a substantial UI change, preserve enough evidence to explain what was actually verified:

- flow or scenario tested
- device / simulator and OS
- runtime environment variants
- full-resolution screenshots for major checkpoints
- accessibility findings/tree observations where available
- Blocker / Major / Minor findings
- fixes made
- deterministic regression added or reason it was not added

The strongest review context combines:

```text
source code
+ interaction history
+ screenshot
+ accessibility semantics
+ environment state
```

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
14. A material UI change is incomplete until the running app has been operated and runtime evidence reviewed.
15. Accessibility is part of design quality, not a post-release task.
16. A screenshot captured from the Mac desktop is navigation evidence; prefer Device Hub's device-resolution capture for final visual evidence when available.
17. Hardware-dependent features require physical-device verification before calling that behavior complete.

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

## Agent output format for runtime/design reviews

Report:

### Runtime coverage
- device / simulator
- flow exercised
- environment variants
- evidence captured

### Blockers
Broken interaction, serious accessibility issues, content obscured, or strongly incorrect platform behavior.

### Major
Problems that materially reduce consistency, hierarchy, readability, platform fit, or task completion.

### Minor
Polish issues that are worth correcting but do not block the screen.

For each finding include:

- rule / principle
- runtime evidence
- affected screen or file
- smallest recommended change

### Regression
State which stable critical paths were encoded as deterministic tests.

Do not provide a fake numerical "design score".

## Reference routing

| Task | Read |
|---|---|
| New app / redesign | `apple-hig-baseline.md`, then relevant refs |
| Navigation / controls | `native-components.md` |
| Spacing / layout | `layout-spacing.md`, `design-tokens.md` |
| Typography / color | `typography-color.md` |
| Animation / glass | `motion-materials.md` |
| Accessibility | `accessibility.md` |
| Agent runtime verification | `agent-device-testing.md` |
| Xcode 27 Device Hub | `device-hub.md` |
| Computer Use fallback | `computer-use-testing.md` |
| Preview / XCUI / snapshots | `testing.md` |
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
- screenshot-only review without exercising the flow
- using Computer Use coordinate clicking when a reliable semantic tool exists
- repeatedly asking an LLM to execute a stable flow that should be an XCUI test

## Completion

A feature is design-complete only when the applicable items in `DESIGN_DOD.md` pass.
