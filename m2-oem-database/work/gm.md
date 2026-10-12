# GM in-vehicle networks & diagnostic access

Research for the M2 OEM vehicle database. Every factual claim carries a quality
grade: **A** = factory documentation or verified capture, **B** = reputable
community source (opendbc, well-documented reverse-engineering, industry tool
vendor docs), **C** = single anecdotal report. Conflicts between sources are
reported, not silently resolved.

Research date: 2026-10-06.

## 1. Bus architecture: GMLAN

GMLAN (GM Local Area Network) is GM's family of CAN-based serial buses that
replaced the Class 2 (J1850 VPW) network. Per ACDelco TechConnect — GM's own
technician publication **[A]** — GMLAN supports three buses:

| Bus | Bitrate | Physical layer | DLC pins |
|---|---|---|---|
| High-Speed (HS) GMLAN | 500 kbps | dual-wire twisted pair | 6 (CAN-H), 14 (CAN-L) |
| Mid-Speed (MS) GMLAN | 95.2 kbps | dual-wire | 3 (MS-H), 11 (MS-L) |
| Low-Speed / Single-Wire (SW) GMLAN | 33.33 kbps | single wire | 1 |

- **HS pins 6/14 [A]**: confirmed by the GM service diagnostic procedure
  "Scan Tool Does Not Communicate With High Speed GMLAN Device" (DLC terminals
  6 and 14 = GMLAN high/low circuits) and the Intrepid Control Systems neoVI
  OBD-II pinout (2002) **[B]**.
- **SW pin 1 [B]**: Intrepid neoVI pinout labels pin 1 "GMLAN SW CAN Line";
  corroborated by a documented owner capture ("vendor specific single wire CAN
  bus on pin 1", 33.3 kbps) **[B]**.
- **MS pins 3/11 [B]**: Intrepid neoVI pinout labels pin 3 "GMLAN MS CAN H"
  and pin 11 "GMLAN MS CAN L". Mid-speed is used for infotainment (display,
  navigation) where response-time demands are higher **[B]** (GM Enhanced
  Diagnostic spec excerpt hosted on pcmhacking.net).
- **Mid-speed bitrate conflict**: ACDelco says 95.2 kbps **[A]**; the GM
  Enhanced Diagnostic spec excerpt says "approximately 95.2 kbps or 125 kbps"
  **[B]**. Both reported; treat MS bitrate as model-dependent.
- **HS termination [B]**: 120-ohm resistors at each physical end of the bus
  (60 ohms measured across DLC pins 6/14 with the vehicle off is the standard
  health check — widely documented; graded B as no factory doc was pulled for
  this specific claim).
- **Multiple HS buses [B/C]**: the GM spec excerpt names HS bus variants —
  Primary HS, Chassis Expansion, Powertrain Expansion **[B]**. A documented
  2010 Camaro has *two* HS 500k buses at the DLC (pins 6/14 **and** pins
  12/13) plus the LS bus on pin 1 **[C]** (single forum report). Note the
  conflict: the 2002 Intrepid pinout labels DLC pins 12/13 "LSFT H/L"
  (discretionary) **[B]** — pin 12/13 usage varies by model and year.
- **Gateway [A/B]**: the Body Control Module (BCM) sits on both the HS and
  LS buses and translates messages between them (ACDelco TechConnect).
- **Network management [B]**: GMLAN uses a "Node Management Strategy" built
  around Virtual Systems (groups of modules collaborating on one vehicle
  function). Unlike Class 2, there are no periodic State-of-Health messages;
  a module with nothing to do for ~8 seconds returns to a low-power state
  (trade-press technical article, Fender Bender).

### SWCAN physical layer detail

- Single-wire CAN per GM spec **GMW3089** (referenced by NXP as
  GMW3089v2.4) **[A]** (NXP MC33897 product page).
- Bitrates: 33.33 kbps normal mode, 83.33 kbps high-speed mode **[A]** (NXP;
  corroborated by NI forum post **[B]**). The high-speed SWCAN mode is used
  for programming/flashing **[B]**.
- High-voltage wake-up: a defined wake-up voltage level on the bus
  reactivates the transceiver's INH output, which re-enables the module's
  external voltage regulator — i.e., a sleeping SWCAN node is woken by a
  high-voltage pulse on the single wire **[A]** (NXP MC33897; EE Times).
  Worst-case sleep current 60 µA **[A]**.

## 2. Legacy: Class 2 / J1850 VPW

- GM's pre-GMLAN network was "Class 2" = **SAE J1850 VPW at 10.4 kbps on DLC
  pin 2 [A]** (SAE/OBD-II standard pin assignment; VPW uses pin 2 only —
  pin 10 is the J1850 PWM negative leg, used by Ford, not GM **[B]**).
- **Model-year split**: GMLAN phase-in began with **2004 model-year vehicles
  [B]** (trade press). One protocols survey claims GM was "nearly all CAN by
  2005" **[C]** (unverified uploader), but owner reports show 2005 models
  (Colorado, Yukon 5.3L) still on J1850 VPW **[C]**, and GMT800 trucks carried
  VPW late. Treat the transition as **gradual, roughly 2004–2007,
  model-dependent [B]**, complete by the **2008 US federal CAN mandate for
  emissions diagnostics [A]**.
- Rule of thumb for the database: 1996–2003 GM ≈ VPW on pin 2 **[B]**;
  2004–2007 = check per model (mixed) **[C]**; 2008+ = GMLAN **[A]**.

## 3. Diagnostic access

### Identifier scheme (11-bit USDT)

Per the GM Enhanced Diagnostic Test Mode spec excerpt (pcmhacking.net)
**[B]**:

| CAN ID | Use |
|---|---|
| $7DF | functional (broadcast) request from tester |
| $7E0–$7E7 | physical request, tester → ECU #1–#8 |
| $7E8–$7EF | physical response, ECU #1–#8 → tester |

- Documented working example **[B]**: ELM327 `AT SH 00 07 E0` /
  `AT CRA 00 00 07 E8`, service $1A $90 (read VIN) answered by the PCM —
  confirming **ECM = ECU #1 → 0x7E0 request / 0x7E8 response** on HS GMLAN.
  TCM is commonly ECU #2 (0x7E1/0x7E9) **[C]** (community convention; the
  spec excerpt only defines the numbering scheme, not the ECU assignment).
