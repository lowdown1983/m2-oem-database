# Hyundai / Kia — in-vehicle networks & diagnostic access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, well-documented
reverse-engineering, trade press, aftermarket tool vendor docs) ·
**C** = single anecdotal report. Unverified items are marked [?].
Grades appear inline as [A], [B], [C].

Research date: 2026-10-06.

---

## 1. Bus architecture

### 1.1 C-CAN (chassis CAN) and M-CAN (multimedia/body CAN)

Hyundai/Kia split the vehicle CAN into function buses. The opendbc DBC names
(`hyundai_2015_ccan`, `hyundai_2015_mcan`) reflect this split [B]:

- **C-CAN (chassis CAN)** — 500 kbps [B], OBD-II pins 6 (H) / 14 (L) [B].
  Carries powertrain/chassis: EMS/ECM, TCU, ESC/ABS, _4WD, EPB, SCC (smart
  cruise), MDPS (steering). Node names confirmed from a 2015 Hyundai C-CAN
  DBC circulating publicly (EMS12, _4WD12, ODS11/12/13 messages; receivers
  include ESC, TCU, ABS, ACU, BCM, CLU, IBOX, SMK) [B/C — DBC content is
  real, hosting is a scribd upload].
- **M-CAN (multimedia/body CAN)** — carries body/comfort/multimedia traffic
  (171 messages in opendbc's `hyundai_2015_mcan.dbc`, incl. HU_TMU head-unit
  messages) [B]. Bitrate NOT confirmed in this pass [?]. DLC pin exposure
  NOT confirmed in this pass [?] — no source found placing M-CAN on
  manufacturer-discretionary OBD-II pins; treat as interior-only unless a
  per-model wiring diagram says otherwise.
- The legislated emissions bus is the standard ISO 15765-4 500 kbps 11-bit
  bus on pins 6/14 [A — regulatory fact; confirmed on a 2018 Kia Soul by the
  bavtech-vci project's field test, which read PIDs/DTCs/VIN with responders
  at 0x7E8–0x7EF] [B].
- **CAN FD era (2021+ select models)**: opendbc's Hyundai port flags
  CAN-FD platforms and uses a separate ECAN bus for ADAS [B]. Per a Kia
  owner-forum technical poster, **diagnostics in Kia/Hyundai vehicles are
  NOT performed via CAN FD** — classic CAN remains the diagnostic transport
  even on CAN-FD vehicles (programming/updates may differ) [C].

### 1.2 Gateway architecture

- Hyundai/Kia DTC documentation references gateway modules (U0146–U0150:
  "data bus, gateway A/B/C/D/E — no communication") [C — machine-translated
  Kia 20-pin connector guide on scribd; confirms gateways exist, not their
  topology].
- opendbc's Hyundai CAN-FD support references an ADAS ECU and ECAN bus
  distinct from the main bus [B] — consistent with a central-gateway
  architecture on newer platforms, but the gateway's diagnostic firewalling
  behavior (if any) was NOT confirmed in this pass [?]. No Stellantis-SGW
  equivalent was found for Hyundai/Kia; do not assume one exists.

### 1.3 Model-year evolution

- Per the HiCOM aftermarket tool manual's Hyundai/Kia protocol table [B]:
  ISO 15765 CAN-BUS from **2005** ("all systems"); UDS (ISO 14229) over CAN
  from **2011** ("all systems"). Implication: 2005–~2010 CAN vehicles likely
  run **KWP2000 over CAN** (ISO 15765 transport, KWP2000 application layer),
  not UDS — verify per model before assuming UDS support.
- The 2008 US CAN mandate transition was messy for Kia: a 2008 Kia van
  owner found the PCM on CAN **plus** a dedicated K-line to the DLC, and
  ScanGauge listed Kia-specific gauges only for 2009+ [C — forum anecdote].
  Treat 2008 as a transition year; probe, don't assume.

---

## 2. Legacy protocols (pre-CAN)

