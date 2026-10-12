# Toyota / Lexus — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, well-documented
reverse-engineering, trade/technician sources) · **C** = single anecdotal
report. Unverified items are marked [?]. Research date: 2026-10-06.

---

## 1. Bus architecture

### 1.1 CAN buses

Toyota's multiplex training material (Toyota Motor Sales USA technician
document, Aug 2014) lists CAN at **500 kbps HS / 250 kbps MS** (max 1 Mbps)
[B]. A Toyota repair-manual CAN communication system description states
"high speed communication at 500 kbps and 250 kbps is possible" [B].

| Bus | Bitrate | DLC3 pins | Role |
|---|---|---|---|
| CAN V Bus (HS) | 500 kbps | 6 (CANH) / 14 (CANL) | Powertrain/chassis: ECM, HV ECU, battery ECU, skid control, EPS, airbag, gateway ECU, DLC3 [B] |
| MS-CAN | 250 kbps | not on DLC (interior) | Body/comfort traffic behind the gateway ECU [B for existence/rate; C for DLC absence — inferred from gateway architecture] |

- DLC3 pin 6/14 assignment and the 54–69 Ω termination check (ignition off)
  are from Toyota service information (© 2012 Toyota, via technician
  handbook) [A].
- The CAN V Bus member list (ECM, center airbag sensor, skid control ECU,
  engine stop/start ECU, certification/smart-key ECU, steering angle sensor,
  radio/display, A/C amplifier, main body ECU, power steering ECU,
  combination meter, network gateway ECU, DLC3) is from a Toyota repair
  manual CAN communication section [B].
- A 2004 Prius repair manual (RM1075U) shows the early single-bus layout:
  one 500 kbps CAN joining battery ECU, skid control ECU, EPS ECU, ECM,
  HV ECU, gateway ECU, steering angle sensor, yaw-rate/deceleration sensor,
  and DLC3, with 120 Ω terminators at the bus ends [B].
- Community confirmation: Prius Gen 2 uses ISO 15765-4 (CAN 11-bit/500k) on
  the DLC [C — PriusChat owner report, consistent with the manuals].

### 1.2 Gateway architecture

- Toyota uses a dedicated **gateway ECU** that performs protocol conversion
  between CAN, BEAN, and AVC-LAN — "data arrangement must be converted before
  transferring data to [a different] communication bus... called gateway
  function, which is performed by the gateway ECU" (2004 Prius New Car
  Features manual RM1075U) [B].
- The DLC3 exposes the HS CAN V Bus (6/14) plus the SIL K-line (pin 7).
  The 250 kbps MS-CAN and the body buses (BEAN/AVC-LAN/LIN) sit behind the
  gateway ECU and are **not** on the DLC — a scan tool reaches them only
  through gateway routing [B for the DLC pinout; C for the MS-CAN routing —
  inferred from the gateway-function architecture; no source was found
  showing MS-CAN pins at the DLC].
- Practical consequence: a passive M2 logger on DLC 6/14 sees the HS bus
  traffic only. Body-module traffic (BEAN/AVC-LAN) requires tapping behind
  the gateway [B/C — inferred from the gateway architecture].

### 1.3 Other multiplex protocols (Toyota training doc, Aug 2014) [B]

| Protocol | Speed | Wire | Use |
|---|---|---|---|
| BEAN (Body Electronics Area Network, Toyota original) | 10 kbps | AV single wire | Body electrical |
| AVC-LAN (Toyota original) | 17.8 kbps (AVC-LAN plus: 7.5 Mbps) | twisted pair | Audio/visual |
| LIN | 9.6 kbps (max 20) | AV single wire | Body sub-buses |
| SIL | 10 kbps | single wire | Non-CAN diagnostics (K-line, DLC pin 7) |
| MOST | 50 Mbps | shielded twisted pair | Infotainment |

