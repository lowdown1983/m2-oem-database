# Volvo — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.4.0 expansion, "new makes"
track). Every factual claim carries a quality grade: **A** = factory
documentation or verified capture · **B** = reputable community source
(opendbc, well-documented reverse-engineering, trade/technician sources) ·
**C** = single anecdotal report. Unverified items are marked [?]. Items
reasonably inferred from solid premises are marked INFERRED. Research
date: 2026-10-07.

Platform reference used throughout: **P1** = C30 / S40 II / V50 / C70
(~2004–2013); **P2** = S60 I / S80 I / XC90 I / V70 II (~1999–2014);
**P3** = S60 II / V60 I / XC60 I / S80 II (~2007–2018); **SPA** = XC90 II
(2016+) / S90 / V90 / XC60 II (2018+) / S60 III (2019+); **CMA** = XC40
(2018+). Model years are US-market approximations [B — industry references,
cross-platform consistent].

---

## 1. Bus architecture

### 1.1 P1 / P2 / P3: two-CAN topology with CEM gateway

- Pre-SPA Volvos run **two CAN buses** behind the **CEM (Central
  Electronic Module)**, which acts as the inter-bus gateway. A community
  CAN-bus diagnostics document (appears to transcribe Volvo/VADIS
  diagnostic material) distinguishes the buses by fault codes: **E000 =
  HS-CAN checksum error, E001 = LS-CAN checksum error**, and documents
  CEM-DTCs 1A51–1A64 as "communication with" individual LS-CAN nodes
  [B — document is a VADIS-era transcription, consistent across multiple
  copies].
- Bitrates (community harness-verified pinout for a 2005 S60R P2) [C —
  single community repo, but consistent with module docs]:
  - 2004 model year: LS-CAN 125 kbps, HS-CAN 250 kbps
  - 2005+: LS-CAN 250 kbps, HS-CAN 500 kbps
- A 2010+ P1 CEM immobilizer-emulator document independently confirms
  **500 kbps, 11-bit (short) CAN IDs** on the P1 CAN for 2010+ cars,
  with CEM↔ECU SYNC traffic on 0x7FC–0x7FF [C — aftermarket vendor doc,
  cartools.lv].
- Network termination per the same diagnostics document [B]: the
  **low-speed network resistors live in the UEM and REM**; the
  **high-speed network resistors live in the ABS/BCM and ETM** (for Bosch
  EMS from MY02 onward, in the BCM and ECM instead).
- Practical topology (assembled from the CEM-1A51–1A64 node list and
  module maps) [B/C]: HS-CAN carries powertrain/chassis nodes
  (ECM, TCM, BCM/ABS, ETM, SAS); LS-CAN carries body/comfort nodes
  (SRS, DDM, PDM, PSM, CCM, DIM, RTI, PHM, AUD/MMM, REM, SWM, UEM).
  The **CEM sits on both** and routes between them [B].

### 1.2 DLC pinout (P1/P2/P3 era)

| DLC pin | Signal | Notes |
|---|---|---|
| 6 / 14 | HS-CAN (CANH/CANL) | Powertrain/chassis bus, 500 kbps (05+) [B/C] |
| 3 / 11 | MS/LS-CAN (CANH/CANL) | Body/comfort bus at the DLC. Bench-guide docs show body modules (DDM/PDM) bench-accessed via "OBD-11 / OBD-3" CAN pairs, and a P3 KVM bench doc states the module works "by CAN2 ... OBD cable pins 3-11" with an option to switch to "CAN1 ... OBD cable 6-14" in software [B — ioterminal bench docs; C — applies to P1/P2/P3 DLCs] |
| 7 | K-line | ISO 9141-2, 1996–2004 era [B — generic Volvo OBD pinout doc] |
| 4 / 5 | Chassis / signal ground | [B] |
| 16 | +12 V battery | [B] |
| 2 / 10 | J1850 Bus+ / Bus− | **Not populated on Volvo** — these columns appear in generic OBD-II pinout tables; Volvo never shipped J1850. Treat as empty [C — absence of any Volvo J1850 use in all sources checked] |

