# Honda / Acura manufacturer-specific UDS Data Identifiers (service 0x22)

Scope: Honda/Acura-specific DIDs read via UDS ReadDataByIdentifier (0x22).
ISO-standard 0xF180–0xF19E DIDs are intentionally NOT listed here (covered separately).
Target: M2 OEM vehicle database v1.3.

## Transport notes (applies to all entries below)

- Honda 29-bit normal fixed addressing: request `0x18DA<target>F1` → response
  `0x18DAF1<target>` (tester address `0xF1`). Observed target bytes:
  `01`, `0E`, `10` (PCM), `11`, `1D` (TCM), `1E`, `26` (TPMS), `28`, `2A`,
  `60` (meter/HVAC), `EF`. Cross-validated on Civic + TLX by scainner research;
  2009 Civic uses TX `0x18DB33F1` / RX `0x18DAF110` (hansonFish/obdii README).
- CONFLICT (unresolved, reported not resolved): target byte `0x01` is documented
  as "body" by scainner RESEARCH.md, but Honda Motor Europe's e:PHEV bulletin
  shows the BAT (battery) ECU responding on `0x18DAF101`, and papataku's RP8
  STEP WGN e:HEV analyzer records SOC-bearing DIDs (`0x2012`, `0x2028/0x202A/0x202C`
  cluster) answering at `0x18DAF101`. Target-byte → ECU mapping varies by platform.
- OBDb signalsets encode bit offsets (`bix`); the absolute base point (whether the
  `62 DID` header is included in the offset) could NOT be confirmed — scainner
  RESEARCH.md deliberately omitted Honda bit offsets for this reason. Field
  widths/scales below are as documented; absolute byte positions are "not documented".

## Battery ECU (e:HEV)

### DA01 on Civic e:HEV (request 0x18DA01F1 → response 0x18DAF101); BAT on e:PHEV/RP8 (request 0x18DBEFF1 → response 0x18DAF101)

## 0x2028
- Name: HighVoltageBatteryCellVoltages
- Description: Individual HV cell voltages A1..A84. Each field 16-bit unsigned, value/5 = millivolts (e.g. raw 18489 → 3697.8 mV). Recorded fixture on Civic hybrid decodes plausible Li-ion cell voltages (~3.69–3.70 V).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [B] DID existence/purpose/encodings (two independent community projects + recorded multi-frame fixture); [C] absolute byte positions (inference — flagged: OBDb bix base point unconfirmed)
- Evidence: OBDb Honda-Civic signalset (DA01, filter from 2023) + recorded test fixture (tests/test_cases/2023/commands/DA01.01.222028) with decoded cell voltages; RP8 STEP WGN e:HEV Session 15 scan also found DID 0x2028 positive on ECU 01 (papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md)

## 0x202A
- Name: HighVoltageBatteryStatusBlock (SOCE / StateOfCharge)
- Description: HV battery status block: SOC (%), pack total current (A, signed), pack voltage (V), cell max/min SOC (%), cabin/outside ambient temps (°C), pack capacity (Ah). OEM method: send `03 22 20 2A` to 0x18DBEFF1; receive multi-frame from 0x18DAF101; SOCE is "the last figure before 55 55 55 55 55" end marker; SOCE% = raw×100/255 (OEM example: FC → 98.82%).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in both Honda EU bulletin example and OBDb recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [A] name/purpose/SOCE formula (Honda Motor Europe OEM service bulletin); [B] community encodings/size (OBDb Civic + recorded fixture decoding SOC 64%, 268 V, 3.66 A); [C] absolute byte positions (inference — flagged: OEM gives relative position only; OBDb bix base unconfirmed)
- Evidence: Honda Motor Europe techinfo bulletin ePHEVBMS_EN 002 (Aug 2024, e:PHEV 2024- BAT ECU SOCE method); OBDb Honda-Civic DA01 (filter from 2023) with test fixture (tests/test_cases/2023/commands/DA01.01.22202A) decoding SOC/current/voltage; RP8 Session 15 scan positive for 0x202A on ECU 01

