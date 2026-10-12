# Bus architecture by make

## General Motors (Chevrolet / Buick / GMC / Cadillac)

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| High-Speed GMLAN | 500 kbps | 6, 14 | 2 | 2004+ (full by 2008) | [A] | Powertrain/chassis bus. 120-ohm terminators at each end; ~60 ohms across DLC 6/14 (key off) is the standard health check. |
| Mid-Speed GMLAN | 95.2 kbps | 3, 11 | 2 | 2004+ | [A] | Infotainment (display, navigation). BITRATE CONFLICT: ACDelco says 95.2 kbps [A]; GM Enhanced Diag spec excerpt says 'approximately 95.2 or 125 kbps' [B] — treat as model-dependent. |
| Single-Wire (Low-Speed) GMLAN | 33.33 kbps | 1 | 1 | 2004+ | [B] | Per GMW3089. 83.33 kbps high-speed mode used for flashing (transceiver must switch, not just the CAN bitrate). Sleeping nodes REQUIRE high-voltage wake-up before they answer normal traffic. |
| Second High-Speed GMLAN (select models) | 500 kbps | 12, 13 | 2 | model-dependent | [C] | CONFLICT: a 2010 Camaro reportedly has a second HS bus on DLC 12/13 [C], but the 2002 Intrepid pinout labels 12/13 'LSFT H/L' (discretionary) [B]. Pin 12/13 usage varies by model/year — verify per vehicle. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| Class 2 / SAE J1850 VPW | 10.4 kbps | 2 | 1996–~2007 (gradual, model-dependent) | [B] | VPW uses pin 2 ONLY (pin 10 is the J1850 PWM negative leg — Ford, not GM). Phase-in of GMLAN began 2004; 2005 Colorado/Yukon still VPW per owner reports; complete by the 2008 federal CAN mandate. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 (TJA1051, HSC_BUS) | High-Speed GMLAN (6/14) | 500 kbps via due_can. Standard M2RET/ELM path. |
| CAN1 (TJA1051, MSC_BUS) | Mid-Speed GMLAN (3/11) | The M2's CAN1 transceiver is wired to DLC 3/11 — exactly the GMLAN mid-speed pins. No extra hardware needed; set due_can to 95.2 or 125 kbps per model. |
| SWCAN (MCP2515 + TH8056, SWC_BUS) | Single-Wire GMLAN (pin 1) | setupSW(33) normal / setupSW(83) flashing; mode(2) HV-wake BEFORE expecting replies from sleeping modules, then mode(3). |
| J1850 discrete circuit, VPW mode (pin 50 LOW) | Class 2 (pin 2) | VPW-only on GM: use pin 52 (VPW RX) / pin 53 (J1850+ TX). M2 J1850- (DLC pin 10) has no GM use. |

