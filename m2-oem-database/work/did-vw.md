# VW Group manufacturer-specific UDS DIDs (service 0x22)

Compiled 2026-10-06. ISO-standard identification DIDs (0xF180-0xF19E) are covered separately and intentionally excluded here.
The 0xF4xx entries are OBD mode-01 PID mirrors exposed over 0x22 (confirmed on VAG); they are included because they are
the manufacturer-specific transport of those values, but they are redundant with mode-01 reads where the module answers EOBD.

Module CAN pairs below come from the ODIS-extracted module table (ConnorHowell/vag-uds-ids, single unlicensed source,
cross-checked against OVMS vehicle_vweup production code where it covers the module) — treat pairs as Grade B/C per entry, not A.

| VCDS module | ECU | Req | Resp |
|---|---|---|---|
| 01 | Engine / motor electronics (J623) | 0x7E0 | 0x7E8 |
| 02 | Transmission / DSG (J217) | 0x7E1 | 0x7E9 |
| 03 | Brake electronics / ABS-ESP (J104) | 0x713 | 0x77D |
| 08 | Auto HVAC / Climatronic (J255) | 0x746 | 0x7B0 |
| 09 | Central electronics (BCM, J519) | 0x70E | 0x778 |
| 15 | Airbag (J234) | 0x715 | 0x77F |
| 17 | Instruments / MFD cluster (J285) | 0x714 | 0x77E |
| 19 | CAN gateway (J533) | 0x710 | 0x77A |
| 23 | Brake boost | 0x73B | 0x743 |
| 25 | Immobilizer (J362) | 0x711 | 0x77B |
| 44 | Steering assist / EPS | 0x712 | 0x71A |
| 51 | Electric drive | 0x7E6 | 0x7EE |
| 5F | Information electronics / infotainment | 0x773 | 0x7DD |
| 65 | TPMS | 0x70B | 0x775 |
| 77 | Telephone / telematics | 0x767 | 0x7D1 |
| 8C | Hybrid/EV battery management | 0x7E5 | 0x7ED |
| BD | HV charge management | 0x765 | 0x7CF |
| C6 | On-board charger | 0x744 | 0x7AE |
| — | DC-DC converter (MEB, target-addressed) | FC00/ta=B9 | FE00B9 |
| — | MEB BMS (target-addressed, OBDb convention) | FC00/ta=7B | FE007B |
| — | MEB electric drive (target-addressed, OBDb convention) | FC00/ta=76 | FE0076 |

Note: 'FC00' with ta= (target address) is the OBDb signalset convention for VW's extended-addressed diagnostics
(same pattern as BMW's 6F1/target-byte scheme): the request is framed through FC00 with a target-address byte.
These are not plain 11-bit CAN IDs; the DID, names and decodes are verified, the raw framing needs field verification.

### Instrument cluster / MFD — 0x714/0x77E (VCDS 17)

## 0x2203
- Name: Odometer
- Description: Odometer, instrument cluster / MFD view. Shared MQB/MEB convention (VW/Audi/Skoda/SEAT).
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids) + OVMS vweup_obd.h #define (VWUP_MFD_ODOMETER) — multi-source community agreement

## 0x2260
- Name: ServiceIntervalRemainingDistance
- Description: Service interval remaining distance. OVMS decodes as plain uint16 in km.
- Make: vw
- Size: 16 bits, uint16 = km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode

## 0x2261
- Name: ServiceIntervalRemainingTime
- Description: Service interval remaining time. OVMS: uint16 value is remaining DAYS (multiplied by 86400 and added to clock).
- Make: vw
- Size: 16 bits, uint16 = days
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode

## 0x22E0
- Name: EstimatedRangeDisplayed
- Description: Estimated range displayed (cluster). OVMS reads as plain uint16 in km.
- Make: vw
- Size: 16 bits, uint16 = km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.h/vweup_obd.cpp (VWUP_MFD_RANGE_DSP)

## 0x22E4
- Name: UsableBatteryEnergyFromRangeEstimation
- Description: Usable battery energy derived from range estimation. OVMS: uint16/10 = kWh; value 511 = invalid.
- Make: vw
- Size: 16 bits, value = raw/10 kWh; 511 = invalid
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode (VWUP_MFD_RANGE_CAP)

### Brake electronics — 0x713/0x77D (VCDS 03)

## 0x1821
- Name: TirePressures
- Description: TPMS tyre pressures, read on brake electronics. Decode/size not documented in either source.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids), single source

### Engine / motor electronics — 0x7E0/0x7E8 (VCDS 01)

## 0xF45B
- Name: MotorElectronicsAbsoluteSoC
- Description: Motor-electronics absolute state of charge (e-Up). NOT battery-management 7E5/7ED. OVMS: uint8, value = raw/2.55 %.
- Make: vw
- Size: 8 bits, value = raw/2.55 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_MOT_ELEC_SOC_ABS) + scainner uds-map (labels corrected 2026-08)

## 0xF802
- Name: VinMotorElectronics
- Description: VIN reported by motor electronics. Single source, medium confidence there; decode/size not documented.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids), single source

#### EDC17 diesel DPF/engine band (shipping product: v-cu/dpf-load-monitor-wide firmware, physically tested on VAG diesels; EDC17 family — README warns DIDs vary by engine code)

## 0x10FB
- Name: TurbochargerTemperature
- Description: Turbocharger temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x11B2
- Name: DpfInletTemperature
- Description: DPF inlet temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x10F9
- Name: DpfOutletTemperature
- Description: DPF outlet temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x14F5
- Name: DpfDifferentialPressure
- Description: DPF differential pressure. Unit not documented in firmware (raw uint16 as-is).
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x1156
- Name: DistanceSinceLastRegen
- Description: Distance since last DPF regeneration.
- Make: vw
- Size: 24 bits BE, value = raw/1000 km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x115E
- Name: TimeSinceLastRegen
- Description: Time since last DPF regeneration.
- Make: vw
- Size: 24 bits BE, value = raw/60 min
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x11BE
- Name: EngineOilTemperature
- Description: Engine oil temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x114F
- Name: SootMassCalculated
- Description: DPF soot mass, calculated value.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x114E
- Name: SootMassMeasured
- Description: DPF soot mass, measured value (sensor).
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x105E
- Name: BatteryVoltage
- Description: 12V battery voltage. Firmware: value = raw×2 into int16, range 0-1999; plausibly centivolts (inference — flagged).
- Make: vw
- Size: 16 bits BE, value = raw×2; unit not documented (inference: cV — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x163B
- Name: PostInjection2
- Description: Post-injection quantity 2. Meaning/units not documented beyond name.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x167D
- Name: PostInjection3
- Description: Post-injection quantity 3. Meaning/units not documented beyond name.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

## 0x1153
- Name: OilAshMass
- Description: DPF oil ash mass. Unit not documented.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

#### 0xF4xx OBD-PID mirror band (confirmed on VAG; redundant with mode-01 where EOBD is available)

## 0xF40C
- Name: EngineRpm
- Description: Engine RPM = OBD PID 0x0C mirror. VAG-confirmed.
- Make: vw
- Size: 16 bits BE, value = raw/4 rpm
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map RESEARCH §3.2 (VAG-confirmed) + v-cu firmware (dec_rpm = raw/4) + OBDb ID.4 signalset (div 4)

## 0xF41F
- Name: RunTimeSinceEngineStart
- Description: Run time since engine start = OBD PID 0x1F mirror.
- Make: vw
- Size: 16 bits BE, value = raw/60 min
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map RESEARCH §3.2 (VAG-confirmed) + v-cu firmware (dec_u16_div60)

## 0xF405
- Name: CoolantTemperature
- Description: Coolant temperature = OBD PID 0x05 mirror.
- Make: vw
- Size: 8 bits, value = raw-40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_temp_m40) + scainner uds-map RESEARCH §3.2 (VAG-confirmed F405)

