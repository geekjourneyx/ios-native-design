# Layout and spacing

Do not invent a universal “Apple 8pt grid”. Apple platform layout is broader than a mandatory grid.

Prefer:

- safe areas
- system margins
- native component intrinsic layout
- alignment guides
- adaptive layout
- project spacing tokens for custom composition

A 4/8-based rhythm can be useful, but it is a product convention rather than HIG law.

## Priorities

1. readable hierarchy
2. consistent alignment
3. appropriate content width
4. safe-area correctness
5. adaptability
6. token consistency
7. optical polish

Use visible containers only when they communicate grouping, selection, hierarchy, interaction, or meaningful separation. Do not wrap every logical group in a rounded rectangle.

`.ignoresSafeArea()` is appropriate for intentional full-bleed media/backgrounds, not as a general layout shortcut.

At minimum verify a small iPhone, a current large iPhone, and an accessibility text size for text-heavy screens.
