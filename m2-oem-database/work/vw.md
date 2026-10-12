# Volkswagen Group (VW / Audi / SEAT / Skoda) — In-Vehicle Networks & Diagnostic Access

Research for the M2 OEM vehicle database (v1.1 expansion). Every factual claim
carries a quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, VCDS/Ross-Tech docs, well-documented
reverse-engineering, VW SSP training docs) · **C** = single anecdotal report.
Conflicts are reported, not silently resolved.

Research date: 2026-10-06.

---

## 1. Bus architecture

### 1.1 The CAN networks (PQ era, ~2005–2015)

VW's Self-Study Programme training material for the 2006–2010 Passat (VW SSP
872802, via a training-course PDF) describes **five main CAN networks** [B]:

- **Powertrain CAN** — engine, transmission, ABS
- **Instrument Cluster CAN**
- **Diagnosis CAN** — DLC to gateway
- **Convenience CAN** (also called comfort CAN) — windows, locks, doors
- **Infotainment CAN** — radio, navigation

Additionally there are **private CAN networks not connected to the gateway**
(e.g. ABS-internal, headlamp range control) [B]. Sensors and actuators hang off
LIN sub-buses instead: wiper motor + rain/light sensor, alarm horn, rear door
modules (VIN-dependent), steering wheel controls [B].

### 1.2 Bitrates and the MQB changeover

- Audi A8L SSP287 (2004, MLB-era): drive-system CAN **500 kbit/s**, convenience
  CAN **100 kbit/s** [B].
- 2017 Tiguan SSP553 (MQB): **"All CAN bus systems have a transmission speed of
  500 kbit/s"** — powertrain, running gear, convenience, infotainment, diagnosis
  CAN. LIN at 19.2 kbit/s. MOST150 (fibre-optic, 150 Mbit/s) for premium audio
  [B].
- BITRATE CONFLICT: one forum thread cites a leaked VW doc putting the
  infotainment bus at 100 kbps, but the same poster measured **500 kbps** on the
  wire and a GTI owner confirmed convenience + infotainment at 500 kbps on MQB
  [C both]. A separate forum reply claims "500K on PQ35, 1Mbit/s on MQB" [C],
  which conflicts with the Tiguan SSP's "all 500 kbit/s". Treat MQB-era buses as
  500 kbps (measured/SSP-backed); the 1 Mbit/s claim is unverified.
- Practical read: PQ-era convenience CAN was 100 kbps; MQB moved everything to
  500 kbps [B for the SSP data points; the generalization is inferred].

### 1.3 The gateway J533 and the DLC

- **J533 — Data Bus On Board Diagnostic Interface** — is the central gateway
  between all buses. Diagnostic address word **0x19** ("19-CAN Gateway" in VCDS)
  [B — Ross-Tech forum scans, VW wiring docs].
- The DLC exposes **one CAN pair: pins 6/14**, which is the diagnosis CAN to the
  gateway. **Correction to the research brief's assumption:** VW does *not* put
  comfort or infotainment CAN pairs on the DLC — those buses are gateway-internal
  and only reachable by tapping behind J533 [B — no source found showing a second
  CAN pair on a VW DLC; the DLC pinout is consistently 6/14 + K-line].
- DLC pin 7 = K-line (retained on early CAN-era cars for some modules) [B].
- On the 2011 Jetta "low" electrical architecture, the J533 function was moved
  *inside* the J519 (vehicle electrical system control module) housing but
  remains a logically separate module at address 0x19 [B — VW SSP 872802].
- **Gateway Installation List**: VCDS can query J533 (~3 seconds) for the list of
  installed modules and their status; the list is edited through Gateway Coding.
  A module physically present but missing from the installation list (or vice
  versa) generates DTCs [B — Ross-Tech VCDS tour docs].
- Gateway failure modes are systemic: a damaged J533 can collapse the whole
  network or fail to send sleep commands (parasitic drain) [C — trade-press
  troubleshooting article].

### 1.4 Platform differences

- **PQ25/PQ35/PQ46** (~2005–2015): the five-bus layout above; convenience CAN at
  100 kbps on some models; MOST (25 Mbit/s) for premium infotainment [B].
- **MQB** (~2012–2020): consolidated to 500 kbps across buses per the Tiguan SSP;
  MOST150 on premium audio [B].
- **MLB** (Audi longitudinal): same gateway concept; the opendbc `vw_mlb.dbc`
  carries 145 messages (platform-level, grade B) [B — local opendbc clone].