## Ford / Lincoln / Mercury

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| HS-CAN | 500 kbps | 6, 14 | 2 | 2004+ (full by 2008) | [B] | Powertrain bus; also the legislated emissions bus (ISO 15765-4) — any generic OBD-II tool sees it. Modules: PCM, TCM, ABS, EPAS. |
| MS-CAN | 125 kbps | 3, 11 | 2 | ~2003+ (not all models) | [B] | Ford-PROPRIETARY pins — dead on non-Ford vehicles. Body/comfort: GEM, doors, cluster, RCM, EATC. This pin split is why FORScan needs the HS/MS toggle on ELM327 adapters. BITRATE CONFLICT: one community glossary claims '125-500 kbps depending on chassis' [C] vs unanimous 125 kbps — treat 125 as standard. MS-CAN is NOT on all Fords: probe, don't assume. |
| HS-CAN2 | 500 kbps | — | 2 | newer platforms | [C] | Second high-speed bus on newer platforms (FDSM, ABS, RCM, PSCM, SCCM, GWM, IPMA per one vendor source). DLC availability varies; often gateway-internal only. |
| CAN FD | 500 kbps | 6, 14 | 2 | 2021+ select models (F-150, Lightning, Mach-E, Escape 2023+, Expedition/Navigator 2022+, Nautilus 2024) | [B] | M2 CANNOT PARTICIPATE: TJA1051 transceivers are CAN 2.0 only. 2021+ CAN-FD Fords are out of scope for M2 CAN work (hardware fact from the knowledge pack; vehicle consequence inferred but solid). |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| SCP / SAE J1850 PWM | 41.6 kbps | 2, 10 | 1996–~2006 (model-dependent); all-CAN by 2008 mandate | [B] | Ford's SCP variant REQUIRES In-Frame Response (IFR) bytes — unlike GM's VPW. Timeline approx: 1996-2001 PWM-only, 2002-2006 mixed by model, post-2006 CAN. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | HS-CAN (6/14) @ 500 kbps | Standard path. |
| CAN0 / CAN1 (TJA1051) | MS-CAN (3/11) @ 125 kbps | KEY M2 ADVANTAGE: a switched ELM327 sees one bus at a time, but the M2's two independent CAN controllers can watch HS-CAN and MS-CAN SIMULTANEOUSLY — FORScan+ELM327 cannot do this. |
| J1850 discrete circuit, PWM mode (pin 50 HIGH) | SCP (pins 2/10) | Pre-2004 Fords. IFR bytes REQUIRED by Ford's SCP variant. |
| LIN1/LIN2 (TJA1027) | Body LIN sub-buses | Door/climate sub-buses on some models, if tapped at the module. |
| NONE | CAN FD (2021+) | Out of scope — TJA1051 is CAN 2.0 only. |

## Stellantis (Chrysler / Dodge / Jeep / RAM / Fiat / Alfa Romeo)

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| CAN-C1 | 500 kbps | 6, 14 | 2 | ~2004/05+ | [A] | Powertrain/chassis high-speed CAN (SAE J2284). 11-bit identifiers the norm. 120-ohm terminators; ~60 ohms per pair (key off) = continuity check. |
| CAN-C2 | 500 kbps | 12, 13 | 2 | some platforms | [C] | Second high-speed CAN on some platforms (e.g. Alfa/Fiat 'second high-speed CANBUS' per aftermarket vendors). Pins confirmed [A]; BITRATE UNCONFIRMED — treat 500 kbps as provisional. |
| CAN-BH | — kbps | 3, 11 | 2 | ~2004/05+ | [C] | Body/harness CAN. Pins confirmed [A]; BITRATE UNCONFIRMED. NOT reachable with stock M2 hardware (both native CAN controllers spoken for by C1/C2; MCP2515 is tied to the SWCAN transceiver). |
| CAN-IHS | 125 kbps | — | 2 | ~2004/05+ | [B] | 'Interior High Speed' is the SLOW bus (125 kbps) — the name misleads. Interior/comfort modules. Not on the DLC; reachable only via gateway or direct tap. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| PCI / SAE J1850 VPW | 10.4 kbps | 2 | ~1999–~2005 (model-dependent) | [B] | Single wire, idle low, active high ~7-7.5V. Used for inter-module comms and scan-tool/flash until CAN replaced it. |
| CCD (Chrysler Collision Detection) | 7.8125 kbps | 3, 11 | 1988–~1998 | [C] | Proprietary 2-wire bus. TRAP: pins 3/11 were later recycled for CAN-BH — year/model determines which protocol is on those pins. |
| SCI (SAE J2610, Chrysler-proprietary serial) | — kbps | 6, 7, 9, 12, 14, 15 | 1990s–early 2000s (PCM/TCM flashing) | [C] | UART-based proprietary serial for PCM/TCM diagnostics and flash reprogramming. Multiple channels (SCI A Engine/Trans, SCI B); pin assignments vary by model/year. M2 HAS NO SCI HARDWARE — pre-CAN Chrysler powertrain flashing via SCI is out of reach for stock M2 firmware. |
| K-line (ISO 9141-2 / ISO 14230) | 10.4 kbps | 7 | 1996–~2004 | [B] | On many 1996-~2004 models alongside PCI/SCI. M2 K-line transceiver (TJA1027) covers this. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | CAN-C1 (6/14) @ 500 kbps | Primary diagnostic bus. On 2018+ SGW vehicles, reads work through the gateway; writes are blocked. |
| CAN0 / CAN1 (TJA1051) | CAN-C2 (12/13) | Second native controller covers this where present. |
| NONE (stock) | CAN-BH (3/11) | Not reachable with stock M2 hardware — would need an external CAN transceiver on SPI. |
| J1850 discrete circuit, VPW mode (pin 50 LOW) | PCI (pin 2) | Pre-CAN Chrysler. |
| K-line (TJA1027) | ISO 9141 K-line (pin 7) | 1996-~2004 models. |
| LIN1/LIN2 (TJA1027) | LIN sub-buses (e.g. CCN -> multifunction switch) | If tapped at the module; plain 19.2k-class LIN. |
| NONE | SCI (J2610) | No M2 hardware support — proprietary serial, not J1850/K-line/LIN. |