## 0x202C
- Name: HighVoltageBatteryModuleTemperatures
- Description: HV battery module temperatures (1A, 3A) plus engine coolant temperature sensors 1–4. Each 16-bit signed, /10 = °C (offset −40 range per OBDb: min −40).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [B] DID existence/purpose/encodings (OBDb Civic + recorded fixture; RP8 Session 15 scan positive on ECU 01); [C] absolute byte positions (inference — flagged)
- Evidence: OBDb Honda-Civic signalset DA01 (filter from 2023) + test fixture (tests/test_cases/2023/commands/DA01.01.22202C); papataku RP8 Session 15 positive-DID list includes 0x202C

## Engine / PCM

### DA10 / DA11 / DA0E (request 0x18DA<target>F1 → response 0x18DAF1<target>)

## 0x2240
- Name: DistanceTraveledSinceLastCharge
- Description: Distance traveled since last charge, 32-bit unsigned, kilometers. Listed for 2012–2014 Civic (DA0E).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source (OBDb Honda-Civic only; no CR-V entry, no recorded fixture found)
- Evidence: OBDb Honda-Civic signalset (DA0E, filter 2012–2014)

## 0x2610
- Name: GeneratorFieldDutyAndACClutch
- Description: Generator field duty, 8-bit: raw×100/255 = percent; plus A/C clutch 1-bit on/off.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two independent model repos agree (OBDb Honda-Civic DA10 + Honda-CR-V DA10, identical fields/scales)
- Evidence: OBDb Honda-Civic and Honda-CR-V signalsets (DA10)

## 0x2611
- Name: FuelAirCommandedEquivalenceRatio
- Description: Fuel/air commanded equivalence ratio (lambda): 16-bit raw×29.4/65535 = ratio (max 29.4). DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V); [C] byte position (inference — flagged)
- Evidence: OBDb Honda-Civic (DA10, filter from 2015) and Honda-CR-V (DA10, DA11) signalsets

## 0x2612
- Name: VariableValveControl
- Description: Variable valve (VTEC) control, 8-bit scalar (DA10). Same DID on DA0E carries current-gear variants (8-bit scalars).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree on DA10 VTEC usage; [C] DA0E gear-variant usage (Civic only, CR-V marks dbg)
- Evidence: OBDb Honda-Civic + Honda-CR-V (DA10); DA0E gear entries from Honda-Civic (CR-V flags them dbg)

## 0x2613
- Name: ACRefrigerantPressure
- Description: A/C pressure, 16-bit unsigned, kilopascals (max 4000). DA0E.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] both model repos list identical DID/scale; [C] noted: CR-V entry is flagged dbg
- Evidence: OBDb Honda-Civic + Honda-CR-V (DA0E)

## 0x2615
- Name: ActiveCylinders
- Description: Active cylinders, 8-bit (max 6). DA10, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

## 0x2660
- Name: OdometerAndEngineRuntime
- Description: Odometer 24-bit unsigned kilometers + time since engine start 16-bit seconds. DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic filter from 2015 + CR-V, identical fields/scales)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

## 0x2661
- Name: FuelAirCommandedEquivalenceRatioAlt
- Description: Fuel/air commanded equivalence ratio, 16-bit: raw/2229.08163265 = ratio (max 29.4). DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

## 0x2662
- Name: KnockControlAndVTCTiming
- Description: Knock control 8-bit (raw×2/255); variable timing control duty 8-bit (raw×100/255 = %); DA11 variant adds catalyst temperature 16-bit (/10 − 40 = °C).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic DA10/DA11 + CR-V DA10/DA11)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets

## 0x2663
- Name: MisfireCountsPerCylinder
- Description: Per-cylinder misfire counts, 16-bit unsigned each (cylinders 1–4 on DA10; DA11 variants carry up to 6 cylinders in multiple layouts).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree on DA10 layout (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10; DA11 variants differ by generation)

## 0x2666
- Name: EngineOilTemperature
- Description: Engine oil temperature, 8-bit: raw − 40 = °C (range −40..215). DA10/DA11.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets

## 0x266C
- Name: MisfireCountVariant1
- Description: Per-cylinder misfire counts, 8-bit unsigned each (6 cylinders). DA11.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] conflict: flagged dbg in Honda-Civic but non-dbg in Honda-CR-V; treat layout as unconfirmed
- Evidence: OBDb Honda-Civic (DA11, dbg, filter to 2011) + Honda-CR-V (DA11)

