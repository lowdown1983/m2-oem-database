# Subaru — In-Vehicle Networks, SSM Protocol & Diagnostic Access

Research for the M2 OEM vehicle database. Every factual claim carries a
quality grade: **A** = factory documentation or verified capture ·
**B** = reputable community source (opendbc, well-documented
reverse-engineering, trade/technician sources, factory-manual excerpts via
third-party hosts) · **C** = single anecdotal report. Unverified items are
marked [?]. Research date: 2026-10-07.

Subaru's diagnostic story is dominated by its proprietary **Subaru Select
Monitor (SSM)** protocol family, documented in §3 as its own protocol,
distinct from UDS.

---

## 1. Bus architecture

### 1.1 CAN buses

- Subaru's primary diagnostic bus is **high-speed CAN at 500 kbps** on DLC
  pins **6 (CAN-H) / 14 (CAN-L)** [A — 2011 Legacy FSM "Data Link Connector"
  page: terminal 6 = "CAN communication (Hi)", 14 = "CAN communication
  (Lo)"; B — Subaru Diesel Crew CAN-message reverse-engineering: "15
  CAN-IDs to be found on the high-speed bus (500 kbps, easily available via
  OBD-II connection)", MY2009/2010 Impreza].
- The U1201 diagnostic procedure (FSM LAN diagnostics) instructs the
  technician to connect a **120 Ω resistance between CAN-Hi and CAN-Lo**
  when the ECM or VDC control module is disconnected, confirming standard
  120 Ω end termination on the HS bus [A — FSM excerpt via justanswer.com
  transcription].
- A **low-speed CAN (CAN-LS)** exists as a separate network: DTC **U1321
  "CAN-LS METER NO-RECEIVE DATA"** (possible combination-meter fault) is
  listed in the 2011 Impreza FSM LAN-diagnostics DTC table [A]. Its bitrate
  and DLC presence were not documented in sources consulted [?].
- An early dual-bus layout is described for the 2005 Legacy: "two CAN
  buses in the '05, one between BIU and Combination meter, and one between
  BIU and Steering Angle Sensor, ECM, TCM (for AT vehicles), VDC and ABS"
  [C — legacygt.com owner post with wiring-diagram screenshots].

### 1.2 Gateway / Body Integrated Unit (BIU)

- The **Body Integrated Unit (BIU)** is Subaru's central body-control
  module (black box right of the steering column on 2005+ Legacy) and
  participates in CAN diagnostics: the FSM LAN-diagnostics DTC tables list
  the BIU as a reporting/detecting node for HS-CAN faults (U1201/U1202
  columns), and DTCs such as C0046 ("Body Integrated Module Communication
  Circuit") and U1201/U1202 reference shorts "near the body integrated
  unit 1" [A — 2010–2013 Legacy FSM LAN(diag) DTC tables].
- The BIU also holds part of the immobilizer system: replacing a BIU
  requires recoding keys/ECU sync with dealer software [C — club.liberty
  forum; consistent with immobilizer DTCs P1570–P1578].
- Whether the BIU performs protocol conversion/gatewaying between HS-CAN
  and CAN-LS (like Toyota's gateway ECU) is **INFERRED, not verified** [C]:
  it sits on both networks per the DTC tables, but no source describes an
  explicit gateway function. Treat as an open item [?].

### 1.3 CAN FD presence

- **No verified CAN FD on native Subaru platforms.** The only CAN FD
  mention in the Subaru context found is the **Solterra 2023**, which the
  comma.ai openpilot wiki lists as "Toyota TSS 3.0 … Toyota B harness, CAN
  FD, SecOC signed" — i.e. a Toyota-platform vehicle, not a native Subaru
  architecture [B — comma.ai openpilot wiki].
- One aftermarket scanner vendor page claims "advanced CAN FD
  functionality required in newer Outback models (2020+)" [C — accio.com
  vendor marketing, uncorroborated]. The openpilot community supports the
  2023–2025 Outback and 2024–2025 Crosstrek with standard-CAN harnesses
  (Subaru D harness), which weighs against CAN FD on the diagnostic bus
  [B — comma.ai openpilot wiki].
- **M2 implication:** the M2 is CAN 2.0 only (TJA1051). Any CAN FD traffic
  is out of M2 scope; none is expected on the DLC of native-Subaru models
  [B/C].

### 1.4 Model-year evolution

- **1999–2007 (EJ era):** SSM2 over K-line (DLC pin 7) is the diagnostic
  path; no CAN at the DLC. FreeSSM covers 1999–2009 [B — FreeSSM/obdii365].
- **~2008+:** CAN (ISO 15765-4, 500k, 11-bit) becomes the legislated OBD-II
  transport; SSM continues in parallel (SSM-III CAN mode). AiM's
  protocol-by-model table lists Impreza 1999–2007 as "SUBARU - SSM" and the
  2008 N14 Impreza as "SUBARU - SSM 2008/2009" with CAN "under development"
  [C — AiM/scribd table; consistent with the 2008 US CAN mandate, A].
- **2017+ (Subaru Global Platform):** single HS-CAN architecture at the
  DLC; EyeSight driver-assist traffic on the HS bus (opendbc
  `subaru_global_2017` DBC) [B — local opendbc clone].
- **2016+:** SSM4 (dealer tool) supersedes SSM3; community tools
  (FreeSSM/BtSsm) stop being useful — "newer ones have moved away from SSM
  and to E-OBDII" [C — legacygt.com BtSsm tester post].

---

## 2. Diagnostic access

### 2.1 DLC pinout (2011 Legacy FSM, ENGINE (DIAGNOSTICS) §7) [A]

| Pin | Function |
|---|---|
| 4, 5 | Ground |
| 6 | CAN communication (Hi) |
| 7 | **Subaru Select Monitor signal** |
| 14 | CAN communication (Lo) |
| 16 | Power supply |
| 1, 2, 3, 8, 9, 10, 11, 12, 13, 15 | Blank |

- The FSM note reads: "This connector is used for Subaru Select Monitor"
  with a caution to connect only SSM or a general scan tool [A].
- Caution: Subaru's own wiring diagrams draw the DLC with the narrow edge
  uppermost, mirroring the standard J1962 pin numbering — always verify
  against the standard wide-edge-up layout before probing [C —
  subaru-svx.net b3lha post].
- Pin 7 is the SSM K-line: "if pin 7 is available, at least the engine
  control unit should be available" (FreeSSM coverage notes) [B]. On
  CAN-era cars pin 7 remains the SSM line — a 2009 Outback works with
  FreeSSM over a KKL cable on pin 7 despite having CAN [C — obdii365
  FreeSSM/KKL thread].

### 2.2 Protocols on the DLC

| Protocol | Pins | Era | Notes |
|---|---|---|---|
| SSM2 (K-line, 4800 bps 8N1) | 7 | 1999–~2015 | Proprietary; §3 |
| ISO 15765-4 CAN 11-bit 500k | 6/14 | 2008+ | Legislated OBD-II; SSM-III CAN mode also here |
| SSM-III/SSM4 (dealer) | 6/14 and/or 7 | 2008+ / 2016+ | Hitachi HDS3000 → Denso DST-i interfaces |

### 2.3 Diagnostic CAN IDs

- Standard emissions OBD-II uses the legislated functional address
  **0x7DF** and physical addresses **0x7E0–0x7E7** (responses +8) on the HS
  bus [A — ISO/SAE standard; B — assumed Subaru compliance, no
  Subaru-specific deviation found].
- **No verified Subaru-proprietary diagnostic CAN IDs** (SSM-over-CAN
  frame IDs) were found in public sources [? — open item]. SSM4 works
  through J2534 with CAN, ISO14230, ISO9141 and ISO15765 channels enabled
  (DST-i registry: `"CAN"=dword:00000001, "ISO14230"=dword:00000001,
  "ISO9141"=dword:00000001, "ISO15765"=dword:00000001`) [C — obdii365 SSM4
  setup blog], but the SSM-over-CAN application-layer CAN IDs are not
  publicly documented.
- Subaru-specific UDS (0x22) DIDs: none found in public sources — §4
  documents SSM parameter IDs instead; the UDS DID catalog is an open gap
  [?].

### 2.4 Tool ecosystem

- **FreeSSM** (open source): SSM2 K-line via FTDI FT232RL cable (VAG-KKL
  409.1 with genuine FTDI; CH340 clones do not work) or Tactrix OpenPort;
  reads/clears generic + manufacturer DTCs, live measuring blocks,
  adjustments, actuator/system tests; no ECU reprogramming, no key
  programming [B — obdii365/FreeSSM docs]. Coverage: 1999–2009 (+2010
  partial) Legacy/Outback/Baja/Impreza/Forester/Tribeca/Exiga; SVX, Justy,
  pre-1999 not supported [B].
- **BtSsm** (Android): SSM K-line logging/gauges/Learning View via
  OTG-USB (Tactrix/KKL) or Bluetooth adapter; later versions added TCU
  support and experimental CAN support; works in CAN mode on 2015–2019
  WRX [C — legacygt.com tester posts]. ELM327 adapters are incompatible
  with SSM (protocol, not AT-command, limitation) [C].
- **SSM-III** (dealer): Hitachi HDS3000 interface, MY1998–2018, full-system
  diagnosis, bidirectional tests, ECU reprogramming, key programming [C —
  vendor blogs].
- **SSM4** (dealer, 2016+): Denso DST-i; works with any J2534 interface by
  swapping the DST-i DLL [C — obdii365]. EDR (crash-recorder) reads use
  SSM3/SSM4 raw (.SSM) files [C — Ruth Consulting EDR presentation].
- **Immobilizer/key work is dealer-tool territory:** key programming needs
  SSM3/SSM4 plus a dealer-supplied immobilizer/teaching code obtained with
  proof of ownership [C — vxdiagshop key-programming walkthrough]. **No
  seed/key algorithms are documented or reproduced here.**

### 2.5 Seed/key policy

- **No public Subaru UDS 0x27 seed/key algorithm was found. None is
  invented or reproduced here.**
- Immobilizer DTCs (P1570–P1578, §5) and key registration are handled
  through SSM3/SSM4 with dealer-issued codes — not something an M2
  implementation should attempt.

---

## 3. Subaru Select Monitor (SSM) — proprietary diagnostic protocol

SSM is Subaru's own diagnostic protocol family, **distinct from UDS**.
It is a memory-address-oriented protocol (read/write ECU RAM), not a
service-ID-oriented one. Three generations are attested:

| Generation | Transport | Tool | Era |
|---|---|---|---|
| SSM1 | Serial (dedicated) | Select Monitor cartridges | pre-1999 (SVX era) [C] |
| SSM2 | K-line, UART **4800 bps, 8N1**, ISO9141-compatible levels | FreeSSM, BtSsm, Tactrix | 1999–~2015 [B] |
| SSM3 / SSM4 | CAN (SSM-over-CAN) and/or K-line via J2534 | SSM-III (Hitachi HDS3000), SSM4 (Denso DST-i) | SSM3: 1998–2018; SSM4: 2016+ [C] |

- FreeSSM's own description: SSM2 is "a modified version of the
  ISO-14230-protocol (KWP2000)" and "on the lower layer, fully compatible
  with ISO-9142/14230" [B — obdii365/FreeSSM docs].
- SSM2 and CAN-era SSM coexist: a CAN-bus 2009 Outback still answers SSM2
  on the K-line, and BtSsm's CAN mode works on 2015–2019 WRX [C].
- SSM4's J2534 registry entry enables CAN, ISO14230, ISO9141 and ISO15765
  channels, confirming SSM4 still spans K-line and CAN transports [C].

### 3.1 SSM2 frame format (RomRaider SsmProtocol documentation) [B]

Serial settings: ISO9141 interface, **4800 bps, no parity, 8 data bits,
1 stop bit**.

Packet structure (max ~250 bytes including echoed bytes):

```
0x80 | DEST | SRC | LEN | CMD | data... | CHECKSUM
```

- `DEST`/`SRC`: **0x10** = engine ECU, **0x18** = TCU/DCCD, **0xF0** =
  diagnostic tool.
- `LEN` = number of data bytes following (command byte + parameters).
- `CHECKSUM` = low 8 bits of the sum of every packet byte including the
  0x80 header.

Commands (tool → ECU) and their response codes:

| Cmd | Name | Response | Notes |
|---|---|---|---|
| 0xA0 | Block read | 0xE0 | `A0 PP AA AA AA CC` — PP=0x00 single / 0x01 continuous; 3-byte address; CC = byte count − 1 |
| 0xA8 | Address read | 0xE8 | `A8 PP A1A1A1 A2A2A2 …` — reads listed 3-byte addresses |
| 0xB0 | Block write | 0xF0 | `B0 AA AA AA DD…` — writes bytes to address |
| 0xB8 | Single-address write | 0xF8 | `B8 AA AA AA DD` |
| 0xBF | ECU init | 0xFF | Returns ECU ID + capability bitmap |

Example (from the doc): init request `80 10 F0 01 BF 40` → ECU answers
`80 F0 10 39 FF …` (0x39 data bytes: 5-byte ECU ID followed by capability
bytes) [B].

### 3.2 ECU-init capability bitmap [B]

Bytes 9+ of the 0xBF response are per-parameter support flags (bit = 1 →
parameter readable). Documented bytes 9–56 cover, among others:

- Byte 9: engine load, coolant temp, A/F correction/learning #1/#2,
  manifold absolute pressure, engine speed
- Byte 10: vehicle speed, ignition timing, intake air temp, MAF, throttle
  angle, O2 sensors
- Byte 11: battery voltage, sensor voltages, injector pulse widths, knock
  correction, atmospheric pressure
- Bytes 12–16: manifold relative pressure, fuel tank pressure, learned
  ignition timing, accelerator angle, fuel temp, O2 heaters, fuel level,
  wastegate duties, VVT angles, OCV duties/currents, A/F sensor currents
- Byte 17: gear position; Byte 20: AT vehicle ID, test-mode connector,
  read-memory connector flags; Bytes 21–28: switches/relays/solenoids
  (neutral, idle, A/C, starter, fans, fuel pump, …); Byte 39: throttle
  motor duty/voltage; Byte 41: throttle/accelerator sensors; Byte 44:
  exhaust VVT/OCV; Byte 46: clutch/stop-light/cruise/brake switches;
  Byte 56: roughness monitor cylinders 1–4.

### 3.3 SSM parameter addresses (ECU, dest 0x10) [B]

Parameters are read with command 0xA8 supplying 3-byte addresses. The
representative engine addresses below come from the RomRaider SsmProtocol
document (community reverse-engineering, cross-consistent with
FreeSSM/RomRaider logger definitions). Conversions are quoted as
documented; all are INFERRED-from-RE unless noted.

See §4 for the tabulated catalog with sizes and grades.

### 3.4 SSM3/SSM4 (CAN era)

- SSM-III runs over CAN on 2008+ models (SSM-over-CAN); SSM4 is the
  2016+ dealer tool on the Denso DST-i J2534 interface [C — vendor blogs].
- **SSM-over-CAN CAN IDs and frame format are not publicly documented**
  [? — open item]. BtSsm's experimental CAN mode demonstrates it is
  implementable, but no public frame-format reference was found.
- EDR (event data recorder) retrieval uses SSM3/SSM4: raw data is saved as
  `.SSM` files; SSM3 files (≤2015) export to CSV, SSM4 (2016+) does not
  [C — Ruth Consulting EDR presentation].

### 3.5 What SSM can do (vs. generic OBD-II)

Per FreeSSM's documented abilities [B]: read/clear current and history
DTCs (generic + manufacturer), real-time measuring blocks (data and
switches), adjustment values (engine/transmission), system component
tests / actuator tests (engine), and customization/coding. ECU
reprogramming and key programming are dealer-SSM3/SSM4-only (not in
FreeSSM) [B].

---

## 4. Parameter catalog — SSM2 ECU addresses (and UDS DID gap)

**No Subaru-specific UDS service-0x22 DIDs were found in any public
source** — this is an explicit gap, not an omission [?]. What *is*
documented is the SSM2 parameter address map: 3-byte ECU memory addresses
read with SSM command **0xA8** (address read), destination byte **0x10**
(engine ECU). Entries below follow the DID entry format; "Session" and
"Security" are marked n/a because SSM2 has no session/security concept.
All conversions are quoted from the RomRaider SsmProtocol document
(community reverse-engineering; INFERRED unless cross-checked).

Conventions: `P0xNNN` = 3-byte address (e.g. `0x000008`); multi-byte
values are big-endian (high byte at the lower address).

## SSM 0x000007
- Name: EngineLoad
- Description: Engine load, 8-bit, value × 100 / 255 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 7)

## SSM 0x000008
- Name: CoolantTemperature
- Description: Coolant temperature, 8-bit, value − 40 = °C.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 6); worked example reads 0x000008 returning 0x7D in the doc