- **MQB Evo / MEB** (2020+): SFD protection era (see §3). opendbc `vw_mqbevo.dbc`
  has 136 messages in classic-CAN DBC format [B]. CAN FD on MQB Evo: one forum
  poster mentions CAN-FD DBCs for MQB cars assumed to be MQB Evo [C] —
  **unconfirmed** in this pass; flagged as an open item with direct M2
  consequences (TJA1051 is CAN 2.0 only).

### 1.5 opendbc VW coverage (local clone, grade B)

| DBC | Messages | Platform |
|---|---|---|
| vw_pq.dbc | 86 | PQ |
| vw_mqb.dbc | 113 | MQB |
| vw_mqbevo.dbc | 136 | MQB Evo |
| vw_mlb.dbc | 145 | MLB |

Platform-level, not model-level; comma.ai's ADAS-driving subset [B].

---

## 2. Legacy: K-line era

- **K-line**: DLC **pin 7** (bidirectional), **L-line pin 15** (optional,
  unidirectional wake-up). 10.4 kbps UART 8-N-1, 12V idle / 0V active [B —
  SparkFun/Digi-Key OBD-II reference, multiple protocol summaries].
- **KWP-1281**: VAG-proprietary diagnostic protocol, roughly **1995–2006**.
  5-baud init; documented ECU addresses include 0x01 (engine), 0x03 (ABS),
  0x08 (HVAC), 0x17 (instruments), 0x19 (gateway), 0x46 (central convenience)
  [B — community KWP-1281 protocol doc with Arduino implementation].
- **KWP2000 (ISO 14230)**: fast init (~500 ms), up to 255-byte messages;
  common on 2003+ pre-CAN VAG vehicles [B].
- CAN transition: Ross-Tech notes 2004 as the first year an aftermarket tool
  needed a **direct CAN connection** for new VW/Audi models [B]. Early CAN-era
  cars often kept the K-line on DLC pin 7 for specific modules (owner reports of
  K-line faults on CAN-era Golfs) [C].
- Rule of thumb: pre-~2004 VAG ≈ K-line (KWP-1281/KWP2000); 2004+ = CAN with
  K-line remnants; all-CAN well before the 2008 mandate [B/C].

---

## 3. Diagnostic access

### 3.1 VCDS (Ross-Tech) — the tool ecosystem reference

- Windows-based VAG diagnostic software; 2000: first affordable full-function
  VAG tool [B — ross-tech.com].
- 2002: first aftermarket tool with 7-digit SKC codes and proprietary KWP-2000
  modes [B].
- 2004: first aftermarket tool with direct-CAN diagnostics [B].
- 2008: first aftermarket UDS/ODX/ASAM support (Audi B8 platform) + Gateway
  Coding Assistant [B].
- VCDS module address convention (hex): 01 Engine, 02 Auto Trans, 03 ABS, 05
  Acc/Start Auth, 08 Auto HVAC, 09 Cent. Elect., 15 Airbags, 16 Steering wheel,
  17 Instruments, **19 CAN Gateway**, 42/52/62/72 Door Elect, 46 Central Conv.,
  53 Parking Brake, 55 Headlight Range, 56 Radio, 5F Information Electr.,
  6C Back-up Cam [B — Ross-Tech forum auto-scans].
- VCDS also supports generic OBD-II and long coding; it remains the
  enthusiast reference for pre-SFD vehicles [B].

### 3.2 ODIS — the dealer tool

- **ODIS (Offboard Diagnostic Information System)**: VW Group dealer software;
  ODIS-S (Service) for diagnostics, ODIS-E (Engineering) for flashing/
  parametrization [B — vendor guides].
- Hardware: VAS 5054A / VAS 6154 interfaces [B].
- **GEKO**: VW's online account system gating security access — immobilizer/key
  programming, component protection removal, control-unit recoding. Application
  ~$100 plus per-brand subscriptions; identity/business verification with 1–2
  week review [C — forum/vendor accounts; treat pricing as approximate].
- SFD fees on 2024+ models reported as ~$16/vehicle or $128/year [C — single
  vendor buying guide].

### 3.3 SFD — Schutz Fahrzeugdiagnose (Vehicle Diagnostic Protection)

This is the VW equivalent of the Stellantis Secure Gateway. Read carefully.

