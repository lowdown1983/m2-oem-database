# Toyota / Lexus — Manufacturer-Specific UDS DIDs (Service 0x22)

Research for the M2 OEM vehicle database (v1.3). Toyota/Lexus-specific Data
Identifiers read via UDS service 0x22 (ReadDataByIdentifier). ISO-standard
identification DIDs (0xF180–0xF19E: VIN, serial, supplier IDs, etc.) are
covered separately and NOT duplicated here, except 0xF19A/0xF19D which are
Toyota-specific live-data DIDs that happen to sit in the F1xx band (flagged
where they appear).

Research date: 2026-10-06. Grades: **A** = OEM service info · **B** =
multi-source community agreement or verified real-car capture · **C** =
single community source. Suffix notes (e.g. "[B] description; [C] size
(inference — flagged)") mark per-field confidence splits.

Conventions used in this file:
- Request: `22 HH LL` on the listed request CAN ID; response `62 HH LL …`
  on the response ID (+8 offset, standard Toyota).
- `bix`/`len` = bit offset / bit length into the response payload AFTER the
  3-byte `62 HH LL` header (OBDb convention). Values are big-endian unsigned
  unless marked signed.
- Temperatures are offset-binary (`raw + add`, typically −40).
- Session/Security: no source documents a required diagnostic session or
  security access for any read below; fields say "not documented" per the
  no-guessing rule. All reads below were observed or defined without 0x27.
- `Make: toyota` covers Toyota and Lexus (no Lexus-specific DID namespace
  was found; one community map explicitly brands its table "Toyota / Lexus"
  with no separate Lexus overlay).

Primary source: OBDb community signalsets (CC BY-SA 4.0) —
`OBDb/Toyota-Prius` signalsets/v3/default.json @ e33a86b (2016+ Prius, incl.
Gen 4 XW50 and Gen 5), cross-checked against `OBDb/Toyota-RAV4-Hybrid` @
6d2bf00 (head-verified identical engine DIDs through 0x1084) and
`cxalem/scainner` RESEARCH.md/CORPUS.md (independently documents Toyota DID
bands 1000–10FF / 1800–1FFF and addresses 7D2/7DA, 747/74F). Real-car capture
evidence: OBDb `tests/test_cases/` YAMLs with raw request/response bytes.

Addressing note: modern (TNGA-era, ~2016+) Toyota hybrids serve hybrid data
on **0x7D2/0x7DA** (hybrid vehicle control ECU) and **0x747/0x74F** (HV
battery ECU). The **0x7E2/0x7EA + 0x7E3/0x7EB** addresses are the legacy
(KWP2000-era, e.g. Gen 2 Prius) hybrid addresses; no verified 0x22 DIDs were
found on them — Gen 2 community data there is service 0x21, not 0x22 (see
Coverage notes). Engine enhanced diagnostics use **0x700/0x708**; the
standard OBD address **0x7E0/0x7E8** also answers 0x22 (one forum example).

---

## 0x0103 — ECU 0x700/0x708 (engine)
- Name: Odometer
- Description: Engine ECM enhanced-diag address. Odometer, 24-bit unsigned at bit offset 8, kilometers.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius (PRIUS_ENG_ODO) + Toyota-RAV4-Hybrid (RAV4HYBRID_ENG_ODO) signalsets agree

## 0x1002 — ECU 0x700/0x708 (engine)
- Name: BatteryVoltage12V
- Description: 12V auxiliary battery voltage, 16-bit unsigned, ×12.207/10000 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius (PRIUS_12V_V_700) + Toyota-RAV4-Hybrid agreement

## 0x1017 — ECU 0x700/0x708 (engine)
- Name: InjectionVolume
- Description: Injection volume, 16-bit unsigned /3200, liters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1018 — ECU 0x700/0x708 (engine)
- Name: InjectorPortPulse
- Description: Injector port pulse width, 16-bit unsigned /1000, milliseconds.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1019 — ECU 0x700/0x708 (engine)
- Name: InjectionMode
- Description: Injection mode enum, 8-bit: 1 = Direct, 2 = Both (port+direct).
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x102A — ECU 0x700/0x708 (engine)
- Name: AfRatioLearnedBank1
- Description: A/F ratio learned values bank 1: idle, low, mid1, mid2, high — five 8-bit fields at bit offsets 0/8/16/24/32, ×100/255 −50 percent.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1041 — ECU 0x700/0x708 (engine)
- Name: EngineCoolantTempIgnInit
- Description: Engine coolant temperature at ignition and initial, two 8-bit fields, ×0.625 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1043 — ECU 0x700/0x708 (engine)
- Name: ElectricWaterPumpSpeed
- Description: Electric water pump target speed and actual RPM, two 8-bit fields, ×25 rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1046 — ECU 0x700/0x708 (engine)
- Name: CoolingFanDutyRatio
- Description: Cooling fan duty ratio, 8-bit, ×127.5/255 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1059 — ECU 0x700/0x708 (engine)
- Name: AcceleratorPedalPosition
- Description: Accelerator pedal position, 8-bit, /1.42 −28.873 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x105C — ECU 0x700/0x708 (engine)
- Name: KnockCorrectionFeedback
- Description: Knock correction learned value + knock feedback value, two 16-bit fields, ×312.5/10000 −1024.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x105E — ECU 0x700/0x708 (engine)
- Name: EcuInternalTemperature
- Description: ECU internal temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source (Gen 5)

## 0x1062 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtOcvDuty
- Description: Exhaust VVT oil control valve control duty, 16-bit, ×400/65535 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source

## 0x106A — ECU 0x700/0x708 (engine)
- Name: FuelPumpDutyRatio
- Description: Fuel pump duty ratio, 16-bit, ×0.0609756098 (source labels unit kilopascal — likely duty %; flagged).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B] description; [C] unit (source labels kilopascal on a duty-ratio signal — flagged)
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x106C — ECU 0x700/0x708 (engine)
- Name: DistanceSinceBatteryDisconnect
- Description: Distance since last 12V battery cable disconnection, 16-bit unsigned, kilometers.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x106F — ECU 0x700/0x708 (engine)
- Name: IntakeVvtTargetAngleB1
- Description: Intake VVT target angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x1071 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtTargetAngleB1
- Description: Exhaust VVT target angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source

