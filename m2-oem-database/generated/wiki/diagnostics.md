# Diagnostic access by make

## General Motors [B]

- Protocol: UDS / ISO 14229 (GMLAN Enhanced Diagnostic Test Mode)
- Evidence: OEM-GM-SPEC (GMLAN Enhanced Diagnostic Test Mode spec excerpt)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| 11-bit USDT physical addressing | $7E0-$7E7 req / $7E8-$7EF resp | ECU #1-#8: tester sends $7E0-$7E7, ECU answers $7E8-$7EF. ECM confirmed as ECU #1 (0x7E0/0x7E8) via documented ELM327 VIN-read capture; TCM commonly ECU #2 (community convention). | [B] |
| Functional (broadcast) diagnostics | $7DF | Reaches all emission-related ECUs. | [B] |
| Legislated OBD-II | Modes $01-$0A | On HS GMLAN (6/14). Always available. | [A] |

### Gateways

#### BCM (Body Control Module) [B] (2004+)

- Effect: Bridges HS GMLAN to LS/SWCAN and legacy Class 2. Scan-tool traffic to non-HS modules routes through it; a BCM fault can look like a whole-bus failure.
- Evidence: OEM-GM-TECH (BCM gateway role [A/B])

### Tool ecosystem

- **Tech2 + CANdi module** — GM handheld 1992-~2009+; CANdi added 2004 for CAN vehicles.
- **Tech2Win / MDI / MDI 2 + GDS2** — Global-A (~2010+) through current; hosted on the Techline Connect portal.
- **SPS2 (Service Programming System)** — Module reflash with VIN-matched calibrations from GM servers — online subscription only.

### Seed/key policy

No factory-published algorithm. Community RE exists for specific OLDER PCMs (E38/E67 — algorithms NOT reproduced here). Tuner-locked PCMs don't follow the GM formula. Global-B and newer: keys are server-issued, not client-computable. For any modern GM controller: NO PUBLIC ALGORITHM — dealer tool (SPS2/GDS2) required.

## Ford / Lincoln / Mercury [B]

- Protocol: UDS / ISO 14229 over ISO-TP (ISO 15765-2)
- Evidence: OEM-FORD-FORSCAN (FORScan capability set); OEM-FORD-COMM

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Physical addressing (+8 response offset) | 0x7E0 -> 0x7E8 | Ford is in the '+8' family: request 0x7E0, response 0x7E8. Known module IDs (2011-2023 Explorer, community spreadsheet): 0x7E0 PCM, 0x7E4 BECM, 0x7E6 SOBDMC, 0x7D0 APIM, 0x726 GWM. | [B] |
| Functional (broadcast) diagnostics | 0x7DF | Standard ISO 15765-4 practice; generic OBD-II scan behavior. | [B] |
| As-built configuration | manufacturer-specific | FORScan reads/writes module as-built config (extended license for writes). Can only enable/disable features Ford built into the module firmware. | [B] |

### Gateways

#### GWM (Gateway Module) [B] (newer platforms)

- Effect: Forwards messages between CAN buses and provides the OBD-II diagnostic bus. Diagnostic requests via the DLC are routed/filtered by the gateway; raw interior-bus traffic may not be visible at the DLC.
- Evidence: OEM-FORD-OPEN (GWM definition); consequence inferred

#### BdyCM (Body Control Module) [B] (CGEA era+)

- Effect: Bridges HS-CAN and MS-CAN.
- Evidence: OEM-FORD-COMM (blueovallabs glossary)

### Tool ecosystem

- **FORScan** — Manufacturer-specific Ford services beyond generic OBD-II: all-module DTCs, PIDs, actuator tests, as-built editing, some programming. Free extended license (expires periodically). Requires fully ELM327-compatible adapter — clones fail on service-level protocols.
- **HS/MS switch adapters** — Stock ELM327 reaches HS-CAN only; Ford/Mazda-compatible adapters add a physical or electronic HS/MS switch for MS-CAN (pins 3/11). FORScan prompts for the switch when it expects MS-CAN modules.