## SSM 0x000009
- Name: AfCorrection1
- Description: Air/fuel correction #1, 8-bit, (value − 128) / 1.28 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 5)

## SSM 0x00000A
- Name: AfLearning1
- Description: Air/fuel learning #1, 8-bit, (value − 128) / 1.28 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 4)

## SSM 0x00000B
- Name: AfCorrection2
- Description: Air/fuel correction #2, 8-bit, (value − 128) / 1.28 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 3)

## SSM 0x00000C
- Name: AfLearning2
- Description: Air/fuel learning #2, 8-bit, (value − 128) / 1.28 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 2)

## SSM 0x00000D
- Name: ManifoldAbsolutePressure
- Description: Manifold absolute pressure, 8-bit, value × 37 / 255 = psig.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 1)

## SSM 0x00000E-0x00000F
- Name: EngineSpeed
- Description: Engine speed, 16-bit big-endian (0x0E = high byte), value / 4 = RPM.
- Make: subaru
- Size: 2 bytes
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 9, bit 0); worked example reads 0x00000E/0x00000F

## SSM 0x000010
- Name: VehicleSpeed
- Description: Vehicle speed, 8-bit, km/h.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 7)

## SSM 0x000011
- Name: IgnitionTiming
- Description: Ignition timing, 8-bit, (value − 128) / 2 = degrees.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 6)

