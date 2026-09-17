# Device Test Matrix

Use the smallest matrix that covers the risks of the changed UI. Do not run irrelevant variants.

| Dimension | Baseline | Add when relevant |
|---|---|---|
| Runtime | affected primary flow | secondary/error flow |
| Appearance | Light + Dark | custom material-heavy states |
| Text | default + one accessibility size | maximum size for text-heavy UI |
| Size | small + large/resized iPhone | iPad / landscape / iPhone Mirroring |
| Content | normal + long | empty / large dataset |
| State | populated | loading / error / offline / permission denied |
| Contrast | default | Increased Contrast |
| Motion | default | Reduce Motion |
| Input | normal | keyboard-present / hardware keyboard |
| Locale | primary locale | expansion-prone locale / RTL |
| Device | simulator | physical device for hardware-dependent behavior |

## Execution record

```text
Scenario:
Build:
Device:
OS:
Appearance:
Text size:
Screen size/orientation:
Locale:
Motion/contrast:
Content state:
Steps:
Expected:
Observed:
Screenshot:
Accessibility notes:
Result: PASS / BLOCKER / MAJOR / MINOR
```

## Stop conditions

Stop and fix before expanding the matrix when you find:

- a Blocker
- app crash
- primary task cannot complete
- serious accessibility failure
- content obscured by system UI
- layout unusable at required text size

After the fix, rerun the failed scenario first, then continue the matrix.
