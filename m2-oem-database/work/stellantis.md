# Stellantis (Chrysler / Dodge / Jeep / RAM / Fiat / Alfa Romeo) — In-Vehicle Networks & Diagnostic Access

Research brief for the M2 OEM vehicle database. Every factual claim carries a quality grade:
**A** = factory documentation or verified capture · **B** = reputable community source (opendbc, trade press, well-documented RE) · **C** = single anecdotal report.
Grades appear inline as [A], [B], [C]. Unverified items are marked [?].

---

## 1. Bus architecture

### 1.1 The three CAN networks (CAN era, ~2004/05 → present)

Chrysler-group vehicles use three distinct CAN networks. Pin assignments below are from an actual FCA STAR service publication (FCA US LLC, v4.2, 02/06/2017, Jeep case S1508000235) [A]:

| Network | OBD-II (DLC) pins | Bitrate | Role |
|---|---|---|---|
| CAN-C1 | 6 (H) / 14 (L) | 500 kbps [B] | Powertrain/chassis high-speed CAN (SAE J2284) [A for pins; B for rate] |
| CAN-C2 | 12 / 13 | 500 kbps [?] | Second high-speed CAN (some platforms; e.g. Alfa/Fiat "second high-speed CANBUS" per aftermarket vendors [C]) |
| CAN-BH | 3 / 11 | not confirmed [?] | Body/harness CAN |

Notes:
- All three networks use 120 Ω terminal resistors; with the battery disconnected, ~60 Ω measured across any of the three pairs at the DLC indicates electrical continuity [A].
- CAN-C1/C2/CAN-BH enter sleep ~10–12 s after key-off and wake when a door transitions closed→open [A].
- CAN-C is the 500 kbps Class-C powertrain/chassis bus (SAE J2284) [B]; 11-bit identifiers are the norm on Chrysler CAN [B] (Colorado State TUCRRC Dodge CAN research, based on Dodge bodybuilder wiring diagrams).
- Wire colors on CAN-C (Ram, per TUCRRC): CAN-C(+) white/light-green stripe, CAN-C(−) white/light-blue stripe [B].

### 1.2 CAN-IHS ("Interior High Speed" / comfort CAN)

