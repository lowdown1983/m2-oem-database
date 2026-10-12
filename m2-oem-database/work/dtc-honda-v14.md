# Honda / Acura — Manufacturer-Specific DTCs (v1.4.0 expansion)

Research for the M2 OEM vehicle database (v1.4.0). Every factual claim carries a
quality grade: **A** = Honda service manual / Honda TSB · **B** = reputable DTC
database or multi-source agreement (incl. Honda/Acura technician sources) ·
**C** = single community source. SAE J2012 generic codes are NOT duplicated here
(they live in the v1.2 generic catalog). These are NEW codes **not** in the v1.2.1
Honda DTC file — the 90 codes already in the database are excluded by the dedup
list and are not repeated here.

Honda SRS, ABS, and VSA modules historically use proprietary blink-code DTCs
rather than standard B1xxx/C1xxx OBD-II codes. Those are documented AS blink
codes in the dedicated section below — no B1xxx/C1xxx equivalents are invented.

Research date: 2026-10-07.

---

## P-codes (powertrain) — new in v1.4.0

## P1009
- Description: Camshaft Position (CMP) Sensor, Intake/Front, Bank 1 — Circuit Malfunction / Timing Over-Advanced / System Performance
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; valve timing; engine mechanical fault; CMP actuator; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source; cites scribd Honda DTC compilation)

## P1020
- Description: Valve Position Control Circuit — Valve Stuck Off
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; VTEC solenoid valve assembly; rocker-arm oil pressure sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1021
- Description: Valve Position Control Circuit — Valve Stuck On
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; VTEC solenoid valve assembly; rocker-arm oil pressure sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1024
- Description: Valve Position Control Circuit — Valve Sticking On
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; rocker arm assembly
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1025
- Description: Valve Position Control Circuit — Valve Sticking Off
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: MAP sensor; rocker arm assembly
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1026
- Description: Valve Position Control Circuit — Valve Stuck On
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: rocker arm assembly
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1103
- Description: Mass Airflow Sensor Higher Than Expected
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1109
- Description: Barometric Pressure (BARO) Sensor — Circuit Malfunction, Out of Range
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1111
- Description: Intake Air Temperature (IAT) Sensor — Circuit/Intermittent Voltage High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; IAT sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1112
- Description: Intake Air Temperature (IAT) Sensor — Circuit/Intermittent Voltage Low
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; IAT sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1114
- Description: Engine Coolant Temperature (ECT) Sensor — Circuit/Intermittent Voltage High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ECT sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1115
- Description: Engine Coolant Temperature (ECT) Sensor — Circuit/Intermittent Voltage High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ECT sensor
- Diagnostic notes: source lists P1114 and P1115 with near-identical descriptions; treated as listed, possible transcription duplication
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1116
- Description: Engine Coolant Temperature (ECT) Sensor — Range/Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ECT sensor 1; ECT sensor 2
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1120
- Description: Throttle Motor Position Sensor 1 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring open/short to ground/short to positive; throttle control unit; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1125
- Description: Throttle Position (TP) Motor — Fail-Safe Mode
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; TP sensor; TP motor; mechanical fault; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1130
- Description: Heated Oxygen Sensor (HO2S) 2/3 — Faulty Components
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: HO2S 2; HO2S 3
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1133
- Description: Heated Oxygen Sensor (HO2S), RH Front — Insufficient Switching
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: exhaust system; wiring; HO2S; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1134
- Description: Heated Oxygen Sensor (HO2S), RH Front — Slow Operation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: exhaust system; wiring; HO2S; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1153
- Description: Heated Oxygen Sensor (HO2S), LH Front — Insufficient Switching
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: exhaust system; wiring; HO2S; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1154
- Description: Heated Oxygen Sensor (HO2S), LH Front — Slow Operation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: exhaust system; wiring; HO2S; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1171
- Description: Heated Oxygen Sensor (HO2S) 1 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; HO2S; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1172
- Description: Heated Oxygen Sensor (HO2S) 1, Bank 1 — Out of Range, High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; HO2S
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1174
- Description: Heated Oxygen Sensor (HO2S) 2, Bank 2 — Out of Range, High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; HO2S
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1182
- Description: Fuel Temperature Sensor Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to ground; fuel temperature sensor (per ninjafix.in)
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1183
- Description: Fuel Temperature Sensor Circuit High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to positive; fuel temperature sensor (per ninjafix.in)
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1187
- Description: Fuel Tank Temperature Sensor — Low Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to ground; fuel tank temperature sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1188
- Description: Fuel Tank Temperature Sensor — High Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to positive; fuel tank temperature sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1192
- Description: Fuel Tank Pressure Sensor — Low Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to ground; fuel tank pressure sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1193
- Description: Fuel Tank Pressure Sensor — High Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring short to positive; fuel tank pressure sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1201
- Description: Cylinder 1 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: Honda-specific per-cylinder misfire code; sources direct readers to compare with generic P0301. ninjafix.in variant wording: "Fuel System Failure Caused No. 1 Cylinder Misfire".
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair Honda codes; freeautomechanic.com Honda OBD II codes; cars-care.net Honda P-code list)

## P1202
- Description: Cylinder 2 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0302
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1203
- Description: Cylinder 3 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0303
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1204
- Description: Cylinder 4 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0304
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1205
- Description: Cylinder 5 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0305
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1206
- Description: Cylinder 6 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0306
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1220
- Description: Throttle Motor Position Sensor 2 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring open/short to ground/short to positive; throttle control unit; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1221
- Description: Throttle Motor Position Sensor 1/2 — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; throttle control unit; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1241
- Description: Throttle Vent Control Motor Circuit 1 Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Throttle Valve Control Motor Circuit 1 Malfunction"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs on meaning

## P1242
- Description: Throttle Vent Control Motor Circuit 2 Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Throttle Valve Control Motor Circuit 2 Malfunction"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1243
- Description: Throttle Position Insufficient
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1244
- Description: Closed Throttle Position Insufficient
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1246
- Description: Accelerator Position Sensor 1 Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Accelerator Pedal Position Sensor 1 Circuit Malfunction"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1247
- Description: Accelerator Position Sensor 2 Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Accelerator Pedal Position Sensor 2 Circuit Malfunction"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1248
- Description: Accelerator Position Sensors 1 & 2 Improper Correlation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Accelerator Pedal Position Sensor 1 and 2 Incorrect correlation"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net); ninjafix.in concurs

