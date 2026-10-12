# BMW — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.4.0 "new makes" track). Every
factual claim carries a quality grade: **A** = factory/BMW documentation or
verified capture · **B** = reputable community source (opendbc,
well-documented reverse-engineering, technician sources, BMW training docs
via archives) · **C** = single anecdotal report. Unverified items are marked
[?]. INFERRED items are labeled as such, never as fact. Research date:
2026-10-07.

BMW spans three very different network generations: **E-series** (~2004–2013,
CAN 2.0 + MOST + byteflight), **F-series** (~2009–2019, CAN 2.0 + FlexRay +
MOST + Ethernet/ENET), **G-series** (2015/2019+, CAN FD + DoIP/Ethernet).
Only the E-series — and the CAN 2.0 diagnostic path of the F-series — is
reachable with M2-class CAN 2.0 hardware. FlexRay, MOST, byteflight,
CAN FD, and DoIP-Ethernet are OUT OF M2 SCOPE and are documented here
precisely so they are not mistaken for CAN targets.

---

## 1. Bus architecture

### 1.1 E-series (E90/E91/E92/E93, E60/E61, E63/E64, E65/E66, E70, E83, E87;
~2004–2013)

BMW technical training (ST401 Body Electronics II, "Bus Systems" — BMW
training document via archive.org) defines the E-era bus set [A]:

| Bus | Bitrate | Role |
|---|---|---|
| PT-CAN (powertrain CAN) | 500 kbit/s | Drivetrain: DME/DDE, EGS, DSC, EKPS, JBE as gateway |
| K-CAN (body CAN) | 100 kbit/s | Body/comfort: CAS, FRM, KOMBI, IHKA, MRS, FZD, CCC, PDC |
| F-CAN (chassis CAN) | 500 kbit/s | DSC ↔ SZL ↔ active steering (AL) |
| D-CAN (diagnostic CAN) | 500 kbit/s | Diagnostic bus to the DLC (from 03/2007 builds) |
| MOST | 22.5 Mbit/s | Infotainment ring (fiber optic): CCC/CIC, CID, CON, amp, TCU/ULF |
| byteflight | 10 Mbit/s | Safety bus, star over fiber (E60/E63/E64 door satellites TMFA/TMBF; E65) |
| K-bus | 9.6 kbit/s | Legacy single-wire body bus (older models) |
| D-bus | 10.5–115 kbit/s | Legacy single-wire diagnostic bus |
| LIN | 9.6–19.2 kbit/s | Sub-buses (mirrors, wipers, IHKA flap motors) |
| BSD | 9.6 kbit/s | Bit-serial data, single wire (alternator, oil sensor) |

- PT-CAN physical detail from the same training doc: three wires, not two —
  CAN-H/CAN-L twisted pair **plus a separate wake-up line**; 120 Ω
  terminators at the ends (60 Ω measured across the pair, de-energized) [A].
- K-CAN is 100 kbit/s per the training doc [A]. Community CAN-project work
  (bimmerforums E90 CAN project) treats K-CAN as fault-tolerant/low-speed
  style (ISO 11898-3-like) and found standard 11898-2 transceivers (MCP2551)
  unreliable on it [C — single experimenter's report, but consistent with
  BMW's 100k body-bus design].
- K-CAN is **not wired to the DLC** on E90; on pre-03/2007 cars even PT-CAN
  may be absent from the DLC — check the wiring diagram per car [C —
  bimmerforums E46/E90 CAN threads].
- D-CAN changeover: 03/2007 for E90/E91/E92/E93, E81/E87; 09/2006 for E83;
  E60/E61 from 03/2007; E70 and R56 from start. Earlier cars use K-line
  (the K+DCAN cable's switch selects between them) [B — cable-vendor model
  tables corroborated by community install reports].
- Sub-bus protocols (BSD, LIN, DWA bus) all run 9.6 kbit/s single-wire per
  the BMW bus table [B — BMW doc via share.qclt.com mirror of the same
  training family].

### 1.2 Gateway architecture (E-series)

- **JBE/JBBF** (junction box electronics) is the gateway between PT-CAN and
  K-CAN (with F-CAN pass-through) [B — BMW E90 "General Vehicle Electrical"
  manual via manualslib: JBE listed as "Gateway Module for vehicle Bus
  System"; e90post K-CAN thread: "SZL is on F-CAN... packet data is forwarded
  to PT-CAN by DSC. Then JBE forwards the data from PT-CAN to K-CAN"].
- **DSC** is the gateway between F-CAN and PT-CAN [B — e90post].
- E65/E66 (and E60/E63/E64 without JBE) use a dedicated **ZGM** (central
  gateway module); E85/E60/E63/E64 have no ZGM [B — BMW training glossary via
  archive.org].
- The DLC D-CAN connects through the gateway structure — diagnostics for
  K-CAN modules are routed, not direct [C — inferred from the gateway
  architecture and the bimmerforums D-CAN protocol notes].

### 1.3 F-series (F01/F02, F10/F11, F30/F31/F32/F80, F15/F25, F56 MINI;
~2009–2019)

BMW F30 "Complete Vehicle" training material (via bimmerscan.com FEM page,
which reproduces the BMW training tables) [B]:

| Bus | Bitrate | Role |
|---|---|---|
| PT-CAN | 500 kbit/s | DME/DDE, EGS, ACSM, EKPS, GWS, KAFAS cameras, REM-A/REM-B |
| PT-CAN2 | 500 kbit/s | Redundancy for engine/transmission control (introduced with BN2020 on F01) [A — ST401] |
| K-CAN (Body CAN) | 100 kbit/s | SMFA/SMBF seat modules, AHM trailer, IHKA, CON controller |
| K-CAN2 | 500 kbit/s | REM, FZD, PMA, FLA, headunit (NBT moved the iDrive controller here) |
| FlexRay | 10 Mbit/s | Chassis dynamics: DSC, ICM, VDM, EPS, TRSVC camera |
| MOST | 25 Mbit/s class | Infotainment ring (headunit distributes) |
| Ethernet | 100BASE-TX | HU-H, KOMBI, CBX-MEDIA, CBX-ECALL, audio amplifier |
| D-CAN | 500 kbit/s | Diagnostic socket link |

- **ZGM (central gateway module) is integrated into the FEM** (Front
  Electronic Module) on F30 and routes between all of the above [B].
- K-CAN2 speed independently confirmed at 500 kbit/s by the open-source
  superwofy E9X-M-CAN-Integration-Module (K-CAN = 100k, K-CAN2 = 500k in its
  CAN setup) [B — open-source hardware project, github.com/superwofy].
- iDrive controller moved from K-CAN to K-CAN2 with the NBT head unit (~2014);
  the two buses run different speeds so modules are not interchangeable [B —
  f30.bimmerpost K-CAN4 thread].
- FlexRay runs the safety-relevant chassis loop; the ZGM contains a FlexRay
  star coupler with 4 bus drivers [B — bimmerscan/FEM training page].

### 1.4 G-series (G11/G12, G30, G20, G05, G07, G29; 2015/2019+)

- **BDC (Body Domain Controller)** replaces FEM as the central gateway and
  is the core immobilizer/security module; **BDC3** from ~2020 model year
  (G20 3-series, G30 5-series, G05 X5, etc.) [B — obdii365.com BDC3 repair
  case study and Autel BDC03 model list].
- **CAN FD** is used on G-series buses (out of M2 scope — the TJA1051 is CAN
  2.0 only) [B — widely documented; per-bus FD topology details not verified
  in this pass, see Open items].
- K-CAN4 in the G30 is the functional equivalent of F30's K-CAN2 (carries
  IHKA, HU, TCB, ZBE) [C — f30.bimmerpost retrofit thread].