- BEAN terminal names: MPX1/2, MPX+/- [B].
- BEAN electrical: single-wire voltage drive, 0–10 V nominal, idle at 0 V
  (Toyota 673 technician handbook) [B]. Protocol: CSMA/CD with bitwise
  arbitration, 8-bit CRC, 25-bit header, 1–11 byte data, NRZ with bit
  stuffing (community reverse-engineering, toymods/eevblog) [C].

### 1.4 Model-year evolution

- **Early 2000s:** BEAN for body electronics + ISO 9141 K-line (SIL, pin 7)
  for diagnostics. 2004 Prius is the transition snapshot: CAN for
  powertrain/hybrid control, but chassis DTCs (EPS, brake) still came out
  over the ISO 9141 serial line to the DLC3 SIL terminal [B — 2004 Prius
  repair manual].
- **2004+:** CAN rolls out across the lineup (Prius first for hybrid
  control) [B].
- **2008:** US federal mandate makes CAN (ISO 15765) compulsory for
  emissions diagnostics on all new vehicles [A — regulatory fact].
- Rule of thumb: 2008+ Toyota/Lexus ≈ CAN on DLC 6/14 + K-line SIL on
  pin 7 for non-CAN modules; pre-2004 ≈ K-line/BEAN era [B].

---

## 2. Legacy protocols

### 2.1 K-line / SIL (ISO 9141-2, ISO 14230 KWP2000)

- DLC3 **pin 7 (SIL)**, optional L-line pin 15; 10.4 kbps UART 8-N-1,
  idles HIGH, active driven LOW, 0–12 V [B — protocol standard + Toyota
  DLC3 terminal table].
- Toyota's DLC3 terminal check: pin 7 (SIL) to pin 5 (SG) shows "pulse
  generation" during transmission [A — Toyota service info].
- Used for non-CAN modules well into the CAN era: a 2008 Lexus GX owner
  report notes ECM/ABS on CAN while "most other modules (TPMS, air
  suspension etc) communicate via the KLINE protocol... physical different
  pins on the diagnostics port" [C].
- M2 implication: the TJA1027 K-line transceiver covers this directly.

### 2.2 BEAN (Body Electronics Area Network)

- Toyota-proprietary single-wire body bus, 10 kbps, 0–10 V [B].
- Used on early-2000s models and "still used somewhat today" per community
  RE (2003 MR2 Spyder A/C and cluster gauge control ran over BEAN) [C].
- **M2 implication:** no M2 hardware speaks BEAN — it is a proprietary
  protocol on a 0–10 V single wire, not J1850, not K-line, not LIN. Treat
  as out of reach for stock M2 firmware [B/C].

### 2.3 AVC-LAN

- Toyota-proprietary audio/visual bus, 17.8 kbps twisted-pair (AVC-LAN plus:
  7.5 Mbps); star topology centered on a master ECU (multi-display or audio
  head unit) [B — 2004 Prius manual]. Not a diagnostic target; listed for
  completeness.

### 2.4 Diagnostic jumper pins (Toyota-specific DLC3)

- DLC3 carries Toyota-proprietary pins beyond the OBD-II standard: pin 9
  (TAC), pin 12 (TS), pin 13 (TC) on 2016–2019 Tacoma; 2020+ dropped pins
  4/9/12, keeping 5/6/7/13/14/16 [C — TacomaWorld owner pinout survey].
- Classic Toyota behavior: jumpering **TC (13) to CG (4)** puts the vehicle
  in diagnostic mode (blink-code DTC output, zero-point calibrations)
  [C — long-standing Toyota practice, owner-reported on the 2020 Tacoma].

---

## 3. Diagnostic access

### 3.1 Protocol and addressing

