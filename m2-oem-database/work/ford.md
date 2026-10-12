# Ford — in-vehicle networks and diagnostic access

Research for the M2 OEM vehicle database. Covers Ford / Lincoln / Mercury
(CGEA-era through CAN-FD transition). Every factual claim carries a quality
grade: **A** = factory documentation or verified capture, **B** = reputable
community source (opendbc, FORScan docs/forum, documented reverse-engineering),
**C** = single anecdotal report or vendor marketing copy.

Marcus context: FORScan user; M2 has dual HSCAN (TJA1051), SWCAN (TH8056),
J1850 VPW/PWM discrete interface, dual LIN (TJA1027), 12VIO.

---

## 1. Bus architecture

### HS-CAN (High-Speed CAN)
- **OBD-II pins 6 (CAN-H) / 14 (CAN-L)** [B — matches ISO 15765-4 standard
  pinout; confirmed by every Ford adapter source].
- **500 kbps** [B — consistent across all sources; scribd Ford compatibility
  list shows "CAN 11bit (500kb)" for CAN-era Fords].
- Carries powertrain: PCM, TCM, ABS, EPAS/EHPAS [B — merlinmb/esp32_odbii_hs_ms
  README documents a Ford Focus 2008 reading both buses; lists PCM/TCM/ABS on
  HS-CAN].
- On the OBD-II connector this is the *legislated* emissions bus
  (ISO 15765-4), so any generic OBD-II tool sees it [A — SAE J1979/ISO 15031
  requirement; generic-scan-tool behavior].

### MS-CAN (Medium-Speed CAN)
- **OBD-II pins 3 (CAN-H) / 11 (CAN-L)** — Ford-proprietary pins, dead on
  non-Ford vehicles [B — stated identically by FORScan forum adapter table,
  multiple ELM327-vendor pages, and the ESP32 Focus project].
- **125 kbps** [B — consistent across community sources].
- Carries body/comfort: GEM, door modules (DDM/PDM), instrument cluster (IC),
  EATC climate, RCM airbag, KVM keyless, PAM parking aid [B —
  merlinmb/esp32_odbii_hs_ms module table for Focus MK2].
- Present on "many Ford and Mazda models approximately since 2003–2004"
  [B — repeated verbatim across ELM327-vendor and FORScan sources; the
  earliest documented dual-bus car is the Focus MK2/C170 (2005–2008)
  (grade B for the platform claim, C for the exact "2003–2004" start].
- Stock ELM327 cannot reach it (only wired to 6/14); Ford-specific adapters
  add a physical HS/MS toggle switch or electronic switching [B — FORScan
  forum adapter table; FORScan prompts the user to flip the switch when it
  expects MS-CAN modules (C — slideshare tutorial)].
- One community glossary claims MS-CAN runs "125–500 kbps depending on
  chassis" [C — blueovallabs/ford-pscm-re glossary; conflicts with the
  otherwise-unanimous 125 kbps; treat 125 kbps as standard, faster variants
  as unverified].

### HS-CAN2 (second high-speed bus, newer models)
- Exists on newer platforms; reported module list: FDSM, ABS, RCM, PSCM,
  SCCM, GWM, IPMA [C — kanbkam adapter listing; single vendor source].
- The Body Control Module (BdyCM) bridges HS-CAN and MS-CAN [B —
  blueovallabs/ford-pscm-re glossary: "BdyCM — lights, doors, gateway.
  Bridges HS-CAN and MS-CAN"].

### Gateway Module (GWM)
- Newer Fords have a dedicated Gateway Module that "forwards messages
  between various CAN buses, provides OBD-II port diagnostic bus" [B —
  openpilot Ford wiki, Make-Specific Terms].
- FORScan module list for 2011–2023 Explorer shows GWM at diagnostic ID
  **0x726** [B — community FORScan Explorer spreadsheet (scribd)].
- Practical consequence: on gateway-equipped vehicles the OBD-II port does
  not expose raw HS/MS traffic directly; diagnostic requests are routed by
  the gateway [B — inferred from the GWM's documented role; FORScan works
  through it transparently].

### CAN FD (2021+ select models)
- BlueCruise / Co-Pilot360 Assist 2.0 platform vehicles use CAN FD:
  F-150 2021–23, F-150 Lightning 2022–23, Mustang Mach-E 2021–23,
  Escape 2023–24, Expedition 2022–24, Navigator 2022–24, Nautilus 2024
  [B — openpilot Ford wiki supported-vehicle table; opendbc `values.py`
  flags these exact platforms `FordFlags.CANFD` (verified in local opendbc
  clone)].