## 0x1074 — ECU 0x700/0x708 (engine)
- Name: EngineOilPressure
- Description: Engine oil pressure, 16-bit, ×10/128 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source. (scainner lists 1074 as unbound — this source binds it to 700/708; conflict flagged, OBDb preferred as primary.)

## 0x1075 — ECU 0x700/0x708 (engine)
- Name: IntercoolerWaterPumpSpeed
- Description: Intercooler water pump speed, 16-bit raw count.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true entry)

## 0x1078 — ECU 0x700/0x708 (engine)
- Name: IdleSparkAdvanceCyl1234
- Description: Idle spark advance control cylinders 1–4, four 8-bit fields, ×6.25/100 degrees.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

## 0x107B — ECU 0x700/0x708 (engine)
- Name: EngineOilTemperature
- Description: Engine oil temperature, 8-bit at bit offset 192, −40 °C offset.
- Make: toyota
- Size: 25 bytes
- Session: not documented
- Security: not documented
- Grade: [B] description; [C] size (inference from bit offset — flagged)
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree (dbg:true)

## 0x1084 — ECU 0x700/0x708 (engine)
- Name: RoughIdleCyl1234
- Description: Rough idle cylinders 1–4, four 8-bit raw fields.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree (dbg:true)

## 0x1087 — ECU 0x700/0x708 (engine)
- Name: IntakeVvtChangeAngleB1
- Description: Intake VVT change angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1088 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtChangeAngleB1
- Description: Exhaust VVT change angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1089 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtHoldLearnB1
- Description: Exhaust VVT hold learn value bank 1, 16-bit, ×399.9/65535 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x108A — ECU 0x700/0x708 (engine)
- Name: VvtIeDutyAndDirection
- Description: VVT-ie duty ratio bank 1 (15-bit, ×399.9/65535 −200 percent) plus 1-bit motor-direction-forward flag at bit 15.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x108D — ECU 0x700/0x708 (engine)
- Name: IntakeVvtOverRetardLearnB1
- Description: Intake VVT most over-retarded learn value bank 1, 16-bit, ×639.99/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x108F — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtOverAdvanceLearnB1
- Description: Exhaust VVT timing most over-advanced learn value bank 1, 16-bit, ×639.99/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x109A — ECU 0x700/0x708 (engine)
- Name: FuelFilterTemperature
- Description: Fuel filter temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x10A2 — ECU 0x700/0x708 (engine)
- Name: AfRatioLearnPortB1
- Description: A/F ratio learn values (port injection) bank 1: idle, low, mid1, mid2, high — five 8-bit fields, ×100/255 −50 percent.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x10A5 — ECU 0x700/0x708 (engine)
- Name: MisfireCountAllCyl
- Description: Misfire counter, all cylinders, 8-bit.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x10A7 — ECU 0x700/0x708 (engine)
- Name: MisfireCountCyl1234
- Description: Misfire counters cylinders 1–4, four 8-bit fields.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x10AA — ECU 0x700/0x708 (engine)
- Name: MisfireLoadRpmMargin
- Description: Misfire load (8-bit ×510/255 %), misfire RPM (8-bit at bit 24, ×6375/255 rpm), misfire margin (8-bit at bit 32, −128 rpm offset).
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x10CD — ECU 0x700/0x708 (engine)
- Name: LowFuelPressureSensor
- Description: Low fuel pressure sensor, 16-bit, /10 −3276.8 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car test capture tests/test_cases/2024/commands/700.708.2210CD.yaml (2023+ filter in source)