### Seed/key policy

NO PUBLIC FORD ALGORITHM — none found, none invented. PATS (immobilizer) programming via FORScan uses TIMED access (maintain connection 10-12 min until 'Security Access Granted'; interruptions reset the timer) or CODED access (vehicle shows Outcode, authorized generator returns Incode; internals not public). UDS 0x27 without the key returns NRC 0x35.

## Stellantis (Chrysler / Dodge / Jeep / RAM / Fiat / Alfa Romeo) [B]

- Protocol: UDS / ISO 14229 over CAN, 11-bit IDs
- Evidence: OEM-STLA-COMM

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Standard emissions OBD-II | Modes 0x01-0x0A | Works through the SGW on 6/14 — READS are not blocked. | [B] |
| UDS reads through SGW | 0x19 (DTC), 0x22 (data) | Reading DTCs, live data, version info works with any tool through the SGW. | [B] |
| UDS writes through SGW | 0x14, 0x2E, 0x2F, 0x31 | BLOCKED without authentication: DTC clear (0x14), write-by-identifier (0x2E), IO control (0x2F), routine control (0x31), actuations, relearns, programming. | [B] |
| Community UDS example (JL Wrangler) | CAN ID 620 + 0x2F | Horn control via UDS InputOutputControlByIdentifier — well-documented community project (pre-SGW or bypassed vehicle). | [C] |

### Gateways

#### SGW (Secure Gateway Module) [B] (2018+ (one vendor doc says 2017 — unresolved conflict; consensus is 2018+))

- Effect: CAN firewall between the OBD-II port and internal networks. READS (DTCs, live data, version info) still work; WRITES (DTC clear, bi-directional controls, actuations, relearns, programming) are BLOCKED without authentication.
- Legitimate access: Legitimate paths only: (1) AutoAuth — $50/yr shop account (6 users), technician accounts free, approved tools only (Autel, Bosch ADS 4.0+, Innova, TOPDON, LAUNCH); (2) dealer wiTECH 2.0; (3) physical bypass on the owner's own vehicle (12+8 STAR cable or SGW bypass module; remove before dealer visits). NO DIY AutoAuth path exists for a homebrew tool.
- Evidence: OEM-STLA-SGW (behavior, pricing, tools); OEM-STLA-COMM (bypass)

#### FCM/CGW (pre-SGW) [B] (pre-2018)

- Effect: Front Control Module / Central Gateway bridged the scan tool (Diagnostic CAN-C at the DLC) to CAN-B/CAN-C; held the Vehicle Build Configuration.
- Evidence: OEM-STLA-COMM

### Tool ecosystem

- **wiTECH 2.0** — FCA dealer tool; authenticates to the SGW natively.
- **AutoAuth-approved aftermarket tools** — Autel tablets, Bosch ADS 325/625 (4.0+), Innova SDS43, TOPDON, LAUNCH, THINKCAR — with paid AutoAuth shop membership.
- **AlfaOBD / appcarFCA (+ 12+8 bypass cable)** — Community tools used with the physical SGW bypass on the owner's vehicle.

### Seed/key policy

NO PUBLIC FCA SEED/KEY OR SGW BYPASS — none found in public sources, none invented, none reproduced. UDS 0x27 algorithms for FCA ECUs are not public. M2 Stellantis strategy: read-only logging/diagnostics through the SGW, or physical bypass on the owner's own vehicle.

## Toyota / Lexus [B]

