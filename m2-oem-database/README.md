# M2/SuperB OEM Vehicle Database

Vehicle-side companion to the M2/SuperB Hardware Knowledge Pack (v1.4.0).
Bus architecture, diagnostic access, and message catalogs for the Big Three —
GM, Ford, Stellantis — graded A/B/C by source quality.

**Why separate:** vehicle data is community-sourced and variable-quality. It
carries its own evidence grades instead of diluting the hardware pack's bar.
Hardware facts (M2 OBD-II connector, transceivers, software) are referenced
from the knowledge pack, not duplicated.

## What's in v1.0.0 (2026-10-06)

- **Bus architecture** (`makes.yaml`): every current bus per make (bitrate,
  DLC pins, years) + legacy protocols (J1850 VPW/PWM, CCD, SCI, K-line) +
  which M2 hardware talks to which bus.
- **Diagnostic access** (`diagnostics.yaml`): UDS addressing per make
  (GM $7E0/$7E8, Ford +8 offset), gateway modules (GM BCM, Ford GWM/BdyCM,
  Stellantis SGW), tool ecosystems (Tech2/GDS2, FORScan, wiTECH/AutoAuth),
  and an explicit seed/key policy: **no public algorithms exist — none are
  invented or reproduced here.**
- **Message catalog** (`vehicles.yaml`): 16 opendbc DBCs, 1,366 messages
  harvested mechanically (GM Global A, Ford CGEA/Fusion/Lincoln, Chrysler
  CUSW/Pacifica/Giorgio). Grade B: real captures, but comma.ai's ADAS-driving
  subset — not complete vehicle databases.
- **Validation:** 12/12 questions answered solely from the generated
  artifacts.

## Key findings for M2 firmware

- GM single-wire GMLAN lives on DLC **pin 1** (33.33 kbps) — the M2's SWCAN
  circuit was built for this. Sleeping nodes need `mode(2)` HV wake-up first.
- Ford MS-CAN is on **pins 3/11** @ 125 kbps — the M2's two CAN controllers
  can watch HS-CAN and MS-CAN **simultaneously** (a switched ELM327 cannot).
- Stellantis **Secure Gateway (2018+)**: reads work through the DLC, writes
  (DTC clear, actuations, programming) are blocked. Legitimate paths:
  AutoAuth ($50/yr shop), wiTECH 2.0, or physical bypass on your own vehicle.
- **CAN FD (2021+ Ford select models)**: the M2's TJA1051 is CAN 2.0 only —
  out of scope for M2 CAN participation.
- Ford SCP (pre-2004) **requires In-Frame Response bytes**; GM VPW does not.

## Layout

- `source/` — hand-editable YAML (the truth layer)
- `schemas/` — JSON schemas
- `scripts/build.py` — one-command rebuild: `python3 scripts/build.py`
- `generated/` — machine JSON, wiki, RAG chunks (never hand-edit)
- `work/` — research notes + opendbc clone (not part of the database)

## Definition of done

For a covered vehicle, an LLM can answer which buses exist on which pins,
what the key message IDs are, and which diagnostic services actually respond —
every claim carrying a source-quality grade.

## Companion repository

- [m2-superb-firmware](https://github.com/lowdown1983/m2-superb-firmware) —
  the seven-mode M2/SuperB PlatformIO firmware whose UDS and OBD2 modes work
  against this database.