## 0x1105 — ECU 0x700/0x708 (engine)
- Name: PmAccumulationRatioB1
- Description: Particulate matter accumulation ratio bank 1, 8-bit, ×2 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x112B — ECU 0x700/0x708 (engine)
- Name: InjectionFeedback1234
- Description: Injection feedback values 1–4, four 8-bit fields, ×5/32 −20 (unit not documented in source).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x112C — ECU 0x700/0x708 (engine)
- Name: InjectionVolumeTarget
- Description: Injection volume target, 16-bit, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x112F — ECU 0x700/0x708 (engine)
- Name: InjectionVolumeTotal
- Description: Injection volume total, 16-bit, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1131 — ECU 0x700/0x708 (engine)
- Name: CylInjectionVolume1234
- Description: Cylinder 1–4 injection volumes, four 16-bit fields, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 8 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x113C — ECU 0x700/0x708 (engine)
- Name: FuelPressure1234
- Description: Fuel pressure 1–4, four 16-bit fields, ×10 kilopascal.
- Make: toyota
- Size: 8 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x113E — ECU 0x700/0x708 (engine)
- Name: FuelTemperature1234
- Description: Fuel temperature 1–4, four 8-bit fields, −40 °C offset.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1141 — ECU 0x700/0x708 (engine)
- Name: FuelReturnTemperature
- Description: Fuel return temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x118B — ECU 0x700/0x708 (engine)
- Name: InjectionVolume1256
- Description: Injection volumes 1, 2, 3, 5, 6, five 16-bit fields, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x119C — ECU 0x700/0x708 (engine)
- Name: IntercoolerCoolantTemperature
- Description: Intercooler coolant temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x11AF — ECU 0x700/0x708 (engine)
- Name: Turbocharger2OutletPressure
- Description: 2nd turbocharger outlet pressure, 16-bit, /100 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x11B8 — ECU 0x700/0x708 (engine)
- Name: InjectionFeedback123456
- Description: Injection feedback values 1–6, six 8-bit fields, ×332/2125 −19.998 (unit not documented in source).
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x11C4 — ECU 0x700/0x708 (engine)
- Name: FuelPressure123456
- Description: Fuel pressure 1–6, six 16-bit fields, ×10 kilopascal.
- Make: toyota
- Size: 12 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x11C5 — ECU 0x700/0x708 (engine)
- Name: FuelTemperature123456
- Description: Fuel temperature 1–6, six 8-bit fields, −40 °C offset.
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x11CD — ECU 0x700/0x708 (engine)
- Name: TurbochargerOutletPressureControl
- Description: 1st and 2nd turbocharger outlet pressure control valves, two 16-bit fields, /100 kilopascal.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15E5 — ECU 0x700/0x708 (engine)
- Name: AuxBatteryFullChargeStatus
- Description: Battery status of full charge, 8-bit, ×255/2 ampere-hours.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15E7 — ECU 0x700/0x708 (engine)
- Name: DarkCurrentBattery
- Description: Dark current of (aux) battery, 16-bit, milliamps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15E8 — ECU 0x700/0x708 (engine)
- Name: AuxBatteryIntegratedCurrent
- Description: Charging integrated current (32-bit /10 Ah), discharging integrated current (32-bit at bit 32, /10 Ah), aux battery capacity after IG ON (8-bit at bit 64, −128 Ah), after IG OFF (8-bit at bit 72, −128 Ah), integrated engine run time (16-bit at bit 80, hours).
- Make: toyota
- Size: 12 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15EE — ECU 0x700/0x708 (engine)
- Name: BatterySensorVoltage
- Description: Voltage of battery sensor, 16-bit, ×13333/10922500 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15F0 — ECU 0x700/0x708 (engine)
- Name: BatterySensorSleepTime
- Description: Sleep time of battery sensor, 8-bit, hours.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15F6 — ECU 0x700/0x708 (engine)
- Name: InitialEngineBatteryVoltageLo
- Description: Initial engine battery voltage lower limit, 8-bit at bit offset 16, /10 volts.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15F7 — ECU 0x700/0x708 (engine)
- Name: BatteryCurrent
- Description: Battery current, 16-bit, ×49/12850 −125 amps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15F8 — ECU 0x700/0x708 (engine)
- Name: BatteryTemperature
- Description: Battery temperature, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x15FA — ECU 0x700/0x708 (engine)
- Name: AlternatorDutyCycle
- Description: Alternator output duty cycle, 16-bit, /164 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1620 — ECU 0x700/0x708 (engine)
- Name: LockUpState
- Description: Torque converter lock-up state, single bit at bit 7, off/on.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1621 — ECU 0x700/0x708 (engine)
- Name: Gear
- Description: Current gear, 8-bit raw.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1622 — ECU 0x700/0x708 (engine)
- Name: TransShiftStateRatio
- Description: Transmission shift state ratio, 16-bit, ×5333/21845000.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1627 — ECU 0x700/0x708 (engine)
- Name: TransFluidTempPanV3
- Description: Transmission fluid pan temperature (variant 3), 16-bit, /256 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1628 — ECU 0x700/0x708 (engine)
- Name: TransFluidTempPostConvV3
- Description: Transmission fluid post-converter temperature (variant 3), 16-bit, /256 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1638 — ECU 0x700/0x708 (engine)
- Name: TransFluidTemperature
- Description: Transmission fluid temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1F2F — ECU 0x700/0x708 (engine)
- Name: FuelLevel
- Description: Fuel level, 8-bit, ×100/255 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F3C — ECU 0x700/0x708 (engine)
- Name: CatalystTempB1S1
- Description: Catalyst temperature bank 1 sensor 1, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F3D — ECU 0x700/0x708 (engine)
- Name: CatalystTempB2S1
- Description: Catalyst temperature bank 2 sensor 1, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1F3E — ECU 0x700/0x708 (engine)
- Name: CatalystTempB1S2
- Description: Catalyst temperature bank 1 sensor 2, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F3F — ECU 0x700/0x708 (engine)
- Name: CatalystTempB2S2
- Description: Catalyst temperature bank 2 sensor 2, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1F46 — ECU 0x700/0x708 (engine)
- Name: AmbientTemperature
- Description: Ambient temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F5C — ECU 0x700/0x708 (engine)
- Name: EngineOilTempV2
- Description: Engine oil temperature variation 2, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2023+ filter in source