- Protocol: UDS-flavored over ISO-TP (+8 response offset)
- Evidence: OEM-TOYOTA-COMM (07E0->07E8 capture)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Physical addressing (+8 offset) | 0x7E0 -> 0x7E8 | Like Ford: request 0x7E0, response 0x7E8. Hybrid ECUs have their own IDs on the same HS bus: 0x7E2/0x7EA (HV ECU), 0x7E3/0x7EB (HV battery) — a generic scanner on 0x7E0 never sees hybrid DTCs. | [B] |
| Hybrid DTC service | 0x13 | Toyota hybrids reportedly use service 0x13 (vs standard UDS 0x19) for DTC reads — treat as model-specific, not a general Toyota rule. | [C] |
| Legislated OBD-II | Modes 0x01-0x0A | On HS CAN 6/14. Always available. | [A] |

### Gateways

#### Gateway ECU [B] (2004+)

- Effect: Performs protocol conversion between CAN, BEAN, and AVC-LAN. MS-CAN and body buses sit behind it — not on the DLC. No Stellantis-style authentication firewall found (absence of evidence; no source describes a Toyota SGW equivalent).
- Evidence: OEM-TOYOTA-TRAIN (2004 Prius manual)

### Tool ecosystem

- **Techstream** — Toyota/Lexus dealer software: full DTC, live data, Active Tests, calibrations. Interfaces: MongoosePro Toyota, Tactrix OpenPort, VCX Nano (clones vary in quality).

### Seed/key policy

NO PUBLIC TOYOTA SEED/KEY ALGORITHM — none found, none invented. TSB T-SB-0043-14 documents the server-side flow: Techstream generates a Seed Number, TIS returns a one-time Pass-Code (management approval required). 2018+ adds NASTF LSID subscription (~$65/2-day, ~$1295/yr) for key programming. Security-gated operations are dealer/TIS territory.

## Honda / Acura [B]

- Protocol: 29-bit ISO 15765-3 diagnostics (primary); 11-bit path single-source
- Evidence: OEM-HONDA-COMM (hansonFish/obdii, papataku analyzer)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| 29-bit diagnostic addressing | 0x18DB33F1 -> 0x18DAF110 | Tester transmits 0x18DB33F1; ECM responds 0x18DAF110 (2009 Civic). e:HEV ECUs answer at 0x18DAF101/102/106/10E/1EF. TRY 29-BIT FIRST. | [B] |
| 11-bit UDS path | 0x7E0 / 0x7E8 | One hobbyist guide reports 2016-2021 Civic UDS at 0x7E0/0x7E8 requiring extended session (0x10 0x03). Single-source — verify on-vehicle. | [C] |
| Legislated OBD-II | Modes 0x01-0x0A | On F-CAN 6/14. Always available. | [A] |

### Gateways

#### Gauge control module (tach) [A] (2006-~2015)

- Effect: IS the F-CAN to B-CAN gateway. Runs network self-diagnostic readable on the odo/trip display (Error 1 = F-CAN, Error 2 = B-CAN, Error 3 = UART).
- Evidence: OEM-HONDA-SVC

#### Dedicated gateway control module [C] (2016+)

- Effect: Behind the lower-left dash. A dead gateway = OBD-II link error with a healthy ECU.
- Evidence: OEM-HONDA-COMM

### Tool ecosystem

- **HDS / i-HDS** — Dealer tool through 2010s (HIM interface); i-HDS is subscription (~$45/day, ~$200/30d, ~$1800/yr). Works with J2534 passthru devices.
- **MPCS short connector (fallback)** — Documented Honda fallback: jumper on the MICU service check connector displays B-CAN DTCs one-by-one on the odo/trip display; holding SELECT/RESET 10+s clears them. No scan tool needed.

### Seed/key policy

NO PUBLIC HONDA UDS 0x27 ALGORITHM — none found, none invented. Immobilizer PCM codes derive from the LAST 5 VIN DIGITS via aftermarket calculators (pre-2020; tool-workflow passwords, NOT the UDS crypto exchange). Immobilizer/key functions are dealer/i-HDS territory.

## Volkswagen Group [B]