## Toyota / Lexus

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| CAN V Bus (HS) | 500 kbps | 6, 14 | 2 | 2004+ | [B] | Powertrain/chassis: ECM, HV ECU, battery ECU, skid control, EPS, airbag, gateway ECU. Termination spec 54-69 ohms across 6/14 (ignition off) [A]. |
| MS-CAN | 250 kbps | — | 2 | 2004+ | [B] | Body/comfort traffic BEHIND the gateway ECU — not on the DLC in any source found. A scan tool reaches it only through gateway routing. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| K-line / SIL (ISO 9141-2) | 10.4 kbps | 7 | pre-2008+ (survived into CAN era) | [B] | DLC3 pin 7 (SIL), optional L-line pin 15. Non-CAN modules (TPMS, air suspension) used K-line deep into the CAN era. |
| BEAN (Body Electronics Area Network) | 10 kbps | — | early 2000s+ | [B] | Toyota-PROPRIETARY single-wire body bus, 0-10V. NO M2 HARDWARE SUPPORT — not J1850, not K-line, not LIN. |
| AVC-LAN | 17.8 kbps | — | early 2000s+ | [B] | Toyota-proprietary audio/visual bus; star topology. Not a diagnostic target. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | HS CAN V Bus (6/14) @ 500 kbps | Primary diagnostic + logging bus. One controller normally suffices at the DLC (no HS/MS pin split like Ford). |
| CAN0 / CAN1 (TJA1051) | MS-CAN @ 250 kbps | Only if tapped behind the gateway (interior harness) — not on the DLC. |
| K-line (TJA1027) | SIL K-line (pin 7) @ 10.4 kbps | Non-CAN modules on CAN-era vehicles; pre-CAN diagnostics. |
| LIN1/LIN2 (TJA1027) | LIN sub-buses @ 9.6 kbps | If tapped at the module. |
| NONE | BEAN | Out of reach — proprietary 0-10V single-wire protocol, no M2 hardware speaks it. |

## Honda / Acura

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| F-CAN | 500 kbps | 6, 14 | 2 | 2003+ | [A] | Powertrain bus: ECM/PCM, TCM, ABS/VSA, EPS, SRS. TWO SEGMENTS: F-CAN A (OBD-II/diagnostic side) and F-CAN B (internal powertrain) — openpilot relays between them. |
| B-CAN | 33.33 kbps | — | 1 | 2006+ | [A] | Body CAN: gauge module, MICU, climate, immobilizer-keyless. SINGLE-WIRE 33.33 kbps per service manual. NEVER at the DLC — requires a behind-dash tap (BCM 36-pin connector on 2016 Civic/2017 CR-V). SPEED CONFLICT: one community project claims 150 kbps on 2016+ [C] — unverified, contradicts the manual. |
| IMA CAN (hybrids) | — kbps | — | 2 | hybrids | [B] | Separate CAN bus for the Integrated Motor Assist hybrid system; own malfunction DTCs. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| K-line (ISO 9141-2) | 10.4 kbps | 7 | 1990s-2010s | [A] | Honda was a heavy K-line user and NEVER used J1850. Pin 7 kept populated alongside CAN into the 2010s (SRS/ABS/VSA/EPS/immobilizer K-line troubleshooting in service manual). |
| SCS (Service Check Signal) | — kbps | 9 | 1990s+ | [B] | Honda-SPECIFIC pin 9: grounding it puts modules into service-check / blink-code mode. Readable as a digital input; a diagnostic aid, not a bus. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | F-CAN (6/14) @ 500 kbps | This is F-CAN A (diagnostic side) at the DLC; F-CAN B (powertrain) sits behind the gateway. |
| SWCAN (MCP2515 + TH8056) | B-CAN 33.33k single-wire | NATURAL FIT (inferred): single-wire 33.33 kbps CAN matches the TH8056. setupSW(33). ONLY via BCM-harness tap — never the DLC. Caveat: if the 150 kbps B-CAN claim proves true for 2016+, the TH8056 cannot do that rate. |
| K-line (TJA1027) | K-line (pin 7) @ 10.4 kbps | Pre-CAN diagnostics and still-populated K-line on CAN-era Hondas. |
| 12VIO digital input | SCS (pin 9) | Readable as a digital input; grounding enters service-check mode. |
| NONE | J1850 | Honda never used J1850 — the M2 J1850 hardware has no Honda application. |