## P1271
- Description: Accelerator Pedal Position (APP) Sensor 1/2 — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1272
- Description: Accelerator Pedal Position (APP) Sensor 2/3 — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1273
- Description: Accelerator Pedal Position (APP) Sensor 1/3 — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1275
- Description: Accelerator Pedal Position (APP) Sensor 1 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring open/short to ground/short to positive; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1280
- Description: Accelerator Pedal Position (APP) Sensor 2 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring open/short to ground/short to positive; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1285
- Description: Accelerator Pedal Position (APP) Sensor 3 — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; APP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1286
- Description: Oil Pressure Sensor, Rocker Arm — Signal Stuck Low
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; VTEC system oil line; rocker-arm oil pressure sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1287
- Description: Oil Pressure Switch, Rocker Arm — Circuit High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; rocker-arm oil pressure switch; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1288
- Description: Oil Pressure Switch, Rocker Arm — Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; rocker-arm oil pressure switch; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1289
- Description: Oil Pressure Sensor, Rocker Arm — Stuck High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; rocker-arm oil pressure sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P128A
- Description: Valve Position Control Circuit — Valve Stuck Off
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; engine oil pressure sensor; rocker arm oil control valve
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P128B
- Description: Valve Position Control Circuit — Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: oil level; wiring; engine oil pressure sensor; rocker arm oil control valve
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1290
- Description: Throttle Position (TP) Motor — Forced Idle Mode
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; APP sensor; TP motor; mechanical fault; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1295
- Description: Throttle Position (TP) Motor — Power Management Mode
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; TP sensor; TP motor; MAP sensor; MAF sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1299
- Description: Throttle Position (TP) Motor — Forced Engine Shut Down Mode
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; TP sensor; TP motor; MAP sensor; MAF sensor; ECM
- Diagnostic notes: CONFLICT (cross-make): Ford uses P1299 for "Cylinder Head Over Temperature Protection Active" (Ford powertrain DTC charts). The Honda-specific meaning above is from the Honda fault-code list.
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source for the Honda meaning)

## P1301
- Description: Cylinder 1 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0301
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1302
- Description: Cylinder 2 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0302
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1303
- Description: Cylinder 3 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0303
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1304
- Description: Cylinder 4 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0304
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1305
- Description: Cylinder 5 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0305
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1306
- Description: Cylinder 6 Misfire
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: compare with generic P0306
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1310
- Description: Ignition Control Module (ICM) — Diagnosis
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ignition coil(s); ICM; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1311
- Description: Ignition Control Module (ICM) — Ignition Coil Secondary Signal, Circuit 1
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ignition coil(s); ICM; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1312
- Description: Ignition Control Module (ICM) — Ignition Coil Secondary Signal, Circuit 2
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ignition coil(s); ICM; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1326
- Description: Ignition Control Module (ICM) — Combustion Quality Input Signal
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ignition coil(s); ICM; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1340
- Description: Ignition Control Module (ICM) — Cylinder Identification/Synchronization
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ignition coil(s); ICM; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1355
- Description: Front Ignition Coil Power Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; fuse; ignition coil; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Intake side ignition coil — power supply circuit malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1356
- Description: Exhaust Side Ignition Coil — Power Supply Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; fuse; ignition coil; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1380
- Description: ECM/ABS Control Module, Rough Road Signal — Communication Fault
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ABS trouble code(s) stored; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1386
- Description: CYP Sensor B Intermittent Interruption
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Cylinder Position Sensor 2 Intermittent Interruption"
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1387
- Description: CYP Sensor B No Signal
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Cylinder Position Sensor Intermittent Interruption" (appears to be a transcription slip for "No Signal"; 5 Star / freeautomechanic / cars-care agree on "No Signal")
- Grade: [B]
- Evidence: three independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com; cars-care.net)

## P1390
- Description: G-Sensor — Intermittent Voltage Low
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; G-sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1391
- Description: G-Sensor — Performance
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: seal damaged/missing; incorrectly installed; wiring; G-sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1392
- Description: G-Sensor — Voltage Low
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; G-sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1393
- Description: G-Sensor — Voltage High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; G-sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1394
- Description: G-Sensor — Intermittent Voltage High
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; G-sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1399
- Description: Random Misfire (Honda-specific; more sensitive than P0300)
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ignition components; incorrect valve clearance; vacuum/intake leaks; fuel delivery; engine compression; timing; air/fuel mixture (per Westwood Honda dealer blog)
- Diagnostic notes: triggered at far lower crank-speed variation than generic P0300 — PCM "suspects" a misfire (P1399) vs "sure" (P0300). Other makes use P1399 with different definitions.
- Grade: [B]
- Evidence: troublecodes.net Honda code page (reputable DTC database); Westwood Honda dealer blog; justanswer Honda technician threads agree

