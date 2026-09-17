# iOS Native Design — Verifier Rules

The verifier is a **P2 guardrail**. Runtime evidence is the primary proof of UI quality.

This document separates rules by what can actually verify them.

## Rule classes

### STATIC
Can be checked from source with reasonable confidence.

### RENDER
Needs a rendered simulator/device screenshot. Prefer Device Hub full-resolution captures.

### INTERACTION
Needs the running app, device/simulator interaction, accessibility semantics/tree, or UI tests.

### JUDGMENT
Needs product/design reasoning across runtime evidence. Never pretend a regex can verify it.

## Priority

```text
P0  INTERACTION + high-fidelity RENDER
P1  deterministic UI regression
P2  STATIC + snapshot drift detection
```

A clean static verifier result does not imply design completion.

---

## Static rules

| ID | Severity | Rule | Default action |
|---|---|---|---|
| IOS-NATIVE-001 | fail | Feature code must not define raw RGB/HEX colors. Put legitimate brand colors in Theme/DesignTokens; use system semantic colors for system roles. | CI fail |
| IOS-NATIVE-002 | fail | Ordinary feature UI must not use `.font(.system(size: ...))` for body/control copy. Use Dynamic Type roles or approved typography tokens. | CI fail |
| IOS-NATIVE-003 | warn | Raw numeric `.padding(...)` should use a spacing token unless the value is required by an API or one-off geometry. | Review |
| IOS-NATIVE-004 | warn | Raw numeric `.cornerRadius(...)` should use a token or system container behavior. | Review |
| IOS-NATIVE-005 | warn | `.ignoresSafeArea()` requires deliberate full-bleed/media reasoning. | Review |
| IOS-NATIVE-006 | warn | Custom types named like `CustomTabBar`, `SegmentedControl`, `CustomToggle`, `CustomNavigationBar` may be recreating native controls. | Review |
| IOS-NATIVE-007 | warn | Repeated `.glassEffect` in ordinary content files may indicate material overuse. | Review |
| IOS-NATIVE-008 | warn | Explicit `.bouncy` on routine state changes should be intentional, not the default motion language. | Review |
| IOS-NATIVE-009 | info | `onTapGesture` used as a button substitute should be reviewed for semantics, accessibility behavior, and hit target. | Review |
| IOS-NATIVE-010 | info | Hard-coded frame sizes near interactive controls below 44 pt require hit-region verification. | Interaction check |

### Static exceptions

```swift
// ios-native-design: allow IOS-NATIVE-002 reason=Approved brand hero display type
Text(title)
    .font(.system(size: 54, weight: .bold))
```

Waivers require a rule ID and meaningful `reason=`.

---

## Render rules

| ID | Severity | Verify |
|---|---|---|
| IOS-RENDER-001 | blocker | Content is not clipped or hidden by safe-area/system UI. |
| IOS-RENDER-002 | blocker | Primary action and primary content remain visible and understandable at accessibility text sizes. |
| IOS-RENDER-003 | major | Visual hierarchy has a clear first, second, and third level. |
| IOS-RENDER-004 | major | Repeated margins, gaps, radii, and control styles are internally consistent. |
| IOS-RENDER-005 | major | Light and Dark appearances preserve hierarchy and legibility. |
| IOS-RENDER-006 | major | Brand color is selective; system content/navigation is not unnecessarily recolored. |
| IOS-RENDER-007 | major | Liquid Glass is not used as a generic content-card material. |
| IOS-RENDER-008 | major | A normal screen is not dominated by nested cards/containers. |
| IOS-RENDER-009 | major | Long strings and localization expansion do not break layout. |
| IOS-RENDER-010 | minor | Optical alignment of text, symbols, dividers, and controls feels deliberate. |
| IOS-RENDER-011 | minor | Empty state has appropriate emphasis without oversized decorative UI. |
| IOS-RENDER-012 | minor | Screen density is appropriate for the task and avoids unnecessary chrome. |

Use runtime screenshots. Prefer Device Hub captures for final evidence.

---

## Interaction rules

| ID | Severity | Verify |
|---|---|---|
| IOS-INT-001 | blocker | Effective interactive hit region is at least 44×44 pt on iOS/iPadOS. |
| IOS-INT-002 | blocker | VoiceOver/accessibility semantics expose understandable names for actionable elements. |
| IOS-INT-003 | blocker | Destructive actions have appropriate confirmation or recovery. |
| IOS-INT-004 | major | Reading/focus order follows visual order. |
| IOS-INT-005 | major | Reduce Motion removes/reduces problematic zoom, scale, repeated bounce, depth movement, or large spatial transitions. |
| IOS-INT-006 | major | Standard navigation gestures and dismissal behavior work in the running app. |
| IOS-INT-007 | major | Loading / disabled controls cannot accidentally trigger duplicate work. |
| IOS-INT-008 | major | Information conveyed by color has another cue. |
| IOS-INT-009 | major | Primary user flow completes through real tap/swipe/scroll/type interaction. |
| IOS-INT-010 | minor | Haptics and sound reinforce meaningful events and are not noisy. |

---

## Judgment rules

These require design review across runtime behavior and visual evidence:

### IOS-JUDGE-001 — Familiarity
Would an experienced iPhone user know how to navigate and act without instruction?

### IOS-JUDGE-002 — Simplicity
Did the design remove unnecessary decisions and chrome without hiding essential actions?

### IOS-JUDGE-003 — Hierarchy
Can a reviewer identify the screen's purpose, primary content, and primary action within a few seconds?

### IOS-JUDGE-004 — Craft
Do typography, spacing, alignment, iconography, states, copy, and motion feel intentionally related?

### IOS-JUDGE-005 — Brand restraint
Does the product feel branded mainly through content, typography, illustration/data visualization, selective color, and key moments rather than by replacing platform conventions?

### IOS-JUDGE-006 — Delight
Is delight the result of useful, coherent behavior and thoughtful moments rather than decorative effects?

---

## Environment matrix

For major screens use the applicable rows from `templates/DEVICE_TEST_MATRIX.md`.

At minimum consider:

| Dimension | Minimum |
|---|---|
| Appearance | Light, Dark |
| Text size | Default, one accessibility size |
| Content | Empty/normal/long as applicable |
| State | Loading/success/error as applicable |
| Device | Small + large/resized iPhone |
| Motion | Reduce Motion for motion-heavy screens |
| Contrast | Increased Contrast where styling is substantial |
| Input | Keyboard-present for input screens |
| Hardware | Physical device when behavior is hardware-dependent |

---

## CI policy

```text
Static FAIL rule → block PR
Static WARN rule → annotate PR
Runtime/screenshot Blocker → block PR
Runtime/screenshot Major → fix or document approved exception
Accessibility blocker → block PR
XCUI critical-path failure → block PR
Snapshot diff → require review, not automatic acceptance
```

Never auto-approve a snapshot merely because the new screenshot is different.

## Verifier output schema

```json
{
  "gate": "pass | fail",
  "findings": [
    {
      "rule": "IOS-NATIVE-002",
      "severity": "fail",
      "file": "Features/Home/HomeView.swift",
      "line": 42,
      "message": "Fixed system font size in feature UI",
      "suggestion": "Use a Dynamic Type style or approved typography token"
    }
  ]
}
```

Do not produce an overall aesthetic score.