## 0xF40D
- Name: VehicleSpeed
- Description: Vehicle speed = OBD PID 0x0D mirror.
- Make: vw
- Size: 8 bits, km/h
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_u8) + OBDb ID.4 signalset (8 bits, km/h, captured test case)

## 0xF40F
- Name: IntakeAirTemperature
- Description: Intake air temperature = OBD PID 0x0F mirror.
- Make: vw
- Size: 8 bits, value = raw-40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_temp_m40) + scainner uds-map RESEARCH §3.2 (VAG-confirmed F40F)

## 0xF449
- Name: AbsolutePedalPositionDrive
- Description: Absolute pedal position (drive). ID.4 signalset only.
- Make: vw
- Size: 8 bits, value = raw/2.55 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case), single source

### HV battery management — 0x7E5/0x7ED (VCDS 8C), pre-MEB / e-Up

## 0x028C
- Name: HvBatteryAbsoluteSoc
- Description: HV battery absolute state of charge (e-Up battery management). OVMS: uint8, value = raw/2.5 %. CONFLICT: OBDb ID.4 names the same DID 'State of charge, display' with a different formula (raw×20.4/46−6.4 %) — platform-dependent, do not mix.
- Make: vw
- Size: 8 bits, e-Up: value = raw/2.5 %; ID.4: value = raw×20.4/46−6.4 % (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.h/.cpp (VWUP_BAT_MGMT_SOC_ABS, production decode) + scainner uds-map (confirmed) + OBDb ID.4 captured test case (17FE007B0462028CAE → 70.77%)

## 0x02BD
- Name: OdometerBmsView
- Description: Odometer as seen by battery management. OVMS: uint24 at offset 1 (after DID echo), value in km.
- Make: vw
- Size: 24 bits @offset 1, km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_ODOMETER) + scainner uds-map listing

## 0x2A0B
- Name: HvBatteryPackTemperature
- Description: HV battery pack temperature (signed). OVMS: signed int16, value = raw/64 °C.
- Make: vw
- Size: 16 bits signed BE, value = raw/64 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_TEMP) + scainner uds-map (scale 0.015625 = 1/64)

## 0x74CB
- Name: HvBatterySohAndCapacity
- Description: HV battery SOH/capacity block (e-Up). OVMS: bytes 0-1 = capacity (uint16, ×0.01 Ah); bytes 2-3 = cell count (uint16); bytes 4+ = per-cell SOH bytes (uint8, value = raw/240×100 % for Gen2). MEB NOTE: uds-map states 74CB is NOT reproduced on MEB (ID.4/Cupra Born use 51E0 instead).
- Make: vw
- Size: composite: 2B (Ah×0.01) + 2B (cell count) + N×1B (cell SOH)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_SOH_CAC) + scainner uds-map

## 0x1E0E
- Name: MaximumBatteryTemperature
- Description: Maximum battery temperature. DECODE NOT VERIFIED: the define exists in vweup_obd.h but the poll-table entries are commented out in the shipping source, so the decode is not exercised by the firmware.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: scainner uds-map (single community source, 'high' there); OVMS has the define but does not poll it

## 0x1E0F
- Name: MinimumBatteryTemperature
- Description: Minimum battery temperature. Same caveat as 1E0E: define exists, polling commented out.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: scainner uds-map (single community source); OVMS has the define but does not poll it