## P1404
- Description: Exhaust Gas Recirculation (EGR) Valve — Valve Closed
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; EGR valve
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1406
- Description: Exhaust Gas Recirculation (EGR) Valve Position Sensor — Circuit Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; EGR valve/position sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1410
- Description: Air Pump Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; AIR pump relay; AIR pump; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Secondary air injection (AIR) pump — malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1415
- Description: Air Pump Electric Current Sensor Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; AIR pump electrical current sensor; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AIR pump electrical current sensor — circuit low"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1416
- Description: Air Pump Electric Current Sensor Circuit High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; AIR pump electrical current sensor; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AIR pump electrical current sensor — circuit high"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1420
- Description: NOx Adsorptive Catalyst System Efficiency Below Threshold
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: NOx adsorptive three-way catalyst (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "NOx adsorptive catalyst system — efficiency below limit"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1429
- Description: Motor Drive Module — Overheating Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); voltage converter module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1430
- Description: Motor Drive Module — Short Circuit Sensor Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); voltage converter module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1431
- Description: Hybrid Battery Pack — Overheating
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: hybrid battery pack
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1432
- Description: Battery Cell — Overheating
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: hybrid battery pack
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1433
- Description: Hybrid Battery Pack — Deterioration
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: hybrid battery pack
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1434
- Description: Voltage Converter Module — High Voltage
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: stored when battery needs protection from very low temperature; system is OK (per source)
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1435
- Description: Charge/Discharge Balance Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: low 12V battery; charging system malfunction
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1436
- Description: Motor Power Inverter Module — Overheating
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: motor power inverter module; hybrid battery pack cooling fan duct; hybrid battery pack cover
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1437
- Description: Motor Power Inverter Module — Short Circuit
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1438
- Description: Motor Drive Module (MDM) Overheating Signal Circuit; Motor Drive Module (MDM) Overheating
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module fan; fan duct line; voltage converter module; motor power inverter module (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1438 (signal circuit / overheating). ninjafix.in variant wording: "Motor driver module — overheating".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1439
- Description: Motor Drive Module (MDM) Short Circuit Sensor Problem; Motor Drive Module (MDM) Short Circuit
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1439. ninjafix.in variant wording: "Motor driver module — short circuit".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1440
- Description: IMA System Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power cable; motor stator; motor power inverter module; motor rotor; MCM programming; MCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor power inverter module — output circuit malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1441
- Description: Evaporative Emission (EVAP) Canister Purge System — Flow Detected
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; EVAP solenoid; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1442
- Description: Evaporative Emission (EVAP) Canister Purge System — Vacuum Switch Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; vacuum switch; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1443
- Description: High Voltage Contactor/Bypass Contactor — Contactor Stays Activated
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; DC-DC converter; hybrid battery pack; motor power inverter module; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1444
- Description: High Voltage Short Circuit
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: motor power inverter module; motor stator; motor power cable assembly; DC-DC converter; power drive unit capacitor; high voltage cable; hybrid battery
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1445
- Description: Bypass Control Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; bypass resistor; DC-DC converter; motor power inverter module; bypass contactor; motor control (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Bypass contactor malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1446
- Description: Hybrid Battery Pack — Individual Voltage Input Deviation
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1447
- Description: Hybrid Battery Pack Deviation
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: hybrid battery pack
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1448
- Description: Battery Module Overheating
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack cooling fan; MCM programming; MCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Hybrid battery pack cooling — malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1449
- Description: Battery Cell Overheating; Battery Module Individual Voltage Input Deviation; Battery Module Deterioration; Battery Module Deviation
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: hybrid battery pack (per ninjafix.in)
- Diagnostic notes: bulletin lists four detection items under P1449. ninjafix.in lists P1449 as "Hybrid battery pack — deterioration".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1454
- Description: Fuel Tank Pressure (FTP) Sensor Range/Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; blockage in EVAP canister/filter/vent hoses/drain joint or FTP sensor air tube; EVAP canister vent shut-off valve; fuel tank (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Fuel tank pressure sensor — circuit range/performance"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list; justanswer Honda technician thread (2011 Pilot EVAP codes) references P1454 as EVAP system pressure sensor code

## P145C
- Description: Evaporative Emission (EVAP) Canister Purge System — Incorrect Flow
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; hose leak/blockage; EVAP canister purge valve; mechanical fault; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1460
- Description: Fuel Level Sensor Power Supply Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1505
- Description: Positive Crankcase Ventilation (PCV) Air Leakage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: vacuum leaks; PCV valve; EVAP canister purge valve; throttle body; intake manifold (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Intake system — leak detected"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1514
- Description: Throttle Position (TP) Sensor / Mass Air Flow (MAF) Sensor — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; TP sensor; MAP sensor; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1515
- Description: Throttle Command / Actual Throttle Position — Signal Variation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; throttle valve sticking; throttle control unit; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1516
- Description: Throttle Position Motor — Position Performance
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: throttle valve tight/sticking; TP sensor; wiring; throttle control unit; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1522
- Description: Brake Booster Pressure Sensor Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Brake booster pressure sensor — circuit malfunction, low voltage"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1523
- Description: Brake Booster Pressure Sensor Circuit High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Brake booster pressure sensor — circuit malfunction, high voltage"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1524
- Description: Brake Booster Pressure Sensor Range/Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Brake booster pressure sensor — range/performance problem"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1541
- Description: Climate Control Unit Signal Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; heater control panel; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Passenger compartment heater standby signal circuit — low input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1542
- Description: Climate Control Unit Signal Circuit High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; heater control panel; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Passenger compartment heater standby signal circuit — high input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1549
- Description: Generator System — High Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; generator; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1553
- Description: Hybrid Battery Pack Temperature Sensor 1 — Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1554
- Description: Hybrid Battery Pack Temperature Sensor 1 — Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1555
- Description: Hybrid Battery Pack Temperature Sensor 2 — Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1556
- Description: Hybrid Battery Pack Temperature Sensor 2 — Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1557
- Description: Hybrid Battery Pack Temperature Sensor 3 — Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1558
- Description: Hybrid Battery Pack Temperature Sensor 3 — Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1559
- Description: Motor Commutation Sensor A — Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); motor commutation sensor; drive plate sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1560
- Description: Motor Commutation Sensor A — Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); motor commutation sensor; drive plate sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1561
- Description: Motor Commutation Sensor B — Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor commutation sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1562
- Description: Motor Commutation Sensor B — Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor commutation sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1563
- Description: Motor Commutation Sensor C — Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor commutation sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1564
- Description: Motor Commutation Sensor C — Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor commutation sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1565
- Description: Motor Commutation Signal Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); motor commutation sensor; MCM (per ninjafix.in)
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1566
- Description: Motor Commutation Sensor — Signal Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1567
- Description: Cylinder Position Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1568
- Description: Battery Module Individual Voltage Input Problem; Battery Module Temperature Signal Circuit Problem; Battery Cell Temperature Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; battery condition monitor module; hybrid battery pack (per ninjafix.in)
- Diagnostic notes: bulletin lists three detection items under P1568. ninjafix.in variant wording: "Battery cell — temperature signal circuit malfunction".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1569
- Description: Battery Cell — Temperature Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1570
- Description: Hybrid Battery Pack — Individual Voltage Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1571
- Description: Motor Commutation Sensor — Voltage Input Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1572
- Description: Motor Drive Module (MDM) Temperature Signal Circuit Low Input; Motor Drive Module (MDM) Temperature Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; voltage converter module; motor power inverter module; motor control module (MCM) (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1572 (low/high input). ninjafix.in variant wording: "Motor driver module — temperature signal circuit high".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1573
- Description: DC-DC Converter — Temperature Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); DC-DC converter
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1574
- Description: Hybrid Battery Pack — Temperature Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1575
- Description: Motor Power Inverter Module — Voltage Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; high voltage contactor; hybrid battery pack; motor control module (MCM)
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1576
- Description: Motor Drive Module (MDM) Voltage Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; motor power inverter module; voltage converter module; battery condition monitor module; high voltage contactor (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor driver module — voltage malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1577
- Description: High Voltage Detection Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); hybrid battery pack (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "High voltage detection signal — circuit problem"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1580
- Description: Battery Current Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; battery current sensor; MCM programming; MCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Battery current sensor — circuit malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1581
- Description: Motor Power Inverter (MPI) Module Current Signal Circuit Low Input; Motor Power Inverter (MPI) Module Current Signal Circuit High Input; Motor Power Inverter (MPI) Module Current Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module; hybrid battery pack; MCM programming (per ninjafix.in)
- Diagnostic notes: bulletin lists three detection items under P1581. ninjafix.in variant wording: "Motor power inverter module — current signal circuit problem".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1582
- Description: Motor Current U Phase Signal Circuit Low Input; Motor Current U Phase Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); motor current U phase sensor (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1582 (low/high input)
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1583
- Description: Motor Current V Phase Signal Circuit Low Input; Motor Current V Phase Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); motor current V phase sensor (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1583 (low/high input)
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1584
- Description: Motor Current W Phase Signal Circuit Low Input; Motor Current W Phase Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1584 as "Brake fluid pressure sensor B — circuit low voltage". The Honda bulletin (A-grade) assigns P1584 to the motor-current W-phase circuit; the bulletin definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1585
- Description: Motor Current Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1585 as "Brake fluid pressure sensor B — circuit range/performance problem". The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1586
- Description: Motor Power Inverter (MPI) Module Current Signal / Battery Current Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1586 as "Brake fluid pressure sensor A/B — circuit malfunction". The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1587
- Description: Motor Power Inverter Module — Current Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor power inverter
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1588
- Description: Motor Power Inverter Module — Current Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor power inverter
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1589
- Description: Motor Power Inverter Module — Current Signal Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: motor power inverter module current sensor; MCM programming; MCM; motor power inverter
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1590
- Description: Motor Current U Phase Signal Circuit — Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor current U phase
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1591
- Description: Motor Current U Phase Signal Circuit — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor current U phase
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1593
- Description: Motor Current V Phase Signal Circuit — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor current V phase
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1594
- Description: Motor Current W Phase Signal Circuit — Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor current W phase
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1595
- Description: Motor Current W Phase Signal Circuit — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM programming; MCM; motor current W phase
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A0
- Description: Motor Driver Module — Temperature Signal Circuit Low
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; voltage converter module; motor power inverter module; motor control module (MCM)
- Diagnostic notes: source renders as "P15AO"; normalized to P15A0 (hex digit) for consistency with the P15Ax family
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A1
- Description: Motor Driver Module — Temperature Signal Circuit High
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; voltage converter module; motor power inverter module; motor control module (MCM)
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A2
- Description: Motor Driver Module — Voltage Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); voltage converter module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A3
- Description: Motor Driver Module — Voltage Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; voltage converter module; motor power inverter module; motor control module (MCM)
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A4
- Description: A/C Compressor Driver — Relay Stays Activated
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; A/C compressor driver; motor power cable; A/C compressor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A5
- Description: Motor Current Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor rotor calibration; U/V/W phase motor current sensors; motor power inverter module; motor power cable; motor control
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A6
- Description: U Phase Motor Current Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; U phase motor current sensor; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A7
- Description: V Phase Motor Current Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; V phase motor current sensor; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15A8
- Description: W Phase Motor Current Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; W phase motor current sensor; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AA
- Description: Motor Rotor — Position Not Learned
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor rotor position sensor
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AB
- Description: Engine Mounting Control Module — Power Supply Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AC
- Description: Engine Mounting Control Module — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AD
- Description: Engine Mounting Control Module — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AE
- Description: Cylinder Pause Signal Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15AF
- Description: Camshaft Position (CMP) Sensor — Signal Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15B0
- Description: Crankshaft Position (CKP) Sensor — Signal Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module; ECM programming; ECM
- Diagnostic notes: source renders as "P15BO"; normalized to P15B0 (hex digit) for consistency with the P15Bx family
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15B1
- Description: Camshaft Position (CMP) Sensor / Crankshaft Position (CKP) Sensor — Signal Correlation
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15B2
- Description: Brake Fluid Pressure Sensor A — Circuit Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; brake fluid pressure sensor; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P15B3
- Description: Brake Fluid Pressure Sensor A — Circuit Range/Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; brake fluid pressure sensor; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1600
- Description: Integrated Motor Assist System Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: other integrated motor assist codes stored
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1601
- Description: Integrated Motor Assist — System Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: other integrated motor assist codes stored
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1605
- Description: CAN Data Bus
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1606
- Description: Integrated Motor Assist Controller Area Network Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1608
- Description: ECM Internal Circuit Failure B
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1608 as "ECM — internal integrated motor assist controller area network — communication circuit malfunction". The 5 Star Auto Repair definition (paired with P1607 "ECM/PCM Internal Circuit Failure A") is used here; both sources are single-source for this code.
- Grade: [B]
- Evidence: 5 Star Auto Repair Honda check-engine-light code list (reputable DTC database); freeautomechanic.com Honda OBD II codes concurs

## P1618
- Description: Engine Control Module (ECM) — Internal Fault
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1625
- Description: Engine Control Module (ECM) — Unexpected Reset
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: interference from non-standard electronics; erase trouble code and re-test
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1629
- Description: Battery Current Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM) programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1630
- Description: Transmission Control Module
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: TCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Transmission control module (TCM) processor error"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1633
- Description: Engine Control Module (ECM) Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM) programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1634
- Description: Motor Power Inverter Module — Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module; motor control module (MCM) relay 2; fuse; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1635
- Description: Battery Condition Monitor (BCM) Module Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; battery condition monitor module (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Battery condition monitor module — malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1636
- Description: Motor Power Inverter Module — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor power inverter module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1637
- Description: Motor Control Module (MCM) — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: motor control module (MCM) programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1638
- Description: Motor Control Module (MCM) — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1639
- Description: MOTB Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor control module (MCM) — signal circuit malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1640
- Description: ACTTRQ Motor Torque Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor torque signal circuit — low input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1641
- Description: ACTTRQ Motor Torque Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor torque signal circuit — high input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1642
- Description: QBATT Battery Signal Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Battery signal circuit — low input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1643
- Description: QBATT Battery Signal Circuit High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Battery signal circuit — high input"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1644
- Description: MOTFSA Signal Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1645
- Description: MOTFSB Signal Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1646
- Description: MOTSTB Signal Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1647
- Description: Power Command Signal Circuit Low Input; Power Command Signal Circuit High Input; Engine Torque Signal Circuit Low Input; Engine Torque Signal Circuit High Input; Mode Signal Circuit 1 Low Input; Mode Signal Circuit 1 High Input; Mode Signal Circuit 2 Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM (per ninjafix.in, which lists P1647 only as "Engine speed signal — circuit problem")
- Diagnostic notes: bulletin lists eight detection items under P1647 (two each for power command, engine torque, mode signal 1, plus mode signal 2 problem and engine speed signal circuit problem). ninjafix.in splits several of these into separate codes (P1685/P1686 engine torque, P1689 mode signal 2, P16B3/P16B4 power command, P16B7/P16B8 mode signal 1) — likely a newer model-year split; both attributions are recorded, not reconciled.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1648
- Description: Engine Speed Signal Circuit Problem; Battery Condition Monitor (BCM) Module Communication Signal Circuit Problem
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM; battery condition monitor module (per ninjafix.in)
- Diagnostic notes: bulletin lists two detection items under P1648. ninjafix.in variant wording: "Motor control module (MCM) — communication signal circuit problem".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1650
- Description: Engine Control Module Quad Driver / Output Driver
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; EVAP canister purge valve; intake manifold air control solenoid
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1658
- Description: Electronic Throttle System (ETS) Control Relay — On Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ETS control relay; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1659
- Description: Electronic Throttle System (ETS) Control Relay — Off Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; fuse; ETS control relay; underhood fusebox/relay plate; ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P165B
- Description: Electronic Throttle System (ETS) Relay — Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; ETS relay; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1671
- Description: A/T FI Data Line No Signal
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com)

