# Mercedes-Benz — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.4.0 expansion, "new makes"
track). Every factual claim carries a quality grade: **A** = factory
documentation or verified capture · **B** = reputable community source
(opendbc, well-documented reverse-engineering, technician sources,
multi-source agreement) · **C** = single anecdotal report. Unverified items
are marked [?]. No seed/key algorithms, gateway-bypass procedures, or
immobilizer defeats are documented or invented here — legitimate paths only
(dealer XENTRY, paid online subscriptions). Research date: 2026-10-07.

Mercedes naming note: control units are referenced by their Daimler
designations where sources give them (e.g. N93 = central gateway, N73/EZS =
electronic ignition switch, N3/10 = ME-SFI engine control, N10/6 / N10/8 =
front/rear SAM). WMI prefixes for Mercedes-Benz/smart per community
VIN-dispatch work: WDB, WDD, WDF, WME [C — ieepirzy/hudson issue #6].

---

## 1. Bus architecture

### 1.1 The CAN generations (factory-documented)

A Daimler AG component description for the central gateway (GF54.21-P-4170GZ,
MODEL 164, © Daimler AG) states the vehicle has 3 CAN buses joined by the
central gateway control unit (N93): a **diagnostic CAN at 500 kbit/s**,
**CAN class B at 83.3 kbit/s**, and **CAN class C at 500 kbit/s** [A]. The
same document lists the gateway's tasks: gateway between CAN-B and CAN-C
(and CAN class D), global variant coding distribution, routing between the
B/C buses and the diagnostic CAN, diagnosis on both, and a data container
function [A].

Mercedes-Benz USA technician training for the W211 (© 2002, via scribd)
names the networks [A/B — factory training material]:
- **CAN B** — interior databus (body CAN)
- **CAN C** — engine databus (also called chassis CAN in this doc)
- **CAN D** — dedicated diagnostic databus: the diagnostic link between the
  Central Gateway Module (N93), the communications platform, and the
  Star Diagnosis / DAS tester
- **MOST** — digital fiber-optic databus for audio (replaces D2B)

The CGW (N93) is described as the primary gateway between CAN C and CAN B,
carrying system-diagnosis functions: it monitors CAN-B modules, produces
DTCs for CAN-B communication problems, and reports to DAS [A/B].

### 1.2 Bitrates and DLC presence

| Bus | Bitrate | Role | DLC presence |
|---|---|---|---|
| CAN-C (powertrain) | 500 kbps [A] | Engine, transmission, ESP, chassis | Yes — DLC pins 6/14 [B, Racelogic W212 CAN doc] |
| CAN-B (interior) | 83.3 kbps [A] | Body/comfort: SAMs, doors, seats, HVAC | Behind the gateway; not the DLC diagnostic bus [B] |
| CAN-D (diagnostic) | 500 kbps [A] | CGW ↔ tester link (W211 era) | Tester path, not raw bus traffic [A/B] |
| CAN-E | 500 kbps [B/C] | Cluster/infotainment link on W204/W212 era | Not on DLC [C — inferred from tap-behind-cluster practice] |
| CAN-F | not documented | Cluster bus on W221/W216 era (cluster pins carry CAN-F) | Not on DLC [C] |
| MOST | fiber optic | Audio/infotainment | Not a CAN target; not on DLC |
| FlexRay | not documented | W222 S-class driver-assistance/chassis per one model wiki | Out of M2 scope [C] |
| Ethernet / DoIP | 100BASE-TX | Diagnostics on W222/W205-era and newer | DLC pins 3/11 (Rx), 12/13 (Tx), pin 8 activation [B — ISO 13400 option 1] |

- CAN-B's odd 83.3 kbps rate is confirmed independently by an open-source
  W203/W211 CAN project whose author notes CAN-B "is NOT compatible with the
  8 MHz clock due to its odd bitrate of 83.3 Kbps" while CAN-C runs at
  500 kbps [B — github.com/c180kompressor/W203-canbus-extension].
- The DLC exposes the 500 kbps CAN on standard pins 6/14: a Racelogic
  vehicle-CAN database for the W212 states "all information is available via
  the OBD-II connector... CAN High on pin 6 and CAN low on pin 14" with the
  bus "configured at a baud rate of 500k" [B].
- CAN-E at 500 kbps: a W204 instrument-cluster bench project documents the
  cluster's CAN running at 500 kbps [C — YouTube], and aftermarket pinout
  tables place the W204/W212 cluster on CAN-E (pins 12/13) rather than
  CAN-B [B/C — ABRITUS72 pinouts via scribd/blog.obdii365]. Combined: CAN-E
  ≈ 500 kbps [B/C].
- CAN-F: the same pinout tables place W221/W216 clusters on CAN-F (pins
  1.12/1.13). Its role beyond the cluster is not documented in sources
  found [?].

### 1.3 Gateway evolution

- **W203/W209/W211/W219 era (~2000–2009):** CGW (N93) central gateway
  between CAN-C and CAN-B; version coding moved from the EIS (N73) into the
  CGW; system-diagnosis module functions folded into the CGW [A/B — W211
  training]. CAN distribution hubs X30/4, X30/5, X30/6, X30/7 in the
  footwells/rocker panels give physical tap points (community CAN projects
  use the X30/7 hub for CAN-B access) [B].
- **W204/W212/X204 era (~2007–2016):** community and aftermarket sources
  refer to the gateway as **ZGW** (also seen as ZGS in module-cloning
  listings) on the W204 [C]. CAN-E appears for the cluster link [B/C].
- **W222/W205 era (~2013–2021):** DoIP (Diagnostics over IP, ISO 13400)
  introduced for the COMAND/audio section — aftermarket tool vendors note
  "when we test mercedes new car like w222 w205, in Audio/Comand section
  you can find DoIP test page" and that DoIP-capable interfaces (XENTRY
  Connect C5, DoIP-reworked SD Connect C4) are needed there [C].