- CAN-era Toyota uses **UDS-flavored diagnostics over ISO-TP** on the HS
  bus, with the **+8 response offset**: request 0x7E0 → response 0x7E8
  [B — community RE: "I query an ECU with 07E0 03 22 20 06, answer 07E8 05
  62 20 06 04 B0"].
- Hybrid-system ECUs have their own diagnostic IDs on the same HS bus
  (Prius community CAN-identification table) [B/C — well-documented
  community project, single-forum source]:
  - Engine ECM: request **0x7E0**, response **0x7E8**
  - HV ECU (power management control): request **0x7E2**, response **0x7EA**
  - HV Battery ECU: request **0x7E3**, response **0x7EB**
- Note: the same community doc shows Toyota hybrids using service **0x13**
  for DTC reads (vs. standard UDS 0x19) — treat as model-specific
  behavior, not a general Toyota rule [C].
- Standard emissions OBD-II (SAE J1979 modes 0x01–0x0A) on 6/14 works with
  any generic tool [A — legislated].

### 3.2 Techstream ecosystem

- **Techstream** is Toyota/Lexus's official dealer diagnostic software:
  full-system DTC read/clear, live data, Active Tests, Utility functions
  (calibrations, zero-point resets), coding/adaptation [B — Toyota TSBs and
  training material describe these functions].
- Interfaces: MongoosePro Toyota, Tactrix OpenPort, VCX Nano (plus clones
  of varying quality — a Lexus GX owner found knock-off Mongoose cables
  broke K-line while genuine Tactrix worked) [C].
- DTCs for the CAN communication system itself (U0073, U0100, U0123…)
  are read via Techstream/GTS through the DLC3 [B — Toyota repair manual].

### 3.3 Gateway restrictions

- No Stellantis-style authentication firewall was found on Toyota's DLC.
  The gateway ECU routes/bridges; it does not cryptographically block
  diagnostic writes [C — absence of evidence; no source describes a Toyota
  SGW equivalent].
- Practical limit is topological, not cryptographic: interior/body buses
  are not on the DLC, so diagnostics for those modules go through gateway
  routing with whatever latency/filtering the gateway applies [C —
  inferred].

### 3.4 Seed/key policy

- **No public Toyota seed/key (UDS 0x27) algorithm was found. None is
  invented or reproduced here.**
- What is publicly documented (Toyota TSB T-SB-0043-14, "Immobilizer and
  Smart Key Reset") [B]: Techstream generates a **Seed Number**; the
  technician submits it to **TIS (Toyota's server)** with management
  approval, and TIS returns a one-time **Pass-Code**. Each attempt
  generates a new seed and a new pass-code. The algorithm is server-side.
- 2018+ models add a further security layer for key programming: options
  are a NASTF LSID vehicle-security subscription (2-day ≈ $65, yearly
  ≈ $1,295) or dealer service [C — aftermarket tool-vendor blogs].
- For M2 firmware: security-gated operations (immobilizer, key
  programming) are dealer/TIS territory. Read-only diagnostics and
  standard UDS services are unaffected.

---

## 4. M2 hardware → Toyota bus mapping

| Toyota bus | DLC3 pins | M2 hardware path |
|---|---|---|
| HS CAN V Bus (500k) | 6 / 14 | CAN0 or CAN1 (TJA1051, due_can). Primary diagnostic + logging bus |
| MS-CAN (250k) | not on DLC | Second CAN controller **if tapped behind the gateway** (interior harness) |
| K-line / SIL (10.4k) | 7 | K-line transceiver (TJA1027). Non-CAN modules (TPMS, air suspension on some models) |
| LIN sub-buses (9.6k) | not on DLC | LIN1/LIN2 (TJA1027) if tapped at the module |
| BEAN (10k, 0–10 V) | not on DLC | **No M2 hardware support** — proprietary protocol |
| AVC-LAN / MOST | not on DLC | Not diagnostic targets |

---

## 5. Notable quirks

1. **The DLC3 is HS-bus-only for CAN.** Unlike Ford's HS/MS pin split,
   Toyota puts a single 500 kbps CAN on 6/14 at the DLC; the 250 kbps
   MS-CAN lives behind the gateway ECU. One M2 CAN controller normally
   suffices at the DLC — the second is for direct-tap work [B/C].
2. **Hybrid ECUs answer on their own IDs.** 0x7E2/0x7EA (HV ECU) and
   0x7E3/0x7EB (HV battery) — a generic OBD-II scanner talking only to
   0x7E0 will never see hybrid DTCs. This is why "Prius-aware" scanners
   exist [B/C].
3. **60 Ω-class check is 54–69 Ω on Toyota.** Toyota's spec is 54–69 Ω
   across DLC 6/14 (ignition off, settled); below 54 Ω = short, 69+ Ω =
   open [A — Toyota service info].
4. **K-line survived deep into the CAN era.** Non-CAN modules (TPMS, air
   suspension) on a 2008 Lexus still used pin-7 K-line — always check pin 7
   before assuming a module is on CAN [C].
5. **TC/CG jumper (13–4).** Toyota's proprietary diagnostic-mode trigger
   survives on the DLC3; useful for blink-code DTC reads without any tool
   [C].
6. **DLC3 pinout changed ~2020** (Tacoma: dropped pins 4/9/12). Aftermarket
   procedures referencing TS (12) or TAC (9) don't apply to 2020+ [C].
7. **opendbc Toyota coverage** (local clone, grade B): toyota_2017_ref_pt,
   toyota_adas, toyota_iQ_2009_can, toyota_prius_2010_pt, toyota_radar_dsu_tssp,
   toyota_tss2_adas — ADAS/powertrain subset, not full-vehicle.

---

## Sources consulted

- Toyota Motor Sales USA, "Multiplex Diagnosis" technician training doc
  (Aug 2014, via oemdtc/NHTSA) — CAN/LIN/AVC-LAN/MOST/BEAN/SIL speeds,
  wires, terminal names [B]
- Toyota 2004 Prius New Car Features manual RM1075U (via priuschat) —
  CAN/BEAN/AVC-LAN comparison table, gateway ECU function [B]
- Toyota 2004 Prius repair material (via share.qclt.com) — CAN member list,
  500 kbps, SIL for chassis DTCs, 120 Ω terminators, DLC3 diagnosis [B]
- Toyota repair manual CAN communication system (via zatonevkredit.ru) —
  500/250 kbps, CAN V Bus member list incl. DLC3 and gateway ECU [B]
- Toyota Prius repair manual RM1076E excerpts (via toyotamanuals.gitlab.io)
  — DLC3 6/14 checks, gateway ECU in CAN topology [B]
- Toyota service info "CHECK DLC3" (© 2012 Toyota, via scribd) — DLC3
  terminal table: SIL pulse on pin 7, 54–69 Ω across 6/14 [A]
- Toyota T-SB-0043-14 Rev2 (via priuschat) — immobilizer/smart-key reset:
  seed number + TIS pass-code flow [B]
- PriusChat community CAN-identification table — 0x7E0/0x7E2/0x7E3
  diagnostic IDs and hybrid service 0x13 usage [B/C]
- eevblog/toymods community RE — BEAN frame format (25-bit header, 8-bit
  CRC, 10 kbps, NRZ+bit stuffing) [C]
- TacomaWorld threads — DLC3 pin surveys (2016–2019 vs 2020), K-line vs
  CAN module split on 2008 GX [C]
- ih8mud, nefariousmotorsports — Techstream cable notes, 07E0→07E8 UDS
  example [C]
- vxdiagshop / obdii365 blogs — 2018+ key-programming security, NASTF
  LSID pricing [C]
- comma.ai opendbc (local clone) — Toyota DBC file list [B]

## Open items

- Whether any Toyota/Lexus model exposes MS-CAN (250k) pins at the DLC3
  (none found; assumed interior-only) [?]
- Per-model gateway part numbers and routing tables [?]
- Toyota-specific UDS DID (0x22) catalog per ECU family [?]
- Lexus-specific deviations from Toyota bus architecture, if any [?]
