# Honda / Acura — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, well-documented
reverse-engineering, trade press) · **C** = single anecdotal report or vendor
marketing. Conflicts between sources are reported, not silently resolved.

Research date: 2026-10-06.

---

## 1. Bus architecture

### F-CAN (Fast Controller Area Network)

- **500 kbps, dual-wire** [A — Honda service manual via civic.hondafitjazz.com;
  corroborated by 2003 Accord MotoLogic manual].
- Powertrain/processor bus: ECM/PCM, TCM, ABS/VSA, EPS, SRS, navigation unit
  [A — service manual; B — MotoLogic].
- **Two F-CAN segments exist on supported models** [B — opendbc
  `car/honda/hondacan.py` comments, verified in the local opendbc clone]:
  - **F-CAN A** = the OBD-II-port / diagnostic side
  - **F-CAN B** = the internal powertrain side
  - openpilot's panda sits between them as a relay; steering commands go to
    the radar, which forwards to the powertrain bus.
- **OBD-II DLC pins 6 (CAN-H) / 14 (CAN-L)** [B — ISO 15765-4 standard pinout;
  confirmed on a 2004 Civic EX (JustAnswer [C]); FN2 ECU pinout shows ECU pins
  A36/A37 = CAN H/L wired to OBD DLC 06/14 (scribd [B])].
- Present by the 2003 model year (2003 Accord navigation diagnosis manual
  already documents F-CAN at 500 kbps) [B].

### B-CAN (Body Controller Area Network)

- Per the Honda service manual (2006–2011 Civic, via civic.hondafitjazz.com):
  **single-wire, 33.33 kbps**, connecting the gauge control (tach) module,
  MICU, climate control unit, and immobilizer-keyless control unit [A].
- A 2008 Civic owner independently confirms listening to the B-CAN at
  33.3 kbps single-wire (Seeed Studio forum) [B].
- **SPEED CONFLICT — reported, not resolved:** the vanillagorillaa
  Honda-Civic-B-CAN openpilot-tap project (2016 Civic / 2017 CR-V, BCM
  36-pin connector tap) states it forwards "BCAN (150kbps)" onto the
  500 kbps F-CAN [C — single community project]. 150 kbps is a non-standard
  rate and conflicts with the service manual's 33.33 kbps single-wire spec.
  Possible explanations: the project author measured loosely, the 2016+
  B-CAN physical layer changed, or the tap point carries a different bus.
  Treat 33.33 kbps single-wire as the documented spec [A/B]; treat the
  150 kbps claim as unverified [C].
- **WIRING CONFLICT — reported, not resolved:** an undated Honda B-CAN
  training deck (slideshare, CraigKielb) depicts B-CAN modules joined by
  *two* wires (CAN HI / CAN LO) with 120Ω terminators [C], contradicting the
  service manual's single-wire description [A]. May reflect a different
  model era or a simplified training diagram.
- **B-CAN is NOT exposed at the OBD-II DLC** in any source found. The DLC
  carries F-CAN (6/14) and K-line (7); B-CAN access requires tapping behind
  the dash — e.g. the BCM 36-pin connector on 2016 Civic / 2017 CR-V [B —
  vanillagorillaa install notes; C for exact connector across models].
- ScannerDanner's Honda B-CAN case study (2009 Odyssey, relay control
  module) confirms the single-wire design in the field [B].

### Gateway architecture — two generations

- **2006–~2015: the gauge control module (tach) IS the gateway.** It
  translates F-CAN ↔ B-CAN and runs the network "loss of communication"
  self-diagnostic (Error 1 = F-CAN, Error 2 = B-CAN, Error 3 = UART, plus
  combination codes) readable on the odo/trip display [A — Honda service
  manual].
- **2016+ (10th-gen Civic and contemporaries): a dedicated gateway control
  module** behind the lower-left dashboard [C — JustAnswer technician
  report]. A 2019 Civic MaxiSys scan report lists "CAN gateway" as a
  discrete system alongside AT, ABS/VSA, SRS, EPS, body electrical [B —
  scannerdanner.com report].
- **Gateway as single point of failure:** if the gateway module fails, the
  OBD-II port stops communicating (link error) even with a good ECU and
  fuses [C — JustAnswer case; the engineering consequence is sound].