## Volkswagen Group (VW / Audi / SEAT / Skoda)

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| Diagnosis CAN | 500 kbps | 6, 14 | 2 | 2004+ | [B] | THE single CAN pair on the DLC — it is the diagnosis CAN to the J533 gateway. VW does NOT put comfort/infotainment CAN pairs on the DLC; those are gateway-internal. |
| Powertrain CAN | 500 kbps | — | 2 | 2004+ | [B] | Engine, transmission, ABS. Gateway-internal; reached through J533 routing from the DLC pair. |
| Convenience CAN | 500 kbps | — | 2 | 2004+ | [B] | Windows, locks, doors. 100 kbps on PQ-era (A8L SSP287); ALL buses moved to 500 kbps on MQB (Tiguan SSP553). Gateway-internal. |
| Infotainment CAN | 500 kbps | — | 2 | 2004+ | [B] | Radio, navigation. Gateway-internal. MOST (fibre-optic, 25M PQ / 150M MQB) carries premium audio — electrically invisible to any CAN tool. |
| CAN FD (MQB Evo) | — kbps | 6, 14 | 2 | 2020+ | [C] | UNCONFIRMED in this pass — one forum poster mentions CAN-FD DBCs assumed MQB Evo. If confirmed, those buses are OUT OF M2 SCOPE (TJA1051 = CAN 2.0 only). |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| K-line (ISO 9141-2) | 10.4 kbps | 7 | pre-2004+ (remnants) | [B] | DLC pin 7 bidirectional, L-line pin 15 optional wake-up. Retained on early CAN-era cars for some modules. |
| KWP-1281 (VAG proprietary) | — kbps | 7 | ~1995-2006 | [B] | 5-baud init. ECU addresses: 0x01 engine, 0x03 ABS, 0x08 HVAC, 0x17 instruments, 0x19 gateway, 0x46 central convenience. |
| KWP2000 (ISO 14230) | 10.4 kbps | 7 | 2003+ pre-CAN | [B] | Fast init (~500ms), up to 255-byte messages. Common on 2003+ pre-CAN VAG vehicles. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | Diagnosis CAN (6/14) @ 500 kbps | Primary diagnostic path — via the J533 gateway to all buses. |
| K-line (TJA1027) | K-line (pin 7) @ 10.4 kbps | Covers KWP-1281 / KWP2000 / ISO 9141. |
| LIN1/LIN2 (TJA1027) | LIN sub-buses @ 19.2 kbps | Doors, sunroof, wipers, steering wheel — if tapped at the module. |
| NONE | MOST (optical) | Fibre-optic — electrically invisible to any CAN tool. |
| NONE (if present) | CAN FD (MQB Evo) | Out of scope if present — TJA1051 is CAN 2.0 only. |