**What it is.** An additional security layer requiring authorization between the
vehicle and the manufacturer, introduced **2020 with the MQB37W (Golf 8)** and
rolled out across MQB Evo and MEB: Golf 8, Skoda Octavia IV, Seat Leon IV, Audi
A3 8Y, Q4, ID.3, ID.4, Skoda Enyaq, plus VW Commercial/Bentley/Lamborghini
[ B — Autel/VW vendor docs, consistent across sources].

**What it blocks.** Writing services on protected control units: **adaptations,
coding, parametrizations** [B]. Commonly protected ECUs (community SFD doc
[ B ]): 19 Gateway, 09 BCM/central electrics, 17 instrument cluster,
5F infotainment, A5 driver-assist camera, 44 steering assist, 13 ACC,
76 park assist, 4B lighting — applicability is per specific coding/adaptation,
not blanket per ECU.

**What it does NOT block.** Per VW's own SFD manual for independent workshops
[B]: normal **reading services** (e.g. event-memory/DTC readout) are not
SFD-protected, and **flashing/update programming via bootloader data strings is
explicitly unaffected** — SFD guards diagnostic *writes*, not reads or
reprogramming. (This is a notable difference from casual "SFD blocks everything"
claims.)

**Two stages** (VW SFD manual [B]): Stage 1 = access protection of protected
diagnostic objects + per-user verifiability of access (who changed what, when).
Stage 2 = end-to-end tamper protection of diagnostic data between VW IT backend
and control units. Backend access requires strong authentication (2FA: PKI
cards, SecurID, or authenticator apps) [B].

**SFD2 (2024+).** A second-generation scheme appears on 2024+ models; community
guidance warns to confirm **SFD2 support for the specific VIN**, not just SFD v1,
before buying a tool [B — community vwcoding docs].

**Legitimate unlock paths** (documented, no invention):
1. **ODIS + GEKO**: dealer path; manual SFD activation in ODIS Service after
   selecting the control unit [B].
2. **Autel**: in-device token purchase (OEM Authorization app); one 24-hour
   token covers all modules of one VIN; 1-year subscriptions also sold [B —
   Autel vendor docs].
3. **Topdon / Thinkcar / Launch X431**: manual SFD activation flow in the tool
   [B — vendor blogs].
4. **OBDeleven**: reported as the first third-party tool authorized by VW for
   real-time SFD unlock; unlock lasts ~90 minutes per session [C —
   QuattroWorld; vendor-adjacent claim].
5. Third-party token services (e.g. credit-based sites generating one-time
   SFD challenge responses, ~€25/25 credits) are **reported in vendor blogs**
   [C] — documented here as observed community practice, not endorsed, and
   their authorization legitimacy is unverified.

**What is NOT documented (deliberately).** No SFD cryptographic bypass, no
seed/key algorithm, and no method to defeat SFD2 was found in public sources.
None is invented or reproduced here. The pre-SFD system used **5-digit login
codes** (e.g. 19249, 31347 seen in Golf 7 coding guides [C]); SFD replaced that
mechanism from 2020.

### 3.4 Seed/key policy

**No public VW Group seed/key (UDS 0x27) algorithm was found.** None is invented
or reproduced. Immobilizer/key functions go through GEKO-gated ODIS; component
protection is dealer/GEKO-only.

---

## 4. M2 hardware → VW bus mapping

| VW bus | DLC pins | M2 hardware path |
|---|---|---|
| Diagnosis CAN (6/14) @ 500 kbps | 6 / 14 | CAN0 or CAN1 (TJA1051) — primary diagnostic path via J533 gateway |
| Powertrain CAN @ 500 kbps | gateway-internal | Same DLC pair reaches it through the gateway's routing |
| Convenience CAN (100k PQ / 500k MQB) | gateway-internal | **Not on the DLC** — requires tapping behind J533 |
| Infotainment CAN / MOST | gateway-internal / optical | Not on the DLC; MOST is fibre-optic — no electrical access at all |
| K-line (pre-CAN / remnants) | 7 | M2 K-line transceiver (TJA1027) — covers KWP-1281/KWP2000/ISO 9141 |
| LIN sub-buses (doors, sunroof, wipers, steering wheel) | not on DLC | M2 LIN1/LIN2 (TJA1027) if tapped at the module |
| CAN FD (MQB Evo, unconfirmed) | 6 / 14 | **Out of scope if present** — TJA1051 is CAN 2.0 only |

VW diagnostic strategy for M2 firmware:
- **OBD-II port**: UDS/KWP diagnostics through the gateway on 6/14; pre-SFD
  vehicles allow coding/adaptations with the right security access, SFD vehicles
  (2020+) require an unlock for any write (see §3.3).
