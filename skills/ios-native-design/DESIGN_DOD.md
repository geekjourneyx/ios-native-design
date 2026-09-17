# iOS Native Design — Definition of Done

Use this as the final UI gate. Mark **N/A** only with a reason.

## A. Runtime verification — P0

- [ ] The changed app was built and launched, not only previewed.
- [ ] An agent or human exercised the primary affected flow in the running app.
- [ ] Tap / swipe / scroll / type interactions were tested where applicable.
- [ ] Major checkpoints have runtime screenshots; Device Hub full-resolution screenshots are preferred when available.
- [ ] Accessibility semantics/tree were inspected where available for critical controls and flow checkpoints.
- [ ] The affected flow was rerun after the final design fix.
- [ ] Hardware-dependent behavior was smoke-tested on a physical device where required.

## B. Environment matrix — P0/P1

- [ ] Light appearance checked in the running app.
- [ ] Dark appearance checked in the running app.
- [ ] At least one accessibility Dynamic Type size checked.
- [ ] Small and large/resized iPhone layout checked where layout is affected.
- [ ] Increased Contrast checked where custom visual styling is substantial.
- [ ] Reduce Motion checked for motion-heavy flows.
- [ ] Keyboard-present layout checked for input flows.
- [ ] Long content / localization expansion checked where text is material.
- [ ] Orientation, iPad, RTL, permissions, or other environment states checked when applicable.

## C. Platform fit

- [ ] Navigation uses the expected iOS pattern.
- [ ] Native SwiftUI components are used where they adequately express the behavior.
- [ ] Any custom recreation of a standard control has a documented product reason.
- [ ] Standard actions use SF Symbols unless custom iconography is part of the product identity.
- [ ] System behaviors such as swipe-back, sheet dismissal, keyboard avoidance, focus, and safe areas work naturally at runtime.
- [ ] Destructive and irreversible actions use appropriate confirmation / recovery patterns.

## D. Visual hierarchy

- [ ] The primary task is understandable within a few seconds.
- [ ] The screen has one clear visual focus.
- [ ] Primary, secondary, and tertiary actions are visually distinguishable.
- [ ] Repeated content uses a consistent structure.
- [ ] Empty space is intentional; density is not created by unnecessary containers.
- [ ] Cards are used because they create meaningful grouping, not because every section needs a background.
- [ ] The interface remains coherent when content is longer than expected.

## E. Layout and spacing

- [ ] Safe areas are respected.
- [ ] Alignment follows a small number of consistent guides.
- [ ] Feature views use approved spacing tokens or system spacing.
- [ ] There are no unexplained "magic" padding, gap, or radius values.
- [ ] Resizing or device-size changes do not expose clipping or broken constraints.

## F. Typography

- [ ] Ordinary UI text uses Dynamic Type-compatible styles.
- [ ] Fixed font sizes are limited to justified brand / display cases.
- [ ] Text hierarchy is clear without relying only on color.
- [ ] Body text remains comfortably legible.
- [ ] Text does not clip at large accessibility sizes.
- [ ] Important labels survive localization expansion.

## G. Color and material

- [ ] System-role colors use semantic system colors.
- [ ] Brand colors come from shared semantic tokens.
- [ ] Light and Dark runtime captures preserve hierarchy and legibility.
- [ ] Color is not the sole carrier of state or meaning.
- [ ] Liquid Glass is primarily used for controls/navigation rather than ordinary content surfaces.
- [ ] Accent color is used selectively rather than washing the entire UI in brand color.

## H. Interaction

- [ ] Every tappable control exposes an effective hit region of at least 44×44 pt.
- [ ] Custom buttons have a visible pressed state.
- [ ] Interactive states are obvious: enabled, disabled, selected, loading, destructive.
- [ ] Gesture behavior follows the visual / spatial model.
- [ ] Core functionality does not depend on hidden gestures alone.
- [ ] Haptics, when used, reinforce meaningful events rather than every tap.
- [ ] Loading/disabled controls cannot accidentally trigger duplicate work.

## I. Motion

- [ ] Motion communicates state, feedback, continuity, spatial relationship, or progress.
- [ ] Decorative animation does not compete with content.
- [ ] Navigation uses system transitions unless a custom transition has a real product reason.
- [ ] Repeated bounce / zoom / scale effects are avoided.
- [ ] Reduce Motion has been checked in the running app where relevant.
- [ ] Important information remains understandable with animation disabled or reduced.

## J. Accessibility

- [ ] VoiceOver labels are meaningful.
- [ ] VoiceOver reading order is logical.
- [ ] Custom controls expose correct accessibility traits / values.
- [ ] Contrast remains sufficient in light and dark appearances.
- [ ] Differentiate Without Color / non-color cues are supported where state depends on color.
- [ ] Accessibility Inspector has no unresolved blocker-level issues.
- [ ] Runtime accessibility semantics agree with what is visually presented.

## K. Screen states

Check every state that applies:

- [ ] Loading
- [ ] Empty
- [ ] Populated
- [ ] Error
- [ ] Offline / unavailable
- [ ] Permission denied
- [ ] Long content
- [ ] Large data set
- [ ] Destructive confirmation
- [ ] Success / completion

## L. Regression and guardrails

- [ ] Stable critical paths discovered during exploration are encoded as XCUI tests, or there is a reason not to.
- [ ] Critical XCUI flow passes.
- [ ] Static design verifier ran.
- [ ] Preview matrix rendered for fast state coverage.
- [ ] Snapshot regression passed where snapshots are maintained.
- [ ] Changed shared components were checked in all major call sites.

## Required evidence for a major UI PR

Attach or link:

1. affected runtime flow/scenario
2. after screenshots from the running app at major checkpoints
3. before screenshot when modifying an existing screen
4. Light + Dark for visually substantial changes
5. accessibility Dynamic Type evidence for text-heavy screens
6. short note for every intentional deviation from native defaults
7. deterministic regression added, or why the flow remains exploratory/manual

## Release gate

A screen may ship when:

- applicable P0 runtime verification is complete
- no unresolved **Blocker** runtime or screenshot-review findings remain
- no unresolved accessibility blockers remain
- any **Major** exception has an explicit product/design rationale
- stable critical flows have deterministic regression coverage where practical