- This is why 2021+ F-150 requires an OBDLink EX / MX+ class adapter
  rather than a basic switched ELM327 [B — FORScan community tutorial;
  f150lightningforum reports of MX+ not recognizing a 2021 F-150 until
  FORScan added support].
- **M2 impact: the M2's TJA1051 transceivers are CAN 2.0 only — the M2
  cannot participate in a CAN-FD bus at all** (hardware fact from the
  knowledge pack; the vehicle consequence is INFERRED but solid).

### opendbc coverage (message catalogs)
Verified in the local opendbc clone (`work/opendbc/opendbc/dbc/`):
- `ford_cgea1_2_ptcan_2011.dbc` — 143 messages (CGEA 1.2 powertrain) [B]
- `ford_cgea1_2_bodycan_2011.dbc` — body CAN [B]
- `ford_fusion_2018_pt.dbc` — 14 messages incl. EPAS_INFO (0x130),
  Steering_Wheel_Data, Yaw_Data, Accel_Data, WheelSpeed, Doors,
  Lane_Keep_Assist_* [B]
- `ford_fusion_2018_adas.dbc` — ADAS bus [B]
- `ford_lincoln_base_pt.dbc` — 368 messages; this is the DBC opendbc maps
  to `Bus.pt` for all current Ford platforms (Bronco Sport, Escape Mk4,
  Explorer Mk6, Focus Mk4, Maverick Mk1, plus the CANFD platforms) [B —
  verified in `opendbc/car/ford/values.py` in the local clone]
- `FORD_CADS.dbc` / `FORD_CADS_64.dbc` — Ford CADS (older driver-assist) [B]

---

## 2. Legacy: Ford SCP (J1850 PWM)

- Ford's pre-CAN corporate protocol is **SCP (Standard Corporate Protocol)**,
  a J1850 **PWM** (41.6 kbps, differential, pins 2/10) implementation [B —
  AutoEnginuity ScanTool documentation; SAE J1850 PWM = "standard of the
  Ford Motor Company" per multiple OBD-II references].
- Ford SCP **requires In-Frame Response (IFR)** bytes; GM's VPW does not use
  IFRs [B — Fordmods BAE 5030 Ford training material].
- Transition timeline (US models):
  - 1996–2001: J1850-PWM only [C — scribd Ford OBD-2 compatibility list]
  - 2002–2006: mixed — J1850-PWM *or* CAN depending on model [C — same list]
  - After 2006: CAN [C — same list]
  - AutoEnginuity (commercial scan-tool maker): "J1850 PWM is the Interface
    Type to use for Fords older than 2004" [B]
  - F-150 specifically: 2003 = PWM J1850; 2004 (4.6L) = CAN 11-bit 500 kbps
    [C — scribd list; single source, treat as approximate]
  - US federal mandate made CAN (ISO 15765) compulsory for all vehicles
    sold from 2008-01-01, so no US Ford newer than MY2008 uses SCP [A —
    regulatory fact, widely cited]
- SCP OBD-II pins: **pin 2 (Bus+) / pin 10 (Bus−)** [B — SAE J1850 PWM
  pinout, consistent across sources].
- Note: some 2004-era Fords also show a **K-line on pin 7** at the DLC
  (troubleshooting reports of K-line shorts on 2004 F-150) [C — JustAnswer
  thread; unclear whether this is a secondary diagnostic line or
  misdiagnosis; do not rely on it].

---

## 3. Diagnostic access

### Protocol and addressing
- CAN-era Fords use **UDS (ISO 14229) over ISO-TP (ISO 15765-2)** on the CAN
  buses [B — FORScan capability set; openpilot glossary defines both terms
  for Ford context].
- Physical addressing uses the **+8 response offset**: request `0x7E0` →
  response `0x7E8` [B — canair VEHICLE-PROTOCOLS.md lists Ford explicitly
  under the "+8" family; blueovallabs glossary: "PCM — `0x7E0` on HS-CAN"].
- Known module diagnostic IDs (2011–2023 Explorer, FORScan community
  spreadsheet) [B — single community spreadsheet, but detailed and
  self-consistent]:
  - `0x7E0` PCM (powertrain) · `0x7E4` BECM (battery energy, 20MY+) ·
    `0x7E6` SOBDMC · `0x7D0` APIM (SYNC) · `0x7A5` FCDIM · `0x7A7` FCIM ·
    `0x7C4`/`0x7C6` SODL/SODR (blind-spot L/R) · `0x7C7` ACCM · `0x726` GWM
    (gateway, "no configurable as-built data").
- Functional (broadcast) diagnostics use `0x7DF` [B — ISO 15765-4 standard
  practice; generic OBD-II scan behavior].

### FORScan's approach
- FORScan speaks manufacturer-specific Ford services beyond generic OBD-II:
  reads/clears DTCs from *all* modules, reads PIDs, runs actuator tests and
  service procedures, edits module **as-built configuration**, and programs
  certain modules [B — FORScan forum; expeditionforum walkthrough].
- **MS-CAN handling:** with a switched ELM327, FORScan analyzes the vehicle
  configuration at connect; if MS-CAN modules are expected it prompts the
  user to flip the HS/MS switch, then proceeds automatically [C —
  slideshare FORScan v2 tutorial; behavior consistent with FORScan forum
  adapter docs].
- **Adapter matrix** (official FORScan forum) [B]:
  - Stock ELM327: HS-CAN yes, MS-CAN no.
  - ELM327 with HS/MS switch ("Ford/Mazda compatible"): both.
  - STN-based (OBDLink MX/MX+, ELS27, OBDLink EX): both, no manual switch
    (electronic switching).
  - None of the listed adapters support Ford UBP (the pre-CAN SCP-adjacent
    protocol column is uniformly "−").
- **Extended license** (free, forum-generated, expires periodically) unlocks
  programming/configuration functions [B — FORScan forum; expeditionforum
  walkthrough].
- FORScan requires adapters *fully* compatible with the original ELM327;
  many clone chips fail on Ford's service-level (non-OBD-II) protocols [B —
  FORScan forum adapter guide].