- Protocol: UDS (2008+); KWP2000 (2003+ pre-CAN); KWP-1281 (1995-2006)
- Evidence: OEM-VW-VCDS (Ross-Tech history)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| VCDS module addressing | hex words | 01 Engine, 02 Auto Trans, 03 ABS, 08 HVAC, 09 Cent. Elect., 15 Airbags, 16 Steering wheel, 17 Instruments, 19 CAN Gateway, 42/52/62/72 Doors, 46 Central Conv., 5F Information Electr. | [B] |
| Gateway Installation List | via 0x19 | J533 reports installed modules and status in ~3 seconds; the list is edited through Gateway Coding. Physically present but unlisted modules (or vice versa) generate DTCs. | [B] |
| Legislated OBD-II | Modes 0x01-0x0A | On diagnosis CAN 6/14. Always available. | [A] |

### Gateways

#### J533 (Data Bus On Board Diagnostic Interface) [B] (2004+)

- Effect: Central gateway between all buses; diagnostic address 0x19. The DLC exposes ONLY the diagnosis CAN pair (6/14) — comfort/infotainment are gateway-internal.
- Evidence: OEM-VW-SSP

#### SFD (Schutz Fahrzeugdiagnose) [B] (2020+ (MQB Evo/MEB); SFD2 on 2024+)

- Effect: Blocks WRITING services (adaptations, coding, parametrizations) on protected ECUs. Per VW own workshop manual: READS and BOOTLOADER-BASED FLASHING are explicitly NOT SFD-protected.
- Legitimate access: Legitimate paths only: (1) ODIS + GEKO (dealer); (2) Autel in-device tokens (24h/VIN); (3) Topdon/Thinkcar manual SFD; (4) OBDeleven (~90-min window, reported VW-authorized). Confirm SFD2 support per VIN on 2024+.
- Evidence: OEM-VW-SFD (VW workshop manual); OEM-VW-COMM (unlock paths)

### Tool ecosystem

- **VCDS (Ross-Tech)** — Enthusiast reference for pre-SFD vehicles: full diagnostics, long coding, Gateway Coding Assistant. First aftermarket UDS/ODX support (2008, Audi B8).
- **ODIS + GEKO (dealer)** — ODIS-S diagnostics, ODIS-E engineering/flashing. GEKO gates immobilizer/key programming and component protection.

### Seed/key policy

NO PUBLIC VW GROUP SEED/KEY ALGORITHM — none found, none invented. Pre-SFD used 5-digit login codes; SFD replaced that mechanism from 2020. Immobilizer/component protection via GEKO-gated ODIS.

## Hyundai / Kia [B]

- Protocol: UDS (ISO 14229) from ~2011; KWP2000-over-CAN on 2005-~2010
- Evidence: OEM-HYUNDAI-COMM (HiCOM protocol table)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Legislated OBD-II | 0x7DF / 0x7E8-0x7EF | Confirmed live on a 2018 Kia Soul with responders at 0x7E8-0x7EF. | [B] |
| ADAS diagnostic addresses | 0x7D0 / 0x730 / 0x7B1 | 0x7D0 radar/SCC, 0x730 camera, 0x7B1 additional ECU — community-verified diagnostic addresses from opendbc Hyundai port (ECU disable during openpilot operation). | [B] |
| KWP2000-over-CAN (transition era) | KWP2000 on ISO 15765 transport | 2005-~2010 CAN Hyundais likely speak KWP2000 on the CAN transport, NOT UDS. A UDS-only tool will fail against these — send KWP2000 session start or verify first. | [B] |

### Gateways

#### Gateway modules (U0146-U0150) [C] (varies)

- Effect: DTC documentation references gateway modules A/B/C/D/E. Topology and any diagnostic firewalling on 2021+ platforms UNCONFIRMED [?]. No Stellantis-SGW equivalent found — do not assume one exists.
- Evidence: OEM-HYUNDAI-COMM

### Tool ecosystem

- **GDS / GDS-Mobile** — Hyundai/Kia OEM tool; one VCI covers both brands. VCI II adds FlexRay/Bluetooth/Wi-Fi. Ships 16-to-12, 16-to-20, 10-8-2 adapters for pre-OBD-II vehicles.

