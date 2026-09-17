# iOS Native Design — Definition of Done

Use this as the final UI gate. Mark **N/A** only with a reason.

## A. Platform fit

- [ ] Navigation uses the expected iOS pattern.
- [ ] Native SwiftUI components are used where they adequately express the behavior.
- [ ] Any custom recreation of a standard control has a documented product reason.
- [ ] Standard actions use SF Symbols unless custom iconography is part of the product identity.
- [ ] System behaviors such as swipe-back, sheet dismissal, keyboard avoidance, focus, and safe areas still work naturally.
- [ ] Destructive and irreversible actions use appropriate confirmation / recovery patterns.

## B. Visual hierarchy

- [ ] The primary task is understandable within a few seconds.
- [ ] The screen has one clear visual focus.
- [ ] Primary, secondary, and tertiary actions are visually distinguishable.
- [ ] Repeated content uses a consistent structure.
- [ ] Empty space is intentional; density is not created by unnecessary containers.
- [ ] Cards are used because they create meaningful grouping, not because every section needs a background.
- [ ] The interface remains coherent when content is longer than expected.

## C. Layout and spacing

- [ ] Safe areas are respected.
- [ ] Alignment follows a small number of consistent guides.
- [ ] Feature views use approved spacing tokens or system spacing.
- [ ] There are no unexplained "magic" padding, gap, or radius values.
- [ ] Small and large iPhone layouts were checked.
- [ ] Keyboard-present layouts were checked for input screens.
- [ ] Landscape / iPad behavior was checked when the product supports it.

## D. Typography

- [ ] Ordinary UI text uses Dynamic Type-compatible styles.
- [ ] Fixed font sizes are limited to justified brand / display cases.
- [ ] Text hierarchy is clear without relying only on color.
- [ ] Body text remains comfortably legible.
- [ ] Text does not clip at large accessibility sizes.
- [ ] Important labels survive localization expansion.

## E. Color and material

- [ ] System-role colors use semantic system colors.
- [ ] Brand colors come from shared semantic tokens.
- [ ] Light Mode was visually checked.
- [ ] Dark Mode was visually checked.
- [ ] Increased Contrast was checked where relevant.
- [ ] Color is not the sole carrier of state or meaning.
- [ ] Liquid Glass is primarily used for controls/navigation rather than ordinary content surfaces.
- [ ] Accent color is used selectively rather than washing the entire UI in brand color.

## F. Interaction

- [ ] Every tappable control exposes an effective hit region of at least 44×44 pt.
- [ ] Custom buttons have a visible pressed state.
- [ ] Interactive states are obvious: enabled, disabled, selected, loading, destructive.
- [ ] Gesture behavior follows the visual / spatial model.
- [ ] Core functionality does not depend on hidden gestures alone.
- [ ] Haptics, when used, reinforce meaningful events rather than every tap.

## G. Motion

- [ ] Motion communicates state, feedback, continuity, spatial relationship, or progress.
- [ ] Decorative animation does not compete with content.
- [ ] Navigation uses system transitions unless a custom transition has a real product reason.
- [ ] Repeated bounce / zoom / scale effects are avoided.
- [ ] Reduce Motion has been checked.
- [ ] Important information remains understandable with animation disabled or reduced.

## H. Accessibility

- [ ] VoiceOver labels are meaningful.
- [ ] VoiceOver reading order is logical.
- [ ] Custom controls expose correct accessibility traits / values.
- [ ] Dynamic Type was tested at an accessibility size.
- [ ] Contrast remains sufficient in light and dark appearances.
- [ ] Differentiate Without Color / non-color cues are supported where state depends on color.
- [ ] Reduce Motion behavior is implemented.
- [ ] Accessibility Inspector has no unresolved blocker-level issues.

## I. Screen states

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

## J. Verification

- [ ] Project builds with no new UI-related warnings.
- [ ] Static design verifier ran.
- [ ] Preview matrix rendered.
- [ ] Core screen screenshots were captured.
- [ ] Screenshot review found no unresolved blockers or majors.
- [ ] Critical XCUI flow passed.
- [ ] Snapshot regression passed where snapshots are maintained.
- [ ] Changed shared components were checked in all major call sites.

## Required evidence for a major UI PR

Attach or link:

1. before screenshot, when modifying an existing screen
2. after screenshot
3. Light + Dark for visually substantial changes
4. large Dynamic Type screenshot for text-heavy screens
5. short note for every intentional deviation from native defaults

## Release gate

A screen may ship when:

- all applicable blocker items pass
- no unresolved **Blocker** screenshot-review findings remain
- no unresolved accessibility blockers remain
- any **Major** exception has an explicit product/design rationale
