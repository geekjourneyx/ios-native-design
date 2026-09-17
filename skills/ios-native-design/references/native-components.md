# Native component policy

## Decision rule

Before implementing custom UI ask:

1. Is this standard platform behavior?
2. Does SwiftUI already provide it?
3. Would a custom version lose accessibility, focus, localization, system motion, safe-area behavior, or future OS adaptation?

If SwiftUI already expresses the behavior, prefer it.

| Need | Prefer |
|---|---|
| hierarchy | `NavigationStack` |
| split navigation | `NavigationSplitView` |
| primary sections | `TabView` |
| settings / grouped data | `List`, `Section`, `Form` |
| binary setting | `Toggle` |
| exclusive option | `Picker` |
| segmented selection | segmented `Picker` when appropriate |
| date/time | `DatePicker` |
| search | `.searchable` |
| progress | `ProgressView` |
| alert | `.alert` |
| destructive/options menu | `.confirmationDialog` |
| contextual actions | `Menu`, swipe actions, context menu |
| modal task | `.sheet` / `.fullScreenCover` when justified |
| standard action | `Button` + SF Symbols |

Do not recreate a native control with `HStack + Capsule + offsets` just to make it visually unique.

Custom components are appropriate for product-specific objects, specialized creation/editing controls, unique visualization, or interactions a native component cannot express.

A custom button still needs Button semantics, a 44×44 pt effective hit region, pressed/disabled states, VoiceOver labeling, contrast, Dynamic Type-safe text, and Reduce Motion-safe feedback.