## Hyundai / Kia

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| C-CAN | 500 kbps | 6, 14 | 2 | 2005+ | [B] | Chassis CAN: EMS/ECM, TCU, ESC/ABS, EPB, SCC, MDPS. Primary diagnostic + powertrain bus. Legislated OBD-II confirmed live (2018 Kia Soul, responders 0x7E8-0x7EF). |
| M-CAN | — kbps | — | 2 | 2005+ | [C] | Multimedia/body CAN (171 messages in opendbc hyundai_2015_mcan.dbc). BITRATE UNCONFIRMED [?]. DLC pin exposure UNCONFIRMED [?] — treat as interior-only unless a per-model wiring diagram says otherwise. |
| CAN FD (select 2021+) | — kbps | 6, 14 | 2 | 2021+ select | [C] | Per community reports, DIAGNOSTICS STAY ON CLASSIC CAN even on CAN-FD vehicles — so M2 CAN 2.0 transceivers can still do OBD-II diagnostics; CAN-FD bus participation is out of scope. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| K-line (ISO 9141 / KWP2000) | 10.4 kbps | 7 | 1991-~2010 | [B] | Hyundai/Kia NEVER used J1850. QUIRK: K-lines appear on MANY DLC pins — 1,2,3,7,8,9,11,12,13 — one per system (engine, ABS, airbag, gearbox), not one shared line. Wire the M2 K-line to the TARGET SYSTEM pin, not just pin 7. KW71 (1991-2001 engine), ISO 9141 (1996-~2005), KWP2000-over-K-line (1996+, all systems). |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | C-CAN (6/14) @ 500 kbps | Primary diagnostic + powertrain bus. Standard M2RET/ELM path. |
| CAN0 / CAN1 (TJA1051) | M-CAN (if tapped) | Interior-only per available sources; tap at the module if needed. |
| K-line (TJA1027) | K-line @ 10.4 kbps | Pre-CAN models. Identify the target SYSTEM pin (1,2,3,7,8,9,11,12,13) — not just pin 7. |
| NONE | J1850 VPW/PWM | Not applicable — Hyundai/Kia never used J1850. |
| NONE | CAN FD (2021+ select) | Out of scope for bus participation; diagnostics reportedly remain on classic CAN. |

## Nissan / Infiniti

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| Main CAN (V-CAN) | 500 kbps | 6, 14 | 2 | ~2003+ | [B] | Powertrain, chassis, body, diagnostics. Two 120-ohm terminators (ECM + IPDM/TCM/BCM); ~60 ohms across 6/14 = healthy [A]. BITRATE CONFLICT: Nissan Tech News claims 1 Mbit/s [A] vs all community captures at 500 kbps [B] — the 1 Mbit/s figure is likely a trade-article error. Most Nissans have a single major CAN bus (6-12 devices). |
| AV-CAN (infotainment) | 500 kbps | 3, 11 | 2 | model-dependent | [B] | Infotainment traffic on models that expose it (e.g. Leaf). |
| AV COMM (audio-NAVI, isolated) | 500 kbps | — | 2 | model-dependent | [B] | Audio unit to NAVI unit (NAVI = bus master). Not on the DLC. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| DDL / Consult I | 9.6 kbps | — | 1989-~2004 | [B] | Nissan-PROPRIETARY 3-wire serial: TX, RX, host-generated 153.6 kHz async clock. Host TX = 12V idle-LOW; ECU = open-collector idle-HIGH (host 5V pull-up). 9600 8N1 LSB-first. Init: FF FF EF -> 0x10 (send twice if needed). Commands: 0xD1 read DTCs, 0xC1 clear, 0x5A stream, 0xC9 read ROM. 14-pin gray connector (~1989-2000); 1996+ 16-pin DLC carries Consult Rx/Tx/Clk lines (exact DLC pin numbers UNCONFIRMED [?]) alongside K-line. ELM327/STN CANNOT speak DDL. |
| K-line (ISO 9141) | 10.4 kbps | 7 | 1996-2004 | [B] | Nissan's OBD2-compliance path during the transition era (DDL is not OBD2-compliant). Factory ECU pinout labels it for GST (generic scan tool) use. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 / CAN1 (TJA1051) | Main CAN (6/14) @ 500 kbps | Standard ISO 15765-4. Note: on BCM-gatewayed models (e.g. 2018 Pathfinder) the DLC is QUERY-ONLY — passive sniffing sees zero frames; send an active request first. |
| CAN0 / CAN1 (TJA1051) | AV-CAN (3/11) @ 500 kbps | Second controller covers it where exposed (Leaf-class). |
| K-line (TJA1027) | K-line (pin 7) @ 10.4 kbps | 1996-2004 transition era. |
| CUSTOM (12VIO + GPIO + PWM clock) | DDL / Consult I | Electrically reachable (12VIO drives 12V idle-low TX; GPIO+divider reads 5V ECU output; SAM3X PWM generates the 153.6 kHz clock) but needs a purpose-written DDL driver — NOT stock-firmware capable. Bench-test against a real ECU first. [C - untested inference] |
| NONE | J1850 / SWCAN | No evidence Nissan ever used J1850 or single-wire CAN [?]. |

