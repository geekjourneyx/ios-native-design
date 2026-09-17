# Accessibility as design quality

Accessibility is part of the default design pass.

## Minimum hit region

Interactive iOS/iPadOS controls should generally expose at least a **44×44 pt hit region**. The visible icon may be smaller.

## Dynamic Type

Test default text size and at least one accessibility size. At large sizes allow text to wrap, avoid fixed-height clipping, allow horizontal layouts to become vertical when necessary, and keep primary actions reachable.

## VoiceOver

Check concise labels, useful values for stateful controls, correct traits, logical reading order, decorative-image hiding, and grouping when reading every child independently creates noise.

## Contrast and color

Check Light and Dark Mode. Do not assume translucent material guarantees contrast. Selection, validation, status, and charts must not rely on color alone.

## Reduce Motion

Reduce or replace problematic zoom, scaling, repetitive animation, excessive bounce, depth movement, large spatial transitions, and uncomfortable blur transitions.

Custom controls still need a semantic role, label, state/value, focus order, adequate hit region, and accessible visual state.

Use Accessibility Inspector and VoiceOver on critical flows.
