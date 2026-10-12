# Mazda — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, well-documented
reverse-engineering, trade/technician sources) · **C** = single anecdotal
report. Unverified items are marked [?]. Research date: 2026-10-07.

Mazda's defining feature is the **era split**: a Ford-platform era (roughly
2001–2012, Ford-derived networks, Ford tooling) and the SkyActiv era
(2012+, Mazda's own HS/MS-CAN architecture). The two eras share the DLC pin
layout but differ in protocols, tooling, and diagnostic conventions.

---

## 1. Bus architecture

### 1.1 CAN buses (both eras)

Mazda's own network training material (Mazda curriculum/TSB doc, "Mazda
Vehicle Networks", via rx8club) states **HS-CAN = 500 kbps** and
**MS-CAN = 125 kbps** [B — Mazda training document]. SkyActiv-era
community reverse-engineering confirms the same split: the 6th-gen Mazda
CAN DBC project (berumiya/CAN_DBC_6thGenMazda, CC-BY-4.0, real-vehicle
analysis of MX-5 ND1/ND2 2015–2023) lists HS-CAN (500 kbps) and MS-CAN
(125 kbps) [B]. Racelogic's Mazda 6 and MX-5 ND vehicle CAN guides specify
500k on DLC pins 6/14 [B].

| Bus | Bitrate | DLC pins | Role |
|---|---|---|---|
| HS-CAN | 500 kbps | 6 (CANH) / 14 (CANL) | Powertrain/chassis: PCM, TCM, DSC/ABS HU/CM, SAS (airbag), IC [B] |
| MS-CAN | 125 kbps | 3 / 11 | Body/comfort: FBCM/RBCM, HVAC, audio, TPMS, RKE modules [B] |

- Unlike Toyota, **Mazda exposes MS-CAN at the DLC (pins 3/11)** — the same
  layout as Ford. Two M2 CAN controllers can watch HS+MS simultaneously
  straight from the OBD port [B — Mazda training doc + FORScan ecosystem].
- Termination: standard 60 Ω class across 6/14 [C — generic CAN practice;
  no Mazda-specific figure found].

### 1.2 Gateway behavior

- The Mazda training doc's Mazda3 example shows the **instrument cluster
  (IC) forwarding messages between buses**: the PCM sends RPM on HS-CAN;
  the IC accepts it and "adapts the message speed for transmission on the
  medium speed CAN network" [B]. I.e., Mazda uses participating modules as
  inter-bus bridges rather than always a dedicated gateway ECU.
- Modules seen in the Mazda3 HS/MS example: PCM, TPMS, EHPAS, ABS HU/CM,
  IC (HS side); SAS, audio, PJB (passenger junction box, MS side) [B].
- No Stellantis-style cryptographic gateway was found on any Mazda source
  [C — absence of evidence]. Diagnostic access to body modules is via the
  MS-CAN pins at the DLC (no gateway traversal needed for bus access)
  [B — DLC pin layout].

### 1.3 CAN FD / 7th generation

- Mazda's 7th-gen architecture (2019 Mazda3 BP, CX-30) is **not verified**
  as CAN 2.0 or CAN FD. Two circumstantial signals point to a network
  change: (a) a widely-sold "FOR Mazda" ELM327 adapter listing explicitly
  warns it "does not support Mazda 3 and CX-30 models" [C — seller
  listing]; (b) the berumiya 6th-gen DBC project notes that 2024+ MX-5
  (ND3) "appear to be significantly different and follow a substantially
  different architecture" [B].
- **M2 implication (INFERRED, not verified):** the M2 is CAN 2.0 only
  (TJA1051). If 7th-gen Mazdas carry CAN FD traffic, the M2 cannot
  participate in or fully decode those buses. Treat 2019+ BP/CX-30 and
  2024+ ND3 as **out of M2 scope until verified** [?].

### 1.4 Module architecture families (SkyActiv/6th gen)

- The berumiya project documents two 6th-gen electrical-architecture
  styles [B]:
  - **BCMM** (single body control module): Demio/Mazda2 (DJ/DL), CX-3 (DK)
  - **FBCM/RBCM** (front/rear body control modules): CX-5 (KE/KF),
    CX-9 (TC), Mazda3 (BM/BN), Mazda6 (GJ/GL)
- They are "broadly similar in overall structure" with high HS/MS message
  similarity within BCMM vehicles [B].

---

## 2. Diagnostic access

### 2.1 DLC pinout (Mazda)

From the Mazda training document's DLC table [B], and corroborated by the
general Mazda OBD-II pinout surveys [C]:

| Pin | Circuit |
|---|---|
| 2 | SCP+ (J1850 PWM, Ford era) |
| 3 | MS-CAN H |
| 4/5 | Ground |
| 6 | HS-CAN H |
| 7 | ISO 9141 K-line |
| 10 | SCP− (J1850 PWM, Ford era) |
| 11 | MS-CAN L |
| 13 | FLASH — signals PCM to erase EPROM during programming (Ford era) [B] |
| 14 | HS-CAN L |
| 16 | Battery+ |

### 2.2 Protocol and addressing

- CAN-era Mazda uses **UDS/ISO-TP diagnostics on HS-CAN** with the standard
  **+8 response offset**: PCM request **0x7E0** → response **0x7E8**
  [B — Ford-family convention carried to Mazda; FORScan Mazda coverage].
  Standard emissions OBD-II (SAE J1979) on 6/14 works with any generic
  tool [A — legislated].
- **Functional broadcast 0x7DF** follows the same Ford/ISO-15765 convention
  [C].
- Module physical addressing follows the Ford-family scheme on shared and
  later platforms (e.g. PCM 0x7E0 class); no Mazda-published physical-ID
  table was found [C/B — FORScan ecosystem evidence].
- Pre-2008 Ford-era models used **SCP (J1850 PWM)** diagnostics on
  pins 2/10 [B — Mazda training doc], and some carried ISO 9141 on pin 7
  [B].

### 2.3 Tooling

- **M-MDS (Mazda Modular Diagnostic System)** is Mazda's dealer tool;
  earlier tools were **WDS** (Worldwide Diagnostic System, Ford-shared)
  and **IDS** (Integrated Diagnostic Software, Ford) on shared platforms
  [B — Mazda curriculum/training material and MNAO service bulletins].
- **FORScan** supports Mazda 1996–2024 (HS+MS CAN with a switched adapter;
  extended license required for module configuration) [B — FORScan
  community/docs]. This is the practical aftermarket path for Mazda
  module-level work.

### 2.4 Security policy

- **No public Mazda seed/key (UDS 0x27) algorithm was found. None is
  invented or reproduced here.**
- Immobilizer work (P1260-class faults, key programming after PCM
  replacement) is documented in owner reports as requiring M-MDS/IDS at
  the dealer — a used PCM will communicate but the vehicle will not start
  until the immobilizer is programmed with Mazda's software [C — owner
  reports; consistent with dealer-tool territory].