## SSM 0x000012
- Name: IntakeAirTemperature
- Description: Intake air temperature, 8-bit, value − 40 = °C.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 5)

## SSM 0x000013-0x000014
- Name: MassAirFlow
- Description: Mass air flow, 16-bit big-endian (0x13 = high byte), value / 100 = g/s.
- Make: subaru
- Size: 2 bytes
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 4)

## SSM 0x000015
- Name: ThrottleOpeningAngle
- Description: Throttle opening angle, 8-bit, value × 100 / 255 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 3)

## SSM 0x000016-0x000017
- Name: FrontO2Sensor1
- Description: Front O2 sensor #1, 16-bit big-endian, value × 0.005 = volts.
- Make: subaru
- Size: 2 bytes
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 2)

## SSM 0x000018-0x000019
- Name: RearO2Sensor
- Description: Rear O2 sensor, 16-bit big-endian, value × 0.005 = volts.
- Make: subaru
- Size: 2 bytes
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 1)

## SSM 0x00001A-0x00001B
- Name: FrontO2Sensor2
- Description: Front O2 sensor #2, 16-bit big-endian, value × 0.005 = volts.
- Make: subaru
- Size: 2 bytes
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 10, bit 0)

## SSM 0x00001C
- Name: BatteryVoltage
- Description: Battery voltage, 8-bit, value × 0.08 = volts.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 7); worked example reads 0x00001C returning 0xB1

## SSM 0x00001D
- Name: AirFlowSensorVoltage
- Description: Air flow sensor voltage, 8-bit, value × 0.02 = volts.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 6)

## SSM 0x00001E
- Name: ThrottleSensorVoltage
- Description: Throttle sensor voltage, 8-bit, value × 0.02 = volts.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 5)

## SSM 0x000020
- Name: FuelInjection1PulseWidth
- Description: Fuel injection #1 pulse width, 8-bit, value × 0.256 = ms.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 3)

## SSM 0x000021
- Name: FuelInjection2PulseWidth
- Description: Fuel injection #2 pulse width, 8-bit, value × 0.256 = ms.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 2)

## SSM 0x000022
- Name: KnockCorrection
- Description: Knock correction, 8-bit, (value − 128) / 2 = degrees.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 1)

## SSM 0x000023
- Name: AtmosphericPressure
- Description: Atmospheric pressure, 8-bit, value × 37 / 255 = psig.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 11, bit 0)