- openpilot's Honda integration confirms the relay topology persists: the
  panda bridges F-CAN A (OBD-II side) and F-CAN B (powertrain side), and
  forwards B-CAN onto its ACC-CAN interface [B — opendbc source].

### Other buses

- **IMA CAN (hybrids):** a separate CAN bus for the Integrated Motor Assist
  hybrid system; appears in scan reports as its own system with its own
  malfunction DTCs (U0038 "IMA CAN malfunction / IMA CAN bus OFF") [B —
  2019 Civic scan report].
- **UART:** referenced in the gauge module's error-code table (Error 3 =
  UART communication) as a third internal link alongside F-CAN/B-CAN [A —
  service manual; role unspecified].

---

## 2. Legacy: pre-CAN Honda

- Honda was a heavy **ISO 9141-2 K-line** user and never adopted J1850 (no
  VPW/PWM on any Honda) [B — protocol-survey consensus; C for the absolute
  "never" — no counterexample found].
- **DLC pin 7 = K-line**, and Honda kept it populated *alongside* CAN well
  into the CAN era: the 2006+ Civic (K20Z) DLC troubleshooting procedure
  walks the K-line circuit through the SRS unit, ABS/VSA modulator, EPS
  control unit, immobilizer-keyless control unit, audio unit, and under-dash
  fuse box [A — Honda service manual].
- **DLC pin 9 = SCS (Service Check Signal)**, Honda-specific: grounding it
  puts modules into service-check / blink-code mode [B — Honda OBD
  documentation via scribd; carrottoptuning OBD2B ECU pinouts show ECU
  pin 9 (BRN) = SCS].
- 1999–2001 OBD2B ECU pinouts document the K-Line terminal explicitly
  (LT BLU wire, "OBD2 Scan Data") [B — carrottoptuning].
- **Pre-OBD-II (OBD0/OBD1):** Honda-specific 2-pin/3-pin service check
  connectors; DTCs read as MIL blink codes (e.g. code 11 = 1 long + 1 short
  blink); SCS service connector (Honda tool 07PAZ-0010100 or jumper-wire
  equivalent) used for SRS memory erase [B — hondabase pinout tables,
  yumpu Honda SRS training excerpts].
- **CAN introduction:** F-CAN present by MY2003 (Accord) [B]; K-line
  retained for non-powertrain diagnostics; all US vehicles CAN-mandated for
  emissions from 2008-01-01 [A — regulatory fact].

---

## 3. Diagnostic access

### Tool ecosystem

- **HDS (Honda Diagnostic System)** with the HIM (Honda Interface Module)
  was the dealer tool through the 2010s [B]; superseded by **i-HDS**, a
  subscription download (Honda TechInfo): ~$45/day, ~$200/30 days,
  ~$1800/365 days [C — autosvs.com knowledge base].
- i-HDS works with any J2534 passthru device (Xhorse MVCI Pro, VXDIAG, etc.)
  [B — vendor tutorials; C for specific version compatibility].
- The HDS checks F-CAN and B-CAN communication status, reads/clears DTCs,
  shows data lists, and runs function tests; body-electrical DTCs live
  under BODY ELECTRICAL → TEST MODE [A — Honda service manual].
- **Without the HDS (documented fallback):** the MPCS short connector
  (07WAZ-0010100) on the MICU service check connector makes stored B-CAN
  DTCs display one-by-one on the odo/trip display (unit codes: 10 = MICU,
  50 = gauge control module, 51 = climate control); holding SELECT/RESET
  10+ seconds clears them [A — Honda service manual].

### Diagnostic CAN addressing

- **29-bit (verified, grade B):** Honda uses ISO 15765-3-style 29-bit
  diagnostic addressing. Tester transmits **0x18DB33F1**; the ECM responds
  on **0x18DAF110** (2009 Civic, documented in hansonFish/obdii). On Honda
  e:HEV vehicles, Mode-01 responses were observed from **0x18DAF101,
  0x18DAF102, 0x18DAF106, 0x18DAF10E, 0x18DAF1EF** — i.e. ECU source
  addresses 0x01/0x02/0x06/0x0E/0xEF answering the tester at 0xF1
  (papataku/honda_ehev_analyzer, real-vehicle project).