- Diagnostic adapter guidance: the V-Tool (third-party Volvo app) adapter
  page states that **MS-CAN support ("ForScan compatibility") is a MUST
  for full functionality on P1/P2/P3**, and explicitly that "SPA/CMA cars
  don't need MS-CAN support" — confirming MS-CAN is reachable at the DLC
  on P1/P2/P3 [B].
- Termination check: expect ≈60 Ω across DLC pins 6/14 (two 120 Ω
  terminators on HS-CAN) and ≈60 Ω across 3/11 (two 120 Ω terminators on
  LS-CAN) with ignition off — by analogy to the documented resistor
  locations [INFERRED — standard CAN practice + documented resistor
  locations; not measured on-vehicle in this pass].

### 1.3 SPA / CMA: domain architecture + Ethernet/DoIP

- SPA's electrical architecture is built around **four domain masters**:
  vehicle dynamics, safety, car body, and infotainment, on "one single
  nerve system" (Volvo Cars press material, 2014) [B].
- **DoIP (Diagnostics over IP) is confirmed on SPA/CMA** [B — Volvo
  Technical Journal 34165.1.1]: VIDA connects to SPA/CMA cars **via the
  OBD connector with an Ethernet cable** through a VOE (Vehicle Over
  Ethernet) adapter (Volvo p/n 9513108 / 9513062; passive aftermarket
  equivalents exist, one reviewer noting no active electronics inside,
  implying the DLC itself carries Ethernet pairs on SPA/CMA) [B — TJ;
  C — passive-adapter inference].
- In-vehicle SPA/CMA buses are widely reported as **CAN FD** by
  aftermarket tool vendors (e.g. "Volvo after 2018" listed under
  CAN-FD/DoIP tool support) [C — tool-vendor marketing, not a factory
  source]. Treat CAN FD on SPA/CMA as **INFERRED, OUT OF M2 SCOPE**:
  the M2's TJA1051 transceivers are CAN 2.0 only and its firmware has no
  CAN FD or DoIP stack [A — hardware fact from the knowledge pack].
- SPA/CMA cars do not expose a useful classic CAN pair at the DLC for
  third-party tools (V-Tool: no MS-CAN needed) [B].

### 1.4 Pre-CAN era (1996–2004)

- Volvo's OBD-II pinout guide: **1996–2004 = ISO 9141** (K-line pin 7,
  optional L-line pin 15), **2005+ = CAN** [B — generic Volvo OBD pinout
  document]. Pre-OBD-II Volvo flash-code boxes (940-era: diagnostic
  socket 2/6/3/4 mapped to DLC pins 3/1/12/16) are out of scope for CAN
  tooling [C].

---

## 2. Diagnostic access

### 2.1 Protocol and addressing (P1/P2/P3)

- Volvo used a **proprietary Volvo diagnostic protocol** on P1/P2/P3 —
  not standard UDS/ISO-TP with public documentation. VIDA talks to
  DiCE/the car in Volvo's own application layer; no public Volvo DID
  catalog was found (see §4). Community decoders treat diagnostic
  traffic as raw bytes [B — opendbc DBCs define `diagXxxReq/Resp` frames
  with opaque byte0–byte7 signals].
- Diagnostic CAN IDs observed in community captures (comma.ai opendbc,
  `volvo_v60_2015_pt.dbc` 41 msgs / `volvo_v40_2017_pt.dbc` 51 msgs —
  these are P3-era PT captures) [B]:
  - CEM: request **0x726**, response **0x72E** (+8 offset)
  - PSCM: request **0x730**, response **0x738**
  - FSM: request **0x764**, response **0x76C**
  - CVM: request **0x793**, response **0x79B**
  - Global/functional request: **0x7DF** (no paired response ID)
- Note the same **+8 response offset** convention as Toyota. The
  proprietary 0x72x–0x79x addressing does NOT follow the generic
  0x7E0/0x7E8 OBD pattern. Engine-ECM diagnostic addressing on these
  platforms was not verified in this pass [?].
