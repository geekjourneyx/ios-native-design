# Static verifier

The verifier is intentionally conservative. It catches source-level drift; it does **not** claim to evaluate aesthetics.

## Run

```bash
python3 skills/ios-native-design/verifier/ios_design_verifier.py /path/to/ios-project
```

JSON output:

```bash
python3 skills/ios-native-design/verifier/ios_design_verifier.py /path/to/ios-project --json
```

Custom config:

```bash
python3 skills/ios-native-design/verifier/ios_design_verifier.py /path/to/ios-project \
  --config skills/ios-native-design/verifier/verifier.config.json
```

## Exit code

- `0` — no configured fail-level findings
- `1` — at least one fail-level finding
- `2` — invalid project path

Warnings still require review.

## Waiver

Place an explicit waiver immediately above the relevant code:

```swift
// ios-native-design: allow IOS-NATIVE-002 reason=Approved brand display title
```

A passing static verifier does **not** mean the UI is good. Rendering, screenshot review, accessibility checks, interaction tests, and the Design DoD still apply.