## Transmission / TCM

### DA1D / DA1E (request 0x18DA1DF1 → response 0x18DAF11D for DA1D)

## 0x2201
- Name: AutomaticTransmissionFluidTemperature
- Description: ATF temperature, first DID data byte: °C = byte − 40 (range −40..215). Torque Pro formula from community: `AA*(9/5)-40` (°F) with OBD header `18DA1DF1`; ScanGauge II XGauge: TXD `1DF1222201`, RXF `032400000000`, RXD `2808`, MTH `00090005FFD8` — same byte, same scale.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] multi-source community agreement: odyclub ScanGauge code + Torque Pro config confirmed working on a 2015 Odyssey EX-L + OBDb Civic (DA1D, filter to 2014) + OBDb CR-V (DA1D) — all describe byte 0, −40 offset
- Evidence: odyclub.com "Transmission Temperature with Torque app and ELM327" (posts by Charlie, TomB985, 0dyfamily; Torque settings "got this to work on my 2015 EX-L"); OBDb Honda-Civic + Honda-CR-V (DA1D 0x2201, bix 208 len 8 add −40 °C)

## 0x2203
- Name: OilPressure
- Description: Oil pressure, 8-bit unsigned, kilopascals (max 255). DA1D.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-CR-V signalset (DA1D, dbg)

## 0x2221
- Name: CurrentGear
- Description: Current gear, 8-bit scalar. DA1D.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic filter to 2014 + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1D)

## 0x3083
- Name: TransmissionFluidTemperatureAlt
- Description: Transmission fluid temperature on DA1E, 8-bit: raw − 40 = °C (range −40..200).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1E, dbg)

## 0x3086
- Name: TransmissionGearEnumerated
- Description: Transmission gear on DA1E, 8-bit with enumerated map (values include 0–9, 14, 15; e.g. Park/Drive positions).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg, enumeration map not verified against a vehicle
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1E, dbg)

## Brake system

### DA28 / DA2A

## 0x4004
- Name: BrakeSwitch
- Description: Brake switch, 1-bit on/off. DA28, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA28)

## 0x4005
- Name: BrakePressure
- Description: Brake pressure, 16-bit: raw − 25 = bars (max 120). DA28, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V); [C] offset semantics (add −25) — single-source convention
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA28)

## 0x4201
- Name: BrakePedalAndCylinderStrokes
- Description: Brake pedal stroke 16-bit (/10 = mm, max 50); brake fluid pressure 16-bit (/100, unit unknown); master cylinder stroke 16-bit signed (/10 = mm); slave cylinder stroke 16-bit (/10 = mm). DA2A, filter from 2023.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] DID existence and signal list in both repos; [C] encodings (single-source convention, fluid-pressure unit unknown)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA2A)

## TPMS

### DA26

## 0x6001
- Name: TirePressuresAndTemperatures
- Description: Four tire pressures, 16-bit each, kilopascals; four tire temperatures, 8-bit signed each, °C. DA26.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-CR-V signalset (DA26, dbg)

## Instrument cluster / meter

### DA60

## 0x7022
- Name: OdometerMiles
- Description: Odometer, 24-bit unsigned, miles (max 200000). DA60, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

## 0x7028
- Name: OutsideAirTemperature
- Description: Outside air temperature, 12-bit signed: raw = °F (range −40..2047; 141 = null/invalid). DA60, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

## 0x7029
- Name: FuelLevel
- Description: Fuel level, 16-bit: raw/100 = liters (max 655). DA60, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

## 0x7060
- Name: MaintenanceMinderItems
- Description: Maintenance minder distances/items (oil & filter, spark plugs & valves, general inspection, tire rotation, cabin filter, transmission fluid, engine coolant, brake fluid, air cleaner), 16-bit each, unit unknown. DA60, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] two repos list it but units are unknown and Civic/CR-V disagree on dbg status
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

## Honda e:WN7 electric motorcycle (2026, EU)

