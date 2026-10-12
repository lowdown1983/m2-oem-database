# Import Makes — Manufacturer-Specific UDS Data Identifiers (v1.3 research)

Merged 2026-10-06 from five per-make research files. Research for the M2 OEM
vehicle database v1.3 (platform-level depth; no VIN required).

**Scope:** manufacturer-specific Data Identifiers read via UDS service 0x22
(ReadDataByIdentifier) for Toyota/Lexus, Honda/Acura, VW Group, Hyundai/Kia,
and Nissan/Infiniti. ISO-standard identification DIDs (0xF180–0xF19E) are
covered separately and NOT duplicated here (two Toyota live-data DIDs that
happen to sit in the F1xx band — 0xF19A/0xF19D — are flagged where they
appear). **Nissan is the exception:** CAN-era Nissan uses KWP2000-style
service 0x21 local IDs (0x22 rejected with NRC 0x12); Nissan entries are
documented as local IDs with the 0x10 0xC0 session prerequisite.

**Grades:** **A** = OEM service info · **B** = multi-source community
agreement or verified real-car capture · **C** = single community source.
Suffix notes (e.g. "[B] description; [C] size (inference — flagged)") mark
which field an inference touches. Nothing was invented; unverifiable items
are "not documented" or excluded.

## Per-make summary

| Make | Entries | A | B | C | Headline source |
|---|---|---|---|---|---|
| Toyota / Lexus | 124 | 0 | 28 | 96 | OBDb/Toyota-Prius signalset v3 (CC BY-SA 4.0) + real-car test captures |
| Honda / Acura | 59 | 1 | 27 | 31 | papataku/honda_ehev_analyzer, scainner research, 29-bit captures |
| VW Group | 323 | 0 | 287 | 36 | OVMS vehicle_vweup production code, OBDb ID.4 signalset (232 test files) |
| Hyundai / Kia | 44 | 0 | 18 | 26 | canair captures, EV-platform community sources |
| Nissan / Infiniti | 27 | 0 | 25 | 2 | Leaf TCU community app (0x21 local-ID table), Pathfinder capture project |
| **Total** | **577** | **1** | **395** | **191** | |

## Key cross-make findings

1. **Toyota generational addressing shift:** 0x7E2/0x7EA + 0x7E3/0x7EB are
   legacy KWP2000-era hybrid addresses (Gen 2 Prius, service 0x21) — no
   verified 0x22 DIDs exist there. Modern TNGA-era hybrids use 0x7D2/0x7DA
   (hybrid control ECU) and 0x747/0x74F (HV battery ECU) for 0x22.
2. **Nissan 0x21 vs 0x22 is model-dependent, not universal:** 0x22 rejected
   with NRC 0x12 on the 2018 Pathfinder, but newer modules (ZE1 AIVC TCU)
   use standard UDS 0x10 0x03 + 0x22 with DIDs like 0x4006.
3. **Hyundai DID numbering is ECU-scoped, not global:** 0x0100 exists on
   HVAC, MFC, SCC, and GSA with unrelated content — always pair a DID with
   its request address.
4. **VW MEB BMS framing conflict:** uds-map claims legacy 0x7E5/0x7ED still
   works on MEB; OBDb ID.4 routes through FC00 extended target addressing
   (ta=7B/76/B9). DID numbers and decodes agree; only framing differs.
5. **Honda transport:** 29-bit normal fixed addressing —
   request 0x18DA<target>F1 → response 0x18DAF1<target> (tester 0xF1).

---

---

## Toyota / Lexus

_Source file: `did-toyota.md`._

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

### 0x0103 — ECU 0x700/0x708 (engine)
- Name: Odometer
- Description: Engine ECM enhanced-diag address. Odometer, 24-bit unsigned at bit offset 8, kilometers.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius (PRIUS_ENG_ODO) + Toyota-RAV4-Hybrid (RAV4HYBRID_ENG_ODO) signalsets agree

### 0x1002 — ECU 0x700/0x708 (engine)
- Name: BatteryVoltage12V
- Description: 12V auxiliary battery voltage, 16-bit unsigned, ×12.207/10000 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius (PRIUS_12V_V_700) + Toyota-RAV4-Hybrid agreement

### 0x1017 — ECU 0x700/0x708 (engine)
- Name: InjectionVolume
- Description: Injection volume, 16-bit unsigned /3200, liters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1018 — ECU 0x700/0x708 (engine)
- Name: InjectorPortPulse
- Description: Injector port pulse width, 16-bit unsigned /1000, milliseconds.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1019 — ECU 0x700/0x708 (engine)
- Name: InjectionMode
- Description: Injection mode enum, 8-bit: 1 = Direct, 2 = Both (port+direct).
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x102A — ECU 0x700/0x708 (engine)
- Name: AfRatioLearnedBank1
- Description: A/F ratio learned values bank 1: idle, low, mid1, mid2, high — five 8-bit fields at bit offsets 0/8/16/24/32, ×100/255 −50 percent.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1041 — ECU 0x700/0x708 (engine)
- Name: EngineCoolantTempIgnInit
- Description: Engine coolant temperature at ignition and initial, two 8-bit fields, ×0.625 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1043 — ECU 0x700/0x708 (engine)
- Name: ElectricWaterPumpSpeed
- Description: Electric water pump target speed and actual RPM, two 8-bit fields, ×25 rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1046 — ECU 0x700/0x708 (engine)
- Name: CoolingFanDutyRatio
- Description: Cooling fan duty ratio, 8-bit, ×127.5/255 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1059 — ECU 0x700/0x708 (engine)
- Name: AcceleratorPedalPosition
- Description: Accelerator pedal position, 8-bit, /1.42 −28.873 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x105C — ECU 0x700/0x708 (engine)
- Name: KnockCorrectionFeedback
- Description: Knock correction learned value + knock feedback value, two 16-bit fields, ×312.5/10000 −1024.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x105E — ECU 0x700/0x708 (engine)
- Name: EcuInternalTemperature
- Description: ECU internal temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source (Gen 5)

### 0x1062 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtOcvDuty
- Description: Exhaust VVT oil control valve control duty, 16-bit, ×400/65535 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source

### 0x106A — ECU 0x700/0x708 (engine)
- Name: FuelPumpDutyRatio
- Description: Fuel pump duty ratio, 16-bit, ×0.0609756098 (source labels unit kilopascal — likely duty %; flagged).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B] description; [C] unit (source labels kilopascal on a duty-ratio signal — flagged)
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x106C — ECU 0x700/0x708 (engine)
- Name: DistanceSinceBatteryDisconnect
- Description: Distance since last 12V battery cable disconnection, 16-bit unsigned, kilometers.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x106F — ECU 0x700/0x708 (engine)
- Name: IntakeVvtTargetAngleB1
- Description: Intake VVT target angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x1071 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtTargetAngleB1
- Description: Exhaust VVT target angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source

### 0x1074 — ECU 0x700/0x708 (engine)
- Name: EngineOilPressure
- Description: Engine oil pressure, 16-bit, ×10/128 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree; 2023+ filter in source. (scainner lists 1074 as unbound — this source binds it to 700/708; conflict flagged, OBDb preferred as primary.)

### 0x1075 — ECU 0x700/0x708 (engine)
- Name: IntercoolerWaterPumpSpeed
- Description: Intercooler water pump speed, 16-bit raw count.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true entry)

### 0x1078 — ECU 0x700/0x708 (engine)
- Name: IdleSparkAdvanceCyl1234
- Description: Idle spark advance control cylinders 1–4, four 8-bit fields, ×6.25/100 degrees.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree

### 0x107B — ECU 0x700/0x708 (engine)
- Name: EngineOilTemperature
- Description: Engine oil temperature, 8-bit at bit offset 192, −40 °C offset.
- Make: toyota
- Size: 25 bytes
- Session: not documented
- Security: not documented
- Grade: [B] description; [C] size (inference from bit offset — flagged)
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree (dbg:true)

### 0x1084 — ECU 0x700/0x708 (engine)
- Name: RoughIdleCyl1234
- Description: Rough idle cylinders 1–4, four 8-bit raw fields.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius + Toyota-RAV4-Hybrid signalsets agree (dbg:true)

### 0x1087 — ECU 0x700/0x708 (engine)
- Name: IntakeVvtChangeAngleB1
- Description: Intake VVT change angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1088 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtChangeAngleB1
- Description: Exhaust VVT change angle bank 1, 16-bit, ×639.9/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1089 — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtHoldLearnB1
- Description: Exhaust VVT hold learn value bank 1, 16-bit, ×399.9/65535 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x108A — ECU 0x700/0x708 (engine)
- Name: VvtIeDutyAndDirection
- Description: VVT-ie duty ratio bank 1 (15-bit, ×399.9/65535 −200 percent) plus 1-bit motor-direction-forward flag at bit 15.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x108D — ECU 0x700/0x708 (engine)
- Name: IntakeVvtOverRetardLearnB1
- Description: Intake VVT most over-retarded learn value bank 1, 16-bit, ×639.99/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x108F — ECU 0x700/0x708 (engine)
- Name: ExhaustVvtOverAdvanceLearnB1
- Description: Exhaust VVT timing most over-advanced learn value bank 1, 16-bit, ×639.99/65535 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x109A — ECU 0x700/0x708 (engine)
- Name: FuelFilterTemperature
- Description: Fuel filter temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x10A2 — ECU 0x700/0x708 (engine)
- Name: AfRatioLearnPortB1
- Description: A/F ratio learn values (port injection) bank 1: idle, low, mid1, mid2, high — five 8-bit fields, ×100/255 −50 percent.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x10A5 — ECU 0x700/0x708 (engine)
- Name: MisfireCountAllCyl
- Description: Misfire counter, all cylinders, 8-bit.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x10A7 — ECU 0x700/0x708 (engine)
- Name: MisfireCountCyl1234
- Description: Misfire counters cylinders 1–4, four 8-bit fields.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x10AA — ECU 0x700/0x708 (engine)
- Name: MisfireLoadRpmMargin
- Description: Misfire load (8-bit ×510/255 %), misfire RPM (8-bit at bit 24, ×6375/255 rpm), misfire margin (8-bit at bit 32, −128 rpm offset).
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x10CD — ECU 0x700/0x708 (engine)
- Name: LowFuelPressureSensor
- Description: Low fuel pressure sensor, 16-bit, /10 −3276.8 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car test capture tests/test_cases/2024/commands/700.708.2210CD.yaml (2023+ filter in source)

### 0x1105 — ECU 0x700/0x708 (engine)
- Name: PmAccumulationRatioB1
- Description: Particulate matter accumulation ratio bank 1, 8-bit, ×2 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x112B — ECU 0x700/0x708 (engine)
- Name: InjectionFeedback1234
- Description: Injection feedback values 1–4, four 8-bit fields, ×5/32 −20 (unit not documented in source).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x112C — ECU 0x700/0x708 (engine)
- Name: InjectionVolumeTarget
- Description: Injection volume target, 16-bit, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x112F — ECU 0x700/0x708 (engine)
- Name: InjectionVolumeTotal
- Description: Injection volume total, 16-bit, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1131 — ECU 0x700/0x708 (engine)
- Name: CylInjectionVolume1234
- Description: Cylinder 1–4 injection volumes, four 16-bit fields, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 8 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x113C — ECU 0x700/0x708 (engine)
- Name: FuelPressure1234
- Description: Fuel pressure 1–4, four 16-bit fields, ×10 kilopascal.
- Make: toyota
- Size: 8 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x113E — ECU 0x700/0x708 (engine)
- Name: FuelTemperature1234
- Description: Fuel temperature 1–4, four 8-bit fields, −40 °C offset.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1141 — ECU 0x700/0x708 (engine)
- Name: FuelReturnTemperature
- Description: Fuel return temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x118B — ECU 0x700/0x708 (engine)
- Name: InjectionVolume1256
- Description: Injection volumes 1, 2, 3, 5, 6, five 16-bit fields, ×19531/1000000 −640 (unit not documented in source).
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x119C — ECU 0x700/0x708 (engine)
- Name: IntercoolerCoolantTemperature
- Description: Intercooler coolant temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x11AF — ECU 0x700/0x708 (engine)
- Name: Turbocharger2OutletPressure
- Description: 2nd turbocharger outlet pressure, 16-bit, /100 kilopascal.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x11B8 — ECU 0x700/0x708 (engine)
- Name: InjectionFeedback123456
- Description: Injection feedback values 1–6, six 8-bit fields, ×332/2125 −19.998 (unit not documented in source).
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x11C4 — ECU 0x700/0x708 (engine)
- Name: FuelPressure123456
- Description: Fuel pressure 1–6, six 16-bit fields, ×10 kilopascal.
- Make: toyota
- Size: 12 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x11C5 — ECU 0x700/0x708 (engine)
- Name: FuelTemperature123456
- Description: Fuel temperature 1–6, six 8-bit fields, −40 °C offset.
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x11CD — ECU 0x700/0x708 (engine)
- Name: TurbochargerOutletPressureControl
- Description: 1st and 2nd turbocharger outlet pressure control valves, two 16-bit fields, /100 kilopascal.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15E5 — ECU 0x700/0x708 (engine)
- Name: AuxBatteryFullChargeStatus
- Description: Battery status of full charge, 8-bit, ×255/2 ampere-hours.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15E7 — ECU 0x700/0x708 (engine)
- Name: DarkCurrentBattery
- Description: Dark current of (aux) battery, 16-bit, milliamps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15E8 — ECU 0x700/0x708 (engine)
- Name: AuxBatteryIntegratedCurrent
- Description: Charging integrated current (32-bit /10 Ah), discharging integrated current (32-bit at bit 32, /10 Ah), aux battery capacity after IG ON (8-bit at bit 64, −128 Ah), after IG OFF (8-bit at bit 72, −128 Ah), integrated engine run time (16-bit at bit 80, hours).
- Make: toyota
- Size: 12 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15EE — ECU 0x700/0x708 (engine)
- Name: BatterySensorVoltage
- Description: Voltage of battery sensor, 16-bit, ×13333/10922500 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15F0 — ECU 0x700/0x708 (engine)
- Name: BatterySensorSleepTime
- Description: Sleep time of battery sensor, 8-bit, hours.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15F6 — ECU 0x700/0x708 (engine)
- Name: InitialEngineBatteryVoltageLo
- Description: Initial engine battery voltage lower limit, 8-bit at bit offset 16, /10 volts.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15F7 — ECU 0x700/0x708 (engine)
- Name: BatteryCurrent
- Description: Battery current, 16-bit, ×49/12850 −125 amps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15F8 — ECU 0x700/0x708 (engine)
- Name: BatteryTemperature
- Description: Battery temperature, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x15FA — ECU 0x700/0x708 (engine)
- Name: AlternatorDutyCycle
- Description: Alternator output duty cycle, 16-bit, /164 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1620 — ECU 0x700/0x708 (engine)
- Name: LockUpState
- Description: Torque converter lock-up state, single bit at bit 7, off/on.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1621 — ECU 0x700/0x708 (engine)
- Name: Gear
- Description: Current gear, 8-bit raw.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1622 — ECU 0x700/0x708 (engine)
- Name: TransShiftStateRatio
- Description: Transmission shift state ratio, 16-bit, ×5333/21845000.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1627 — ECU 0x700/0x708 (engine)
- Name: TransFluidTempPanV3
- Description: Transmission fluid pan temperature (variant 3), 16-bit, /256 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1628 — ECU 0x700/0x708 (engine)
- Name: TransFluidTempPostConvV3
- Description: Transmission fluid post-converter temperature (variant 3), 16-bit, /256 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1638 — ECU 0x700/0x708 (engine)
- Name: TransFluidTemperature
- Description: Transmission fluid temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1F2F — ECU 0x700/0x708 (engine)
- Name: FuelLevel
- Description: Fuel level, 8-bit, ×100/255 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F3C — ECU 0x700/0x708 (engine)
- Name: CatalystTempB1S1
- Description: Catalyst temperature bank 1 sensor 1, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F3D — ECU 0x700/0x708 (engine)
- Name: CatalystTempB2S1
- Description: Catalyst temperature bank 2 sensor 1, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1F3E — ECU 0x700/0x708 (engine)
- Name: CatalystTempB1S2
- Description: Catalyst temperature bank 1 sensor 2, 16-bit, /10 −40 °C.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F3F — ECU 0x700/0x708 (engine)
- Name: CatalystTempB2S2
- Description: Catalyst temperature bank 2 sensor 2, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1F46 — ECU 0x700/0x708 (engine)
- Name: AmbientTemperature
- Description: Ambient temperature, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F5C — ECU 0x700/0x708 (engine)
- Name: EngineOilTempV2
- Description: Engine oil temperature variation 2, 8-bit, −40 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2023+ filter in source