- **11-bit (single source, grade C):** one hobbyist integration guide
  (apatt124/ai-car-tuner) reports 2016–2021 Civic UDS at TX **0x7E0** /
  RX **0x7E8**, requiring extended diagnostic session (**0x10 0x03**)
  before feature toggles. Plausible but single-source — verify on-vehicle
  before relying on it.
- Standard emissions OBD-II (SAE J1979 modes 0x01–0x0A) on F-CAN 6/14
  works with any generic scan tool [A — regulatory/standards fact].

### Immobilizer and seed/key — policy enforced

- **No public UDS 0x27 seed/key algorithm for Honda was found. None is
  invented or reproduced here.**
- What IS publicly documented about Honda immobilizer access [C —
  aftermarket tool-vendor blogs, procedure-level only]:
  - Key programming and PCM replacement through HDS require a **PCM code**
    derived from the **last 5 digits of the VIN**; aftermarket "Honda IMMO
    PCM code calculator" tools compute it (USB-dongle-gated, stated to fit
    pre-2020 models; HDS v3.015+ reportedly uses a new algorithm these tools
    don't support).
  - Entering the wrong PIN 3 times locks the HDS immobilizer function
    ("This function blocked"); first/second/release passwords exist in the
    HDS workflow.
  - These are tool-workflow passwords, not the UDS 0x27 cryptographic
    exchange — do not confuse them.
- For M2 purposes: reading DTCs/data and generic OBD-II need no security
  access; immobilizer/key functions are dealer/i-HDS territory.

---

## 4. M2 hardware → Honda bus mapping

| Honda bus | DLC pins | M2 hardware path |
|---|---|---|
| F-CAN (500k) | 6 / 14 | CAN0 or CAN1 (TJA1051), 500 kbps via due_can. This is F-CAN **A** (diagnostic side) at the DLC; F-CAN **B** (powertrain) sits behind the gateway — tap there (as openpilot does) for raw powertrain traffic. |
| B-CAN (33.33k single-wire) | not at DLC — BCM tap | **M2 SWCAN circuit (MCP2515 + TH8056)** is a natural fit: single-wire CAN at 33.33 kbps. `setupSW(33)` per the pack's SWCAN software audit. Not reachable from the OBD-II port; requires a BCM-harness tap (e.g. 36-pin BCM connector on 2016 Civic/2017 CR-V). |
| K-line (ISO 9141) | 7 | M2 K-line transceiver (TJA1027), 10.4 kbps. Covers pre-CAN diagnostics and the still-populated K-line on CAN-era Hondas. |
| SCS (pin 9) | 9 | Honda-specific service-check signal; readable as a digital input (12VIO input channel). Grounding it enters service-check mode — a diagnostic aid, not a bus. |
| IMA CAN (hybrids) | internal | Standard CAN if tapped; electrically reachable with a TJA1051-class interface on a free controller. |
| J1850 | — | **Honda never used J1850.** The M2's J1850 hardware has no Honda application. |

Notes:
- Honda B-CAN on the M2's SWCAN circuit is INFERRED from the physical-layer
  match (single-wire 33.33 kbps CAN vs. TH8056 single-wire transceiver) —
  the electrical fit is solid, but no source was found of anyone doing it.
- If the 150 kbps B-CAN claim (§1) proves true for 2016+ models, the TH8056
  cannot do 150 kbps single-wire; that case would need re-evaluation.
- The M2's dual native CAN controllers cover F-CAN A at the DLC plus one
  tapped internal bus (F-CAN B or IMA CAN) simultaneously.

---

## 5. Notable quirks

1. **B-CAN speed conflict is the biggest open item** (§1): 33.33 kbps
   single-wire [A/B] vs. a 150 kbps claim on 2016+ BCM taps [C]. Anyone
   building a Honda B-CAN tool should auto-detect rather than assume.
2. **The gateway is a single point of failure for OBD-II.** A dead gateway
   module = link error at the DLC with a healthy ECU [C]. On 2016+ cars,
   check the dedicated gateway module (lower-left dash) before condemning
   the ECM.
3. **B-CAN carries immobilizer-keyless traffic** [A — service manual module
   list]. A B-CAN tap sees security-relevant frames; handle captures
   accordingly.