- GMLAN diagnostics follow **UDS / ISO 14229** ("GMLAN Enhanced Diagnostic
  Test Mode Specification") **[B]**.

### Tool ecosystem

- **Tech2** handheld: GM's tool from 1992 through ~2009+ **[B]**; the **CANdi
  (CAN Diagnostic Interface) module** was added in 2004 so the Tech2 could
  talk to CAN vehicles **[B/C]** (aftermarket vendor blog).
- **Tech2Win** (PC emulation): ~1992–2013 **[B]**.
- **MDI / MDI 2 + GDS2** (Global Diagnostic System 2): Global-A platform
  (~2010+) through current; **Techline Connect** portal hosts GDS2 (diag),
  SPS2 (programming), and Tech2Win **[B]** (techroute66 guide).
- **SPS2** (Service Programming System): module reflash with VIN-matched
  calibrations from GM servers — online subscription only **[B]**.

### Gateways and security

- The **BCM is the gateway** between HS GMLAN and other serial data
  (LS/SWCAN, legacy Class 2) **[A/B]** — scan-tool access to non-HS modules
  routes through it.
- **Seed/key (UDS $27)**: GM uses controller-specific $27 security-access
  algorithms; the generic $27 challenge/response mechanism is described in
  SAE J2186 terms on the HP Tuners forum **[B]** (mechanism description
  only). Community-reverse-engineered implementations exist for specific
  **older** PCMs (E38/E67 discussed on pcmhacking.net) **[B]** — algorithms
  are **not reproduced here**. Tuner-locked PCMs do not follow the GM
  formula; brute-forcing (2-byte key space, ~10 s lockout between attempts)
  is discussed as a fallback **[C]**. For Global-B and newer: keys are
  server-issued, not client-computable **[C]** (small research repo).
- **Database policy**: no factory-published seed/key algorithm exists. For
  any modern GM controller: **no public algorithm — dealer tool (SPS2/GDS2)
  required.**

## 4. M2 hardware mapping to GM buses

M2 OBD-II connector facts are VERIFIED in the knowledge pack v1.4.0
(`constraints.yaml` → `obd2_connector`); GM bus assignments are graded from
this research:

| GM bus | DLC pins | Bitrate | M2 hardware | M2 net |
|---|---|---|---|---|
| GMLAN High-Speed | 6 / 14 **[A]** | 500 kbps | CAN0 via TJA1051 (due_can) | HSC_BUS |
| GMLAN Mid-Speed | 3 / 11 **[B]** | 95.2 kbps | CAN1 via TJA1051 (due_can) | MSC_BUS |
| GMLAN Single-Wire | 1 **[B]** | 33.33 / 83.33 kbps | MCP2515 + TH8056 SWCAN circuit | SWC_BUS |
| Class 2 (legacy) | 2 **[A]** | 10.4 kbps VPW | J1850 discrete circuit (VPW mode) | J1850+_BUS |

- The M2's CAN1 transceiver is wired to DLC pins 3/11 — exactly the GMLAN
  mid-speed pins — so **no extra hardware is needed for MS-CAN** (within the
  95.2/125 kbps conflict noted above; due_can can be set to either rate).
- SWCAN init on the M2: `setupSW(33)` normal / `setupSW(83)` high-speed,
  `mode(3)` normal / `mode(2)` HV-wake / `mode(0)` sleep (pack v1.4.0 software
  audit, VERIFIED in Macchina's Single-Wire-CAN-mcp2515 source).
- J1850 on GM is **VPW-only**: drive M2 pin 50 (J1850_PWM_VPW) LOW and use
  pin 52 (VPW RX) / pin 53 (J1850+ TX). The M2's J1850- (DLC pin 10) has no
  GM use.
- DLC pins 12/13 on the M2 are test points (TP3/TP4), **not** a second HS
  bus — a second HS GMLAN bus (where present, e.g. 2010 Camaro **[C]**) is
  not reachable with stock M2 hardware.
- LIN ch1 is on M2 DLC pin 7 (K-line); not a GM primary bus.

## 5. Notable quirks

1. **SWCAN HV wake-up is required to talk to sleeping modules [A]**: a
   sleeping GMLAN SW node ignores normal 33.3k traffic until it sees the
   high-voltage wake-up. M2 procedure: `mode(2)` (HV wake) before expecting
   responses, then `mode(3)` for normal communication.
2. **SWCAN high-speed (83.33k) mode exists for flashing [B]**: the
   transceiver — not just the CAN controller bitrate — must be switched.
   On the M2 this is `setupSW(83)` + `mode(1)` per the SWCAN library audit.
3. **No SOH chatter on GMLAN [B]**: unlike Class 2's ~2 s State-of-Health
   broadcasts, pure-GMLAN buses go quiet when idle; a silent bus does not
   mean a dead bus. Modules sleep after ~8 s of inactivity.
4. **0x7E0/0x7E8 is the ECM's physical diagnostic pair [B]**; functional
   $7DF reaches all emission-related ECUs. Enhanced (non-emissions)
   diagnostics may reuse these IDs per the spec excerpt **[B]**.
5. **Class 2 and GMLAN coexist during 2004–2007 [B]**: transition-era
   vehicles may have VPW on pin 2 *and* GMLAN on 6/14 — check the DLC pins
   present before assuming the protocol.
6. **BCM gateway dependency [A/B]**: scan-tool traffic to LS/SWCAN modules
   passes through the BCM; a BCM fault can look like a whole-bus failure.
7. **60 Ω across DLC 6/14 (key off) [B]** is the quick HS-bus health check;
   ~120 Ω suggests one terminator missing/open, 0 Ω a short.

## Sources consulted

- ACDelco TechConnect, "GM Can Communication" (via scribd) — GM technician
  publication: three GMLAN buses, bitrates, BCM gateway role.
- Intrepid Control Systems neoVI OBD-II/J1962 pinout (2002, via scribd) —
  DLC pin assignments incl. SW/MS/HS GMLAN and J1850.
- GM "Scan Tool Does Not Communicate With High Speed GMLAN Device" service
  procedure (via scribd) — HS pins 6/14, module list.
- NXP MC33897 single-wire CAN transceiver product page — GMW3089v2.4,
  33.33/83.33 kbps, high-voltage wake-up, 60 µA sleep.
- EE Times / EDN (2005): Freescale MC33897 launch — HV wake-up mechanism.
- GM Enhanced Diagnostic Test Mode spec excerpt + 11-bit USDT ID table
  (pcmhacking.net forum attachment) — $7DF/$7E0–$7E7/$7E8–$7EF, HS/MS/LS
  bus definitions.
- Fender Bender, "Scope & Scan: GMLAN Functional Diagnostics" — 2004
  introduction, node management, virtual systems, Tech2 functional diags.
- pcmhacking.net threads — E38/E67 seed/key discussion (algorithms not
  reproduced), ELM327 0x7E0/0x7E8 VIN-read capture.
- HP Tuners forum — $27 security-access mechanism description (SAE J2186).
- techroute66.com — GM SPS2/GDS2/Tech2Win/Techline Connect tool matrix.
- obdii365 blog — Tech2/CANdi history (vendor blog, lower weight).
- opendbc forks' docs/CARS.md — GM coverage: Chevrolet Bolt EV/EUV,
  Equinox, Malibu, Silverado 1500, Suburban, Trailblazer; Cadillac
  XT5/XT4/XT6/CT6/ATS/Escalade; Buick Enclave/LaCrosse/Regal (ADAS-bus
  DBCs for openpilot, not full vehicle catalogs).
- RealDash forum — 2010 Camaro 3-bus DLC report (pins 6/14, 12/13, 1).
- gmtnation.com / tahoeyukonforum.com — Class 2/VPW year anecdotes,
  Tech2 usage notes.
- Knowledge pack v1.4.0 (`~/workspace/m2-superb-knowledge/`) — M2 OBD-II
  connector mapping, SWCAN/J1850/due_can software facts (VERIFIED).

## Open items / gaps for the database

- Per-model bus tables (which exact models/years have MS-CAN at the DLC,
  second HS bus on 12/13) — needs model-level research or captures.
- MS-CAN bitrate per model (95.2 vs 125 kbps conflict unresolved).
- GM-specific UDS service support matrix (which services beyond legislated
  OBD-II respond on 0x7E0).
- opendbc GM DBC harvest: pull the actual DBC files and grade message
  coverage per vehicle (next step).