## Subaru

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| HS CAN | 500 kbps | 6, 14 | 2 | 2008+ | [A] | Primary diagnostic bus. 120-ohm end termination (U1201 FSM procedure confirms: fit 120 ohms across CAN-Hi/Lo when ECM or VDC module is disconnected). |
| CAN-LS (low-speed CAN) | 250 kbps | — | 2 | 2008+ | [C] | Separate body/comfort network; U1321 'CAN-LS METER NO-RECEIVE DATA' confirms it exists. Bitrate and DLC presence NOT documented — interior only unless proven otherwise. BIU gateway function HS<->LS is INFERRED, not verified. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| SSM2 (Subaru Select Monitor, K-line) | 4.8 kbps | 7 | 1999-~2015 | [B] | Proprietary memory-address-oriented protocol (not UDS): 4800 bps 8N1, packet 0x80 DEST SRC LEN CMD data CHECKSUM; dest 0x10 = ECM, 0x18 = TCU. Commands 0xA0 block read, 0xA8 address read, 0xBF ECU init. Lives on pin 7 even on CAN-era cars. |
| ISO 9141-2 (generic OBD-II) | 10.4 kbps | 7 | 1999-2007 | [B] | Emissions OBD-II on the K-line for EJ-era cars; SSM2 shares the same pin with its own protocol. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 or CAN1 (TJA1051, due_can) | HS CAN (6/14) | Primary diagnostic + logging bus, all platforms 2008+. |
| K-line transceiver (TJA1027) | SSM2 on pin 7 | 4800 bps 8N1 is within the TJA1027's capability; the work is the SSM2 packet layer (init 0xBF, address reads 0xA8, checksum). Covers 1999-~2015 ECM/TCU including CAN-era cars — two independent diagnostic paths from the DLC alone. |
| Second CAN controller (TJA1051) | CAN-LS (interior tap) | Only if tapped behind the BIU (combination-meter branch); bitrate undocumented, verify per car. |

## Mazda

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| HS-CAN | 500 kbps | 6, 14 | 2 | 2001+ (SkyActiv 2012+) | [B] | Powertrain/chassis: PCM, TCM, DSC/ABS HU/CM, SAS (airbag), IC. |
| MS-CAN | 125 kbps | 3, 11 | 2 | 2001+ | [B] | Body/comfort: FBCM/RBCM, HVAC, audio, TPMS, RKE. EXPOSED AT THE DLC (pins 3/11) — the M2's two CAN controllers can watch HS+MS simultaneously straight from the OBD port, unlike Toyota. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| SCP (SAE J1850 PWM, Ford era) | 41.6 kbps | 2, 10 | ~2001-2012 | [B] | Ford-platform-era diagnostics; pin 13 FLASH line signals the PCM to erase EPROM during programming — never drive it from the M2. |
| ISO 9141 K-line | 10.4 kbps | 7 | Ford era | [B] | On some Ford-era models. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 or CAN1 (TJA1051, due_can) | HS-CAN (6/14) | Primary diagnostic + logging bus. |
| Second CAN controller (TJA1051) | MS-CAN (3/11) | Exposed at the DLC — no gateway traversal needed. |
| M2 J1850 hardware (discrete circuit, pins 49-54) | SCP J1850 PWM (2/10) | Ford-era models only (pre-~2008). |
| K-line transceiver (TJA1027) | K-line (7) | Ford-era non-CAN modules. |
| None | 7th-gen BP/CX-30 / 2024+ ND3 buses | OUT OF M2 SCOPE IF CAN FD — unverified, treat as unknown [?]. |