4. **The MPCS short-connector trick** reads and clears B-CAN DTCs with no
   scan tool at all (odo/trip display readout) [A]. Useful field fallback.
5. **No B-CAN at the DLC, ever.** Every B-CAN project taps behind the dash
   (BCM connector). An M2 plugged into the OBD-II port sees F-CAN A and
   K-line only.
6. **Honda skipped J1850 entirely** — a K-line shop, then straight to CAN.
   Ford/GM J1850 experience does not transfer.
7. **opendbc Honda coverage is thin:** the local clone has a single Honda
   DBC (`acura_ilx_2016_nidec.dbc`, 36 messages, ADAS/radar-focused) [B —
   mechanically verified]. The real Honda message knowledge lives in
   openpilot's `hondacan.py` fingerprints and community RE, not in DBCs.
8. **29-bit vs 11-bit diagnostics:** Honda's documented diagnostic path is
   29-bit (0x18DB33F1/0x18DAF1xx) [B]; the 11-bit 0x7E0/0x7E8 path is
   single-source [C]. Firmware should try 29-bit first.

---

## Sources consulted

- Honda service manual content via civic.hondafitjazz.com — B-CAN System
  Description (single-wire 33.33 kbps, gateway function, error codes),
  B-CAN troubleshooting (HDS + MPCS short-connector procedures), DLC
  Circuit Troubleshooting K20Z (DLC pin 7 = K-line circuit) [A]
- MotoLogic 2003 Honda Accord navigation diagnosis manual via manuals.plus
  (F-CAN 500 kbps, B-CAN link checks) [B]
- commaai/opendbc local clone — `car/honda/hondacan.py` (F-CAN A/B +
  ACC-CAN bus layout), `dbc/acura_ilx_2016_nidec.dbc` (36 messages) [B]
- vanillagorillaa/Honda-Civic-B-CAN (GitHub) — 2016 Civic/2017 CR-V BCM-tap
  project, 150 kbps B-CAN claim [C]
- papataku/honda_ehev_analyzer (GitHub) — real-vehicle 29-bit diagnostic
  IDs (18DAF101/102/106/10E/1EF), Mode-01 PID observations [B]
- hansonFish/obdii (GitHub) — 2009 Civic 29-bit diagnostic IDs
  (18DB33F1/18DAF110) [B]
- apatt124/ai-car-tuner (GitHub) — 2016–2021 Civic 11-bit UDS notes
  (0x7E0/0x7E8, extended session) [C]
- ScannerDanner/MaxiSys 2019 Civic scan report (scannerdanner.com) — "CAN
  gateway" as discrete system, IMA CAN DTCs [B]
- ScannerDanner Honda B-CAN video (2009 Odyssey single-wire case study) [B]
- Seeed Studio forum — 2008 Civic B-CAN 33.3 kbps owner confirmation [B]
- JustAnswer technician threads — 2017 Civic gateway module location,
  gateway-failure link-error case, 2004 Civic EX DLC pins 6/14 [C]
- FN2 ECU pinout (scribd) — ECU CAN H/L → OBD DLC 06/14 [B]
- Honda OBD system document (scribd) — 4P→16P DLC mapping: K-line → 7,
  SCS → 9 [B]
- carrottoptuning OBD2B Honda ECU pinouts — K-Line terminal, SCS pin [B]
- hondabase.com pinout tables — pre-OBD-II service connectors [B]
- obdii365 / xhorsetool / vxdiagshop / autosvs.com — HDS/i-HDS tooling,
  immobilizer PCM-code workflow, subscription pricing [C]
- CraigKielb B-CAN training deck (slideshare) — two-wire B-CAN depiction
  (conflicts with service manual) [C]

## Open items for the database build

- Resolve the B-CAN speed question for 2016+ models (33.33k vs 150k) —
  needs a real vehicle or a second independent source.
- Whether B-CAN on 2016+ is still single-wire (the 150k claim implies it
  may not be).
- Per-model gateway introduction years (which models got the dedicated
  gateway module and when).
- Honda-specific UDS DIDs per module (0x22) — a separate harvest task.
- IMA CAN bitrate/pins on hybrid models.