Reverse-engineered via MeatPi WiCAN on the diagnostic connector. Field positions
verified against a passive bus capture of Honda's own official MCS diagnostic
tool plus its 18-page all-systems report. 29-bit: request `0x18DA<ECU>F1` →
response `0x18DAF1<ECU>`. Honda's tool uses plain service 0x22 in the DEFAULT
session (`10 01`) with periodic TesterPresent (`3E`) and NO `27` SecurityAccess
— none of the data below is access-locked (verified capture).

## 0xA870
- Name: BatteryStatusBlock
- Description: 56-byte battery status block (BMU, target 0xD4). Verified positions: in-fact SOC u16×0.01 % (payload p41:42); displayed SOC u16×0.01 % (p43:44); SOC control u16×0.01 % (p45:46); remaining-energy field u16 (p47:48); pack voltage u16×0.1 V (p12:13, ~392 V nominal); pack current s16×0.1 A (p14:15, negative = charging); cell temp max u8−40 °C (p37); cell temp min u8−40 °C (p38); SOH u8 % (p49, 100 on new pack); SOCP/SOCE u8 (p50/p51).
- Make: honda
- Size: 56 bytes (verified)
- Session: default session (verified — Honda MCS tool capture used 10 01 + periodic 3E)
- Security: none required (verified — no 27 SecurityAccess in captured tool session)
- Grade: [B] verified capture: positions matched against Honda's official MCS diagnostic tool passive capture and its 18-page all-systems report; single vehicle (2026 WN7 EU)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md ("Verified positions (matched against the official diagnostic report)")

## 0xF012
- Name: Odometer
- Description: Odometer, 32-bit: raw×0.1 = km. Response `62 F0 12 <u32>`; matches the TFT display exactly. (Meter, target 0xDE.)
- Make: honda
- Size: 4 bytes (verified — response `62 F0 12 <u32>`)
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (matches display exactly; official-report matched)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xCFA1
- Name: ChargePortTemperature
- Description: Charge-port temperature, u8: raw − 40 = °C (payload p18). (Meter, target 0xDE.)
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (matched against official diagnostic report)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xCFA2
- Name: DisplayAggregateBlock
- Description: Cluster's display block (meter, target 0xDE): displayed SOC u8 % at p30 (integer, exactly the TFT number); ambient temp u8 °C at p18; cell voltage max u16/5 = mV at p31:32; cell voltage min u16/5 = mV at p33:34; pack voltage copy u16 at p24:25; plug-state mirror u8 at p16 (4→0 when cable in).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (TFT-calibrated over weeks; report-matched)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xDB00
- Name: ChargeConnectBlock
- Description: 56-byte charge-connect block (PCU/DCDC, target 0xCB). Decoded via plug-in before/after snapshots: cable flag u8 at p9 (1 = no cable, 3 = cable plugged in, stays 3 while charging); charge-active flag u8 at p8 (1 = not charging, 2 = charging — verified during a real AC session); proximity-pilot resistance u16 at p27:28 (0xFFFF = no plug, ~220 with cable); control-pilot values at p19:20/p25:26 go 0→non-zero with cable; DCDC output u8 at p31 (14.7 V).
- Make: honda
- Size: 56 bytes (verified)
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (before/after plug snapshots + real AC charge session)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xCF03
- Name: OnboardChargerTemperature
- Description: OBC temperature at payload byte 8 (u8: raw − 40 = °C). Confirmed against the diagnostic report; early "charging flag" hypothesis definitively disproven. (OBC, target 0xD0.)
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (confirmed against official diagnostic report)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xDA10
- Name: BatterySerialNumber
- Description: Battery serial number (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table)