### 0x1F6D — ECU 0x700/0x708 (engine)
- Name: FuelPressureHighLow
- Description: High fuel pressure target (16-bit at bit 8), high fuel pressure actual (16-bit at bit 24), low fuel pressure (16-bit at bit 64); all ×10 kilopascal.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F77 — ECU 0x700/0x708 (engine)
- Name: IntakeAirTempB1S1S2
- Description: Intake air temperature bank 1 sensor 1 (8-bit at bit 8) and sensor 2 (8-bit at bit 16), −40 °C offset.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1FF8 — ECU 0x700/0x708 (engine)
- Name: BatteryTemperatureF
- Description: Battery temperature, 16-bit, ×9/50 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x2820 — ECU 0x700/0x708 (engine)
- Name: IntercoolerWaterPump
- Description: Intercooler water pump, 16-bit, ×80/13107 percent.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x2827 — ECU 0x700/0x708 (engine)
- Name: ElectricWaterPump
- Description: Electric water pump, 8-bit, ×40 rpm.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x2829 — ECU 0x700/0x708 (engine)
- Name: ElectricThermostatDuty
- Description: Electric thermostat duty ratio, 8-bit raw percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x282C — ECU 0x700/0x708 (engine)
- Name: CoolantValve1Closed
- Description: Coolant water route switching valve 1 closed flag, single bit at bit 15, no/yes.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x2843 — ECU 0x700/0x708 (engine)
- Name: VvtIeOpeningAngleB1
- Description: Variable valve timing (electric) opening angle bank 1, 8-bit raw percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x2847 — ECU 0x700/0x708 (engine)
- Name: CoolantValve2Closed
- Description: Coolant water route switching valve 2 closed flag, single bit at bit 15, no/yes.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x2848 — ECU 0x700/0x708 (engine)
- Name: EngineOilPressureControlValve
- Description: Engine oil pressure control valve, 16-bit, ×762.93/10000 milliamps.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2023+ filter in source

### 0xF19D — ECU 0x700/0x708 (engine)
- Name: FuelRateEngineVehicle
- Description: Toyota-specific live data in the F1xx band (NOT an ISO identification DID): engine fuel rate + vehicle fuel rate, two 16-bit fields, /50 grams/second.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x0103 — ECU 0x701/0x709 (transmission)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers. (Same DID as engine 0x700 variant; 0x701/0x709 is the transmission-side address.)
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1614 — ECU 0x701/0x709 (transmission)
- Name: Nc1Speed
- Description: NC1 speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1616 — ECU 0x701/0x709 (transmission)
- Name: SecondarySpeed
- Description: Secondary speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1618 — ECU 0x701/0x709 (transmission)
- Name: NoSpeed
- Description: NO speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x161A — ECU 0x701/0x709 (transmission)
- Name: NtSpeed
- Description: NT speed, 16-bit, rpm.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1620 — ECU 0x701/0x709 (transmission)
- Name: LockUpState
- Description: Lock-up state, single bit at bit 7, off/on.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1622 — ECU 0x701/0x709 (transmission)
- Name: TransShiftStateRatio
- Description: Transmission shift state ratio, 16-bit, ×5333/21845000.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1627 — ECU 0x701/0x709 (transmission)
- Name: TransFluidTempPan
- Description: Transmission fluid pan temperature, 16-bit, ×0.00703125 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1628 — ECU 0x701/0x709 (transmission)
- Name: TransFluidTempPostConv
- Description: Transmission fluid post-converter temperature, 16-bit, ×0.00703125 −40 °F.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x162B — ECU 0x701/0x709 (transmission)
- Name: AtfThermalDegradationEst
- Description: Automatic transmission fluid thermal degradation estimate, 16-bit raw.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1634 — ECU 0x701/0x709 (transmission)
- Name: SynchronizeStrokePosition
- Description: Synchronize stroke sensor position, 16-bit, ×256/65535 millimeters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x0103 — ECU 0x747/0x74F (HV battery ECU)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers (battery-ECU copy).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x106E — ECU 0x747/0x74F (HV battery ECU)
- Name: AcPowerConsumption
- Description: Air conditioning power consumption, 8-bit, /2000 −12500 kilowatts (formula as documented in source; magnitude looks suspect — flagged).
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C] description; [C] formula (source formula yields implausible range — flagged, compare 7D2 0x106E variant)
- Evidence: OBDb Toyota-Prius signalset only

### 0x1802 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryFan1
- Description: Hybrid battery 1 fan, 8-bit at bit offset 16, /2 percent.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x180B — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryIntakeAirTemp12
- Description: Hybrid battery intake air temperature 1 and 2, two 16-bit fields, ×458/65535 −58 °F.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1814 — ECU 0x747/0x74F (HV battery ECU)
- Name: BatteryTemperature01to16
- Description: Battery temperatures 01–16, sixteen 16-bit fields, ×19531/5000000 −50 °C.
- Make: toyota
- Size: 32 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + scainner brand-research-brief independently notes "max HV cell temperature" among Toyota's notable decodes

### 0x1819 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryBlockVoltage1to5
- Description: Hybrid battery block 1–5 average voltages, five 16-bit fields, ×5/65536 volts.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1824 — ECU 0x747/0x74F (HV battery ECU)
- Name: BatteryHeaterTemperature
- Description: Battery heater temperature, 8-bit, −50 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1825 — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryHeaterTemp2
- Description: Hybrid battery heater temperature 2, 8-bit, ×9/5 −58 °F.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x182E — ECU 0x747/0x74F (HV battery ECU)
- Name: HvBatteryCellVoltage01to96
- Description: HV battery cell #01–#96 voltages, ninety-six 16-bit fields, ×5/65535 volts.
- Make: toyota
- Size: 192 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1F5B — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatterySoc
- Description: Hybrid battery state of charge, 8-bit, ×20/51 percent.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.7DA.221F5B*.yaml) + scainner notes "HV battery SOC" as a notable Toyota decode. CONFLICT: captures at pinned commit address it to 7D2/7DA; OBDb HEAD signalset places it on 747/74F — module attribution changed between commits, flagged.

### 0x1F9A — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryCurrent
- Description: Hybrid battery current, 16-bit at bit offset 32, /10 amps.
- Make: toyota
- Size: 6 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.7DA.221F9A.yaml). CONFLICT: same 7D2/7DA-vs-747/74F module-attribution change as 0x1F5B, flagged.

### 0xF19A — ECU 0x747/0x74F (HV battery ECU)
- Name: HybridBatteryVoltage
- Description: Toyota-specific live data in the F1xx band (NOT an ISO identification DID): hybrid battery voltage, 8-bit at bit offset 16, ×4 volts.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + scainner brand-research-brief independently notes "HV battery … pack voltage" among Toyota's notable decodes (dbg:true)

### 0x1004 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TireTemperatureV2
- Description: Tire temperatures FL/FR/RL/RR/spare (variant 2), five 8-bit fields, −40 °C offset. TPMS uses extended addressing (eax 0x2A); 2023+ model years.
- Make: toyota
- Size: 5 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true). (TPMS service-0x21 local IDs 0x15/0x16/0x30 are KWP2000, excluded from this 0x22 catalog.)

### 0x1005 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TirePressureV2
- Description: Tire pressures FL/FR/RL/RR/spare (variant 2), five 8-bit fields at bit offsets 8/24/40/56/72, /58 −0.5 bar. 2023+ model years.
- Make: toyota
- Size: 10 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x2021 — ECU 0x750/0x758 eax 0x2A (TPMS)
- Name: TirePositionIds
- Description: Tire 1–4 position IDs, four 8-bit enum fields: 1=FL, 2=FR, 3=RL, 4=RR.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only (dbg:true)

### 0x1006 — ECU 0x7B0/0x7B8 (ABS/brake actuator)
- Name: MasterCylinderSensorTemp
- Description: Master cylinder sensor temperature, 8-bit, −80 °C offset.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1004 — ECU 0x7B3/0x7BB (steering)
- Name: SteeringAngle
- Description: Steering angle, 16-bit SIGNED big-endian, ×1.5 degrees.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x1021 — ECU 0x7C0/0x7C8 (combination meter)
- Name: BPlusBatteryVoltage
- Description: B+ battery voltage, 8-bit, /10 volts.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only. (scainner lists 1021 as unbound for Toyota — this source binds it to 7C0/7C8; conflict flagged, OBDb preferred as primary.)

### 0x1022 — ECU 0x7C0/0x7C8 (combination meter)
- Name: FuelRemaining
- Description: Fuel remaining, 16-bit, /100 liters.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only

### 0x0102 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: KeyCycle
- Description: Key cycle counter, 16-bit raw.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x0103 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: Odometer
- Description: Odometer, 24-bit unsigned at bit offset 8, kilometers (hybrid-ECU copy).
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x1002 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: AuxBatteryVoltage
- Description: Aux (12V) battery voltage, 16-bit, ×61/50000 volts.
- Make: toyota
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x1039 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: FrontRearMotorTorqueRatio
- Description: Front/rear motor torque ratio, 16-bit at bit offset 16, /1000 −32.768.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x1040 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: TransaxleOilTemperature
- Description: Transaxle oil temperature, 8-bit at bit offset 16, −40 °C offset.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x1069 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: MotorRegenBrakeTorque
- Description: Motor regenerative brake torque requested + actual, two 16-bit fields, /8 −4096 kilowatts.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x106A — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: RearMotorRegenBrakeTorque
- Description: Rear motor regenerative brake torque requested + actual (AWD), two 16-bit fields, /8 −4096 kilowatts.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x106C — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: HvBatteryChargeMaxMin
- Description: HV battery charge maximum (8-bit at bit 8) and minimum (8-bit at bit 16), /2 percent.
- Make: toyota
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [B]
- Evidence: OBDb Toyota-Prius signalset + real-car captures (telltale pins OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2022,2024,2025}/commands/7D2.22106C*.yaml); 2016+ filter in source

### 0x106E — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: AcPowerConsumption
- Description: Air conditioning power consumption, 8-bit, /20 kilowatts.
- Make: toyota
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source (compare the 747/74F 0x106E variant, whose formula is flagged)

### 0x1075 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: FrontWheelSpeedFRFL
- Description: Front right and front left wheel speeds, two 16-bit fields, /100 −327.68 km/h.
- Make: toyota
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: OBDb Toyota-Prius signalset only; 2016+ filter in source

### 0x10A1 — ECU 0x7D2/0x7DA (hybrid vehicle control ECU)
- Name: MotorRpmTorque
- Description: Motor RPM (signed) + motor torque (signed); exact bit layout not in the signalset — answered in real-car captures with expected decoded values. Payload ~9–10 bytes after the 62 10 A1 header (multi-frame ISO-TP).
- Make: toyota
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] response bytes; [C] content (inference — flagged)
- Evidence: Real-car captures OBDb/Toyota-Prius@0a8c4ec tests/test_cases/{2024,2025}/commands/7D2.7DA.2210A1.yaml — e.g. request `22 10 A1` on 0x7D2 answered on 0x7DA with `10 0C 62 10 A1 7E 49 7F …` (12-byte ISO-TP transfer), decoded by the test harness as PRIUS_RPM/PRIUS_TQ. NOT present in the signalset's decoded signal list — content decode is harness-side, flagged.

### 0x2006 — ECU 0x7E0/0x7E8 (engine, standard OBD address)
- Name: not documented
- Description: Unknown function. Known-good read: request `07E0 03 22 20 06` answered `07E8 05 62 20 06 04 B0 …` (5-byte single frame; bytes after 62 20 06 not fully recorded).
- Make: toyota
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: Community UDS example quoted in prior project research (ih8mud/nefariousmotorsports): "I query an ECU with 07E0 03 22 20 06, answer 07E8 05 62 20 06 04 B0". Establishes 0x22 works on the standard 7E0/7E8 engine address; DID meaning unknown.

---

### Coverage notes

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

#### Sources consulted (this pass)
- OBDb/Toyota-Prius signalsets/v3/default.json @ e33a86b (CC BY-SA 4.0) — primary DID/signal source, read in full (2333 lines)
- OBDb/Toyota-RAV4-Hybrid signalsets/v3/default.json @ 6d2bf00 (CC BY-SA 4.0) — engine-DID cross-check (head verified)
- OBDb/Toyota-Prius tests/test_cases/2024,2025/commands/7D2.7DA.2210A1.yaml @ 0a8c4ec — raw real-car capture, 0x10A1
- OBDb/Toyota-Prius tests/test_cases/2024/commands/700.708.2210CD.yaml @ 0a8c4ec — raw real-car capture, 0x10CD
- iml1s/telltale + aa22396584/telltale THIRD_PARTY_NOTICES_POWERTRAIN_BATTERY.md — independent pinning/verification of 0x1F5B/0x1F9A/0x106C captures at 0a8c4ec
- cxalem/scainner packages/uds-map/RESEARCH.md, COVERAGE.md, docs/uds/CORPUS.md, docs/product/brand-research-brief.md — Toyota DID bands, addressing (7D2/7DA, 747/74F), unbound-DID list (1F9A/106C/1F05/1074/1021), "Toyota / Lexus" branding note
- Local opendbc clone (opendbc/car/toyota/) — checked; no 0x22 DID content (fingerprinting only; KWP2000 1A 88 version query noted in values.py)
- Prior project research (work/toyota.md) — 0x7E0/7E2/7E3 addressing, 07E0→07E8 0x22 example, service-0x13 note

---

## Honda / Acura

_Source file: `did-honda.md`._

Scope: Honda/Acura-specific DIDs read via UDS ReadDataByIdentifier (0x22).
ISO-standard 0xF180–0xF19E DIDs are intentionally NOT listed here (covered separately).
Target: M2 OEM vehicle database v1.3.

### Transport notes (applies to all entries below)

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

### Battery ECU (e:HEV)

#### DA01 on Civic e:HEV (request 0x18DA01F1 → response 0x18DAF101); BAT on e:PHEV/RP8 (request 0x18DBEFF1 → response 0x18DAF101)

### 0x2028
- Name: HighVoltageBatteryCellVoltages
- Description: Individual HV cell voltages A1..A84. Each field 16-bit unsigned, value/5 = millivolts (e.g. raw 18489 → 3697.8 mV). Recorded fixture on Civic hybrid decodes plausible Li-ion cell voltages (~3.69–3.70 V).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [B] DID existence/purpose/encodings (two independent community projects + recorded multi-frame fixture); [C] absolute byte positions (inference — flagged: OBDb bix base point unconfirmed)
- Evidence: OBDb Honda-Civic signalset (DA01, filter from 2023) + recorded test fixture (tests/test_cases/2023/commands/DA01.01.222028) with decoded cell voltages; RP8 STEP WGN e:HEV Session 15 scan also found DID 0x2028 positive on ECU 01 (papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md)

### 0x202A
- Name: HighVoltageBatteryStatusBlock (SOCE / StateOfCharge)
- Description: HV battery status block: SOC (%), pack total current (A, signed), pack voltage (V), cell max/min SOC (%), cabin/outside ambient temps (°C), pack capacity (Ah). OEM method: send `03 22 20 2A` to 0x18DBEFF1; receive multi-frame from 0x18DAF101; SOCE is "the last figure before 55 55 55 55 55" end marker; SOCE% = raw×100/255 (OEM example: FC → 98.82%).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in both Honda EU bulletin example and OBDb recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [A] name/purpose/SOCE formula (Honda Motor Europe OEM service bulletin); [B] community encodings/size (OBDb Civic + recorded fixture decoding SOC 64%, 268 V, 3.66 A); [C] absolute byte positions (inference — flagged: OEM gives relative position only; OBDb bix base unconfirmed)
- Evidence: Honda Motor Europe techinfo bulletin ePHEVBMS_EN 002 (Aug 2024, e:PHEV 2024- BAT ECU SOCE method); OBDb Honda-Civic DA01 (filter from 2023) with test fixture (tests/test_cases/2023/commands/DA01.01.22202A) decoding SOC/current/voltage; RP8 Session 15 scan positive for 0x202A on ECU 01

### 0x202C
- Name: HighVoltageBatteryModuleTemperatures
- Description: HV battery module temperatures (1A, 3A) plus engine coolant temperature sensors 1–4. Each 16-bit signed, /10 = °C (offset −40 range per OBDb: min −40).
- Make: honda
- Size: 246 bytes (verified — ISO-TP first frame `10 F6` in recorded fixture)
- Session: not documented
- Security: not documented
- Grade: [B] DID existence/purpose/encodings (OBDb Civic + recorded fixture; RP8 Session 15 scan positive on ECU 01); [C] absolute byte positions (inference — flagged)
- Evidence: OBDb Honda-Civic signalset DA01 (filter from 2023) + test fixture (tests/test_cases/2023/commands/DA01.01.22202C); papataku RP8 Session 15 positive-DID list includes 0x202C

### Engine / PCM

#### DA10 / DA11 / DA0E (request 0x18DA<target>F1 → response 0x18DAF1<target>)

### 0x2240
- Name: DistanceTraveledSinceLastCharge
- Description: Distance traveled since last charge, 32-bit unsigned, kilometers. Listed for 2012–2014 Civic (DA0E).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source (OBDb Honda-Civic only; no CR-V entry, no recorded fixture found)
- Evidence: OBDb Honda-Civic signalset (DA0E, filter 2012–2014)

### 0x2610
- Name: GeneratorFieldDutyAndACClutch
- Description: Generator field duty, 8-bit: raw×100/255 = percent; plus A/C clutch 1-bit on/off.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two independent model repos agree (OBDb Honda-Civic DA10 + Honda-CR-V DA10, identical fields/scales)
- Evidence: OBDb Honda-Civic and Honda-CR-V signalsets (DA10)

### 0x2611
- Name: FuelAirCommandedEquivalenceRatio
- Description: Fuel/air commanded equivalence ratio (lambda): 16-bit raw×29.4/65535 = ratio (max 29.4). DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V); [C] byte position (inference — flagged)
- Evidence: OBDb Honda-Civic (DA10, filter from 2015) and Honda-CR-V (DA10, DA11) signalsets

### 0x2612
- Name: VariableValveControl
- Description: Variable valve (VTEC) control, 8-bit scalar (DA10). Same DID on DA0E carries current-gear variants (8-bit scalars).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree on DA10 VTEC usage; [C] DA0E gear-variant usage (Civic only, CR-V marks dbg)
- Evidence: OBDb Honda-Civic + Honda-CR-V (DA10); DA0E gear entries from Honda-Civic (CR-V flags them dbg)