## SSM 0x000024
- Name: ManifoldRelativePressure
- Description: Manifold relative pressure, 8-bit, (value − 128) × 37 / 255 = psig (boost pressure on turbo models).
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 12, bit 7)

## SSM 0x000026
- Name: FuelTankPressure
- Description: Fuel tank pressure, 8-bit, (value − 128) × 0.0035 = psig.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 12, bit 5)

## SSM 0x000029
- Name: AcceleratorOpeningAngle
- Description: Accelerator opening angle, 8-bit, value / 2.56 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 12, bit 2)

## SSM 0x00002A
- Name: FuelTemperature
- Description: Fuel temperature, 8-bit, value − 40 = °C.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 12, bit 1)

## SSM 0x00002E
- Name: FuelLevel
- Description: Fuel level sensor, 8-bit, value × 0.02 = volts (sensor voltage, not percent).
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 13, bit 5)

## SSM 0x000030
- Name: PrimaryWastegateDutyCycle
- Description: Primary wastegate duty cycle, 8-bit, value × 100 / 255 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 13, bit 3)

## SSM 0x000031
- Name: SecondaryWastegateDutyCycle
- Description: Secondary wastegate duty cycle, 8-bit, value × 100 / 255 = percent.
- Make: subaru
- Size: 1 byte
- Session: n/a (SSM2)
- Security: n/a
- Grade: [B]
- Evidence: RomRaider SsmProtocol doc (capability byte 13, bit 2)

### Catalog coverage notes (§4)

- TCU parameter addresses (destination 0x18) were not documented in the
  sources consulted [?].
- VVT/OCV/A-F-sensor-current addresses (capability bytes 15–16) and the
  switch/relay bitmap addresses (bytes 21–28) are named in the capability
  list but their numeric addresses were not extracted in this pass [?].
- The RomRaider doc's parameter table continues past secondary wastegate
  duty (CPC valve duty ratio, …) but the fetched text was truncated; the
  addresses above are the verified subset.
- **UDS 0x22 DIDs for Subaru: none found** — no public DID catalog, no
  documented Subaru-specific identifiers in the F1xx identification band
  beyond the ISO standard ones. Open gap [?].

---

## 5. Manufacturer-specific DTCs

Covers Subaru-specific P1xxx/B1xxx/C1xxx/U1xxx only. SAE J2012 generic
codes are NOT duplicated, except where a Subaru-specific note applies.
Grades: [A] = Subaru factory service manual excerpt · [B] = reputable
DTC database or multi-source agreement · [C] = single community source.
"not documented" means the sources consulted gave no cause/note — never
an invitation to guess.

Subaru quirks relevant to DTC work:
- Immobilizer DTCs **P1570–P1578** are reported by the ECM but involve the
  BIU, combination meter, and key — diagnose as a system, not as an
  engine fault [B — FSM immobilizer DTC table].
- **P1718** is Subaru-specific for AT CAN communication faults; it is
  routinely accompanied by U12xx LAN codes — read the LAN system too
  [C — thesubaruforums + FSM LAN-diag table co-occurrence].
- U12xx = HS-CAN node-receive faults, U13xx = LS-CAN faults, per the FSM
  LAN-diagnostics tables [A].
- VDC/ABS codes (C0041–C0054) carry Subaru "detailed codes" (e.g. 1504H,
  5135) shown on SSM alongside the 5-character DTC [A — FSM VDC(diag)
  lists].

---

