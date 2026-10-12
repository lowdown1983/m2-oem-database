# Volkswagen Group (VW / Audi / SEAT / Skoda) — Manufacturer-Specific DTCs

Research for the M2 OEM vehicle database (v1.2.1 expansion). Every factual claim
carries a quality grade: **A** = VAG service info/TSB · **B** = Ross-Tech wiki,
reputable DTC database, or multi-source agreement · **C** = single community
source. "not documented" means no source was found — nothing invented.

VAG quirk: VCDS/VAG tools report a 5-digit VAG fault code (e.g. 17884) alongside
the SAE P-code (e.g. P1476). Generic OBD-II tools show only the P-code, and some
VAG faults have NO P-code equivalent at all. The 5-digit form is recorded in
diagnostic notes for every code where the mapping was verified.

Research date: 2026-10-06.

---

## P-codes (powertrain, VAG-specific)

### O2 sensor circuits (P1101–P1110)

## P1101
- Description: O2 Sensor Circuit (Bank 1 Sensor 1) — Voltage Too Low / Air Leak
- Category: P
- Scope: manufacturer (VW)
- Possible causes: exhaust leak upstream of sensor; faulty O2 sensor; wiring fault
- Diagnostic notes: VAG 5-digit: 17509. CONFLICT: one community DTC list maps P1102 (not P1101) to this text — the 5-digit mapping here follows the VAG DTC table transcription.
- Grade: [C]
- Evidence: VAG DTC table transcription (archive-host PDF, single source)

## P1102
- Description: O2 Sensor Heater Circuit (Bank 1 Sensor 1) — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17510. CONFLICT: a second community list gives "O2S Heating Circuit Bank 1 Sensor 1 Voltage Too Low/Air Leak" for P1102 — the two sources disagree; 5-digit mapping follows the VAG DTC table transcription.
- Grade: [C]
- Evidence: VAG DTC table transcription; conflict with scribd VW fault-code list

