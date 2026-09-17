# Agent UI Test Prompt

Use this after a material SwiftUI implementation or design change.

---

Operate the **running app**, not only the source or Preview.

## Goal

Verify the affected user flow end-to-end and collect runtime evidence before declaring the UI complete.

## Tool selection

Use the best available path:

1. Xcode native agent simulator/device tools.
2. Semantic iOS simulator automation.
3. Computer Use driving Xcode + Device Hub.
4. Manual Device Hub fallback.

Prefer CLI/semantic tools for deterministic build/install/launch/test steps. Use Computer Use for visual exploration and GUI-only controls.

## Execute

1. Build and launch the app.
2. Navigate to the affected flow.
3. Complete the primary task using realistic tap / swipe / scroll / type interactions.
4. Inspect accessibility semantics/tree for critical controls when available.
5. Capture a Device Hub full-resolution screenshot at every major checkpoint.
6. Run applicable variants from `DEVICE_TEST_MATRIX.md`.
7. Inspect:
   - task completion
   - native platform behavior
   - visual hierarchy
   - alignment and spacing
   - typography
   - color/material
   - loading/disabled/selected states
   - keyboard behavior
   - clipping/overflow
   - accessibility
8. Record Blocker / Major / Minor findings.
9. Fix Blocker and Major findings.
10. Rebuild/relaunch when needed and rerun the affected path.
11. Once a critical path is stable, encode it as an XCUI regression test when practical.

## Evidence

Report:

### Runtime coverage
- device/simulator:
- OS:
- flow:
- variants:
- screenshots:
- accessibility evidence:

### Blockers
- Evidence:
- Why it matters:
- Smallest fix:

### Major
...

### Minor
...

### Regression
- XCUI test added:
- If not, reason:

Do not claim design completion from build success, Preview success, or source inspection alone.