## P1152
- Description: O2 Sensor Circuit Range/Performance (Low) (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex Subaru list agrees

## P1153
- Description: O2 Sensor Circuit Range/Performance (High) (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex Subaru list agrees

## P1160
- Description: Return Spring Failure
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Throttle-body return-spring plausibility (drive-by-wire era).
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list (single transcription)

## P1400
- Description: Fuel Tank Pressure Control Solenoid Valve Circuit Low
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: EVAP system (fuel tank pressure control solenoid), distinct from the generic P044x EVAP family.
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex agrees

## P1410
- Description: Secondary Air Injection System Switching Valve Stuck Open
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Secondary-air injection (cold-start emissions) — a common Subaru-specific code family.
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex agrees

## P1420
- Description: Fuel Tank Pressure Control Solenoid Valve Circuit High
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Pair to P1400 (circuit low).
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex agrees

## P1443
- Description: Vent Control Solenoid Valve Function Problem
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: EVAP vent control solenoid functional fault (vs. circuit faults).
- Grade: [B]
- Evidence: 2011 Legacy FSM engine-diagnostics DTC reference (jdmcarmanuals.com); OBDCodex agrees

## P1491
- Description: Positive Crankcase Ventilation (Blowby) Function Problem
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: PCV/blowby functional monitor, not a circuit code.
- Grade: [B]
- Evidence: 2007 Legacy FSM engine-diagnostics DTC list (jdmcarmanuals.com); OBDCodex agrees

## P1500
- Description: Radiator Fan Relay 1 Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Subaru Specific Error Codes Guide (scribd.com transcription); troublecodes.net Subaru list agrees

## P1501
- Description: Idle Control System Malfunction (Fail Safe)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Fail-safe idle control fault.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1502
- Description: Radiator Fan Function Problem
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Fan functional fault (vs. P1500 circuit fault).
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1507
- Description: Idle Control System Malfunction (Fail Safe)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1510
- Description: Idle Air Control Solenoid Signal 1 Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1511
- Description: Idle Air Control Solenoid Signal 1 Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1512
- Description: Idle Air Control Solenoid Signal 2 Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1513
- Description: Idle Air Control Solenoid Signal 2 Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1514
- Description: Idle Air Control Solenoid Signal 3 Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1515
- Description: Idle Air Control Solenoid Signal 3 Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1516
- Description: Idle Air Control Solenoid Signal 4 Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1517
- Description: Idle Air Control Solenoid Signal 4 Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1518
- Description: Starter Switch Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Starter-request switch input circuit.
- Grade: [A] description
- Evidence: 2007 Legacy FSM + 2011 Legacy FSM engine-diagnostics DTC lists (jdmcarmanuals.com)

## P1520
- Description: Cooling Fan Relay 1 Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Pair to P1500 (circuit malfunction).
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list (single transcription)

## P1540
- Description: Vehicle Speed Sensor Malfunction 2
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1544
- Description: Exhaust Gas Temperature Too High
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: High exhaust-temperature detection (turbo models).
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1560
- Description: Back-Up Voltage Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: ECM keep-alive/backup power circuit — check ECM backup power supply.
- Grade: [A] description
- Evidence: 2007 Legacy FSM + 2011 Legacy FSM engine-diagnostics DTC lists (jdmcarmanuals.com)

## P1570
- Description: Antenna
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: faulty immobilizer antenna / key communication coil
- Diagnostic notes: Immobilizer system. Key registration and antenna diagnosis are SSM3/SSM4 dealer procedures.
- Grade: [A] description; [B] causes/notes
- Evidence: 2011 Legacy FSM immobilizer DTC list (jdmcarmanuals.com: "P1570 Antenna — Faulty antenna"); Outback immobilizer DTC table (yumpu.com)

## P1571
- Description: Reference Code Incompatibility
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: reference code incompatibility between body integrated unit and ECM
- Diagnostic notes: Immobilizer system — BIU/ECM pairing mismatch.
- Grade: [A] description; [B] causes
- Evidence: 2011 Legacy FSM immobilizer DTC list (jdmcarmanuals.com); Outback immobilizer table

## P1572
- Description: IMM Circuit Failure (Except Antenna Circuit)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: communication failure between body integrated unit and ECM; combination meter and BIU registration failure
- Diagnostic notes: Immobilizer system (non-antenna circuit).
- Grade: [A] description; [B] causes
- Evidence: 2007/2011 Legacy FSM immobilizer DTC lists (jdmcarmanuals.com); Outback immobilizer table

## P1574
- Description: Key Communication Failure
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: communication failure between key and body integrated unit
- Diagnostic notes: Immobilizer system.
- Grade: [A] description; [B] causes
- Evidence: 2007/2011 Legacy FSM immobilizer DTC lists (jdmcarmanuals.com); Outback immobilizer table

## P1576
- Description: EGI Control Module EEPROM
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: ECM malfunctioning (EEPROM)
- Diagnostic notes: Immobilizer system — ECM-side EEPROM fault.
- Grade: [A] description; [B] causes
- Evidence: 2007/2011 Legacy FSM immobilizer DTC lists (jdmcarmanuals.com); Outback immobilizer table

## P1577
- Description: IMM Control Module EEPROM
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: body integrated unit malfunctioning (EEPROM)
- Diagnostic notes: Immobilizer system — BIU-side EEPROM fault.
- Grade: [A] description; [B] causes
- Evidence: 2007/2011 Legacy FSM immobilizer DTC lists (jdmcarmanuals.com); Outback immobilizer table

## P1578
- Description: Meter Failure
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: reference code incompatibility between combination meter and BIU; communication failure between BIU and ECM
- Diagnostic notes: Immobilizer system — combination-meter involvement.
- Grade: [A] description; [B] causes
- Evidence: 2007/2011 Legacy FSM immobilizer DTC lists (jdmcarmanuals.com); Outback immobilizer table

## P1590
- Description: Neutral Position Switch Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1591
- Description: Neutral Position Switch Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Pair to P1590.
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1592
- Description: Neutral Position Switch Circuit (MT Model)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Manual-transmission variant.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1594
- Description: Automatic Transaxle Diagnosis Input Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: AT diagnosis input signal family (P1594/P1595/P1596).
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1595
- Description: Automatic Transaxle Diagnosis Input Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1596
- Description: Automatic Transaxle Diagnosis Input Signal Circuit High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1602
- Description: Control Module Programming Error
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: ECM programming/flash integrity fault.
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list (single transcription)

## P1698
- Description: Engine Torque Control Cut Signal Circuit Malfunction (Low Input)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: ECM↔TCM torque-control interface (AT torque-down request line).
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1699
- Description: Engine Torque Control Cut Signal Circuit Malfunction (High Input)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Pair to P1698.
- Grade: [C]
- Evidence: OBDCodex Subaru manufacturer-specific list; Subaru Specific Error Codes Guide agrees [B on description]

## P1700
- Description: Throttle Position Sensor Circuit Malfunction (A/T)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: AT-related TPS circuit code.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1701
- Description: Cruise Control Set Signal Circuit Malfunction (A/T)
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1702
- Description: Auto Trans Diagnosis Input Signal Circuit
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Related to the P1594/P1595/P1596/P1722/P1742 family.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1703
- Description: Low Clutch Timing Control Solenoid Valve Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: AT clutch timing solenoid.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1704
- Description: 2-4 Brake Timing Solenoid Valve Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: AT 2-4 brake timing solenoid.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1705
- Description: 2-4 Brake Pressure Solenoid Valve (Solenoid D) Circuit
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: AT 2-4 brake pressure solenoid.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1711
- Description: Engine Torque Control Signal 1 Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: ECM↔TCM torque-control interface, channel 1.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1712
- Description: Engine Torque Control Signal 2 Circuit Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: ECM↔TCM torque-control interface, channel 2.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1718
- Description: AT CAN Communication Circuit
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: CAN communication line fault (ECM↔TCM/BIU); wiring harness, grounds, power, CAN twisted pair
- Diagnostic notes: 2006 Legacy GT owner report: "P1718 code meaning an issue with the CAN communication circuit". Appears in the FSM LAN-diagnostics tables alongside U1201/U1221 — always read the LAN system DTCs together with it. On a 2005+ vehicle, check harness grounds (the DLC shares a ground point with the BIU) before condemning modules.
- Grade: [C] description; [B] notes (FSM table co-occurrence + field report)
- Evidence: thesubaruforums.com BIU-diagnostics thread (2006 Legacy GT); 2010–2013 Legacy FSM LAN(diag) DTC tables (P1718 in ECM column with U1201/U1221)

## P1722
- Description: Auto Trans Diagnosis Input Signal High Input
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Related to the P1594/P1595/P1596/P1702/P1742 family.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

## P1742
- Description: Auto Trans Diagnosis Input Signal Malfunction
- Category: P
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Related to the P1594/P1595/P1596/P1702/P1722 family.
- Grade: [C]
- Evidence: Subaru Specific Error Codes Guide (scribd.com, single transcription)

---

## B1100
- Description: Integ. Unit System Error
- Category: B
- Scope: manufacturer (Subaru)
- Possible causes: internal fault in the body integrated unit
- Diagnostic notes: From the FSM LAN-diagnostics DTC table; BIU-internal fault (vs. communication faults U12xx).
- Grade: [A] description; [B] causes
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com: "B1100 INTEG. UNIT SYSTEM ERROR — There could be a problem in the body integrated unit")

## B1500
- Description: Keyless UART Communication Malfunction
- Category: B
- Scope: manufacturer (Subaru)
- Possible causes: internal problem in the keyless entry control module, or a problem in the communication line
- Diagnostic notes: Keyless-entry UART link fault (BIU system).
- Grade: [A]
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com: "B1500 KEYLESS UART COM. MALFUNCTION")

---