## P1672
- Description: A/T FI Data Line Failure
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com)

## P1673
- Description: Motor Control Module (MCM) — Relay Stays Activated
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; MCM relay 1; MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1677
- Description: Traction Control System FI Data Line Failure
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com)

## P1679
- Description: RSCD Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in concurs ("RSCD Signal Circuit Malfunction", no causes listed)
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1683
- Description: Throttle Valve Default Position Spring Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; dirty throttle body; throttle body (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Throttle valve — default position spring performance problem"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1684
- Description: Throttle Valve Return Spring Performance Problem
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; dirty throttle body; throttle body (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "Throttle valve — return spring performance problem"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1685
- Description: Engine Torque Signal — Circuit Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: not in Honda SB 03-020 (which assigns engine-torque low/high to P1647 sub-items); likely a newer split — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

> **INTEGRATOR NOTE — P1686 upgrade (not a new code):** P1686 is already in the
> v1.2.1 database as "Automatic Transaxle FI Signal B Low Input" [C]
> (single-transcription evidence). This pass found the A-grade definition in
> Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors"
> (2003-03-29): "A/T FI Signal B Circuit Low Voltage". Recommended: upgrade the
> existing P1686 entry's description/evidence/grade to [A] with evidence
> "Honda Service Bulletin 03-020 (2003-03-29), detection-item list". CONFLICT
> noted: ninjafix.in lists P1686 as "Engine torque signal — circuit high
> input"; the bulletin (A-grade) definition is used; the alternative likely
> reflects the newer P1647-sub-item split (see P1647/P1685 notes).

## P1689
- Description: Mode Signal Circuit 2
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: not in Honda SB 03-020 (which assigns mode signal circuit 2 problem to a P1647 sub-item); likely a newer split — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1690
- Description: Traction Control System STB Line Failure
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Traction Control System Circuit Failure"
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com); ninjafix.in concurs on meaning

## P1696
- Description: Traction Control Fuel Cut Signal Low Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Traction Control System Voltage Low"
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com)