## 0x1E33
- Name: MaximumCellVoltage
- Description: Maximum HV cell voltage. e-Up/MQB decode: uint16 ×(1/4096) V. CONFLICT: OBDb ID.4 fmt block says mul 2441/div 10000 (unit volts, max 15.997) — the two sources' scalings do not obviously reconcile; the /4096 form is the one with a verified physical decode. Cupra-Born signalset confirms the DID on MEB.
- Make: vw
- Size: 16 bits BE; e-Up/MQB: value = raw/4096 V; ID.4 fmt ambiguous (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map (confirmed on MEB fixtures) + OBDb ID.4 signalset with captured test cases + OBDb Cupra-Born signalset — multi-source

## 0x1E34
- Name: MinimumCellVoltage
- Description: Minimum HV cell voltage. Same decode/conflict note as 1E33.
- Make: vw
- Size: 16 bits BE; e-Up/MQB: value = raw/4096 V; ID.4 fmt ambiguous (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map + OBDb ID.4 signalset with captured test cases + OBDb Cupra-Born signalset — multi-source

## 0x1E3B
- Name: HvBatteryPackVoltage
- Description: HV battery pack voltage. VERIFIED CAPTURE: ID.4 test case response ...62 1E 3B 05 26 → raw 0x0526=1318 → 1318/4 = 329.5 V.
- Make: vw
- Size: 16 bits BE, value = raw/4 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb ID.4 captured test case (raw response verified) + scainner uds-map (confirmed on MEB) + OBDb Cupra-Born

## 0x1E3D
- Name: HvBatteryPackCurrent
- Description: HV battery pack current, positive when discharging. uint16: value = 511 − raw/4 A (scale −0.25, bias 511).
- Make: vw
- Size: 16 bits BE, value = 511 − raw/4 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map (confirmed on MEB) + OBDb ID.4 signalset (add −511) + OBDb Cupra-Born — multi-source

## 0x51E0
- Name: HvBatteryStateOfHealthMeb
- Description: HV battery state of health, MEB platform (ID.4, Cupra Born). Supersedes 74CB on MEB. Unit %; size/decode not documented beyond unit.
- Make: vw
- Size: not documented (unit: %)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb ID.4 signalset + OBDb Cupra-Born signalset (both name it SOH, module 7E5/7ED or ta=7B) — multi-source; no captured test case found

### HV charge management — 0x765/0x7CF (VCDS BD)

## 0x1DD0
- Name: DisplayedSoc
- Description: Displayed state of charge — matches instrument cluster; the user-facing SOC. OVMS: uint8, value = raw/2 %.
- Make: vw
- Size: 8 bits, value = raw/2 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_CHG_MGMT_SOC_NORM) + scainner uds-map (high)

### Electric drive — 0x7E6/0x7EE (VCDS 51)

## 0x465C
- Name: DcDcConverterOutputVoltage
- Description: DC-DC converter output voltage (12V system). OVMS: uint16/512 V. ID.4 signalset agrees (div 512).
- Make: vw
- Size: 16 bits BE, value = raw/512 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode + OBDb ID.4 signalset (div 512, captured test case) — two independent sources

## 0x465B
- Name: DcDcConverterOutputCurrent
- Description: DC-DC converter output current (12V system). OVMS: uint16/16 A. ID.4 has a separate 'alternate' entry 465B on ta=B9 with div 16 — consistent scaling.
- Make: vw
- Size: 16 bits BE, value = raw/16 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode + OBDb ID.4 signalset (div 16, captured test case) — two independent sources

### CAN gateway — 0x710/0x77A (VCDS 19), ID.4 MEB (OBDb signalset v3, captured test cases)

## 0x15D1
- Name: ElectricMotorPowerLimitation
- Description: Composite: bits8-23 motor power limit (×50 W), bits24-31 non-vehicle power limit (×50 W), bits32-39 non-vehicle energy req (×0.05 kWh), bits40-55 motor battery energy info (×0.05 kWh).
- Make: vw
- Size: composite, 56 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2A0E
- Name: StartStopBatteryResistance
- Description: Start/stop (12V aux) battery resistance.
- Make: vw
- Size: 8 bits, value = raw×0.2 mΩ
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2A53
- Name: DcDcConverterStatus
- Description: Composite: LV voltage (8b, /10 V), current (16b @8, −511..65024 A offset-binary), reserved current (16b @24, same).
- Make: vw
- Size: composite: 8+16+16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB2
- Name: HvBatteryMaxEnergy
- Description: HV battery max energy.
- Make: vw
- Size: 16 bits, value = raw×0.05 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB4
- Name: RangeReserveAndConsumption
- Description: bits16-31 estimated electric power reserve (km); bits72-79 average battery consumption (A). Partially documented.
- Make: vw
- Size: composite, partial decode
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB5
- Name: EstimatedReserveRange
- Description: Estimated reserve range (CAN).
- Make: vw
- Size: 16 bits @32, km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB6
- Name: RangeRemainingDisplayed
- Description: Range remaining, displayed (miles per signalset — unit flagged as-is from source).
- Make: vw
- Size: 16 bits, miles (source unit)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB7
- Name: AverageConsumptionCategories
- Description: 7× uint16 average consumption categories 0-6, each /10 kWh.
- Make: vw
- Size: 7×16 bits, each value = raw/10 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB8
- Name: HvBatteryEnergy
- Description: HV battery energy.
- Make: vw
- Size: 16 bits @16, value = raw×0.025 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AF7
- Name: Aux12VBatteryStatus
- Description: Composite 12V battery: voltage (16b, /1000+4 V), current (32b @16, signed ×0.001 A), SOC (8b @56, %), temp (8b @64, −40 °C), sensor temp (8b @72, −40 °C), total charge (32b @96, /10 Ah), total discharge (32b @128, /10 Ah), aging by capacity (8b @160, %).
- Make: vw
- Size: composite, 168 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### On-board charger — 0x744/0x7AE (VCDS C6), ID.4 MEB

## 0x103D
- Name: ObcHvDcCurrent
- Description: On-board charger HV/DC current.
- Make: vw
- Size: 16 bits, value = raw/10 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x103E
- Name: ObcCycleEnergy
- Description: Cycle energy transformation.
- Make: vw
- Size: 16 bits, value = raw/100 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1507
- Name: ChargerRailEnergies
- Description: 3× uint24 rail energy transformations (rails 1-3).
- Make: vw
- Size: 3×24 bits, each value = raw/10 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1525
- Name: ObcVoltageProximitySocketA
- Description: Voltage proximity, socket A.
- Make: vw
- Size: 16 bits, mV
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15D6
- Name: ChargerPowerEfficiency
- Description: Power efficiency. NOTE: source labels unit 'amps' — likely a source typo; value = raw/10 + 75, plausible as %.
- Make: vw
- Size: 8 bits, value = raw/10 + 75 (unit ambiguous in source — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15E2
- Name: ChargerCoolantTemperature
- Description: Charger coolant temperature.
- Make: vw
- Size: 8 bits, value = raw−40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15EE
- Name: ChargingDurationTotal
- Description: Total charging duration.
- Make: vw
- Size: 32 bits, minutes
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1DA7
- Name: ObcHighVoltageOutput
- Description: High voltage output.
- Make: vw
- Size: 16 bits, value = raw/10 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1DDA
- Name: ObcTemperatureSocketA
- Description: Temperature sensor, socket A.
- Make: vw
- Size: 16 bits @8, value = raw/10 − 55 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### Auto HVAC / Climatronic — 0x746/0x7B0 (VCDS 08), ID.4 MEB

## 0x0800
- Name: AcCompressorPowerActual
- Description: A/C compressor power, actual.
- Make: vw
- Size: 16 bits @40, W
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2603
- Name: AcCompressorSpeed
- Description: A/C compressor speed.
- Make: vw
- Size: 8 bits, value = raw×100 rpm
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2605
- Name: RefrigerantPressure
- Description: Refrigerant pressure.
- Make: vw
- Size: 8 bits, value = raw×0.2 bar
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2606
- Name: RadiatorFanActual
- Description: Radiator fan actual #1 (16b) and #2 (16b @16).
- Make: vw
- Size: 2×16 bits, each value = raw/10 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only)

## 0x260A
- Name: OutsideTemperatureCabinSensor
- Description: Outside temperature from cabin sensor.
- Make: vw
- Size: 8 bits, value = raw×0.5 − 50 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x260C
- Name: TemperatureFrontLeftDeflector
- Description: Front left deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x260D
- Name: TemperatureFrontRightDeflector
- Description: Front right deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2612
- Name: TemperatureEvaporatorOutput
- Description: Evaporator output temperature (signed).
- Make: vw
- Size: 16 bits signed, value = raw/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2613
- Name: TemperatureInterior
- Description: Interior temperature (signed).
- Make: vw
- Size: 16 bits signed, value = raw/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x261E
- Name: RecircFlapActual
- Description: Recirculation flap actual: steps (16b) + percent (8b @16, ×0.5 %).
- Make: vw
- Size: 16+8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x261F
- Name: RecircFlapCommandedSteps
- Description: Recirculation flap commanded steps.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2620
- Name: RecircFlapStopFreshAir
- Description: Recirculation flap stop, fresh air.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2621
- Name: RecircFlapStopRecircAir
- Description: Recirculation flap stop, recirculated air.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2622
- Name: FrontLeftTempFlapActual
- Description: Front left temperature flap actual.
- Make: vw
- Size: 8 bits @16, value = raw×0.5 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2626
- Name: FrontRightTempFlapActual
- Description: Front right temperature flap actual.
- Make: vw
- Size: 8 bits @16, value = raw×0.5 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x263D
- Name: TemperatureRearDeflector
- Description: Rear deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x26ED
- Name: AirPollutionLevel
- Description: Air pollution level (signed).
- Make: vw
- Size: 8 bits signed, value = raw/10
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x27C3
- Name: OutsideHumidity
- Description: Outside humidity.
- Make: vw
- Size: 8 bits @56, value = raw/2 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only)