### Seed/key policy

NO PUBLIC HYUNDAI/KIA UDS 0x27 ALGORITHM — none found, none invented. Immobilizer/key programming is PIN-GATED (6-digit newer, 4-digit older), dealer/third-party sourced — not seed/key-computed.

## Nissan / Infiniti [B]

- Protocol: KWP2000-style (0x10 0xC0 + 0x21); UDS 0x22 REJECTED (NRC 0x12)
- Evidence: OEM-NISSAN-COMM (2018 Pathfinder capture project)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Physical addressing | 0x7E0 -> 0x7E8 | ECM request 0x7E0, response 0x7E8; TCM/CVT at 0x7E9; functional 0x7DF. Standard ISO 15765-4 layout. | [B] |
| KWP-style local-ID reads | 0x10 0xC0 then 0x21 | Nissan enhanced diagnostics answer DiagnosticSessionControl 0x10 0xC0 + readDataByLocalIdentifier 0x21. A strict UDS scanner sending 0x22 gets NRC 0x12 — Marcus UDS mode should offer a KWP-0x21 fallback for Nissan targets. | [B] |
| DDL command set (legacy) | DDL bytes | 0xD1 read DTCs, 0xC1 clear DTCs, 0x51 clear transient DTCs, 0xD0 read ECU part number, 0x5A start sensor stream, 0xC9 read ROM/RAM, 0x0A active tests. | [B] |
| Legislated OBD-II | Modes 0x01-0x0A | On main CAN 6/14. Always available on CAN-era vehicles. | [A] |

### Gateways

#### BCM CAN-gateway [B] (2018+ (Pathfinder confirmed))

- Effect: On gatewayed models the OBD-II port carries DIAGNOSTIC REQUEST/RESPONSE TRAFFIC ONLY. Passive sniffing sees ZERO frames — that is normal, not a fault. Raw inter-module traffic requires a physical internal-bus tap.
- Evidence: OEM-NISSAN-COMM (Pathfinder project)

### Tool ecosystem

- **CONSULT-II / CONSULT-III plus** — Dealer tools across eras. CONSULT-III plus requires selecting the correct "CAN type" per model family (per 2024 TSB).
- **DDL-aware tools (legacy)** — Nissan DataScan, ECUtalk, Nistune, open-source cansult. ELM327/STN chips do NOT speak DDL.

### Seed/key policy

NO PUBLIC NISSAN SEED/KEY ALGORITHM — none found, none invented. NATS/NVIS uses a PIN-to-password scheme via dealer systems; key registration ERASES ALL existing key IDs first — a half-finished procedure can leave zero working keys.

## Subaru [B]

- Protocol: SSM2 (proprietary, K-line 4800 bps 8N1) + ISO 15765-4 CAN 11-bit 500k (2008+); SSM-III/SSM4 (dealer)
- Evidence: OEM-SUBARU-SSM (RomRaider SsmProtocol doc); OEM-SUBARU-FSM (2011 Legacy FSM DLC page); OEM-SUBARU-COMM (FreeSSM/BtSsm docs)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| SSM2 ECU init / address read / block read | SSM commands 0xBF / 0xA8 / 0xA0 (dest 0x10 = ECM, 0x18 = TCU) | Packet: 0x80 DEST SRC LEN CMD data CHECKSUM. 0xBF init returns ECU ID + capability bitmap (bytes 9+ = per-parameter support flags). 0xA8 reads 3-byte RAM addresses (§4 parameter catalog). Memory-address-oriented, not service-oriented — no modes/PIDs. | [B] |
| Legislated OBD-II | 0x7DF / 0x7E0-0x7E7 (+8 responses) | Standard emissions OBD-II on HS CAN 6/14, 2008+. No Subaru-specific deviation found. | [B] |
| FreeSSM / BtSsm (community tools) | SSM2 over K-line | FreeSSM: read/clear generic + manufacturer DTCs, live measuring blocks, adjustments, actuator tests; no ECU reprogramming, no key programming. BtSsm: Android SSM logging/gauges. ELM327 adapters are INCOMPATIBLE with SSM (protocol limitation). | [B] |