- Standard emissions OBD-II (SAE J1979) on HS-CAN 6/14 works with any
  generic tool, 2005+ [A — legislated]. Volvo-specific diagnostics
  (beyond emissions) on P1/P2/P3 require Volvo's protocol — practically,
  DiCE + VIDA or a Volvo-aware third-party tool (VDASH/VDD, V-Tool)
  [B/C].

### 2.2 VIDA / DiCE ecosystem (legitimate paths)

- **VIDA (Vehicle Information & Diagnostics for Aftersales)** is Volvo's
  dealer diagnostic software: full-system DTC read/clear, live data,
  software downloads, module programming, key programming [B — Volvo
  TechInfo materials, forum documentation].
- Interface: **DiCE** (Diagnostic Communication Equipment, Volvo
  factory tool) or J2534 passthrough devices for limited programming
  (PCM only on 2004+ per a 2011 Volvo TechInfo guide) [B].
- **Legitimate path for security-gated operations: a paid VIDA
  subscription** from Volvo (volvotechinfo). Historical pricing found:
  $115.50 / 3 days (2011 Volvo TechInfo guide), $77.72 / 3 days (2016
  owner report). Treat as dated — current pricing is via Volvo
  TechInfo [C, dated]. All module software downloads live on Volvo's
  servers and are released per-VIN after payment — nothing ships on the
  VIDA media [B — matthewsvolvosite technician write-up].
- **Seed/key policy: no public Volvo UDS 0x27 algorithm exists in the
  sources consulted, and none is invented or reproduced here.**
  Security-gated work (module software, keys, CEM configuration) is
  dealer/paid-VIDA territory [B/C — absence of any documented
  community algorithm; consistent with the VIDA-server model].
- Immobilizer note (P1/P2/P3): CEM↔ECM pairing uses SYNC + ABS_ID on
  CAN 0x7FC–0x7FF (vendor doc) [C]; configuration changes on CEM/P1/P2/P3
  via VDASH require the CEM PIN (community tools decode it; the
  decoding method is not documented here) [C].
- Offline/community VIDA copies ("2014D" era, DiCE clones) are widely
  discussed in forums; they are not a legitimate path and are not
  endorsed here — documented only to distinguish from the paid
  subscription route [C].

### 2.3 What a DLC-connected M2 can see/do (P1/P2/P3)

- **Reads:** passive logging of both HS-CAN (6/14) and LS/MS-CAN (3/11)
  broadcast traffic — a dual-CAN tool sees the whole vehicle. The
  opendbc Volvo DBCs decode real signals (steering angle, wheel speeds,
  engine data, cruise buttons) from the PT bus [B — opendbc].
- **Emissions OBD-II:** standard modes on HS-CAN [A].
- **Writes:** Volvo-proprietary diagnostic addressing means generic UDS
  writes are not directly usable; writes to body modules go through the
  CEM's proprietary protocol, and security-gated writes need VIDA. The
  M2's 7-mode firmware can log both buses and run OBD2/ELM polling,
  but Volvo-specific module writes are a documented gap [C/INFERRED].
- **SPA/CMA:** out of reach — DoIP/Ethernet and (inferred) CAN FD have
  no M2 hardware path [B + hardware fact].

---

## 3. M2 hardware → Volvo bus mapping

| Volvo bus | DLC pins | Bitrate | M2 hardware path |
|---|---|---|---|
| HS-CAN (P1/P2/P3) | 6 / 14 | 500k (05+), 250k (04) | CAN0 or CAN1 (TJA1051, due_can). Primary powertrain/chassis bus |
| LS/MS-CAN (P1/P2/P3) | 3 / 11 | 250k (05+), 125k (04) | Second CAN controller (TJA1051) — body/comfort traffic. **Both DLC CAN pairs are usable simultaneously: the M2's dual CAN controllers match Volvo's dual-bus DLC exactly** |
| K-line (1996–2004) | 7 | 10.4k | K-line transceiver (TJA1027) |
| LIN sub-buses | not on DLC | 9.6–19.2k | LIN1/LIN2 (TJA1027) if tapped at the module [INFERRED — P1 wiring diagrams show LIN links, e.g. SWM] |
| J1850 | 2 / 10 | — | **Not populated on Volvo — no M2 J1850 use case** |
| SPA/CMA Ethernet/DoIP | DLC (via VOE adapter) | 100BASE-TX | **OUT OF SCOPE — no M2 hardware path** |
| SPA/CMA CAN FD | interior | — | **OUT OF SCOPE — TJA1051 is CAN 2.0 only** |

