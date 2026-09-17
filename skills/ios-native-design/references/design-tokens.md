# Design tokens

Tokens exist to prevent feature screens from inventing parallel design systems.

Use system semantics first. Add project tokens only where the platform does not already express the intent.

Good token names describe meaning:

```text
spacing.section
spacing.controlGap
color.brandAccent
color.success
radius.contentCard
motion.stateChange
```

## Starter spacing rhythm

```text
xxs = 4
xs  = 8
sm  = 12
md  = 16
lg  = 24
xl  = 32
xxl = 48
```

This is a **project convention**, not an Apple HIG mandate.

## Rules

- Feature views consume tokens; they do not define them.
- System semantic colors stay system semantic colors.
- Prefer Dynamic Type roles before custom typography tokens.
- Keep the radius scale small; add only radii the product actually repeats.
- Prefer system motion/presentation before custom duration and spring tokens.
- A new token needs repeated use, a clear semantic role, or an approved brand need.

“18 looked better here” is not a semantic role.