- **W206/W223/W214 era (2021+):** tool-vendor sources describe buses named
  **CAN_D, CAN_EXT, CAN_INT, CAN_PTI plus Ethernet/DoIP** as required for
  diagnosis [C]. A diagnostic-tool vendor states that from MY2021 (W223,
  then W206) "select Mercedes-Benz vehicles are equipped with a Secure
  Gateway... a firewall, preventing any communication performed via the OBD
  II connector without authentication" — blocking reads, live data, DTC
  reads and bidirectional functions until authenticated [C — iSCAN/iscantech
  video description]. Coding on these models additionally involves
  per-ECU certificate schemes (vendor term "ZenZefi") [C]. CAN FD on
  Mercedes buses was **not** verified in any source consulted [?].

### 1.4 Legacy connectors

- Pre-2000 Mercedes used a **38-pin round diagnostic connector** (Bosch
  KTS-era pinout tables document 38-pin layouts for W124/W140/W202/W210)
  [B — Robert Bosch GmbH pinout doc via scribd]. OBD-II 16-pin became the
  standard service connector on later models.
- Older (ME9.7-era) OBD-II DLCs carried multiple K-lines on pins
  1/7/9/11/12/13/15 alongside CAN on 6/14 per an aftermarket ECU-bench
  pinout table [C — blog.xhorsetool.com]. KWP2000-over-CAN superseded
  K-line for most modules by the W203 era.

---

## 2. Diagnostic access

### 2.1 Protocol and addressing

- **KWP2000 era (W203/W211, ~2000–2009):** diagnostics run over CAN using
  KWP2000. A community XENTRY-passthru capture on a W203 (Macchina M2
  under-the-dash + XENTRY) shows the tester setting a CAN filter for
  response ID 0x05FF with request ID 0x04E0 — i.e. diagnostic addressing
  in the **0x4xx/0x5xx CAN-ID range**, not 0x7xx [C — single community log,
  mercedes-hacking-docs Ch. 3].
- **UDS era (W204 onward):** Mercedes uses UDS (service 0x22 etc.) but
  "do not use standard UDS Arbitration IDs 0x7DF–0x7E7. In order to use
  UDS, you should set the IDs lower, such as 0x300" [C —
  mercedes-hacking-docs Ch. 1, community]. The UDS-era per-module address
  table is **not publicly documented**: XENTRY keeps it in proprietary
  CBF files, and the community project that parsed them lost its parser
  to a Daimler DMCA takedown [B — cxalem/scainner RESEARCH.md]. No free
  public source is expected to appear.
- **Wake-up:** many modules sleep with the car off. A per-model wake-up
  frame is required before the bus carries traffic. Crowd-sourced values
  (mercedes-hacking-docs Ch. 3) [B — community, multiple models]:

| Model | Wake-up CAN ID | DLC | Payload |
|---|---|---|---|
| W164 (M) / W240 (Maybach) / W251 (R) | 04E4 | 8 | 02 10 92 00 00 00 00 00 |
| W169 (A) / W203 (C) / W209 (CLK) / W211 (E) / W215 (CL) / W219 (CLS) / W245 (B) | 001C | 8 | 02 10 92 00 00 00 00 00 |
| W216 (CL) / W221 (S) | 0692 | 8 | 02 10 92 00 00 00 00 00 |

  (W204/W205/W212/W213 wake-up frames were not in the table — gap [?].)
  A W204 cluster bench project independently documents a wake-up frame of
  ID 0x001 with payload `04 00 00 00 00 00 00 00` for the cluster alone
  [C — YouTube].

### 2.2 The filtered OBD-II port

- The OBD-II port on Mercedes models is **filtered** (via the EIS/EZS or
  SAM/gateway module): it passes reads of CAN traffic from the vehicle
  networks, but **only diagnostic CAN IDs may be written** — "attempting
  to write a standard CAN ID to the car's CAN bus networks via the OBD-II
  port will be rejected" [B — mercedes-hacking-docs Ch. 1].
- The gateway **silently drops traffic for unrecognized diagnostic CAN
  IDs**: "A non-response on Mercedes may mean 'filtered', not 'module
  absent'" [B — scainner RESEARCH.md]. A discovery sweep must not conclude
  a module is absent from a silent reply.
- Practical consequence: passive logging at the DLC works after wake-up;
  active probing only works with correct (model-specific, mostly
  undocumented) diagnostic IDs; arbitrary frame injection from the DLC is
  rejected by the gateway.

### 2.3 XENTRY / DAS ecosystem (legitimate paths)

- **DAS** (Diagnosis Assistance System) served older models (roughly
  pre-2015); **XENTRY** is the current dealer diagnostic platform for
  fault reading/erasing, live data, adaptations, coding and programming
  [C — aftermarket tool-vendor video/docs].
- **Vediamo** and **DTS Monaco** are engineering-level tools for deep
  coding/programming [C].
- **Online SCN coding:** replacing a control unit requires SCN
  (Software Calibration Number) coding performed through XENTRY with an
  online connection to Mercedes servers — e.g. documented procedure for a
  W205 N3/10 (ME) control unit: XENTRY → Adaptations → Control unit
  update → Updating of SCN coding, with the online connection enabled
  [C — blog.vxdiagshop.com]. Legitimate paths: Mercedes dealer, or an
  independent shop holding an official XENTRY online account/subscription.
- **DoIP hardware:** SD Connect C4 (DoIP-reworked), XENTRY Connect C5, and
  XENTRY Diagnosis VCI C6 support DoIP; the C6 is the current interface
  for W206/W223-era vehicles [C — vendor listings].
- **Seed/key policy: no public Mercedes UDS 0x27 algorithm was found.
  None is invented or reproduced here.** Security-gated operations
  (immobilizer/key learning on DAS-3 systems, component protection) are
  dealer/XENTRY-online territory. Whether ordinary read DIDs need 0x27 on
  Mercedes is unknown — no source either way; treat NRC 0x33 as
  "skip this DID" [B — scainner].

