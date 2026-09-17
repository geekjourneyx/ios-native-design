# Computer Use testing

Computer Use is a runtime driver, not a replacement for semantic tools.

Use it when the agent can see and operate macOS applications and there is no more reliable structured interface for the task.

## Preferred split

```text
deterministic operation
  → CLI / API / semantic tool

visual or GUI-only operation
  → Computer Use
```

Examples:

### Prefer CLI / semantic tool
- build
- install
- launch
- select a known simulator when an API/tool exists
- run XCUI tests
- query test results
- repeat a stable critical path

### Prefer Computer Use
- explore an unfamiliar flow
- operate Device Hub controls not exposed semantically
- inspect the actual visual hierarchy
- change GUI environment controls
- reproduce a visual bug
- capture a Device Hub screenshot
- navigate Xcode when required by a tool/workflow

## Coordinate-clicking rule

Do not choose coordinate clicking merely because it is possible.

Prefer:

1. accessibility/semantic target
2. named UI element
3. stable visual target
4. raw coordinate only as last resort

If the interface moved and the click target is uncertain, reacquire the screen before clicking.

## Screenshot workflow

Computer Use may capture the Mac display so the agent can navigate.

For final iOS visual evidence:

1. navigate Device Hub to the target state
2. use Device Hub's Screenshot action
3. use the saved device-resolution file for review/comparison
4. keep the desktop screenshot only as operational context

## Failure recovery

If a GUI step fails:

- inspect current state instead of retrying blind coordinates
- determine whether a modal, build state, keyboard, or focus changed
- use semantic tools to recover when possible
- reset to a known app state before resuming

## Safety

Avoid destructive Xcode/device operations unless they are required by the test plan. Do not erase devices, reset content/settings, revoke signing, or modify production credentials merely to recover a test.