Hyundai/Kia never used J1850 (no VPW/PWM on any Hyundai/Kia per the HiCOM
protocol table) [B]. Their pre-CAN world was K-line:

- **KW71 (Bosch) over ISO 9141**: 1991–2001, engine only [B].
- **ISO 9141**: 1996–present (per manual; effectively to ~2005), engine / ABS /
  airbag [B].
- **KWP2000 over ISO 9141**: 1996–present ("all systems") [B] — KWP2000
  persisted on K-line alongside CAN for years.
- **OBD-II pinout quirk**: Hyundai/Kia put **K-lines on many DLC pins** —
  pins 1, 2, 3, 7, 8, 9, 11, 12, 13 are all documented as "ISO9141 K Line"
  in the HiCOM manual [B]. One K-line per system (engine, ABS, airbag,
  gearbox) rather than a single shared K-line — unusual vs. European makes.
- **Hyundai 12-pin connector** (pre-OBD-II): pin 1 engine K-line, pin 2
  airbag K-line, pin 4 ABS K-line, pin 6 gearbox K-line, pin 10 engine
  L-line, pin 11 speed signal, pin 12 ground [B]. The GDS kit ships 16-pin
  to 12-pin, 16-pin to 20-pin, and 10-8-2 adapters for these older vehicles
  [B].

---

## 3. Diagnostic access

### 3.1 Tool ecosystem

- **GDS (Global Diagnostic System)** is Hyundai/Kia's OEM tool — one VCI
  works for both Hyundai and Kia software packages [B]. **GDS-Mobile** is
  the 3rd-generation (tablet-based) system; the VCI II module adds
  FlexRay/Bluetooth/Wi-Fi [B/C].
- Aftermarket: HiCOM (obdtester.com), Autel IM508/IM608 (strong Hyundai/Kia
  immobilizer support), OBDSTAR, Xhorse VVDI [B/C — vendor/tuner sources].

### 3.2 Protocol and addressing

- Legislated OBD-II: standard 0x7DF functional / 0x7E8–0x7EF responses,
  confirmed live on a 2018 Kia Soul [B].
- UDS (ISO 14229) over CAN from ~2011 [B]; KWP2000-over-CAN on 2005–~2010
  [B — inferred from the HiCOM timeline; verify per model].
- opendbc's Hyundai port disables ECUs for openpilot longitudinal control
  via diagnostic address **0x7D0** (radar/SCC; on ECAN for CAN-FD cars) and
  **0x730** (camera), **0x7B1** (additional ECU) [B — verified in the local
  opendbc clone, `car/hyundai/interface.py`]. These are community-verified
  diagnostic addresses for ADAS modules, not factory documentation.

### 3.3 Seed/key and immobilizer

- **No public UDS 0x27 seed/key algorithm was found for Hyundai/Kia. Do not
  invent one.**
- What IS public: immobilizer/key programming uses a **PIN code** —
  6 digits on newer models (4 digits on older; some older tools accept the
  last 4 of the chassis number) [C — tuner/locksmith sources]. The PIN is
  obtained from the dealer or third-party PIN providers; tools (Autel,
  OBDSTAR, VVDI) consume it but its derivation is not public.
- Newer smart-key systems (2021+, 2024+ new fob style) have caused tool
  failures; the working path is via the Diagnostics menu (not the IMMO
  menu) with a valid PIN [C].

---

## 4. M2 hardware mapping (which M2 hardware talks to which Hyundai/Kia bus)

| Hyundai/Kia bus | DLC pins | M2 hardware | Notes |
|---|---|---|---|
| C-CAN (500k) | 6 / 14 | CAN0 or CAN1 (TJA1051), 500 kbps | Primary diagnostic + powertrain bus. Standard M2RET/ELM path. |
| M-CAN | not confirmed on DLC [?] | CAN0/CAN1 if tapped | Interior-only per available sources; tap at the module if needed. |
| K-line (ISO 9141/KWP2000) | 7 (plus 1,2,3,8,9,11,12,13 per system) | K-line (TJA1027) | Pre-CAN models; multiple K-lines — identify the right pin per target system. |
| LIN sub-buses | not on DLC | LIN1/LIN2 (TJA1027) | If tapped at the module. |
| J1850 VPW/PWM | — | **not applicable** | Hyundai/Kia never used J1850 [B]. The M2's J1850 hardware has no Hyundai/Kia use. |
| CAN FD (2021+ select) | 6 / 14 | **NOT supported** — TJA1051 is CAN 2.0 only | Diagnostics reportedly stay on classic CAN [C], so OBD-II diagnostics may still work; CAN-FD bus participation is out of scope. |