- Diagnostics are DoIP-over-Ethernet (ENET cable, OBD pins 3/11/12/13);
  ISTA is the dealer tool [B — ENET cable pinout docs + E-Sys coding
  community].
- BDC3 immobilizer work is heavily encrypted and requires specialist
  equipment (ISN extraction, new OEM module); legitimate path is dealer or
  licensed locksmith tooling — no bypass material is sought or reproduced
  here.

### 1.5 Model-year evolution (rule of thumb)

- **Pre-2007 E-series:** K-line diagnostics (pin 7/15 style), PT-CAN +
  K-CAN + F-CAN + MOST (+ byteflight on some).
- **03/2007+:** D-CAN (500k, pins 6/14) replaces K-line as the diagnostic
  bus; dual-stack diagnostics (KWP2000 + UDS on later DMEs).
- **F-series (2009+):** ZGM/FEM gateway, FlexRay for chassis, K-CAN2 500k,
  MOST + Ethernet for infotainment, ENET/DoIP for coding and diagnostics.
- **G-series (2015/2019+):** BDC gateway, CAN FD, DoIP primary; K-CAN4
  naming appears.

---

## 2. Diagnostic access

### 2.1 DLC pinout per generation

| DLC pin | E-series (03/2007+) | F-series | G-series |
|---|---|---|---|
| 6 / 14 | D-CAN 500k (diagnostic bus) [B] | D-CAN to ZGW 500k [B] | D-CAN / DoIP-adjacent CAN [C — pin presence varies] |
| 3 / 11 / 12 / 13 | — | ENET Ethernet: 3=TX+, 11=TX−, 12=RX+, 13=RX− (100BASE-TX) [B] | same ENET/DoIP [B] |
| 4 / 5 | chassis/signal ground | ground | ground |
| 16 | +12 V | +12 V | +12 V |
| 7 / 15 | K-line (pre-D-CAN cars) [C] | — | — |

- ENET pinout confirmed by two independent DIY references (beemuu project
  docs on GitHub; team-bhp DIY thread): OBD 3→TX+, 11→TX−, 12→RX+, 13→RX−,
  with the standard 100BASE-TX 100 Ω termination in the cable [B].
- AiM motorsport documentation confirms DLC **6/14 = CAN-H/CAN-L** on BMW
  (their BMW_PT6 profile reads PT-CAN traffic at the DLC) [B].

### 2.2 E-series: D-CAN diagnostic protocol (0x6F1 scheme)

Documented by the bimmerforums E90 CAN-bus project (multi-year community
reverse-engineering effort, corroborated against EDIABAS/Tool32 job
definitions) [B]:

- Every ECU has a **module ID**; diagnostic conversations use CAN ID
  **0x6F1** (tester → ECU) and **0x600 + module ID** (ECU → tester).
- Request frame: `0x6F1: [moduleID] [len] [cmd0..cmd5]` — byte 0 is the
  target module, byte 1 the command length, bytes 2–7 the command payload.
- Response frame: `0x6XX: [0xF1] [0x10] [len] [data...]` — byte 0 is 0xF1
  (tester address), byte 1 is 0x10, then length + data.