## 0x1F6D — ECU 0x700/0x708 (engine)
- Name: FuelPressureHighLow
- Description: High fuel pressure target (16-bit at bit 8), high fuel pressure actual (16-bit at bit 24), low fuel pressure (16-bit at bit 64); all ×10 kilopascal.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F77 — ECU 0x700/0x708 (engine)
- Name: IntakeAirTempB1S1S2
- Description: Intake air temperature bank 1 sensor 1 (8-bit at bit 8) and sensor 2 (8-bit at bit 16), −40 °C offset.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1FF8 — ECU 0x700/0x708 (engine)
- Name: BatteryTemperatureF
- Description: Battery temperature, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x2820 — ECU 0x700/0x708 (engine)
- Name: IntercoolerWaterPump
- Description: Intercooler water pump, 16-bit, ×80/13107 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x2827 — ECU 0x700/0x708 (engine)
- Name: ElectricWaterPump
- Description: Electric water pump, 8-bit, ×40 rpm.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x2829 — ECU 0x700/0x708 (engine)
- Name: ElectricThermostatDuty
- Description: Electric thermostat duty ratio, 8-bit raw percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x282C — ECU 0x700/0x708 (engine)
- Name: CoolantValve1Closed
- Description: Coolant water route switching valve 1 closed flag, single bit at bit 15, no/yes.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x2843 — ECU 0x700/0x708 (engine)
- Name: VvtIeOpeningAngleB1
- Description: Variable valve timing (electric) opening angle bank 1, 8-bit raw percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x2847 — ECU 0x700/0x708 (engine)
- Name: CoolantValve2Closed
- Description: Coolant water route switching valve 2 closed flag, single bit at bit 15, no/yes.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x2848 — ECU 0x700/0x708 (engine)
- Name: EngineOilPressureControlValve
- Description: Engine oil pressure control valve, 16-bit, ×762.93/10000 milliamps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2023+ filter in source