## P1697
- Description: Traction Control Fuel Cut Signal High Input
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant wording: "Traction Control System Voltage High"
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (5 Star Auto Repair; freeautomechanic.com)

## P16B3
- Description: Power Command Signal Circuit — Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: source renders "signaf" (typo for "signal"); likely a newer split of the P1647 sub-items — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16B4
- Description: Power Command Signal Circuit — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: likely a newer split of the P1647 sub-items — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16B7
- Description: Mode Signal Circuit 1 — Low Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: likely a newer split of the P1647 sub-items — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16B8
- Description: Mode Signal Circuit 1 — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; motor control module (MCM); ECM
- Diagnostic notes: likely a newer split of the P1647 sub-items — see P1647 notes
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16BA
- Description: Battery Cell — High Input
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; battery condition monitor module; hybrid
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16BB
- Description: Generator System — Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; generator; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16BC
- Description: Generator System — Low Voltage
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; generator; ECM
- Diagnostic notes: source lists P16BB and P16BC with identical descriptions; treated as listed, possible transcription duplication
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C0
- Description: ECM — Programming Error
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C1
- Description: Motor Control Module (MCM) — Program Not Installed — Battery Condition Monitor Module Program
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: MCM programming; MCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C3
- Description: DC-DC Converter Temperature Sensor — Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: wiring; blocked hybrid battery pack cooling fan duct; hybrid battery pack cooling fan; DC-DC converter
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C4
- Description: Engine Mounting Control Actuator — Power Supply Circuit Stuck Off
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; fuse; engine mounting control relay; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C5
- Description: Engine Mounting Control Actuator — Power Supply Circuit Stuck On
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control relay; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C6
- Description: Engine Mounting Control Actuator — High Voltage During Function Test
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module; front, rear engine mountings
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C7
- Description: Rear Engine Mounting Actuator Control Circuit — High Current
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C8
- Description: Front Engine Mounting Actuator Control Circuit — High Current
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16C9
- Description: Engine Mounting Control Module — Internal Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; engine mounting control module
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16D5
- Description: CAN Data Bus
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16D6
- Description: Integrated Motor Assist Controller Area Network Malfunction
- Category: P
- Scope: manufacturer (Honda) — IMA hybrid
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P16D7
- Description: ECM — CAN Data Bus — Communication Circuit Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: ECM programming; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1709
- Description: Problem in Transmission Gear Selection Switch Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; mode switch; TCM (per ninjafix.in)
- Diagnostic notes: freeautomechanic.com lists P1709 only as "Automatic Transmission System Malfunction". ninjafix.in variant wording: "AT — Sport shift mode malfunction". The bulletin definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in and freeautomechanic.com Honda lists