### Gateways

#### BIU (Body Integrated Unit) [B] (2005+)

- Effect: Central body-control module on HS-CAN; participates in LAN diagnostics (U1201/U1202, C0046). Whether it protocol-converts between HS-CAN and CAN-LS is INFERRED, not verified.
- Evidence: OEM-SUBARU-FSM (FSM LAN-diag DTC tables)

### Tool ecosystem

- **FreeSSM** — Open-source SSM2 via FTDI FT232RL cable (VAG-KKL 409.1; CH340 clones do not work) or Tactrix OpenPort. 1999-2009 (+2010 partial).
- **BtSsm** — Android SSM K-line logging/gauges via OTG-USB or Bluetooth; experimental CAN mode works on 2015-2019 WRX.
- **SSM-III / SSM4 (dealer)** — Hitachi HDS3000 (1998-2018) / Denso DST-i (2016+). Full-system diagnosis, bidirectional tests, ECU reprogramming, key programming.

### Seed/key policy

No public Subaru UDS 0x27 seed/key algorithm was found. None is invented or reproduced here. Immobilizer DTCs (P1570-P1578) and key registration go through SSM3/SSM4 with dealer-issued codes — not something an M2 implementation should attempt.

## Mazda [B]

- Protocol: UDS/ISO-TP on HS-CAN (+8 response offset); SCP J1850 PWM (Ford era); M-MDS dealer tool
- Evidence: OEM-MAZDA-COMM (Mazda Vehicle Networks training doc; FORScan community)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Physical addressing (+8 response offset) | 0x7E0 -> 0x7E8 | Ford-family convention carried to Mazda: PCM request 0x7E0, response 0x7E8. Standard emissions OBD-II (SAE J1979) on 6/14 works with any generic tool. | [B] |
| Functional (broadcast) diagnostics | 0x7DF | Follows the Ford/ISO-15765 convention. | [C] |
| As-built-style configuration | manufacturer-specific | Ford-format as-built records (7E0-01-01 lines) appear in FORScan Mazda workflows on Ford-era models. Whether SkyActiv models retain Ford-style as-built block addressing is UNVERIFIED. | [C] |
### Tool ecosystem

- **M-MDS (Mazda Modular Diagnostic System)** — Mazda dealer tool; earlier WDS (Ford-shared) and IDS on shared platforms.
- **FORScan** — Supports Mazda 1996-2024 (HS+MS CAN with switched adapter; extended license for module configuration). The practical aftermarket path for module-level work.

### Seed/key policy

No public Mazda seed/key (UDS 0x27) algorithm was found. None is invented or reproduced here. Immobilizer work (P1260-class, key programming after PCM replacement) is documented as requiring M-MDS/IDS at the dealer. Read-only diagnostics and standard UDS services are the in-scope surface.

## BMW [B]

- Protocol: KWP2000-over-CAN (0x6F1 scheme, E-series) -> UDS over DoIP (F/G-series)
- Evidence: OEM-BMW-COMM (bimmerforums E90 CAN project, corroborated against EDIABAS/Tool32 job definitions)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| E-series D-CAN diagnostics (0x6F1 scheme) | 0x6F1 tester->ECU / 0x600+moduleID ECU->tester | Request: 0x6F1: [moduleID] [len] [cmd0..cmd5]. Response: 0x6XX: [0xF1] [0x10] [len] [data...]. Command bytes = KWP2000 service/subfunction numbers (EDIABAS Tool32 jobs). 0xEF = broadcast, 0xF1 = tester address. Partial module IDs: 0x00 JBBF, 0x01 MRS, 0x40 CAS, 0x60 KOMBI, 0x72 FRM, 0x78 IHKA. | [B] |
| Legislated OBD-II | SAE J1979 modes | On 6/14, 2008+ (US) / 2001+ petrol, 2004+ diesel (EU). | [A] |
| F/G-series UDS over DoIP | DoIP (ISO 13400) | Primary diagnostic protocol on F/G-series; CAN-side diagnostics go through the ZGW/BDC gateway. ENET cable on OBD 3/11/12/13. | [B] |