## 0xF19D — ECU 0x700/0x708 (engine)
- Name: FuelRateEngineVehicle
- Description: Toyota-specific live data in the F1xx band (NOT an ISO identification DID): engine fuel rate + vehicle fuel rate, two 16-bit fields, /50 grams/second.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x0103 — ECU 0x701/0x709 (transmission)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers. (Same DID as engine 0x700 variant; 0x701/0x709 is the transmission-side address.)
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1614 — ECU 0x701/0x709 (transmission)
- Name: Nc1Speed
- Description: NC1 speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1616 — ECU 0x701/0x709 (transmission)
- Name: SecondarySpeed
- Description: Secondary speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1618 — ECU 0x701/0x709 (transmission)
- Name: NoSpeed
- Description: NO speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x161A — ECU 0x701/0x709 (transmission)
- Name: NtSpeed
- Description: NT speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1620 — ECU 0x701/0x709 (transmission)
- Name: LockUpState
- Description: Lock-up state, single bit at bit 7, off/on.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1622 — ECU 0x701/0x709 (transmission)
- Name: TransShiftStateRatio
- Description: Transmission shift state ratio, 16-bit, ×5333/21845000.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1627 — ECU 0x701/0x709 (transmission)
- Name: TransFluidTempPan
- Description: Transmission fluid pan temperature, 16-bit, ×0.00703125 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1628 — ECU 0x701/0x709 (transmission)
- Name: TransFluidTempPostConv
- Description: Transmission fluid post-converter temperature, 16-bit, ×0.00703125 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x162B — ECU 0x701/0x709 (transmission)
- Name: AtfThermalDegradationEst
- Description: Automatic transmission fluid thermal degradation estimate, 16-bit raw.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1634 — ECU 0x701/0x709 (transmission)
- Name: SynchronizeStrokePosition
- Description: Synchronize stroke sensor position, 16-bit, ×256/65535 millimeters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x0103 — ECU 0x747/0x74F (HV battery ECU)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers (battery-ECU copy).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x106E — ECU 0x747/0x74F (HV battery ECU)
- Name: AcPowerConsumption
- Description: Air conditioning power consumption, 8-bit, /2000 −12500 kilowatts (formula as documented in source; magnitude looks suspect — flagged).
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C] description; [C] formula (source formula yields implausible range — flagged, compare 7D2 0x106E variant)
- Evidence: OBDb Toyota-Prius signalset only