### 2.4 What a DLC-connected CAN 2.0 tool can actually do

| Capability | Pre-2021 (W203–W213) | 2021+ (W206/W223) |
|---|---|---|
| Legislated OBD-II (J1979) on 6/14 | Yes [A — legislated] | Yes, where the secure gateway permits [C] |
| Passive CAN logging after wake-up | Yes — gateway passes reads [B] | Behind secure-gateway authentication [C] |
| UDS reads (0x22) | Only with correct model-specific diagnostic IDs, mostly undocumented [B/C] | Authentication-gated [C] |
| DTC clear / actuations / coding | Via gateway diagnostic IDs where known; SCN coding needs XENTRY online [C] | Authentication + certificates; legitimate path is dealer/XENTRY online [C] |
| Arbitrary frame injection | Rejected at the DLC by the gateway [B] | Rejected [B/C] |
| MOST / FlexRay / Ethernet-DoIP | No M2 hardware path — out of scope | Out of scope |

---

## 3. M2 hardware → Mercedes bus mapping

| Mercedes bus | Access point | M2 hardware path |
|---|---|---|
| CAN-C / diagnostic CAN (500k) | DLC 6/14 | CAN0 or CAN1 (TJA1051, due_can). Primary bus: legislated OBD-II + gateway-filtered diagnostics |
| CAN-B (83.3k) | Behind gateway: X30/x-hub tap in footwell/rocker | Second CAN controller (TJA1051 handles 83.3k). Interior/body traffic |
| CAN-E (500k) | Behind cluster (W204/W212) | Second CAN controller if tapped |
| K-line (older models) | DLC pins 7 etc. | K-line transceiver (TJA1027) |
| LIN sub-buses | At modules | LIN1/LIN2 (TJA1027) if tapped |
| MOST / FlexRay / Ethernet-DoIP | Fiber / dedicated pairs | **No M2 hardware support** — out of scope |
| CAN FD (if present on newest) | — | **No M2 hardware support** — TJA1051 is CAN 2.0 only; treat as out of scope |

Firmware notes for the M2's 7 modes:
- The M2's ELM/OBD2 modes work on DLC 6/14 for legislated diagnostics on
  any CAN-2.0 Mercedes. Extended UDS modes need the wake-up frame first
  and correct (largely undocumented) diagnostic CAN IDs; expect silent
  drops for wrong IDs and do not treat silence as module absence.
- MITM/bridge use at the DLC is neutered by the gateway's write filter —
  only diagnostic-ID frames pass. Direct-tap (behind the gateway) is the
  only path to raw bus traffic, and it bypasses the gateway's filtering
  entirely: standard safety posture applies.

---

## 4. UDS DID catalog

Mercedes-specific DID findings are thin — this is an honest gap, not an
omission. XENTRY's DID definitions live in proprietary CBF files; the one
community parser was DMCA'd by Daimler, and no public UDS-era
(W204-onward) DID table exists [B — scainner RESEARCH.md]. ISO-standard
identification DIDs (0xF180–0xF19E) are NOT duplicated here; only 0xF190
carries a Mercedes-specific note.

## 0xF190 — ECU (any UDS-era module)
- Name: VIN (ISO 14229-1 standard identification DID)
- Description: Vehicle Identification Number, 17 bytes ASCII. The single
  best brand-agnostic first probe on a newly discovered Mercedes ECU.
- Make: mercedes
- Size: 17 bytes
- Session: not documented
- Security: not documented (whether reads need 0x27 on Mercedes is unknown
  — no source either way [B])
- Grade: [B] for Mercedes support (independently confirmed present on
  Mercedes per scainner RESEARCH.md, which cites opendbc's uds.py table
  mirroring ISO 14229-1); [A] for the DID meaning (ISO standard)
- Evidence: cxalem/scainner packages/uds-map/RESEARCH.md — "F190 is the
  single best brand-agnostic first probe... confirmed present on PSA,
  Renault, VAG, BMW and Mercedes independently"

---

## 5. Manufacturer-specific DTCs

### 5.1 Reading Mercedes fault codes — two numbering schemes

Mercedes shows faults two ways, and sources must not be mixed without
care:
- **P/B/C/U codes** (SAE J2012 format) — used by generic tools and DAS
  printouts. Listed below.