## P1103
- Description: O2 Sensor Heater Circuit (Bank 1 Sensor 1) — Output Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17511
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1104
- Description: O2 Sensor Circuit (Bank 1 Sensor 2) — Voltage Too Low / Air Leak
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17512
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1105
- Description: O2 Sensor Heater Circuit (Bank 1 Sensor 2) — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17513
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1106
- Description: O2 Sensor Circuit (Bank 2 Sensor 1) — Voltage Too Low / Air Leak
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17514
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1107
- Description: O2 Sensor Heater Circuit (Bank 2 Sensor 1) — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17515
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1108
- Description: O2 Sensor Heater Circuit (Bank 2 Sensor 1) — Output Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17516
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1109
- Description: O2 Sensor Circuit (Bank 2 Sensor 2) — Voltage Too Low / Air Leak
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17517
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1110
- Description: O2 Sensor Heater Circuit (Bank 2 Sensor 2) — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17518
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1113
- Description: O2 Sensor Heater Resistance Too High (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: aging heater element; wiring resistance
- Diagnostic notes: From the community VW fault-code list; no 5-digit mapping verified.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1115
- Description: O2 Sensor Heater Circuit Short to Ground (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list; no 5-digit mapping verified.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1116
- Description: O2 Sensor Heater Circuit Open (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list; no 5-digit mapping verified.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1117
- Description: O2 Sensor Heater Circuit Short to Ground (Bank 1 Sensor 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list; no 5-digit mapping verified.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1118
- Description: O2 Sensor Heater Circuit Open (Bank 1 Sensor 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list; no 5-digit mapping verified.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

### Fuel trim (P1127–P1139)

## P1127
- Description: Long Term Fuel Trim — System Too Rich (Bank 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: leaking injector; excessive fuel pressure; faulty MAF over-reporting
- Diagnostic notes: VAG 5-digit: 17535. Check MVB 032 fuel trim values.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1128
- Description: Long Term Fuel Trim — System Too Lean (Bank 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: vacuum/intake leaks (unmetered air); MAF under-reporting (Ross-Tech notes the MAF may die slowly without setting a MAF code — 17536/P1128 is the classic symptom); exhaust leak ahead of O2 sensor; low fuel pressure
- Diagnostic notes: VAG 5-digit: 17536. Ross-Tech MAF tech tip: a dying MAF under-reports airflow and the ECU compensates lean — check MAF g/s against spec under load, not just at idle. WD-40/propane around intake joints to find vacuum leaks.
- Grade: [B]
- Evidence: VAG DTC table transcription + Ross-Tech MAF tech tip + technician Q&A agreement

## P1129
- Description: Long Term Fuel Trim — System Too Rich (Bank 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: Bank-2 counterpart of P1127. From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1130
- Description: Long Term Fuel Trim — System Too Lean (Bank 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: Bank-2 counterpart of P1128. From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1136
- Description: Long Term Fuel Trim Additive Fuel — System Too Lean (Bank 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: Additive (idle-range) trim variant. From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1137
- Description: Long Term Fuel Trim Additive Fuel — System Too Rich (Bank 1)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1138
- Description: Long Term Fuel Trim Additive Fuel — System Too Lean (Bank 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1139
- Description: Long Term Fuel Trim Additive Fuel — System Too Rich (Bank 2)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

### Air metering (P1141–P1177)

## P1141
- Description: Load Calculation Cross Check — Range/Performance
- Category: P
- Scope: manufacturer (VW)
- Possible causes: faulty MAF sensor (classic 1.8T cause); intake leaks
- Diagnostic notes: Well-known 1.8T code — the ECU cross-checks MAF against throttle/rpm model. From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list + community agreement (single-doc description)

## P1144
- Description: Mass Air Flow Sensor — Open / Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1145
- Description: Mass Air Flow Sensor — Short to Positive
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1146
- Description: Mass Air Flow Sensor — Supply Voltage
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1155
- Description: Manifold Absolute Pressure Sensor — Short to Positive
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1156
- Description: Manifold Absolute Pressure Sensor — Open / Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1157
- Description: Manifold Absolute Pressure Sensor — Supply Voltage
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1160
- Description: Intake Air Temperature Sensor — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1161
- Description: Intake Air Temperature Sensor — Open / Short to Positive
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1162
- Description: Intake Air Temperature Sensor — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list (duplicate-text variant of P1160 in the source).
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1163
- Description: Fuel Temperature Sensor — Open / Short to Positive
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1164
- Description: Fuel Temperature Sensor — Implausible Signal
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1171
- Description: Throttle Actuation Potentiometer Signal 2 — Range/Performance
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1172
- Description: Throttle Actuation Potentiometer Signal 2 — Signal Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1173
- Description: Throttle Actuation Potentiometer Signal 2 — Signal Too High
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1176
- Description: Rear O2S Correction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list; terse source text.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1177
- Description: O2 Correction Behind Catalyst Bank 1 — Limit Attained
- Category: P
- Scope: manufacturer (VW)
- Possible causes: aging catalyst; exhaust leak
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1196
- Description: O2 Sensor Heater Circuit Bank 1 Sensor 1 — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

## P1197
- Description: O2 Sensor Heater Circuit Bank 2 Sensor 1 — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: From the community VW fault-code list.
- Grade: [C]
- Evidence: scribd VW fault-code list (single source)

### Fuel injectors (P1201–P1244, pattern families)

## P1201
- Description: Cylinder 1 Fuel Injector Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: injector coil open/shorted; wiring fault; driver fault in ECU
- Diagnostic notes: VAG 5-digit: 17609. Pattern repeats P1201–P1208 for cylinders 1–8.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1208
- Description: Cylinder 8 Fuel Injector Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17616. Pattern P1201–P1208 covers cylinders 1–8 (electrical malfunction).
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1213
- Description: Cylinder 1 Fuel Injector Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17621. Pattern P1213–P1220 = cylinders 1–8 short to B+.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1225
- Description: Cylinder 1 Fuel Injector Circuit — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17633. Pattern P1225–P1232 = cylinders 1–8 short to ground.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1237
- Description: Cylinder 1 Fuel Injector Circuit — Open Circuit
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17645. Pattern P1237–P1244 = cylinders 1–8 open circuit.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1250
- Description: Fuel Level Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: actually low fuel; faulty fuel level sender
- Diagnostic notes: VAG 5-digit: 17656. Informational — set when the tank runs dry; can accompany lean codes.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### Knock control (P1325–P1340)

## P1325
- Description: Cylinder 1 Knock Control — Limit Attained
- Category: P
- Scope: manufacturer (VW)
- Possible causes: poor fuel quality; carbon buildup; excessive timing advance
- Diagnostic notes: VAG 5-digit: 17733. Pattern P1325–P1332 = cylinders 1–8 knock control at limit.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1332
- Description: Cylinder 8 Knock Control — Limit Attained
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17740. End of the P1325–P1332 cylinder 1–8 pattern.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1339
- Description: Crankshaft Position / Engine Speed Sensors — Cross Connected
- Category: P
- Scope: manufacturer (VW)
- Possible causes: sensors swapped during repair; wiring mix-up
- Diagnostic notes: VAG 5-digit: 17747. Appears after sensor replacement with connectors crossed.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1340
- Description: Camshaft Position Sensor (G40) / Engine Speed Sensor (G28) — Incorrect Correlation
- Category: P
- Scope: manufacturer (VW)
- Possible causes: timing belt/chain incorrectly installed (chain probably lengthened); Camshaft Position Sensor (G40) faulty; Engine Speed Sensor (G28) faulty
- Diagnostic notes: VAG 5-digit: 17748. Ross-Tech: check timing installation (use MVB to check chain), check/replace G40 and G28. Special notes: on 1.8T check engine oil pressure (pickup may be restricted) and confirm the correct G40 is installed (single-gap vs 4-gap); on VR6 see Technical Bulletin 15-07-03; on 30-valve V6 with companion code 17755 check cam chain tensioners are on the correct heads. Almost always a mechanical timing deficiency, not just a sensor.
- Grade: [B]
- Evidence: Ross-Tech wiki 17748/P1340/004928 (causes, solutions, special notes) + VAG DTC table

### Ignition coil power stages (P1341–P1396)

## P1341
- Description: Ignition Coil Power Output Stage 1 — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17749. Pattern: P1341/P1343/P1345 = stages 1/2/3 short to ground.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1343
- Description: Ignition Coil Power Output Stage 2 — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17751
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1345
- Description: Ignition Coil Power Output Stage 3 — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17753
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1391
- Description: Camshaft Position Sensor (Bank 2) — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17799
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1392
- Description: Camshaft Position Sensor (Bank 2) Open — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17800
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1393
- Description: Ignition Coil Power Output Stage 1 — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17801. Pattern P1393–P1395 = stages 1–3 electrical malfunction.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1396
- Description: Engine Speed Sensor — Missing Tooth
- Category: P
- Scope: manufacturer (VW)
- Possible causes: damaged reluctor ring; faulty G28
- Diagnostic notes: VAG 5-digit: 17804
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### EGR (P1400–P1440)

## P1400
- Description: EGR Valve Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17808
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1401
- Description: EGR Valve Circuit — Power Stage Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17809
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1402
- Description: EGR Valve Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17810
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1407
- Description: EGR Temperature Sensor — Signal Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17815
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1408
- Description: EGR Temperature Sensor — Signal Too High
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17816
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1440
- Description: EGR Valve Circuit — Power Stage Open
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17848
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### Secondary air injection (P1409–P1452)

## P1409
- Description: Tank Ventilation Valve — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17817
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1410
- Description: Tank Ventilation Valve — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17818
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1411
- Description: Secondary Air Injection System (Bank 2) — Restricted Flow
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17819
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1414
- Description: Secondary Air Injection System (Bank 2) — Leak Detected
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17822
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1418
- Description: Fuel Level Sensor — Signal Too High
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17826
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1420
- Description: Secondary Air Injection System Control Module — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17828
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1421
- Description: Secondary Air Injection System Control Valve Circuit — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17829
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1422
- Description: Secondary Air Injection System Control Valve Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17830
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1423
- Description: Secondary Air Injection System (Bank 1) — Flow Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: combi valve stuck; SAI pump weak; hoses split
- Diagnostic notes: VAG 5-digit: 17831
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1424
- Description: Secondary Air Injection System (Bank 1) — Leak Detected
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17832
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1425
- Description: Tank Ventilation Valve — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17833
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1426
- Description: Tank Ventilation Valve — Open Circuit
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17834
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1434
- Description: Secondary Air Injection System Pump Relay Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17842
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1436
- Description: Secondary Air Injection System Pump Relay Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17844
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1450
- Description: Secondary Air Injection System Pump Relay Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17858. Source text duplicates P1434 wording; kept as transcribed.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1451
- Description: Secondary Air Injection System Pump Relay Circuit — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17859
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1452
- Description: Secondary Air Injection System Pump Relay Circuit — Open Circuit
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17860
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### EVAP leak detection pump (P1470–P1478)

## P1470
- Description: EVAP Emission Control System Leak Detection Pump Circuit — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17878
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1471
- Description: EVAP Emission Control System Leak Detection Pump Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17879
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1475
- Description: EVAP Emission Control System Leak Detection Pump — Malfunction, Signal Circuit Open
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17883
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1476
- Description: EVAP Emission Control System Leak Detection Pump — Malfunction / Insufficient Vacuum
- Category: P
- Scope: manufacturer (VW)
- Possible causes: EVAP system faulty/leaking; leak detection pump faulty; insufficient vacuum supply to the pump
- Diagnostic notes: VAG 5-digit: 17884. Check the EVAP system for leaks, check the LDP itself, check vacuum supply at the LDP. Technician guidance: check the gas cap first (worn seal), then inspect all vacuum lines — the braided fabric lines near the air filter housing are known to fail; larger lines can soften, collapse or split. The LDP sits below the air filter housing at the frame rail (2.0). VCDS basic settings can exercise the LDP (listen for clicking).
- Grade: [B]
- Evidence: VAG DTC table transcription + VW technician Q&A + community repair agreement

## P1477
- Description: EVAP Emission Control System Circuit — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17885. From the Bentley-derived DTC table; not in the PDF transcription.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1478
- Description: EVAP Emission Control System — Clamped Tube Detected
- Category: P
- Scope: manufacturer (VW)
- Possible causes: kinked/clamped EVAP hose
- Diagnostic notes: VAG 5-digit: 17886. From the Bentley-derived DTC table; not in the PDF transcription.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

### Fuel pump relay, idle, manifold changeover (P1500–P1544)

## P1500
- Description: Fuel Pump Relay Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17908
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1502
- Description: Fuel Pump Relay Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17910
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1504
- Description: Intake Air System — Leak Detected (Bypass Air Determined)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17912
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1509
- Description: Idle Air Control Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17917
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1510
- Description: Idle Air Control Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17918
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1511
- Description: Intake Manifold Changeover Valve Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17919
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1512
- Description: Intake Manifold Changeover Valve Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17920. Related: P1521 (changeover valve 2 electrical malfunction).
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1516
- Description: Intake Manifold Changeover Valve 2 Circuit — Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17924 (Bentley-derived table; numbering offset vs PDF). From the scribd DTC table.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1518
- Description: Intake Camshaft Control Bank 1 — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17926. From the scribd DTC table.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1521
- Description: Intake Manifold Changeover Valve 2 Circuit — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17929. From the scribd DTC table.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1522
- Description: Intake Camshaft Control Bank 2 — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17930. From the scribd DTC table.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1525
- Description: Intake Camshaft Control Bank 1 — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17933. From the scribd DTC table.
- Grade: [C]
- Evidence: scribd VW Online Technical Library DTC table (single source)

## P1543
- Description: Throttle Actuation Potentiometer — Signal Too Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17951
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1544
- Description: Throttle Actuation Potentiometer — Signal Too High
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 17952
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### Throttle actuator, power supply, coding (P1580–P1613)

## P1580
- Description: Throttle Actuator (Bank 1) — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: low battery voltage; throttle body fault
- Diagnostic notes: VAG 5-digit: 17988. May be caused by a low battery if found together with 16487/P0103 — check charging system first.
- Grade: [B]
- Evidence: VAG DTC table transcription + cross-code note corroborated in table

## P1582
- Description: Idle Adaptation at Limit
- Category: P
- Scope: manufacturer (VW)
- Possible causes: vacuum leak; dirty throttle body
- Diagnostic notes: VAG 5-digit: 17990
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1600
- Description: Power Supply (B+) Terminal 15 — Low Voltage
- Category: P
- Scope: manufacturer (VW)
- Possible causes: weak battery; poor terminal 15 supply
- Diagnostic notes: VAG 5-digit: 18008
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1602
- Description: Power Supply (B+) Terminal 30 — Low Voltage
- Category: P
- Scope: manufacturer (VW)
- Possible causes: battery disconnected or discharged; blown fuse; wiring fault
- Diagnostic notes: VAG 5-digit: 18010. The classic "battery was disconnected" signature — frequently spurious after battery work; clear and recheck.
- Grade: [B]
- Evidence: VAG DTC table transcription + widespread technician agreement

## P1606
- Description: Rough Road Specification Engine Torque (ABS Control Unit) — Electrical Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 18014
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1611
- Description: MIL Call-up Circuit / Transmission Control Module — Short to Ground
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 18019
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1612
- Description: Engine Control Module — Incorrectly Coded
- Category: P
- Scope: manufacturer (VW)
- Possible causes: wrong coding after module replacement; coding lost
- Diagnostic notes: VAG 5-digit: 18020. Recode the ECU with VCDS/ODIS.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1613
- Description: MIL Call-up Circuit — Open or Short to B+
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 18021
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

### Transmission (P0705–P1782)

## P0705
- Description: Multi-Function Transmission Range Switch — Malfunction (PRNDL Input)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: F125 multifunction switch failure; water ingress at the switch; wiring fault
- Diagnostic notes: VAG 5-digit: 00293. The infamous F125 switch on 01M/01V automatics — causes limp mode and wrong gear display. The switch sits on the transmission and is moisture-prone.
- Grade: [B]
- Evidence: VAG DTC table transcription + widespread technician agreement

## P0712
- Description: Transmission Fluid Temperature Sensor Circuit — Low Input (G93)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00300 (shared 5-digit with P0713)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0713
- Description: Transmission Fluid Temperature Sensor Circuit — High Input (G93)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00300 (shared 5-digit with P0712)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0715
- Description: Input / Turbine Speed Sensor Circuit — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00297 (shared 5-digit with P0721/P0722)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0721
- Description: Vehicle Speed Sensor Circuit — Range/Performance, Signal Noisy (G38)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00297
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0722
- Description: Vehicle Speed Sensor Circuit — No Signal
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00297
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0725
- Description: Engine Speed Input Circuit (RPM Sensor) — Malfunction
- Category: P
- Scope: manufacturer (VW)
- Possible causes: loose ECM power relay; faulty engine speed sensor
- Diagnostic notes: VAG 5-digit: 00529. The table notes "also check for loose ECM power relay".
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0726
- Description: Engine Speed Input Circuit — RPM Upper Limit Exceeded
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00543
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0727
- Description: Engine Speed Input Circuit (RPM Sensor) — No Signal
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00529
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0730
- Description: Transmission Shift-Range Controller — Incorrect Gear Ratio
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00652 (shared with P0731–P0734)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P0731
- Description: Transmission Shift-Range Controller — Gear 1 Incorrect Ratio
- Category: P
- Scope: manufacturer (VW)
- Possible causes: slipping clutch pack; low ATF; valve body fault
- Diagnostic notes: VAG 5-digit: 00652. Pattern P0731–P0734 = gears 1–4 incorrect ratio.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1704
- Description: Kick-down Switch — Short to Ground (F8)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00296
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1711
- Description: ABS Wheel Speed Signal 1 (Left Front) — Range/Performance (G47)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00283. Transmission sees these when the ABS wheel-speed signal is implausible.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1716
- Description: ABS Wheel Speed Signal 2 (Right Front) — Range/Performance (G45)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00285
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1721
- Description: ABS Wheel Speed Signal 3 (Right Rear) — Range/Performance (G44)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00287
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1726
- Description: ABS Wheel Speed Signal 4 (Left Rear) — Range/Performance (G46)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00290
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1728
- Description: Varying ABS Wheel Speed Signals — Range/Performance
- Category: P
- Scope: manufacturer (VW)
- Possible causes: mismatched tire sizes; faulty wheel-speed sensor
- Diagnostic notes: VAG 5-digit: 00597
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1746
- Description: Transmission Control Module Relay — Supply Voltage (B+) Malfunction, Low
- Category: P
- Scope: manufacturer (VW)
- Possible causes: low battery; bad ground
- Diagnostic notes: VAG 5-digit: 00532. Table notes "Low Battery or Bad Ground".
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1749
- Description: Transmission Control Module — Incorrectly Coded
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 01044. Recode the TCM.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1750
- Description: Supply Voltage (B+)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00532 (shared with P1746). Terse source text.
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1766
- Description: Throttle Angle Signal — Stuck Off
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00638 (shared with P1767)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1767
- Description: Throttle Angle Signal — Stuck On
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00638 (shared with P1766)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1771
- Description: Load Signal — Stuck Off (RPM Signal Missing)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00549 (shared with P1772)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1772
- Description: Load Signal — Stuck On (RPM Signal Missing)
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00549 (shared with P1771)
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1780
- Description: Engine Intervention — Unreadable
- Category: P
- Scope: manufacturer (VW)
- Possible causes: loose ECM power relay
- Diagnostic notes: VAG 5-digit: 00545 (shared with P1781/P1782). Table notes "also check for loose ECM power relay".
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1781
- Description: Engine Intervention — Stuck Off
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00545
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

## P1782
- Description: Engine Intervention — Stuck On
- Category: P
- Scope: manufacturer (VW)
- Possible causes: not documented
- Diagnostic notes: VAG 5-digit: 00545
- Grade: [C]
- Evidence: VAG DTC table transcription (single source)

---

## U-codes (network, VAG-specific)

## U1121
- Description: Databus — Missing Message
- Category: U
- Scope: manufacturer (VW)
- Possible causes: indicated control module not transmitting; wiring/connector fault; module offline after coding change
- Diagnostic notes: VW TSB 01-21-10 lists U112100 as logged across multiple control units (front camera, HV battery charger, etc.), usually passive/sporadic. Extremely common on MQB-platform vehicles — often a consequence of another module's fault rather than a databus wiring problem. Diagnose the indicated missing-message source (symptom byte identifies it) before condemning wiring.
- Grade: [A]
- Evidence: VW TSB 01-21-10 (via NHTSA) + VCDS scan agreement

## U1122
- Description: Databus — Implausible Message
- Category: U
- Scope: manufacturer (VW)
- Possible causes: transmitting module sending out-of-range values; software mismatch after retrofit
- Diagnostic notes: Seen in VCDS scans as "U1122 00 - Implausible Message". Often accompanies retrofits or module swaps.
- Grade: [B]
- Evidence: VCDS scan examples (golfmk7 community) + databus-code family agreement

## U1123
- Description: Databus — Received Error Value
- Category: U
- Scope: manufacturer (VW)
- Possible causes: transmitting module reporting an error state; e.g. ACC reporting irreversible error cascades U1123 into dependent modules
- Diagnostic notes: VW TSB 01-21-10 lists U112300 (received error value for data bus). VCDS scans show it with a bracketed source identifier (e.g. the ACC or instrument cluster message that carried the error value). Usually passive; clear and road-test.
- Grade: [A]
- Evidence: VW TSB 01-21-10 (via NHTSA) + VCDS scan agreement

---

## VAG quirks

1. **5-digit vs P-code**: VCDS shows both forms (e.g. "17884 - EVAP Leak Detection Pump ... P1476 - 002 - Lower Limit Exceeded"). Generic OBD-II tools show only the P-code. Some VAG faults (immobilizer 01176/01177/01179, many comfort-system codes) have NO P-code equivalent — a generic scanner is blind to them.
2. **65535**: means "Control Unit Faulty" in some systems and "No Faults Recorded (if MIL not illuminated)" in others — read it in context, not as a literal code.
3. **Terminal 30 (P1602/18010)** is the classic battery-disconnect signature — clear it and recheck before diagnosing further.
4. **Shared 5-digit codes**: several P-codes share one 5-digit VAG code (e.g. P0712/P0713 = 00300; P1780/P1781/P1782 = 00545). The P-code carries the failure-type detail the 5-digit code lacks.
5. **UDS-era status bytes**: on 2009+ modules VCDS appends a status byte (e.g. U1121 00 [009]); the bracketed text names the missing message source — that is the real diagnostic lead.
6. **SFD-era behavior**: on 2020+ MQB Evo/MEB vehicles, reading these codes still works without SFD authorization (reads are not SFD-protected); clearing codes or running output tests on protected modules needs the SFD unlock.

## Conflicts reported (not resolved)

- **P1102**: the VAG DTC table transcription maps 17510/P1102 to "O2 Sensor Heater Circuit (B1-S1) — Short to B+", while a second community fault-code list gives "O2S Heating Circuit Bank 1 Sensor 1 Voltage Too Low/Air Leak" for P1102. The two sources disagree; both are recorded here with the 5-digit mapping following the transcription.
- **P1450 vs P1434**: the transcription gives both the text "Secondary Air Injection System Pump Relay Circuit — Short to B+" (5-digit 17842 vs 17858). Kept as transcribed; likely a source duplication.
- **P1160 vs P1162**: the community list gives "Intake Air Temperature Sensor — Short to Ground" for both codes. Kept as transcribed.

## Coverage notes

- **B-codes / C-codes (VAG-specific)**: NOT covered in this pass. VAG airbag codes (00588–00595 squib series), ABS codes (00277–00302 valve/pump series) and similar live primarily as 5-digit codes with no verified P/B/C-code equivalents in the sources consulted. Needs a second pass against Ross-Tech wiki body/chassis pages.
- **P2xxx VAG diesel codes**: out of scope for this pass (TDI-specific P2xxx families).
- **2018+ UDS symptom-byte codes** (e.g. B1AD0F0, U14FE00): the UDS-era extended DTC format is a separate harvest task.
- **Unverified ranges**: P1131–P1135, P1147–P1154, P1158–P1159, P1165–P1170, P1174–P1175, P1178–P1195, P1198–P1200, P1209–P1212, P1221–P1224, P1233–P1236, P1245–P1249, P1251–P1324, P1333–P1338, P1346–P1390, P1397–P1399, P1403–P1406, P1412–P1413, P1415–P1417, P1419, P1427–P1433, P1435, P1437–P1439, P1441–P1449, P1453–P1469, P1472–P1474, P1479–P1499, P1501, P1503, P1505–P1508, P1513–P1515, P1517, P1519–P1520, P1523–P1524, P1526–P1542, P1545–P1579, P1581, P1583–P1599, P1601, P1603–P1605, P1607–P1610, P1614–P1703, P1705–P1710, P1712–P1715, P1717–P1720, P1722–P1725, P1727, P1729–P1745, P1747–P1748, P1751–P1765, P1768–P1770, P1773–P1779, P1783–P1999, P1Axx+ hybrid codes.
- **Grade honesty**: descriptions sourced only from the single VAG DTC table transcription are graded C. The SAE J2012 standard text itself was not consulted (paywalled); no A grades claimed on descriptions except the VW TSB U-codes.
