# OpenUSD Industrial Assets

A growing collection of industrial and manufacturing assets built with **OpenUSD** and Python.

This repository is part of my hands-on learning journey in OpenUSD, digital twins, and smart manufacturing. The goal is to gradually build reusable industrial objects that can later be combined into larger factory and warehouse digital-twin scenes.

## Current Assets

### Conveyor

A simple industrial conveyor built using OpenUSD primitives.

Features:

- Conveyor frame
- Belt
- Support legs
- Rollers
- Digital-twin attributes
  - Status
  - Speed
  - Motor temperature
  - Conveyor ID
- Status visualization
  - Green: Running
  - Yellow: Warning
  - Red: Stopped / Overheating
- Animated product movement along the conveyor

### Industrial Storage Rack

A simple warehouse pallet rack composed of:

- Four vertical posts
- Three shelf levels
- Horizontal support beams
- Pallet
- Cardboard box
- Basic display colors for easier visualization

## OpenUSD Concepts Practiced

This repository is being built gradually to practice core OpenUSD concepts including:

- USD Stage
- Prims
- Xforms
- Scene hierarchy
- Cube and Cylinder geometry
- Translate, Scale, and Rotate operations
- Custom attributes
- Display colors
- Time-sampled animation
- Manufacturing asset organization

## Project Structure

```text
openusd-industrial-assets/
│
├── conveyor/
│   ├── conveyor.py
│   └── conveyor.usda
│
├── industrial_rack/
│   ├── industrial_rack.py
│   └── industrial_rack.usda
│
└── README.md# openusd-industrial-assets
```

## Visualization

#### Conveyor
<img width="1911" height="867" alt="Image" src="https://github.com/user-attachments/assets/4b4411ab-b0cc-4705-a489-2ab70dd2b62a" />

#### Industrial Rack
<img width="1912" height="871" alt="Image" src="https://github.com/user-attachments/assets/e3985c6a-dc3a-4af0-b7da-8e955230da65" />
