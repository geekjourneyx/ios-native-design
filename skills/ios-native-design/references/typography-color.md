# Typography and color

## Typography

Use SF Pro / system typography and Dynamic Type-compatible styles for ordinary application UI.

Prefer roles such as:

```swift
.font(.largeTitle)
.font(.title)
.font(.headline)
.font(.body)
.font(.callout)
.font(.caption)
```

over arbitrary fixed point sizes.

Fixed display sizes can be justified for brand hero type, specialized visualization labels, or editorial moments. They should not become the default for body copy, settings, form labels, controls, or navigation.

Use size/style, weight, spacing, position, and grouping together. Do not encode hierarchy with color alone.

## Color

Prefer semantic/system colors for platform roles. Do not hard-code HEX approximations of system backgrounds, labels, or separators.

Use brand color selectively for primary action, current selection, status, key data emphasis, or distinctive product content.

Dark Mode is a design state, not a filter. Check hierarchy, imagery, muted text, materials, selected states, and disabled states.

Validation, selection, and status must have a non-color cue such as a symbol, label, shape, border, position, or accessibility value.
