# Agent-operated device testing

Use this for material UI work whenever the agent can operate a simulator, Device Hub, or physical device.

## Why this is P0

Source inspection can catch implementation mistakes. Previews can expose static state problems. Neither proves that the user can actually complete the flow.

The highest-value verifier is the running app.

Xcode 27 agents can interact with a running app — tapping, swiping, scrolling, typing — and can receive screenshots plus accessibility tree / semantic information. Use that capability for exploratory verification, then encode stable critical paths as deterministic tests.

## Capability routing

Choose the highest-level reliable interface:

1. Xcode native agent simulator/device tools.
2. Semantic iOS simulator automation, such as ZCode `ios-simulator`.
3. Computer Use driving Xcode + Device Hub.
4. Manual Device Hub interaction.
5. Preview/screenshot fallback when runtime operation is unavailable.

Prefer semantic tools to coordinate clicking. They are more robust and expose richer state.

## Runtime loop

For each material UI change:

```text
build
  ↓
launch
  ↓
exercise primary flow
  ↓
inspect accessibility tree/semantics + screenshots
  ↓
change environment
  ↓
exercise again
  ↓
find Blocker / Major issues
  ↓
fix
  ↓
rerun affected path
  ↓
stable critical path?
  ↓
encode XCUI regression
```

## What to explore

Do not only follow the happy path.

Where applicable test:

- primary task
- back/dismiss navigation
- scroll boundaries
- keyboard presentation/dismissal
- repeated taps while loading
- empty state
- long content
- failure/retry
- destructive confirmation
- permission denied
- disabled state
- interrupted state
- state restoration where important

## Evidence checkpoints

At each meaningful screen capture:

- current task/step
- expected state
- observed state
- accessibility tree role/label/value for critical elements when available
- full-resolution screenshot
- issue severity if something is wrong

## Explore first, codify second

Exploratory agent testing is best for:

- finding unknown UI problems
- trying edge cases
- understanding a new flow
- evaluating visual polish
- discovering a reliable path

XCUI is best for:

- stable critical paths
- CI repetition
- preventing regression
- known interaction invariants

Do not use an expensive exploratory agent run as a substitute for a deterministic test once the path is known.

## Physical device escalation

Escalate from simulator to physical device when verification depends on:

- camera / microphone / media capture
- Bluetooth or nearby-device behavior
- sensors
- hardware performance
- telephony / VoIP behavior
- device-only permissions or entitlements
- any API unavailable or materially different in simulation