## P1710
- Description: First Hold Switch Circuit Fault Stuck On
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1717
- Description: AT — Gear Selection Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; range position switch; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1730
- Description: Problem in Shift Control System — Shift Solenoid Valve A and D Stuck OFF, Shift Solenoid Valve B Stuck ON, Shift Valves A, B, and D Stuck
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: transmission fluid; wiring (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AT — gear shift malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1731
- Description: Problem in Shift Control System — Shift Solenoid Valve E Stuck ON, Shift Valve E Stuck
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: transmission fluid; wiring; shift solenoid E; A/T clutch pressure control solenoid A; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AT — gear shift malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1732
- Description: A/T Clutch Pressure Control Solenoid Valve A Stuck OFF
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in lists P1732 only as "Problem In Shift Control System"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1733
- Description: Problem in Shift Control System — Shift Solenoid Valve B and C Stuck ON, Shift Valves B and C Stuck
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: transmission fluid; wiring; shift solenoid D; A/T clutch pressure control solenoid C; ECM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AT — gear shift malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1734
- Description: Problem in Shift Control System — Shift Solenoid Valve D Stuck ON, Shift Valve D Stuck
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: transmission fluid; wiring (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "AT — gear shift malfunction"
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1740
- Description: Problem in 2nd Clutch Pressure Switch Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1740 as "AT — 4th clutch pressure switch" (wiring; range position switch; 4th clutch pressure switch; ECM). The Honda bulletin (A-grade) positional mapping gives 2nd clutch pressure switch circuit; the bulletin definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1750
- Description: Problem in 3rd Clutch Pressure Switch Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1750 as "AT — hydraulic system mechanical malfunction" (wiring; shift solenoids; ECM; transmission mechanical fault). The Honda bulletin (A-grade) positional mapping gives 3rd clutch pressure switch circuit; the bulletin definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1751
- Description: Problem in 4th Clutch Pressure Switch Circuit; Mechanical Problem in Hydraulic Control System of Shift Solenoid Valve B and A/T Clutch Pressure Control Solenoid Valves A and B
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: bulletin lists P1751 twice with two detection items (4th clutch pressure switch circuit; mechanical/hydraulic problem). CONFLICT: ninjafix.in lists P1751 as "AT — hydraulic system mechanical malfunction" only.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1778
- Description: Clutch Pressure Control Solenoid Valve 'C' Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1787
- Description: Automatic Transmission Lock-Up Clutch Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1794
- Description: Automatic Transaxle Concerns
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: ninjafix.in variant (V6): "Automatic transmission — BARO signal" (wiring; ECM; TCM)
- Grade: [B]
- Evidence: two independent Honda DTC lists agree (scribd Honda OBD-II Error Codes list; freeautomechanic.com Honda OBD II codes)

## P1835
- Description: AT — Kick-Down Switch
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; kick-down switch; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1850
- Description: AT — Brake Band Solenoid Malfunction
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: AT trouble code(s) stored
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1860
- Description: AT — Torque Converter Clutch (TCC) Solenoid Circuit
- Category: P
- Scope: manufacturer (Honda)
- Possible causes: wiring; TCC solenoid; ECM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1870
- Description: Manifold Absolute Pressure Sensor Circuit
- Category: P
- Scope: manufacturer (Honda) — TCM context
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1870 as "CVT — poor acceleration" (wiring; shift control linear solenoid; TCM); Honda DTC lists (troublecodes.net Honda list; freeautomechanic.com) list it only as "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here. (GM uses P1870 for transmission component slipping — different make, not applicable.)
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1873
- Description: Problem in CVT Speed Change Control Valve Assembly Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1873 as "CVT — poor acceleration" (wiring; PH-PL control linear solenoid; TCM); Honda DTC lists give only "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1876
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1877
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1878
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; start clutch control linear solenoid; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1879
- Description: Problem in CVT Pulley Pressure Control Valve Assembly Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1879 as "CVT — poor acceleration" (wiring; start clutch control linear solenoid; TCM); Honda DTC lists give only "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1880
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; start clutch control linear solenoid; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1881
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; start clutch control linear solenoid; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1882
- Description: Problem in CVT Start Clutch Pressure Control Valve Assembly Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1882 as "Constantly variable transmission (CVT)" (wiring; inhibitor solenoid; TCM). The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1884
- Description: Problem in Inhibitor Solenoid Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: not documented
- Diagnostic notes: CONFLICT: ninjafix.in lists P1884 as "Secondary Gear Speed Sensor 2 Circuit Malfunction". The Honda bulletin (A-grade) definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list

## P1888
- Description: CVT Driven Pulley Speed Sensor Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; speed sensor 1; TCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "CVT — poor acceleration" (speed sensor 1). Honda DTC lists give only "Automatic Transaxle Concerns".
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1889
- Description: CVT Speed Sensor
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; speed sensor 2; TCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "CVT — poor acceleration" (speed sensor 2)
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1892
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1893
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1895
- Description: CVT Speed Change Control Valve Circuit
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM (per ninjafix.in)
- Diagnostic notes: ninjafix.in variant wording: "CVT — poor acceleration" (drive pulley pressure control valve). The bulletin definition is used here.
- Grade: [A]
- Evidence: Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list; corroborated by ninjafix.in Honda fault code list

## P1896
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1897
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1898
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

## P1899
- Description: CVT — Poor Acceleration
- Category: P
- Scope: manufacturer (Honda) — CVT
- Possible causes: wiring; drive pulley pressure control valve; TCM
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: ninjafix.in Honda fault code list (single source)

---

## Honda blink-code systems

Honda SRS, ABS, and VSA modules historically report proprietary blink codes
rather than standard B1xxx/C1xxx OBD-II codes. Codes are read by shorting the
SCS (service check signal) connector — special tool 07PAZ-0010100 or a jumper
(pins 4 and 9 of the DLC on many models) — with the ignition on, then counting
flashes of the SRS/ABS indicator: long blinks = main code, short blinks =
sub-code (e.g., 1 long + 2 short = 1-2). No B1xxx/C1xxx equivalents are
invented here; the blink code IS the entry.

### SRS blink codes

Base chart: Honda 1988–2002 / Acura 1995–2002 SRS DTC information, via the
honda-tech.com "Complete SRS code list" technician transcription. 1999–2002
and 2003–2011 charts refine sub-code splits and add side-impact/OPDS/buckle-
tensioner families; refinements are noted per entry. The 5-x through 8-x
internal-failure grouping is corroborated by Honda service documentation
(justanswer Honda technician thread, 2001 Civic).

## SRS blink 1-1, 1-2
- Description: Open or high resistance in driver's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: open in driver's airbag inflator circuit; faulty cable reel; faulty SRS unit
- Diagnostic notes: read via SCS connector short, count SRS light flashes; main-code 1-x = driver airbag inflator faults
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription); justanswer Honda technician threads agree 1-1/1-2 = driver inflator open/high resistance

## SRS blink 1-3
- Description: Short to another wire or low resistance in driver's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 1-4
- Description: Short to power in driver's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 1-5
- Description: Short to ground in driver's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 2-1, 2-2
- Description: Open in passenger's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: main-code 2-x = passenger airbag inflator faults
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 2-3
- Description: Short to another wire or low resistance in passenger's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 2-4
- Description: Short to power in passenger's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 2-5
- Description: Short to ground in passenger's airbag inflator
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 3-1, 3-2
- Description: Open or high resistance in driver's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: main-code 3-x = driver's seat belt tensioner faults
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 3-3
- Description: Short to another wire or low resistance in driver's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 3-4
- Description: Short to power in driver's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 3-5
- Description: Short to ground in driver's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 4-1, 4-2
- Description: Open or high resistance in front passenger's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: main-code 4-x = front passenger's seat belt tensioner faults
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 4-3
- Description: Short to another wire or low resistance in passenger's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 4-4
- Description: Short to power in passenger's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 4-5
- Description: Short to ground in passenger's seat belt tensioner
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 5-x through 8-x (internal failure group)
- Description: Internal failure of SRS unit — sub-codes 5-1, 5-2, 5-3, 5-4, 5-5, 5-8, 6-1, 6-2, 6-3, 6-4, 6-5, 6-6, 6-7, 6-8, 7-1, 7-2, 7-3, 8-1, 8-2, 8-3, 8-4, 8-5, 8-6, 8-7, 8-8
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty SRS unit; low battery/system voltage can set these spuriously
- Diagnostic notes: Honda service documentation procedure: check battery/charging-system voltage FIRST — if low, repair charging system before SRS troubleshooting; a dead/discharged battery can trigger these. Clear the code; if it returns, the SRS unit needs replacement. Sub-code coverage varies slightly by chart: 1999–2002 Honda chart lists 5-1, 5-2, 5-4, 5-5, 5-8, 6-1…6-8, 7-1, 7-2, 7-3, 8-1, 8-2, 8-5, 8-6, 8-7, 8-8; Civic/CR-V/Element/Ridgeline chart lists the full 5-1…8-8 set; 2001 Civic Honda service documentation lists 5-1, 5-2, 5-3, 5-4, 5-5, 5-8, 6-1, 6-2, 6-3, 6-4, 6-7, 6-8, 7-1, 7-2, 7-3, 8-1…8-8.
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription); Honda service repair documentation quoted by Honda technicians (justanswer 2001 Civic SRS thread) corroborates the internal-failure grouping and the battery-voltage-first procedure

## SRS blink 9-1
- Description: SRS failure or indicator light fault
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999–2002 charts word this as "Intermittent SRS failures"; 2003–2011 Civic/CR-V chart: "SRS failure or indicator light"
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 9-2
- Description: SRS unit internal failure of power supply
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty SRS power supply
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 9-3
- Description: Faulty driver's seat belt buckle switch
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 9-4
- Description: Faulty passenger's seat belt buckle switch
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 9-6
- Description: Faulty left-hand front impact sensor
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 2003–2011 Civic/CR-V/Element/Ridgeline chart only; no 9-5 exists in any chart found — 9-x jumps from 9-4 to 9-6
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 9-7
- Description: Faulty right-hand front impact sensor
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 2003–2011 Civic/CR-V/Element/Ridgeline chart only
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 10-1
- Description: SRS air bag deployed
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: airbag(s)/tensioner(s) deployed in a collision — SRS unit must be replaced after deployment
- Diagnostic notes: 1999–2002 Acura chart splits deployment codes: 10-1 seat belt pretensioner deployed; 10-2 driver's side air bag deployed; 10-3 pretensioner & driver's side air bag deployed; 10-4 passenger's side air bag deployed; 10-5 pretensioner & passenger's side air bag deployed; 10-6 driver & passenger air bags deployed; 10-7 all deployed. 2003–2011 charts use D1-11/F1-11 style deployment codes instead.
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 10-3
- Description: Seat belt pretensioner and driver's side air bag deployed
- Category: B
- Scope: manufacturer (Acura) — blink-code scheme, 1999–2002 models
- Possible causes: airbag/tensioner deployed in a collision — SRS unit must be replaced
- Diagnostic notes: from the 1999–2002 Acura deployment sub-code split (see 10-1 notes); Honda 1988–2002 chart lists only 10-1
- Grade: [B]
- Evidence: Acura SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 11-1, 11-2
- Description: Open or high resistance in driver's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: main-code 11-x = driver's side airbag module faults (1999+ charts)
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 11-3
- Description: Short to another wire or low resistance in driver's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 11-4
- Description: Short to power in driver's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 11-5
- Description: Short to ground in driver's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 12-1, 12-2
- Description: Open or high resistance in front passenger's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: main-code 12-x = passenger's side airbag module faults (1999+ charts)
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 12-3
- Description: Short to another wire or low resistance in passenger's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 12-4
- Description: Short to power in passenger's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 12-5
- Description: Short to ground in passenger's side airbag module
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 13-1 through 13-5
- Description: Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 14-1 through 14-5
- Description: Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999+ charts
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 15-1
- Description: Faulty OPDS unit (occupant position detection system)
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999+ charts; some charts add "or OPDS not initialized"
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 15-2
- Description: Faulty side airbag cutoff indicator circuit
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 15-3
- Description: Faulty OPDS sensor
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 21-1, 21-3, 21-4, 21-5
- Description: Driver's seat belt buckle tensioner faults — 21-1 open/high resistance; 21-3 short to another wire/low resistance; 21-4 short to ground; 21-5 short to power
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999+ charts; the original poster of the honda-tech thread traced a 21-2 to a seat belt tensioner recall fix
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