### 0x2613
- Name: ACRefrigerantPressure
- Description: A/C pressure, 16-bit unsigned, kilopascals (max 4000). DA0E.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] both model repos list identical DID/scale; [C] noted: CR-V entry is flagged dbg
- Evidence: OBDb Honda-Civic + Honda-CR-V (DA0E)

### 0x2615
- Name: ActiveCylinders
- Description: Active cylinders, 8-bit (max 6). DA10, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

### 0x2660
- Name: OdometerAndEngineRuntime
- Description: Odometer 24-bit unsigned kilometers + time since engine start 16-bit seconds. DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic filter from 2015 + CR-V, identical fields/scales)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

### 0x2661
- Name: FuelAirCommandedEquivalenceRatioAlt
- Description: Fuel/air commanded equivalence ratio, 16-bit: raw/2229.08163265 = ratio (max 29.4). DA10.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10)

### 0x2662
- Name: KnockControlAndVTCTiming
- Description: Knock control 8-bit (raw×2/255); variable timing control duty 8-bit (raw×100/255 = %); DA11 variant adds catalyst temperature 16-bit (/10 − 40 = °C).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic DA10/DA11 + CR-V DA10/DA11)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets

### 0x2663
- Name: MisfireCountsPerCylinder
- Description: Per-cylinder misfire counts, 16-bit unsigned each (cylinders 1–4 on DA10; DA11 variants carry up to 6 cylinders in multiple layouts).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree on DA10 layout (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA10; DA11 variants differ by generation)

### 0x2666
- Name: EngineOilTemperature
- Description: Engine oil temperature, 8-bit: raw − 40 = °C (range −40..215). DA10/DA11.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets

### 0x266C
- Name: MisfireCountVariant1
- Description: Per-cylinder misfire counts, 8-bit unsigned each (6 cylinders). DA11.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] conflict: flagged dbg in Honda-Civic but non-dbg in Honda-CR-V; treat layout as unconfirmed
- Evidence: OBDb Honda-Civic (DA11, dbg, filter to 2011) + Honda-CR-V (DA11)

### Transmission / TCM

#### DA1D / DA1E (request 0x18DA1DF1 → response 0x18DAF11D for DA1D)

### 0x2201
- Name: AutomaticTransmissionFluidTemperature
- Description: ATF temperature, first DID data byte: °C = byte − 40 (range −40..215). Torque Pro formula from community: `AA*(9/5)-40` (°F) with OBD header `18DA1DF1`; ScanGauge II XGauge: TXD `1DF1222201`, RXF `032400000000`, RXD `2808`, MTH `00090005FFD8` — same byte, same scale.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] multi-source community agreement: odyclub ScanGauge code + Torque Pro config confirmed working on a 2015 Odyssey EX-L + OBDb Civic (DA1D, filter to 2014) + OBDb CR-V (DA1D) — all describe byte 0, −40 offset
- Evidence: odyclub.com "Transmission Temperature with Torque app and ELM327" (posts by Charlie, TomB985, 0dyfamily; Torque settings "got this to work on my 2015 EX-L"); OBDb Honda-Civic + Honda-CR-V (DA1D 0x2201, bix 208 len 8 add −40 °C)

### 0x2203
- Name: OilPressure
- Description: Oil pressure, 8-bit unsigned, kilopascals (max 255). DA1D.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-CR-V signalset (DA1D, dbg)

### 0x2221
- Name: CurrentGear
- Description: Current gear, 8-bit scalar. DA1D.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic filter to 2014 + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1D)

### 0x3083
- Name: TransmissionFluidTemperatureAlt
- Description: Transmission fluid temperature on DA1E, 8-bit: raw − 40 = °C (range −40..200).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1E, dbg)

### 0x3086
- Name: TransmissionGearEnumerated
- Description: Transmission gear on DA1E, 8-bit with enumerated map (values include 0–9, 14, 15; e.g. Park/Drive positions).
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg, enumeration map not verified against a vehicle
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA1E, dbg)

### Brake system

#### DA28 / DA2A

### 0x4004
- Name: BrakeSwitch
- Description: Brake switch, 1-bit on/off. DA28, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA28)

### 0x4005
- Name: BrakePressure
- Description: Brake pressure, 16-bit: raw − 25 = bars (max 120). DA28, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V); [C] offset semantics (add −25) — single-source convention
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA28)

### 0x4201
- Name: BrakePedalAndCylinderStrokes
- Description: Brake pedal stroke 16-bit (/10 = mm, max 50); brake fluid pressure 16-bit (/100, unit unknown); master cylinder stroke 16-bit signed (/10 = mm); slave cylinder stroke 16-bit (/10 = mm). DA2A, filter from 2023.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] DID existence and signal list in both repos; [C] encodings (single-source convention, fluid-pressure unit unknown)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA2A)

### TPMS

#### DA26

### 0x6001
- Name: TirePressuresAndTemperatures
- Description: Four tire pressures, 16-bit each, kilopascals; four tire temperatures, 8-bit signed each, °C. DA26.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source, flagged dbg
- Evidence: OBDb Honda-CR-V signalset (DA26, dbg)

### Instrument cluster / meter

#### DA60

### 0x7022
- Name: OdometerMiles
- Description: Odometer, 24-bit unsigned, miles (max 200000). DA60, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

### 0x7028
- Name: OutsideAirTemperature
- Description: Outside air temperature, 12-bit signed: raw = °F (range −40..2047; 141 = null/invalid). DA60, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

### 0x7029
- Name: FuelLevel
- Description: Fuel level, 16-bit: raw/100 = liters (max 655). DA60, filter from 2015.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [B] two model repos agree (Civic + CR-V)
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

### 0x7060
- Name: MaintenanceMinderItems
- Description: Maintenance minder distances/items (oil & filter, spark plugs & valves, general inspection, tire rotation, cabin filter, transmission fluid, engine coolant, brake fluid, air cleaner), 16-bit each, unit unknown. DA60, filter from 2016.
- Make: honda
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] two repos list it but units are unknown and Civic/CR-V disagree on dbg status
- Evidence: OBDb Honda-Civic + Honda-CR-V signalsets (DA60)

### Honda e:WN7 electric motorcycle (2026, EU)

Reverse-engineered via MeatPi WiCAN on the diagnostic connector. Field positions
verified against a passive bus capture of Honda's own official MCS diagnostic
tool plus its 18-page all-systems report. 29-bit: request `0x18DA<ECU>F1` →
response `0x18DAF1<ECU>`. Honda's tool uses plain service 0x22 in the DEFAULT
session (`10 01`) with periodic TesterPresent (`3E`) and NO `27` SecurityAccess
— none of the data below is access-locked (verified capture).

### 0xA870
- Name: BatteryStatusBlock
- Description: 56-byte battery status block (BMU, target 0xD4). Verified positions: in-fact SOC u16×0.01 % (payload p41:42); displayed SOC u16×0.01 % (p43:44); SOC control u16×0.01 % (p45:46); remaining-energy field u16 (p47:48); pack voltage u16×0.1 V (p12:13, ~392 V nominal); pack current s16×0.1 A (p14:15, negative = charging); cell temp max u8−40 °C (p37); cell temp min u8−40 °C (p38); SOH u8 % (p49, 100 on new pack); SOCP/SOCE u8 (p50/p51).
- Make: honda
- Size: 56 bytes (verified)
- Session: default session (verified — Honda MCS tool capture used 10 01 + periodic 3E)
- Security: none required (verified — no 27 SecurityAccess in captured tool session)
- Grade: [B] verified capture: positions matched against Honda's official MCS diagnostic tool passive capture and its 18-page all-systems report; single vehicle (2026 WN7 EU)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md ("Verified positions (matched against the official diagnostic report)")

### 0xF012
- Name: Odometer
- Description: Odometer, 32-bit: raw×0.1 = km. Response `62 F0 12 <u32>`; matches the TFT display exactly. (Meter, target 0xDE.)
- Make: honda
- Size: 4 bytes (verified — response `62 F0 12 <u32>`)
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (matches display exactly; official-report matched)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xCFA1
- Name: ChargePortTemperature
- Description: Charge-port temperature, u8: raw − 40 = °C (payload p18). (Meter, target 0xDE.)
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (matched against official diagnostic report)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xCFA2
- Name: DisplayAggregateBlock
- Description: Cluster's display block (meter, target 0xDE): displayed SOC u8 % at p30 (integer, exactly the TFT number); ambient temp u8 °C at p18; cell voltage max u16/5 = mV at p31:32; cell voltage min u16/5 = mV at p33:34; pack voltage copy u16 at p24:25; plug-state mirror u8 at p16 (4→0 when cable in).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (TFT-calibrated over weeks; report-matched)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xDB00
- Name: ChargeConnectBlock
- Description: 56-byte charge-connect block (PCU/DCDC, target 0xCB). Decoded via plug-in before/after snapshots: cable flag u8 at p9 (1 = no cable, 3 = cable plugged in, stays 3 while charging); charge-active flag u8 at p8 (1 = not charging, 2 = charging — verified during a real AC session); proximity-pilot resistance u16 at p27:28 (0xFFFF = no plug, ~220 with cable); control-pilot values at p19:20/p25:26 go 0→non-zero with cable; DCDC output u8 at p31 (14.7 V).
- Make: honda
- Size: 56 bytes (verified)
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (before/after plug snapshots + real AC charge session)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xCF03
- Name: OnboardChargerTemperature
- Description: OBC temperature at payload byte 8 (u8: raw − 40 = °C). Confirmed against the diagnostic report; early "charging flag" hypothesis definitively disproven. (OBC, target 0xD0.)
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [B] verified capture (confirmed against official diagnostic report)
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xDA10
- Name: BatterySerialNumber
- Description: Battery serial number (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table)

### 0xDA5C
- Name: EventCounterBlock1
- Description: Event/error counter block (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xDA5F
- Name: EventCounterBlock2
- Description: Event/error counter block (BMU, target 0xD4). Present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xA820
- Name: EventCounterBlockRangeStart
- Description: First of the A820–A82A event/error counter blocks (BMU, target 0xD4). Present, not decoded. Range listed as a family; individual block semantics unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xCF01
- Name: ChargeDCDCBlock1
- Description: First of the CF01–CF04 charge/DCDC blocks (OBC, target 0xD0). Present, not decoded (only CF03's temperature byte is verified).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xD300
- Name: CellUnitSOHBlockRangeStart
- Description: First of the D300–D30A per-cell-unit SOH blocks (meter, target 0xDE). Pattern `00 00 64 xx xx` = SOH 100% plus a capacity value (695/631 observed on a new pack). Range listed as a family.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; pattern observed, not fully decoded
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md

### 0xE700
- Name: PCUUnknownBlock
- Description: PCU (target 0xCB) DID, present, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table)

### 0xF802
- Name: VehicleIdentificationNumberASCII
- Description: VIN in ASCII (meter, target 0xDE). PII — handle with care in logs.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; noted in ECU table, not byte-decoded
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table; "F802 = VIN (ASCII — PII, be careful with logs)")

### 0x7122
- Name: BodyABSUnknown1
- Description: Body/ABS (target 0x60) DID, not decoded.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: cnc-lasercraft/honda-wn7-wican docs/obd-protocol.md (Known ECUs table: "7122, 7128, 712A (not decoded)")

### Honda STEP WGN e:HEV RP8 (2023) — discovery results, semantics unknown

From papataku/honda_ehev_analyzer (real vehicle, KONNWEI KW905 ELM327-compatible
adapter, 29-bit ISO 15765-4 500 kbit/s). Automated discovery is read-only 0x22,
no 0x10 session changes, no 0x27 — so all reads below work in the default session.
The project explicitly warns: "Do not guess Honda-specific semantics from an ID,
byte offset, correlation, or ECU source address" and "A high correlation is
candidate evidence, not a signal definition."

### 0x2012
- Name: UnknownSOCMirrorCandidate
- Description: 36-byte payload from responder 0x18DAF101 (ECU source 01). Data byte 5 tracked standard OBD-II PID 0x5B (hybrid battery SOC) with Pearson ~0.9985 / MAE ~0.39 pct across sessions — a strong SOC-mirror candidate, but NOT an official Honda semantic definition. Bytes 24–27 also SOC-correlated. No convincing traction-motor RPM behavior.
- Make: honda
- Size: 36 bytes (verified — Session 12: "383 samples, reconstructed data length 36 bytes")
- Session: default session (verified — discovery uses plain 0x22, no 0x10)
- Security: none required (verified — no 0x27 in discovery)
- Grade: [B] DID existence/size (multiple sessions reproduced, incl. Session 16); [C] SOC-mirror interpretation (inference — flagged: project states it is "still not an official Honda semantic definition")
- Evidence: papataku/honda_ehev_analyzer docs/SESSION12_ANALYSIS.md, docs/SESSION16_ANALYSIS.md, docs/PROJECT_CONTEXT.md (DID 2012 section; request `22 2012`, positive prefix `62 20 12`, responder 18DAF101)

### 0x2001
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 0x2000-range scan. Semantics and size unknown (some responses in the scan were complete, some long/partial).
- Make: honda
- Size: not documented
- Session: default session (verified — discovery uses plain 0x22, no 0x10)
- Security: none required (verified — no 0x27 in discovery)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md (Session 15 positive-DID list)

### 0x2010
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x2013
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

### 0x2018
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

### 0x2019
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x2020
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan; had drive samples in Session 16. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md, docs/SESSION16_ANALYSIS.md

### 0x2025
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x2059
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x2068
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x206A
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x206B
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x206C
- Name: UnknownRP8ECU01Block
- Description: Positive 0x22 response on RP8 ECU source 01 (0x18DAF101), Session 15 scan. Semantics and size unknown.
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/PROJECT_CONTEXT.md

### 0x2680
- Name: UnknownRP8ECU0EBlock
- Description: Complete positive 0x22 response on RP8 ECU source 0E (0x18DAF10E), Session 16. Semantics and size unknown. Part of a 0x2600-range cluster (2680, 2681, 2685, 2686, 2691, 2692, 2693, 269F complete; 26A0/26A1 partial).
- Make: honda
- Size: not documented
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md, docs/PROJECT_CONTEXT.md

### 0xC000
- Name: UnknownRP8ECUEFBlock
- Description: Complete positive 0x22 response, 56-byte payload, on RP8 ECU source EF (0x18DAF1EF), Session 16. Semantics unknown.
- Make: honda
- Size: 56 bytes (verified — Session 16: "C000 — 56-byte payload")
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence/size only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md

### 0xC020
- Name: UnknownRP8ECUEFBlock
- Description: Complete positive 0x22 response, 4-byte payload, on RP8 ECU source EF (0x18DAF1EF), Session 16. Semantics unknown.
- Make: honda
- Size: 4 bytes (verified — Session 16: "C020 — 4-byte payload")
- Session: default session (verified)
- Security: none required (verified)
- Grade: [C] single community source; existence/size only
- Evidence: papataku/honda_ehev_analyzer docs/SESSION16_ANALYSIS.md

### Coverage notes

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

### Sources (live, fetched 2026-10-06)

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

---

## VW Group

_Source file: `did-vw.md`._

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

#### Instrument cluster / MFD — 0x714/0x77E (VCDS 17)

### 0x2203
- Name: Odometer
- Description: Odometer, instrument cluster / MFD view. Shared MQB/MEB convention (VW/Audi/Skoda/SEAT).
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids) + OVMS vweup_obd.h #define (VWUP_MFD_ODOMETER) — multi-source community agreement

### 0x2260
- Name: ServiceIntervalRemainingDistance
- Description: Service interval remaining distance. OVMS decodes as plain uint16 in km.
- Make: vw
- Size: 16 bits, uint16 = km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode

### 0x2261
- Name: ServiceIntervalRemainingTime
- Description: Service interval remaining time. OVMS: uint16 value is remaining DAYS (multiplied by 86400 and added to clock).
- Make: vw
- Size: 16 bits, uint16 = days
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode

### 0x22E0
- Name: EstimatedRangeDisplayed
- Description: Estimated range displayed (cluster). OVMS reads as plain uint16 in km.
- Make: vw
- Size: 16 bits, uint16 = km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.h/vweup_obd.cpp (VWUP_MFD_RANGE_DSP)

### 0x22E4
- Name: UsableBatteryEnergyFromRangeEstimation
- Description: Usable battery energy derived from range estimation. OVMS: uint16/10 = kWh; value 511 = invalid.
- Make: vw
- Size: 16 bits, value = raw/10 kWh; 511 = invalid
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: ODIS-database extraction + OVMS vweup_obd.cpp production decode (VWUP_MFD_RANGE_CAP)

#### Brake electronics — 0x713/0x77D (VCDS 03)

### 0x1821
- Name: TirePressures
- Description: TPMS tyre pressures, read on brake electronics. Decode/size not documented in either source.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids), single source

#### Engine / motor electronics — 0x7E0/0x7E8 (VCDS 01)

### 0xF45B
- Name: MotorElectronicsAbsoluteSoC
- Description: Motor-electronics absolute state of charge (e-Up). NOT battery-management 7E5/7ED. OVMS: uint8, value = raw/2.55 %.
- Make: vw
- Size: 8 bits, value = raw/2.55 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_MOT_ELEC_SOC_ABS) + scainner uds-map (labels corrected 2026-08)

### 0xF802
- Name: VinMotorElectronics
- Description: VIN reported by motor electronics. Single source, medium confidence there; decode/size not documented.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: ODIS-database extraction (ConnorHowell/vag-uds-ids), single source

