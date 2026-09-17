# Runtime visual review

Static source cannot determine whether an iOS flow actually feels polished or behaves correctly. A single screenshot is also insufficient for interaction-heavy work.

For material UI changes, review the **running app** and combine visual evidence with what happened immediately before and after the capture.

## Preferred evidence bundle

Use as much of this bundle as the runtime exposes:

```text
interaction history
+ Device Hub full-resolution screenshot
+ accessibility tree / semantics
+ environment state
+ relevant source
```

A Computer Use screenshot of the Mac is useful for locating Xcode/Device Hub controls. For final visual evidence, prefer Device Hub's own device-resolution Screenshot capture when available.

## Review order

### 1. Task completion

Can the user actually complete the intended flow? Verify the path with taps, swipes, scrolls, typing, presentation/dismissal, and back navigation where applicable.

A beautiful screenshot of a broken flow is a Blocker.

### 2. Purpose

Can you tell what the current screen is for and what the user should do next?

### 3. Focus

What attracts the eye first? Is it the right content or action for the current runtime state?

### 4. Hierarchy

Are primary content, supporting content, metadata, and primary/secondary actions distinguishable?

### 5. Platform familiarity

Do navigation, controls, sheets, menus, search, keyboard behavior, and dismissal read and behave as recognizable iOS patterns?

### 6. Semantic agreement

Compare the rendered UI with the accessibility semantics/tree when available.

Look for mismatches such as:

- an element visually reads as a button but exposes no actionable semantic role
- a selected state is visible but not represented semantically
- a meaningful image or control has a weak/missing label
- visual order and accessibility reading order disagree
- a disabled/loading control still exposes an inappropriate action

### 7. Density

Is complexity coming from the task, or from unnecessary cards, labels, separators, controls, materials, and chrome?

### 8. Alignment and spacing

Are there stable leading/trailing edges and consistent relationships between related elements? Look for optical misalignment in symbols, labels, dividers, and controls.

### 9. Typography

Are text roles consistent? Does the hierarchy survive long content and an accessibility Dynamic Type size without clipping or accidental competition?

### 10. Color and material

Is accent color selective? Is muted content still legible in Light/Dark? Does Liquid Glass/material establish a functional layer instead of decorating ordinary content surfaces?

### 11. State coherence

Exercise applicable loading, empty, error, selected, disabled, success, permission-denied, and long-content states. They should look like one product and preserve the primary task.

### 12. Motion

Watch the transition in the running app. Does it explain state/continuity or merely attract attention? Recheck motion-heavy paths with Reduce Motion enabled.

### 13. Environment variants

For substantial changes, review the applicable Device Hub/runtime matrix rather than one default state:

- Light / Dark
- default / accessibility text
- small / resized / large iPhone
- normal / long content
- loading / empty / error
- Increased Contrast
- Reduce Motion
- keyboard-present input
- locale / RTL / orientation / iPad when relevant

## Severity

- **Blocker** — task cannot be completed, serious accessibility failure, content/action is obscured, destructive behavior is unsafe, or platform interaction is fundamentally broken.
- **Major** — hierarchy, semantic agreement, consistency, density, component choice, readability, environment adaptation, or interaction feedback materially lowers quality.
- **Minor** — optical polish or small consistency issue that does not prevent task completion.

## Design smells

Look for:

- excessive rounded cards or nested containers
- excessive borders, blur, or Liquid Glass
- competing accent colors
- giant low-value headings
- tiny low-contrast labels used as fake sophistication
- custom controls that look almost native but behave differently
- inconsistent margins/radii between equivalent sections
- mixed icon languages when SF Symbols cover the action
- unjustified floating controls
- hidden primary actions
- animation that competes with the task
- runtime semantics that disagree with the rendered UI
- layouts that only work at one device size or text size

## Review loop

```text
operate flow
  ↓
capture runtime evidence
  ↓
review Blocker / Major / Minor
  ↓
fix highest-leverage issue
  ↓
rerun the affected path
  ↓
capture again
```

Do not mark a visual issue fixed from source inspection alone. The post-fix running state is the evidence.

A polished Apple-native flow tends to feel understandable, calm, consistent, responsive, semantically correct, familiar where behavior matters, and expressive where product content matters.