## SRS blink 22-1, 22-3, 22-4, 22-5
- Description: Passenger's seat belt buckle tensioner faults — 22-1 open/high resistance; 22-3 short to another wire/low resistance; 22-4 short to ground; 22-5 short to power
- Category: B
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: 1999+ charts
- Grade: [B]
- Evidence: Honda SRS DTC chart (via honda-tech.com technician transcription)

### ABS blink codes

Base: Honda brake-system troubleshooting guide DTC detection index (service-manual
excerpt, page 19B references) corroborated by the Acura 3.5 RL service manual
troubleshooting index (ManualsLib) and Honda owner forums (s2ki, thehondaforums
CR-V ABS thread). Read by jumping the ABS service check connector and counting
ABS light flashes (long = tens, short = ones).

## ABS blink 11, 13, 15, 17
- Description: Wheel sensor — open, short to body ground, or short to power (11 = right-front, 13 = left-front, 15 = right-rear, 17 = left-rear)
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty wheel sensor; wiring open/short
- Diagnostic notes: ABS indicator stays on until ignition off for these codes. Corroborated by CR-V owner thread: 15 = right rear wheel sensor, 17 = left rear wheel sensor, 54 = fail-safe relay.
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib); thehondaforums.com CR-V ABS thread

## ABS blink 12, 14, 16, 18
- Description: Wheel sensor — electrical noise / intermittent interruption (12 = right-front, 14 = left-front, 16 = right-rear, 18 = left-rear)
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty wheel sensor pulse signal; damaged pulser ring; electrical noise
- Diagnostic notes: corroborated by s2ki S2000 thread: 12 = faulty right front wheel sensor pulse signal, 14 = left front, 16 = right rear, 18 = left rear
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib); s2ki.com S2000 ABS thread

## ABS blink 21, 22, 23, 24
- Description: Pulser — 21 = right-front, 22 = left-front, 23 = right-rear, 24 = left-rear
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 31–38
- Description: Solenoid (short to body ground / short to wire)
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: individual solenoid (inlet/outlet per wheel) assignment not documented in sources found
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 41–44
- Description: Wheel lock
- Category: C
- Scope: manufacturer (Acura) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: listed in the Acura 3.5 RL manual index; not present in the Honda brake-guide excerpt found
- Grade: [A]
- Evidence: Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 51
- Description: Motor lock
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 52
- Description: Motor stuck OFF
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 53
- Description: Motor stuck ON
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 54
- Description: ABS fail-safe relay
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty fail-safe relay
- Diagnostic notes: corroborated by CR-V owner thread (code 54 = fail-safe relay, often set alongside wheel-sensor codes)
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib); thehondaforums.com CR-V ABS thread

## ABS blink 61
- Description: Low IG1 voltage
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: low battery/system voltage
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd); Acura 3.5 RL service manual troubleshooting index (ManualsLib)

## ABS blink 62
- Description: High IG1 voltage
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: charging system overvoltage
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd)

## ABS blink 81
- Description: Central Processing Unit (CPU) diagnosis; ROM/RAM diagnosis
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme
- Possible causes: faulty ABS control unit
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Honda brake system troubleshooting guide (service-manual excerpt via scribd)

### VSA blink codes (newer main–sub format)

2000s Honda VSA systems report main-code/sub-code pairs (e.g., 11-19) via the
ABS/VSA indicator. Main-code wheel assignments DIFFER BY MODEL/GENERATION —
verify against the model-specific service manual. The entries below are from a
2009 Civic case (Honda master technician) unless noted.

## VSA blink 11-19
- Description: Right front wheel speed sensor malfunction
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme (2009 Civic)
- Possible causes: faulty wheel speed sensor; damaged wiring
- Diagnostic notes: CONFLICT: a 2006 Odyssey case reports 11-1 as a LEFT REAR wheel speed sensor fault — main-code wheel assignment varies by model/generation; do not generalize across models
- Grade: [C]
- Evidence: justanswer Honda thread (2009 Civic ABS/SRS lights; Honda master technician Anthony P.)

## VSA blink 13-19
- Description: Left front wheel speed sensor malfunction
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme (2009 Civic)
- Possible causes: faulty wheel speed sensor; damaged wiring
- Diagnostic notes: model-specific; see 11-19 conflict note
- Grade: [C]
- Evidence: justanswer Honda thread (2009 Civic ABS/SRS lights; Honda master technician Anthony P.)

## VSA blink 54-3
- Description: Relay 1 stuck on
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme (2009 Civic)
- Possible causes: faulty VSA relay
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: justanswer Honda thread (2009 Civic ABS/SRS lights; Honda master technician Anthony P.)

## VSA blink 61-1
- Description: Modulator control unit initial IG low voltage
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme (2009 Civic)
- Possible causes: low battery/system voltage; wiring
- Diagnostic notes: a 2012 Pilot case reports 61-11 alongside wheel-sensor codes with similar low-voltage context
- Grade: [C]
- Evidence: justanswer Honda thread (2009 Civic ABS/SRS lights; Honda master technician Anthony P.)

## VSA blink 86-1
- Description: F-CAN bus-OFF malfunction
- Category: C
- Scope: manufacturer (Honda) — blink-code scheme (2009 Civic)
- Possible causes: CAN wiring fault; faulty module pulling the bus down
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: justanswer Honda thread (2009 Civic ABS/SRS lights; Honda master technician Anthony P.)

---

## U-codes (network) — new in v1.4.0

## U1280
- Description: B-CAN Communication Bus Line Error (BUS-OFF)
- Category: U
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: Honda DTC troubleshooting procedure: clear with HDS, cycle OFF→ON, wait 6+ seconds, recheck; if indicated, go to BCM DTC U1280 troubleshooting (intermittent otherwise). Flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight.
- Grade: [A]
- Evidence: Honda DTC troubleshooting document for U1280 (via laboratoryb.org); American Honda Interactive Network message "2018-2020 Accord/Insight MIL On w/ BCM DTCs in Active Fault" (via oemdtc.com NHTSA filing)