### Seed/key and PATS
- **No public Ford seed/key algorithm was found. Do not invent one.**
- What is publicly documented about PATS (immobilizer) programming via
  FORScan [C — cartipsdaily how-to; procedure-level, not cryptographic]:
  - Two access methods: **timed access** (maintain connection 10–12 min
    until "Security Access Granted"; interruptions reset the timer; some
    models impose 30–60 min anti-scan lockout after failures) and **coded
    access** (vehicle shows an Outcode; an authorized generator returns the
    matching Incode; FORScan has built-in generators for many older models).
  - The Incode generators' internals are not public.
- UDS service `0x27` (SecurityAccess) exists on Ford ECUs and gates
  sensitive operations; attempts without the key return NRC `0x35`
  (invalidKey) [B — UDS standard behavior; demonstrated on a virtual Ford
  ECU in dawidkantowicz/virtual-can-hacking-lab docs].
- As-built *reading* needs no security access; *writing* configuration and
  PATS functions do [B — FORScan extended-license gating].

---

## 4. M2 mapping (which M2 hardware talks to which Ford bus)

| Ford bus | OBD-II pins | M2 hardware | Notes |
|---|---|---|---|
| HS-CAN | 6 / 14 | CAN0 or CAN1 (TJA1051), 500 kbps | Standard; matches M2RET/ELM modes directly |
| MS-CAN | 3 / 11 | CAN0 or CAN1 (TJA1051), **125 kbps** | Ford-proprietary pins — the whole reason FORScan needs the HS/MS switch; on the M2 just wire the second CAN controller to 3/11 and run 125k. No switch needed since the M2 has two independent CAN controllers |
| HS-CAN2 | (model-specific) | CAN0/CAN1 if exposed at DLC | Availability at the OBD-II port varies; often gateway-internal only |
| SCP (J1850 PWM) | 2 / 10 | M2 J1850 interface in **PWM mode** (pin 50 HIGH = 41.6k PWM), 12V bus | Pre-2004 Fords; IFR bytes required by Ford's SCP variant |
| LIN body modules | various | LIN1/LIN2 (TJA1027), 19.2 kbps typical | Door/climate sub-buses on some models |
| CAN FD (2021+ select) | 6 / 14 | **NOT supported** — TJA1051 is CAN 2.0 only | 2021+ F-150, Mach-E, etc. are out of reach for M2 CAN participation |

Key M2 advantage for Ford, worth stating plainly: a switched ELM327 can only
see one bus at a time (HS *or* MS), but the M2's two independent CAN
controllers can watch **HS-CAN (6/14) and MS-CAN (3/11) simultaneously** —
something FORScan+ELM327 cannot do. This is INFERRED from the hardware
topology (two TJA1051 + dual SAM3X CAN controllers) but follows directly.

---

## 5. Notable quirks

1. **MS-CAN is not on all Fords.** FORScan only prompts for the HS/MS switch
   when the vehicle configuration expects MS-CAN modules; absence of the
   prompt means no MS-CAN on that vehicle [C — slideshare tutorial].
   Firmware should probe, not assume.