## 0xDA5C
- Name: EventCounterBlock1
- Description: Event/error counter block (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xDA5F
- Name: EventCounterBlock2
- Description: Event/error counter block (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xA820
- Name: EventCounterBlockRangeStart
- Description: First of the A820–A82A event/error counter blocks (BMU, target 0xD4). Present, not decoded. Range listed as a family; individual block semantics unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xCF01
- Name: ChargeDCDCBlock1
- Description: First of the CF01–CF04 charge/DCDC blocks (OBC, target 0xD0). Present, not decoded (only CF03's temperature byte is verified).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xD300
- Name: CellUnitSOHBlockRangeStart
- Description: First of the D300–D30A per-cell-unit SOH blocks (meter, target 0xDE). Pattern `00 00 64 xx xx` = SOH 100% plus a capacity value (695/631 observed on a new pack). Range listed as a family.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; pattern observed, not fully decoded
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

## 0xE700
- Name: PCUUnknownBlock
- Description: PCU (target 0xCB) DID, present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table)

## 0xF802
- Name: VehicleIdentificationNumberASCII
- Description: VIN in ASCII (meter, target 0xDE). PII — handle with care in logs.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; noted in ECU table, not byte-decoded
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table; "F802 = VIN (ASCII — PII, be careful with logs)")

## 0x7122
- Name: BodyABSUnknown1
- Description: Body/ABS (target 0x60) DID, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table: "7122, 7128, 712A (not decoded)")

## Honda STEP WGN e:HEV RP8 (2023) — discovery results, semantics unknown

From papataku/honda_ehev_analyzer (real vehicle, KONNWEI KW905 ELM327-compatible
adapter, 29-bit ISO 15765-4 500 kbit/s). Automated discovery is read-only 0x22,
no 0x10 session changes, no 0x27 — so all reads below work in the default session.
The project explicitly warns: "Do not guess Honda-specific semantics from an ID,
byte offset, correlation, or ECU source address" and "A high correlation is
candidate evidence, not a signal definition."

## 0x2012
- Name: UnknownSOCMirrorCandidate
- Description: 36-byte payload from responder 0x18DAF101 (ECU source 01). Data byte 5 tracked standard OBD-II PID 0x5B (hybrid battery SOC) with Pearson ~0.9985 / MAE ~0.39 pct across sessions — a strong SOC-mirror candidate, but NOT an official Honda semantic definition. Bytes 24–27 also SOC-correlated. No convincing traction-motor RPM behavior.
- Make: honda
- Size: 36 bytes (verified — Session 12: "383 samples, reconstructed data length 36 bytes")
- Session: default session (verified — discovery uses plain 0x22, no 0x10)
- Security: none required (verified — no 0x27 in discovery)
- Grade: [B] DID existence/size (multiple sessions reproduced, incl. Session 16); [C] SOC-mirror interpretation (inference — flagged: project states it is "still not an official Honda semantic definition")
- Evidence: papataku/honda_ehev_analyzer docs/SESSION12_ANALYSIS.md, docs/SESSION16_ANALYSIS.md, docs/PROJECT_CONTEXT.md (DID 2012 section; request `22 2012`, positive prefix `62 20 12`, responder 18DAF101)

## 0x2001
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 0x2000-range scan. Semantics and size unknown (some responses in the scan were complete, some long/partial).
- Make: honda
- Size: not documented
- Session: default session (verified — discovery uses plain 0x22, no 0x10)
- Security: none required (verified — no 0x27 in discovery)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md (Session 15 positive-DID list)

## 0x2010
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x2013
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

## 0x2018
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

## 0x2019
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x2020
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

## 0x2025
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x2059
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x2068
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x206A
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x206B
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x206C
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

## 0x2680
- Name: UnknownRP8ECU0EBlock
- Description: Complete positive 0x22 response on RP8 ECU source 0E (0x18DAF10E), Session 16. Semantics and size unknown. Part of a 0x2600-range cluster (2680, 2681, 2685, 2686, 2691, 2692, 2693, 269F complete; 26A0/26A1 partial).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md, docs/PROJECT_CONTEXT.md

## 0xC000
- Name: UnknownRP8ECUEFBlock
- Description: Complete positive 0x22 response, 56-byte payload, on RP8 ECU source EF (0x18DAF1EF), Session 16. Semantics unknown.
- Make: honda
- Size: 56 bytes (verified — Session 16: "C000 — 56-byte payload")
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence/size only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md

## 0xC020
- Name: UnknownRP8ECUEFBlock
- Description: Complete positive 0x22 response, 4-byte payload, on RP8 ECU source EF (0x18DAF1EF), Session 16. Semantics unknown.
- Make: honda
- Size: 4 bytes (verified — Session 16: "C020 — 4-byte payload")
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence/size only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md