## 0x27C4
- Name: WindshieldTempAndInsideHumidity
- Description: Windshield temperature (8b, ×0.576−38.8 °C) + inside humidity (8b @32, /2 %).
- Make: vw
- Size: 8+8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x42DB
- Name: Co2ContentInterior
- Description: CO2 content, interior.
- Make: vw
- Size: 8 bits @8, value = raw×100 (unit scalar as in source — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x4EEF
- Name: AcRefrigerantSensors
- Description: A/C refrigerant: pressure sensor 1 (16b, ×0.0088 bar), temperature sensor 1 (16b @16, ×0.1−40 °C), interior temp sensor 1 (16b @32, ×0.1−40 °C).
- Make: vw
- Size: 3×16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### Telematics — 0x767/0x7D1 (VCDS 77), ID.4 MEB

## 0x2431
- Name: GpsSatellites
- Description: GPS satellites visible (8b) / tracked (8b @8).
- Make: vw
- Size: 2×8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### MEB target-addressed band (OBDb hdr FC00; ta=7B battery / ta=76 electric drive / ta=B9 DC-DC)

DIDs below are addressed through FC00 with a target-address byte (ta). DID, signal names and decodes are from the
OBDb ID.4 signalset v3; 'captured test case' means a real vehicle response is on file in tests/test_cases (Grade B),
'signalset only' means decode-from-schema with no capture on file (Grade C). Raw CAN framing needs field verification
(see addressing note at top).

## 0x0308
- Name: CALCFROMMEASIS
- Description: ta=7B (battery). Torque, calculated from measured currents [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x0335
- Name: MOTORTRQFRONT
- Description: ta=76 (electric drive). Motor torque, front [16 bits @bit 0; signed; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x033B
- Name: MOTORTRQREAR
- Description: ta=76 (electric drive). Motor torque, rear [16 bits @bit 0; signed; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0343
- Name: MOTORTRQDIFF
- Description: ta=76 (electric drive). Motor torque difference, front to rear [16 bits @bit 0; signed; value = raw ÷2; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0344
- Name: MOTORTRQRATEDFRONT
- Description: ta=76 (electric drive). Motor torque rated, front [16 bits @bit 0; signed; value = raw ÷2; newtonMeters] | Motor torque rated, rear [16 bits @bit 16; signed; value = raw ÷2; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0346
- Name: STEERANGLE
- Description: ta=76 (electric drive). Steering wheel angle [16 bits @bit 0; value = raw ÷10; degrees]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x035E
- Name: HVBATIENG
- Description: ta=76 (electric drive). Battery current, motor controller [16 bits @bit 0; signed; value = raw ÷10; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0360
- Name: HVAUXI
- Description: ta=76 (electric drive). HV auxiliary current total [16 bits @bit 0; signed; value = raw ÷100; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0364
- Name: HVAUXPWR
- Description: ta=76 (electric drive). HV auxiliary power [16 bits @bit 0; signed; value = raw ÷10; kilowatts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0800
- Name: ACCOMPRESSORPWRACT
- Description: ta=?. A/C compressor power, actual [16 bits @bit 40; watts]
- Make: vw
- Size: up to 56 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x0805
- Name: ELDRIVEECUT1
- Description: ta=7B (battery). Electric drive ECU temperature 1 [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x0806
- Name: ELDRIVEECUT2
- Description: ta=7B (battery). Electric drive ECU temperature 2 [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x086D
- Name: ODO
- Description: ta=7B (battery). Odometer, electric drive [32 bits @bit 0; kilometers]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1007
- Name: MOTORVDACT
- Description: ta=7B (battery). Motor voltage, d-axis actual [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1008
- Name: MOTORVQACT
- Description: ta=7B (battery). Motor voltage, q-axis actual [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1009
- Name: MOTORVDCMD
- Description: ta=7B (battery). Motor voltage, d-axis commanded [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x100A
- Name: MOTORVQCMD
- Description: ta=7B (battery). Motor voltage, q-axis commanded [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x103D
- Name: OBCHVDCC
- Description: ta=?. On-board charger, hv/dc current [16 bits @bit 0; value = raw ÷10; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x103E
- Name: OBCCYCLEENERGY
- Description: ta=?. Cycle energy transformation [16 bits @bit 0; value = raw ÷100; kilowattHours]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1040
- Name: INVERTERPWRLOSSPHASEU
- Description: ta=7B (battery). Inverter power loss phase u [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1041
- Name: INVERTERPWRLOSSPHASEV
- Description: ta=7B (battery). Inverter power loss phase v [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1042
- Name: INVERTERPWRLOSSPHASEW
- Description: ta=7B (battery). Inverter power loss phase w [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x1507
- Name: CHRGRRAIL1E
- Description: ta=?. Rail 1 energy transformation [24 bits @bit 0; value = raw ÷10; kilowattHours] | Rail 2 energy transformation [24 bits @bit 24; value = raw ÷10; kilowattHours] | Rail 3 energy transformation [24 bits @bit 48; value = raw ÷10; kilowattHours]
- Make: vw
- Size: up to 72 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1525
- Name: OBCVPROXA
- Description: ta=?. Voltage proximity, socket a [16 bits @bit 0; millivolts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15D1
- Name: HVEMPWRLIMITATION
- Description: ta=?. Electric motor power limitation [16 bits @bit 8; value = raw ×50; watts] | Electric motor non-vehicle power limitation [8 bits @bit 24; value = raw ×50; watts] | Non-vehicle energy requirement [8 bits @bit 32; value = raw ×50 ÷1000; kilowattHours] | Electric motor battery energy [16 bits @bit 40; value = raw ×50 ÷1000; kilowattHours]
- Make: vw
- Size: up to 56 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15D6
- Name: CHRGREFFICIENCY
- Description: ta=?. Power efficiency [8 bits @bit 0; value = raw ÷10 +75; amps]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15E2
- Name: CHRGRCOOLANTT
- Description: ta=?. Temperature, Charger coolant [8 bits @bit 0; value = raw -40; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x15EE
- Name: CHRGRDURTOTAL
- Description: ta=?. Charging duration total [32 bits @bit 0; minutes]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1620
- Name: HVBATPTCI
- Description: ta=7B (battery). Battery heater current [8 bits @bit 0; value = raw ÷4; amps]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1621
- Name: HVBATPTCV
- Description: ta=7B (battery). Battery heater voltage [8 bits @bit 0; value = raw ÷10; volts]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1622
- Name: HVBATECUT
- Description: ta=7B (battery). ECU temperature [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1623
- Name: HVBATPTCT1
- Description: ta=7B (battery). Battery heater temperature, #1 [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1624
- Name: HVBATPTCT2
- Description: ta=7B (battery). Battery heater temperature, #2 [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x189B
- Name: HVBATAFTERCONTACTSV
- Description: ta=7B (battery). HV battery after contacts voltage [16 bits @bit 0; value = raw ×0.5 -1000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x189D
- Name: HVBATTOUT
- Description: ta=7B (battery). Battery temperature, outlet [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, inlet [16 bits @bit 16; signed; value = raw ÷64; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1DA7
- Name: OBCHIGHVOUTPUT
- Description: ta=?. High voltage output [16 bits @bit 0; value = raw ÷10; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1DDA
- Name: OBCTA
- Description: ta=?. Temperature sensor, socket a [16 bits @bit 8; value = raw ÷10 -55; celsius]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E0E
- Name: HVBATTMAX
- Description: ta=7B (battery). Battery temperature, max [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, max sensor ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E0F
- Name: HVBATTMIN
- Description: ta=7B (battery). Battery temperature, min [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, min sensor ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E1B
- Name: HVBATILIMCHG
- Description: ta=7B (battery). Battery current limit, charging [16 bits @bit 0; value = raw ÷5; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E1C
- Name: HVBATILIMDSCH
- Description: ta=7B (battery). Battery current limit, discharging [16 bits @bit 0; value = raw ÷5; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E2C
- Name: HVBATCELLSOCMAX
- Description: ta=7B (battery). Battery cell soc, maximum [16 bits @bit 0; value = raw ÷100; percent] | Battery cell soc max, ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E2D
- Name: HVBATCELLSOCMIN
- Description: ta=7B (battery). Battery cell soc, minimum [16 bits @bit 0; value = raw ÷100; percent] | Battery cell soc min, ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E36
- Name: HVBATVBEFORE
- Description: ta=7B (battery). Battery voltage, before main switch [16 bits @bit 0; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E38
- Name: HVBATVAFTER
- Description: ta=7B (battery). Battery voltage, after main switch [16 bits @bit 0; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E39
- Name: HVBATVCHG
- Description: ta=7B (battery). Battery voltage, charging [16 bits @bit 0; signed; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E3C
- Name: HVBATVCELLSSUM
- Description: ta=7B (battery). Battery voltage, sum of all cells [32 bits @bit 0; signed; value = raw ×244140625 ÷1000000000; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E3E
- Name: HVBATIDC2
- Description: ta=7B (battery). Battery current, DC (alt) [32 bits @bit 0; value = raw ÷100 -1500; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E40
- Name: HVBATCELLV001
- Description: ta=7B (battery). HV battery cell voltage, #1 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E41
- Name: HVBATCELLV002
- Description: ta=7B (battery). HV battery cell voltage, #2 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E42
- Name: HVBATCELLV003
- Description: ta=7B (battery). HV battery cell voltage, #3 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E43
- Name: HVBATCELLV004
- Description: ta=7B (battery). HV battery cell voltage, #4 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E44
- Name: HVBATCELLV005
- Description: ta=7B (battery). HV battery cell voltage, #5 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E45
- Name: HVBATCELLV006
- Description: ta=7B (battery). HV battery cell voltage, #6 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E46
- Name: HVBATCELLV007
- Description: ta=7B (battery). HV battery cell voltage, #7 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E47
- Name: HVBATCELLV008
- Description: ta=7B (battery). HV battery cell voltage, #8 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E48
- Name: HVBATCELLV009
- Description: ta=7B (battery). HV battery cell voltage, #9 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E49
- Name: HVBATCELLV010
- Description: ta=7B (battery). HV battery cell voltage, #10 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4A
- Name: HVBATCELLV011
- Description: ta=7B (battery). HV battery cell voltage, #11 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4B
- Name: HVBATCELLV012
- Description: ta=7B (battery). HV battery cell voltage, #12 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4C
- Name: HVBATCELLV013
- Description: ta=7B (battery). HV battery cell voltage, #13 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4D
- Name: HVBATCELLV014
- Description: ta=7B (battery). HV battery cell voltage, #14 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4E
- Name: HVBATCELLV015
- Description: ta=7B (battery). HV battery cell voltage, #15 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E4F
- Name: HVBATCELLV016
- Description: ta=7B (battery). HV battery cell voltage, #16 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E50
- Name: HVBATCELLV017
- Description: ta=7B (battery). HV battery cell voltage, #17 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E51
- Name: HVBATCELLV018
- Description: ta=7B (battery). HV battery cell voltage, #18 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E52
- Name: HVBATCELLV019
- Description: ta=7B (battery). HV battery cell voltage, #19 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E53
- Name: HVBATCELLV020
- Description: ta=7B (battery). HV battery cell voltage, #20 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E54
- Name: HVBATCELLV021
- Description: ta=7B (battery). HV battery cell voltage, #21 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E55
- Name: HVBATCELLV022
- Description: ta=7B (battery). HV battery cell voltage, #22 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E56
- Name: HVBATCELLV023
- Description: ta=7B (battery). HV battery cell voltage, #23 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E57
- Name: HVBATCELLV024
- Description: ta=7B (battery). HV battery cell voltage, #24 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E58
- Name: HVBATCELLV025
- Description: ta=7B (battery). HV battery cell voltage, #25 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E59
- Name: HVBATCELLV026
- Description: ta=7B (battery). HV battery cell voltage, #26 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5A
- Name: HVBATCELLV027
- Description: ta=7B (battery). HV battery cell voltage, #27 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5B
- Name: HVBATCELLV028
- Description: ta=7B (battery). HV battery cell voltage, #28 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5C
- Name: HVBATCELLV029
- Description: ta=7B (battery). HV battery cell voltage, #29 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5D
- Name: HVBATCELLV030
- Description: ta=7B (battery). HV battery cell voltage, #30 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5E
- Name: HVBATCELLV031
- Description: ta=7B (battery). HV battery cell voltage, #31 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E5F
- Name: HVBATCELLV032
- Description: ta=7B (battery). HV battery cell voltage, #32 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E60
- Name: HVBATCELLV033
- Description: ta=7B (battery). HV battery cell voltage, #33 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E61
- Name: HVBATCELLV034
- Description: ta=7B (battery). HV battery cell voltage, #34 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E62
- Name: HVBATCELLV035
- Description: ta=7B (battery). HV battery cell voltage, #35 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E63
- Name: HVBATCELLV036
- Description: ta=7B (battery). HV battery cell voltage, #36 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E64
- Name: HVBATCELLV037
- Description: ta=7B (battery). HV battery cell voltage, #37 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E65
- Name: HVBATCELLV038
- Description: ta=7B (battery). HV battery cell voltage, #38 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E66
- Name: HVBATCELLV039
- Description: ta=7B (battery). HV battery cell voltage, #39 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E67
- Name: HVBATCELLV040
- Description: ta=7B (battery). HV battery cell voltage, #40 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E68
- Name: HVBATCELLV041
- Description: ta=7B (battery). HV battery cell voltage, #41 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E69
- Name: HVBATCELLV042
- Description: ta=7B (battery). HV battery cell voltage, #42 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6A
- Name: HVBATCELLV043
- Description: ta=7B (battery). HV battery cell voltage, #43 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6B
- Name: HVBATCELLV044
- Description: ta=7B (battery). HV battery cell voltage, #44 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6C
- Name: HVBATCELLV045
- Description: ta=7B (battery). HV battery cell voltage, #45 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6D
- Name: HVBATCELLV046
- Description: ta=7B (battery). HV battery cell voltage, #46 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6E
- Name: HVBATCELLV047
- Description: ta=7B (battery). HV battery cell voltage, #47 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E6F
- Name: HVBATCELLV048
- Description: ta=7B (battery). HV battery cell voltage, #48 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E70
- Name: HVBATCELLV049
- Description: ta=7B (battery). HV battery cell voltage, #49 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E71
- Name: HVBATCELLV050
- Description: ta=7B (battery). HV battery cell voltage, #50 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E72
- Name: HVBATCELLV051
- Description: ta=7B (battery). HV battery cell voltage, #51 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E73
- Name: HVBATCELLV052
- Description: ta=7B (battery). HV battery cell voltage, #52 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E74
- Name: HVBATCELLV053
- Description: ta=7B (battery). HV battery cell voltage, #53 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E75
- Name: HVBATCELLV054
- Description: ta=7B (battery). HV battery cell voltage, #54 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E76
- Name: HVBATCELLV055
- Description: ta=7B (battery). HV battery cell voltage, #55 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E77
- Name: HVBATCELLV056
- Description: ta=7B (battery). HV battery cell voltage, #56 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E78
- Name: HVBATCELLV057
- Description: ta=7B (battery). HV battery cell voltage, #57 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E79
- Name: HVBATCELLV058
- Description: ta=7B (battery). HV battery cell voltage, #58 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7A
- Name: HVBATCELLV059
- Description: ta=7B (battery). HV battery cell voltage, #59 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7B
- Name: HVBATCELLV060
- Description: ta=7B (battery). HV battery cell voltage, #60 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7C
- Name: HVBATCELLV061
- Description: ta=7B (battery). HV battery cell voltage, #61 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7D
- Name: HVBATCELLV062
- Description: ta=7B (battery). HV battery cell voltage, #62 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7E
- Name: HVBATCELLV063
- Description: ta=7B (battery). HV battery cell voltage, #63 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E7F
- Name: HVBATCELLV064
- Description: ta=7B (battery). HV battery cell voltage, #64 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E80
- Name: HVBATCELLV065
- Description: ta=7B (battery). HV battery cell voltage, #65 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E81
- Name: HVBATCELLV066
- Description: ta=7B (battery). HV battery cell voltage, #66 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E82
- Name: HVBATCELLV067
- Description: ta=7B (battery). HV battery cell voltage, #67 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E83
- Name: HVBATCELLV068
- Description: ta=7B (battery). HV battery cell voltage, #68 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E84
- Name: HVBATCELLV069
- Description: ta=7B (battery). HV battery cell voltage, #69 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E85
- Name: HVBATCELLV070
- Description: ta=7B (battery). HV battery cell voltage, #70 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E86
- Name: HVBATCELLV071
- Description: ta=7B (battery). HV battery cell voltage, #71 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E87
- Name: HVBATCELLV072
- Description: ta=7B (battery). HV battery cell voltage, #72 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E88
- Name: HVBATCELLV073
- Description: ta=7B (battery). HV battery cell voltage, #73 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E89
- Name: HVBATCELLV074
- Description: ta=7B (battery). HV battery cell voltage, #74 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8A
- Name: HVBATCELLV075
- Description: ta=7B (battery). HV battery cell voltage, #75 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8B
- Name: HVBATCELLV076
- Description: ta=7B (battery). HV battery cell voltage, #76 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8C
- Name: HVBATCELLV077
- Description: ta=7B (battery). HV battery cell voltage, #77 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8D
- Name: HVBATCELLV078
- Description: ta=7B (battery). HV battery cell voltage, #78 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8E
- Name: HVBATCELLV079
- Description: ta=7B (battery). HV battery cell voltage, #79 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E8F
- Name: HVBATCELLV080
- Description: ta=7B (battery). HV battery cell voltage, #80 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E90
- Name: HVBATCELLV081
- Description: ta=7B (battery). HV battery cell voltage, #81 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E91
- Name: HVBATCELLV082
- Description: ta=7B (battery). HV battery cell voltage, #82 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E92
- Name: HVBATCELLV083
- Description: ta=7B (battery). HV battery cell voltage, #83 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E93
- Name: HVBATCELLV084
- Description: ta=7B (battery). HV battery cell voltage, #84 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E94
- Name: HVBATCELLV085
- Description: ta=7B (battery). HV battery cell voltage, #85 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E95
- Name: HVBATCELLV086
- Description: ta=7B (battery). HV battery cell voltage, #86 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E96
- Name: HVBATCELLV087
- Description: ta=7B (battery). HV battery cell voltage, #87 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E97
- Name: HVBATCELLV088
- Description: ta=7B (battery). HV battery cell voltage, #88 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E98
- Name: HVBATCELLV089
- Description: ta=7B (battery). HV battery cell voltage, #89 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E99
- Name: HVBATCELLV090
- Description: ta=7B (battery). HV battery cell voltage, #90 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9A
- Name: HVBATCELLV091
- Description: ta=7B (battery). HV battery cell voltage, #91 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9B
- Name: HVBATCELLV092
- Description: ta=7B (battery). HV battery cell voltage, #92 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9C
- Name: HVBATCELLV093
- Description: ta=7B (battery). HV battery cell voltage, #93 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9D
- Name: HVBATCELLV094
- Description: ta=7B (battery). HV battery cell voltage, #94 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9E
- Name: HVBATCELLV095
- Description: ta=7B (battery). HV battery cell voltage, #95 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1E9F
- Name: HVBATCELLV096
- Description: ta=7B (battery). HV battery cell voltage, #96 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA0
- Name: HVBATCELLV097
- Description: ta=7B (battery). HV battery cell voltage, #97 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA1
- Name: HVBATCELLV098
- Description: ta=7B (battery). HV battery cell voltage, #98 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA2
- Name: HVBATCELLV099
- Description: ta=7B (battery). HV battery cell voltage, #99 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA3
- Name: HVBATCELLV100
- Description: ta=7B (battery). HV battery cell voltage, #100 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA4
- Name: HVBATCELLV101
- Description: ta=7B (battery). HV battery cell voltage, #101 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA5
- Name: HVBATCELLV102
- Description: ta=7B (battery). HV battery cell voltage, #102 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA6
- Name: HVBATCELLV103
- Description: ta=7B (battery). HV battery cell voltage, #103 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA7
- Name: HVBATCELLV104
- Description: ta=7B (battery). HV battery cell voltage, #104 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA8
- Name: HVBATCELLV105
- Description: ta=7B (battery). HV battery cell voltage, #105 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EA9
- Name: HVBATCELLV106
- Description: ta=7B (battery). HV battery cell voltage, #106 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EAA
- Name: HVBATCELLV107
- Description: ta=7B (battery). HV battery cell voltage, #107 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EAB
- Name: HVBATCELLV108
- Description: ta=7B (battery). HV battery cell voltage, #108 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EAE
- Name: HVBATMODT1
- Description: ta=7B (battery). HV battery module temperature, #1 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EAF
- Name: HVBATMODT2
- Description: ta=7B (battery). HV battery module temperature, #2 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB0
- Name: HVBATMODT3
- Description: ta=7B (battery). HV battery module temperature, #3 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB1
- Name: HVBATMODT4
- Description: ta=7B (battery). HV battery module temperature, #4 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB2
- Name: HVBATMODT5
- Description: ta=7B (battery). HV battery module temperature, #5 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB3
- Name: HVBATMODT6
- Description: ta=7B (battery). HV battery module temperature, #6 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB4
- Name: HVBATMODT7
- Description: ta=7B (battery). HV battery module temperature, #7 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB5
- Name: HVBATMODT8
- Description: ta=7B (battery). HV battery module temperature, #8 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB6
- Name: HVBATMODT9
- Description: ta=7B (battery). HV battery module temperature, #9 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB7
- Name: HVBATMODT10
- Description: ta=7B (battery). HV battery module temperature, #10 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB8
- Name: HVBATMODT11
- Description: ta=7B (battery). HV battery module temperature, #11 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EB9
- Name: HVBATMODT12
- Description: ta=7B (battery). HV battery module temperature, #12 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EBA
- Name: HVBATMODT13
- Description: ta=7B (battery). HV battery module temperature, #13 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EBB
- Name: HVBATMODT14
- Description: ta=7B (battery). HV battery module temperature, #14 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EBC
- Name: HVBATMODT15
- Description: ta=7B (battery). HV battery module temperature, #15 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x1EBD
- Name: HVBATMODT16
- Description: ta=7B (battery). HV battery module temperature, #16 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2005
- Name: BRAKEBOOSTERP
- Description: ta=76 (electric drive). Brake booster pressure [16 bits @bit 0; value = raw ÷1000; bars]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2055
- Name: RADIATORFANDUTY
- Description: ta=76 (electric drive). Radiator fan duty [16 bits @bit 0; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2431
- Name: GPSSATSVISIBLE
- Description: ta=?. Satellites, visible [8 bits @bit 0; scalar] | Satellites, tracked [8 bits @bit 8; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2603
- Name: ACCMPRSPEED
- Description: ta=?. A/C compressor, speed [8 bits @bit 0; value = raw ×100; rpm]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2605
- Name: REFRIGP
- Description: ta=?. Refrigerant pressure [8 bits @bit 0; value = raw ×0.2; bars]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2606
- Name: HVACFAN1ACT
- Description: ta=?. Radiator fan actual #1 [16 bits @bit 0; value = raw ÷10; percent] | Radiator fan actual #2 [16 bits @bit 16; value = raw ÷10; percent]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x260A
- Name: AATCABIN
- Description: ta=?. Outside temperature, from cabin sensor [8 bits @bit 0; value = raw ×0.5 -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x260C
- Name: FRONTLEFTDEFLT
- Description: ta=?. Temperature, front left deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x260D
- Name: FRONTRIGHTDEFLT
- Description: ta=?. Temperature, front right deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2612
- Name: HVACEVAPT
- Description: ta=?. Temperature, evaporator output [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2613
- Name: HVACIAT
- Description: ta=?. Temperature, interior [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x261E
- Name: RECIRCFLAPACTSTEPS
- Description: ta=?. Recirculation flap, actual steps [16 bits @bit 0; scalar] | Recirculation flap, actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x261F
- Name: RECIRCFLAPCMDSTEPS
- Description: ta=?. Recirculation flap, commanded steps [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2620
- Name: RECIRCFLAPSTOPFRESH
- Description: ta=?. Recirculation flap stop, fresh air [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2621
- Name: RECIRCFLAPSTOPRECIRC
- Description: ta=?. Recirculation flap stop, recirculated air [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2622
- Name: FRONTLEFTTFLAPACT
- Description: ta=?. Front left temperature flap actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2626
- Name: FRONTRIGHTTFLAPACT
- Description: ta=?. Front right temperature flap actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x263D
- Name: REARDEFLT
- Description: ta=?. Temperature, rear deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x26ED
- Name: AIRPOLUTION
- Description: ta=?. Air pollution level [8 bits @bit 0; signed; value = raw ÷10; scalar]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x276D
- Name: COOLANTCIRCPUMPDUTY
- Description: ta=76 (electric drive). Coolant circulation pump duty [16 bits @bit 0; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x27C3
- Name: HVACOUTSIDEHUM
- Description: ta=?. Outside humidity [8 bits @bit 56; value = raw ÷2; percent]
- Make: vw
- Size: up to 64 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x27C4
- Name: WNDSHLDTEMP
- Description: ta=?. Windshield, temperature [8 bits @bit 0; value = raw ×0.576 -38.8; celsius] | Humidity, inside [8 bits @bit 32; value = raw ÷2; percent]
- Make: vw
- Size: up to 40 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x295A
- Name: ENGODO
- Description: ta=76 (electric drive). Odometer [24 bits @bit 0; kilometers]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x29D4
- Name: MOTORTRQREQ
- Description: ta=76 (electric drive). Motor torque requested [16 bits @bit 0; value = raw ÷10; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2A0E
- Name: SSBR
- Description: ta=?. Start/stop battery resistance [8 bits @bit 0; value = raw ×2 ÷10; milliohms]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2A53
- Name: DCDCVLOW
- Description: ta=?. DC-DC converter, low voltage [8 bits @bit 0; value = raw ÷10; volts] | DC-DC converter, current [16 bits @bit 8; value = raw -511; amps] | DC-DC converter, reserved current [16 bits @bit 24; value = raw -511; amps]
- Make: vw
- Size: up to 40 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB2
- Name: HVBATCAP
- Description: ta=?. HV battery, max energy [16 bits @bit 0; value = raw ×50 ÷1000; kilowattHours]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB4
- Name: RANGERESERVEEST
- Description: ta=?. Estimated electric power reserve [16 bits @bit 16; kilometers] | Average battery consumption [8 bits @bit 72; amps]
- Make: vw
- Size: up to 80 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB5
- Name: RANGEESTCAN
- Description: ta=?. Estimated reserve range [16 bits @bit 32; kilometers]
- Make: vw
- Size: up to 48 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB6
- Name: RANGE
- Description: ta=?. Range remaining, displayed [16 bits @bit 0; miles]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB7
- Name: AVGCSMPCAT0
- Description: ta=?. Average consumption (category 0) [16 bits @bit 0; value = raw ÷10; kilowattHours] | Average consumption (category 1) [16 bits @bit 16; value = raw ÷10; kilowattHours] | Average consumption (category 2) [16 bits @bit 32; value = raw ÷10; kilowattHours] | Average consumption (category 3) [16 bits @bit 48; value = raw ÷10; kilowattHours] | Average consumption (category 4) [16 bits @bit 64; value = raw ÷10; kilowattHours] | Average consumption (category 5) [16 bits @bit 80; value = raw ÷10; kilowattHours] | Average consumption (category 6) [16 bits @bit 96; value = raw ÷10; kilowattHours]
- Make: vw
- Size: up to 112 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AB8
- Name: HVBATKWH
- Description: ta=?. HV battery energy [16 bits @bit 16; value = raw ×25 ÷1000; kilowattHours]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2AF7
- Name: AUXBATV
- Description: ta=?. 12V battery voltage [16 bits @bit 0; value = raw ÷1000 +4; volts] | 12V battery current [32 bits @bit 16; signed; value = raw ×0.001; amps] | 12V battery soc [8 bits @bit 56; percent] | Temperature, 12V battery [8 bits @bit 64; value = raw -40; celsius] | Temperature, 12V battery sensor [8 bits @bit 72; value = raw -40; celsius] | 12V battery total charge [32 bits @bit 96; value = raw ÷10; ampereHours] | 12V battery total discharge [32 bits @bit 128; value = raw ÷10; ampereHours] | 12V battery aging by capacity [8 bits @bit 160; percent] | 12V battery aging by power [8 bits @bit 168; percent] | 12V battery adapted capacity [8 bits @bit 176; ampereHours]
- Make: vw
- Size: up to 184 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x2CCC
- Name: ROTORTMODEL
- Description: ta=7B (battery). Rotor temperature model [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3DEF
- Name: SOC
- Description: ta=76 (electric drive). State of charge [16 bits @bit 0; signed; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x3DF8
- Name: MOTORRPM
- Description: ta=76 (electric drive). Motor speed [16 bits @bit 0; signed; value = raw ÷2; rpm]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x3E93
- Name: DCLINKV
- Description: ta=7B (battery). DC link voltage [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3E98
- Name: DCLINKI
- Description: ta=7B (battery). DC link current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EE7
- Name: MOTORMAXIMUMI
- Description: ta=7B (battery). Motor maximum current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EE8
- Name: MOTORMINIMUMI
- Description: ta=7B (battery). Motor minimum current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EE9
- Name: ACTUALMECHANICALTORQUECALC
- Description: ta=7B (battery). Actual mechanical torque calculated [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EEA
- Name: ACTUALPOSSIBLEMAXIMUMTORQUE
- Description: ta=7B (battery). Actual possible maximum torque [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EEB
- Name: ACTUALPOSSIBLEMINIMUMTORQUE
- Description: ta=7B (battery). Actual possible minimum torque [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x3EED
- Name: DESIREDLINKV
- Description: ta=7B (battery). Desired link voltage [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x40C8
- Name: ELDRIVEMOTORRADSEC
- Description: ta=7B (battery). Electric drive motor speed (rad/sec) [32 bits @bit 0; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x42DB
- Name: CO2CONTENTINTERIOR
- Description: ta=?. CO2 content interior [8 bits @bit 8; value = raw ×100; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x43B8
- Name: DCDCTCOOL
- Description: ta=76 (electric drive). Temperature, DC-DC converter coolant [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x43B9
- Name: DCLINKVRESERVE
- Description: ta=7B (battery). DC link voltage reserve [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x4539
- Name: ACCEL
- Description: ta=76 (electric drive). Acceleration [16 bits @bit 0; signed; value = raw ÷1000; metersPerSecondSquared]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x4657
- Name: ELDRIVEMOTORFREQ
- Description: ta=7B (battery). Motor electrical frequency (rad/sec) [32 bits @bit 0; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x465D
- Name: DCDCV
- Description: ta=B9 (DC-DC). DC-DC voltage [16 bits @bit 0; value = raw ÷512; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x4672
- Name: MOTORT
- Description: ta=7B (battery). Temperature, motor [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x4675
- Name: HVBATVTRAC
- Description: ta=76 (electric drive). Battery voltage, traction mode [16 bits @bit 0; signed; value = raw ÷10; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x4EEF
- Name: ACREFRIGPSENS1
- Description: ta=?. A/C refrigerant pressure, sensor 1 [16 bits @bit 0; value = raw ×88 ÷10000; bars] | A/C refrigerant temperature, sensor 1 [16 bits @bit 16; value = raw ×10 ÷100 -40; celsius] | A/C refrigerant temperature, sensor 1 interior [16 bits @bit 32; value = raw ×10 ÷100 -40; celsius]
- Make: vw
- Size: up to 48 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x4FAE
- Name: ELECDRIVEINFLOWCOOLANTT
- Description: ta=7B (battery). Temperature, electric drive inflow coolant [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x5170
- Name: MINIMUMDISCHARGEV
- Description: ta=7B (battery). Discharge voltage, min [16 bits @bit 0; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x5171
- Name: MAXIMUMCHARGEV
- Description: ta=7B (battery). Charge voltage, max [16 bits @bit 0; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x5867
- Name: ODOBMS2
- Description: ta=7B (battery). Odometer, BMS #2 [16 bits @bit 16; value = raw ×10; kilometers]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x58E1
- Name: ACTUALMECHANICALTORQUECMDVALUE
- Description: ta=7B (battery). Actual mechanical torque commanded [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

## 0x7425
- Name: HVBATMODT17
- Description: ta=7B (battery). HV battery module temperature, #17 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x7426
- Name: HVBATMODT18
- Description: ta=7B (battery). HV battery module temperature, #18 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x7427
- Name: HVBATMODT19
- Description: ta=7B (battery). HV battery module temperature, #19 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x7428
- Name: HVBATMODT20
- Description: ta=7B (battery). HV battery module temperature, #20 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x7429
- Name: HVBATMODT21
- Description: ta=7B (battery). HV battery module temperature, #21 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x742A
- Name: HVBATMODT22
- Description: ta=7B (battery). HV battery module temperature, #22 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x742B
- Name: HVBATMODT23
- Description: ta=7B (battery). HV battery module temperature, #23 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x742C
- Name: HVBATMODT24
- Description: ta=7B (battery). HV battery module temperature, #24 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x743B
- Name: CIRCPUMPFLOW
- Description: ta=7B (battery). HV battery: circulation pump flow [8 bits @bit 0; value = raw ×10; percent]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## 0x7448
- Name: RAPIDCHARGEPORT
- Description: ta=7B (battery). Charging, rapid? [1 bits @bit 4; noyes] | AC charging [1 bits @bit 5; noyes] | Current gear [1 bits @bit 7; enum: 0=STANDBY, 1=DRIVING]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

## Coverage notes

- No Grade A (OEM service information) DIDs: VW publishes these in ODIS/ASAM datasets which are not publicly available.
  The closest to OEM provenance is the ODIS-database extraction (ConnorHowell/vag-uds-ids), an unlicensed single source.
- Could NOT verify any manufacturer-specific 0x22 DIDs for: central electronics 09 (0x70E/0x778),
  infotainment 5F (0x773/0x7DD), transmission 02 (0x7E1/0x7E9), airbag 15 (0x715/0x77F), immobilizer 25 (0x711/0x77B),
  steering assist 44 (0x712/0x71A), brake boost 23 (0x73B/0x743). The module address pairs are known (see table) but no
  public DID list with verified reads was found for those modules.
- Systematic gaps: VCDS 'Advanced Measuring Values' IDE codes (e.g. IDE00558/IDE00559 broadband O2, IDE01912) are UDS DIDs
  under the hood (community-confirmed), but no public IDE-code-to-DID-hex mapping was found — that mapping is a major
  unverified area; adaptation channels (0x2E/0x31 flows) likewise map to DIDs internally but no verified table exists publicly.
- CONFLICT (reported, not resolved): MEB BMS addressing — scainner uds-map lists MEB DIDs on legacy 11-bit 0x7E5/0x7ED-style
  addresses ('legacy pre-MEB address still alive on MEB'), while the OBDb ID.4 signalset routes the same DIDs through
  FC00 with extended target addressing (ta=7B/76/B9). Both agree on DID numbers and decodes; only the CAN framing differs.
- CONFLICT (reported, not resolved): 0x028C — e-Up absolute SOC = raw/2.5 % vs ID.4 display SOC = raw×20.4/46−6.4 %.
  Same DID, different platform, different formula. Treat as platform-specific.
- CONFLICT (reported, not resolved): 0x1E33/0x1E34 cell-voltage scaling — /4096 V (verified physical decode on e-Up/MQB,
  matches OVMS) vs the ID.4 signalset's mul 2441/div 10000 entry whose unit scaling is ambiguous. Prefer /4096 until
  a captured ID.4 1E33 response is hand-decoded.
- F4xx band entries are OBD-PID mirrors; deprioritise for sweep purposes (mode-01 covers the same data where EOBD answers).
- Pre-UDS / KWP2000-era VAG ECUs do not answer 0x22 at all (community-verified on MED17.5 TP2.0) — a silent 0x22 on those
  is expected, not a fault.
- Local opendbc clone checked (2026-10-06): no VW 0x22/DID references beyond the generic uds.py service table;
  opendbc/car/volkswagen/*.py contain only cyclic broadcast CAN frames.
- MEB cell-voltage band 0x1E40-0x1EAB (cells 1-108) and module-temperature bands 0x1EAE-0x1EBD / 0x7425-0x742C follow a
  uniform one-DID-per-cell pattern; each has a captured test case on file.
