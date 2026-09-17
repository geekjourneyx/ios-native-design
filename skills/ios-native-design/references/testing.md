# UI testing and design verification

No single test type proves design quality. Prefer the highest-fidelity evidence available and move stable discoveries into deterministic regression.

## Priority order

```text
P0  Agent-operated runtime exploration
P0  Device Hub screenshots + accessibility semantics
P1  XCUI regression + physical-device smoke tests
P1  Preview matrix
P2  Static verifier + snapshot tests
```

## 1. Build and launch

Confirm the intended target builds and launch the app. A successful build proves compilation, not design quality.

Use deterministic CLI/API mechanisms for build/install/launch when they are reliable; use Device Hub or other runtime tools for visual and interaction verification.

## 2. Agent runtime exploration — P0

Read `agent-device-testing.md`.

Exercise the affected flow as a real user:

- tap
- swipe
- scroll
- type
- navigate
- dismiss/present
- trigger loading/error/empty states when practical

Capture evidence at major checkpoints and inspect accessibility semantics/tree where available.

## 3. Device Hub environment verification — P0

Read `device-hub.md`.

For major screens, cover the applicable matrix:

```text
Light / Dark
Default text / Accessibility text
Normal / Long content
Loading / Empty / Error
Small / resized / large iPhone
Increased Contrast
Reduce Motion
Keyboard / permissions when relevant
```

Use Device Hub's device-resolution Screenshot control for final visual evidence when available.

## 4. Explore → codify — P1

Agent exploration is useful for discovering broken flows and reliable interaction paths.

Once a critical path is stable, encode it as XCUI so ordinary CI does not require an LLM to rediscover it.

Automate business-critical:

- launch/onboarding
- primary task
- save/submit
- navigation
- destructive actions
- permissions when practical
- error recovery

Use stable accessibility identifiers for test-critical elements.

## 5. Physical-device smoke tests — P1

Simulator/Device Hub cannot reproduce every hardware-specific feature.

Use a physical device for behavior depending on hardware, sensors, media capture, telephony/VoIP constraints, Bluetooth, performance, or other device-specific APIs.

## 6. Preview matrix — P1

Previews remain valuable for rapid state coverage:

```text
Light / Dark
Default text / Accessibility text
Empty / Normal / Long
Loading / Error
```

Add RTL, iPad, keyboard, permission, or high-contrast fixtures when applicable.

Preview is fast feedback, not runtime truth.

## 7. Static verifier — P2

```bash
python3 verifier/ios_design_verifier.py <project-path>
```

Use it for enforceable drift: raw colors, fixed font sizes, magic spacing/radii, and likely native-control recreation.

A pass means "no configured static violation found", not "the UI is good".

## 8. Snapshot tests — P2

Snapshot tests protect shared components and stable screens from accidental drift.

A snapshot diff is a review request, not proof the new design is correct.

A common Swift option is:
https://github.com/pointfreeco/swift-snapshot-testing

## Evidence hierarchy

Prefer this combined evidence:

```text
running behavior
+ interaction history
+ Device Hub screenshot
+ accessibility semantics
+ environment state
+ source code
```

A Mac desktop screenshot is useful for navigation/Computer Use, but Device Hub's own screenshot is preferred for final visual evidence because it captures the simulated or physical device at device resolution.