## C0041
- Description: Parameter Selection Error
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: parameter selection failure (VDC control module configuration)
- Diagnostic notes: VDC system. Detailed codes 5148/5149.
- Grade: [A]
- Evidence: 2010 Legacy FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0042
- Description: Power Supply Voltage Failure
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: power voltage malfunction to the VDC control module
- Diagnostic notes: VDC system. Check power/ground to the VDCCM&H/U before condemning the module. Detailed code 5000/5001.
- Grade: [A]
- Evidence: 2010 Legacy FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0044
- Description: TCM Communication Circuit
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: CAN communication failure of transmission control module
- Diagnostic notes: VDC system view of a TCM communication loss. Detailed codes 5137/5140/5142.
- Grade: [A]
- Evidence: 2010 Legacy FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0045
- Description: TCM Malfunction / Incorrect VDC Control Module Specifications
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: malfunction of transmission control module; different VDC control module specification
- Diagnostic notes: VDC system. Detailed codes 5144/5146.
- Grade: [A]
- Evidence: 2010 Legacy FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0046
- Description: Body Integrated Module Communication Circuit
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: body integrated module communication circuit fault
- Diagnostic notes: VDC system view of a BIU communication loss. Detailed code 5155.
- Grade: [A]
- Evidence: 2010 Legacy FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0047
- Description: Improper CAN Communication
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: CAN communication line circuit is open or shorted
- Diagnostic notes: Detecting condition (FSM): CAN communication line circuit open or shorted. Symptoms: ABS and VDC do not operate. Detailed codes 1504H–15C0H family; FSM detailed code 5135. Diagnose the physical CAN pair, not the module, first.
- Grade: [A]
- Evidence: 2007–2013 Tribeca/Legacy/Impreza FSM VDC(diag) diagnostic procedures (jdmcarmanuals.com, multiple model years agree)

## C0051
- Description: Valve Relay
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: VDC valve relay circuit fault
- Diagnostic notes: VDC hydraulic control unit valve relay. Detailed codes 021FH/0220H/0221H/0280H.
- Grade: [A] description; [B] causes (INFERRED from name — flagged)
- Evidence: 2010/2011 Impreza FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0052
- Description: Motor and Motor Relay OFF Failure / ON Failure / Motor Malfunction
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: VDC pump motor / motor relay fault
- Diagnostic notes: VDC hydraulic unit pump motor circuit. Detailed codes 0562H/0574H/0580H/05A0H/0560H/04B0H.
- Grade: [A] description; [B] causes (INFERRED from name — flagged)
- Evidence: 2010 Impreza FSM VDC(diag) DTC list (jdmcarmanuals.com)

## C0054
- Description: BLS Circuit Open / BLS ON Malfunction
- Category: C
- Scope: manufacturer (Subaru)
- Possible causes: brake lamp switch (BLS) circuit open or stuck ON
- Diagnostic notes: VDC system monitors the brake lamp switch input. Detailed codes 04B0H/043CH.
- Grade: [A] description; [B] causes (INFERRED from name — flagged)
- Evidence: 2010 Impreza FSM VDC(diag) DTC list (jdmcarmanuals.com)

---

## U1201
- Description: CAN-HS Counter Abnormal
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: unstable high-speed CAN communication (high-speed CAN communication error); faulty control module on the HS bus
- Diagnostic notes: FSM detecting condition: "Communication is unstable due to a high-speed CAN communication error." Symptoms: combination-meter fault display; possible control issues. Diagnostic procedure: if U0073 is current, diagnose U0073 first; clear and recheck (temporary poor communication is common); if persistent, disconnect control modules other than the BIU one at a time (fitting 120 Ω across CAN-Hi/Lo when the ECM or VDC CM is disconnected) until U1201 clears — the last-removed module is faulty.
- Grade: [A]
- Evidence: Subaru FSM LAN-diagnostics U1201 procedure (transcribed via justanswer.com Forester U0073/U1201 guide); 2010–2013 Legacy FSM LAN(diag) DTC tables

## U1202
- Description: not verified — appears in FSM LAN-diagnostics tables in the TCM/BIU columns adjacent to U1201
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Seen in 2010–2013 Legacy FSM LAN(diag) DTC tables (e.g. "U1202 or P1725" in the TCM column). Textual definition was not extracted in this pass.
- Grade: [?]
- Evidence: 2010–2013 Legacy FSM LAN(diag) DTC tables (jdmcarmanuals.com)

## U1221
- Description: CAN-HS ECM No-Receive Data
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: CAN system communication-line failure (ECM to integrated unit); ECM failure
- Diagnostic notes: BIU-detected loss of ECM data on HS-CAN. A 2005 Legacy GT owner report documents a U1221 stranding event traced to a computer/communication issue. In the FSM LAN table it pairs with P1718 and C0047/C0140.
- Grade: [A] description; [B] notes
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com: "U1221 CAN-HS ECM NO-RECEIVE DATA — It is possible that the ECM is faulty"); legacygt.com U1221 field report

## U1222
- Description: CAN-HS TCM No-Receive Data
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: TCM faulty (per FSM probable-cause column)
- Diagnostic notes: BIU-detected loss of TCM data on HS-CAN. Pairs with U0101/C0047/C0140 in the FSM table.
- Grade: [A] description; [B] causes
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com)

## U1223
- Description: CAN-HS VDC/ABS No-Receive Data
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: VDC/ABS control module faulty (per FSM probable-cause column)
- Diagnostic notes: BIU-detected loss of VDC/ABS data on HS-CAN. Pairs with U0122/P1718 in the FSM table.
- Grade: [A] description; [B] causes
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com)

## U1229
- Description: not verified — appears in FSM LAN-diagnostics tables in EPB-related rows ("Hi and Loside circuits near electronic parking brake are open/are shorted to ground")
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Textual definition was not extracted in this pass; context suggests electronic-parking-brake CAN faults.
- Grade: [?]
- Evidence: 2010–2013 Legacy FSM LAN(diag) DTC tables (jdmcarmanuals.com)

## U122A
- Description: not verified — appears in FSM LAN-diagnostics tables in FUEL-related rows
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Textual definition was not extracted in this pass.
- Grade: [?]
- Evidence: 2010–2013 Legacy FSM LAN(diag) DTC tables (jdmcarmanuals.com)

## U122B
- Description: not verified — appears in FSM LAN-diagnostics tables in ABS-related rows
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: not documented
- Diagnostic notes: Textual definition was not extracted in this pass.
- Grade: [?]
- Evidence: 2010–2013 Legacy FSM LAN(diag) DTC tables (jdmcarmanuals.com)

## U1321
- Description: CAN-LS Meter No-Receive Data
- Category: U
- Scope: manufacturer (Subaru)
- Possible causes: combination meter faulty (per FSM probable-cause column)
- Diagnostic notes: Low-speed-CAN fault — the combination meter is on CAN-LS, confirming a second, slower CAN network exists. This is the only LS-CAN DTC extracted in this pass.
- Grade: [A] description; [B] causes
- Evidence: 2011 Impreza FSM LAN(diag) DTC table (jdmcarmanuals.com)

---

### DTC coverage notes (§5)

- P-code coverage is strongest for 2005–2013 EJ-era models (FSM excerpts).
  Later-model P1xxx and direct-injection FA/FB-era extensions were not
  verified [?].
- P1244/P1245/P1301/P1312/P1325/P1480 appear on the troublecodes.net
  Subaru list with **no descriptions found** — omitted rather than
  fabricated [?].
- P1718's description ("AT CAN Communication Circuit") rests on one
  owner report plus FSM table co-occurrence — graded C, flagged.
- U1202/U1229/U122A/U122B are recorded as seen-in-FSM with definitions
  unverified [?].
- Subaru SRS (airbag) manufacturer B-codes were not found in the sources
  consulted [?].