- The Alfaa123/Volvo-CAN-Gauge project (2011 C30 T5, P1) built a working
  gauge (boost/coolant/intake/timing) on a **Macchina M2** — proof the
  M2 hardware path to a P1 Volvo works in practice [C — community repo].
- P2 projects (martonn98/VolvoP2_CAN: Arduino + MCP2515 sniffing on a
  2002 S60; najnesnaj/moosesnif: P1 RE with DICE cable + WIP docs PDF)
  are the community reference points for P1/P2 frame decoding [C].

---

## 4. UDS DID catalog

**Honest gap:** no public Volvo-specific UDS DID (service 0x22) catalog
was found in this pass. Pre-SPA Volvo used a proprietary diagnostic
application layer (see §2.1); SPA uses UDS over DoIP but no community
DID tables were located. Entries below record only what can be
supported; per the task brief, ISO-standard DIDs are not duplicated
except where a Volvo-specific note applies.

## 0xF190 — (SPA, via DoIP)
- Name: VehicleIdentificationNumber (ISO 14229-1 standard DID)
- Description: 17-byte ASCII VIN. ISO-standard identification DID; on SPA
  it is served over DoIP. Not verified by capture in this pass.
- Make: volvo
- Size: 17 bytes
- Session: not documented
- Security: not documented
- Grade: [INFERRED — ISO standard DID + SPA uses UDS-over-DoIP; no
  Volvo-specific capture found]
- Evidence: ISO 14229-1 (standard); Volvo TJ 34165.1.1 (DoIP on SPA/CMA)

## 0xF187 / 0xF18A / 0xF18C — (SPA, via DoIP) [?]
- Name: VehicleManufacturerSparePartNumber / SystemSupplierIdentifier /
  ECU Manufacturing Date (ISO standard DIDs)
- Description: Standard identification DIDs expected on any UDS ECU.
  Listed as expected-but-unverified on SPA.
- Make: volvo
- Size: variable
- Session: not documented
- Security: not documented
- Grade: [? — not verified on any Volvo]
- Evidence: ISO 14229-1 only; no Volvo source

## Pre-SPA diagnostic identifiers — NOT UDS DIDs
- Note: Volvo's P1/P2/P3 diagnostic protocol is proprietary, not
  UDS-0x22. Community captures address modules by CAN ID
  (0x726/0x730/0x764/0x793 requests, +8 responses, 0x7DF functional)
  with opaque payloads — there is no public DID table to catalog
  [B — opendbc DBCs]. Do not confuse these CAN IDs with DIDs.

### Coverage notes (DIDs)
- Volvo-specific configuration/sensor DIDs (CEM configuration blocks,
  ECM live data): **not found in any public source** [?]. VIDA/DiCE
  reads these through the proprietary protocol; VDASH/VDD expose
  similar data through their own tooling without publishing DID tables.
- SPA DoIP DID tables (0xF190 confirmed only by inference): a future
  pass could target Volvo SPA community tooling (VDASH logs, V-Tool
  captures) for a real DID harvest.

---

## 5. Manufacturer-specific DTCs

Volvo DTC convention: **`<MODULE>-<CODE>`** — e.g. `CEM-1A51`,
`ECM-2A30`. VIDA displays the module-prefixed form; VADIS-era
documentation includes a **conversion table (Group 2, "Conversion
table...") mapping SAE P-codes to Volvo module codes** (e.g. P0607 ↔
ECM-711A per a VADIS quote on volvoxc) [B]. Generic OBD-II readers show
only the P-code side. Cause/notes fields are filled only where sources
support them; several descriptions below are terse because the sources
are terse.