## 0x1802 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryFan1
- Description: Hybrid battery 1 fan, 8-bit at bit offset 16, /2 percent.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x180B — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryIntakeAirTemp12
- Description: Hybrid battery intake air temperature 1 and 2, two 16-bit fields, ×458/65535 −58 °F.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1814 — ECU 0x747/0x74F (HV battery ECU)
- Name: BatteryTemperature01to16
- Description: Battery temperatures 01–16, sixteen 16-bit fields, ×19531/5000000 −50 °C.
- Make: toyota
- Size: 32 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + scainner brand-research-brief independently notes "max HV cell temperature" among Toyota's notable decodes

## 0x1819 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryBlockVoltage1to5
- Description: Hybrid battery block 1–5 average voltages, five 16-bit fields, ×5/65536 volts.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1824 — ECU 0x747/0x74F (HV battery ECU)
- Name: BatteryHeaterTemperature
- Description: Battery heater temperature, 8-bit, −50 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1825 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryHeaterTemp2
- Description: Hybrid battery heater temperature 2, 8-bit, ×9/5 −58 °F.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x182E — ECU 0x747/0x74F (HV battery ECU)
- Name: HvBatteryCellVoltage01to96
- Description: HV battery cell #01–#96 voltages, ninety-six 16-bit fields, ×5/65535 volts.
- Make: toyota
- Size: 192 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1F5B — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatterySoc
- Description: Hybrid battery state of charge, 8-bit, ×20/51 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.7DA.221F5B*.yaml) + scainner notes "HV battery SOC" as a notable Toyota decode. CONFLICT: captures at pinned commit address it to 7D2/7DA; OBDb HEAD signalset places it on 747/74F — module attribution changed between commits, flagged.

## 0x1F9A — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryCurrent
- Description: Hybrid battery current, 16-bit at bit offset 32, /10 amps.
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.7DA.221F9A.yaml). CONFLICT: same 7D2/7DA-vs-747/74F module-attribution change as 0x1F5B, flagged.

## 0xF19A — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryVoltage
- Description: Toyota-specific live data in the F1xx band (NOT an ISO identification DID): hybrid battery voltage, 8-bit at bit offset 16, ×4 volts.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + scainner brand-research-brief independently notes "HV battery … pack voltage" among Toyota's notable decodes (dbg:true)

## 0x1004 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TireTemperatureV2
- Description: Tire temperatures FL/FR/RL/RR/spare (variant 2), five 8-bit fields, −40 °C offset. TPMS uses extended addressing (eax 0x2A); 2023+ model years.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true). (TPMS service-0x21 local IDs 0x15/0x16/0x30 are KWP2000, excluded from this 0x22 catalog.)

## 0x1005 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TirePressureV2
- Description: Tire pressures FL/FR/RL/RR/spare (variant 2), five 8-bit fields at bit offsets 8/24/40/56/72, /58 −0.5 bar. 2023+ model years.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x2021 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TirePositionIds
- Description: Tire 1–4 position IDs, four 8-bit enum fields: 1=FL, 2=FR, 3=RL, 4=RR.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

## 0x1006 — ECU 0x7B0/0x7B8 (ABS/brake actuator)
- Name: MasterCylinderSensorTemp
- Description: Master cylinder sensor temperature, 8-bit, −80 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1004 — ECU 0x7B3/0x7BB (steering)
- Name: SteeringAngle
- Description: Steering angle, 16-bit SIGNED big-endian, ×1.5 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x1021 — ECU 0x7C0/0x7C8 (combination meter)
- Name: BPlusBatteryVoltage
- Description: B+ battery voltage, 8-bit, /10 volts.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only. (scainner lists 1021 as unbound for Toyota — this source binds it to 7C0/7C8; conflict flagged, OBDb preferred as primary.)