### Gateways

#### JBE/JBBF (E90) [B] (E-series)

- Effect: Gateway between PT-CAN and K-CAN (F-CAN pass-through). Diagnostics for K-CAN modules are routed, not direct; K-CAN is not on the DLC.
- Evidence: OEM-BMW-TRAIN (E90 General Vehicle Electrical manual)

#### ZGM in FEM (F30) [B] (F-series)

- Effect: Central gateway routing all buses; contains FlexRay star coupler. CAN-side diagnostic frames are encapsulated (e.g. CAN->FlexRay); raw PT-CAN/K-CAN2/FlexRay traffic is NOT on the DLC.
- Evidence: OEM-BMW-TRAIN (F30 Complete Vehicle training)

#### BDC / BDC3 (G-series) [B] (2015+)

- Effect: Body Domain Controller replaces FEM as central gateway and core immobilizer/security module. CAN FD + DoIP world.
- Evidence: OEM-BMW-COMM (obdii365 BDC3 case study)

### Tool ecosystem

- **ISTA (Rheingold)** — BMW dealer diagnostic/programming software.
- **E-Sys** — F/G-series coding/flashing over ENET.
- **INPA / NCS Expert / Tool32 / WinKFP (EDIABAS suite)** — E-series diagnostics, coding, module flashing via K+DCAN cable.
- **ICOM / ICOM Next** — BMW dealer interface for DoIP + MOST + all buses.

### Seed/key policy

BMW UDS 0x27 security access for flashing/programming exists but no public algorithm is documented; none is invented or reproduced here. Immobilizer (EWS/CAS/FEM/BDC + DME ISN alignment) is dealer or licensed-specialist territory. Read-side operations (passive logging, OBD-II, E-series 0x6F1 reads, fault-memory reads) need none of that.

## Mercedes-Benz [B]