## BMW

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| D-CAN (diagnostic CAN) | 500 kbps | 6, 14 | 2 | 03/2007+ E-series; F-series | [B] | Diagnostic bus to the DLC (replaced K-line 03/2007). E-series diagnostics are KWP2000-over-CAN on the 0x6F1/0x6XX scheme, not UDS DIDs. |
| PT-CAN (powertrain CAN) | 500 kbps | 6, 14 | 3 | E-series | [A] | DME/DDE, EGS, DSC, EKPS; JBE as gateway. Three wires: CAN-H/CAN-L twisted pair PLUS a separate wake-up line (not CAN signaling — never connect to a transceiver). 120-ohm terminators. DLC presence is model-dependent (absent pre-03/2007). |
| K-CAN (body CAN) | 100 kbps | — | 2 | E-series | [A] | Body/comfort: CAS, FRM, KOMBI, IHKA, MRS, FZD, CCC, PDC. NOT on the DLC — tap behind the JBE. Reported as fault-tolerant-style; TJA1051 compatibility on a tap is UNVERIFIED. |
| K-CAN2 | 500 kbps | — | 2 | F-series | [B] | REM, FZD, PMA, FLA, FEM-internal ZGW, HU-H (NBT). Not on DLC. |
| F-CAN (chassis CAN) | 500 kbps | — | 2 | E-series | [B] | DSC <-> SZL <-> active steering (AL). Direct tap at DSC/SZL. |
| Ethernet / ENET / DoIP | — kbps | 3, 11, 12, 13 | 8 | F-series; G-series | [B] | 100BASE-TX on OBD 3=TX+, 11=TX-, 12=RX+, 13=RX-. F/G-series coding and diagnostics. OUT OF M2 SCOPE — needs Ethernet MAC + DoIP stack. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| K-line | — kbps | 7 | pre-03/2007 E-series | [C] | Pre-D-CAN diagnostics; the K+DCAN cable switch selects between K-line and D-CAN. |
| MOST (fiber-optic ring) | — kbps | — | E/F-series | [B] | Infotainment ring (CCC/CIC, amp, TCU). Fiber — no copper tap. OUT OF M2 SCOPE. |
| byteflight (fiber star) | — kbps | — | E60/E63/E64/E65 | [B] | Safety bus, 10 Mbit/s over fiber. OUT OF M2 SCOPE. |
| FlexRay | — kbps | — | F-series | [B] | Chassis dynamics (DSC, ICM, VDM, EPS). 10 Mbit/s. OUT OF M2 SCOPE — no M2 hardware. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 or CAN1 (TJA1051, due_can) | D-CAN (6/14) | Primary diagnostic + logging path. E-series 0x6F1 KWP2000-over-CAN is implementable in the M2's UDS/diagnostics mode (11-bit IDs, 8-byte frames, fully CAN 2.0). |
| Second CAN controller (TJA1051) | PT-CAN / K-CAN2 / F-CAN (direct taps) | Harness taps only; K-CAN tap needs transceiver-compatibility verification first [C]. |
| None | MOST / byteflight / FlexRay / Ethernet-DoIP / CAN FD (G-series) | OUT OF M2 SCOPE — no hardware path. |