##### EDC17 diesel DPF/engine band (shipping product: v-cu/dpf-load-monitor-wide firmware, physically tested on VAG diesels; EDC17 family — README warns DIDs vary by engine code)

### 0x10FB
- Name: TurbochargerTemperature
- Description: Turbocharger temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x11B2
- Name: DpfInletTemperature
- Description: DPF inlet temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x10F9
- Name: DpfOutletTemperature
- Description: DPF outlet temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x14F5
- Name: DpfDifferentialPressure
- Description: DPF differential pressure. Unit not documented in firmware (raw uint16 as-is).
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x1156
- Name: DistanceSinceLastRegen
- Description: Distance since last DPF regeneration.
- Make: vw
- Size: 24 bits BE, value = raw/1000 km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x115E
- Name: TimeSinceLastRegen
- Description: Time since last DPF regeneration.
- Make: vw
- Size: 24 bits BE, value = raw/60 min
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x11BE
- Name: EngineOilTemperature
- Description: Engine oil temperature.
- Make: vw
- Size: 16 bits BE, value = (raw-2731)/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x114F
- Name: SootMassCalculated
- Description: DPF soot mass, calculated value.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x114E
- Name: SootMassMeasured
- Description: DPF soot mass, measured value (sensor).
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x105E
- Name: BatteryVoltage
- Description: 12V battery voltage. Firmware: value = raw×2 into int16, range 0-1999; plausibly centivolts (inference — flagged).
- Make: vw
- Size: 16 bits BE, value = raw×2; unit not documented (inference: cV — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x163B
- Name: PostInjection2
- Description: Post-injection quantity 2. Meaning/units not documented beyond name.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x167D
- Name: PostInjection3
- Description: Post-injection quantity 3. Meaning/units not documented beyond name.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

### 0x1153
- Name: OilAshMass
- Description: DPF oil ash mass. Unit not documented.
- Make: vw
- Size: 16 bits BE, unit not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu/dpf-load-monitor-wide firmware can_dpf.c (shipping product, physically tested) + scainner uds-map listing the same DIDs — multi-source community agreement

##### 0xF4xx OBD-PID mirror band (confirmed on VAG; redundant with mode-01 where EOBD is available)

### 0xF40C
- Name: EngineRpm
- Description: Engine RPM = OBD PID 0x0C mirror. VAG-confirmed.
- Make: vw
- Size: 16 bits BE, value = raw/4 rpm
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map RESEARCH §3.2 (VAG-confirmed) + v-cu firmware (dec_rpm = raw/4) + OBDb ID.4 signalset (div 4)

### 0xF41F
- Name: RunTimeSinceEngineStart
- Description: Run time since engine start = OBD PID 0x1F mirror.
- Make: vw
- Size: 16 bits BE, value = raw/60 min
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map RESEARCH §3.2 (VAG-confirmed) + v-cu firmware (dec_u16_div60)

### 0xF405
- Name: CoolantTemperature
- Description: Coolant temperature = OBD PID 0x05 mirror.
- Make: vw
- Size: 8 bits, value = raw-40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_temp_m40) + scainner uds-map RESEARCH §3.2 (VAG-confirmed F405)

### 0xF40D
- Name: VehicleSpeed
- Description: Vehicle speed = OBD PID 0x0D mirror.
- Make: vw
- Size: 8 bits, km/h
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_u8) + OBDb ID.4 signalset (8 bits, km/h, captured test case)

### 0xF40F
- Name: IntakeAirTemperature
- Description: Intake air temperature = OBD PID 0x0F mirror.
- Make: vw
- Size: 8 bits, value = raw-40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: v-cu firmware (dec_temp_m40) + scainner uds-map RESEARCH §3.2 (VAG-confirmed F40F)

### 0xF449
- Name: AbsolutePedalPositionDrive
- Description: Absolute pedal position (drive). ID.4 signalset only.
- Make: vw
- Size: 8 bits, value = raw/2.55 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case), single source

#### HV battery management — 0x7E5/0x7ED (VCDS 8C), pre-MEB / e-Up

### 0x028C
- Name: HvBatteryAbsoluteSoc
- Description: HV battery absolute state of charge (e-Up battery management). OVMS: uint8, value = raw/2.5 %. CONFLICT: OBDb ID.4 names the same DID 'State of charge, display' with a different formula (raw×20.4/46−6.4 %) — platform-dependent, do not mix.
- Make: vw
- Size: 8 bits, e-Up: value = raw/2.5 %; ID.4: value = raw×20.4/46−6.4 % (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.h/.cpp (VWUP_BAT_MGMT_SOC_ABS, production decode) + scainner uds-map (confirmed) + OBDb ID.4 captured test case (17FE007B0462028CAE → 70.77%)

### 0x02BD
- Name: OdometerBmsView
- Description: Odometer as seen by battery management. OVMS: uint24 at offset 1 (after DID echo), value in km.
- Make: vw
- Size: 24 bits @offset 1, km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_ODOMETER) + scainner uds-map listing

### 0x2A0B
- Name: HvBatteryPackTemperature
- Description: HV battery pack temperature (signed). OVMS: signed int16, value = raw/64 °C.
- Make: vw
- Size: 16 bits signed BE, value = raw/64 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_TEMP) + scainner uds-map (scale 0.015625 = 1/64)

### 0x74CB
- Name: HvBatterySohAndCapacity
- Description: HV battery SOH/capacity block (e-Up). OVMS: bytes 0-1 = capacity (uint16, ×0.01 Ah); bytes 2-3 = cell count (uint16); bytes 4+ = per-cell SOH bytes (uint8, value = raw/240×100 % for Gen2). MEB NOTE: uds-map states 74CB is NOT reproduced on MEB (ID.4/Cupra Born use 51E0 instead).
- Make: vw
- Size: composite: 2B (Ah×0.01) + 2B (cell count) + N×1B (cell SOH)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_BAT_MGMT_SOH_CAC) + scainner uds-map

### 0x1E0E
- Name: MaximumBatteryTemperature
- Description: Maximum battery temperature. DECODE NOT VERIFIED: the define exists in vweup_obd.h but the poll-table entries are commented out in the shipping source, so the decode is not exercised by the firmware.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: scainner uds-map (single community source, 'high' there); OVMS has the define but does not poll it

### 0x1E0F
- Name: MinimumBatteryTemperature
- Description: Minimum battery temperature. Same caveat as 1E0E: define exists, polling commented out.
- Make: vw
- Size: not documented
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: scainner uds-map (single community source); OVMS has the define but does not poll it

### 0x1E33
- Name: MaximumCellVoltage
- Description: Maximum HV cell voltage. e-Up/MQB decode: uint16 ×(1/4096) V. CONFLICT: OBDb ID.4 fmt block says mul 2441/div 10000 (unit volts, max 15.997) — the two sources' scalings do not obviously reconcile; the /4096 form is the one with a verified physical decode. Cupra-Born signalset confirms the DID on MEB.
- Make: vw
- Size: 16 bits BE; e-Up/MQB: value = raw/4096 V; ID.4 fmt ambiguous (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map (confirmed on MEB fixtures) + OBDb ID.4 signalset with captured test cases + OBDb Cupra-Born signalset — multi-source

### 0x1E34
- Name: MinimumCellVoltage
- Description: Minimum HV cell voltage. Same decode/conflict note as 1E33.
- Make: vw
- Size: 16 bits BE; e-Up/MQB: value = raw/4096 V; ID.4 fmt ambiguous (see conflict note)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map + OBDb ID.4 signalset with captured test cases + OBDb Cupra-Born signalset — multi-source

### 0x1E3B
- Name: HvBatteryPackVoltage
- Description: HV battery pack voltage. VERIFIED CAPTURE: ID.4 test case response ...62 1E 3B 05 26 → raw 0x0526=1318 → 1318/4 = 329.5 V.
- Make: vw
- Size: 16 bits BE, value = raw/4 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb ID.4 captured test case (raw response verified) + scainner uds-map (confirmed on MEB) + OBDb Cupra-Born

### 0x1E3D
- Name: HvBatteryPackCurrent
- Description: HV battery pack current, positive when discharging. uint16: value = 511 − raw/4 A (scale −0.25, bias 511).
- Make: vw
- Size: 16 bits BE, value = 511 − raw/4 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: scainner uds-map (confirmed on MEB) + OBDb ID.4 signalset (add −511) + OBDb Cupra-Born — multi-source

### 0x51E0
- Name: HvBatteryStateOfHealthMeb
- Description: HV battery state of health, MEB platform (ID.4, Cupra Born). Supersedes 74CB on MEB. Unit %; size/decode not documented beyond unit.
- Make: vw
- Size: not documented (unit: %)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb ID.4 signalset + OBDb Cupra-Born signalset (both name it SOH, module 7E5/7ED or ta=7B) — multi-source; no captured test case found

#### HV charge management — 0x765/0x7CF (VCDS BD)

### 0x1DD0
- Name: DisplayedSoc
- Description: Displayed state of charge — matches instrument cluster; the user-facing SOC. OVMS: uint8, value = raw/2 %.
- Make: vw
- Size: 8 bits, value = raw/2 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode (VWUP_CHG_MGMT_SOC_NORM) + scainner uds-map (high)

#### Electric drive — 0x7E6/0x7EE (VCDS 51)

### 0x465C
- Name: DcDcConverterOutputVoltage
- Description: DC-DC converter output voltage (12V system). OVMS: uint16/512 V. ID.4 signalset agrees (div 512).
- Make: vw
- Size: 16 bits BE, value = raw/512 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode + OBDb ID.4 signalset (div 512, captured test case) — two independent sources

### 0x465B
- Name: DcDcConverterOutputCurrent
- Description: DC-DC converter output current (12V system). OVMS: uint16/16 A. ID.4 has a separate 'alternate' entry 465B on ta=B9 with div 16 — consistent scaling.
- Make: vw
- Size: 16 bits BE, value = raw/16 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OVMS vweup_obd.cpp production decode + OBDb ID.4 signalset (div 16, captured test case) — two independent sources

#### CAN gateway — 0x710/0x77A (VCDS 19), ID.4 MEB (OBDb signalset v3, captured test cases)

### 0x15D1
- Name: ElectricMotorPowerLimitation
- Description: Composite: bits8-23 motor power limit (×50 W), bits24-31 non-vehicle power limit (×50 W), bits32-39 non-vehicle energy req (×0.05 kWh), bits40-55 motor battery energy info (×0.05 kWh).
- Make: vw
- Size: composite, 56 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2A0E
- Name: StartStopBatteryResistance
- Description: Start/stop (12V aux) battery resistance.
- Make: vw
- Size: 8 bits, value = raw×0.2 mΩ
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2A53
- Name: DcDcConverterStatus
- Description: Composite: LV voltage (8b, /10 V), current (16b @8, −511..65024 A offset-binary), reserved current (16b @24, same).
- Make: vw
- Size: composite: 8+16+16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB2
- Name: HvBatteryMaxEnergy
- Description: HV battery max energy.
- Make: vw
- Size: 16 bits, value = raw×0.05 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB4
- Name: RangeReserveAndConsumption
- Description: bits16-31 estimated electric power reserve (km); bits72-79 average battery consumption (A). Partially documented.
- Make: vw
- Size: composite, partial decode
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB5
- Name: EstimatedReserveRange
- Description: Estimated reserve range (CAN).
- Make: vw
- Size: 16 bits @32, km
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB6
- Name: RangeRemainingDisplayed
- Description: Range remaining, displayed (miles per signalset — unit flagged as-is from source).
- Make: vw
- Size: 16 bits, miles (source unit)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB7
- Name: AverageConsumptionCategories
- Description: 7× uint16 average consumption categories 0-6, each /10 kWh.
- Make: vw
- Size: 7×16 bits, each value = raw/10 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB8
- Name: HvBatteryEnergy
- Description: HV battery energy.
- Make: vw
- Size: 16 bits @16, value = raw×0.025 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AF7
- Name: Aux12VBatteryStatus
- Description: Composite 12V battery: voltage (16b, /1000+4 V), current (32b @16, signed ×0.001 A), SOC (8b @56, %), temp (8b @64, −40 °C), sensor temp (8b @72, −40 °C), total charge (32b @96, /10 Ah), total discharge (32b @128, /10 Ah), aging by capacity (8b @160, %).
- Make: vw
- Size: composite, 168 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

#### On-board charger — 0x744/0x7AE (VCDS C6), ID.4 MEB

### 0x103D
- Name: ObcHvDcCurrent
- Description: On-board charger HV/DC current.
- Make: vw
- Size: 16 bits, value = raw/10 A
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x103E
- Name: ObcCycleEnergy
- Description: Cycle energy transformation.
- Make: vw
- Size: 16 bits, value = raw/100 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1507
- Name: ChargerRailEnergies
- Description: 3× uint24 rail energy transformations (rails 1-3).
- Make: vw
- Size: 3×24 bits, each value = raw/10 kWh
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1525
- Name: ObcVoltageProximitySocketA
- Description: Voltage proximity, socket A.
- Make: vw
- Size: 16 bits, mV
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15D6
- Name: ChargerPowerEfficiency
- Description: Power efficiency. NOTE: source labels unit 'amps' — likely a source typo; value = raw/10 + 75, plausible as %.
- Make: vw
- Size: 8 bits, value = raw/10 + 75 (unit ambiguous in source — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15E2
- Name: ChargerCoolantTemperature
- Description: Charger coolant temperature.
- Make: vw
- Size: 8 bits, value = raw−40 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15EE
- Name: ChargingDurationTotal
- Description: Total charging duration.
- Make: vw
- Size: 32 bits, minutes
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1DA7
- Name: ObcHighVoltageOutput
- Description: High voltage output.
- Make: vw
- Size: 16 bits, value = raw/10 V
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1DDA
- Name: ObcTemperatureSocketA
- Description: Temperature sensor, socket A.
- Make: vw
- Size: 16 bits @8, value = raw/10 − 55 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

#### Auto HVAC / Climatronic — 0x746/0x7B0 (VCDS 08), ID.4 MEB

### 0x0800
- Name: AcCompressorPowerActual
- Description: A/C compressor power, actual.
- Make: vw
- Size: 16 bits @40, W
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2603
- Name: AcCompressorSpeed
- Description: A/C compressor speed.
- Make: vw
- Size: 8 bits, value = raw×100 rpm
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2605
- Name: RefrigerantPressure
- Description: Refrigerant pressure.
- Make: vw
- Size: 8 bits, value = raw×0.2 bar
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2606
- Name: RadiatorFanActual
- Description: Radiator fan actual #1 (16b) and #2 (16b @16).
- Make: vw
- Size: 2×16 bits, each value = raw/10 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only)

### 0x260A
- Name: OutsideTemperatureCabinSensor
- Description: Outside temperature from cabin sensor.
- Make: vw
- Size: 8 bits, value = raw×0.5 − 50 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x260C
- Name: TemperatureFrontLeftDeflector
- Description: Front left deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x260D
- Name: TemperatureFrontRightDeflector
- Description: Front right deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2612
- Name: TemperatureEvaporatorOutput
- Description: Evaporator output temperature (signed).
- Make: vw
- Size: 16 bits signed, value = raw/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2613
- Name: TemperatureInterior
- Description: Interior temperature (signed).
- Make: vw
- Size: 16 bits signed, value = raw/10 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x261E
- Name: RecircFlapActual
- Description: Recirculation flap actual: steps (16b) + percent (8b @16, ×0.5 %).
- Make: vw
- Size: 16+8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x261F
- Name: RecircFlapCommandedSteps
- Description: Recirculation flap commanded steps.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2620
- Name: RecircFlapStopFreshAir
- Description: Recirculation flap stop, fresh air.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2621
- Name: RecircFlapStopRecircAir
- Description: Recirculation flap stop, recirculated air.
- Make: vw
- Size: 16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2622
- Name: FrontLeftTempFlapActual
- Description: Front left temperature flap actual.
- Make: vw
- Size: 8 bits @16, value = raw×0.5 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2626
- Name: FrontRightTempFlapActual
- Description: Front right temperature flap actual.
- Make: vw
- Size: 8 bits @16, value = raw×0.5 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x263D
- Name: TemperatureRearDeflector
- Description: Rear deflector temperature.
- Make: vw
- Size: 8 bits, value = raw×0.333 °C
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x26ED
- Name: AirPollutionLevel
- Description: Air pollution level (signed).
- Make: vw
- Size: 8 bits signed, value = raw/10
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x27C3
- Name: OutsideHumidity
- Description: Outside humidity.
- Make: vw
- Size: 8 bits @56, value = raw/2 %
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only)

### 0x27C4
- Name: WindshieldTempAndInsideHumidity
- Description: Windshield temperature (8b, ×0.576−38.8 °C) + inside humidity (8b @32, /2 %).
- Make: vw
- Size: 8+8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x42DB
- Name: Co2ContentInterior
- Description: CO2 content, interior.
- Make: vw
- Size: 8 bits @8, value = raw×100 (unit scalar as in source — flagged)
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x4EEF
- Name: AcRefrigerantSensors
- Description: A/C refrigerant: pressure sensor 1 (16b, ×0.0088 bar), temperature sensor 1 (16b @16, ×0.1−40 °C), interior temp sensor 1 (16b @32, ×0.1−40 °C).
- Make: vw
- Size: 3×16 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

#### Telematics — 0x767/0x7D1 (VCDS 77), ID.4 MEB

### 0x2431
- Name: GpsSatellites
- Description: GPS satellites visible (8b) / tracked (8b @8).
- Make: vw
- Size: 2×8 bits
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

#### MEB target-addressed band (OBDb hdr FC00; ta=7B battery / ta=76 electric drive / ta=B9 DC-DC)