- Command bytes line up with **KWP2000 service/subfunction numbers** as
  listed in EDIABAS Tool32 job definitions — i.e. E-series diagnostics are
  KWP2000-over-CAN, not UDS DIDs [B].
- `0xEF` is the broadcast/all-call module address; `0xF1` is the tester
  address on the bus [B].
- Partial module-ID table (from the same thread; DME/EGS/DSC IDs were not
  in the reproduced portion — see Open items):

| ID | Module |
|---|---|
| 0x00 | JBBF (junction box) |
| 0x01 | MRS (airbag) |
| 0x40 | CAS (car access system, incl. ELV) |
| 0x41 | DWA (anti-theft alarm) |
| 0x50 | SINE (siren + tilt sensor) |
| 0x56 | FZD (roof function center) |
| 0x60 | KOMBI (instrument cluster) |
| 0x64 | PDC (park distance control) |
| 0x72 | FRM (footwell module) |
| 0x78 | KLIMA / IHKA (climate) |

### 2.3 KWP2000 → UDS transition

- Early E-series: KWP2000 only (EDIABAS/INPA jobs: `STATUS_*`,
  `C_*_LESEN`, `FS_LESEN` for fault memory).
- Later E-series DMEs (MSD80/MSD81 on N54, MEVD17 family): dual-stack —
  KWP2000 preserved for Tool32/INPA, plus UDS services (0x19 for the hex
  fault-code format, 0x22 for data). The "CAN DME Code List" for the N54
  (hex codes 29CD…, 2A87…, 3100…) is the UDS-0x19-era format [C — scribd
  transcription of a community N54 code list].
- F/G-series: UDS over DoIP is the primary diagnostic protocol; CAN-side
  diagnostics go through the ZGW/BDC gateway. Bench flashing of modern
  Bosch MG1 DMEs happens in the bootloader over FlexRay-encapsulated or
  Ethernet paths — "there is no CAN tester communication with the ECU
  outside of SBOOT" for the MG1 application software [C — nefariousmotorsports
  ECU-flashing thread; single expert source, flagged].

### 2.4 Tool ecosystem (legitimate paths)

- **ISTA** (Integrated Service Technical Application, "Rheingold") — BMW
  dealer diagnostic/programming software; full fault read/clear, live data,
  service functions, programming [B — universally referenced in BMW
  technician sources].
- **E-Sys** — F/G-series coding/flashing over ENET (needs a token/launcher
  for full function; community-supported) [B — bimmerpost coding threads].
- **INPA / NCS Expert / Tool32 / WinKFP** (EDIABAS suite) — E-series
  diagnostics, coding, module flashing via K+DCAN cable [B — long-standing
  community tooling].
- **BimmerCode / BimmerLink / ProTool / Deep OBD** — phone/PC apps for
  coding and BMW-specific fault codes [C].
- **ICOM** — BMW dealer interface (ICOM Next) for DoIP + MOST + all buses;
  aftermarket ICOM clones exist [B].
- Seed/key: BMW UDS 0x27 security access for flashing/programming exists
  but **no public algorithm is documented; none is invented or reproduced
  here**. Immobilizer (EWS/CAS/FEM/BDC + DME ISN alignment) is dealer or
  licensed-specialist territory. What a DLC CAN tool CAN do without any of
  that: passive logging, OBD-II legislated modes, E-series 0x6F1 reads,
  fault-memory reads — all read-side operations.

### 2.5 What a DLC-connected CAN 2.0 tool can actually see

- **E-series (D-CAN, 03/2007+):** full diagnostic conversations via 0x6F1
  (KWP2000 jobs, fault memory, live data) plus passive PT-CAN traffic at
  500k. K-CAN (100k) is reachable only by tapping the interior harness
  behind the JBE — it is not on the DLC. F-CAN (DSC/SZL/AL) likewise needs
  a direct tap. MOST/byteflight are fiber — unreachable.
- **F-series:** DLC 6/14 carries D-CAN to the ZGW (diagnostic gateway
  function — the ZGW routes/encapsulates, e.g. CAN→FlexRay encapsulation
  for chassis ECUs). Reading fault memory and live data through the gateway
  works with the right addressing; raw PT-CAN/K-CAN2/FlexRay traffic is
  NOT on the DLC — it is filtered by the gateway. Full access needs ENET +
  DoIP (out of M2 scope).
- **G-series:** primarily a DoIP/Ethernet diagnostic world; CAN FD buses
  are out of M2 scope entirely. DLC CAN presence is model-dependent —
  verify per car [?].
- Writes: E-series KWP2000 coding/actuation via 0x6F1 is the classic
  community path (NCS/Tool32); F/G-series writes go through ENET/DoIP and
  increasingly behind security (SFD-style locks on 2020+ — the bmw-unified-db
  project notes writes gated behind a BMW-signed token it cannot produce).
  No gateway-bypass or lock-defeat material is documented here.

---

## 3. M2 hardware → BMW bus mapping