## Coverage notes

DID ranges / areas that could NOT be verified — systematic gaps:

1. Acura: no Acura-specific DIDs found anywhere. OBDb has no Acura repos;
   scainner RESEARCH.md cross-validates the 29-bit target scheme on the Acura
   TLX (DA10/DA1D/DA60 targets) but lists no TLX DIDs. The 26 Honda entries
   above are expected to carry over to Acura where the ECU is shared, but this
   is inference — do not assert it per-DID.
2. SRS (airbag), VSA/ABS, EPS, gateway, forward camera/radar, combination meter
   (passenger cars): no 0x22 DID reads documented in any source checked.
   opendbc fingerprints show these ECUs answer 0xF18x/0xF19x identification
   reads (e.g. SRS at 0x18DAF153 on Civic Type R FK8) but no Honda-specific
   data DIDs are published.
3. Honda-Clarity and Honda-M-NV OBDb repos exist but are empty stubs (21 bytes)
   — no DIDs. The Honda EU e:PHEV bulletin covers the battery ECU of the
   e:PHEV only.
4. Honda e:HEV motor/generator RPM, torque, and current: no verified DID found.
   The RP8 analyzer explicitly concluded Session 16 "is not sufficient to
   identify traction motor/generator RPM" and that DID 0x2012 "has not shown
   convincing traction-motor RPM behavior."
5. Pre-2008 Honda hybrids (IMA, 11-bit CAN): those use KWP2000-style service
   0x21 local identifiers, out of scope for this 0x22 catalog.
6. Absolute byte positions within multi-hundred-byte responses: not documented
   for any OBDb-sourced DID (bix base point unconfirmed — see transport notes).
   Treat all OBDb field offsets as relative/encoding hints, not wire positions.
7. Session/security for passenger-car DIDs (all non-WN7 entries): not
   documented. Community reads were done in the default session without
   SecurityAccess, but no source states this as a requirement the way the WN7
   project does for its own platform.
8. Unresolved conflict reported above: target byte 0x01 = "body" (scainner)
   vs battery ECU (Honda EU bulletin, RP8 analyzer). Do not hard-code
   0x01 = battery or 0x01 = body without a per-platform check.
9. The 0x2028/0x202A/0x202C battery cluster appears on the Civic e:HEV at
   target DA01 and on the RP8/e:PHEV at target 0x01 — same DIDs, different
   target bytes by platform. Request addressing must be platform-qualified.

## Sources (live, fetched 2026-10-06)

- OBDb org, Honda-Civic + Honda-CR-V signalsets v3
  (https://github.com/OBDb/Honda-Civic, https://github.com/OBDb/Honda-CR-V),
  including recorded test fixtures under tests/test_cases/ (real CAN captures
  with decoded values).
- Honda Motor Europe techinfo bulletin ePHEVBMS_EN 002 (Aug 2024), "Method of
  reading SOCE" for e:PHEV 2024- BAT ECU
  (https://www.techinfo.honda-eu.com/sites/default/files/2024-08/phevbms_en_002.pdf).
- cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Honda e:WN7 EV
  motorcycle; positions verified against passive capture of Honda's official
  MCS tool + report).
- papataku/honda_ehev_analyzer (Honda STEP WGN e:HEV RP8 2023; docs/PROJECT_CONTEXT.md,
  docs/SESSION12_ANALYSIS.md, docs/SESSION16_ANALYSIS.md, AGENTS.md).
- odyclub.com thread "Transmission Temperature with Torque app and ELM327"
  (ScanGauge XGauge + Torque Pro 0x2201 settings, verified on 2015 Odyssey EX-L).
- cxalem/scainner packages/uds-map/RESEARCH.md (Honda 29-bit target-byte scheme
  cross-validation Civic/TLX; OBDb provenance; confirmed gaps list).
- hansonFish/obdii README.md (2009 Civic 29-bit IDs 0x18DB33F1/0x18DAF110 —
  transport only, no DIDs).
- apatt124/ai-car-tuner: checked; contains no Honda UDS 0x22 DID content
  (mock/demo project) — nothing usable.
