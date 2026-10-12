# Nissan / Infiniti — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (well-documented reverse-engineering,
technician sources, open-source implementations) · **C** = single anecdotal
report. Unverified items are marked [?]. Research date: 2026-10-06.

Note: opendbc coverage is thin — one DBC (`nissan_xterra_2011.dbc`, 15
messages). This brief is correspondingly research-heavy.

---

## 1. Bus architecture

### 1.1 CAN buses

| Bus | Bitrate | DLC pins | Role |
|---|---|---|---|
| Main CAN ("CAN COMM" / V-CAN) | **500 kbps, 11-bit IDs** | 6 (CANH) / 14 (CANL) | Powertrain, chassis, body, diagnostics [A for pins, B for bitrate] |
| AV-CAN (infotainment) | 500 kbps, 11-bit IDs | 3 / 11 (on models that expose it, e.g. Leaf) | Infotainment traffic [B] |
| AV COMM (audio↔NAVI, isolated) | 500 kbps, 11-bit IDs | not on DLC | Audio unit ↔ NAVI unit (NAVI is bus master), on Qashqai J10 [B] |

- Nissan's own technician publication (Nissan Tech News, March 2011) puts
  CAN on **DLC pins 6 and 14** with **two 120 Ω terminating resistors**
  (usually one in the ECM, the other in the IPDM or TCM) and specifies the
  **~60 Ω across pins 6/14** ignition-off resistance check [A]
  (source: https://automotivetechinfo.com/wp-content/uploads/2011/03/Nissan-CAN-Controller-Area-Networks-Advantages-Diagnosis-Repair.pdf).
- The 500 kbps / 11-bit figure is from community reverse-engineering: the
  Nissan Leaf OBD manual documents "ISO 15765-4 CAN (11-bit ID, 500 kBd)" on
  the diagnostic connector [B]
  (https://github.com/sethfischer/nissan-leaf-obd-manual); a 2013 Qashqai J10
  capture project found both the main bus and the AV COMM bus running
  "500kbps with 11-bit addresses" [B]
  (https://github.com/13621732127/nissan-qashqai-can-info); a 2018 Pathfinder
  diagnostics project measured "ISO 15765-4 CAN, 11-bit, 500 kbps" at the
  OBD-II port [B] (https://github.com/howeypeter/nissan-diagnose-jutter).
- ⚠️ **CONFLICT:** the Nissan Tech News article quoted above states data
  "flows on the CAN bus at a rate of 1Mbit/s". That contradicts the
  community-verified 500 kbps captures. It is reported here as an
  unresolved conflict rather than silently discarded — the 1 Mbit/s figure
  is likely an error in the trade article [A vs B].
- Most Nissans appear to have a **single major CAN bus** with 6–12 devices
  depending on configuration (Qashqai J10 finding, believed to generalize
  to Juke/Pulsar/Sentra/370Z/X-Trail/Murano of the same era) [B].

### 1.2 Terminators, comm codes, and factory tooling [A]

From Nissan TSB NTB10-066C (May 20, 2024, "CAN communication" diagnosis
tips; source: https://vinveil.com/master/assets/tsbs/MC-11004960-0001.pdf):

- ~60 Ω across DLC pins 6/14 = healthy bus; ~120 Ω at a terminating module.
- Terminating modules vary by model — examples include **IPDM, ECM, or BCM**.
- Standard CAN fault codes: **U1000** (missing CAN comms, general),
  **U1001** (ECM missing CAN comms), **U1002** (missing comms, tighter spec
  than U1000), **U1010** (module internal error).
- CONSULT-III plus usage requires selecting the correct **"CAN type"** per
  model; the TSB references a V-CAN diagram per model family.
- **Excluded from that TSB:** 2023–2024 Ariya, 2022–2024 Pathfinder R53,
  2021–2024 Rogue T33, 2020–2024 Sentra B18 [A]. These models use a
  different/newer CAN architecture not covered by the legacy CAN diagnosis
  procedure — an open question for v1.2 research (possible CAN FD or
  multi-bus gateway design) [?].

### 1.3 Gateway architecture

- On at least the 2018 Pathfinder, the **BCM performs a CAN-gateway
  function**: the OBD-II (J1962) port carries **diagnostic
  request/response traffic only**. Passive sniffing sees **zero frames** —
  that is normal, not a fault — because the BCM gateway never forwards raw
  inter-module traffic to the diagnostic segment. Raw-CAN sniffing requires
  a physical internal-bus tap (a 40-pin BCM "T" cable on that vehicle) [B —
  howeypeter/nissan-diagnose-jutter project notes].
- Practical consequence: a passive M2 logger on DLC 6/14 of a
  gatewayed-era Nissan will capture nothing unless it actively sends
  diagnostic requests; monitoring real inter-module traffic means tapping
  the internal bus behind the BCM [B for Pathfinder; generalization to
  other gatewayed models marked C].

### 1.4 Model-year evolution

- **1989–~2000:** DDL (Consult I), 14-pin gray connector — see §2 [B].
- **1996–~2004:** transition era — 16-pin J1962 DLC present, but Nissan's
  primary diagnostics still flowed through Consult/DDL lines; OBD-II DLC
  also carried K-line for generic scan tools [A/B — see §2].
- **~2003+:** CAN rollout (community rule of thumb: "all 2003 and newer
  are CAN" [C]). Mid-2000s vehicles (e.g. 2009 Titan service manual) show
  CAN-based signal transfer (e.g. electrical-load signal from BCM to ECM
  "transferred through the CAN communication line" via IPDM E/R) [B].

---

## 2. Legacy: DDL (Diagnostic Data Link) and K-line

### 2.1 DDL / Consult I physical layer [B]

Source: "Consult Protocol & Commands Issue 7", a Nissan Technical egroup
technical note archived at http://www.clara.net/www/nissanlinks/tech/consult_spec.pdf,
cross-checked against the open-source `cansult` implementation
(https://github.com/irudoy/cansult). Quotes are brief and paraphrased.

- **Wiring:** 3 wires — **TX, RX, Async Clock**. Host↔ECU point-to-point
  (not a multidrop bus).
- **Voltage levels:** host TX-to-ECU is **12 V, idle low** (i.e. 0 V idle,
  driven high to ~12 V); ECU output is **open-collector, idle high**
  (host must source a 5 V pull-up). In other words the link is inverted
  relative to RS-232 conventions: idle-low on the host TX line.
- **Timing:** **9600 baud default**, 8 data bits, no parity, 1 stop bit,
  **LSB first**. Bit timing is governed by a **153.6 kHz clock (16×
  baud) generated by the host (the scan tool)**, free-running — "no clock
  synchronization is required".
- **Init sequence:** host sends `FF FF EF`; ECU responds `0x10` (bitwise
  inverse of `EF`). The last byte is an ECU-variant ID: `0xEF` = engine
  ECU, `0xED` = A32 OBD2 engine ECU, `0xEA` = A/T, `0xE4` = S-HICAS,
  `0xDF` = aircon. Init sometimes must be sent twice before the ECU
  responds (confirmed independently by the `cansult` author).
- **Framing:** host sends a command byte; ECU echoes the **bitwise
  inverted** command byte as an ACK. A `0xF0` ("go ahead") opens a stream;
  streamed frames are `0xFF` + byte-count + data bytes, repeated until
  stopped. Spec stop byte is `0x30`; the ECU then finishes the current
  frame and replies `0xCF`. ⚠️ **Conflict:** the `cansult` implementation
  uses `0x03` to stop the stream, noting a spec/firmware discrepancy —
  reported, not resolved [B].
- **Idle timeout:** ECU waits **>30 minutes** for host input before
  abandoning the session; there is **no ECU-side watchdog on active
  streaming** — the host must terminate it [B].
- **Command set (engine ECU):**
  - `0xD1` — read diagnostic trouble codes
  - `0xC1` — clear DTCs
  - `0x51` — clear "transient" DTC set
  - `0xD0` — read ECU part number (22-byte response, format `XXXX
    23710-YYYYYY`); on A32 (OBD2-era) the command is `D0 F0` and returns
    32 bytes [B]
  - `0x5A <reg>` — start sensor data stream for register `<reg>`
    (ACK `0xA5 <reg>`; `0xA5 0xFE` = unsupported register). Max **20 bytes**
    per stream frame. Register map includes RPM, speed, coolant temp,
    battery voltage, TPS, timing, MAF, O2, injector time, etc.
  - `0xC9` — read ROM/RAM (max 8 bytes, address range 0x8000–0xFFFF)
  - `0x0A` — active tests: fuel trim, timing advance, IACV, power balance,
    fuel pump relay, clear self-learn values.

### 2.2 DDL connectors and years

- **14-pin gray Consult connector**, usually near the driver's-side fuse
  box, on vehicles ~1989–2000 (some through ~2004) [B — multiple
  community/parts sources].
- **ECU-side DDL pins vary by ECU family** (connector pins, looking at the
  ECU plug) [B — Nistune "MAF and Consult pinouts" document]:
  - S13 CA18DET / S14 SR20DET / HCR32 RB20 / BNR32 RB20 / Z32 VG30:
    RX=21, TX=22, CLK=31
  - S13/S14A/S15 SR20DET / B13 SR20DE / S13 KA24DE: RX=7, TX=15, CLK=14
    (CHK pin present, unused by CONSULT)
  - B14 SR20DE / S14 KA24DE / N15 GA16DE: RX=64, TX=65, CLK=68
  - A32 Maxima VQ30DE / ER34 RB25DET: RX=75, TX=76 (CLK=78 on Z32 only)
- **16-pin J1962 DLC, OBD2 era (1996+):** the factory 1996 Altima ECU
  pinout shows both a **K-line for generic OBD2 scan ("GST KLINE") tools**
  (~9 V) **and** CONSULT Rx/Tx/Clk lines routed to the Data Link Connector
  (CONSULT RX ~0.1 V idle, TX ~4–9 V idle, CLK ~3.5 V) [A — factory ECU
  pinout document]. So 1996+ Nissans carry DDL-family serial on the 16-pin
  DLC alongside K-line. The exact 16-pin DLC pin numbers for the Consult
  Rx/Tx/Clk lines were **not confirmed from sources** [?] — DLC pin 7 is
  the standard K-line pin [B, general OBD2 standard].
- 1999 Maxima A32 has **both** a 16-pin J1962 port and the 14-pin gray
  Consult port [B]. Per a 19-year Nissan tech answering on JustAnswer, on
  that car the 16-pin OBD2 port is intentionally limited (reads readiness
  monitors/SRTs only); the gray Consult port is the real diagnostic port
  [C — single anecdotal report, though from a claimed Nissan tech].
- From 2002 (e.g. Altima SE), community Q&A reports the Consult II
  connector became the **white 16-pin OBD-II-style** connector under the
  dash — same shape as the OBD-II DLC [C].

### 2.3 K-line (ISO 9141)

- Nissan used **K-line for generic OBD2 scan-tool communication** through
  at least the 1996–2004 transition era (factory ECU pinout explicitly
  labels a K-line for "GST" — generic scan tool — use) [A]. Community
  sources summarize this as "some vehicles up to year 2004 use OBDII
  (K-Line) for communicating with the ECU" [C].
- DDL is **not OBD2-compliant** — generic OBD2 tools cannot speak it; the
  K-line path was Nissan's OBD2-compliance mechanism on these cars [C —
  sr20-forum]. Nissan DataScan and ECUtalk default to 9600 baud for DDL
  links [B — tool documentation/community].

### 2.4 Can standard tools speak DDL?

Yes — but only Nissan-specific or DDL-aware tools [B]:

- **Nissan DataScan** (commercial), **ECUtalk** (free), **Nistune**
  (tuning), and the open-source **`cansult`** project implement the init
  sequence and command set.
- Cheap eBay "conzult"/DDL cables (FTDI + transistor level-shifting) are
  widely sold but are **hit-or-miss** per community reports [C].
- Bluetooth/Wi-Fi DDL adapters exist (e.g. consultbt-style) but are
  expensive relative to the cables, and Android app support is reported as
  flaky [C].
- ELM327/STN-family chips do **not** speak DDL natively — it requires the
  153.6 kHz host-generated clock and inverted 12 V signaling, which no
  ELM AT command set provides [B — inferred from the DDL spec; no ELM
  documentation lists DDL support].

---

## 3. Diagnostic access

### 3.1 Tool ecosystem

- **CONSULT-II** (1990s–2000s): dealer tool for DDL/K-line/CAN-era cars;
  used interchangeable ROM cards per system. Factory service manuals
  through the 2000s specify "CONSULT-II hardware and CONSULT-II software"
  for immobilizer work [B — manuals.plus factory-manual excerpts].
- **CONSULT-III plus** (current): Nissan's dealer diagnostic platform; the
  2024 CAN TSB instructs technicians to use it and to select the correct
  **"CAN type"** per model family [A]. It covers CAN diagnostics,
  NATS/NVIS key registration, and module reprogramming.
- Aftermarket tools with Nissan enhanced coverage (Autel, Launch, etc.)
  implement NATS functions — e.g. Autel MaxiCOM procedures for ECM
  replacement / key registration on a Note E12 [B —
  blog.autelshop.de walkthrough].

### 3.2 CAN-era diagnostic addressing

- **Physical addressing on the diagnostic CAN follows the OBD-II
  convention: ECM request `0x7E0` → response `0x7E8`; TCM/CVT responds at
  `0x7E9`; functional broadcast `0x7DF`** [B — 2018 Pathfinder capture
  project]. This is the standard ISO 15765-4 layout, not Nissan-specific.
- **Protocol flavor is KWP2000-style, not pure UDS:** Nissan enhanced
  diagnostics use **DiagnosticSessionControl `0x10 0xC0` followed by
  service `0x21` (readDataByLocalIdentifier)**. On the 2018 Pathfinder,
  **UDS service `0x22` is rejected with NRC `0x12`**
  (sub-function-not-supported) [B — same project]. This is a notable quirk
  for Marcus's UDS mode: a Nissan target may need `0x21`-style local-ID
  reads rather than `0x22`.
- CAN system architecture ("CAN type") varies per model and must be
  selected in CONSULT-III plus [A — TSB].

### 3.3 Immobilizer (NATS / NVIS) and seed/key policy

- NATS/NVIS key IDs are registered into the **ECM and BCM** (NATS control
  unit); max **5 key IDs** per vehicle [B — factory manual excerpts].
- Key registration **erases all existing key IDs first** — all customer
  keys must be present before starting [B].
- Registration requires CONSULT-II/III (factory manual: "must be carried
  out using CONSULT-II hardware and CONSULT-II NATS software") [B]; on
  Intelligent-Key vehicles the procedure uses the "CONSULT-III Operation
  Manual NATS-IVIS/NVIS" [B].
- An aftermarket-tool vendor document states the workflow as: read the
  **5-digit BCM PIN**, provide it to the dealer, receive a corresponding
  **4-digit password**, then perform initialization [B —
  autoequipment.com.au technical guidance]. This confirms a
  PIN→password scheme in which the password is computed by Nissan/dealer
  systems.
- **No public seed/key algorithm exists for Nissan NATS/NVIS.** This
  brief states that explicitly and invents nothing, per the project rule.
  Legitimate paths are the dealer tool chain (CONSULT-III plus, with
  Nissan's online NATS data) or aftermarket tools that have licensed the
  flow.

---

## 4. M2 mapping

| Nissan bus / protocol | M2 hardware path | Notes |
|---|---|---|
| Main CAN (500 kbps, DLC 6/14) | **HSCAN** (CAN1 or CAN2, TJA1051) | Standard ISO 15765-4; M2 logs/requests normally on non-gatewayed models [A/B] |
| AV-CAN (DLC 3/11, e.g. Leaf) | **Second HSCAN** channel | Only M2 can watch both buses at once if wired 6/14 + 3/11; watch total bus load in MITM [B] |
| AV COMM (audio↔NAVI) | HSCAN via physical tap | Not on DLC; isolated infotainment bus [B] |
| Internal CAN behind BCM gateway | HSCAN via physical tap | DLC is query-only on gatewayed models; passive sniffing at the DLC sees nothing [B] |
| K-line (1996–2004) | **LIN channel** (TJA1027, K-line-capable) | Single-wire 12 V serial; TJA1027 is K-line-compatible hardware. ISO 9141 init (5-baud / fast init) would need firmware support [B — hardware inference] |
| DDL / Consult I | **Custom — 12VIO + GPIO + PWM clock** | See below. Not reachable with stock firmware protocols [derived assessment] |
| J1850 VPW/PWM | n/a | No evidence Nissan ever used J1850 [?] |
| SWCAN (single-wire CAN) | n/a | No evidence of SWCAN on Nissan [?] |

### 4.1 Is DDL reachable with M2 hardware? (engineering assessment)

DDL's physical layer is nonstandard, but the M2 has the raw pieces
[assessment derived from the DDL spec §2.1 + M2 hardware facts from the
knowledge pack; grade C as an untested inference]:

- **Host TX (idle-low, 12 V high):** an M2 **12VIO channel** can drive
  0–12 V, matching the "12 V, idle low" requirement.
- **ECU RX (open-collector, idle-high from host 5 V pull-up):** needs a
  5 V pull-up and a level-shifted/protected input into the SAM3X (3.3 V).
  A GPIO with a divider or a protected input buffer works; do not feed
  5 V directly into a SAM3X pin.
- **153.6 kHz host clock:** the hard requirement. The SAM3X can generate
  this from a timer/PWM output pin — no stock protocol does it, so a
  custom DDL driver (bit-banged UART synced to the generated clock, or a
  timer-driven state machine) is required. The spec explicitly says the
  clock is free-running with no synchronization requirement, which
  simplifies this.
- **Framing:** 9600 8N1 LSB-first is ordinary; the `FF FF EF` init,
  inverted-byte ACKs, and `0xFF`-count streaming frames are easy in
  firmware.
- **Verdict:** DDL is *electrically* reachable with M2 hardware (12VIO +
  one GPIO in + one PWM clock out) but needs a purpose-written DDL
  driver; none of the M2's stock modes (M2RET, ELM, STN, UDS) can speak
  it, and no ELM AT command set covers it. Bench-test against a real ECU
  before trusting it. The 14-pin gray connector also needs a physical
  adapter cable (14-pin Consult → M2), or tap the ECU-side pins directly
  (see pin table in §2.2).

---

## 5. Notable quirks

1. **Query-only DLC on gatewayed models** — passive logging at the OBD-II
   port yields zero frames on (at least) the 2018 Pathfinder because the
   BCM gateway withholds raw inter-module traffic. Always send an active
   request first to determine whether you're on a gatewayed segment [B].
2. **UDS `0x22` rejected; use KWP-style `0x21`** — Nissan's enhanced
   protocol answers `0x10 0xC0` + `0x21 <local ID>`; a strict UDS scanner
   will find nothing [B]. Marcus's UDS mode should offer a KWP-`0x21`
   fallback for Nissan targets.
3. **DDL init may need to be sent twice** — documented in the factory
   spec and confirmed by the open-source implementation; a DDL driver
   must retry init rather than failing on the first `FF FF EF` [B].
4. **No ECU-side DDL stream watchdog** — if the host stops sending
   without the stop byte, the ECU streams indefinitely (idle timeout is
   >30 min). Always send the stop byte (`0x30` per spec / `0x03` per
   cansult — conflict unresolved, try both) [B].
5. **Two-port cars (late 90s)** — e.g. 1999 Maxima: the 16-pin OBD2 port
   is deliberately limited (readiness monitors only); real diagnostics
   live on the 14-pin gray Consult port. A generic scan tool "works" but
   shows little [C].
6. **TSB-excluded models** — 2023–24 Ariya, 2022–24 Pathfinder R53,
   2021–24 Rogue T33, 2020–24 Sentra B18 are excluded from the legacy CAN
   diagnosis TSB, implying a newer network architecture (possibly CAN FD
   or a different gateway layout). Flagged as open research [A for the
   exclusion, ? for the cause].
7. **1 Mbit/s vs 500 kbps** — Nissan's own Tech News article claims
   1 Mbit/s while all community captures show 500 kbps; treat the
   article's figure as suspect [A vs B, unresolved].
8. **IPDM E/R as network member** — the Intelligent Power Distribution
   Module is a CAN node and frequently a terminating module; CAN
   electrical-load signals route BCM → ECM *via* IPDM E/R [A/B].
9. **ECU-side DDL pins are not standardized** — RX/TX/CLK pin numbers
   differ per ECU family (see §2.2 table); never assume one pinout [B].
10. **NATS wipes all keys on registration** — any key-registration
    procedure (dealer or aftermarket) erases every registered key ID
    first; a half-finished procedure can leave the customer with zero
    working keys [B].