### 5.1 CEM communication codes (LS-CAN node supervision)

## CEM-1A51
- Description: Communication with the supplemental restraint system module (SRS). Signal missing
- Category: U (network/communication; VIDA-internal family)
- Scope: manufacturer (Volvo)
- Possible causes: open circuit on LS-CAN to SRS; SRS node disconnected; weak/disturbed CAN message
- Diagnostic notes: Typical of an open circuit in the CAN bus; often appears with other CEM-1A5x codes. Disconnecting a node without first disconnecting the battery can set these.
- Grade: [B] description; [B] notes (Volvo CAN-bus diagnostics document)
- Evidence: Volvo CANbus diagnostics overview (VADIS-era transcription, via scribd)

## CEM-1A52
- Description: Communication with the driver door module (DDM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring to DDM; DDM disconnected
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A53
- Description: Communication with the passenger door module (PDM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring to PDM; PDM disconnected
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A55
- Description: Communication with the climate control module (CCM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring to CCM
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A56
- Description: Communication with the driver information module (DIM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring to DIM
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A5E
- Description: Communication with the steering wheel angle sensor module (SAS). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring to SAS
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A5F
- Description: Communication with the brake control module (BCM/ABS). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN wiring to BCM
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A61
- Description: Communication with the transmission control module (TCM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN wiring to TCM
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-1A62
- Description: Communication with the engine control module (ECM). Signal missing
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN wiring to ECM
- Diagnostic notes: See CEM-1A51 pattern.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

- Remaining codes in the family (not individually verified in this
  pass, listed for completeness) [B — same document]: CEM-1A54 (power
  seat module), CEM-1A57 (RTI), CEM-1A58 (phone module PHM),
  CEM-1A59 (audio module AUM), CEM-1A5A (rear electronic module REM),
  CEM-1A5B (steering wheel module SWM), CEM-1A5C (upper electronic
  module UEM), CEM-1A5D (electronic throttle module ETM),
  CEM-1A64 (differential electronic module DEM).

### 5.2 CEM CAN physical-layer codes

## CEM-DF03
- Description: CAN_H (or CAN_L) short to battery, low speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: pinched/shorted LS-CAN wiring; short between CAN_H and CAN_L; single-wire operation
- Diagnostic notes: Detection is continuous; a permanent fault is detected within a few seconds. Check for shorts between CAN H/L and to battery/ground on the LS bus.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF04
- Description: CAN_L short to ground, low speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN_L wiring shorted to ground
- Diagnostic notes: See CEM-DF03.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF05
- Description: CAN_H short to ground, low speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN_H wiring shorted to ground
- Diagnostic notes: See CEM-DF03.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF06
- Description: CAN_L or CAN_H short to battery, low speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: LS-CAN wiring shorted to battery
- Diagnostic notes: See CEM-DF03.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF13
- Description: CAN_H or CAN_L short to battery, high speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN wiring shorted to battery
- Diagnostic notes: High-speed-network counterpart of DF03–DF06.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF14
- Description: CAN_L short to ground, high speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN_L wiring shorted to ground
- Diagnostic notes: See CEM-DF13.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF15
- Description: CAN_H short to ground, high speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN_H wiring shorted to ground
- Diagnostic notes: See CEM-DF13.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## CEM-DF16
- Description: CAN_L or CAN_H short to battery, high speed network
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: HS-CAN wiring shorted to battery
- Diagnostic notes: See CEM-DF13.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## E000 (any node)
- Description: CAN high speed checksum error — communication fault with control unit on HS-CAN
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: disturbed/corrupt CAN message; contact bounce; single-wire operation; wrong-baud-rate node; faulty crystal in a node
- Diagnostic notes: Posted by any node; designed for contact-bounce/corrupted-message detection but also appears on CAN_H↔CAN_L shorts or one-wire communication. A permanent fault is detected within seconds.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

## E001 (any node)
- Description: CAN low speed checksum error — communication fault with control unit on LS-CAN
- Category: U
- Scope: manufacturer (Volvo)
- Possible causes: see E000, on the LS bus
- Diagnostic notes: LS counterpart of E000. E003 in some modules = configuration fault on the same buses.
- Grade: [B]
- Evidence: Volvo CANbus diagnostics overview

### 5.3 ECM P-code ↔ Volvo-code mappings (VADIS conversion table family)

These pairings come from community transcriptions of Volvo DTC lists
[B for the VADIS conversion-table mechanism per the volvoxc VADIS quote;
C for individual pairings — transcription sources]. Descriptions are the
Volvo-side wording.

## P0016 → ECM-670C
- Description: Camshaft position, inlet — High
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0532 → ECM-520D
- Description: A/C pressure sensor — Signal too low
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0533 → ECM-520C
- Description: A/C pressure sensor — Signal too high
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0560 → ECM-8200
- Description: Battery voltage — Faulty signal
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0561 → ECM-800B
- Description: System relay — Signal too low
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0602 → ECM-5110
- Description: Malfunction indicator light CEM — Faulty signal
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0604 → ECM-9970
- Description: Memory error RAM — Faulty signal
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0605 → ECM-9980
- Description: Memory error ROM — Faulty signal
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0606 → ECM-9990
- Description: Engine control module (ECM) — Faulty signal
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0607 → ECM-711A
- Description: Control module, internal fault (timer circuit)
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: corroded ECM connector (one shop report); internal ECM timer fault
- Diagnostic notes: VADIS conversion-table example: "DTC ECM-711A is stored if the engine control module registers a fault in the internal circuit for the timer in the control module." P0607 maps to a family of ECM-98xx/72xx internal-fault codes.
- Grade: [B] mapping mechanism + ECM-711A description (VADIS quote via volvoxc); [C] connector-cause note (single shop report)
- Evidence: volvoxc forum quoting VADIS Group 2 conversion table

## P0627 → ECM-291B
- Description: Fuel pump control module — Signal missing
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0628 → ECM-291D
- Description: Fuel pump control module — Signal too low
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0642 → ECM-810D
- Description: Power supply (5 volt) — Signal too low
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

## P0650 → ECM-660B
- Description: Malfunction indicator lamp (MIL) — Signal missing
- Category: P
- Scope: manufacturer (Volvo)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: carcarehacks Volvo fault-code list (transcription)

### Coverage notes (DTCs)
- The full Volvo code lists (scribd "PPC Volvo DTC" / "Volvo Fault
  Codes" transcriptions, thousands of ECM-xxxx/TCM-xxxx/SRS-xxxx/
  BCM-xxxx/DDM-xxxx/PDM-xxxx/CCM-xxxx/SWM-xxxx/SUM-xxxx/IAM-xxxx
  entries) were surveyed but only the communication-layer and
  P-code-mapping families above were extracted with grades — the
  remaining thousands of entries are raw transcriptions without
  cause/notes and were deliberately not bulk-imported [?].
- BCM/ABS, TCM, SRS, and SAS manufacturer ranges (e.g. BCM-0090
  family, TCM-E000/E003) appear in the CAN diagnostics doc but per-code
  descriptions are thin — future pass [?].
- SUM (suspension module, Four-C) codes (SUM-0322/0324/0326...,
  SUM-E000/E003) seen in transcriptions only [?].
- No Volvo-specific U-code (U1xxx) manufacturer definitions beyond the
  CEM communication family were verified [?].
- Diesel-specific codes (D5244T/D4204T ECM families) out of scope for
  this pass [?].
- No seed/key, immobilizer-defeat, or gateway-bypass material was
  sought or reproduced; immobilizer-adjacent notes (CEM↔ECM SYNC/ABS_ID
  IDs, CEM PIN tooling) are documented at the descriptive level only.

---

## 6. Module map notes (platforms)

### 6.1 P2 — XC90 I (2003–2014), representative

- **HS-CAN (500k, DLC 6/14):** ECM, TCM, BCM (ABS), ETM (electronic
  throttle module), SAS. Terminators in BCM + ECM (Bosch EMS MY02+)
  [B — CAN diagnostics doc].
- **LS-CAN (250k, DLC 3/11):** CEM (gateway), SRS, DDM, PDM, PSM, CCM,
  DIM, RTI, PHM, AUD/MMM, REM, SWM, UEM, DEM. Terminators in UEM + REM
  [B — CAN diagnostics doc].
- Community harness pinout exists for the 2005 S60R (433 pins across
  ECM, CEM, REM, TCM, SRS + 15 modules — jasongainor/volvo-p2-pinout,
  CSV) [C — single repo, harness-verified per author].
- opendbc has no P2 DBC; the V60/V40 PT DBCs are P3-era [B].

### 6.2 P3 — XC60 I (2009–2017), representative

- Same two-bus architecture as P2, CEM as gateway [B — architecture
  continuity; P3 KVM bench doc confirms the CAN1(6/14)/CAN2(3/11)
  split on P3 modules].
- **opendbc evidence (41-msg `volvo_v60_2015_pt.dbc`)** [B — real
  community captures]: PT-bus nodes include ECM (ECM1/ECM1_2/ECM2/ECM3),
  TCM, BCM, CEM (CEM0/CEM1/CEMBCM0), DIM (DIM0/DIM1), SRS (SRS0/SRS1),
  SAS (SAS0), PSCM, FSM, CVM; decoded signals include steering angle,
  wheel speeds, vehicle speed, accelerator pedal, cruise buttons,
  brake info, gear. Diagnostic addresses: 0x726/0x72E (CEM),
  0x730/0x738 (PSCM), 0x764/0x76C (FSM), 0x793/0x79B (CVM), 0x7DF
  functional.
- `volvo_v40_2017_pt.dbc` (51 msgs, V40 = P1-platform car, MY2017)
  shows the same PT node set plus ACC — indicating the P1 bus
  architecture carried through to end of production [B].

### 6.3 SPA — XC90 II (2016+), representative

- Four domain masters (vehicle dynamics, safety, car body,
  infotainment) on a unified network [B — Volvo Cars press].
- **Diagnostics = DoIP over Ethernet via VOE adapter** at the DLC
  [B — Volvo TJ 34165.1.1]; in-vehicle buses reported as CAN FD by
  tool vendors [C/INFERRED].
- **M2 scope boundary: SPA/CMA are out of scope** — no CAN FD, no
  Ethernet/DoIP hardware on the M2 [A — hardware fact].
- CMA (XC40 2018+): same diagnostic posture as SPA (VOE/DoIP; "SPA/CMA
  cars don't need MS-CAN") [B].

---

## 7. Notable quirks

1. **Volvo's DLC exposes BOTH CAN buses (6/14 HS + 3/11 LS).**
   Unlike Toyota (HS only at DLC), a two-channel tool sees the entire
   P1/P2/P3 vehicle from the DLC — the M2's dual CAN controllers map
   1:1 onto this. MS-CAN-capable adapters are mandatory for full
   third-party coverage [B].
2. **Proprietary diagnostic addressing.** No 0x7E0/0x7E8 convention
   for Volvo-specific diagnostics — captured modules answer on
   0x72x–0x79x with a +8 response offset and 0x7DF functional requests.
   Generic UDS scan logic aimed at 0x7E0 will miss everything except
   emissions [B].
3. **E000/E001 are per-node CAN checksum codes**, not module faults —
   treat as bus-health indicators first, module faults second [B].
4. **Bitrate changed across model years.** '04: 125k/250k; '05+: 250k/500k
   for LS/HS. A sniffer set to the wrong rate sees nothing — check model
   year first [C].
5. **No J1850 on Volvo despite generic pinout tables.** Pins 2/10 are
   empty; don't chase J1850 firmware paths [C].
6. **VIDA is server-tethered.** Software downloads are per-VIN from
   Volvo's servers; offline/community VIDA copies can't do module
   programming — the legitimate path is a paid subscription [B/C].
7. **CEM PIN culture.** P1/P2/P3 configuration tooling (VDASH) works
   with decoded CEM PINs; decoding methods are not documented here —
   configuration writes stay in the legitimate-tools lane [C].
8. **P1 blink codes.** A 2008 C30 owner reports DTCs can be displayed
   in the cluster by holding the trip-reset button with the key in
   position II — a no-tool read path on P1 [C — single owner video
   report, unverified scope].
9. **SPA hard boundary.** Anything SPA/CMA (2016+) needs DoIP/CAN FD —
   flag early so M2 time isn't wasted there [B].

---

## Sources consulted

- Volvo CAN-bus diagnostics overview (VADIS-era transcription, "Tech-net
  bus info Volvo CANBUS", via scribd) — E000/E001, CEM-1A51–1A64,
  DF03–DF16, resistor locations, VADIS reference [B]
- jasongainor/volvo-p2-pinout (GitHub) — 2005 S60R harness-verified
  pinout, LS/HS speeds by model year, CEM gateway role, community
  project pointers (VolvoP2_CAN, Volvo-CAN-Gauge/M2, moosesnif) [C]
- ioterminal Volvo module bench guides (via scribd) — DLC pins 3/11
  vs 6/14 for CAN2/CAN1 on P3 KVM and DDM/PDM modules [B]
- Volvo OBD-II diagnostic connector pinout (via scribd) — pin table,
  1996–2004 ISO 9141 / 2005+ CAN split [B]
- Volvo CEM signal descriptions (via scribd) — CEM connector CAN_H/L
  high/low speed pins [B]
- V-Tool supported-adapters page (v-tool.app) — MS-CAN mandatory on
  P1/P2/P3, not needed on SPA/CMA [B]
- Volvo Technical Journal 34165.1.1 (via tsbsearch.com) — VOE/Ethernet
  VIDA connection on SPA/CMA, DiCE fallback, VCM reset [B]
- Volvo Cars SPA press material (via autoserviceworld.com) — four
  domain masters [B]
- OTOFIX/ThinkDiag tool listings — "Volvo after 2018" under CAN-FD/
  DoIP support [C]
- comma.ai opendbc (local clone): volvo_v60_2015_pt.dbc (41 msgs),
  volvo_v40_2017_pt.dbc (51 msgs) — PT signal decodes + proprietary
  diagnostic CAN IDs [B]
- cartools.lv VOLVO_CEM5_en.pdf — P1 2010+ 500k 11-bit CAN, CEM↔ECM
  SYNC/ABS_ID on 0x7FC–0x7FF [C]
- volvoxc.com forum — VADIS P0607↔ECM-711A conversion-table quote [B];
  VIDA subscription how-to thread [C]
- matthewsvolvosite.com forums — VIDA 2014D/2015 software-download
  model (server-side, per-VIN) [B]; $77.72 3-day subscription report
  (2016) [C]
- automotivetechinfo.com 2011 VIDA guide — $115.50/3-day historical
  pricing, DiCE/J2534 programming notes [B, dated]
- carcarehacks.com Volvo fault-code list — P-code↔ECM-xxxx pairings
  (transcription) [C]
- algperformance.co.uk — VDASH/J2534 community diagnostics overview [C]
- YouTube: P1 C30 trip-button DTC display report [C]

## Open items / Coverage notes

- Engine-ECM diagnostic CAN addressing on P1/P2/P3 (the 0x72x set
  covers CEM/PSCM/FSM/CVM; ECM/TCM/BCM diagnostic IDs unplaced) [?]
- Full extraction of the thousands-entry Volvo module-code lists
  (TCM/SRS/BCM/DDM/PDM/CCM/SWM/IAM/SUM families) — surveyed, not
  imported [?]
- Volvo-specific UDS DID tables (pre-SPA proprietary protocol notes;
  SPA DoIP capture harvest) [?]
- Confirmation of in-vehicle CAN FD on SPA/CMA from a primary source
  [?]
- Per-platform gateway routing tables / CEM part numbers [?]
- Diesel (D5/D4/D2) ECM DTC families [?]
- XC40 CMA vs SPA electrical differences, if any [?]
- Polestar-era (SPA2/EX) platforms: assumed further out of scope,
  not researched [?]
