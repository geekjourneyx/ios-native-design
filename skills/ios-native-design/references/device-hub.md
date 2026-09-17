# Xcode 27 Device Hub

Device Hub is the preferred Apple runtime surface for visual and interaction verification when Xcode 27 is available.

## What Device Hub provides

Apple documents Device Hub as a unified place for simulated and physical devices. It provides a live interactive device view and supports device/environment configuration.

Useful design-verification capabilities include:

- interact with the live device screen
- tap, scroll, keyboard input, hardware controls
- rotate
- resize a simulated iPhone to valid screen sizes
- change appearance such as Light/Dark
- change text size
- evaluate accessibility-related environment settings
- capture screenshots
- record simulator video
- work with both simulated and physical devices

## Screenshot rule

For final visual evidence, prefer Device Hub's Screenshot control over a screenshot of the Mac window.

Apple states that Device Hub captures screenshots at the **full resolution of the simulated or physical device regardless of the Mac display resolution** and saves them to the Mac Desktop.

That makes Device Hub captures suitable for:

- visual review
- before/after evidence
- localization review
- accessibility-state evidence
- snapshot/reference comparison

Computer Use screenshots remain useful for locating controls and understanding the current desktop state, but they are operational evidence, not the preferred final visual artifact.

## Environment pass

For a material UI change, test applicable variants:

| Dimension | Minimum |
|---|---|
| Appearance | Light, Dark |
| Text | Default, accessibility size |
| Device size | small + large/resized |
| Content | normal + long |
| State | loading/empty/error as applicable |
| Contrast | Increased Contrast when styling is substantial |
| Motion | Reduce Motion when motion is material |
| Input | keyboard-present for input flows |

Use Device Hub resize mode to probe layout behavior without maintaining a simulator for every width. Device Hub snaps arbitrary resizing to valid sizes.

## Simulator vs physical device

A simulator is excellent for layout/environment coverage but cannot reproduce every hardware-specific feature.

Use a physical device for hardware-dependent behavior. Device Hub can surface physical devices too, but the test plan must still acknowledge device-only constraints.

## Automation boundary

Use semantic/CLI tools such as Xcode agent tooling or `devicectl` for deterministic operations when available.

Use Device Hub's GUI/Computer Use for:

- interactive exploration
- visual inspection
- changing GUI-only environment controls
- screenshots/video
- reproducing user-visible behavior

## Primary sources

- Device Hub documentation  
  https://developer.apple.com/documentation/xcode/device-hub/
- Capture screenshots and videos  
  https://developer.apple.com/documentation/xcode/capturing-screenshots-and-videos-from-devices
- Configure simulated device environment  
  https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device
- WWDC26 — Get the most out of Device Hub  
  https://developer.apple.com/videos/play/wwdc2026/260/
- WWDC26 — Platforms State of the Union  
  https://developer.apple.com/videos/play/wwdc2026/102/
