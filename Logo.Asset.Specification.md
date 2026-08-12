# SVG Logo Asset Specification
## AegisAI Ecosystem Brand Standards v1.0

---

# Purpose

This document defines the official SVG logo specifications for all AegisAI ecosystem brands.

The goal is to ensure:

- Consistent visual identity
- Infinite scalability
- GitHub compatibility
- Adobe Illustrator compatibility
- Figma compatibility
- Print readiness
- Dark and light theme support

---

# Supported Brands

| Brand | Role |
|---------|---------|
| AegisAI | Guardian Agent |
| SeaAI | Intelligence Explorer |
| FutureAI Agents | Ecosystem Extensions |

---

# Design Philosophy

The entire ecosystem is based on:

```text
Guardian + Explorer
Trust + Discovery
Protection + Intelligence
```

Every future logo must inherit these principles.

---

# Official SVG Requirements

## File Format

Required:

```text
SVG 1.1
SVG Tiny 1.2
SVG 2.0 Compatible
```

---

## Encoding

Required:

```text
UTF-8
```

---

## ViewBox

Standard:

```svg
viewBox="0 0 512 512"
```

Reason:

- GitHub rendering consistency
- Easy export sizes
- Favicon generation

---

# Asset Variants

Each logo must provide:

## 1. Full Logo

```text
[Symbol]

Brand Name
```

Example:

```text
🛡
AegisAI
```

---

## 2. Icon Only

```text
🛡
```

Used for:

- GitHub Avatar
- Teams
- Slack
- Application Icon

---

## 3. Monochrome Version

```text
Black
White
```

Required for:

- Documents
- Watermarks
- Printing

---

## 4. App Icon Version

Square layout only.

Example:

```text
┌──────┐
│  🛡  │
└──────┘
```

---

# Geometry Rules

## Grid System

Base Grid:

```text
8px
```

All design elements should align to an 8px grid.

---

## Corner Radius

Application Icons:

```text
64px
```

Preferred.

Allowed:

```text
48px – 72px
```

---

## Stroke Weight

Recommended:

```text
8px
```

Minimum:

```text
4px
```

Maximum:

```text
12px
```

---

# AegisAI Logo Specification

## Symbol

Shield

### Meaning

```text
Protection
Trust
Control
Governance
```

---

## Shield Ratio

```text
Height: 100
Width: 80
```

Ratio:

```text
1 : 0.8
```

---

## Visual Weight

```text
70% Symbol
30% Typography
```

---

## Construction

```text
      🛡

   AegisAI
```

---

## Safe Area

Minimum clear space:

```text
X = shield width / 4
```

```text
┌──────────────┐
│      X       │
│  X Logo X    │
│      X       │
└──────────────┘
```

No object may enter this area.

---

# SeaAI Logo Specification

## Symbol

Wave + Shield

---

### Meaning

Wave

```text
Discovery
Exploration
Information Ocean
```

Shield

```text
Security
Trust
Protection
```

---

## Construction

```text
      🌊
      🛡

     SeaAI
```

---

## Visual Weight

```text
50% Wave
30% Shield
20% Typography
```

---

## Wave Geometry

Requirements:

```text
Single SVG Path
```

Preferred:

```svg
M0 50
C50 20,100 80,150 50
```

Characteristics:

- Smooth
- Minimal
- Symmetrical

---

# Color Standards

## AegisAI

### Primary

```text
Deep Navy
#051B44
```

### Secondary

```text
Azure Blue
#0F5FFF
```

### Accent

```text
Cyan
#27D8FF
```

---

### Gradient

```css
linear-gradient(
  180deg,
  #27D8FF 0%,
  #0F5FFF 100%
)
```

---

## SeaAI

### Primary

```text
Ocean Navy
#061B44
```

### Secondary

```text
Ocean Blue
#198BFF
```

### Accent

```text
Aqua
#18D2CC
```

---

### Gradient

```css
linear-gradient(
  180deg,
  #18D2CC 0%,
  #198BFF 100%
)
```

---

# Typography Standards

## Primary Font

```text
Montserrat SemiBold
```

---

## Fallback Fonts

```text
Inter
Segoe UI
Aptos
Arial
```

---

## Logo Text Weight

Preferred:

```text
SemiBold
600
```

Allowed:

```text
Bold
700
```

---

# Dark Mode Rules

GitHub primarily uses dark themes.

Required:

```text
Contrast Ratio ≥ 4.5:1
```

---

Preferred:

```text
Navy Background
Cyan Accent
```

---

# Light Mode Rules

Requirements:

```text
No pure white symbol
```

Instead:

```text
#051B44
```

or

```text
#061B44
```

---

# GitHub Usage Standards

## Repository Avatar

Use:

```text
Symbol Only
```

Recommended:

```text
512x512 SVG
```

---

## README Logo

Use:

```text
Full Logo
```

Recommended Width:

```text
280px–400px
```

---

## Documentation

Preferred:

```text
Monochrome Version
```

---

# Export Standards

## Master Asset

```text
SVG
```

Source of Truth.

---

## Production Exports

Required:

```text
512x512 PNG
1024x1024 PNG
2048x2048 PNG
```

Transparent background.

---

# Prohibited Usage

Do NOT:

```text
Add glow effects
Add drop shadows
Stretch logo
Rotate logo
Change colors
Modify typography
Distort proportions
```

---

# Future Agent Extension Rules

Every future ecosystem logo follows:

```text
[Unique Symbol]
+
[Shared Shield]
+
[AI Name]
```

Examples:

```text
SeaAI
ThreatAI
CloudAI
PrivacyAI
GovAI
RiskAI
```

---

# Brand Consistency Principle

The AegisAI ecosystem must always communicate:

```text
Trust
Protection
Discovery
Intelligence
```

Visual shorthand:

```text
Shield = Guardian

Wave = Explorer
```

Together:

```text
Guardian + Explorer
```

This principle governs all future logo designs, visual assets, and ecosystem branding.