2. **Gateway filtering.** On GWM-equipped vehicles, diagnostic requests via
   the OBD-II port are routed/filtered by the gateway; raw bus traffic on
   interior buses may not be visible at the DLC at all [B — openpilot wiki
   GWM definition; consequence is INFERRED].
3. **2021+ F-150 / Mach-E / etc. are CAN FD.** FORScan itself had limited
   support at launch ("all of the modules have changed so much") and needed
   newer adapter hardware [B — f150lightningforum, FORScan tutorial]. The M2
   cannot do CAN FD (see §4).
4. **PATS timed access is fragile.** Battery voltage must stay 13.0–13.5 V
   during key programming; dropping below ~11.5 V mid-write risks a
   permanent no-start [C — cartipsdaily; plausible but single-source —
   treat the exact voltages as anecdotal, the fragility as real].
5. **As-built editing is powerful but bounded.** FORScan can only
   enable/disable features Ford built into the module firmware; it cannot
   make hardware do things it was never designed for [B — FORScan tutorial].
   Same applies to any M2-based configuration tool.
6. **Clone adapters lie.** ~80% of "ELM327" adapters are bad clones that work
   for generic OBD-II but fail on Ford's service-level protocols [B —
   FORScan forum]. For M2 firmware emulating ELM/STN behavior, implement the
   full ELM327 command set faithfully — FORScan probes for it.
7. **SCP IFR requirement.** Any M2 J1850-PWM implementation targeting
   pre-2004 Fords must generate In-Frame Response bytes; Ford's SCP variant
   requires them, unlike GM's VPW [B — Fordmods BAE 5030].
8. **Model-year overlap.** The 2002–2006 transition means a 2004 Ford may be
   SCP *or* CAN — always auto-detect (pin presence: 2/10 vs 6/14) rather than
   trusting the model year [C — scribd list; the engineering advice is sound
   regardless].

---

## Sources consulted

- merlinmb/esp32_odbii_hs_ms (GitHub) — ESP32 project reading HS+MS CAN on
  a 2008 Ford Focus; bus/pin/module tables [B]
- blueovallabs/ford-pscm-re `docs/glossary.md` (GitHub) — Ford RE project
  glossary: HS/MS-CAN, BdyCM gateway role, PCM 0x7E0 [B]
- forum.forscan.org "ELM327-compatible adapters - how to choose" — official
  FORScan forum adapter capability matrix [B]
- FORScan community tutorial (Google Doc) — adapter recommendations incl.
  2021+ F-150 OBDLink EX requirement [B]
- slideshare "How to access ms can bus using for scan v2 and modified
  elm327" — FORScan v2 MS-CAN switch-prompt behavior, switch wiring [C]
- scribd "Ford OBD-2 Compatibility List" — model/year/protocol table [C]
- AutoEnginuity ScanTool docs (via scantool.net) — "J1850 PWM for Fords
  older than 2004" [B]
- Fordmods BAE 5030 (Ford training material) — J1850 PWM/VPW
  characteristics, Ford IFR requirement [B]
- commaai/openpilot wiki "Ford" — supported vehicles, CAN-FD list, GWM
  definition, module terms [B]
- commaai/opendbc (local clone, `work/opendbc/`) — Ford DBC files and
  `car/ford/values.py` platform/CANFD flags [B]
- philipkocanda/canair `VEHICLE-PROTOCOLS.md` (GitHub) — Ford in the
  0x7E0→0x7E8 "+8" addressing family [B]
- Ford Explorer FORScan spreadsheet (scribd) — module diagnostic IDs incl.
  GWM 0x726 [B]
- expeditionforum.com FORScan walkthrough — extended license, HS/MS switch
  adapter [C]
- cartipsdaily.com FORScan PATS guide — timed vs coded access [C]
- kanbkam adapter listing — HS-CAN2 module list [C]
- f150lightningforum.com — 2021 F-150 adapter issues [C]

## Open questions (for a later pass or vehicle testing)
- Exact MS-CAN bitrate on post-2020 platforms (125k vs faster?) — the
  "125–500 kbps depending on chassis" claim is single-source.
- Which modules sit on HS-CAN2 vs HS-CAN per platform, and whether HS-CAN2
  is reachable at the DLC.
- Ford-specific UDS DIDs (0x22) per module — FORScan as-built addresses are
  the practical source; harvesting them is a separate task.
- Whether any Ford gateway implements diagnostic firewalling comparable to
  Chrysler's Secure Gateway (none found in these sources).