| BMW bus | DLC pins | Speed | M2 hardware path |
|---|---|---|---|
| D-CAN (diagnostic, E 03/2007+, F) | 6 / 14 | 500k CAN 2.0 | CAN0 or CAN1 (TJA1051, due_can). Primary diagnostic + logging path |
| PT-CAN (E-series, where on DLC) | 6 / 14 on early E90s [C] | 500k CAN 2.0 | Same — passive logging of drivetrain traffic |
| PT-CAN (direct tap) | not on DLC | 500k CAN 2.0 | Second CAN controller if tapped in harness |
| K-CAN (100k) | not on DLC | 100k, fault-tolerant-style [C] | Tap behind JBE only; transceiver compatibility not verified — flag before assuming MCP2551/TJA1051 works [C] |
| K-CAN2 (F, 500k) | not on DLC | 500k CAN 2.0 | Tap at ZGW/FEM harness with second CAN controller |
| F-CAN (E, 500k) | not on DLC | 500k CAN 2.0 | Direct tap at DSC/SZL |
| K-bus single wire (9.6k) | not on DLC | proprietary single-wire | **No M2 hardware support** — not K-line, not LIN |
| LIN sub-buses | not on DLC | 9.6–19.2k | LIN1/LIN2 (TJA1027) if tapped at the module |
| BSD (9.6k single wire) | not on DLC | proprietary | Out of scope |
| MOST (fiber ring) | not on DLC | 22.5 Mbit/s optical | **Out of scope** — fiber, no copper tap |
| byteflight (fiber star) | not on DLC | 10 Mbit/s optical | **Out of scope** — fiber |
| FlexRay | not on DLC | 10 Mbit/s | **Out of scope** — no M2 hardware |
| Ethernet/ENET/DoIP | 3 / 11 / 12 / 13 | 100BASE-TX | **Out of scope** — needs Ethernet MAC + DoIP stack |
| CAN FD (G-series) | various | up to 2–5 Mbit/s data phase | **Out of scope** — TJA1051 is CAN 2.0 only |

M2 firmware notes:
- The 7-mode firmware's UDS/diagnostics mode can implement the **0x6F1
  KWP2000-over-CAN** scheme on E-series directly (11-bit IDs, 8-byte
  frames — fully CAN 2.0).
- The OBD2 poller mode covers legislated SAE J1979 on any 2008+ BMW via
  6/14 (US) / 2001+ petrol, 2004+ diesel (EU).
- MITM mode is CAN-2.0-only: usable on E-series PT-CAN/K-CAN/F-CAN taps
  and F-series D-CAN, never on FlexRay/MOST/CAN FD.

---

## 4. UDS DID catalog

BMW-specific note (structural finding): **E-series diagnostics are not
DID-oriented.** The D-CAN diagnostic layer is KWP2000-over-CAN addressed by
the 0x6F1/0x6XX scheme (§2.2); EDIABAS jobs (`STATUS_*`, `C_*_LESEN`,
`FS_LESEN`) are the canonical data interface, not service 0x22. Later
E-series DMEs add UDS services, and F/G-series use UDS over DoIP — but **no
publicly verified BMW-specific DID table was found** in this pass (see Open
items). ISO-standard identification DIDs live in `did-iso.md` and are NOT
duplicated here; BMW-specific notes on them follow.

## 0xF190 — BMW VIN note
- Name: VINDataIdentifier (ISO) — BMW application note
- Description: 17-byte ASCII VIN. On BMW it is readable from multiple
  modules (DME/DDE, CAS/FEM/BDC, KOMBI); E-series via EDIABAS
  `C_FG_NR_LESEN`-family jobs or UDS 0x22 on later DMEs; F/G-series via UDS
  over DoIP. BMW WMI codes include WBA/WBS/WBY (Germany), 5UX (US
  Spartanburg), MM0/MM3 (various). The 11th character is the plant code.
- Make: bmw
- Size: 17 bytes ASCII
- Session: not documented (default session typical for VIN)
- Security: not documented
- Grade: [B] (ISO size/encoding [A] in did-iso.md; BMW multi-module
  readability and job names from community INPA/EDIABAS documentation [B])
- Evidence: did-iso.md (0xF190); BMW EDIABAS/INPA community documentation;
  BMW VIN structure per bmwinsights.com VIN decoder guide

## 0xF186 — BMW active-session note
- Name: ActiveDiagnosticSessionDataIdentifier (ISO) — BMW application note
- Description: BMW dealer tools (ISTA) and E-Sys move ECUs into extended /
  programming sessions for coding and flashing; reading 0xF186 confirms the
  session actually switched before sending session-gated services. Relevant
  because BMW gateways have been observed dropping session-gated writes
  silently when the session request did not take.
- Make: bmw
- Size: 1 byte
- Session: default
- Security: not documented
- Grade: [C] (ISO definition [A] in did-iso.md; BMW behavioral note from
  E-Sys/ISTA community reports, single-thread sources)
- Evidence: did-iso.md (0xF186); bimmerpost E-Sys coding threads

### KWP2000-era equivalent (E-series, service 0x21 — NOT UDS 0x22)
- Name: readDataByLocalIdentifier (KWP2000 0x21)
- Description: On E-series ECUs the analog of DIDs is KWP2000 service 0x21
  local identifiers, sent inside the 0x6F1 frame format (§2.2). Do not
  confuse these local IDs with UDS 0x22 DIDs — different service, different
  numbering. No verified BMW local-identifier table was found in this pass.
- Make: bmw
- Size: ECU-specific
- Session: not documented
- Security: not documented
- Grade: [C] (protocol fact [B]; table absence [?])
- Evidence: bimmerforums E90 CAN project (KWP2000 command bytes in 0x6F1);
  EDIABAS Tool32 job definitions

### Coverage notes (DID)
- No verified BMW-specific sensor/live-data DID table (0x0100–0xA5FF
  ranges) was found in public sources this pass. BMW live data is
  conventionally read via EDIABAS jobs (E-series) or ISTA/DoIP (F/G) —
  those interfaces are job-oriented, not DID-oriented.
