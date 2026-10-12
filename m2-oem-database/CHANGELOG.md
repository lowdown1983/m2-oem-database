# Changelog — M2/SuperB OEM Vehicle Database

All notable changes to the OEM vehicle database. Vehicle data is
community-sourced and variable-quality, so every factual claim carries an
evidence grade: **A** = factory documentation or verified capture;
**B** = reputable community source (opendbc, FORScan docs, documented
reverse-engineering, trade press); **C** = single anecdotal report or
vendor marketing. Source: `source/_meta.yaml` changelog (dates per that
file).

## [Unreleased]

## [1.4.0] — 2026-10-07 — Three-track expansion

13 makes, 45 DBCs, 4,411 DTCs, 637 DID/parameter records, 51 module maps,
8,764 RAG chunks; validation 36/36.

### Added
- Five new makes: Subaru (SSM2 protocol + 30-entry SSM parameter-address
  catalog, FSI/FSM DTCs, module maps), Mazda (HS/MS-CAN era split, DTCs,
  module maps), BMW (E/F/G bus generations, 0x6F1 KWP2000 diagnostic
  scheme, factory hex DTCs, module maps), Mercedes-Benz (CAN-B/C/D/E,
  filtered-DLC behavior, DAS/community DTCs, module maps), Volvo
  (P1/P2/P3 dual-CAN + CEM gateway, proprietary diagnostic addressing,
  CEM module-code DTCs, module maps).
- 13 new DBCs harvested (626 messages, 1,474 signals; 45 DBCs total).
- Import DTC expansion: +175 Toyota/Lexus, +Honda P-codes and SRS/ABS/VSA
  blink-code mappings (their own entries, never forced into B1xxx/C1xxx),
  +183 Nissan/Infiniti. DTCs 3,344 → 4,411.
- Thin-spot fills: +4 Stellantis DIDs, +18 Honda/VW body/chassis DIDs
  (with DID-reuse conflict notes); Hyundai/Kia B/C/U corroboration
  (117 codes → A, 50 → B; truncated descriptions expanded; 7 conflicts +
  1 not-found carried with caveats). DIDs 581 → 637.
- Module maps 32 → 51.

### Changed
- DTC code pattern widened (BMW factory hex, Honda blink codes, Volvo
  module codes, UDS failure-type byte); DID make enum + pattern widened
  (Subaru 3-byte SSM addresses, service SSM2).

### Key research findings (for M2 firmware)
- BMW E-series speaks KWP2000-over-CAN, not UDS.
- Subaru SSM is memory-address-oriented, not service-oriented.
- Mercedes post-DMCA UDS addressing is effectively undocumented
  (structural gap).
- Mazda/Volvo/Mercedes manufacturer DID catalogs effectively empty;
  G-series BMW / SPA-CMA Volvo / 2021+ Mercedes secure-gateway = out of
  M2 scope (CAN FD / DoIP / Ethernet).

## [2026-10-08] — Watchlist v1.4.0 extension draft recovered

- Recovered the lost signal-watchlist v1.4.0 extension draft: all 19 rows
  (Mazda, BMW, Mercedes, Volvo) re-extracted byte-for-byte from the raw
  opendbc DBCs; one byte-order transcription slip fixed
  (Volvo BrakePedalActive). Saved merge-ready (markdown rows +
  schema-valid JSON + 5 footnotes) at
  `~/workspace/goals/oem-vehicle-database/files/watchlist-v140-extension.md`.
  (Per parent agent notes; the draft previously existed only in /tmp,
  which was wiped.)

## [1.3.0] — 2026-10-06 — Platform-level depth

### Added
- 581 UDS DIDs (36 ISO-standard [A] + 545 make-specific: GM 7, Ford 13,
  Stellantis 3, Toyota 124, Honda 59, VW 280, Hyundai 33, Nissan 26).
  Nissan entries flagged 0x21-local (KWP2000-style local IDs, not 0x22).
- Ford as-built reference: 41 module addresses with block ranges,
  checksum/format spec, UDS read/write mapping.
- Per-platform bus/module maps for all 32 DBC platforms (DBC node names
  cross-checked against bus briefs; gateway-forwarded traffic flagged).

### Known thin spots
- Stellantis DIDs (single community source), VAG/Honda B/C-code DIDs,
  Hyundai ECU-scoped DID numbering.