- Generic U0xxx (U0073, U0001/U0002, U0100, U0122, U0140) appear throughout
  the Subaru LAN-diagnostics tables but are SAE-generic and already in the
  database — not duplicated here.
- No seed/key or immobilizer-bypass material was sought or reproduced;
  immobilizer codes (P1570–P1578) are documented at the DTC-description
  level only.

---

## 6. Module-map notes (representative platforms)

### 6.1 Subaru Global Platform — 2017+ Impreza / Crosstrek / Forester (2019+) / Ascent / Outback-Legacy (2020+)

- Single HS-CAN (500 kbps) at DLC 6/14. EyeSight stereo-camera traffic is
  on the HS bus [B — local opendbc clone,
  `opendbc/dbc/generator/subaru/_subaru_global.dbc` + per-model DBCs].
- Message IDs seen on the bus (opendbc, 11-bit):

| CAN ID | opendbc name | Source module (INFERRED) |
|---|---|---|
| 0x002 | Steering | Steering angle sensor |
| 0x040 | Throttle | ECM |
| 0x118 / 0x121 / 0x122 | Steering_Torque, Steering_2, ES_LKAS_ANGLE | EPS / EyeSight LKAS |
| 0x139 / 0x13A | Brake_Pedal, Wheel_Speeds | VDC/ABS |
| 0x13C | Brake_Status | VDC/ABS |
| 0x146 | Cruise_Buttons | Steering switches |
| 0x220 / 0x221 / 0x222 | ES_Brake, ES_Distance, ES_Status | EyeSight camera |
| 0x321 / 0x322 / 0x323 | ES_DashStatus, ES_LKAS_State, ES_Infotainment | EyeSight → cluster/HU |
| 0x240 | Cruise_Status | EyeSight/ECM |
| 0x228 | BSD_RCTA | Blind-spot radar |
| 0x390 | Dashlights | Combination meter |
| 0x3A4 | BodyInfo | BIU |
| 0x2D2 | AC_State | HVAC |
| 0x68D | Dash_State | Combination meter |

- openpilot supports these platforms with standard-CAN harnesses
  (Subaru C/D); steering control is angle-based on 2023+ models [B —
  comma.ai openpilot wiki].

### 6.2 Pre-global CAN era — 2008–2016 (e.g. BM/BR Legacy/Outback 2010–2014, SH Forester, GH/GE Impreza)

- HS-CAN 500 kbps at DLC 6/14; SSM2 K-line on pin 7 remains live for
  SSM diagnostics [B — 2011 Legacy FSM DLC table; C — FreeSSM/KKL on
  2009 Outback].
- Message IDs seen on the bus (opendbc `_subaru_preglobal_2015.dbc`)
  [B — local opendbc clone]:

| CAN ID | opendbc name | Source module (INFERRED) |
|---|---|---|
| 0x002 | Steering | Steering angle sensor |
| 0x070 / 0x075 / 0x080 | (yaw/G sensor frames) | Yaw/G sensor → VDC |
| 0x140 / 0x141 | Transmission, CVT | TCM |
| 0x141 | Engine | ECM (rpm, accel, torque) |
| 0x201 | ES_Distance / ES_Status family | EyeSight |
| 0x240 | CruiseControl | ECM/EyeSight |
| 0x282 | Dashlights | Combination meter |
| 0x370 | BodyInfo | BIU |
| 0x360 | Engine_Temp | ECM |
| 0x372 | Fuel | BIU/cluster |
| 0x6D1 | Dash_State | Combination meter |

- The 2005 Legacy (transition year) has **two** CAN buses with the BIU in
  the middle: BIU↔combination meter and BIU↔ECM/TCM/VDC/ABS/steering-angle
  sensor [C — legacygt.com with wiring diagrams].
- LAN-diagnostics modules on these cars: ECM, TCM, VDC/ABS CM, BIU,
  combination meter, EPB, A/C, steering angle sensor [A — FSM LAN(diag)
  DTC tables].

### 6.3 EJ-era / SSM2 K-line era — 1999–2007 (GD Impreza WRX/STI, SG Forester, BP/BL Legacy)

- No CAN at the DLC. Diagnostics = SSM2 on pin 7 (4800 bps 8N1);
  destinations 0x10 (ECU) / 0x18 (TCU) [B — RomRaider SsmProtocol doc].
- Generic OBD-II also answers on the K-line for emissions PIDs [B —
  FreeSSM docs describe SSM2 as KWP2000-derived on ISO-9141/14230
  physical layer].
- The 2005 Legacy DLC: pin 7 = ECU data line, pin 11 also to the ECU;
  pins 12/13 (Subaru numbering) = grounds [C — ultimatesubaru.org;
  note the mirrored-numbering caution in §2.1].
- Tuning/logging ecosystem (RomRaider, ECUFlash, Learning View) is built
  on SSM2 block reads (0xA0) against ECU RAM [B].

### 6.4 BRZ / Toyota 86 (2012+)

- The BRZ rides on a Toyota-led platform: AiM's protocol table maps the
  BRZ to "TOYOTA - GT86/SCION_FRS" rather than a Subaru protocol [C].
- Expect Toyota-style CAN diagnostics (500k HS CAN, standard 0x7E0/0x7E8
  addressing per work/toyota.md) with a Subaru FA20 engine underneath;
  SSM2 K-line behavior on the BRZ was not verified [?].

---

## 7. M2 hardware → Subaru bus mapping

| Subaru bus | DLC pins | M2 hardware path |
|---|---|---|
| HS CAN (500k) | 6 / 14 | CAN0 or CAN1 (TJA1051, due_can). Primary diagnostic + logging bus; all platforms 2008+ |
| SSM2 K-line (4800 bps 8N1) | 7 | K-line transceiver (TJA1027). SSM2 packet layer (0x80 hdr, checksum) in firmware; covers 1999–~2015 ECM/TCU incl. CAN-era cars |
| CAN-LS (rate undocumented) | not on DLC (interior) | Second CAN controller **if tapped behind the BIU** (combination-meter branch) |
| LIN sub-buses | not on DLC | LIN1/LIN2 (TJA1027) if tapped at the module |
| CAN FD (Solterra/Toyota-platform only) | — | **No M2 hardware support** — TJA1051 is CAN 2.0 only; out of scope |

- Practical note: on 2008+ cars the M2 gets two independent diagnostic
  paths from the DLC alone — CAN 6/14 for OBD-II/UDS-style traffic and
  pin-7 K-line for SSM2 — with no interior tapping [B/C].
- SSM2 at 4800 bps 8N1 is well within the TJA1027 K-line transceiver's
  capability; the work is all in the packet layer (init 0xBF, address
  reads 0xA8, checksum) [B].

---

## 8. Notable quirks

1. **Pin 7 is SSM, not generic K-line OBD.** Subaru labels DLC pin 7
   "Subaru Select Monitor signal" in the factory manual. Generic scan
   tools use CAN; SSM2 lives on pin 7 in parallel — even on CAN-era cars
   [A/B].