- The open-source `gediz/bmw-unified-db` project (GitHub) claims 2,466 BMW
  ECUs decoded from BMW diagnostic data including UDS service bytes and
  fault dictionaries, but it was not ingested here (653 MB; provenance is
  BMW-internal data; not independently verified) — flagged as a lead, not
  a source [?].

---

## 5. Manufacturer-specific DTCs

BMW uses **two code formats**: factory **hex fault codes** (e.g. `2A87`)
are the native format stored by the ECUs and read by BMW tools; **P1xxx /
B1xxx / C1xxx / U1xxx** are the OBD-II-legislated translations. One P-code
can correspond to several hex codes (e.g. the meeknet BMW fault-code PDF for
1996–2003 DME/DDE/EML/GS documents an explicit P-code → BMW-FC decimal
mapping table) [B]. Hex-code descriptions below come from EDIABAS Tool32
`.prg` data (MSD80 DME), BMW service bulletins, and technician sources.

### P-code (OBD-II translation) entries

## P1014
- Description: Valvetronic reference — eccentric shaft sensor parity error
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: valvetronic eccentric shaft sensor shorted or poor electrical connection; valvetronic system electrical fault
- Diagnostic notes: Check-engine light on; valvetronic system is complex — professional diagnosis recommended per the source.
- Grade: [C]
- Evidence: obdeleven.com BMW fault-code blog (single source)

## P1083
- Description: Fuel Control Mixture Lean (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd, single transcription of a BMW-specific list)