- CAN-IHS runs at **125 kbps** and is the low-speed "comfort" bus for interior/body modules (despite the "High Speed" name — it is the *slower* bus relative to CAN-C's 500 kbps) [B].
- Chrysler's own service literature classifies IHS in SAE Class B (10–125 kbps), alongside J1850 and GM/Ford medium-speed CAN [B] (Fender Bender trade-press training article).
- In the pre-SGW architecture, the scan tool did **not** talk to interior buses directly: it communicated with the Front Control Module / Central Gateway (FCM/CGW) over a separate "Diagnostic CAN-C" line at the DLC, and the FCM/CGW bridged to CAN-B, CAN-C, etc. The FCM/CGW also holds the Vehicle Build Configuration (VBC) used for the network-topology display [B].

### 1.3 LIN sub-buses

- Chrysler uses LIN sub-buses under body modules — e.g. the Cabin Compartment Node (CCN / instrument cluster) acts as LIN master for the multifunction (turn-signal) switch slave; the CCN then forwards onto CAN/IHS to the TIPM [B] (Auto Service World trade article). LIN master reference on the wire is the usual 7–12 V [B].
- Directly relevant: these are plain 19.2 kbps-class LIN networks — no gateway tricks at the LIN level [B].

### 1.4 Model-year evolution (network generations)

- **1988 – ~1998: CCD bus** — Chrysler Collision Detection, proprietary 2-wire bus at 7812.5 bps. First full-vehicle multiplexing on 1988 New Yorker / Dodge Dynasty (earlier: 1981 Imperial cluster) [B].
- **~1999 – ~2004/05: PCI bus** — replaced CCD; single-wire SAE J1850 VPW (~10.4 kbps) [B]. One owner-community summary gives "CCD → 1999, PCI 1999–2005, CAN 2005 →" [C] — treat exact cutover years as model-dependent.
- **~2004/05 – 2008: CAN transition** — CAN-C/CAN-IHS/CAN-B roll out model by model; by the 1 Jan 2008 US mandate every new vehicle uses ISO 15765-4 CAN on pins 6/14 for OBD-II [B].
- **2018 → present: SGW era** — Secure Gateway Module added (see §3). The SGW supersedes the old FCM/CGW as the DLC-facing gatekeeper and adds authentication [B].

---

## 2. Legacy protocols

### 2.1 J1850 VPW / PCI bus
- Chrysler's PCI bus is SAE J1850 VPW: single wire on **OBD-II pin 2**, ~10.4 kbps, idle low, active high ~7–7.5 V (half charging-system voltage) [B].
- Typical wire color: yellow with purple stripe (or vice versa) [B].
- Used for both inter-module communication and scan-tool/flash functions until CAN replaced it [B].

### 2.2 CCD (Chrysler Collision Detection)
- Two-wire bus, 7812.5 bps; DLC pins **3 (CCD+) / 11 (CCD−)** per compiled pinout lists [C]. (Note: pins 3/11 were later reused by CAN-BH — do not assume; check the model year.)
- Pre-OBD-II-era module communication; of historical interest only for 1988–~1998 vehicles [B].

### 2.3 SCI — Chrysler's proprietary serial (SAE J2610)
- SCI = Serial Communication Interface, Chrysler-proprietary UART-based protocol used for PCM/TCM diagnostics and **flash reprogramming** in the 1990s–early 2000s [B].
- Multiple SCI channels existed: SCI A Engine (RX/TX), SCI A Trans (RX/TX), SCI B Engine (RX/TX). Compiled pinout lists place them on DLC pins 6, 7, 9, 12, 14, 15 depending on channel/direction [C — pin assignments vary by model year; verify per vehicle].
- Bitrates cited: 7812.5 bps, 62.5 kbps, and 125 kbps depending on channel [C].
- **M2 implication:** the M2 has no SCI hardware. SCI is a 0–12 V UART-ish serial; it is not J1850, not K-line, not LIN. Treat pre-CAN Chrysler powertrain flashing via SCI as out of reach for stock M2 firmware [B/C].

### 2.4 K-line (ISO 9141-2 / ISO 14230)
- Chrysler also used ISO 9141-2 K-line on **pin 7** (L-line pin 15 optional), 10.4 kbps, on many 1996–~2004 models alongside PCI/SCI [B].

---

## 3. Diagnostic access — the Secure Gateway Module (SGW)

This is the highest-value section of this brief. Read carefully.

### 3.1 What the SGW is
- Starting with **2018 model-year vehicles** (one aftermarket vendor doc says "since 2017" [C]; overwhelming consensus across trade press, tool vendors, and owner forums is **2018+** [B]), most FCA/Stellantis vehicles — Chrysler, Dodge, Jeep, Ram, Fiat, Alfa Romeo — ship with a Secure Gateway Module [B].
- The SGW is a **CAN firewall between the OBD-II port and the vehicle's internal networks**. With the SGW in place, only authenticated/authorized messages are received and acted upon; unauthenticated traffic from the DLC is dropped [B] (described nearly identically by Autel/Bosch/Innova press material and owner-forum explainers).
- Commonly cited motivation: the 2015 remote compromise of a Jeep Grand Cherokee (Miller/Valasek) [C — widely repeated, plausible, but an aftermarket-forum attribution, not an FCA statement].

### 3.2 Exactly what it blocks (and what still works)
Multiple independent sources agree [B]:
- **Still works through the SGW with any tool:** reading DTCs, reading live data streams, reading version/identification info.
- **Blocked without authentication:** clearing DTCs, bi-directional controls / active tests / actuations, calibrations, relearns (e.g. TPMS sensor-ID relearn, oil-reset on some models), module programming.
- FCA's own framing (via Autel's published guideline): the SGW was "developed not to restrict access to diagnostic *data* but rather to restrict the ability of non-registered and non-authenticated users to perform *intrusive diagnostics* such as bi-directional controls" — but in practice **even DTC clearing is denied** [B].

### 3.3 Legitimate access path #1 — AutoAuth (commercial tools)
- FCA/Stellantis appointed **AutoAuth** (Automatic Authentication Authority) as the broker: an approved scan tool with internet access authenticates the user/shop against FCA servers and receives credentials to unlock the SGW [B].
- Pricing (from LAUNCH/TOPDON-published FCA guidance; [B], vendor-published but consistent across vendors):
  - Shop account: **$50/year**, covers up to 6 users (owner included); +$2/year per additional user; max 100 users / 100 tools per shop.
  - Technician accounts: free (must be attached to a shop account).
  - Payment goes to AutoAuth directly.