## 0x1022 — ECU 0x7C0/0x7C8 (combination meter)
- Name: FuelRemaining
- Description: Fuel remaining, 16-bit, /100 liters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

## 0x0102 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: KeyCycle
- Description: Key cycle counter, 16-bit raw.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x0103 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers (hybrid-ECU copy).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x1002 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: AuxBatteryVoltage
- Description: Aux (12V) battery voltage, 16-bit, ×61/50000 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x1039 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: FrontRearMotorTorqueRatio
- Description: Front/rear motor torque ratio, 16-bit at bit offset 16, /1000 −32.768.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x1040 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: TransaxleOilTemperature
- Description: Transaxle oil temperature, 8-bit at bit offset 16, −40 °C offset.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x1069 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: MotorRegenBrakeTorque
- Description: Motor regenerative brake torque requested + actual, two 16-bit fields, /8 −4096 kilowatts.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x106A — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: RearMotorRegenBrakeTorque
- Description: Rear motor regenerative brake torque requested + actual (AWD), two 16-bit fields, /8 −4096 kilowatts.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x106C — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: HvBatteryChargeMaxMin
- Description: HV battery charge maximum (8-bit at bit 8) and minimum (8-bit at bit 16), /2 percent.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.22106C*.yaml); 2016+ filter in source

## 0x106E — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: AcPowerConsumption
- Description: Air conditioning power consumption, 8-bit, /20 kilowatts.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source (compare the 747/74F 0x106E variant, whose formula is flagged)

## 0x1075 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: FrontWheelSpeedFRFL
- Description: Front right and front left wheel speeds, two 16-bit fields, /100 −327.68 km/h.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

## 0x10A1 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: MotorRpmTorque
- Description: Motor RPM (signed) + motor torque (signed); exact bit layout not in the signalset — answered in real-car captures with expected decoded values. Payload ~9–10 bytes after the 62 10 A1 header (multi-frame ISO-TP).
- Make: toyota
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] response bytes; [C] content (inference — flagged)
- Evidence: Real-car captures OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2024,2025}/commands/7D2.7DA.2210A1.yaml — e.g. request `22 10 A1` on 0x7D2 answered on 0x7DA with `10 0C 62 10 A1 7E 49 7F …` (12-byte ISO-TP transfer), decoded by the test harness as PRIUS_RPM/PRIUS_TQ. NOT present in the signalset's decoded signal list — content decode is harness-side, flagged.

## 0x2006 — ECU 0x7E0/0x7E8 (engine, standard OBD address)
- Name: not documented
- Description: Unknown function. Known-good read: request `07E0 03 22 20 06` answered `07E8 05 62 20 06 04 B0 …` (5-byte single frame; bytes after 62 20 06 not fully recorded).
- Make: toyota
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: Community UDS example quoted in prior project research (ih8mud/nefariousmotorsports): "I query an ECU with 07E0 03 22 20 06, answer 07E8 05 62 20 06 04 B0". Establishes 0x22 works on the standard 7E0/7E8 engine address; DID meaning unknown.

---

## Coverage notes