- **Passive logging**: the DLC's diagnosis CAN carries gateway-routed traffic —
  a silent M2 logger sees what J533 forwards, not raw internal buses [B —
  inferred from the gateway architecture].
- **MITM**: injecting frames toward the vehicle through the DLC means going
  through J533's routing; on SFD vehicles, protected writes additionally need
  SFD authorization [B/C — inferred from the two mechanisms].

---

## 5. Notable quirks

1. **SFD does not block flashing.** The VW SFD manual explicitly excludes
   bootloader-based flashing/update programming from SFD protection [B] — so an
   M2-based programming mode targeting VW ECUs is not SFD-gated at the flash
   step (the *diagnostic session* to reach it still follows normal rules).
2. **SFD2 (2024+)** is a separate scheme — tool compatibility must be confirmed
   per VIN [B].
3. **DLC = one CAN pair.** Unlike Stellantis (three pairs on the DLC), VW
   exposes only the diagnosis CAN on 6/14. Everything else is behind J533 [B].
4. **Convenience CAN bitrate conflict**: 100 kbps in PQ-era docs vs 500 kbps
   measured on MQB — set the rate per platform, don't assume [B/C].
5. **MQB "1 Mbit/s" claim** [C] conflicts with the Tiguan SSP's "all 500 kbit/s"
   [B] — unverified; treat 500k as the working value.
6. **Gateway Installation List**: coding must reflect physically installed
   modules or DTCs result; VCDS's ~3-second query is the reference check [B].
7. **K-line remnants**: early CAN-era VWs kept pin 7 K-line for some modules —
   a dead K-line can break diagnostics on cars that are otherwise CAN [C].
8. **MOST is optical**: premium infotainment audio runs on fibre — electrically
   invisible to any CAN tool [B].
9. **Private CANs**: some modules (ABS-internal, headlamp range) sit on private
   CANs not connected to J533 at all — invisible at the DLC by design [B].
10. **CAN FD on MQB Evo unconfirmed** [?] — if confirmed, those buses are out of
    M2 scope (TJA1051 = CAN 2.0 only).

---

## Sources consulted

- VW SSP 872802 (2006–2010 Passat network topology, via datarunners training
  PDF) — five CAN networks, private CANs, LIN nodes [B]
- VW SSP553 (2017 Tiguan electrical system) — all-CAN-500k, LIN 19.2k, MOST150,
  J533 role [B]
- Audi SSP287 (2004 A8L electrical components, via vwts.ru) — J533 gateway
  versions, 500k drive CAN / 100k convenience CAN [B]
- Audi data-bus technologies SSP (via vwts.ru) — CAN overview incl. MOST,
  diagnosis CAN [B]
- 2011 Jetta SSP excerpt (via datarunners) — high/low electrical architectures,
  J533-inside-J519 [B]
- ross-tech.com — VCDS history/firsts (2000–2008) [B]
- forums.ross-tech.com / VCDS Tour (via scribd) — Gateway Installation List,
  module address convention [B]
- VW SFD manual for independent workshops (EN_SFD-Manual_for_UMB, via
  flashdaten.2y.net) — SFD stages, scope, 2FA, 2020/MQB37W introduction [B]
- Autel / Topdon / VXDIAG vendor blogs — SFD unlock flows, token model,
  protected-module lists [B]
- kanaduchi/vwcoding docs/sfd.en.md (GitHub) — SFD2 (2024+), per-ECU protection
  table [B]
- QuattroWorld — OBDeleven VW-authorized SFD unlock report [C]
- rxtx4816/obd-kkl-kw1281-arduino-tripcomputer (GitHub) — KWP-1281 protocol doc,
  ECU addresses [B]
- SparkFun/Digi-Key OBD-II reference — K-line/L-line pins and levels [B]
- golfmk7.com — infotainment/convenience CAN bitrate measurements [C]
- nefariousmotorsports.com — PQ35 vs MQB CAN discussion [C]
- Local opendbc clone — vw_pq/vw_mqb/vw_mqbevo/vw_mlb DBC message counts [B]

## Open items for the database build

- CAN FD on MQB Evo: confirm or deny (determines M2 scope on 2020+ VW) [?]
- VW UDS physical CAN IDs per module family (ASAM/ODX-derived; not enumerated
  here — not verified in this pass) [?]
- Per-model gateway part numbers and installation-list coding details [?]
- MEB platform bus layout (ID.3/ID.4/Enyaq) — SFD-covered but bus topology not
  researched [?]