- Coverage: US, Mexico, Canada (Europe via Fiat's technicalinformation portal) [B].
- Approved/certified tools include: Autel tablets (FCA-approved June 2020), Bosch ADS 325/625 (certified, needs ADS 4.0+ software), Innova SDS43, TOPDON Phoenix/ArtiDiag series, LAUNCH, THINKCAR [B].
- Without the unlock, tools report only version info / read DTC / read data stream [B].

### 3.4 Legitimate access path #2 — dealer tool
- The FCA dealer tool is **wiTECH 2.0**; it authenticates to the SGW natively [B] (owner-forum reports; consistent with Bosch's note that "until now, only the FCA U.S. dealership diagnostic tool has supported scan-tool authentication" [B]).

### 3.5 Legitimate access path #3 — physical bypass (owner's own vehicle)
Aftermarket vendors sell hardware that physically removes the SGW from the path [B/C — vendor product pages; mechanism descriptions are consistent]:
- **12+8 bypass cable**: plugs into the STAR connector (the CAN junction blocks behind/around the SGW location) and routes the internal CAN pairs straight to the OBD-II device, bypassing the gateway. Used with AlfaOBD, Autel 12+8 adapter, OBDSTAR, Xhorse, or Advanced Diagnostics ADC2011 cable + Smart Pro [B].
- **SGW bypass modules** (e.g. ZAutomotive, ~$69): unplug the SGW module, plug the bypass block in its place; the OBD-II port then has direct bus access [C — vendor claim]. ZAutomotive's own fitment notes: covers 2018–2023 Durango and 2018–2022 Grand Cherokee explicitly, and "any 2018+ FCA vehicle **except** Cherokee L/WL or Grand Cherokee L/WL" [C — vendor's words; WL-platform exceptions noted].
- SGW physical locations vary: behind the OBD-II port, behind the instrument cluster, behind the radio, behind the glovebox [C].
- Practical caveat from owner forums [C]: with a bypass installed, the dealer's wiTECH cannot find the gateway to unlock — **remove the bypass and restore the SGW before dealer visits**.

### 3.6 What is NOT documented (deliberately)
- **No seed/key algorithm, no SGW authentication bypass, and no proprietary unlock sequence is documented here.** None was found in public sources during this research, and none should be invented. The legitimate paths are AutoAuth (§3.3), wiTECH (§3.4), or physical bypass on the owner's own vehicle (§3.5).
- UDS security-access (service 0x27) seed/key algorithms for FCA ECUs are not public [? — not found; do not guess].

### 3.7 UDS usage on FCA vehicles
- FCA diagnostics run **UDS (ISO 14229) over CAN** with 11-bit IDs [B].
- Concrete in-the-wild example: the JL Wrangler community reverse-engineering project documents horn control via **CAN ID 620 + UDS service 0x2F** (InputOutputControlByIdentifier) and idle-speed control via UDS [B/C — well-documented community project, single-forum source].
- Standard emissions OBD-II (SAE J1979: modes 0x01–0x0A) on pins 6/14 works through the SGW — reads are not blocked [B].

---

## 4. M2 hardware → Stellantis bus mapping

| Stellantis bus | DLC pins | M2 hardware path |
|---|---|---|
| CAN-C1 (500k) | 6 / 14 | M2 CAN0 or CAN1 (native SAM3X HSCAN) |
| CAN-C2 (500k) | 12 / 13 | M2's other native CAN controller |
| CAN-BH (body) | 3 / 11 | **Not directly reachable with stock M2 hardware** — both native CAN controllers are spoken for by C1/C2; the M2's MCP2515 is wired to the TH8056 single-wire transceiver, not a standard CAN pair. Would need external CAN transceiver on SPI. |
| CAN-IHS (125k) | not on DLC (interior) | Reachable only via gateway or direct tap; electrically standard CAN if tapped |
| J1850 VPW / PCI (pre-CAN) | 2 | M2 J1850 hardware (pins 49–54; VPW mode) |
| K-line ISO 9141 (pre-CAN) | 7 | M2 K-line transceiver (TJA1027) |
| LIN sub-buses | not on DLC | M2 dual LIN (Serial1/Serial2) if tapped at the module |
| SCI (J2610, pre-CAN PCM/TCM) | various (see §2.3) | **No M2 hardware support** — proprietary serial, not J1850/K-line/LIN |

SGW-era diagnostic strategy for M2 firmware:
- **OBD-II port on 2018+ vehicles:** M2RET-style logging and read-only diagnostics (DTC read, live data, UDS 0x19/0x22 reads) work through the SGW. Anything write-like — DTC clear (0x14), routine control (0x31), IO control (0x2F), write-by-identifier (0x2E), programming/flashing — is blocked at the gateway [B].
- **MITM mode on SGW vehicles:** passive bridging/logging of DLC-visible traffic works; injecting or modifying frames toward the vehicle through the OBD-II port will be dropped by the SGW's authentication filter. True MITM on 2018+ FCA requires either the physical bypass (§3.5) or tapping buses behind the SGW [B/C — inferred from the firewall mechanism; the "writes are blocked" part is [B]].
- **Pre-SGW vehicles (pre-2018):** the DLC's CAN-C1 (6/14) is directly usable for full diagnostics; CAN-C2 (12/13) and CAN-BH (3/11) are also on the DLC per the FCA STAR doc [A].

---

## 5. Notable quirks

1. **Read-only logging is SGW-immune.** The SGW filters *intrusive* traffic, not eavesdropping. A silent CAN logger on DLC 6/14 sees everything the gateway forwards — which, on the diagnostic CAN, is the gateway's bridged traffic, not necessarily the raw internal buses [B for the block/allow split; C for exactly which frames the diagnostic CAN carries vs. internal buses].
2. **Two CAN pairs on the DLC is normal for FCA.** 6/14 (CAN-C1) plus 12/13 (CAN-C2) plus 3/11 (CAN-BH) — a generic OBD-II scanner only uses 6/14; the extra pairs are FCA-specific [A for pins].
3. **The 60 Ω quick-check works per pair.** Battery disconnected, ~60 Ω across 6/14, 12/13, or 3/11 each indicates that network's termination is intact [A].
4. **Bypass-vs-dealer conflict.** A physical SGW bypass must be removed before dealer service; wiTECH looks for the gateway to unlock and fails against a bypassed bus [C].
5. **AutoAuth is per-shop, not per-tool-hacker.** There is no documented DIY path to AutoAuth credentials for a homebrew tool like the M2 — it requires an approved commercial scan tool plus paid shop membership [B]. Plan M2 Stellantis work around read-only access or the physical bypass.
6. **opendbc coverage is thin but real for FCA.** comma.ai opendbc lists Ram 1500 2019–24 (ACC, upstream support), Ram 2500 2020–24, Ram 3500 2019–22, and openpilot docs note Chrysler/Jeep/Ram with LaneSense + ACC as "likely" supported [B]. The JL Wrangler community project (jlwranglerforums master thread) maintains a decoded message spreadsheet, SavvyCAN DBCs (github.com/darksotmoon/jlcan), and Pi-based scripts (github.com/rstellhorn/jeepjlpowernetscripts) — the best public FCA CAN database found in this pass [B].
7. **Naming trap: "CAN-IHS" is the slow bus.** Interior *High* Speed is 125 kbps — slower than CAN-C's 500 kbps. Don't let the name mislead bitrate assumptions [B].
8. **CCD pins 3/11 were recycled.** Pre-1999 CCD used DLC 3/11; later CAN-BH reused the same pins. Year/model determines which protocol is actually on those pins [B for CCD era, A for CAN-BH pins — the overlap is the quirk].

---

## Sources consulted

- FCA US LLC STAR Online Publication v4.2 (02/06/2017), Jeep case S1508000235 — via tsbsearch.com [A]
- Colorado State Univ. TUCRRC, "Dodge CAN Messages" (J. Daily) — engr.colostate.edu [B]
- Fender Bender trade articles: "Chrysler CAN Network Diagnostics", "All Aboard Chrysler's PCI Bus", "Network Communication Diagnostics" [B]
- Auto Service World: "Diagnostic Tips for Chrysler's LIN-Bus Network" [B]
- AutoAuth/FCA guidance as published by LAUNCH / TOPDON / Autel (obdii365.com) [B]
- Bosch / Innova / Autel press material on SGW certification (autoserviceworld.com, PR Newswire) [B]
- ZAutomotive SGW bypass product page; GMS/Alfa Romeo forum thread [C]
- jlwranglerforums.com: JL CAN-bus reverse-engineering master thread; SGW bypass threads [B/C]
- ramforum.com: SGW bypass cable threads, AlfaOBD usage [C]
- comma.ai opendbc docs/CARS.md; openpilot docs/CARS.md [B]
- allpinouts.org / yumpu.com compiled OBD-II pinout docs [C]
- forum.arduino.cc Jeep PCI-bus thread [C]

## Open items for the database build
- CAN-BH and CAN-C2 bitrates: pins confirmed [A], bitrates not confirmed in this pass [?].
- Per-model SGW introduction years (which 2018 models first; the "2017" vendor claim unresolved) [?].
- FCA UDS physical addressing IDs per model family (openpilot/opendbc + JL DBCs are the next harvest target) [?].
- Whether DLC 6/14 on SGW vehicles carries raw CAN-C or only gateway-bridged diagnostic traffic — affects what a passive M2 logger actually sees [?].