- For M2 firmware: read-only diagnostics and standard UDS services are the
  in-scope surface. Security-gated operations are dealer-tool territory.

---

## 3. Era split (the key Mazda angle)

### 3.1 Ford-platform heritage (approx. 2001–2012)

- **Models:** Mazda3 BK (Ford C1), Mazda6 GG/GY (Ford CD3), Mazda5,
  Tribute (Ford Escape rebadge, fully Ford), early CX-7/CX-9, RX-8 [B —
  platform sharing is well documented].
- **Networks:** Ford-derived. SCP (SAE J1850 PWM, 41.6 kbps) on DLC
  pins 2/10 for diagnostics; HS-CAN 500k (6/14) and MS-CAN 125k (3/11)
  added progressively; ISO 9141 K-line on pin 7 on some models; pin 13
  FLASH line for PCM programming [B — Mazda training doc].
- **Diagnostics:** Ford-style addressing and Ford-style DTCs. Mazda DTCs
  from this era read like Ford's: P1000 (OBD monitor testing not
  completed), P1001 (unable to achieve self-test / SCP error), KOEO/KOER
  self-test P11xx-series semantics [B — Mazda DTC overview lists].
- **Tooling:** WDS, then IDS (Ford's Integrated Diagnostic Software)
  [B].
- **As-built/config:** Ford-format as-built records (7xx-xx-xx lines,
  e.g. 7E0-01-01) appear in FORScan Mazda workflows for these models
  [C — FORScan community; format inherited from Ford].
- The RX-8 training doc shows the full transitional pinout on one
  vehicle: SCP on 2/10, MS-CAN on 3/11, HS-CAN on 6/14, K-line on 7,
  FLASH on 13 [B].

### 3.2 SkyActiv era (2012+)

- **Models:** CX-5 KE (2012, first SkyActiv), Mazda3 BM/BN, Mazda6 GJ/GL,
  CX-3 DK, CX-9 TC, MX-5 ND, Mazda2 DJ; 7th gen: Mazda3 BP, CX-30 DM
  [B].
- **Networks:** Mazda's own architecture but the **HS/MS-CAN pin layout
  is retained** (6/14 = HS 500k, 3/11 = MS 125k) [B — berumiya repo,
  Racelogic guides, opendbc]. SCP is gone; K-line largely gone.
- **Body modules:** BCMM style (Mazda2/CX-3) or FBCM/RBCM style
  (CX-5, Mazda3 BM, Mazda6 GJ) [B — berumiya].
- **Diagnostics:** M-MDS dealer tool; FORScan covers these models for
  module DTCs and configuration [B]. Mazda-specific CAN IDs for
  diagnostics follow the 0x7E0-class convention [C/B].
- **DTC format:** Mazda workshop manuals print SAE J2012-DA extended
  codes with a **:00 suffix**, e.g. DTC P0101:00 (MAF sensor circuit
  range/performance, SkyActiv-D 2.2), each with detection conditions,
  fail-safe behavior, and possible causes [A — Mazda service manual
  via mazda3.neocities.org mirror].

### 3.3 What changed vs. what stayed

- Stayed: DLC pin layout (3/11 MS, 6/14 HS), HS=500k/MS=125k rates, the
  P-code family conventions, FORScan compatibility.
- Changed: SCP dropped; Mazda-specific body modules (BCMM/FBCM/RBCM)
  replaced Ford GEM/PJB conventions; M-MDS replaced IDS; DTC detail
  format moved to the :00 extended-code style.

---

## 4. DID catalog (Mazda-specific UDS 0x22)

**Coverage status: thin — recorded honestly.** No public Mazda-specific
0x22 DID catalog comparable to the Toyota OBDb signalsets was found in
this pass. What is documented:

- **As-built-style configuration records** on Ford-era models use the
  Ford format `7E0-01-01 xxxx xxxx xxxx` (module-block-line, hex data),
  read/written via FORScan for PCM and body modules [C — FORScan
  community; convention inherited from Ford].
- **VIN** is read via the ISO-standard DID **0xF190** (not Mazda-specific;
  listed for completeness) [A — ISO 14229-1].
- Mazda workshop manuals describe PID/data-monitor access through
  WDS/M-MDS ("read/clear diagnostic results, PID monitor and record,
  active command modes") but do not publish the underlying DID numbers
  [B — Mazda3 workshop manual excerpts].
- **open items:** Mazda-specific 0x22 DIDs for VIN/configuration/sensor
  data on SkyActiv models (no verified entries found — no padding
  invented); whether SkyActiv models retain Ford-style as-built block
  addressing [?].

---

## 5. Manufacturer-specific DTCs

Mazda quirks relevant to DTC work:
- Mazda workshop manuals print codes in SAE J2012-DA extended form with a
  **:00 suffix** (e.g. P0101:00) [A]. Community lists usually drop the
  suffix (P0101) — the same code [B].
- P1000/P1001 and much of the P11xx range are Ford-legacy self-test codes
  shared with Ford [B].

### P-codes

## P0126
- Description: Insufficient coolant temperature for stable operation
- Category: P
- Scope: manufacturer usage (Mazda SkyActiv-G)
- Possible causes: failsafe thermostat stuck open (coolant infiltration of the dry cavity in the Coolant Control Valve integrated thermostat)
- Diagnostic notes: Mazda-specific pattern failure: the engine fails to reach operating temperature. Mazda issued a chain of TSBs (#01-011/21, #01-013/22, #01-005/23, #01-005/24, #01-001/26) and Special Service Program SSP D8 extended the warranty to 15 years/150,000 miles (2018–2025 CX-5, 2019–2023 Mazda3, 2019–2022 CX-3, 2018–2021 Mazda6, 2020–2023 CX-30). Fix is an updated dummy-plug kit plus PCM software update — check dealer VIN coverage before paying.
- Grade: [B]
- Evidence: SlashGear summary of Mazda TSBs/SSP D8; Mazda MNAO TSB numbers

## P1000
- Description: OBD II Monitor Testing Not Completed
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: Set when drive cycles are incomplete; not a fault.
- Grade: [B]
- Evidence: Mazda DTC overview list (enginelighthelp.com transcription)

## P1001
- Description: Unable to Achieve Self-Test Function or SCP Error
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: SCP network fault (Ford era)
- Diagnostic notes: Ford-era self-test code; SCP = the J1850 PWM network.
- Grade: [B]
- Evidence: Mazda DTC overview list

## P1100
- Description: Mass Airflow Sensor Circuit Intermittent
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Mazda DTC overview list (single transcription)

## P1101
- Description: Mass Airflow Sensor Circuit out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: KOEO/KOER self-test-era code.
- Grade: [C]
- Evidence: Mazda DTC overview list

## P1116
- Description: ECT Sensor Circuit Out of Self Test Range
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Mazda DTC overview list

## P1120
- Description: Throttle Position Sensor out of Range Low
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Mazda DTC overview list

## P1131
- Description: HO2S Bank 1 Sensor 1 Signal Below 0.45v (A/F Ratio Too Lean)
- Category: P
- Scope: manufacturer (Ford-shared)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Mazda DTC overview list

## P1260
- Description: THEFT Detected, Vehicle Immobilized (Anti-Theft System Signal Detected — Engine Disabled)
- Category: P
- Scope: manufacturer (Ford-shared PATS)
- Possible causes: unprogrammed/incorrect key; PCM replaced without immobilizer programming
- Diagnostic notes: Seen as an archived (inactive) code on the engine ECU via generic scanners. Immobilizer programming after PCM replacement requires M-MDS/IDS — dealer-tool territory. Do not attempt key workarounds.
- Grade: [B]
- Evidence: Car Scanner ELM OBD2 DTC report (Mazda) via JustAnswer; Mazda PCM-replacement owner reports

## P2006
- Description: Intake Manifold Runner Control Stuck Closed
- Category: P
- Scope: manufacturer usage (Mazda)
- Possible causes: not documented
- Diagnostic notes: Listed in the Mazda3 OBD code chart; IMRC actuator.
- Grade: [C]
- Evidence: Mazda3 OBD-II diagnostic codes chart (scribd transcription)

### B-codes (Mazda3 workshop manual DTC tables)

## B1041
- Description: Adaptive Front Lighting System (AFS) control module
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: SkyActiv-era code with :54 suffix seen (B1041:54).
- Grade: [C]
- Evidence: Mazda M-Tip MT-004/18 (MNAO, via manuals.plus)

## B1238
- Description: EHPAS control module
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: EHPAS = electro-hydraulic power assist steering (Mazda3 BK era). See also B1342/B2141/B2477 (module/configuration) and C1099/C1278/C1956.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table (WDS column)

## B1251 / B1253
- Description: Cabin temperature sensor
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: HVAC DTCs from the Mazda3 workshop manual table.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## B1260 / B1261
- Description: Solar radiation sensor
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: HVAC DTCs; B1261 appears in owner Q&A as a real stored code.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table; JustAnswer owner thread

## B1274 / B1275
- Description: Airflow mode actuator (potentiometer)
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: HVAC DTCs.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## B1282
- Description: Air mix actuator (potentiometer)
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: HVAC DTCs. See also B2832/B2834 (motor lock).
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## B1317 / B1318
- Description: Battery power supply
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: low/high system voltage to the module
- Diagnostic notes: Voltage codes; check charging system before module faults.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## B1342
- Description: EHPAS control module (internal malfunction)
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Mazda3 workshop manual cross-references B1342 with C1267/C1730 under DSC.
- Grade: [B]
- Evidence: Mazda3 workshop manual brake/DSC DTC table

## B1352
- Description: Ignition power supply
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## B2141 / B2477
- Description: EHPAS control module configuration
- Category: B
- Scope: manufacturer (Mazda)
- Possible causes: module not configured / configuration mismatch
- Diagnostic notes: Configuration codes — set after module replacement without coding.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

### C-codes (Mazda3 workshop manual DTC tables)

## C0061
- Description: DSC HU/CM
- Category: C
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: SkyActiv-era code with :54 suffix seen (C0061:54).
- Grade: [C]
- Evidence: Mazda M-Tip MT-004/18 (MNAO)

## C1001
- Description: Forward Sensing Camera (FSC)
- Category: C
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Seen as C1001:92 and C1001:97 (ADAS camera).
- Grade: [C]
- Evidence: Mazda M-Tip MT-004/18 (MNAO)

## C1099
- Description: Electric power steering oil pump (motor)
- Category: C
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: EHPAS pump motor circuit (Mazda3 BK era).
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## C1278 / C1956
- Description: P/S angle sensor
- Category: C
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Power-steering angle sensor codes.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

### U-codes

## U0073
- Description: CAN bus communication error
- Category: U
- Scope: manufacturer usage (Mazda)
- Possible causes: CAN wiring fault; module pulling the bus down
- Diagnostic notes: Listed in the Mazda3 workshop manual DTC table.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## U0100
- Description: Lost communication with the PCM
- Category: U
- Scope: manufacturer usage (Mazda)
- Possible causes: PCM power/ground; HS-CAN wiring
- Diagnostic notes: Listed in the Mazda3 workshop manual DTC table.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## U0140 / U0155 / U0184 / U0516
- Description: CAN communication system (lost communication with body modules)
- Category: U
- Scope: manufacturer usage (Mazda)
- Possible causes: not documented
- Diagnostic notes: HVAC-section U-codes from the Mazda3 workshop manual — body/MS-CAN module communication losses.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## U0415 / U0420
- Description: Invalid data received from MRCC/SBS (Mazda Radar Cruise Control / Smart Brake Support)
- Category: U
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Seen as U0415:00 / U0420:00 in the MNAO M-Tip.
- Grade: [C]
- Evidence: Mazda M-Tip MT-004/18 (MNAO)

## U2023
- Description: Fault received from other modules
- Category: U
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Listed in the Mazda3 workshop manual DTC table.
- Grade: [B]
- Evidence: Mazda3 workshop manual DTC table

## U300A
- Description: Electric Parking Brake (EPB) — control module
- Category: U
- Scope: manufacturer (Mazda)
- Possible causes: not documented
- Diagnostic notes: Seen as U300A:62.
- Grade: [C]
- Evidence: Mazda M-Tip MT-004/18 (MNAO)

### Coverage notes (DTCs)

- B-code coverage is Mazda3-workshop-manual based (B12xx HVAC, B13xx
  power/EHPAS, B2xxx config); full SRS B0xxx/B1xxx ranges not verified [?].
- C-code coverage centers on EHPAS/DSC; C0xxx chassis detail is partial [?].
- Diesel (SkyActiv-D) P-codes: P0101:00 format verified with full
  detection-condition detail on one code; the D-range catalog is not
  harvested [?].
- No immobilizer/seed-key material sought or reproduced.

---

## 6. Module-map notes

### 6.1 SkyActiv Mazda3 BM/BN (2014–2018) — FBCM style [B]

- **HS-CAN (500k):** PCM, TCM, DSC HU/CM, EPS, SRS (SAS), IC.
- **MS-CAN (125k):** FBCM/RBCM, HVAC, audio, TPMS, RKE/keyless.
- opendbc: mazda_2017.dbc (102 messages, HS-CAN ADAS/powertrain subset);
  Mazda 3 2017–18 supported in dashcam mode [B — local opendbc clone].
- Diagnostics: 0x7E0-class PCM addressing; M-MDS or FORScan [C/B].

### 6.2 Ford-shared Mazda6 GG (2003–2008) — transitional [B]

- **SCP (J1850 PWM):** DLC pins 2/10, 41.6 kbps — primary diagnostic bus
  for early GG; WDS/IDS tooling [B].
- **HS-CAN (500k) / MS-CAN (125k):** added progressively; modules PCM,
  TCM, ABS, IC, PJB, EHPAS [B — Mazda training doc Mazda3/BK example,
  GG shares the architecture].
- **K-line (pin 7)** and **FLASH (pin 13)** present [B].
- Diagnostics are Ford-style (P1000/P1001 self-test codes, as-built
  config) [B].

### 6.3 SkyActiv CX-5 KE/KF (2012+) — FBCM/RBCM style [B]

- First SkyActiv model (2012) [B — WardsAuto].
- **HS-CAN (500k):** PCM, TCM, DSC, EPS, SRS, IC; **MS-CAN (125k):**
  FBCM/RBCM, HVAC, audio [B — berumiya FBCM/RBCM style classification].
- opendbc: CX-5 2017–21 dashcam mode; 2022–25 upstream [B — opendbc
  CARS.md].
- Racelogic CAN guides exist for Mazda6 and MX-5 (500k on 6/14) as
  reference captures [B].

---

## 7. M2 hardware → Mazda bus mapping

| Mazda bus | DLC pins | M2 hardware path |
|---|---|---|
| HS-CAN (500k) | 6 / 14 | CAN0 or CAN1 (TJA1051, due_can). Primary diagnostic + logging bus |
| MS-CAN (125k) | 3 / 11 | Second CAN controller — **exposed at the DLC**, no gateway traversal needed |
| K-line (10.4k) | 7 | K-line transceiver (TJA1027). Ford-era non-CAN modules |
| SCP J1850 PWM (41.6k) | 2 / 10 | M2 J1850 hardware (discrete circuit, pins 49–54). Ford-era models only (pre-~2008) |
| FLASH programming line | 13 | Not a data bus — PCM programming signal; not an M2 target |
| 7th-gen BP/CX-30 / 2024+ ND3 buses | 6 / 14 | **Out of M2 scope if CAN FD** — unverified, treat as unknown [?] |

---

## 8. Notable quirks

1. **MS-CAN at the DLC is the Mazda/Ford signature.** Pins 3/11 carry
   125k body traffic straight to the scan tool — the M2's two CAN
   controllers can watch HS+MS simultaneously with no direct-tap work,
   unlike Toyota [B].
2. **The era split is real and testable.** SCP on 2/10 = Ford-era
   (pre-~2008); no SCP = SkyActiv-era. A single DLC pin check dates the
   architecture [B].
3. **Pin 13 FLASH is a programming trigger**, not a bus — 12–18 V
   signals the PCM to erase EPROM. Never drive it from the M2 [B].
4. **P0126 is the Mazda-specific pattern failure** on SkyActiv-G: the
   coolant-control-valve thermostat sticks open; SSP D8 extends warranty
   to 15y/150k on 2018–2025 CX-5, 2019–2023 Mazda3, 2019–2022 CX-3,
   2018–2021 Mazda6, 2020–2023 CX-30 [B].
5. **Aftermarket DLC devices are a known Mazda fault source.** MNAO
   M-Tip MT-004/18 (2018) documents insurance/GPS dongles and phone
   chargers disrupting the CAN system, blocking IDS/M-MDS communication,
   and storing U0xxx codes — check for dongles before chasing network
   DTCs [B].
6. **BCMM vs FBCM/RBCM** splits the SkyActiv body architecture; cross-
   model DBC reuse is strongest within a style (berumiya: BCMM =
   Mazda2/CX-3; FBCM/RBCM = CX-5, Mazda3 BM, Mazda6 GJ) [B].
7. **7th-gen unknown.** 2019+ Mazda3 BP / CX-30 and 2024+ MX-5 ND3 may
   use a different network architecture (possibly CAN FD); cheap
   CAN 2.0 adapters are reported incompatible with BP/CX-30 [C].
   Do not assume M2 compatibility there.

---

## Sources consulted

- Mazda "Vehicle Networks" curriculum/TSB document (via rx8club.com
  attachment) — DLC pin table (SCP 2/10, MS-CAN 3/11, HS-CAN 6/14,
  K-line 7, FLASH 13), HS=500k/MS=125k, Mazda3 HS/MS module example,
  IC inter-bus forwarding [B]
- berumiya/CAN_DBC_6thGenMazda (GitHub, CC-BY-4.0) — HS-CAN 500k /
  MS-CAN 125k on MX-5 ND1/ND2 (2015–2023), BCMM vs FBCM/RBCM model
  grouping, ND3-2024+ architecture-change note [B]
- Local opendbc clone (work/opendbc): mazda_2017.dbc (102 messages),
  mazda_3_2019.dbc (59 messages), mazda_rx8.dbc (7 messages); CARS.md
  Mazda coverage rows (3 2017–18, 6 2017–20, CX-5 2017–25, CX-9
  2016–23) [B]
- Mazda3 workshop manual DTC tables (via scribd) — B12xx HVAC, B13xx
  EHPAS/power, B2xxx config, C1099/C1278/C1956, U0073/U0100/U2023,
  U0140/U0155/U0184/U0516, P1260 [B]
- Mazda3 SkyActiv-D 2.2 service manual, DTC P0101:00 page
  (mazda3.neocities.org mirror) — :00 extended-code format, detection
  conditions, fail-safe, possible causes [A]
- Mazda M-Tip MT-004/18 (MNAO, via manuals.plus, 2018) — aftermarket
  DLC-device CAN disruption; B1041:54, C0061:54, C1001:92/:97,
  U0415:00/U0420:00, U300A:62 [B]
- Mazda M-MDS curriculum training material (via manuals.plus) —
  M-MDS/WDS/IDS tooling, abbreviations [B]
- Mazda DTC overview lists (enginelighthelp.com; scribd transcriptions)
  — P1000/P1001, P11xx Ford-legacy codes [C]
- SlashGear "5 Of The Most Common Mazda DTC Codes" — P0126 SkyActiv-G
  thermostat, TSB chain, SSP D8 coverage [B]
- Racelogic vehicle CAN guides: Mazda 6, Mazda MX-5 ND (500k on
  DLC 6/14) [B]
- FORScan community material (forum threads, module-address guides) —
  HS/MS adapter switching (pins 3/11 vs 6/14), Mazda 1996–2024
  coverage, module list [C/B]
- Mazda OBD-II connector pinout surveys (yumpu) — 3/11 low-speed CAN,
  6/14 high-speed CAN, 7 K-line [C]
- JustAnswer owner threads — P1260 (THEFT/immobilized, PCM replacement
  needs M-MDS/IDS), B1261 solar sensor, 2007 Mazda3 DLC location [C]

## Open items

- Mazda-specific UDS 0x22 DID catalog for SkyActiv models (no verified
  entries found; honest gap, nothing invented) [?]
- Whether 2019+ Mazda3 BP / CX-30 and 2024+ MX-5 ND3 use CAN FD
  (unverified — M2 scope question) [?]
- Mazda physical diagnostic CAN IDs per module beyond the 0x7E0-class
  convention [?]
- SkyActiv-era gateway module identity and routing behavior (the IC
  forwarding example is Ford-era Mazda3 BK) [?]
- Full SRS B0xxx/B1xxx ranges; diesel SkyActiv-D P-code catalog [?]
- Whether SkyActiv models retain Ford-style as-built block addressing
  for module configuration [?]