- **Mercedes internal fault codes** — 4-character alphanumeric codes shown
  by XENTRY in full-system scans (e.g. a 2024 XENTRY scan of a WDC164
  ML-class shows `9100` "The Instrument Cluster No Longer Transmits Over
  The Engine CAN Databus. Status 'CAN Bus OFF'", `9101`/`9107`/`9108`/
  `9109`/`910D`/`910F` "Control Module [ESP/CGW/EZS/Airbag/ISM] Is Not
  Sending Any Data", `90BE`/`91C8`/`9137`/`9127` SAM output faults,
  `C300` "Event: CAN Bus OFF", `C361` "Event: Local Undervoltage At
  Circuit 30 (voltage < 9.5 V)", `C30E` "Event: Signal 'Vehicle Speed' On
  CAN Bus Is Not Present Or Is Faulty", each qualified Stored/Event)
  [B — scribd "Mercedes-Benz Diagnostic Fault Codes", real XENTRY scan
  report]. No public mapping table between these internal codes and the
  P/B/C/U codes was found — do not invent one [?].
- **UDS-format codes with failure-type byte** also appear on newer models
  (e.g. `P261F71` on a Sprinter — see below) [C].

### 5.2 P-codes

## P1000
- Description: Electronic gear selector module (N15/5) defective
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: faulty gear selector module (N15/5); wiring; CAN communication faults
- Diagnostic notes: Transmission/EGS family code. See also P1747/P1750/P1832/P1910/P1912.
- Grade: [B]
- Evidence: adsitco.com Mercedes OBD-II guide; scribd "OBD2 Error Codes Overview" agrees

## P1228
- Description: Unknown code (reported on 1997 C220 CDI)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Listed as "yet unknown" in community lists — do not act on without model-specific documentation.
- Grade: [C]
- Evidence: adsitco.com; scribd "OBD2 Error Codes Overview" (both transcribe as unknown)

## P1386
- Description: Knock control fault
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: faulty knock sensor(s); incorrect fuel octane; engine mechanical issues
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: adsitco.com Mercedes OBD-II guide (single detailed source)

## P1570
- Description: Intermittent no-start — immobilizer module
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: faulty immobilizer module; wiring; key/transponder issues
- Diagnostic notes: Immobilizer-adjacent code documented at DTC-description level only. No bypass material sought or reproduced.
- Grade: [B]
- Evidence: adsitco.com; scribd "Common Mercedes Fault Codes Explained" agrees

## P1664
- Description: Electronic heater booster fault
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Seen on a 2001 W203 CDI Autocom scan alongside P0703 (brake signal). Diesel models.
- Grade: [B]
- Evidence: Autocom CARS CDP+ scan report, 2001 W203 (mbworld.org attachment) — real scan

## P1747
- Description: Electronic gear selector module — defective interaction of CAN with control unit A1 (instrument cluster)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: CAN communication fault between EGS and cluster; wiring; module faults
- Diagnostic notes: EGS family — see P1000.
- Grade: [B]
- Evidence: scribd "OBD2 Error Codes Overview"; adsitco.com agrees

## P1750
- Description: Electronic gear selector module — very low control unit supply voltage
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: low system voltage; wiring; charging system
- Diagnostic notes: Check battery/charging first — low voltage causes cascading CAN faults on Mercedes (cf. C1010/C361).
- Grade: [B]
- Evidence: scribd "OBD2 Error Codes Overview"; adsitco.com agrees

## P1832
- Description: Electronic gear selector module — short in circuit N15/5 output stage
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: short in selector-module output circuit; module fault
- Diagnostic notes: EGS family — see P1000.
- Grade: [B]
- Evidence: scribd "OBD2 Error Codes Overview"; adsitco.com agrees

## P1910
- Description: Electronic gear selector module — control unit overvoltage
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: charging-system overvoltage; wiring
- Diagnostic notes: EGS family — see P1000.
- Grade: [B]
- Evidence: scribd "OBD2 Error Codes Overview"; adsitco.com agrees

## P1912
- Description: Electronic gear selector module — weak touch push-button voltage
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: EGS family — see P1000.
- Grade: [B]
- Evidence: scribd "OBD2 Error Codes Overview"; adsitco.com agrees

## P2000
- Description: NOx trap efficiency below threshold (Bank 1)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: degraded NOx storage catalyst; exhaust system faults
- Diagnostic notes: Diesel emissions. NOTE: on a 2001 W203 Autocom scan, P2000 appears with a different text ("Braking torque from the traction system over CAN bus; implausible") — meaning is model/era-dependent; confirm per model [B — real scan].
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"; conflict from Autocom W203 scan (mbworld.org)

## P2001
- Description: NOx trap efficiency below threshold (Bank 2)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: degraded NOx storage catalyst; exhaust system faults
- Diagnostic notes: Diesel emissions.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2003
- Description: Particulate trap efficiency below threshold (Bank 1)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: degraded DPF; exhaust system faults
- Diagnostic notes: Diesel emissions.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2004
- Description: Particulate trap efficiency below threshold (Bank 2)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: degraded DPF; exhaust system faults
- Diagnostic notes: Diesel emissions.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2031
- Description: Exhaust gas temperature sensor circuit (Bank 1 Sensor 2)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: EGT sensor; wiring
- Diagnostic notes: See P2032/P2033 for low/high variants.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2032
- Description: Exhaust gas temperature sensor circuit low (Bank 1 Sensor 2)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: EGT sensor; wiring short to ground
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2033
- Description: Exhaust gas temperature sensor circuit high (Bank 1 Sensor 2)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: EGT sensor; wiring short to positive/open
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2080
- Description: Exhaust gas temperature sensor circuit range/performance (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: EGT sensor; wiring
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2081
- Description: Exhaust gas temperature sensor circuit intermittent (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: EGT sensor; wiring/connector
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2100
- Description: Throttle actuator control motor circuit / open
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: throttle actuator; wiring
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2101
- Description: Throttle actuator control motor circuit range/performance
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: throttle actuator; wiring
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P2208
- Description: Transmission — speed of Y3/6n2 to Y3/6n3 excessive
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: transmission speed sensors; internal transmission fault
- Diagnostic notes: 722.x transmission speed-sensor plausibility.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"

## P261F71
- Description: Coolant circulation pump output malfunction — actuator blocked (Sprinter, OM651)
- Category: P
- Scope: manufacturer (Mercedes)
- Possible causes: coolant intrusion into vacuum system via water pump internal seal (documented field pattern on OM651)
- Diagnostic notes: UDS-format code (P261F + failure-type byte 0x71). Newer-model code format; do not expect on pre-UDS models.
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single detailed source)

### 5.3 B-codes

## B1000
- Description: HRA headlamp range adjustment — control unit supply voltage too low (undervoltage)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: low vehicle battery voltage; wiring to control unit; defective control unit
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: adsitco.com; a1-diagnostics.com; scribd "Common Mercedes Fault Codes Explained" agree

## B1004
- Description: LCP lower control panel — control unit does not match vehicle type
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: incorrect control unit installed (part-number mismatch)
- Diagnostic notes: Coding/variant mismatch — verify part number against VIN.
- Grade: [B]
- Evidence: adsitco.com; a1-diagnostics.com; scribd agree

## B1056
- Description: Automatic air conditioning — problem in CAN communication with control unit DCM-RL
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: CAN wiring/connections; defective DCM-RL
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: adsitco.com; a1-diagnostics.com; scribd agree

## B1128
- Description: Heater core temperature sensor (B10/1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC (automatic air conditioning) sensor family — see B1226–B1235. NOTE: one community list prints "B1128 Heater core temperature (B10/1)" while another prints "B1229 Heater core temperature (B10/1)" — transcription conflict, flagged [?].
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1201
- Description: Electric seat adjustment front left — hall sensor front height (M27m3)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: faulty hall sensor; wiring
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: adsitco.com; a1-diagnostics.com; scribd agree

## B1213
- Description: Seat memory installed — exterior right rearview mirror voltage faulty
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: mirror actuator/wiring
- Diagnostic notes: One community list prints B1213 as LEFT mirror and B1214 as RIGHT; another prints both as right — transcription conflict, flagged [?].
- Grade: [B] description; [C] left/right attribution
- Evidence: adsitco.com; a1-diagnostics.com; scribd agree on the code family

## B1214
- Description: Seat memory installed — exterior right rearview mirror voltage faulty
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: mirror actuator/wiring
- Diagnostic notes: See B1213 left/right conflict note.
- Grade: [B] description; [C] left/right attribution
- Evidence: adsitco.com; a1-diagnostics.com; scribd agree on the code family

## B1226
- Description: In-car temperature sensor (B10/4)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1227
- Description: Outside temperature indicator temperature sensor
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1229
- Description: Heater core temperature sensor (B10/1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See B1128 transcription conflict.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1230
- Description: Evaporator temperature sensor (B10/6)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1231
- Description: ECT sensor (B11/4)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1232
- Description: Refrigerant pressure sensor (B12)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1233
- Description: Refrigerant temperature sensor (B12/1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1234
- Description: Sun sensor (B32)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1235
- Description: Emissions sensor (B31)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC sensor family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1241
- Description: Refrigerant fill
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC — refrigerant charge issue.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1246
- Description: PTS Parktronic — A42b1 (left outer sensor, front bumper)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Parktronic sensor fault.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1310
- Description: Left/window airbag sensor defective
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: SRS component — follow standard airbag safety practice (battery disconnect, wait before probing).
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1315
- Description: Front passenger child seat recognition problem
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Occupant-classification system.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1416
- Description: Coolant circulation pump (M13)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family — see B1417–B1425.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1417
- Description: Duovalve (Y21y1), left
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1418
- Description: Duovalve (Y21y2), right
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1419
- Description: Electromagnetic clutch (A9k1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1420
- Description: Idle speed increase
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1421
- Description: Pulse module (N05)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1422
- Description: Series interface (K1) connection to instrument cluster (A1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1423
- Description: Switchover valve block (Y11)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1424
- Description: Activated charcoal filter actuator (A32m2) open
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1425
- Description: Activated charcoal filter actuator (A32m2) closed
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: AAC actuator family.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1432
- Description: Non-USA DTC
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Market-variant code — not applicable to US vehicles.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1459
- Description: Series interface (K2) connection to instrument cluster (A1)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1462
- Description: Wide open throttle (WOT) position signal — diesel engines
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Diesel models.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1476
- Description: Airbag malfunction indicator and warning lamp defective
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: SRS telltale circuit.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1481
- Description: HRA — part E2m1 (right headlamp range adjustment motor) short to ground
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See B1489/B1492 for open/short-to-positive variants.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1489
- Description: HRA — part E2m1 (right headlamp range adjustment motor) open or short to positive
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See B1481.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1492
- Description: HRA — part E1m1 (left headlamp range adjustment motor) short to positive
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See B1481.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## B1703
- Description: Intermittent no-start in AAM — immobilizer module
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: all-activity module (AAM) / immobilizer circuit
- Diagnostic notes: Immobilizer-adjacent code documented at DTC-description level only.
- Grade: [B]
- Evidence: scribd "Common Mercedes Fault Codes Explained"; yumpu 1996-models DTC doc agrees

## B1729
- Description: PSE pneumatic system door lock control module (A37)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Pneumatic central locking.
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single source)

## B1736
- Description: Navigation system's CD player — check general CD / CD data block
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Infotainment.
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single source)

## B1768
- Description: Faulty open data flap limit switch (front flap)
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single source)

## B1773
- Description: HRA — zero position programming not yet carried out or not possible
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: programming incomplete; mechanical fault
- Diagnostic notes: Requires headlamp-range zero-position programming (XENTRY).
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single source)

## B1850
- Description: Electric seat adjustment front right — CAN communication interrupted with DCM
- Category: B
- Scope: manufacturer (Mercedes)
- Possible causes: CAN wiring; door control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "Common Mercedes Fault Codes Explained" (single source)

### 5.4 C-codes (DAS-documented set first)

The following are transcribed from Daimler DAS (Diagnosis Assistance
System, © 1999) fault-code printouts [A — factory diagnostic texts].
Where community transcriptions disagree, the conflict is flagged inline.

## C1000
- Description: Control unit N47-5 (ESP and BAS control module) is defective
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented (one DAS print variant phrases C1000 as "Check power supply of component N47-5" — flagged variant)
- Diagnostic notes: CONFLICT — a community code list labels C1000 "Traction System Control Module" [C]; the DAS text is preferred.
- Grade: [A]
- Evidence: Daimler DAS printouts via benzbits.com (ESPCodes.pdf) and mbworld.org (DTC-ESP pdf) — both © 1999 Daimler AG

## C1001–C1013 (range)
- Description: Control unit N47-5 (ESP and BAS control module) is defective (each code in range)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model.
- Grade: [A]
- Evidence: Daimler DAS printouts via benzbits.com and mbworld.org

## C1014
- Description: Y10 (SPS solenoid valve) — electrical fault
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Speed-sensitive power steering solenoid.
- Grade: [A]
- Evidence: Daimler DAS printout via benzbits.com

## C1018
- Description: Short circuit in the voltage supply of sensors B34 (ESP brake pressure sensor) and A7/7b1 (BAS diaphragm travel sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Daimler DAS printout via benzbits.com

## C1020
- Description: Fault or defect in CAN communication
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — community list labels C1020 "CAN Communication Fault" (consistent) [C].
- Grade: [A]
- Evidence: Daimler DAS printouts via benzbits.com and mbworld.org

## C1035
- Description: Signal from component N49 (steering angle sensor) is faulty
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Daimler DAS printouts via benzbits.com and mbworld.org

## C1037
- Description: Fault in CAN communication with component B24/15 (rotary speed and lateral acceleration sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Daimler DAS printout via mbworld.org

## C1038
- Description: Engine control module not identified, or incorrect control module
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Module-identification/coding mismatch.
- Grade: [A]
- Evidence: Daimler DAS printouts via benzbits.com and mbworld.org

## C1040
- Description: Fault in CAN communication with component B24/15 (rotary speed and lateral acceleration sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See C1037.
- Grade: [A]
- Evidence: Daimler DAS printout via mbworld.org

## C1046
- Description: Fault or defect in CAN communication
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: See C1020.
- Grade: [A]
- Evidence: Daimler DAS printout via benzbits.com

## C1047
- Description: Vehicle version — coding is faulty
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Variant-coding mismatch — recode with XENTRY (SCN path for module replacement).
- Grade: [A]
- Evidence: Daimler DAS printout via benzbits.com

## C1140
- Description: Steering angle sensor not initialized
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: sensor replacement / battery disconnect without initialization
- Diagnostic notes: Seen as Intermittent on a real 2001 W203 scan. Initialize the steering angle sensor, then clear.
- Grade: [B]
- Evidence: Autocom scan report, 2001 W203 (mbworld.org) — real scan

## C1141
- Description: Brake pressure sensor B34 (brake master cylinder)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Seen on a 2000 ML320 with dealer + independent scans (owner report).
- Grade: [C]
- Evidence: justanswer.com ML320 thread (single owner report)

## C1200
- Description: Brake light switch (open/shorted/implausible)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: faulty brake light switch; wiring
- Diagnostic notes: Seen as Intermittent on a real 2001 W203 scan. A classic cause of ESP/BAS warnings.
- Grade: [B]
- Evidence: Autocom scan report, 2001 W203 (mbworld.org); community lists agree

## C1202
- Description: BAS release switch — plausibility
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Seen as Intermittent on a real 2001 W203 scan.
- Grade: [B]
- Evidence: Autocom scan report, 2001 W203 (mbworld.org) — real scan

## C1314
- Description: Voltage supply solenoid valves
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Seen on a 2000 ML320 with dealer + independent scans (owner report).
- Grade: [C]
- Evidence: justanswer.com ML320 thread (single owner report)

## C1529
- Description: Precharging of accumulator is not available
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: SBC (Sensotronic Brake Control) system. Seen as Intermittent on a real 2001 W203 scan.
- Grade: [B]
- Evidence: Autocom scan report, 2001 W203 (mbworld.org) — real scan

### 5.5 C-codes (community-transcribed set)

Single-source community transcriptions [C throughout]. Where they conflict
with the DAS texts above, DAS is preferred (flagged per code where known).

## C1010
- Description: Battery voltage low
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: weak battery; charging system
- Diagnostic notes: CONFLICT with DAS (see C1001–C1013 range). Low voltage causes cascading CAN faults — always check supply voltage first.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1011
- Description: ASR/ETS/ESP circuit open or shorted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT with DAS (see C1001–C1013 range).
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1012
- Description: Battery voltage high
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: charging-system overvoltage
- Diagnostic notes: CONFLICT with DAS (see C1001–C1013 range). An ML320 owner report independently shows "C1012 - ESP and BAS Control Module Is Faulty" from dealer/indie scans [C] — a third variant; meaning is model-dependent, verify per model.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview"; variant from justanswer.com ML320 thread

## C1021
- Description: CAN communication with EA/CC/ISC control module interrupted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1024
- Description: CAN communication with engine control module interrupted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1025
- Description: CAN communication — BAS communication with ESP control unit faulty
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1100
- Description: Left front axle VSS circuit fault
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: wheel speed sensor; wiring; tone ring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1101
- Description: Right front axle VSS circuit fault
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: wheel speed sensor; wiring; tone ring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1102
- Description: ETS/ASR, ABS left axle VSS circuit fault
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: wheel speed sensor; wiring; tone ring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1103
- Description: Right rear axle VSS circuit fault
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: wheel speed sensor; wiring; tone ring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1121
- Description: AIRmatic — fault in component B24/3 (acceleration sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — one community list prints B22/3 (level sensor) for C1121 [C]; component attribution flagged [?].
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1122
- Description: AIRmatic — fault in component B24/4 (acceleration sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — one list prints B22/4 (level sensor) for C1122 [C]; flagged [?].
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1123
- Description: AIRmatic — fault in component B24/6 (acceleration sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — one list prints B22/6 (level sensor) for C1123 [C]; flagged [?].
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1132
- Description: AIRmatic — fault in component B22/8 (level sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1133
- Description: AIRmatic — fault in component B22/9 (level sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1135
- Description: AIRmatic — fault in component B22/3 (level sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1142
- Description: ABS lateral acceleration sensor open/shorted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: sensor; wiring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1144
- Description: AIRmatic — fault in component B7 (pressure sensor)
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1185
- Description: Faulty BAS diaphragm travel sensor unit
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1300
- Description: Left front axle solenoid valve (Hold) (A7/3y6) open/shorted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: solenoid; wiring
- Diagnostic notes: An ML320 owner report independently shows "C1300 - Solenoid Valve A7/3YC Hold Pressure" [C] — consistent.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview"; justanswer.com ML320 thread agrees

## C1303
- Description: Right front axle solenoid valve (Hold) open/shorted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: solenoid; wiring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1311
- Description: Switchover solenoid valve (Release) open/shorted
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: solenoid; wiring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1312
- Description: Master cylinder switchover valve
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1401
- Description: High pressure return pump circuit open/shorted; will not shut off
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: pump; relay; wiring
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1501
- Description: SPS P-valve
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Speed-sensitive steering valve.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1512
- Description: Brakes overheated
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

## C1600
- Description: Temperature after engine is turned off
- Category: C
- Scope: manufacturer (Mercedes)
- Possible causes: not documented
- Diagnostic notes: Heat-soak informational code.
- Grade: [C]
- Evidence: scribd "OBD2 Error Codes Overview" (single transcription)

### 5.6 U-codes

## U0020
- Description: Low speed CAN communication bus B
- Category: U
- Scope: manufacturer (Mercedes)
- Possible causes: CAN-B wiring/module fault
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: yumpu.com 1996-models DTC doc (single transcription)

- **U1xxx manufacturer codes: none verified in this pass** [?]. Generic
  U0xxx communication codes (U0100 lost comm with ECM, U0121 lost comm
  with ABS, etc.) are SAE-defined and already in the database — not
  duplicated here.

---

## 6. Module map notes (platforms)

### 6.1 W204 C-class (2007–2014) — KWP2000/early-UDS transition

- Buses: CAN-C (500k powertrain), CAN-B (83.3k interior), CAN-E (cluster
  link, ≈500k), MOST for audio [B/C — see §1].
- Gateway: community/aftermarket sources call it **ZGW** on the W204
  (naming mixed with CGW in threads) [C].
- Key modules (designations from community pinout/scan sources [B/C]):
  EZS (electronic ignition switch, immobilizer master), ME (engine
  control, e.g. ME9.7 with CAN-H/L on ECU pins 2.41/2.54), ETC (722.9
  transmission), ESP, IC (instrument cluster on CAN-E, connector pins
  12/13), front SAM, rear SAM.
- Diagnostic wake-up frames for the W204 were not in the crowd-sourced
  table [?]; the cluster alone wakes on ID 0x001 (`04 00 00 00 00 00 00
  00`) [C].

### 6.2 W205 C-class (2014–2021) — UDS + DoIP

- UDS-era addressing (undocumented publicly — see §2.1) [B].
- DoIP over Ethernet used for the COMAND/audio section; DoIP-capable
  interface required there [C — aftermarket tool vendors].
- Online SCN coding documented for the N3/10 (MED40/M274) engine control
  unit via XENTRY [C].
- Detailed bus/module topology not verified in this pass [?].

### 6.3 W213 E-class (2016–2023) — UDS + DoIP

- A Daimler overall-network (GVN) component overview (© Mercedes-Benz AG,
  2023, via mbworld.org) lists control units including: N3/10 ME-SFI /
  N3/9 CDI engine controls, N10/6 front SAM, N10/8 rear SAM, N22/1 climate
  control, N88 tire pressure monitor, N112/9 HERMES (telematics),
  N118 fuel pump control, N118/5 AdBlue control, N83/5 DC/DC converter
  (48V models), N97/N3/43 suspension controls, N5/110 weight sensing
  [B — factory component overview].
- Tool-vendor sources describe diagnosis as requiring **CAN_D, CAN_EXT,
  CAN_INT, CAN_PTI with Ethernet/DoIP** on W213-facelift and newer
  [C]. Pre-facelift W213 remains CAN-2.0 accessible at the DLC for
  legislated diagnostics.

---

## 7. Notable quirks

1. **The DLC is a filtered window, not a raw bus tap.** Reads pass;
   writes are restricted to diagnostic CAN IDs; unknown diagnostic IDs
   are silently dropped. Non-response ≠ module absent — this is the
   single most important behavioral fact for any M2 diagnostic work on
   Mercedes [B].
2. **Wake-up is mandatory for passive logging.** The buses sleep with the
   car off; nothing appears until the model-specific wake-up frame is
   sent (or the car is woken by other means, e.g. opening a door) [B].
3. **No 0x7DF–0x7E7.** Mercedes does not use the standard OBD/UDS
   functional/physical ID block; UDS probing must use lower IDs (0x300
   suggested by community) — but the real per-module table is
   undocumented [C/B].
4. **Two fault-code schemes coexist.** XENTRY shows 4-character internal
   codes (9100, C300, …); generic tools show P/B/C/U. No public mapping
   between them was found — record both when available, never convert
   [B].
5. **DAS vs community C-code conflicts.** Factory DAS texts and community
   transcriptions disagree on several C10xx codes (C1000–C1013 range,
   C1121–C1123 component attributions). Trust DAS per model; flag the
   rest [A/C].
6. **Low voltage cascades.** Mercedes ESP/ABS/SAM systems throw
   communication and sensor codes (C1010/C1241-family, C361 internal)
   on weak batteries — load-test the battery before chasing CAN codes
   [B/C].
7. **Odometer lives in multiple modules.** EZS and instrument cluster
   (and gateway) cross-check mileage; this is why aftermarket mileage
   tools need CAN filters/blockers on W204-era cars [C — aftermarket
   threads]. Recorded for context; no procedures given.
8. **2021+ secure gateway.** W223/W206 (and newer) authenticate OBD-II
   access; unauthenticated reads, DTC clears and bidirectional functions
   are blocked at the firewall. A CAN-2.0 tool without authentication
   gets nothing — flag these models as auth-gated [C].
9. **38-pin round connector** on pre-2000 models — a different physical
   adapter is needed for anything before OBD-II [B].
10. **opendbc has no Mercedes DBCs** of note for this database's purposes
    (checked implicitly — no Mercedes signal content surfaced in any
    source; the local opendbc clone was not re-checked in this pass) [?].

---

## Sources consulted

- Daimler AG, GF54.21-P-4170GZ "Central gateway control unit, component
  description" (MODEL 164, © Daimler AG, via mbworld.org attachment) —
  CAN-B 83.3k / CAN-C 500k / diagnostic CAN 500k, N93 tasks [A]
- Mercedes-Benz USA, "W211 Networking" technician training (© 2002,
  via scribd.com/document/320709008) — CAN B/C/D, MOST, CGW N93 system
  diagnosis, X30 connectors [A/B]
- Racelogic, "W212 E-Class CAN Bus Overview" (via
  scribd.com/document/550421944) — DLC 6/14, 500k [B]
- rnd-ash/mercedes-hacking-docs, Chapters 1 & 3 (GitHub) — filtered OBD
  port, non-standard UDS IDs, wake-up table, M2UTD XENTRY capture
  (0x04E0/0x05FF) [B]
- c180kompressor/W203-canbus-extension (GitHub) — CAN-B 83.3k vs CAN-C
  500k, X30/7 tap [B]
- cxalem/scainner packages/uds-map/RESEARCH.md (GitHub) — F190 on
  Mercedes, missing UDS-era DID table, DMCA note, silent-drop behavior,
  unknown 0x27 requirement [B]
- ABRITUS72 "Mercedes ECU and Dashboard Pinouts" (via
  scribd.com/doc/122816089 and blog.obdii365.com) — cluster CAN
  assignment by platform (CAN-B vs CAN-E vs CAN-F) [B/C]
- autopi-io/documentation DoIP setup guide (GitHub) + Vector VN8810
  accessories manual (via manuals.plus) — DoIP OBD pins 3/11, 12/13,
  pin 8 activation, ISO 13400 option 1 [B]
- obdii365.com, vxdiagshop.com, vxdas.com, bestsuppliers.com,
  autoexplain.com, labelmyproducts.com (aftermarket tool vendors) — DoIP
  on W222/W205, XENTRY Connect C5/C6, SCN online procedure, W223/W206
  CAN_D/EXT/INT/PTI + ZenZefi [C]
- iscantech video description (YouTube) — MY2021+ secure gateway
  firewall behavior [C]
- Daimler DAS fault-code printouts (© 1999): benzbits.com ESPCodes.pdf
  and mbworld.org DTC-ESP attachment — C1000–C1047 texts [A]
- Autocom CARS CDP+ scan report, 2001 W203 (mbworld.org attachment) —
  P1664, P0703, C1200, C1140, C1529, C1202, B110D real-scan data [B]
- scribd.com/document/718269216 "Mercedes-Benz Diagnostic Fault Codes"
  — XENTRY full-system scan (WDC164): internal 91xx/C3xx codes [B]
- adsitco.com "Mercedes OBD-II Trouble Codes" guide; a1-diagnostics.com
  B-code pages; scribd.com/document/657299246 "Common Mercedes Fault
  Codes Explained"; scribd.com/document/881681039 "OBD2 Error Codes
  Overview" — P/B/C community lists [B where agreeing / C]
- justanswer.com ML320 ABS/ETS thread — C1300/C1200/C1012/C1314/C1140/
  C1141 owner report with dealer+indie scans [C]
- yumpu.com 1996-models DTC doc — B1703, U0020 [C]
- blog.xhorsetool.com VVDI ME9.7 pinout — older-model DLC K-lines [C]
- scribd.com/doc/315789501 "Mercedes Diagnostic Connector PDF" (Robert
  Bosch GmbH) — 38-pin round connector [B]
- ieepirzy/hudson issue #6 (GitHub) — WMI WDB/WDD/WDF/WME, MB UDS 0x22
  note [C]
- mbworld.org W213 GVN overview (© Mercedes-Benz AG, 2023,
  gf00.19-p-9997fg) — W213 control-unit designations [B]
- Daimler DAS © 1999 and Daimler component docs are quoted only as
  short factual fault-code phrases; longer prose is paraphrased.

## Open items / Coverage notes

- **UDS-era (W204+) per-module diagnostic CAN IDs: not found.** The only
  honest entry is the addressing behavior (non-standard IDs, silent
  drop). This is the biggest functional gap for M2 UDS-mode work [?].
- **Manufacturer-specific DID catalog: effectively empty.** Beyond
  0xF190, no Mercedes DID with name/size/decode was verified. Filling
  this needs a legitimate XENTRY CBF processed through a CBF parser —
  no free public source is expected (DMCA history) [?].
- **W204/W205/W212/W213 wake-up frames:** not in the crowd-sourced
  table [?].
- **Mercedes U1xxx codes:** none verified [?].
- **CAN FD on Mercedes:** not verified on any model in sources
  consulted; W222 documented with FlexRay (single model-wiki source).
  Newest models (W206/W223) are Ethernet/DoIP-centric with named CAN
  buses CAN_D/EXT/INT/PTI whose bitrates are unverified [?].
- **CAN-F role** beyond the W221/W216 cluster link: unverified [?].
- **W205 detailed topology:** not verified [?].
- **B-code coverage:** AAC sensor/actuator block (B1226–B1492) is single-
  transcription; SRS B1xxx range beyond B1310/B1315/B1476 not verified [?].
- **C-code conflicts** (DAS vs community on C1000–C1013, C1121–C1123,
  C1213/C1214 left/right) are flagged inline, not resolved [?].
- **P-code coverage** centers on EGS (P1000/P1747/P1750/P1832/P1910/
  P1912), diesel emissions (P2000–P2101), and a handful of others;
  CDI-specific P-codes (e.g. full OM651/OM642 ranges) not covered [?].
- No seed/key, gateway-bypass, or immobilizer-defeat material was
  sought or reproduced, per project hard rules.