## P1084
- Description: Fuel Control Mixture Rich (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1083.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1085
- Description: Fuel Control Mixture Lean (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1083.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1086
- Description: Fuel Control Mixture Rich (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1083.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1087
- Description: O2 Sensor Circuit Slow Response in Lean Control Range (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: aging O2 sensor
- Diagnostic notes: Slow-response code — sensor still functions but is lazy.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1088
- Description: O2 Sensor Circuit Slow Response in Rich Control Range (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: aging O2 sensor
- Diagnostic notes: See P1087.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1090
- Description: Pre-Catalyst Fuel Trim Too Lean Bank 1
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: Fuel-trim extreme — check for intake leaks before condemning sensors.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1091
- Description: Pre-Catalyst Fuel Trim Too Rich Bank 1
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1090.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1092
- Description: Pre-Catalyst Fuel Trim Too Lean Bank 2
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1090.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1093
- Description: Pre-Catalyst Fuel Trim Too Rich Bank 2
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: See P1090.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1111
- Description: Engine Coolant Temperature Radiator Outlet Sensor Low Input
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: radiator outlet temp sensor circuit low
- Diagnostic notes: BMW uses a separate radiator-outlet temp sensor in addition to the engine coolant sensor.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1112
- Description: Engine Coolant Temperature Radiator Outlet Sensor High Input
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: radiator outlet temp sensor circuit high
- Diagnostic notes: See P1111.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1115
- Description: Coolant Temperature Sensor Plausibility
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: Plausibility code — compares redundant temp sensors; check both before replacing either.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1120
- Description: Pedal Position Sensor Circuit
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1121
- Description: Pedal Position 1 Range/Performance Problem
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1132
- Description: O2 Sensor Heater Control Circuit (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: open/short in heater circuit; failed heater element
- Diagnostic notes: Check heater resistance at the sensor connector first.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1133
- Description: O2 Sensor Heater Control Circuit (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: open/short in heater circuit; failed heater element
- Diagnostic notes: See P1132.
- Grade: [C]
- Evidence: "DTC P1xxx BMW" transcription (scribd)

## P1318
- Description: Camshaft Position Sensor 'B' Circuit Signal Duration after Initialization (Bank 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: camshaft position sensor B (exhaust); wiring
- Diagnostic notes: BMW-specific code — generic scanners list no definition. Often appears with P0340/P0365.
- Grade: [C]
- Evidence: bimmerforums thread (2003 Z4 owner; definition supplied by a second member — single thread)

## P1339
- Description: Camshaft Position Sensor 'B' Faulty Phase Position (Bank 1)
- Category: P
- Scope: manufacturer (BMW)
- Possible causes: camshaft sensor B; timing/phase issue
- Diagnostic notes: See P1318.
- Grade: [C]
- Evidence: bimmerforums thread (same as P1318)

### BMW factory hex-code entries (native ECU format)

## 2A82
- Description: VANOS intake — stiff; jammed mechanically
- Category: P (factory hex; surfaces via UDS 0x19 / Tool32 FS_LESEN)
- Scope: manufacturer (BMW)
- Possible causes: insufficient oil pressure supply to the intake VANOS adjustment unit; sticking VANOS solenoid; oil passages restricted
- Diagnostic notes: BMW SIB 11 02 08: faults set when the camshaft is "late" or does not reach target position in the specified time under all engine conditions; engine power may be reduced with a check-control message. Check oil quality/level and pressure before replacing solenoids. N52/N54 engines.
- Grade: [A] description (BMW SIB 11 02 08 via oemdtc/NHTSA); [B] causes (SIB cause section + community agreement)
- Evidence: BMW SIB 11 02 08 (2020-04-21); bimmerforums VANOS threads

## 2A87
- Description: VANOS exhaust — stiff; jammed mechanically
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: insufficient oil pressure to the exhaust VANOS unit; sticking exhaust VANOS solenoid
- Diagnostic notes: Exhaust-side companion to 2A82 — same SIB, same diagnostic path. Tool32 MSD80 list phrases it as "outlet-Vanos variable cam control test, mechanics". N52/N54.
- Grade: [A] description; [B] causes
- Evidence: BMW SIB 11 02 08; Tool32 MSD80.prg fault list (bimmerforums archive)

## 2A7C
- Description: Intake VANOS solenoid fault
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: faulty or dirty intake VANOS solenoid; infrequent oil changes
- Diagnostic notes: A BMW technician (JustAnswer) notes the solenoids can be removed and cleaned as a first step; proper testing needs a BMW-specific scan tool. Solenoid electrical connectors can be swapped by mistake on reinstallation — verify routing.
- Grade: [C]
- Evidence: JustAnswer BMW technician Q&A (2011 328i 2A7C/2B3A case); bimmerforums VANOS thread (connector-swap caution)

## 2B3A
- Description: DMTL pump fault (diagnosis module for tank leakage)
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: failed DMTL pump (in left rear fender liner); wiring
- Diagnostic notes: EVAP leak-detection pump; common failure, ~1 hour replacement per the technician source. The N54 CAN DME list phrases it "DMTL diagnosis module tank leakage, system failure".
- Grade: [C]
- Evidence: JustAnswer BMW technician Q&A; N54 CAN DME code list (scribd transcription)

## 29CD / 29CE / 29CF / 29D0 / 29D1 / 29D2
- Description: Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: spark plug; ignition coil; injector; carbon buildup (N54 direct injection)
- Diagnostic notes: Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts.
- Grade: [C]
- Evidence: N54 CAN DME code list (scribd transcription)

## 29E0 / 29E1
- Description: Fuel Mixture Control 1 / 2
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: N54 CAN DME code list (scribd transcription)

## 29E2
- Description: Fuel injection rail — pressure sensor signal
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: high-pressure fuel rail sensor; wiring
- Diagnostic notes: N54 direct-injection high-pressure side.
- Grade: [C]
- Evidence: N54 CAN DME code list (scribd transcription)

## 2AAF
- Description: Fuel pump plausibility
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: low-pressure fuel pump delivery vs demand mismatch
- Diagnostic notes: N54; often accompanies HPFP issues.
- Grade: [C]
- Evidence: N54 CAN DME code list; Tool32 MSD80 list ("fuel pumpe, plausibility")

## 2A94 / 2A95
- Description: Crankshaft sensor — signal / synchronisation
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: crankshaft position sensor; wiring; trigger wheel damage
- Diagnostic notes: From the Tool32 MSD80 fault table.
- Grade: [B]
- Evidence: Tool32 MSD80.prg fault list (bimmerforums archive)

## 2A98 / 2A99
- Description: Crankshaft – inlet camshaft correlation / crankshaft – outlet camshaft correlation
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: timing chain stretch/jump; VANOS fault; sensor faults
- Diagnostic notes: Correlation codes point at mechanical timing rather than a single sensor.
- Grade: [B]
- Evidence: Tool32 MSD80.prg fault list (bimmerforums archive)

## 2A9A / 2A9B
- Description: Camshaft sensor inlet — signal / camshaft sensor outlet — signal
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: camshaft position sensor; wiring
- Diagnostic notes: See 2A94.
- Grade: [B]
- Evidence: Tool32 MSD80.prg fault list (bimmerforums archive)

## 3100
- Description: Boost pressure control — deactivation; boost pressure buildup prohibited
- Category: P (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: set as a consequential fault when VANOS or charge-air faults are present — not a root cause
- Diagnostic notes: INFORMATIONAL per BMW SIB 11 02 08 (listed as a secondary fault to 2A82/2A87, alongside 120408 "charge-air pressure control, cutout"). Do not chase as a turbo fault; fix the primary code first. N54.
- Grade: [B]
- Evidence: BMW SIB 11 02 08; N54 CAN DME code list; bimmerforums

### Body/chassis hex-code entries (representative)

## 9CB5
- Description: FRM: Battery exhausted (exhaustive-discharge protection: deactivation)
- Category: B (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: weak/dead battery; FRM load-shedding active
- Diagnostic notes: FRM shuts down lighting outputs to protect the battery — check battery/charging first; the lighting faults (A8AA/A8AC/A8B7…) are consequences.
- Grade: [C]
- Evidence: E90 owner thread with BMW-specific reader (bimmerforums); text is the reader's BMW code database

## A559
- Description: KOMBI: Power supply switched off — closed-circuit current cutoff relay
- Category: B (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: parasitic drain countermeasure; battery rundown
- Diagnostic notes: Set when the car cuts terminal 30g loads due to low battery.
- Grade: [C]
- Evidence: E90 owner thread (bimmerforums)

## 931D
- Description: KOMBI: Undervoltage or overvoltage
- Category: B (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: battery; alternator/charging system
- Diagnostic notes: Voltage faults cascade into many body codes — address charging system before chasing the others.
- Grade: [C]
- Evidence: E90 owner thread (bimmerforums)

## 93C3
- Description: MRS: Seat-occupancy detector, passenger
- Category: B (factory hex)
- Scope: manufacturer (BMW)
- Possible causes: passenger occupancy sensor mat; wiring under seat
- Diagnostic notes: SRS system — observe airbag safety precautions (battery disconnect, wait time) before probing.
- Grade: [C]
- Evidence: E90 owner thread (bimmerforums)

---

## 6. Module map notes (representative platforms)

### 6.1 E90 3-series (2005–2011; E91/E92/E93 share the architecture)

| Bus | Modules (from BMW junction-box overview + ST401 + community captures) |
|---|---|
| PT-CAN 500k | DME/DDE (engine), EGS (transmission), DSC, EKPS (fuel pump), GWS (gear selector); JBE as gateway [B] |
| K-CAN 100k | CAS, JBE/JBBF, FRM, KOMBI, IHKA/IHR, MRS (airbag), FZD, CCC/CIC + CID + CON, PDC, AHM, CA, DWA [B] |
| F-CAN 500k | DSC, SZL (steering column switch cluster), AL (active steering) [B] |
| MOST ring | CCC/CIC (gateway GW variants), CID, amplifier, TCU/ULF, SDARS, CD changer [B] |
| D-CAN (03/2007+) | diagnostic socket link [B] |
| LIN sub-buses | FRM→ mirrors/door switch blocks/headlight stepper motors; FZD→ rain/light sensor; IHKA→ flap motors/aux heater [B — junction-box overview] |

CAN-ID evidence (opendbc `bmw_e9x_e8x.dbc`, local clone — grade B): DME
sends 0xAA/0xA8/0xB4/0x175/0x1D0/0x332/0x337/0x464/0x492/0x592; DSC sends
0xC8/0xCE/0x19E/0x1A0/0x1A6/0x1A7/0x1B6/0x1B7; EGS 0xBA/0x1A2/0x3B2/0x3D1;
SZL 0xC4/0x1C4/0x1F4/0x2BE; CAS 0x130 (TerminalStatus); KOMBI 0x1B4/0x2F8/0x330;
IHKA 0x1B5/0x242/0x43F. Cross-checked against the bimmerforums E90 CAN
project's module-attributed captures, which agree on the same senders [B].

### 6.2 F30 3-series (2012–2018)

| Bus | Modules (BMW F30 Complete Vehicle training via bimmerscan FEM page) [B] |
|---|---|
| PT-CAN 500k | DME/DDE, EGS, ACSM, EKPS, GWS, KAFAS cameras, REM-A/REM-B |
| PT-CAN2 500k | engine/transmission redundancy |
| K-CAN (Body) 100k | SMFA/SMBF seat modules, AHM, IHKA, CON |
| K-CAN2 500k | REM, FZD, PMA, FLA, FEM-internal ZGW, HU-H (NBT) |
| FlexRay 10M | DSC, ICM, VDM, EPS, TRSVC |
| MOST | headunit-centered infotainment ring |
| Ethernet | HU-H, KOMBI, CBX-MEDIA, CBX-ECALL, amplifier |
| D-CAN | diagnostic socket |

Central gateway: **ZGM integrated in the FEM**; FEM also absorbs CAS, JBE,
and FRM functions of the E-series (F30 has no separate CAS/JBE/FRM in the
old sense) [B]. Immobilizer generation: CAS4 (E90: CAS2/CAS3/CAS3+ by year)
→ FEM/BDC on F30 [B — obdii365 CAS/FEM/BDC table].

### 6.3 G20 3-series (2019+)

- Central gateway and immobilizer: **BDC** (Body Domain Controller); BDC3
  from 2020 [B].
- CAN FD buses replace several CAN 2.0 buses; K-CAN4 ≈ F30 K-CAN2 role
  (IHKA, HU, TCB, ZBE) [C].
- Diagnostics: DoIP over Ethernet (OBD 3/11/12/13); ISTA dealer tool [B].
- **Full G20 bus/module table not verified in this pass** — BMW G-series
  training material was not found in public sources consulted [?].

---

## 7. Notable quirks

1. **E-series diagnostics are KWP2000-over-CAN, not UDS.** The 0x6F1 scheme
   with per-module IDs is the native tongue; UDS services only appear on
   later DMEs. An M2 tool must speak KWP2000 framing to be useful on an E90
   — plain 0x22 DID reads will get silence from most modules [B].
2. **D-CAN exists only from 03/2007.** Earlier E-series need K-line; the
   K+DCAN cable switch exists for exactly this split. Always check the
   build date before assuming 6/14 carries diagnostics [B].
3. **K-CAN is not on the DLC and may not be 11898-2.** 100 kbit/s and
   reported as fault-tolerant-style; verify transceiver compatibility on a
   bench tap before trusting a TJA1051 there [C].
4. **PT-CAN has a third wake-up wire.** It is not CAN signaling — do not
   connect it to a transceiver [A].
5. **Hex codes are the native format.** A generic OBD-II reader shows only
   the P-code translation (or nothing, for body codes). The 2A87-style hex
   code is what BMW tools, forums, and bulletins reference [B].
6. **3100 and C1201-style informational codes.** 3100 (boost deactivation)
   is a consequential fault to VANOS/charge-air faults per the BMW SIB —
   fix the primary code first [B].
7. **F-series gateway encapsulation.** Chassis ECUs (DSC/ICM/EPS) live on
   FlexRay; CAN-side diagnostic frames are encapsulated by the ZGW — a
   passive DLC sniffer never sees raw FlexRay traffic, and raw CAN IDs from
   E-series captures do not transfer [B/C].
8. **FEM absorbed CAS+JBE+FRM on F30.** E-series module-ID knowledge
   (0x40 CAS, 0x72 FRM) does not carry over; F-series addressing is
   gateway-mediated [B].
9. **G-series is a DoIP world.** A CAN-2.0-only tool's role on a G20 is
   limited to whatever the BDC exposes on classic-CAN DLC pins, if
   anything — verify per car [?].

---

## Sources consulted

- BMW ST401 "Body Electronics II — Bus Systems" training document (via
  archive.org BMWTechnicalTrainingDocuments) — PT-CAN/K-CAN/F-CAN/D-CAN
  speeds, PT-CAN 3-wire + wakeup, PT-CAN2, K-CAN2, termination, K-CAN2
  module list [A — BMW-authored training]
- BMW bus-system table (via share.qclt.com mirror of BMW training: Kbus,
  Dbus, byteflight, MOST, BSD, LIN, gateway list E38–E87) [B]
- BMW E90 "General Vehicle Electrical" manual (via manualslib) — JBE
  gateway functions, module responsibilities [B]
- BMW "System Overview of Junction Box Electronics E90/E91/E92/E93" (via
  scribd) — F-CAN/K-CAN/PT-CAN module lists, LIN sub-buses [B]
- BMW F30 Complete Vehicle training tables (via bimmerscan.com FEM page) —
  F-series bus table, ZGM-in-FEM, FlexRay/Ethernet/MOST/D-CAN roles [B]
- bimmerforums "E90 Can bus project" (multi-year thread) — 0x6F1/0x6XX
  diagnostic scheme, module-ID table, PT-CAN message attribution [B]
- bimmerforums E46 CAN project — K-CAN fault-tolerant note, K-CAN not on
  DLC [C]
- e90post "E9x KCAN 101" + "CANBUS errors" threads — JBE/DSC gateway
  behavior, K-CAN/F-CAN wiring [B/C]
- opendbc local clone `dbc/bmw_e9x_e8x.dbc` — 326 messages with sender
  attribution (DME/DSC/EGS/SZL/CAS/KOMBI/IHKA) [B]
- superwofy/E9X-M-CAN-Integration-Module (GitHub) — K-CAN 100k / K-CAN2
  500k confirmation, 0x6F1 usage [B]
- beemuu ENET cable pinout (GitHub) + team-bhp DIY ENET thread — OBD
  3/11/12/13 Ethernet pinout [B]
- BMW SIB 11 02 08 (via static.oemdtc.com NHTSA PDF) — 2A82/2A87
  descriptions, causes, consequential faults 3100/120408 [A]
- Tool32 MSD80.prg fault list (via bimmerforums archive) — 2A8x/2A9x/2AAx
  hex-code descriptions [B]
- N54 CAN DME code list (via scribd transcription) — 29CD–29F5, 2A87,
  2AAF, 2B3A, 3100 descriptions [C]
- meeknet.co.uk BMW fault-code PDF (1996–2003 DME/DDE/EML/GS) — P-code ↔
  BMW-FC mapping-table concept [B]
- "DTC P1xxx BMW" list (via scribd transcription) — P1083–P1138
  descriptions [C]
- obdeleven.com BMW fault-code blog — P1014 [C]
- JustAnswer BMW technician Q&A — 2A7C/2B3A causes and fixes (2011 328i)
  [C]
- bimmerforums E90 "Engine Code help" thread — 9CB5/A559/931D/93C3 body
  hex codes via BMW-specific reader [C]
- bimmerforums Z4 thread — P1318/P1339 definitions [C]
- f30.bimmerpost K-CAN4 thread — K-CAN/K-CAN2 speeds, NBT move, G30
  K-CAN4 equivalence [B/C]
- obdii365.com — BDC3 G-series case study; CAS/FEM/BDC generation table
  (2000–2019) [B]
- blog.autelshop.de — BDC03 model list (2020–2024 G-series) [B]
- nefariousmotorsports MG1 thread — no CAN tester comms outside SBOOT
  [C]
- bmwinsights.com — chassis-code list (E90/F30/G20 years), VIN decoder
  guide [B]
- AiM "BMW_OBDIICAN+BMWPT6" doc (via manuals.plus) — DLC 6/14 CAN-H/L
  [B]

## Open items / Coverage notes

- **DME/EGS/DSC module IDs for the 0x6F1 scheme** were not in the
  reproduced portion of the E90 CAN-project post; needed for DME
  conversations on E-series [?].
- **No verified BMW-specific UDS DID table** (sensor/live-data DIDs)
  found in public sources; BMW live data is job-oriented (EDIABAS/ISTA),
  not DID-oriented [?]. The `gediz/bmw-unified-db` GitHub project is an
  unvetted lead.
- **G20/G-series full bus/module table** not verified — BMW G-series
  training docs were not found publicly; CAN FD per-bus details are a gap
  (out of M2 scope regardless) [?].
- **F-series DLC 6/14 behavior**: D-CAN-to-ZGW confirmed [B], but what a
  passive sniffer sees there (gateway-filtered vs raw) is not pinned down
  [?].
- **K-CAN fault-tolerant physical layer**: single experimenter's report;
  TJA1051 compatibility on a K-CAN tap is unverified [?].
- **Pre-03/2007 E-series K-line diagnostics**: pinout and protocol details
  not verified in this pass [?].
- DTC coverage: P-code list centers on the DME P1083–P1138 block plus
  VANOS/DMTL/misfire hex codes; B1xxx/C1xxx/U1xxx BMW-specific ranges and
  the full hex dictionary (e.g. the complete Tool32 .prg tables per ECU)
  were not harvested [?].
- Diesel (DDE/M57/N47) and hybrid/EME-specific codes not covered [?].
- No seed/key algorithms, gateway bypasses, or immobilizer defeats were
  sought or reproduced, per the hard rules.