- Protocol: KWP2000 over CAN (0x4xx/0x5xx IDs, pre-UDS) -> UDS with non-standard arbitration IDs (W204+)
- Evidence: OEM-MERCEDES-COMM (mercedes-hacking-docs Ch. 1/3; scainner RESEARCH.md)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| KWP2000-era diagnostics | 0x04E0 tester->ECU / 0x05FF ECU->tester (observed) | W203/W211 era: diagnostic addressing in the 0x4xx/0x5xx CAN-ID range, not 0x7xx (single community XENTRY-passthru capture). | [C] |
| UDS (non-standard arbitration IDs) | e.g. 0x300 (model-specific) | Mercedes does NOT use 0x7DF-0x7E7. UDS probing must use lower IDs (0x300 suggested by community), but the real per-module table is undocumented (XENTRY CBF files; community parser DMCA'd). The gateway silently drops unrecognized diagnostic IDs — non-response means 'filtered', not 'module absent'. | [B] |
| Legislated OBD-II | SAE J1979 modes | On 6/14 for CAN-2.0 models. 2021+ secure gateway may gate even reads. | [A] |
| Wake-up frames | model-specific CAN IDs | Modules sleep with the car off; a per-model wake-up frame is required before the bus carries traffic (e.g. W203: ID 001C, DLC 8, payload 02 10 92 00 00 00 00 00). W204/W205/W212/W213 frames not in the crowd-sourced table. | [B] |

### Gateways

#### CGW / N93 (central gateway) [A] (W203/W209/W211/W219 era (~2000-2009))

- Effect: Gateway between CAN-C and CAN-B (and CAN-D); monitors CAN-B modules, produces DTCs for CAN-B communication problems. The OBD-II port is FILTERED: reads pass, only diagnostic CAN IDs may be written; arbitrary frame injection from the DLC is rejected.
- Evidence: OEM-MERCEDES-DOC (Daimler GF54.21-P-4170GZ; W211 training)

#### ZGW (W204 era) [C] (~2007-2016)

- Effect: Gateway function continues; naming mixed with CGW in community sources.
- Evidence: OEM-MERCEDES-COMM (community/aftermarket sources)

#### Secure Gateway (2021+) [C] (W223/W206+)

- Effect: Firewall preventing any OBD-II communication without authentication — blocks reads, live data, DTC reads and bidirectional functions until authenticated. Legitimate path: dealer/XENTRY online.
- Evidence: OEM-MERCEDES-COMM (iSCAN video description)

### Tool ecosystem

- **XENTRY** — Current dealer diagnostic platform (fault read/erase, live data, adaptations, coding, programming).
- **DAS** — Diagnosis Assistance System for older models (roughly pre-2015).
- **Vediamo / DTS Monaco** — Engineering-level tools for deep coding/programming.

### Seed/key policy

No public Mercedes UDS 0x27 algorithm was found. None is invented or reproduced here. Security-gated operations (immobilizer/key learning on DAS-3, component protection, SCN coding) are dealer/XENTRY-online territory. Whether ordinary read DIDs need 0x27 on Mercedes is unknown — treat NRC 0x33 as 'skip this DID'.

## Volvo [B]

- Protocol: Proprietary Volvo diagnostic protocol (P1/P2/P3); UDS over DoIP (SPA/CMA)
- Evidence: OEM-VOLVO-COMM (opendbc volvo DBCs: diagXxxReq/Resp frames with opaque payloads)

### Services

| Service | ID | Support | Grade |
|---|---|---|---|
| Proprietary diagnostic addressing (P1/P2/P3) | 0x726/0x72E (CEM), 0x730/0x738 (PSCM), 0x764/0x76C (FSM), 0x793/0x79B (CVM); 0x7DF functional | +8 response offset (same convention as Toyota). The 0x72x-0x79x addressing does NOT follow the generic 0x7E0/0x7E8 OBD pattern. Engine-ECM diagnostic addressing not verified. Volvo-specific diagnostics beyond emissions need DiCE + VIDA or a Volvo-aware third-party tool. | [B] |
| Legislated OBD-II | SAE J1979 modes | Standard modes on HS-CAN 6/14, 2005+. | [A] |
| DoIP diagnostics (SPA/CMA) | DoIP (ISO 13400) via VOE adapter | VIDA connects via the OBD connector with an Ethernet cable through a VOE adapter (Volvo p/n 9513108 / 9513062). OUT OF M2 SCOPE. | [B] |

### Gateways

#### CEM (Central Electronic Module) [B] (P1/P2/P3)

- Effect: Inter-bus gateway between HS-CAN and LS-CAN. Supervises LS-CAN nodes (CEM-1A51-1A64 communication DTCs). CEM<->ECM immobilizer pairing uses SYNC + ABS_ID on CAN 0x7FC-0x7FF.
- Evidence: OEM-VOLVO-VADIS (CAN-bus diagnostics overview)

### Tool ecosystem

- **VIDA + DiCE** — Volvo dealer diagnostic software; full-system DTC read/clear, live data, software downloads, module programming, key programming. Paid subscription; software downloads are per-VIN from Volvo servers.
- **VDASH / VDD / V-Tool** — Community Volvo-aware tools; configuration changes via decoded CEM PIN (method not documented here).

### Seed/key policy

No public Volvo UDS 0x27 algorithm exists in the sources consulted, and none is invented or reproduced here. Security-gated work (module software, keys, CEM configuration) is dealer/paid-VIDA territory.

_Generated by scripts/build.py — do not hand-edit._