## U1281
- Description: Auto Light Control Unit Lost Communication with MICU (Body Control Module)
- Category: U
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight
- Grade: [B]
- Evidence: American Honda Interactive Network message "2018-2020 Accord/Insight MIL On w/ BCM DTCs in Active Fault" (via oemdtc.com NHTSA filing)

## U128D
- Description: Auto Light Control Unit Lost Communication with MICU (Body Control Module)
- Category: U
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: listed alongside U1281 with near-identical wording in the Honda message; treated as listed
- Grade: [B]
- Evidence: American Honda Interactive Network message "2018-2020 Accord/Insight MIL On w/ BCM DTCs in Active Fault" (via oemdtc.com NHTSA filing)

## U1291
- Description: BCM Lost Communication with Relay Control Module
- Category: U
- Scope: manufacturer (Honda)
- Possible causes: not documented
- Diagnostic notes: flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight
- Grade: [B]
- Evidence: American Honda Interactive Network message "2018-2020 Accord/Insight MIL On w/ BCM DTCs in Active Fault" (via oemdtc.com NHTSA filing)

---

## Coverage notes

### Deliberately excluded (duplicates or out-of-scope)
- **P2xxx targets are NOT included**: every P2xxx on the target list (P2100s, P2120s,
  P2135, P2138, P2176–P2196, P2227–P2229, P2237–P2245, P2270/P2271, P2626, P2650s,
  P2A00) was verified present in the v1.2 generic catalog (e.g., P2119, P2122,
  P2123, P2127, P2128, P2135, P2138, P2176, P2185, P2195, P2197, P2227–P2229,
  P2237–P2255, P2270, P2279, P2413, P2422, P2552, P2626–P2631, P2769, P2770, P2A00,
  P2A03). Per this file's convention (SAE J2012 generic codes live in the generic
  catalog), they are excluded here. The same applies to U0156, U0164, U0198,
  U0199, U0073, U0107, U0121, and U0155 — all present in the generic catalog.
- **P1299 (Ford)**: Ford powertrain charts define P1299 as "Cylinder Head Over
  Temperature Protection Active" — a Ford code, not Honda. The Honda-specific
  P1299 (TP motor forced engine shutdown mode, [C]) IS included above with the
  cross-make conflict noted.
- **P1170–P1178**: diesel injection-pump codes from a generic multi-make
  compilation (injection pump rotor/cam-ring position sensors, fuel quantity
  adjuster) — no Honda attribution found; not included.
- **P1160/P1161**: no Honda definition found in any source (Honda SB 03-020 jumps
  P1159 → P1162; the only P1160/P1161 references found are Kenworth/Paccar
  heavy-duty codes). Not included.
- **U1208, U1220, U129D, U1600–U1602**: no Honda-specific definitions found.
  Generic EOBD compilations assign U1208/U1220 to J1850 "invalid/missing data"
  seat-switch/interior-lamp messages — not Honda-specific; not included. U129D
  was not found at all (the Honda TRS message lists U128D, a different code).
- **SRS blink 9-5**: does not exist in any chart found (9-x jumps 9-4 → 9-6).
  Not included.
- **B1xxx/C1xxx equivalents**: not invented, per the Honda blink-code quirk.

### Conflicts and thin areas worth flagging to the integrator
- **P1894**: v1.2.1 (micro-tronik, [C]) says "CVT Drive Pulley Pressure Control
  Valve Malfunction"; Honda SB 03-020 ([A]) says "Problem in Start Clutch System".
  The bulletin should win on grade, but the entry predates this research.
- **P1890**: v1.2.1 (Honda advanced diagnostics, Insight CVT, [A]) says "Problem
  in Shift Control System (CVT Speed Control System)"; SB 03-020 ([A]) maps P1890
  to "Problem in CVT Speed Sensor 2 Circuit" and P1891 to "Shift Control System".
  Genuine A-vs-A conflict — likely model/generation-dependent.
- **P1885**: v1.2.1 (Honda advanced diagnostics, Insight CVT, [A]) says CVT drive
  pulley speed sensor circuit; SB 03-020 ([A]) says "Secondary Gear Speed Sensor
  2 Circuit Malfunction". ninjafix.in agrees with v1.2.1. Another A-vs-A split.
- **P1647 sub-items vs newer split codes**: SB 03-020 packs eight IMA signal
  faults under P1647; ninjafix.in lists them as separate codes P1685/P1686
  (engine torque), P1689 (mode signal 2), P16B3/P16B4 (power command), P16B7/P16B8
  (mode signal 1). Both attributions are recorded; likely a model-year split.
- **P1738/P1739/P1740**: SB 03-020 positional mapping gives solenoid-stuck/clutch-
  pressure-switch-circuit definitions; ninjafix.in gives clutch-pressure-switch
  2/3/4. P1738/P1739 are already in v1.2.1 as generic "A/T concerns", so the
  conflict only bites the new P1740 entry — recorded inline.
- **P1584/P1585/P1586**: SB 03-020 (motor-current circuits) vs ninjafix.in (brake
  fluid pressure sensors). Bulletin wins on grade; conflict recorded inline.
- **P1608**: 5 Star ("ECM Internal Circuit Failure B") vs ninjafix.in ("ECM
  internal IMA CAN communication malfunction"). Recorded inline.
- **P1686**: SB 03-020 (A/T FI signal B low) vs ninjafix.in (engine torque high).
  Bulletin wins; conflict recorded inline.
- **VSA main-code wheel assignment** varies by model/generation (11-x = right
  front on 2009 Civic vs left rear on 2006 Odyssey). VSA entries are [C] and
  model-tagged; do not generalize.
- **Thin**: P-codes P1254–P1256, P1260–P1270, P1360, P1363–P1365, P1368–P1380,
  P1383–P1385, P1388–P1389, P1395–P1398, P1400–P1403, P1405, P1407–P1409,
  P1411–P1414, P1417–P1419, P1421–P1428, P1450–P1453, P1458, P1461–P1485,
  P1487–P1490, P1492–P1497, P1499–P1504, P1506–P1507, P1510–P1513, P1517–P1518,
  P1520–P1521, P1525–P1540, P1543–P1548, P1550–P1552, P1602–P1604, P1609–P1617,
  P1619–P1624, P1626–P1628, P1631–P1632, P1649, P1651–P1654, P1656–P1657,
  P1661–P1670, P1674–P1675, P1680, P1688, P1691–P1695, P1698–P1704, P1707–P1708,
  P1711–P1716, P1718–P1729, P1735–P1737, P1742–P1749, P1752, P1754–P1757,
  P1759–P1767, P1769–P1772, P1774–P1776, P1779–P1784, P1789, P1796–P1834,
  P1836–P1849, P1851–P1859, P1861–P1869, P1871–P1872, P1874–P1875, P1883, P1887 —
  no Honda source found for these numbers; they are likely unassigned, not just
  undocumented. They are omitted rather than invented.
- **ninjafix.in transcription quirks** (all [C]): P1114/P1115 near-identical;
  P16BB/P16BC identical; "P15AO"/"P15BO" normalized to P15A0/P15B0;
  "P1687 … signal 8" typo for "signal B"; P1387 wording slip noted inline.