---

## 5. Notable quirks

1. **Many K-lines.** DLC pins 1, 2, 3, 7, 8, 9, 11, 12, 13 can all be
   K-lines on Hyundai/Kia [B] — one per system. On a pre-CAN car, the M2's
   single K-line transceiver must be wired to the pin of the *target*
   system, not just pin 7.
2. **KWP2000-over-CAN transition.** 2005–~2010 CAN Hyundais likely speak
   KWP2000 on the CAN transport, not UDS [B — inferred from HiCOM
   timeline]. A UDS-only tool will fail against these; send KWP2000
   (0x10 0x81 startDiagnosticSession etc.) or verify first.
3. **2008 is a transition year.** Some 2008 Kias have CAN *and* a live
   K-line to the DLC [C]. Auto-detect the protocol; don't trust the year.
4. **Diagnostics avoid CAN FD.** Even on CAN-FD Hyundais/Kias, diagnostics
   stay on classic CAN per community reports [C] — the M2's CAN 2.0
   transceivers can still do OBD-II diagnostics on these vehicles even
   though they can't join CAN-FD buses.
5. **0x7D0 is the ADAS back door.** opendbc uses 0x7D0 (radar/SCC) and
   0x730 (camera) for ECU disable during openpilot operation [B] — useful
   known-good diagnostic addresses for Hyundai ADAS work.
6. **PIN-gated immobilizer, not seed/key-gated.** Key programming wants the
   6-digit PIN (dealer/third-party sourced), not a computed UDS 0x27 key
   [C]. There is no public algorithm to compute it.
7. **GDS adapter zoo.** 12-pin, 20-pin, and 10-8-2 adapters exist for
   pre-OBD-II Hyundais [B] — a full-coverage Hyundai bench needs more than
   the 16-pin DLC.

---

## Sources consulted

- HiCOM user manual (obdtester.com, via slideshare) — Hyundai/Kia OBD-II
  pinout, 12-pin connector, protocol timeline table [B]
- redthepro/bavtech-vci (GitHub) — 2018 Kia Soul field test: ISO 15765-4,
  0x7E8–0x7EF responders [B]
- commaai/opendbc (local clone) — `hyundai_2015_ccan` (113 msgs),
  `hyundai_2015_mcan` (171 msgs), `hyundai_i30_2014`, `hyundai_santafe_2007`;
  `car/hyundai/interface.py` diagnostic addresses 0x7D0/0x730/0x7B1 [B]
- 2015 Hyundai C-CAN DBC (scribd upload) — node names (EMS, TCU, ESC, IBOX,
  SMK, SCC…) [B/C]
- GDS/GDS-Mobile product docs (m2kinc.com, manuals.plus, automotiveworld.com)
  — OEM tool, VCI II FlexRay [B/C]
- Locksmith/tuner sources (vvdishop, obdii365, autelshop.de) — 6-digit PIN,
  smart-key procedures [C]
- Kia owner forum (forum.kia-motors.pl) — diagnostics not via CAN FD [C]
- bobistheoilguy.com — 2008 Kia van CAN + K-line thread [C]

## Open items for the database build

- M-CAN bitrate and DLC pin exposure: not confirmed in this pass [?].
- Hyundai/Kia gateway topology and any diagnostic firewalling on 2021+
  platforms [?].
- Per-model UDS vs KWP2000-over-CAN split for 2005–2011 vehicles [?].
- Factory UDS physical addressing IDs beyond the opendbc ADAS addresses [?].
