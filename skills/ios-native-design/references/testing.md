# UI testing and design verification

No single test type proves design quality.

## 1. Build
Confirm the intended target builds. This catches implementation problems, not visual quality.

## 2. Preview matrix
For important screens cover:

```text
Light / Dark
Default text / Accessibility text
Empty / Normal / Long
Loading / Error
Small iPhone / Large iPhone
```

Add RTL, iPad, keyboard, permission, or high-contrast states when applicable.

## 3. Static verifier

```bash
python3 verifier/ios_design_verifier.py <project-path>
```

Use it for enforceable drift: raw colors, fixed font sizes, magic spacing/radii, and likely native-control recreation.

## 4. Screenshot review
Render, capture, review with `templates/SCREENSHOT_REVIEW_PROMPT.md`, fix Blocker/Major issues, then render again.

## 5. Accessibility
Use Accessibility Inspector, VoiceOver, Dynamic Type, and Reduce Motion checks for critical flows.

## 6. XCUI
Automate business-critical launch/onboarding, primary task, save/submit, navigation, destructive actions, permissions when practical, and error recovery.

## 7. Snapshots
Snapshot tests protect shared components and stable screens from accidental drift. A snapshot diff is a review request, not proof the new design is correct.

A common Swift option is https://github.com/pointfreeco/swift-snapshot-testing