2. **SSM is memory-address-oriented, not service-oriented.** There are no
   "modes" or "PIDs" in SSM2 — you read 3-byte RAM addresses (0xA8) after
   a 0xBF init that returns a capability bitmap. Porting UDS thinking
   (0x22 DIDs) to Subaru will mislead; §4 is addresses, not DIDs [B].
3. **The DLC pin numbering is mirrored in Subaru's own diagrams.**
   Subaru draws the J1962 with the narrow edge up, reversing the numbers
   vs. the standard wide-edge-up layout. Verify with a meter before
   probing [C].
4. **U-code family semantics:** U12xx = HS-CAN node-receive faults
   (U1221 = ECM, U1222 = TCM, U1223 = VDC/ABS, from the BIU's point of
   view); U1201 = BIU's CAN-health counter flag; U13xx = LS-CAN faults
   (U1321 = meter). U0073 remains the generic bus-off code [A].
5. **P1718 is the code that sends you to the LAN section.** A Subaru
   P1718 (AT CAN communication circuit) without the accompanying U12xx
   LAN codes is only half the story — the FSM diagnoses them as a group
   [B/C].
6. **The BIU is half the immobilizer.** P1570–P1578 span ECM, BIU,
   combination meter and key; a used-BIU swap needs dealer key/ECU
   recoding to sync [B/C]. Nothing here is a bypass procedure.
7. **EyeSight lives on the HS bus** (0x1xx/0x2xx/0x3xx IDs in opendbc)
   and its calibration/diagnostics go through SSM3/SSM4 — not through
   generic OBD [B/C].
8. **Community SSM tooling stops ~2015.** FreeSSM (≤2010) and BtSsm
   (≤~2019 WRX in CAN mode) cover the SSM era; newer models are E-OBD/UDS
   per community reports — which is also where the public UDS DID
   documentation gap bites hardest [C].
9. **120 Ω field termination trick is in the FSM.** The U1201 procedure's
   instruction to fit 120 Ω across CAN-Hi/Lo when the ECM or VDC module
   is unplugged both confirms the termination scheme and gives a
   bench-test recipe [A].

---

## Sources consulted

- Subaru 2011 Legacy USDM FSM, ENGINE (DIAGNOSTICS) §7 "Data Link
  Connector" (via jdmcarmanuals.com) — DLC pinout: 6/14 CAN, 7 SSM
  signal [A]
- Subaru 2007 Legacy / 2011 Legacy / 2010–2013 Legacy / 2010–2011
  Impreza / 2007–2013 Tribeca USDM FSM excerpts (via jdmcarmanuals.com)
  — engine DTC lists (P1152/P1153/P1400/P1410/P1420/P1443/P1491/
  P1518/P1560/P1570–P1578), immobilizer DTC tables, VDC(diag) DTC lists
  and procedures (C0041–C0054, C0047 detecting condition), LAN(diag)
  DTC tables (U1201/U1202/U1221–U122B/U1321/B1100/B1500) [A]
- RomRaider SsmProtocol documentation (via github.com/DaStivi/subduino
  mirror of romraider.com) — SSM2 serial settings, packet format,
  commands 0xA0/0xA8/0xB0/0xB8/0xBF, capability bitmap, parameter
  addresses + conversions [B]
- Local opendbc clone (work/opendbc): `dbc/generator/subaru/`
  `_subaru_global.dbc` (27 msgs), `_subaru_preglobal_2015.dbc` (26
  msgs), `subaru_global_2017.dbc`, `subaru_global_2020_hybrid.dbc`,
  `subaru_forester_2017.dbc`, `subaru_outback_2015.dbc`,
  `subaru_outback_2019.dbc` — HS-bus message IDs and module
  attribution [B]
- comma.ai openpilot wiki, Subaru page — platform support, harness
  generations, Solterra CAN FD note, angle-based steering 2023+ [B]
- Subaru Diesel Crew "CAN Messages" (web.archive.org) — MY2009/2010
  Impreza HS-bus 500k capture: 15 CAN IDs with sources and 0x410/0x2
  decodes [B/C]
- FreeSSM/obdii365.com docs — SSM2 = modified KWP2000 on ISO-9141/14230
  layer, pin-7 availability note, FTDI-only cable requirement,
  1999–2009 (+2010 partial) coverage, no reprogramming/key
  programming [B]
- obdii365.com SSM4-with-J2534 blog — DST-i registry (CAN/ISO14230/
  ISO9141/ISO15765 channels), SSM4 = 2016+ [C]
- legacygt.com threads — 2005 Legacy dual-CAN-bus description [C];
  BtSsm tester post (K-line + CAN mode, 2015–2019 WRX; newer models
  moved to E-OBDII) [C]; U1221 stranding field report [C]
- thesubaruforums.com — 2006 Legacy GT P1718 = CAN communication
  circuit [C]
- subaruoutback.org — P0600/P0700 = HS-CAN ECM/TCM/ABS/VDC fault [C]
- ultimatesubaru.org — 2005 Legacy DLC pin notes [C]
- subaru-svx.net (b3lha) — mirrored DLC numbering in Subaru diagrams
  [C]; SSM1 cable notes [C]
- vxdiagshop.com / obdii365.com SSM3-vs-FreeSSM blogs — SSM
  generations, tool capabilities, key-programming dealer-code flow [C]
- Ruth Consulting EDR presentation (2019) — SSM3/SSM4 EDR reads, .SSM
  files, CSV limitation on SSM4 [C]
- OBDCodex Subaru manufacturer-specific DTC list (slideshare.net);
  "Subaru Specific Error Codes Guide" (scribd.com);
  troublecodes.net/subaru — P1xxx description cross-checks [B/C]
- justanswer.com — U1201 CAN-HS counter-abnormal procedure
  transcription [B]
- AiM OBDII-protocols-by-model table (scribd.com) — Impreza 1999–2007
  SSM / 2008 SSM-then-CAN; BRZ → Toyota GT86 protocol [C]
- accio.com vendor page — uncorroborated 2020+ Outback CAN FD claim
  [C]

## Open items

- SSM-over-CAN (SSM3/SSM4) CAN IDs and application-layer frame format —
  not publicly documented [?]
- Subaru-specific UDS 0x22 DID catalog — none found [?]
- TCU (0x18) SSM parameter addresses [?]
- VVT/OCV/A-F-current and switch/relay SSM addresses beyond the §4
  subset [?]
- CAN-LS bitrate, topology, and DLC presence [?]
- BIU gateway function (HS↔LS protocol conversion) — INFERRED only [?]
- U1202/U1229/U122A/U122B textual definitions [?]
- P1244/P1245/P1301/P1312/P1325/P1480 descriptions [?]
- Subaru SRS (airbag) manufacturer B-codes [?]
- EyeSight diagnostic CAN IDs / calibration procedure [?]
- BRZ/86 SSM2 K-line behavior [?]
- FA/FB direct-injection-era P1xxx extensions [?]