## Mercedes-Benz

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| CAN-C (powertrain CAN) | 500 kbps | 6, 14 | 2 | 2000+ | [A] | Engine, transmission, ESP, chassis. The DLC exposes the 500k CAN on standard pins 6/14. |
| CAN-B (interior CAN) | 83.3 kbps | — | 2 | 2000+ | [A] | Body/comfort: SAMs, doors, seats, HVAC. Behind the gateway; tap at X30/4-7 distribution hubs in footwells/rocker panels. Odd 83.3k rate is real — confirmed by open-source W203 CAN project. |
| CAN-D (diagnostic CAN) | 500 kbps | — | 2 | W211 era | [A] | Dedicated diagnostic databus: CGW <-> tester link. Tester path, not raw bus traffic. |
| CAN-E (cluster/infotainment link) | 500 kbps | — | 2 | W204/W212 era | [C] | Cluster link behind the cluster (W204 cluster connector pins 12/13). Not on DLC. |
| Ethernet / DoIP | — kbps | 3, 11, 12, 13 | 8 | W222/W205 era+ | [B] | Diagnostics on newer models; DLC pins 3/11 (Rx), 12/13 (Tx), pin 8 activation (ISO 13400 option 1). OUT OF M2 SCOPE. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| KWP2000 over CAN (0x4xx/0x5xx diagnostic IDs) | 500 kbps | 6, 14 | W203/W211 era (~2000-2009) | [C] | Tester request 0x04E0 -> response 0x05FF observed in an XENTRY-passthru capture (Macchina M2 under-dash). Not the 0x7xx block. |
| K-line | — kbps | 7 | pre-W203 | [C] | Older (ME9.7-era) DLCs carried multiple K-lines on pins 1/7/9/11/12/13/15. |
| MOST (fiber-optic) | — kbps | — | 2000+ | [B] | Audio/infotainment (replaces D2B). Fiber — OUT OF M2 SCOPE. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 or CAN1 (TJA1051, due_can) | CAN-C / diagnostic CAN (6/14) | Legislated OBD-II + gateway-filtered diagnostics. THE DLC IS FILTERED: reads pass, writes are restricted to diagnostic CAN IDs, unknown diagnostic IDs are silently dropped — non-response means 'filtered', not 'module absent'. Wake-up frame required before buses carry traffic. |
| Second CAN controller (TJA1051) | CAN-B (83.3k, X30 hub tap) | TJA1051 handles 83.3k. Interior/body traffic behind the gateway. |
| K-line transceiver (TJA1027) | K-line (older models) | Pre-W203 modules. |
| None | MOST / FlexRay / Ethernet-DoIP / 2021+ secure gateway | OUT OF M2 SCOPE. 2021+ (W223/W206) secure gateway authenticates OBD-II access — unauthenticated reads blocked. |

## Volvo

### Buses

| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| HS-CAN | 500 kbps | 6, 14 | 2 | 2005+ (250k in 2004) | [B] | Powertrain/chassis: ECM, TCM, BCM/ABS, ETM, SAS. CEM acts as inter-bus gateway. Terminators in ABS/BCM + ETM (Bosch EMS MY02+: BCM + ECM). |
| LS/MS-CAN | 250 kbps | 3, 11 | 2 | 2005+ (125k in 2004) | [B] | Body/comfort: SRS, DDM, PDM, PSM, CCM, DIM, RTI, PHM, AUD, REM, SWM, UEM. AT THE DLC on P1/P2/P3 — MS-CAN-capable adapter is mandatory for full third-party coverage. Terminators in UEM + REM. |

### Legacy protocols

| Protocol | Bitrate | DLC pins | Years | Grade | Notes |
|---|---|---|---|---|---|---|
| ISO 9141-2 (K-line) | 10.4 kbps | 7 | 1996-2004 | [B] | 2005+ = CAN. Pins 2/10 are NOT populated on Volvo — Volvo never shipped J1850 despite generic pinout tables. |

### M2 hardware mapping

| M2 hardware | Bus | Notes |
|---|---|---|
| CAN0 or CAN1 (TJA1051, due_can) | HS-CAN (6/14) | Primary powertrain/chassis bus. Community proof: Alfaa123/Volvo-CAN-Gauge ran on a Macchina M2 against a 2011 C30 (P1). |
| Second CAN controller (TJA1051) | LS/MS-CAN (3/11) | BOTH DLC CAN pairs are usable simultaneously — the M2's dual CAN controllers map 1:1 onto Volvo's dual-bus DLC. Note the model-year bitrate split ('04: 125k/250k; '05+: 250k/500k). |
| K-line transceiver (TJA1027) | K-line (7) | 1996-2004 models. |
| None | SPA/CMA (2016+) Ethernet-DoIP / CAN FD | OUT OF M2 SCOPE — no Ethernet/DoIP hardware, TJA1051 is CAN 2.0 only. SPA/CMA need a VOE adapter + VIDA. |

_Generated by scripts/build.py — do not hand-edit._