DIDs below are addressed through FC00 with a target-address byte (ta). DID, signal names and decodes are from the
OBDb ID.4 signalset v3; 'captured test case' means a real vehicle response is on file in tests/test_cases (Grade B),
'signalset only' means decode-from-schema with no capture on file (Grade C). Raw CAN framing needs field verification
(see addressing note at top).

### 0x0308
- Name: CALCFROMMEASIS
- Description: ta=7B (battery). Torque, calculated from measured currents [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x0335
- Name: MOTORTRQFRONT
- Description: ta=76 (electric drive). Motor torque, front [16 bits @bit 0; signed; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x033B
- Name: MOTORTRQREAR
- Description: ta=76 (electric drive). Motor torque, rear [16 bits @bit 0; signed; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0343
- Name: MOTORTRQDIFF
- Description: ta=76 (electric drive). Motor torque difference, front to rear [16 bits @bit 0; signed; value = raw ÷2; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0344
- Name: MOTORTRQRATEDFRONT
- Description: ta=76 (electric drive). Motor torque rated, front [16 bits @bit 0; signed; value = raw ÷2; newtonMeters] | Motor torque rated, rear [16 bits @bit 16; signed; value = raw ÷2; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0346
- Name: STEERANGLE
- Description: ta=76 (electric drive). Steering wheel angle [16 bits @bit 0; value = raw ÷10; degrees]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x035E
- Name: HVBATIENG
- Description: ta=76 (electric drive). Battery current, motor controller [16 bits @bit 0; signed; value = raw ÷10; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0360
- Name: HVAUXI
- Description: ta=76 (electric drive). HV auxiliary current total [16 bits @bit 0; signed; value = raw ÷100; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0364
- Name: HVAUXPWR
- Description: ta=76 (electric drive). HV auxiliary power [16 bits @bit 0; signed; value = raw ÷10; kilowatts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0800
- Name: ACCOMPRESSORPWRACT
- Description: ta=?. A/C compressor power, actual [16 bits @bit 40; watts]
- Make: vw
- Size: up to 56 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x0805
- Name: ELDRIVEECUT1
- Description: ta=7B (battery). Electric drive ECU temperature 1 [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x0806
- Name: ELDRIVEECUT2
- Description: ta=7B (battery). Electric drive ECU temperature 2 [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x086D
- Name: ODO
- Description: ta=7B (battery). Odometer, electric drive [32 bits @bit 0; kilometers]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1007
- Name: MOTORVDACT
- Description: ta=7B (battery). Motor voltage, d-axis actual [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1008
- Name: MOTORVQACT
- Description: ta=7B (battery). Motor voltage, q-axis actual [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1009
- Name: MOTORVDCMD
- Description: ta=7B (battery). Motor voltage, d-axis commanded [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x100A
- Name: MOTORVQCMD
- Description: ta=7B (battery). Motor voltage, q-axis commanded [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x103D
- Name: OBCHVDCC
- Description: ta=?. On-board charger, hv/dc current [16 bits @bit 0; value = raw ÷10; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x103E
- Name: OBCCYCLEENERGY
- Description: ta=?. Cycle energy transformation [16 bits @bit 0; value = raw ÷100; kilowattHours]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1040
- Name: INVERTERPWRLOSSPHASEU
- Description: ta=7B (battery). Inverter power loss phase u [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1041
- Name: INVERTERPWRLOSSPHASEV
- Description: ta=7B (battery). Inverter power loss phase v [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1042
- Name: INVERTERPWRLOSSPHASEW
- Description: ta=7B (battery). Inverter power loss phase w [32 bits @bit 0; watts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x1507
- Name: CHRGRRAIL1E
- Description: ta=?. Rail 1 energy transformation [24 bits @bit 0; value = raw ÷10; kilowattHours] | Rail 2 energy transformation [24 bits @bit 24; value = raw ÷10; kilowattHours] | Rail 3 energy transformation [24 bits @bit 48; value = raw ÷10; kilowattHours]
- Make: vw
- Size: up to 72 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1525
- Name: OBCVPROXA
- Description: ta=?. Voltage proximity, socket a [16 bits @bit 0; millivolts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15D1
- Name: HVEMPWRLIMITATION
- Description: ta=?. Electric motor power limitation [16 bits @bit 8; value = raw ×50; watts] | Electric motor non-vehicle power limitation [8 bits @bit 24; value = raw ×50; watts] | Non-vehicle energy requirement [8 bits @bit 32; value = raw ×50 ÷1000; kilowattHours] | Electric motor battery energy [16 bits @bit 40; value = raw ×50 ÷1000; kilowattHours]
- Make: vw
- Size: up to 56 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15D6
- Name: CHRGREFFICIENCY
- Description: ta=?. Power efficiency [8 bits @bit 0; value = raw ÷10 +75; amps]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15E2
- Name: CHRGRCOOLANTT
- Description: ta=?. Temperature, Charger coolant [8 bits @bit 0; value = raw -40; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x15EE
- Name: CHRGRDURTOTAL
- Description: ta=?. Charging duration total [32 bits @bit 0; minutes]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1620
- Name: HVBATPTCI
- Description: ta=7B (battery). Battery heater current [8 bits @bit 0; value = raw ÷4; amps]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1621
- Name: HVBATPTCV
- Description: ta=7B (battery). Battery heater voltage [8 bits @bit 0; value = raw ÷10; volts]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1622
- Name: HVBATECUT
- Description: ta=7B (battery). ECU temperature [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1623
- Name: HVBATPTCT1
- Description: ta=7B (battery). Battery heater temperature, #1 [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1624
- Name: HVBATPTCT2
- Description: ta=7B (battery). Battery heater temperature, #2 [8 bits @bit 0; value = raw -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x189B
- Name: HVBATAFTERCONTACTSV
- Description: ta=7B (battery). HV battery after contacts voltage [16 bits @bit 0; value = raw ×0.5 -1000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x189D
- Name: HVBATTOUT
- Description: ta=7B (battery). Battery temperature, outlet [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, inlet [16 bits @bit 16; signed; value = raw ÷64; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1DA7
- Name: OBCHIGHVOUTPUT
- Description: ta=?. High voltage output [16 bits @bit 0; value = raw ÷10; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1DDA
- Name: OBCTA
- Description: ta=?. Temperature sensor, socket a [16 bits @bit 8; value = raw ÷10 -55; celsius]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E0E
- Name: HVBATTMAX
- Description: ta=7B (battery). Battery temperature, max [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, max sensor ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E0F
- Name: HVBATTMIN
- Description: ta=7B (battery). Battery temperature, min [16 bits @bit 0; signed; value = raw ÷64; celsius] | Battery temperature, min sensor ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E1B
- Name: HVBATILIMCHG
- Description: ta=7B (battery). Battery current limit, charging [16 bits @bit 0; value = raw ÷5; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E1C
- Name: HVBATILIMDSCH
- Description: ta=7B (battery). Battery current limit, discharging [16 bits @bit 0; value = raw ÷5; amps]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E2C
- Name: HVBATCELLSOCMAX
- Description: ta=7B (battery). Battery cell soc, maximum [16 bits @bit 0; value = raw ÷100; percent] | Battery cell soc max, ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E2D
- Name: HVBATCELLSOCMIN
- Description: ta=7B (battery). Battery cell soc, minimum [16 bits @bit 0; value = raw ÷100; percent] | Battery cell soc min, ID [16 bits @bit 16; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E36
- Name: HVBATVBEFORE
- Description: ta=7B (battery). Battery voltage, before main switch [16 bits @bit 0; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E38
- Name: HVBATVAFTER
- Description: ta=7B (battery). Battery voltage, after main switch [16 bits @bit 0; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E39
- Name: HVBATVCHG
- Description: ta=7B (battery). Battery voltage, charging [16 bits @bit 0; signed; value = raw ×312499785 ÷10000000000; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E3C
- Name: HVBATVCELLSSUM
- Description: ta=7B (battery). Battery voltage, sum of all cells [32 bits @bit 0; signed; value = raw ×244140625 ÷1000000000; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E3E
- Name: HVBATIDC2
- Description: ta=7B (battery). Battery current, DC (alt) [32 bits @bit 0; value = raw ÷100 -1500; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E40
- Name: HVBATCELLV001
- Description: ta=7B (battery). HV battery cell voltage, #1 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E41
- Name: HVBATCELLV002
- Description: ta=7B (battery). HV battery cell voltage, #2 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E42
- Name: HVBATCELLV003
- Description: ta=7B (battery). HV battery cell voltage, #3 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E43
- Name: HVBATCELLV004
- Description: ta=7B (battery). HV battery cell voltage, #4 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E44
- Name: HVBATCELLV005
- Description: ta=7B (battery). HV battery cell voltage, #5 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E45
- Name: HVBATCELLV006
- Description: ta=7B (battery). HV battery cell voltage, #6 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E46
- Name: HVBATCELLV007
- Description: ta=7B (battery). HV battery cell voltage, #7 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E47
- Name: HVBATCELLV008
- Description: ta=7B (battery). HV battery cell voltage, #8 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E48
- Name: HVBATCELLV009
- Description: ta=7B (battery). HV battery cell voltage, #9 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E49
- Name: HVBATCELLV010
- Description: ta=7B (battery). HV battery cell voltage, #10 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4A
- Name: HVBATCELLV011
- Description: ta=7B (battery). HV battery cell voltage, #11 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4B
- Name: HVBATCELLV012
- Description: ta=7B (battery). HV battery cell voltage, #12 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4C
- Name: HVBATCELLV013
- Description: ta=7B (battery). HV battery cell voltage, #13 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4D
- Name: HVBATCELLV014
- Description: ta=7B (battery). HV battery cell voltage, #14 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4E
- Name: HVBATCELLV015
- Description: ta=7B (battery). HV battery cell voltage, #15 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E4F
- Name: HVBATCELLV016
- Description: ta=7B (battery). HV battery cell voltage, #16 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E50
- Name: HVBATCELLV017
- Description: ta=7B (battery). HV battery cell voltage, #17 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E51
- Name: HVBATCELLV018
- Description: ta=7B (battery). HV battery cell voltage, #18 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E52
- Name: HVBATCELLV019
- Description: ta=7B (battery). HV battery cell voltage, #19 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E53
- Name: HVBATCELLV020
- Description: ta=7B (battery). HV battery cell voltage, #20 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E54
- Name: HVBATCELLV021
- Description: ta=7B (battery). HV battery cell voltage, #21 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E55
- Name: HVBATCELLV022
- Description: ta=7B (battery). HV battery cell voltage, #22 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E56
- Name: HVBATCELLV023
- Description: ta=7B (battery). HV battery cell voltage, #23 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E57
- Name: HVBATCELLV024
- Description: ta=7B (battery). HV battery cell voltage, #24 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E58
- Name: HVBATCELLV025
- Description: ta=7B (battery). HV battery cell voltage, #25 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E59
- Name: HVBATCELLV026
- Description: ta=7B (battery). HV battery cell voltage, #26 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5A
- Name: HVBATCELLV027
- Description: ta=7B (battery). HV battery cell voltage, #27 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5B
- Name: HVBATCELLV028
- Description: ta=7B (battery). HV battery cell voltage, #28 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5C
- Name: HVBATCELLV029
- Description: ta=7B (battery). HV battery cell voltage, #29 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5D
- Name: HVBATCELLV030
- Description: ta=7B (battery). HV battery cell voltage, #30 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5E
- Name: HVBATCELLV031
- Description: ta=7B (battery). HV battery cell voltage, #31 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E5F
- Name: HVBATCELLV032
- Description: ta=7B (battery). HV battery cell voltage, #32 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E60
- Name: HVBATCELLV033
- Description: ta=7B (battery). HV battery cell voltage, #33 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E61
- Name: HVBATCELLV034
- Description: ta=7B (battery). HV battery cell voltage, #34 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E62
- Name: HVBATCELLV035
- Description: ta=7B (battery). HV battery cell voltage, #35 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E63
- Name: HVBATCELLV036
- Description: ta=7B (battery). HV battery cell voltage, #36 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E64
- Name: HVBATCELLV037
- Description: ta=7B (battery). HV battery cell voltage, #37 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E65
- Name: HVBATCELLV038
- Description: ta=7B (battery). HV battery cell voltage, #38 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E66
- Name: HVBATCELLV039
- Description: ta=7B (battery). HV battery cell voltage, #39 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E67
- Name: HVBATCELLV040
- Description: ta=7B (battery). HV battery cell voltage, #40 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E68
- Name: HVBATCELLV041
- Description: ta=7B (battery). HV battery cell voltage, #41 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E69
- Name: HVBATCELLV042
- Description: ta=7B (battery). HV battery cell voltage, #42 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6A
- Name: HVBATCELLV043
- Description: ta=7B (battery). HV battery cell voltage, #43 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6B
- Name: HVBATCELLV044
- Description: ta=7B (battery). HV battery cell voltage, #44 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6C
- Name: HVBATCELLV045
- Description: ta=7B (battery). HV battery cell voltage, #45 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6D
- Name: HVBATCELLV046
- Description: ta=7B (battery). HV battery cell voltage, #46 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6E
- Name: HVBATCELLV047
- Description: ta=7B (battery). HV battery cell voltage, #47 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E6F
- Name: HVBATCELLV048
- Description: ta=7B (battery). HV battery cell voltage, #48 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E70
- Name: HVBATCELLV049
- Description: ta=7B (battery). HV battery cell voltage, #49 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E71
- Name: HVBATCELLV050
- Description: ta=7B (battery). HV battery cell voltage, #50 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E72
- Name: HVBATCELLV051
- Description: ta=7B (battery). HV battery cell voltage, #51 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E73
- Name: HVBATCELLV052
- Description: ta=7B (battery). HV battery cell voltage, #52 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E74
- Name: HVBATCELLV053
- Description: ta=7B (battery). HV battery cell voltage, #53 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E75
- Name: HVBATCELLV054
- Description: ta=7B (battery). HV battery cell voltage, #54 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E76
- Name: HVBATCELLV055
- Description: ta=7B (battery). HV battery cell voltage, #55 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E77
- Name: HVBATCELLV056
- Description: ta=7B (battery). HV battery cell voltage, #56 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E78
- Name: HVBATCELLV057
- Description: ta=7B (battery). HV battery cell voltage, #57 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E79
- Name: HVBATCELLV058
- Description: ta=7B (battery). HV battery cell voltage, #58 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7A
- Name: HVBATCELLV059
- Description: ta=7B (battery). HV battery cell voltage, #59 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7B
- Name: HVBATCELLV060
- Description: ta=7B (battery). HV battery cell voltage, #60 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7C
- Name: HVBATCELLV061
- Description: ta=7B (battery). HV battery cell voltage, #61 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7D
- Name: HVBATCELLV062
- Description: ta=7B (battery). HV battery cell voltage, #62 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7E
- Name: HVBATCELLV063
- Description: ta=7B (battery). HV battery cell voltage, #63 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E7F
- Name: HVBATCELLV064
- Description: ta=7B (battery). HV battery cell voltage, #64 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E80
- Name: HVBATCELLV065
- Description: ta=7B (battery). HV battery cell voltage, #65 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E81
- Name: HVBATCELLV066
- Description: ta=7B (battery). HV battery cell voltage, #66 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E82
- Name: HVBATCELLV067
- Description: ta=7B (battery). HV battery cell voltage, #67 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E83
- Name: HVBATCELLV068
- Description: ta=7B (battery). HV battery cell voltage, #68 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E84
- Name: HVBATCELLV069
- Description: ta=7B (battery). HV battery cell voltage, #69 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E85
- Name: HVBATCELLV070
- Description: ta=7B (battery). HV battery cell voltage, #70 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E86
- Name: HVBATCELLV071
- Description: ta=7B (battery). HV battery cell voltage, #71 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E87
- Name: HVBATCELLV072
- Description: ta=7B (battery). HV battery cell voltage, #72 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E88
- Name: HVBATCELLV073
- Description: ta=7B (battery). HV battery cell voltage, #73 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E89
- Name: HVBATCELLV074
- Description: ta=7B (battery). HV battery cell voltage, #74 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8A
- Name: HVBATCELLV075
- Description: ta=7B (battery). HV battery cell voltage, #75 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8B
- Name: HVBATCELLV076
- Description: ta=7B (battery). HV battery cell voltage, #76 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8C
- Name: HVBATCELLV077
- Description: ta=7B (battery). HV battery cell voltage, #77 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8D
- Name: HVBATCELLV078
- Description: ta=7B (battery). HV battery cell voltage, #78 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8E
- Name: HVBATCELLV079
- Description: ta=7B (battery). HV battery cell voltage, #79 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E8F
- Name: HVBATCELLV080
- Description: ta=7B (battery). HV battery cell voltage, #80 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E90
- Name: HVBATCELLV081
- Description: ta=7B (battery). HV battery cell voltage, #81 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E91
- Name: HVBATCELLV082
- Description: ta=7B (battery). HV battery cell voltage, #82 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E92
- Name: HVBATCELLV083
- Description: ta=7B (battery). HV battery cell voltage, #83 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E93
- Name: HVBATCELLV084
- Description: ta=7B (battery). HV battery cell voltage, #84 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E94
- Name: HVBATCELLV085
- Description: ta=7B (battery). HV battery cell voltage, #85 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E95
- Name: HVBATCELLV086
- Description: ta=7B (battery). HV battery cell voltage, #86 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E96
- Name: HVBATCELLV087
- Description: ta=7B (battery). HV battery cell voltage, #87 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E97
- Name: HVBATCELLV088
- Description: ta=7B (battery). HV battery cell voltage, #88 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E98
- Name: HVBATCELLV089
- Description: ta=7B (battery). HV battery cell voltage, #89 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E99
- Name: HVBATCELLV090
- Description: ta=7B (battery). HV battery cell voltage, #90 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9A
- Name: HVBATCELLV091
- Description: ta=7B (battery). HV battery cell voltage, #91 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9B
- Name: HVBATCELLV092
- Description: ta=7B (battery). HV battery cell voltage, #92 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9C
- Name: HVBATCELLV093
- Description: ta=7B (battery). HV battery cell voltage, #93 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9D
- Name: HVBATCELLV094
- Description: ta=7B (battery). HV battery cell voltage, #94 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9E
- Name: HVBATCELLV095
- Description: ta=7B (battery). HV battery cell voltage, #95 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1E9F
- Name: HVBATCELLV096
- Description: ta=7B (battery). HV battery cell voltage, #96 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA0
- Name: HVBATCELLV097
- Description: ta=7B (battery). HV battery cell voltage, #97 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA1
- Name: HVBATCELLV098
- Description: ta=7B (battery). HV battery cell voltage, #98 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA2
- Name: HVBATCELLV099
- Description: ta=7B (battery). HV battery cell voltage, #99 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA3
- Name: HVBATCELLV100
- Description: ta=7B (battery). HV battery cell voltage, #100 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA4
- Name: HVBATCELLV101
- Description: ta=7B (battery). HV battery cell voltage, #101 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA5
- Name: HVBATCELLV102
- Description: ta=7B (battery). HV battery cell voltage, #102 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA6
- Name: HVBATCELLV103
- Description: ta=7B (battery). HV battery cell voltage, #103 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA7
- Name: HVBATCELLV104
- Description: ta=7B (battery). HV battery cell voltage, #104 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA8
- Name: HVBATCELLV105
- Description: ta=7B (battery). HV battery cell voltage, #105 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EA9
- Name: HVBATCELLV106
- Description: ta=7B (battery). HV battery cell voltage, #106 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EAA
- Name: HVBATCELLV107
- Description: ta=7B (battery). HV battery cell voltage, #107 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EAB
- Name: HVBATCELLV108
- Description: ta=7B (battery). HV battery cell voltage, #108 [16 bits @bit 0; value = raw ÷1000 +1; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EAE
- Name: HVBATMODT1
- Description: ta=7B (battery). HV battery module temperature, #1 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EAF
- Name: HVBATMODT2
- Description: ta=7B (battery). HV battery module temperature, #2 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB0
- Name: HVBATMODT3
- Description: ta=7B (battery). HV battery module temperature, #3 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB1
- Name: HVBATMODT4
- Description: ta=7B (battery). HV battery module temperature, #4 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB2
- Name: HVBATMODT5
- Description: ta=7B (battery). HV battery module temperature, #5 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB3
- Name: HVBATMODT6
- Description: ta=7B (battery). HV battery module temperature, #6 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB4
- Name: HVBATMODT7
- Description: ta=7B (battery). HV battery module temperature, #7 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB5
- Name: HVBATMODT8
- Description: ta=7B (battery). HV battery module temperature, #8 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB6
- Name: HVBATMODT9
- Description: ta=7B (battery). HV battery module temperature, #9 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB7
- Name: HVBATMODT10
- Description: ta=7B (battery). HV battery module temperature, #10 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB8
- Name: HVBATMODT11
- Description: ta=7B (battery). HV battery module temperature, #11 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EB9
- Name: HVBATMODT12
- Description: ta=7B (battery). HV battery module temperature, #12 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EBA
- Name: HVBATMODT13
- Description: ta=7B (battery). HV battery module temperature, #13 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EBB
- Name: HVBATMODT14
- Description: ta=7B (battery). HV battery module temperature, #14 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EBC
- Name: HVBATMODT15
- Description: ta=7B (battery). HV battery module temperature, #15 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x1EBD
- Name: HVBATMODT16
- Description: ta=7B (battery). HV battery module temperature, #16 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2005
- Name: BRAKEBOOSTERP
- Description: ta=76 (electric drive). Brake booster pressure [16 bits @bit 0; value = raw ÷1000; bars]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2055
- Name: RADIATORFANDUTY
- Description: ta=76 (electric drive). Radiator fan duty [16 bits @bit 0; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2431
- Name: GPSSATSVISIBLE
- Description: ta=?. Satellites, visible [8 bits @bit 0; scalar] | Satellites, tracked [8 bits @bit 8; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2603
- Name: ACCMPRSPEED
- Description: ta=?. A/C compressor, speed [8 bits @bit 0; value = raw ×100; rpm]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2605
- Name: REFRIGP
- Description: ta=?. Refrigerant pressure [8 bits @bit 0; value = raw ×0.2; bars]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2606
- Name: HVACFAN1ACT
- Description: ta=?. Radiator fan actual #1 [16 bits @bit 0; value = raw ÷10; percent] | Radiator fan actual #2 [16 bits @bit 16; value = raw ÷10; percent]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x260A
- Name: AATCABIN
- Description: ta=?. Outside temperature, from cabin sensor [8 bits @bit 0; value = raw ×0.5 -50; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x260C
- Name: FRONTLEFTDEFLT
- Description: ta=?. Temperature, front left deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x260D
- Name: FRONTRIGHTDEFLT
- Description: ta=?. Temperature, front right deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2612
- Name: HVACEVAPT
- Description: ta=?. Temperature, evaporator output [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2613
- Name: HVACIAT
- Description: ta=?. Temperature, interior [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x261E
- Name: RECIRCFLAPACTSTEPS
- Description: ta=?. Recirculation flap, actual steps [16 bits @bit 0; scalar] | Recirculation flap, actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x261F
- Name: RECIRCFLAPCMDSTEPS
- Description: ta=?. Recirculation flap, commanded steps [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2620
- Name: RECIRCFLAPSTOPFRESH
- Description: ta=?. Recirculation flap stop, fresh air [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2621
- Name: RECIRCFLAPSTOPRECIRC
- Description: ta=?. Recirculation flap stop, recirculated air [16 bits @bit 0; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2622
- Name: FRONTLEFTTFLAPACT
- Description: ta=?. Front left temperature flap actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2626
- Name: FRONTRIGHTTFLAPACT
- Description: ta=?. Front right temperature flap actual [8 bits @bit 16; value = raw ×0.5; percent]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x263D
- Name: REARDEFLT
- Description: ta=?. Temperature, rear deflector [8 bits @bit 0; value = raw ×0.333; celsius]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x26ED
- Name: AIRPOLUTION
- Description: ta=?. Air pollution level [8 bits @bit 0; signed; value = raw ÷10; scalar]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x276D
- Name: COOLANTCIRCPUMPDUTY
- Description: ta=76 (electric drive). Coolant circulation pump duty [16 bits @bit 0; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x27C3
- Name: HVACOUTSIDEHUM
- Description: ta=?. Outside humidity [8 bits @bit 56; value = raw ÷2; percent]
- Make: vw
- Size: up to 64 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x27C4
- Name: WNDSHLDTEMP
- Description: ta=?. Windshield, temperature [8 bits @bit 0; value = raw ×0.576 -38.8; celsius] | Humidity, inside [8 bits @bit 32; value = raw ÷2; percent]
- Make: vw
- Size: up to 40 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x295A
- Name: ENGODO
- Description: ta=76 (electric drive). Odometer [24 bits @bit 0; kilometers]
- Make: vw
- Size: up to 24 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x29D4
- Name: MOTORTRQREQ
- Description: ta=76 (electric drive). Motor torque requested [16 bits @bit 0; value = raw ÷10; newtonMeters]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2A0E
- Name: SSBR
- Description: ta=?. Start/stop battery resistance [8 bits @bit 0; value = raw ×2 ÷10; milliohms]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2A53
- Name: DCDCVLOW
- Description: ta=?. DC-DC converter, low voltage [8 bits @bit 0; value = raw ÷10; volts] | DC-DC converter, current [16 bits @bit 8; value = raw -511; amps] | DC-DC converter, reserved current [16 bits @bit 24; value = raw -511; amps]
- Make: vw
- Size: up to 40 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB2
- Name: HVBATCAP
- Description: ta=?. HV battery, max energy [16 bits @bit 0; value = raw ×50 ÷1000; kilowattHours]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB4
- Name: RANGERESERVEEST
- Description: ta=?. Estimated electric power reserve [16 bits @bit 16; kilometers] | Average battery consumption [8 bits @bit 72; amps]
- Make: vw
- Size: up to 80 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB5
- Name: RANGEESTCAN
- Description: ta=?. Estimated reserve range [16 bits @bit 32; kilometers]
- Make: vw
- Size: up to 48 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB6
- Name: RANGE
- Description: ta=?. Range remaining, displayed [16 bits @bit 0; miles]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB7
- Name: AVGCSMPCAT0
- Description: ta=?. Average consumption (category 0) [16 bits @bit 0; value = raw ÷10; kilowattHours] | Average consumption (category 1) [16 bits @bit 16; value = raw ÷10; kilowattHours] | Average consumption (category 2) [16 bits @bit 32; value = raw ÷10; kilowattHours] | Average consumption (category 3) [16 bits @bit 48; value = raw ÷10; kilowattHours] | Average consumption (category 4) [16 bits @bit 64; value = raw ÷10; kilowattHours] | Average consumption (category 5) [16 bits @bit 80; value = raw ÷10; kilowattHours] | Average consumption (category 6) [16 bits @bit 96; value = raw ÷10; kilowattHours]
- Make: vw
- Size: up to 112 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AB8
- Name: HVBATKWH
- Description: ta=?. HV battery energy [16 bits @bit 16; value = raw ×25 ÷1000; kilowattHours]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2AF7
- Name: AUXBATV
- Description: ta=?. 12V battery voltage [16 bits @bit 0; value = raw ÷1000 +4; volts] | 12V battery current [32 bits @bit 16; signed; value = raw ×0.001; amps] | 12V battery soc [8 bits @bit 56; percent] | Temperature, 12V battery [8 bits @bit 64; value = raw -40; celsius] | Temperature, 12V battery sensor [8 bits @bit 72; value = raw -40; celsius] | 12V battery total charge [32 bits @bit 96; value = raw ÷10; ampereHours] | 12V battery total discharge [32 bits @bit 128; value = raw ÷10; ampereHours] | 12V battery aging by capacity [8 bits @bit 160; percent] | 12V battery aging by power [8 bits @bit 168; percent] | 12V battery adapted capacity [8 bits @bit 176; ampereHours]
- Make: vw
- Size: up to 184 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x2CCC
- Name: ROTORTMODEL
- Description: ta=7B (battery). Rotor temperature model [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3DEF
- Name: SOC
- Description: ta=76 (electric drive). State of charge [16 bits @bit 0; signed; value = raw ÷100; percent]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x3DF8
- Name: MOTORRPM
- Description: ta=76 (electric drive). Motor speed [16 bits @bit 0; signed; value = raw ÷2; rpm]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x3E93
- Name: DCLINKV
- Description: ta=7B (battery). DC link voltage [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3E98
- Name: DCLINKI
- Description: ta=7B (battery). DC link current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EE7
- Name: MOTORMAXIMUMI
- Description: ta=7B (battery). Motor maximum current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EE8
- Name: MOTORMINIMUMI
- Description: ta=7B (battery). Motor minimum current [32 bits @bit 0; amps]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EE9
- Name: ACTUALMECHANICALTORQUECALC
- Description: ta=7B (battery). Actual mechanical torque calculated [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EEA
- Name: ACTUALPOSSIBLEMAXIMUMTORQUE
- Description: ta=7B (battery). Actual possible maximum torque [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EEB
- Name: ACTUALPOSSIBLEMINIMUMTORQUE
- Description: ta=7B (battery). Actual possible minimum torque [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x3EED
- Name: DESIREDLINKV
- Description: ta=7B (battery). Desired link voltage [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x40C8
- Name: ELDRIVEMOTORRADSEC
- Description: ta=7B (battery). Electric drive motor speed (rad/sec) [32 bits @bit 0; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x42DB
- Name: CO2CONTENTINTERIOR
- Description: ta=?. CO2 content interior [8 bits @bit 8; value = raw ×100; scalar]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x43B8
- Name: DCDCTCOOL
- Description: ta=76 (electric drive). Temperature, DC-DC converter coolant [16 bits @bit 0; signed; value = raw ÷10; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x43B9
- Name: DCLINKVRESERVE
- Description: ta=7B (battery). DC link voltage reserve [32 bits @bit 0; volts]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x4539
- Name: ACCEL
- Description: ta=76 (electric drive). Acceleration [16 bits @bit 0; signed; value = raw ÷1000; metersPerSecondSquared]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x4657
- Name: ELDRIVEMOTORFREQ
- Description: ta=7B (battery). Motor electrical frequency (rad/sec) [32 bits @bit 0; scalar]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x465D
- Name: DCDCV
- Description: ta=B9 (DC-DC). DC-DC voltage [16 bits @bit 0; value = raw ÷512; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x4672
- Name: MOTORT
- Description: ta=7B (battery). Temperature, motor [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x4675
- Name: HVBATVTRAC
- Description: ta=76 (electric drive). Battery voltage, traction mode [16 bits @bit 0; signed; value = raw ÷10; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x4EEF
- Name: ACREFRIGPSENS1
- Description: ta=?. A/C refrigerant pressure, sensor 1 [16 bits @bit 0; value = raw ×88 ÷10000; bars] | A/C refrigerant temperature, sensor 1 [16 bits @bit 16; value = raw ×10 ÷100 -40; celsius] | A/C refrigerant temperature, sensor 1 interior [16 bits @bit 32; value = raw ×10 ÷100 -40; celsius]
- Make: vw
- Size: up to 48 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x4FAE
- Name: ELECDRIVEINFLOWCOOLANTT
- Description: ta=7B (battery). Temperature, electric drive inflow coolant [32 bits @bit 0; celsius]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x5170
- Name: MINIMUMDISCHARGEV
- Description: ta=7B (battery). Discharge voltage, min [16 bits @bit 0; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x5171
- Name: MAXIMUMCHARGEV
- Description: ta=7B (battery). Charge voltage, max [16 bits @bit 0; volts]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x5867
- Name: ODOBMS2
- Description: ta=7B (battery). Odometer, BMS #2 [16 bits @bit 16; value = raw ×10; kilometers]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x58E1
- Name: ACTUALMECHANICALTORQUECMDVALUE
- Description: ta=7B (battery). Actual mechanical torque commanded [32 bits @bit 0; newtonMeters]
- Make: vw
- Size: up to 32 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [C]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (signalset only, no capture on file)

### 0x7425
- Name: HVBATMODT17
- Description: ta=7B (battery). HV battery module temperature, #17 [16 bits @bit 0; value = raw ÷8 -40; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x7426
- Name: HVBATMODT18
- Description: ta=7B (battery). HV battery module temperature, #18 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x7427
- Name: HVBATMODT19
- Description: ta=7B (battery). HV battery module temperature, #19 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x7428
- Name: HVBATMODT20
- Description: ta=7B (battery). HV battery module temperature, #20 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x7429
- Name: HVBATMODT21
- Description: ta=7B (battery). HV battery module temperature, #21 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x742A
- Name: HVBATMODT22
- Description: ta=7B (battery). HV battery module temperature, #22 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x742B
- Name: HVBATMODT23
- Description: ta=7B (battery). HV battery module temperature, #23 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x742C
- Name: HVBATMODT24
- Description: ta=7B (battery). HV battery module temperature, #24 [16 bits @bit 0; celsius]
- Make: vw
- Size: up to 16 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x743B
- Name: CIRCPUMPFLOW
- Description: ta=7B (battery). HV battery: circulation pump flow [8 bits @bit 0; value = raw ×10; percent]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### 0x7448
- Name: RAPIDCHARGEPORT
- Description: ta=7B (battery). Charging, rapid? [1 bits @bit 4; noyes] | AC charging [1 bits @bit 5; noyes] | Current gear [1 bits @bit 7; enum: 0=STANDBY, 1=DRIVING]
- Make: vw
- Size: up to 8 bits payload
- Session: not documented; sources read in default session (no source shows an 0x10 prerequisite)
- Security: none documented (read-only; no source performs 0x27)
- Grade: [B]
- Evidence: OBDb Volkswagen-ID.4 signalset v3 (captured test case)

### Coverage notes

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

---

## Hyundai / Kia

_Source file: `did-hyundai.md`._

Research for the M2 OEM vehicle database v1.3. Manufacturer-specific DIDs only.
ISO-standard DIDs 0xF180–0xF19E are deliberately excluded (covered separately).
KWP2000 service 0x21 "local IDs" (2101/2102/…) used by older platforms are
out of scope but cross-referenced where the same DID number speaks 0x22 on
newer platforms.

Grade key: **A** = OEM service info; **B** = multi-source community agreement
or verified capture; **C** = single community source. Per-entry flags mark
which field of the grade an inference touches.

Research date: 2026-10-06.

### Conventions

- Request addressing is normal 11-bit physical: request `0x7Ex` → response `0x7Ex+8` on most ECUs (verified on BMS 0x7E4→0x7EC, CLU 0x7C6→0x7CE). canair's `B-index` counts the 3-byte response echo (`62 DID_hi DID_lo`), so **B04 = first data byte** (cross-verified against EVNotiPi's byte offsets for 0x0101 and 0xB002).
- `Session`: none of the sources used a non-default session (0x10) before these reads. `Security`: no source reported a seed/key (0x27) requirement for any read listed. Both are stated as "not documented" where the source does not explicitly confirm.
- Model applicability is per-entry. 2017 Ioniq EV data comes from canair's whole-day capture/reverse-engineering program (WiCAN community, 2026). Kona/Niro EV data comes from JejuSoul OBD-PIDs (Torque community, years of real-world use) and EVNotiPi (Kona EV, open source). Genesis shares the Hyundai/Kia platform and DIDs; Kia-specific evidence is noted per entry.
- Sizes marked "not documented" were never explicitly stated; "≥N bytes inferred" means the highest referenced byte index requires at least N.

---

### BMS (0x7E4 → 0x7EC) — Kona EV / Niro EV / Ioniq 5-era platforms

NOTE: on the 2017 Ioniq EV these same DID numbers (0101/0102/…) are served
over KWP2000 service 0x21 at the same address (canair BMS profile,
`id_protocol: KWP2000`). The 0x22 form below is for the UDS-speaking
Kona/Niro EV platform. Genesis EV models share this platform.

### 0x0101
- Name: BMS main telemetry block
- Description: Battery pack state: SOC (BMS + display), pack current, pack DC voltage, max/min cell temps, 4 module temps, inlet temp, aux battery voltage, charge/discharge power limits, cumulative charge/ discharge Ah and kWh, operating time, charge-port and relay status bits. Byte layout cross-verified byte-for-byte between two independent community sources (SOC at data byte 5 = e/2, signed current at bytes 11–12 = (K*256+L)/10 A, voltage at bytes 13–14 = (m*256+n)/10 V, max/min temps at bytes 15–16).
- Make: hyundai
- Size: not documented (EVNotiPi decodes 62 response bytes / 59 data bytes; JejuSoul references up to data byte 58; ≥61 bytes inferred)
- Session: default session (no 0x10 used by any source)
- Security: not documented (no seed/key reported)
- Grade: [B] multi-source community agreement (EVNotiPi Kona EV open-source decoder + JejuSoul Kona/Niro EV Torque PID set, years of use, byte layouts agree exactly)
- Evidence: EVNotiPi car/kona_ev.py fields + JejuSoul 003_Kona&Niro_EV_BMS.csv (65 PID rows); independent third corroboration claimed in cxalem/scainner RESEARCH.md (EVNotiPi vs OVMS byte offsets)

### 0x0102
- Name: BMS cell voltages 1–32
- Description: Cells 1–32, one byte each, value/50 = volts (JejuSoul) = ×0.02 V (EVNotiPi). Sources agree on layout exactly.
- Make: hyundai
- Size: not documented (~39 bytes inferred: 3 echo + 4 pad + 32 cell bytes)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

### 0x0103
- Name: BMS cell voltages 33–64
- Description: Cells 33–64, same 1-byte ×0.02 V encoding as 0x0102.
- Make: hyundai
- Size: not documented (~39 bytes inferred, same layout as 0x0102)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

### 0x0104
- Name: BMS cell voltages 65–96
- Description: Cells 65–96, same 1-byte ×0.02 V encoding. Cells 97–98 are in 0x0105, not here.
- Make: hyundai
- Size: not documented (~39 bytes inferred, same layout as 0x0102)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

### 0x0105
- Name: BMS secondary block (SOH, deterioration, cells 97–98)
- Description: State of health ((z*256+aa)/10 %), minimum deterioration, max/min deterioration cell numbers, display SOC (af/2), battery heater 1/2 temps, airbag duty, cell voltage deviation, cells 97–98 (ai/aj, ×0.02).
- Make: hyundai
- Size: not documented (EVNotiPi decodes 46 bytes; JejuSoul references up to data byte 36; ≥38 bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] existence/size agreement; [C] some individual field decodings (EVNotiPi decodes SOH + display SOC only; heater-temp/deterioration decodings are JejuSoul-only)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 003_Kona&Niro_EV_BMS.csv (17 PID rows)

---

### HVAC (0x7B3 → 0x7BB) — Kona/Niro EV + 2017 Ioniq EV

NOTE: byte layouts agree across platforms for 0x0100 (canair 2017 Ioniq EV
uses B-index; B11 = 6th data byte = Torque letter F; B12 = 7th data byte =
Torque letter G — identical to JejuSoul's Kona EV F/G formulas). Treat as
one DID with platform-shared encoding.

### 0x0100
- Name: HVAC temperature block
- Description: Outdoor temp (G/2−40 °C, 7th data byte), indoor/interior temp (F/2−40 °C, 6th data byte), heat-pump temp (13th data byte, /2−40), compressor duty and assorted status bytes. Verified fields: interior temp, ambient temp (canair); outdoor/indoor temps (JejuSoul).
- Make: hyundai
- Size: not documented (canair references up to B37 → ≥34 data bytes, ≥37 bytes inferred on 2017 Ioniq EV)
- Session: default session
- Security: not documented
- Grade: [B] description/size; [C] unverified trailing fields (canair marks compressor-duty and most bytes unverified)
- Evidence: canair ioniq-2017 hvac.yaml (active, whole-day capture program) + JejuSoul 002_Kona&Niro_EV_HVAC.csv

### 0x0102
- Name: HVAC heat-exchanger block
- Description: Heat exchanger temps ((B10/2)−40, (B11/2)−40), compressor on flag (B17, verified), compressor-on mirror (B18), hotside temp.
- Make: hyundai
- Size: not documented (references up to B19 → ≥16 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description (canair active; 2017 Ioniq EV); [C] most field encodings (only compressor-on verified)
- Evidence: canair ioniq-2017 hvac.yaml

### 0x01A0
- Name: HVAC control/status block
- Description: Driver/passenger set temps, HVAC on/off flags, cooling/ heating mode flags. canair notes "62 bytes. Primary HVAC control/status DID."
- Make: hyundai
- Size: 62 bytes (canair note)
- Session: default session
- Security: not documented
- Grade: [B] description/size; [C] field encodings (canair active, 2017 Ioniq EV; parameter-level detail not fully extracted in this pass)
- Evidence: canair ioniq-2017 hvac.yaml

---

### BCM (0x7A0 → 0x7A8) — 2017 Ioniq EV

NOTE: canair BCM responses are 13 bytes for the 0xB0xx family (10 data
bytes). The 0xC00B response is longer (≥25 bytes, multi-frame).

### 0xC00B
- Name: TPMS tyre pressures and temperatures
- Description: Four tyre pressures (B10, B14, B19, B23 / 72.52 = bar — kPa/psi convention), four tyre temperatures (B11, B15, B20, B25 − 50 °C). Kia Niro EV WiCAN PR#716 corroborated the temperature bytes.
- Make: hyundai
- Size: not documented (≥25 bytes inferred from B25; multi-frame, response_frames=4)
- Session: default session
- Security: not documented
- Grade: [B] multi-source (canair active+verified, 2017 Ioniq EV; OVMS Ioniq 5 poll table independently uses 22 C0 0B for pressures/temperatures per cxalem/scainner RESEARCH.md)
- Evidence: canair ioniq-2017 bcm.yaml + scainner RESEARCH.md citing OVMS

### 0xC002
- Name: TPMS sensor IDs
- Description: TPMS wheel-sensor IDs per OVMS Ioniq 5 poll table.
- Make: hyundai
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single second-hand citation (scainner RESEARCH.md citing OVMS `vehicle_hyundai_ioniq5`; OVMS source not directly read in this pass)
- Evidence: cxalem/scainner RESEARCH.md (Hyundai/Kia section)

### 0xB00E
- Name: BCM charge-port status
- Description: Charge-port-open bit (B10:5), confirmed via Kia Niro EV WiCAN PR#716. Multi-frame (response_frames=2).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [B] single-source but verified true + independent PR corroboration
- Evidence: canair ioniq-2017 bcm.yaml (active)

### 0xB004
- Name: BCM door-lock state
- Description: 13-byte response; B11:6 = door lock state (1=locked), confirmed via fob lock/unlock test.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB005
- Name: BCM unlock bits A
- Description: 13-byte response; B10 changes A0↔AC during fob lock/unlock (bits 2,3). Correlated with B004 lock state.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB006
- Name: BCM unlock bits B
- Description: 13-byte response; B12 changes 00↔04 during fob lock/unlock (bit 2). Correlated with B004/B005.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB003
- Name: BCM 12V battery sensing
- Description: 12V battery voltage (B10×0.08), second 12V sense (B28×0.08), plus B12.
- Make: hyundai
- Size: not documented (references up to B28 → ≥26 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB007
- Name: BCM preheat departure time
- Description: Preheat departure-time setting (draft, decode pending).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB00C
- Name: BCM preheat schedule days
- Description: Preheat schedule day bitmask (draft, decode pending).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB001
- Name: BCM unknown A
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB002
- Name: BCM unknown B
- Description: Answers; content not decoded (draft). NOTE: same DID number as the CLU odometer DID 0xB002 (different ECU, 0x7A0 vs 0x7C6) — DID numbers are ECU-scoped on this platform.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB008
- Name: BCM unknown C
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB009
- Name: BCM unknown D
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xB00A
- Name: BCM unknown E
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

### 0xC011
- Name: BCM 12V bus monitor
- Description: 13-byte response; B11/12.8 = 12V bus voltage, [B13:B14] = event counter; bytes 8–9 (ELM index) change rapidly — not static.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

---

### CLU — cluster (0x7C6 → 0x7CE)

### 0xB002
- Name: Odometer
- Description: 3-byte odometer in km at response offset 9–11 (canair [B12:B14]; EVNotiPi padding 9 + 3-byte field — identical). Total response 15 bytes. Verified across three independent community sources. Also carries an unverified byte at B11 (candidate CLU internal temp, (B11/2)−40).
- Make: hyundai
- Size: 15 bytes
- Session: default session
- Security: not documented
- Grade: [B] multi-source agreement (EVNotiPi Kona EV + JejuSoul Kona/Niro/Soul EV + canair 2017 Ioniq EV); [C] the B11 temp byte (canair inference — flagged)
- Evidence: EVNotiPi car/kona_ev.py (odo 3 bytes at offset 9, `optional`) + JejuSoul Kia_Soul_EV_Cluster_data.csv & Hyundai_Ioniq_EV_BMS_data.csv (Int24(g:h:i)) + canair ioniq-2017 clu.yaml (active)

### 0xB001
- Name: CLU unknown A
- Description: 13-byte response, all zeros when stationary; purpose unknown. Captured payload example: 62 B0 01 followed by 10 zero bytes.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 clu.yaml (draft)

### 0xB003
- Name: CLU unknown B
- Description: 13-byte response; B3=0x88, B7=0x01, rest zeros; purpose unknown. Captured payload example: 62 B0 03 88 00 00 00 01 00 00 00 00 00.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 clu.yaml (draft)

---

### ESC/ABS (0x7D1) — 2017 Ioniq EV

### 0xC101
- Name: ESC vehicle and wheel speeds
- Description: Real vehicle speed (B12, km/h), 4 wheel speeds (B18–B21, km/h, r=+1.000 vs real speed in driving capture), gear selector (B14), steering angle ([B35:B36]−32768)/10 deg (verified via held-wheel + driving steer sweep vs EPS). Unverified: longitudinal accel candidate (S23−128), brake pressure (B44).
- Make: hyundai
- Size: not documented (references up to B44 → ≥42 data bytes, ≥45 bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified fields; [C] accel/brake-pressure fields (canair inference — flagged)
- Evidence: canair ioniq-2017 esc.yaml (active, 2026-07-22/26/30 driving captures)

### 0xC102
- Name: ESC unknown
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 esc.yaml (draft)

---

### EPS/MDPS (0x7D4) — 2017 Ioniq EV

### 0x0101
- Name: EPS steering/speed block
- Description: 18-byte payload. Absolute steering angle (signed big-endian S9:B10, −(S9×256+B10)/10 deg — verified 2026-07-30, r=+1.000 vs ESC steering angle), EPS-side vehicle speed (B14, km/h, verified), speed band (B15), tail constant 0x1010 at B18/B19. Unverified: B05/B06/B07, B11, candidate torque at B12:S13 (LE signed 16-bit).
- Make: hyundai
- Size: 18 bytes data (21 bytes response inferred; canair states "18-byte payload")
- Session: default session (vehicle state READY required by canair profile)
- Security: not documented
- Grade: [B] description/verified fields; [C] torque and unresolved bytes (canair inference — flagged)
- Evidence: canair ioniq-2017 eps.yaml (active, 2026-07-22 driving capture + 2026-07-30 angle resolution)

### 0x0102
- Name: EPS unknown (static)
- Description: Static/constant response; content not decoded.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] single source, content unknown
- Evidence: canair ioniq-2017 eps.yaml (static)

---

### IGPM — integrated gateway/power module (0x770) — 2017 Ioniq EV

### 0xBC03
- Name: IGPM door/hood/lamp status
- Description: Door-open bits (B10: driver, passenger, RL, RR; trunk B10:7; hood B11:0), door-lock bits (B10:1, B10:3), DRL/tail/high/low beam (B12:2–5), seatbelt FL (B11:1), ACC2/IGN status bits, config byte B09. Most bits verified via timed event captures 2026-07-24.
- Make: hyundai
- Size: not documented (references up to B13 → ≥11 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified bits (canair active; Kia Niro EV WiCAN PR#716 corroboration on door bits); [C] unverified bits (flagged)
- Evidence: canair ioniq-2017 igpm.yaml (active)

### 0xBC04
- Name: IGPM door-lock status
- Description: Door-lock FL/FR bits plus B10 bit 0 field.
- Make: hyundai
- Size: not documented (references up to B10 → ≥8 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] single-source active, verified per canair
- Evidence: canair ioniq-2017 igpm.yaml (active)

### 0xBC06
- Name: IGPM brake/turn-signal status
- Description: Brake light (B10), left/right turn signals (B11:0, B11:1 — corrected 2026-08-09, user-confirmed), brake-pedal bits (B10:2, unverified).
- Make: hyundai
- Size: not documented (references up to B11 → ≥9 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified fields; [C] brake-pedal bits (flagged)
- Evidence: canair ioniq-2017 igpm.yaml (active)

### 0xBC01
- Name: IGPM unknown A
- Description: Static byte field B5; purpose unknown (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 igpm.yaml (draft)

### 0xBC05
- Name: IGPM unknown B
- Description: Static byte B5; unlock-flash bits (B10), trunk indicator (B11:3) partially decoded.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 igpm.yaml (draft)

### 0xBC07
- Name: IGPM charge-port lock status
- Description: Charge-port lock (B11:7), inverted copy (B12:0), ACC2-related (B12:3), IGPM wake latch (B12:2) — decoded, unverified.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, decoded-but-unverified single source
- Evidence: canair ioniq-2017 igpm.yaml (draft)

---

### SCC / ADAS radar (0x7D0) — openpilot-era platforms

### 0xF100
- Name: ECU long description (firmware identification string)
- Description: Hyundai-proprietary firmware ID string used by openpilot/ opendbc for ECU fingerprinting. Captured format example (camera ECU): `AEE MFC  AT EUR LHD 1.00 1.00 95740-G2600 190730` — platform code, module name, region, HW/SW versions, part number, date code. Response to `22 F1 00` is `62 F1 00 <ascii>`. Same DID also read from EPS and ADAS ECUs (opendbc PLATFORM_CODE_ECUS = fwdRadar, fwdCamera, eps).
- Make: hyundai
- Size: variable ASCII, not documented (captured examples ~40–50 bytes of payload)
- Session: default session
- Security: not documented
- Grade: [B] verified captures in opendbc + defined read path in opendbc values.py/interface.py
- Evidence: opendbc clone car/hyundai/values.py (HYUNDAI_VERSION_REQUEST_LONG) + car/hyundai/fingerprints.py (real `62 F1 00` responses, e.g. MDPS C `56310G7300` variants)

### 0xF110
- Name: ECU alternate long description
- Description: Alternate firmware-description DID queried by opendbc when 0xF100 does not yield a platform code (HYUNDAI_VERSION_REQUEST_ALT).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] defined in opendbc code; no captured response found in the local clone's fingerprints
- Evidence: opendbc clone car/hyundai/values.py only

### 0x0142
- Name: SCC radar configuration (radar-points debug output)
- Description: Radar config register; openpilot community tooling reads and writes it via 0x22/0x2E to enable radar-track debug output on bus 1 for certain Hyundai radars. Persistent across reboots. Safety-relevant: community notes warn AEB/FCW behavior may be affected.
- Make: hyundai
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source family (openpilot HOW-TOS text, copied across sunnypilot/animalpilot forks — one origin)
- Evidence: openpilot HOW-TOS.md "Radar Tracks" (via kirito3481/sunnypilot, alexandresato/animalpilot, taik/twilsonco-openpilot mirrors)

### 0x0100
- Name: SCC unknown
- Description: Answers on SCC (0x7D0); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 scc.yaml (draft)

---

### ADAS camera / MFC (0x730) and parking ADAS (0x7B1)

The 0xF100/0xF110 firmware-identification DIDs are read here by opendbc
(see SCC section for full entries — same DIDs, same encoding):

### 0xF100
- Name: ECU long description (firmware identification string)
- Description: See full entry under SCC. opendbc reads it from the ADAS camera ECU (0x730) and parking ADAS ECU (0x7B1) for fingerprinting; 0x7B1 is also the address opendbc silences via 0x28 communication control on CAN-FD blinker platforms (interface.py).
- Make: hyundai
- Size: variable ASCII, not documented
- Session: default session
- Security: not documented
- Grade: [B] verified captures in opendbc
- Evidence: opendbc clone car/hyundai/values.py + fingerprints.py + interface.py (0x730/0x7B1 usage)

### 0xF110
- Name: ECU alternate long description
- Description: Alternate firmware-description DID (see SCC section).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] defined in opendbc code; no captured response in local clone
- Evidence: opendbc clone car/hyundai/values.py only

### 0x0100
- Name: MFC unknown
- Description: Answers on MFC/camera ECU (0x7C4 in canair ioniq-2017; 0x730 on openpilot-era ADAS platforms); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 mfc.yaml (draft)

---

### GSA (0x7B6) — 2017 Ioniq EV

### 0x0100
- Name: GSA unknown
- Description: Answers on GSA (0x7B6); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 gsa.yaml (draft)

---

### Coverage notes

Verified ranges and systematic gaps:

1. **EV powertrain (0x7E2/0x7E3/0x7E5/0x7E6)** — the JejuSoul and canair
   sources show these ECUs (VCU, MCU, OBC/LDC, AAF) speaking KWP2000
   service **0x21** (LIDs 2100/2101/2102/2106) on Soul EV 27 kWh and 2017
   Ioniq EV. No 0x22 equivalents for VCU/MCU/OBC were found — on the
   UDS-speaking Kona/Niro platform only the BMS 0x01xx block is documented
   via 0x22. Motor/inverter, on-board charger, and DC-DC 0x22 DIDs are a
   gap.
2. **EMS/ECM, TCU, EPB, SRS, TPMS-module, BCM on ICE platforms** — no
   community 0x22 captures found for gasoline/diesel EMS or TCU. canair's
   ICE-relevant DIDs stop at the EV ECUs listed above. GDS/KDS technician
   documentation is not publicly available; no OEM service-info source
   was found for any entry (nothing here is Grade A).
3. **DID numbering is ECU-scoped, not global**: 0x0100 exists on HVAC,
   MFC, SCC, and GSA with unrelated content; 0x0101 exists on BMS, EPS,
   and HVAC-draft; 0xB002 exists on both BCM (unknown) and CLU (odometer).
   A DID number alone does not identify the data — always pair with the
   request address.
4. **0xF1xx identity block**: 0xF100/0xF110 are documented; no other
   manufacturer-specific F1xx DIDs (F101–F10F, F111–F17F) were verified.
   The 0xF18B manufacturing-date read used by opendbc is an ISO-standard
   DID and excluded per scope.
5. **Write access (0x2E)**: only 0x0142 (SCC radar) has a documented write
   path; no other 0x2E-writable DIDs verified.
6. **CAN-FD / E-GMP platforms (Ioniq 5/6, EV6, 2021+)**: canair's
   ioniq-5-2022 profile exists but only the CLU ECU file was populated;
   raw captures contain many 0x22 requests (e.g. 22 10 10, 22 51 00,
   22 1A xx families) that are not yet attributed to ECUs — a rich but
   unmined source. OVMS's Ioniq 5 poll table (cited second-hand) is the
   only E-GMP-specific confirmation (0xC002/0xC00B at 0x7A0).
7. **N-performance / ICE telemetry DIDs** (boost, knock, fuel-rail, DCT
   temps, eLSD) appear in an aftermarket app's roadmap as GDS-derived
   targets but no DID numbers were published — unverifiable, excluded.
8. **Kia vs Hyundai**: Kia evidence appears via Kia Niro EV WiCAN PRs and
   shared Kona/Niro EV PID files (same DIDs, same addresses). No
   Kia-only DID divergence was found; all entries apply to both makes
   unless noted. Genesis data is absent but platform-shared by design.
9. **Session/security**: every source performed these reads in the default
   session with no 0x27 unlock. Extended-session-only or secured DIDs
   (if any) are not represented here.

---

## Nissan / Infiniti

_Source file: `did-nissan.md`._

> **Nissan CAN-era quirk (applies to every entry below):** Nissan's enhanced
> diagnostics are KWP2000-style, NOT pure UDS. The working sequence is
> **DiagnosticSessionControl `0x10 0xC0` followed by service `0x21`
> (readDataByLocalIdentifier)** with a **1-byte local ID**. Positive
> response is `0x61 <localID> <data…>`. On CAN-era ICE modules UDS service
> `0x22` is **rejected with NRC `0x12`** — verified live on a 2018
> Pathfinder R52 (ECM `0x7E0`/`0x7E8`, TCM `0x7E1`/`0x7E9`) [B], and
> independently corroborated by the Leaf TCU community app (session
> `02 10 C0`, reads `02 21 <id>`, writes `3B <id> …`) [B] and by the 370Z
> community (session `02 10 C0` to BCM `0x745` unlocks enhanced commands)
> [C]. ISO-standard DIDs (mode 0x01 PIDs, `0xF190` VIN, etc.) are NOT
> duplicated here — this file covers only Nissan/Infiniti-specific
> identifiers. Every identifier below is a **0x21 local ID unless stated
> otherwise**.

Addressing seen in captures (Nissan follows ISO 15765-4 physical addressing):
- ECM: request `0x7E0` → response `0x7E8`
- TCM/CVT: request `0x7E1` → response `0x7E9`
- Leaf TCU (ZE0/AZE0): request `0x746` → response `0x783` (EV-CAN)

---

### TCU — Nissan Leaf ZE0/AZE0 (Continental 2012 / Ficosa Gen2.5 profiles)

All reads are `02 21 <id>` after `02 10 C0`; writes are `3B <id> …`.
No security access required for reads. These are the local-ID field
definitions of a working open-source TCU configurator app tested against
real Leaf TCUs (TX `0x746` / RX `0x783`).

### 0x04
- Name: TcuActivation
- Description: TCU activation state; 0x21 local ID (not UDS 0x22). Non-zero = activated. Writable via 0x3B (activation write uses value 01 to activate, 00 to deactivate).
- Make: nissan
- Size: 1 byte
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required for reads; writes via service 0x3B (Ficosa profile adds session 0x10 0xFA + routines 0x31 0x1000/0x1001 before writes — routine contents not documented)
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (Continental 2012 and Ficosa Gen2.5 profiles); read command "02 21 04", activation write "3B 04 01/00"

### 0x09
- Name: TcuSignalLevel
- Description: TCU cellular signal data; 0x21 local ID (not UDS 0x22). App decodes first 3 bytes as antenna level, reception power, error rate; remaining bytes not documented. Read-only.
- Make: nissan
- Size: 20 bytes
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required (read-only field)
- Grade: [B] name/encoding; [C] meaning of bytes 3–19 (not documented)
- Evidence: open-source Leaf TCU configurator (both profiles); app renders byte 0/1/2 as ANT level, reception power, error rate

### 0x81
- Name: TcuVin
- Description: VIN stored in the TCU; 0x21 local ID (not UDS 0x22). App reads 19 bytes = 17-char VIN followed by a 2-byte big-endian checksum, and validates the checksum against a CRC of the VIN before display. Writable via "3B 81" with fresh checksum appended.
- Make: nissan
- Size: 17 bytes VIN + 2-byte checksum = 19 bytes on the wire
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required for reads
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (both profiles); VIN+CRC split and validation implemented in the app's adapter code

### 0x59
- Name: TcuDtcStatus
- Description: DTC read/clear function on the TCU. **Not** read via 0x21: the app reads it with service `0x19 0x02 0xFF` and clears with `0x14 0xFF 0xFF 0xFF`. Included because it lives in the same TCU local-ID/field namespace.
- Make: nissan
- Size: not documented (multi-frame, up to 4096-byte app buffer)
- Session: 0x10 0xC0 prerequisite
- Security: not documented
- Grade: [B] services used; [C] payload layout (not documented)
- Evidence: open-source Leaf TCU configurator (both profiles); clear command "14FFFFFF", read "031902FF"

### 0x03
- Name: TcuServicesFlags
- Description: Telematics service enable flags (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). 12 bytes; bytes 8–11 are 0/1 flags for SVTB, RLU, horn, remote start (in that order). Writable via "3B 03".
- Make: nissan
- Size: 12 bytes
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads; Ficosa writes add session 0x10 0xFA + routines 0x31 0x1000/0x1001
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile); byte-8..11 flag positions used by the app's service switches

### 0x10
- Name: TcuApnDial (Continental 2012) / TcuApnName (Ficosa Gen2.5)
- Description: Cellular APN dial/name string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Same ID, different label per TCU supplier profile. Writable via "3B 10 01 <data>".
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name/size; [C] size (app buffer length, wire length assumed equal — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles; label differs by profile)

### 0x11
- Name: TcuApnUser (Continental 2012) / TcuDns1 (Ficosa Gen2.5)
- Description: APN username (Continental) / DNS1 (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile. Writable via "3B 11 01 <data>".
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x12
- Name: TcuApnPass (Continental 2012) / TcuDns2 (Ficosa Gen2.5)
- Description: APN password (Continental) / DNS2 (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile. Writable via "3B 12 01 <data>".
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x13
- Name: TcuApnName (Continental 2012) / TcuObsServerPort (Ficosa Gen2.5)
- Description: APN name (Continental) / OBS server port (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x14
- Name: TcuDns1 (Continental 2012) / TcuObsServerUrl (Ficosa Gen2.5)
- Description: DNS1 (Continental) / OBS server URL (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x15
- Name: TcuDns2 (Continental 2012) / TcuApnUser (Ficosa Gen2.5)
- Description: DNS2 (Continental) / APN username (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x16
- Name: TcuProxy (Continental 2012) / TcuApnPass (Ficosa Gen2.5)
- Description: Proxy (Continental) / APN password (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x17
- Name: TcuProxyPort (Continental 2012) / TcuTspApnUser (Ficosa Gen2.5)
- Description: Proxy port (Continental) / TSP APN username (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x18
- Name: TcuApnConnectionType (Continental 2012) / TcuTspApnPass (Ficosa Gen2.5)
- Description: APN connection type (Continental) / TSP APN password (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

### 0x19
- Name: TcuServerHostname
- Description: Server hostname string (Continental 2012 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Continental 2012 profile only)

### 0x21
- Name: TcuSmsNumber
- Description: SMS number string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 20 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x22
- Name: TcuSmsNumberTsp
- Description: TSP SMS number string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 20 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x2C
- Name: TcuTspApnName
- Description: TSP APN name string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x2E
- Name: TcuTspDns1
- Description: TSP DNS1 string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 32 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x2F
- Name: TcuTspDns2
- Description: TSP DNS2 string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 32 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x30
- Name: TcuTspServerPort
- Description: TSP server port string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x31
- Name: TcuTspServerUrl
- Description: TSP server URL string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

### 0x32
- Name: TcuTspPki
- Description: TSP PKI data (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). **Conflict in source: the same profile maps 0x32 to both "TSP PKI" and "TSP root CA"** — one of the two labels is wrong in the app source. Treat the ID as existing but the semantic as disputed.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] ID exists/responds; [C] semantic (conflict — flagged, unresolved)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile lists 0x32 twice with different labels)

---

### TCM — 2018 Nissan Pathfinder R52 (JATCO CVT), request 0x7E1 → response 0x7E9

Verified by a live 0x21 local-ID sweep (0x01–0x20) after `02 10 C0` on a
real 2018 Pathfinder. Positive response format `61 <lid> <data>`.

### 0x02
- Name: TcmUnknownStoredBlock02
- Description: TCM 0x21 local ID (not UDS 0x22) that returns a positive response. **Content is stored/static data, NOT a live CVT monitor** — it stayed byte-identical across a full 0–104 km/h driving capture (2026-07-04). Meaning, size, and encoding not documented.
- Make: nissan
- Size: not documented
- Session: 0x10 0xC0 prerequisite (verified: session opens on TCM, `61 02 …` returned)
- Security: none required for reads
- Grade: [B] existence/response verified; [C] everything else (not documented — flagged)
- Evidence: 2018 Pathfinder live-diagnostics project; 0x21 LID sweep 0x01–0x20 on TCM 0x7E1→0x7E9; driving capture proved data is static

### 0x04
- Name: TcmUnknownStoredBlock04
- Description: TCM 0x21 local ID (not UDS 0x22) that returns a positive response. **Content is stored/static data, NOT a live CVT monitor** — it stayed byte-identical across a full 0–104 km/h driving capture (2026-07-04). Meaning, size, and encoding not documented.
- Make: nissan
- Size: not documented
- Session: 0x10 0xC0 prerequisite (verified: session opens on TCM, `61 04 …` returned)
- Security: none required for reads
- Grade: [B] existence/response verified; [C] everything else (not documented — flagged)
- Evidence: 2018 Pathfinder live-diagnostics project; 0x21 LID sweep 0x01–0x20 on TCM 0x7E1→0x7E9; driving capture proved data is static

---

### ECM — 2018 Nissan Pathfinder R52 (VQ35DD), request 0x7E0 → response 0x7E8

The same project ran a 0x21 sweep of local IDs 0x01–0x20 on the ECM after
opening session `10 C0`. **No positive responses were documented for any
LID 0x01–0x20 on the ECM** (contrast: the TCM answered 0x02/0x04). The
project therefore relies on generic mode-0x01 PIDs for ECM data. UDS
`0x22` (attempted: VIN DID `0xF190`) was **rejected with NRC `0x12`**
even after session `10 C0` — verified live. No ECM-specific 0x21 local
ID could be verified; none is listed above. This is a verified
negative result, not an absence of data.

---

### Qashqai — single-source UDS DIDs (unconfirmed, model-dependent)

The Pathfinder project notes (from CONSULT-III research, not its own
capture) that fuel-rail-pressure DIDs were "confirmed on Nissan Qashqai"
via UDS `0x22` — but they did **not** verify on their car, and their car
rejects `0x22` outright. Treat as model-dependent.

### 0x2801
- Name: FuelRailPressureMeasured
- Description: Fuel rail pressure, measured value; **UDS 0x22 DID (not a 0x21 local ID)**. Units reported as 0.1 bar per LSB (big-endian u16). Only claimed for Qashqai; the 2018 Pathfinder rejected 0x22 with NRC 0x12, so do not assume it works elsewhere.
- Make: nissan
- Size: 2 bytes (u16, 0.1 bar/LSB)
- Session: 0x10 0xC0 was attempted on Pathfinder; Qashqai session requirement not documented
- Security: not documented (claimed: no security needed for 0x22 live-data reads)
- Grade: [C] (single community source, unconfirmed on the capture vehicle — flagged)
- Evidence: 2018 Pathfinder project's notes citing CONSULT-III research ("confirmed on Nissan Qashqai; UNCONFIRMED for VQ35DD")

### 0x2802
- Name: FuelRailPressureSetpoint
- Description: Fuel rail pressure, setpoint/commanded value; **UDS 0x22 DID (not a 0x21 local ID)**. Units reported as 0.1 bar per LSB (big-endian u16). Same Qashqai-only caveat as 0x2801.
- Make: nissan
- Size: 2 bytes (u16, 0.1 bar/LSB)
- Session: 0x10 0xC0 was attempted on Pathfinder; Qashqai session requirement not documented
- Security: not documented (claimed: no security needed for 0x22 live-data reads)
- Grade: [C] (single community source, unconfirmed on the capture vehicle — flagged)
- Evidence: 2018 Pathfinder project's notes citing CONSULT-III research ("confirmed on Nissan Qashqai; UNCONFIRMED for VQ35DD")

---

### Coverage notes

**Identifier ranges NOT verified:**
- ECM `0x21` local IDs above `0x20` on any Nissan — no public sweep found.
- TCM local IDs above `0x20` (only `0x01`–`0x20` swept on the Pathfinder).
- BCM / ABS / IPDM / airbag / other modules: no `0x21` sweep published. (The 370Z community documented session `10 C0` on BCM `0x745` plus KWP service `0x30` for commanding — e.g. `04 30 05 00 01 00 00 00` door lock/unlock — but no `0x21` local-ID reads.)
- Infiniti-specific modules: nothing found.
- Leaf battery/LBC (`0x7BB`) and VCM local IDs: no verified `0x21` ID list found (LeafSpy reads these but its request set is not publicly documented).
- Consult-I/DDL-era (pre-CAN) is out of scope per task.

**Systematic gaps:**
- No OEM (Nissan/Infiniti service-manual) source for local IDs is publicly available; everything here is community reverse-engineering. Nothing in this file reaches Grade A.
- Encodings: only the TCU string fields (ASCII) and the `0x81` VIN checksum layout are decoded. TCM `0x02`/`0x04` payloads are opaque.
- Newer modules are migrating OFF the `0x21` scheme: per the Leaf TCU community's migration report, the ZE1 AIVC v2.5 TCU (TX `0x7CA`/RX `0x7DA`) uses standard UDS — session `0x10 0x03`, `0x22` with 2-byte DIDs (`0xF190`, `0x4006`, …) and `0x2E` writes. So post-~2018 modules may answer `0x22` after all; the `0x21`/NRC-`0x12` behavior is model- and module-dependent, not a universal Nissan rule. Non-ISO DIDs on those newer modules (e.g. `0x4006`) are not documented anywhere found — open research.

**Conflicts reported (not silently resolved):**
1. Ficosa Gen2.5 profile maps local ID `0x32` to BOTH "TSP PKI" and "TSP root CA" — one label is wrong in the app source.
2. `0x22` acceptance is model-dependent: rejected with NRC `0x12` on the 2018 Pathfinder (verified capture) vs. claimed working on Qashqai for DIDs `0x2801`/`0x2802` (single source, unconfirmed).
3. TCU string-field sizes are the app's buffer lengths (`fieldLength`); wire payload length is assumed equal but not independently verified — flagged `[C]` on each.
4. TCM `0x02`/`0x04` look like plausible live-data IDs but a driving capture proved they are static stored data; do not log them as live CVT signals.
