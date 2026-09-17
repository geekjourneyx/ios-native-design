# Motion and materials

Custom motion should communicate state, feedback, continuity, spatial relationship, progress, or direct manipulation. If none apply, consider removing it.

## Default order

1. system component motion
2. system navigation/presentation transition
3. SwiftUI standard presets
4. custom spring/timing only for a repeated product-specific need

A reasonable project convention is:

```text
routine interaction      → snappy / system behavior
layout or state change   → smooth / system behavior
rare expressive moment   → bouncy, sparingly
navigation               → system transition
gesture-driven movement  → track the gesture / interactive spring
```

These mappings are project conventions, not Apple mandates.

## Reduce Motion

Review zooming, scaling, repeated automatic animation, strong bounce, large spatial/depth transitions, and animated blur. Important state changes must remain understandable with reduced motion.

## Liquid Glass

Treat Liquid Glass primarily as a functional layer for controls and navigation above content.

- prefer system components that acquire it automatically
- use custom glass sparingly
- do not make it the default content-card material
- preserve legibility
- consider Reduce Transparency / Increased Contrast
- keep color on glass restrained

Use haptics for meaningful confirmation, boundaries, selection, or important transitions — not every tap.