## [1.2.1] — 2026-10-06 — Import DTC expansion

### Added
- +851 manufacturer-specific DTCs: 108 Toyota/Lexus, 90 Honda/Acura,
  140 VW Group, 440 Hyundai/Kia, 73 Nissan/Infiniti. Catalog now
  3,344 DTCs across all 8 makes. Same per-entry format and A/B/C grading
  as v1.2.0.

### Known thin spots
- VAG B/C codes (5-digit only, no verified P/B/C equivalents),
  Honda B1xxx/C1xxx (blink-code era), Hyundai B/C/U single-source
  sections.

## [1.2.0] — 2026-10-06 — DTC catalog

### Added
- New DTC catalog: 2,493 trouble codes (2,098 SAE J2012 generic + 395 Big
  Three manufacturer-specific: 107 GM, 182 Ford, 106 Stellantis). Each
  entry: code, description, category, scope, possible causes and
  diagnostic notes where sources support them (186 with causes, 242 with
  notes), graded A/B/C (27/1080/1386).
- Inference-flagged causes/notes from researchers were omitted rather
  than laundered. Ford split-grade entries keep the description grade
  with grade detail preserved in evidence.

### Changed
- Imports (Toyota/Honda/VW/Hyundai/Nissan) deferred to v1.2.1.

## [1.1.0] — 2026-10-06 — Imports + signal-level decode

### Added
- Toyota/Lexus, Honda/Acura, VW Group, Hyundai/Kia, Nissan/Infiniti
  (8 makes total).
- Signal-level decode for ALL 32 DBCs: 21,568 signals with start bit,
  length, byte order, factor, offset, unit.
- Key findings: Honda B-CAN maps to the M2 SWCAN circuit; Toyota DLC3 is
  HS-CAN only; VW SFD blocks writes but not reads or bootloader flashing;
  Hyundai/Kia use KWP2000-over-CAN (2005–2010); Nissan uses KWP-style
  0x21 reads (0x22 rejected) and has a query-only BCM gateway DLC.

### Fixed
- Big Three message count 1366 → 1368 (whitespace-aware parser now
  includes two indented BO_ records in gm_global_a_object.dbc).

## [1.0.0] — 2026-10-06 — Initial Big Three release

### Added
- Bus architecture (`makes.yaml`): every current bus per make (bitrate,
  DLC pins, years) + legacy protocols (J1850 VPW/PWM, CCD, SCI, K-line)
  + which M2 hardware talks to which bus. Makes: GM, Ford, Stellantis.
- Diagnostic access (`diagnostics.yaml`): UDS addressing per make
  (GM $7E0/$7E8, Ford +8 offset), gateway modules (GM BCM, Ford GWM/
  BdyCM, Stellantis SGW), tool ecosystems (Tech2/GDS2, FORScan,
  wiTECH/AutoAuth). Explicit seed/key policy: no public algorithms
  exist — none are invented or reproduced here.
- Message catalog (`vehicles.yaml`): 16 opendbc DBCs, 1,366 messages
  harvested mechanically (GM Global A, Ford CGEA/Fusion/Lincoln, Chrysler
  CUSW/Pacifica/Giorgio). Grade B: real captures, but comma.ai's
  ADAS-driving subset — not complete vehicle databases.
- Validation: 12/12 questions answered solely from the generated
  artifacts.

### Key findings for M2 firmware
- GM single-wire GMLAN lives on DLC pin 1 (33.33 kbps) — the M2's SWCAN
  circuit was built for this; sleeping nodes need `mode(2)` HV wake-up
  first.
- Ford MS-CAN is on pins 3/11 @ 125 kbps — the M2's two CAN controllers
  can watch HS-CAN and MS-CAN simultaneously (a switched ELM327 cannot).
- Stellantis Secure Gateway (2018+): reads work through the DLC; writes
  (DTC clear, actuations, programming) are blocked. Legitimate paths:
  AutoAuth ($50/yr shop), wiTECH 2.0, or physical bypass on your own
  vehicle.
- CAN FD (2021+ Ford select models): the M2's TJA1051 is CAN 2.0 only —
  out of scope for M2 CAN participation.
- Ford SCP (pre-2004) requires In-Frame Response bytes; GM VPW does not.