DID ranges / areas that could NOT be verified:
- **0x7E2/0x7EA (HV ECU) and 0x7E3/0x7EB (HV battery ECU): no verified 0x22 DIDs found.** These are the legacy KWP2000-era hybrid diagnostic addresses (Gen 2 Prius XW20). The extensive Gen 2 community PID documentation (PriusChat CAN-code tables, Torque Pro custom PIDs, Dr. Prius / Hybrid Assistant, hakanrolsson/priusgen2batterymonitor) uses KWP2000 **service 0x21** readDataByLocalIdentifier there (e.g. `21 CE` block voltages — often mislabeled "UDS mode 0x22" in project READMEs; it is 0x21). Do not confuse 0x21 local IDs with 0x22 DIDs.
- **0x1800–0x1FFF band on 0x747**: only 1802/180B/1814/1819/1824/1825/182E verified; the rest of the band is unmapped in every source checked.
- **0x1000–0x10FF band**: well covered on 0x700 and 0x7D2, sparse elsewhere (1004/1006/1021/1022 on 7B0/7B3/7C0/750 only).
- **0x716/0x724**: listed as a Toyota module pair in scainner's response-offset research but no DIDs documented for it — module identity unknown.
- **0x1F05**: scainner lists it as a known Toyota DID with unknown module binding; it does not appear in the OBDb Prius signalset. Unplaced.
- **5th-gen THS AWD (2023+)**: scainner's changelog notes "2 new DIDs for 5th-gen THS AWD" added 2026-08-23; which two could not be determined from available sources (candidates in OBDb with 2023+ filters: 0x105E, 0x1062, 0x1071, 0x1074, 0x10CD, 0x1F5C, 0x2848 on 0x700; 0x1004/0x1005 TPMS v2 on 0x750).
- **Lexus-specific deviations**: none found. No Lexus-only DID namespace surfaced; Lexus is assumed to share the Toyota DID catalog (one community map brands its table "Toyota / Lexus" with no separate Lexus overlay).
- **Non-hybrid Toyota models** (Corolla/Camry ICE, Tacoma/Tundra, etc.): no dedicated OBDb signalsets were found populated for them; the Prius/RAV4-Hybrid engine DIDs (0x700 band) are the best available proxy and the two models agree, but ICE-truck/SUV coverage is a gap.
- **OBDb Toyota-Prius-Prime and Toyota-RAV4 (non-hybrid) signalsets** exist but were not harvested in this pass — likely overlap, possible Prime-specific additions.
- **KWP2000 0x21 local IDs** (750/7B0/7C0/7C4/7D0/780 body/ABS/cluster data, TPMS 0x15/0x16/0x30) are deliberately excluded: this file is 0x22 only.
- **Session/security**: no source documents required sessions or 0x27 gating for any read above; several sources describe Toyota reads as usable without authentication, but absence of a documented requirement is not proof none exists on all models/years.
- **Module-attribution conflict**: 0x1F5B/0x1F9A (SOC/current) were captured on 0x7D2/0x7DA at OBDb/Toyota-Prius@0a8c4ec and moved to 0x747/0x74F in HEAD (e33a86b); 0x106C stayed on 0x7D2. Treat the 747 vs 7D2 attribution for 1F5B/1F9A as generation-dependent until re-verified on a vehicle.
- **700/708 vs 7E0/7E8**: OBDb engine commands all use 0x700/0x708 (Toyota's enhanced-diagnostics ECM address); the standard 0x7E0/0x7E8 address also answers 0x22 (0x2006 example) but no DID catalog was found for it.

### Sources consulted (this pass)
- OBDb/Toyota-Prius signalsets/v3/default.json @ e33a86b (CC BY-SA 4.0) — primary DID/signal source, read in full (2333 lines)
- OBDb/Toyota-RAV4-Hybrid signalsets/v3/default.json @ 6d2bf00 (CC BY-SA 4.0) — engine-DID cross-check (head verified)
- OBDb/Toyota-Prius tests/test_cases/2024,2025/commands/7D2.7DA.2210A1.yaml @ 0a8c4ec — raw real-car capture, 0x10A1
- OBDb/Toyota-Prius tests/test_cases/2024/commands/700.708.2210CD.yaml @ 0a8c4ec — raw real-car capture, 0x10CD
- iml1s/telltale + aa22396584/telltale THIRD_PARTY_NOTICES_POWERTRAIN_BATTERY.md — independent pinning/verification of 0x1F5B/0x1F9A/0x106C captures at 0a8c4ec
- cxalem/scainner packages/uds-map/RESEARCH.md, COVERAGE.md, docs/uds/CORPUS.md, docs/product/brand-research-brief.md — Toyota DID bands, addressing (7D2/7DA, 747/74F), unbound-DID list (1F9A/106C/1F05/1074/1021), "Toyota / Lexus" branding note
- Local opendbc clone (opendbc/car/toyota/) — checked; no 0x22 DID content (fingerprinting only; KWP2000 1A 88 version query noted in values.py)
- Prior project research (work/toyota.md) — 0x7E0/7E2/7E3 addressing, 07E0→07E8 0x22 example, service-0x13 note
