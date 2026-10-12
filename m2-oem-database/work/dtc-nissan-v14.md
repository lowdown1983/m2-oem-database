# Nissan / Infiniti — Manufacturer-Specific DTCs (v1.4.0 expansion)

Research for the M2 OEM vehicle database v1.4.0 expansion. All codes below are
NEW — none appear in the v1.2.1 Nissan DTC set (73 codes). SAE J2012 generic
codes are NOT duplicated here (they live in work/dtc-generic.md). Every entry
carries a quality grade: **A** = Nissan/Infiniti service manual or TSB text ·
**B** = reputable DTC database / multi-source agreement · **C** = single
community source. "not documented" means no source was found — nothing is
invented. Research date: 2026-10-07.

---

## P-codes (Nissan-specific)

## P0603
- Description: ECM Back Up Circuit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "ECM BACK UP/CIRCUIT P0603")

## P0850
- Description: Park/Neutral Position Switch Circuit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "P-N POS SW/CIRCUIT P0850")

## P1032
- Description: Air Fuel Ratio (A/F) Sensor 1 Heater Control Circuit High (Bank 1)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: faulty A/F sensor 1 (bank 1); A/F sensor 1 heater harness open or shorted; poor electrical connection in A/F sensor 1 circuit
- Diagnostic notes: High-circuit counterpart of P1031. Nissan TSB NTB04-032a (2004 Titan/Armada) covers the A/F sensor heater low-circuit codes P1031/P1051 (ECM reprogram after confirming ECM part number); the high-circuit codes P1032/P1052 share the same heater circuit diagnosis.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1031 P1032 P1051 P1052 A/F sensor 1 heater"); eobdcode.com Nissan P1032 page (heater control circuit high, bank 1)

## P1052
- Description: Air Fuel Ratio (A/F) Sensor 1 Heater Control Circuit High (Bank 2)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: High-circuit counterpart of P1051 (bank 2). See P1032 notes for the shared heater-circuit context.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1031 P1032 P1051 P1052 A/F sensor 1 heater"); MyAirbags/UpFix Nissan/Infiniti factory DTC list ("A/F ratio sensor bank 2 heater voltage high")

## P1065
- Description: ECM Power Supply (Battery Voltage Supply)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: failing battery (voltage below 12V engine-off); failing alternator (outside 13.2–14.4V running); loose/corroded battery cables; wiring fault to ECM backup power
- Diagnostic notes: ECM receives battery voltage at all times for memory backup. Per Nissan tech guidance: check alternator output (13.2–14.4V running), then battery voltage after 15 min rest (below 12V suggests a bad cell); code may self-clear after 75–100 miles of driving if power supply is healthy.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1065 ECM power supply"); JustAnswer Nissan technicians (ECM power supply / PCM backup circuit diagnosis)

## P1102
- Description: MAF Sensor Performance Problem
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan and 2008 Altima FSM indexes)

## P1110
- Description: Intake Valve Timing Control, Bank 1
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: dirty/low engine oil; faulty intake valve timing control solenoid valve (bank 1); solenoid harness open/shorted; faulty crankshaft position sensor (POS); faulty camshaft position sensor
- Diagnostic notes: Set when the gap between target and actual cam phase angle exceeds the threshold. Check/change engine oil and filter before replacing the solenoid valve.
- Grade: [B]
- Evidence: eobdcode.com Nissan P1110 page; nicoclub.com forum (P1110 = Intake Valve Timing Control Bank 1, causes list); MyAirbags/UpFix factory DTC list

## P1111
- Description: Intake Valve Timing Control Solenoid Valve Circuit, Bank 1
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Circuit-level counterpart of P1110 on some models/years.
- Grade: [B]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list ("Camshaft position (CMP) actuator intake bank 1 circuit malfunction"); swirlzcupcakes.com Nissan P1111 page (defined by Nissan as "Intake Valve Timing Control Solenoid Valve Circuit Bank 1")

## P1116
- Description: Automatic Transmission Turbine Revolution Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1119
- Description: Engine Coolant Temperature (ECT) Sensor Radiator Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1120
- Description: Throttle Position (TP) Sensor 2 Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; 2005 Titan/2008 Altima FSMs use P0122/P0123 for TP sensor 2 instead)

## P1121
- Description: Electric Throttle Control Actuator
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: In fail-safe, ECM regulates throttle opening around idle; engine speed will not rise above ~2,000 rpm.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart and fail-safe chart: "P1121 Electric throttle control actuator")

## P1122
- Description: Electric Throttle Control Function
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1122 Electric throttle control function")

## P1123
- Description: Throttle Motor Relay Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1124
- Description: Electric Throttle Control Actuator
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Groups with P1126/P1128 in the Titan priority chart under electric throttle control actuator faults.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1124 P1126 P1128 Electric throttle control actuator")

## P1125
- Description: Throttle Position (TP) Sensor 1 and 2 Signal Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1128
- Description: Electric Throttle Control Actuator
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Groups with P1124/P1126 in the Titan priority chart under electric throttle control actuator faults.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1124 P1126 P1128 Electric throttle control actuator")

## P1131
- Description: Intake Manifold Air Control Solenoid Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1132
- Description: Intake Manifold Air Control Solenoid Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1135
- Description: Camshaft Position (CMP) Actuator RH Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 (RH) counterpart of P1110; intake valve timing control solenoid valve, bank 2.
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1136
- Description: Camshaft Position (CMP) Actuator Intake Bank 2 Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Circuit-level counterpart of P1135; bank 2 analog of P1111.
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1137
- Description: Intake Manifold Air Control Actuator Position Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1138
- Description: Intake Manifold Air Control Solenoid Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1140
- Description: Camshaft Position (CMP) Actuator LH Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 1 (LH) circuit-level analog; pairs with P1110/P1111 family.
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1143
- Description: Heated Oxygen Sensor 1 Lean Shift Monitoring, Bank 1
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: faulty front heated oxygen sensor (bank 1); intake air leaks; HO2S1 harness open/shorted; poor electrical connection; fuel pressure; injectors
- Diagnostic notes: Detected when the sensor's max/min voltages do not reach specified values. Reported on 2002–2003 Frontier/Altima; Nissan issued ground-fix guidance (reinforce intake/sensor grounds) for persistent P1143 before replacing sensors.
- Grade: [B]
- Evidence: eobdcode.com Nissan P1143 page; carobdcode.com P1143 Nissan page; JustAnswer (2002 Frontier P1143/P1163 cases)

## P1144
- Description: Heated Oxygen Sensor 1 Rich Shift Monitoring, Bank 1
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: faulty front heated oxygen sensor (bank 1); HO2S1 harness open/shorted; poor electrical connection; inappropriate fuel pressure; faulty injectors; intake or exhaust leaks
- Diagnostic notes: Detected when an excessively high sensor voltage is sent to the ECM. Replacing the front O2 sensor (bank 1) usually resolves it.
- Grade: [B]
- Evidence: eobdcode.com Nissan P1144 page (also Infiniti G35 page); carobdcode.com P1144 Nissan/Infiniti pages; dtcsearch.com P1144 Nissan entry

## P1145
- Description: Camshaft Position (CMP) Actuator Position Sensor Intake Bank 2 Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 intake valve timing control position sensor circuit; pairs with P1140 (bank 1).
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1146
- Description: Heated Oxygen Sensor 2 (Bank 1) — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Rear (post-catalyst) oxygen sensor, bank 1.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P0138 P0139 P0158 P0159 P1146 P1147 P1166 P1167 Heated oxygen sensor 2"); MyAirbags/UpFix factory DTC list ("Heated oxygen sensor (HO2S) 2 bank 1 voltage low")

## P1147
- Description: Heated Oxygen Sensor 2 (Bank 1) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Rear (post-catalyst) oxygen sensor, bank 1.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "Heated oxygen sensor 2" group); MyAirbags/UpFix factory DTC list ("Heated oxygen sensor (HO2S) 2 bank 1 voltage high")

## P1164
- Description: Heated Oxygen Sensor 1 (Bank 2) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; entry for P1163 in the same source is truncated and is excluded — see coverage notes)

## P1166
- Description: Heated Oxygen Sensor 2 (Bank 2) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Rear (post-catalyst) oxygen sensor, bank 2. Note: the source list gives P1166 and P1167 the identical description; the FSM groups both under heated oxygen sensor 2 without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "Heated oxygen sensor 2" group); MyAirbags/UpFix factory DTC list

## P1167
- Description: Heated Oxygen Sensor 2 (Bank 2) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1166 — source list duplicates the description for P1166/P1167; FSM does not distinguish them.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "Heated oxygen sensor 2" group); MyAirbags/UpFix factory DTC list

## P1169
- Description: Heated Oxygen Sensor 3 — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1169 and P1170 the identical description ("HO2S 3 voltage low").
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1170
- Description: Heated Oxygen Sensor 3 — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1169 — source list duplicates the description for P1169/P1170.
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1220
- Description: Fuel Pressure (FP) Control Module Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan and 2008 Altima FSM indexes)

## P1223
- Description: Throttle Position (TP) Sensor 2 — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; 2005 Titan/2008 Altima FSMs use P0122/P0123 for TP sensor 2 instead)

## P1224
- Description: Throttle Position (TP) Sensor 2 — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; 2005 Titan/2008 Altima FSMs use P0122/P0123 for TP sensor 2 instead)

## P1225
- Description: Closed Throttle Position Learning, Bank 1 (CTP Learning)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Closed-throttle-position learning value out of range; usually corrected by performing the throttle valve closed position learning procedure.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "CTP LEARNING-B1 P1225"); 2005 Nissan Titan FSM, EC section (priority chart throttle position sensor group)

## P1226
- Description: Closed Throttle Position Learning, Bank 1 (CTP Learning)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1225 — FSM lists P1225/P1226 under the same CTP LEARNING-B1 item without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "CTP LEARNING-B1 P1226"); 2005 Nissan Titan FSM, EC section (priority chart)

## P1227
- Description: Accelerator Pedal Position (APP) Sensor 2 — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; 2005 Titan/2008 Altima FSMs use P2127/P2128 for APP sensor 2 instead)

## P1228
- Description: Accelerator Pedal Position (APP) Sensor 2 — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; 2005 Titan/2008 Altima FSMs use P2127/P2128 for APP sensor 2 instead)

## P1229
- Description: Sensor Power Supply
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ECM sensor power supply circuit fault; diagnose before sensor-level codes that share the supply.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1229 Sensor power supply"); 2008 Nissan Altima FSM uses P0643 for the same function (model variation noted)

## P1271
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "P1271 P1272 P1273 P1274 P1276 P1278 P1279 P1281 P1282 P1283 P1284 P1286 P1288 P1289 A/F sensor 1"); MyAirbags/UpFix factory DTC list

## P1272
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1276
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Activity
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: A/F sensor 1 activity monitor, bank 1.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list ("A/F ratio sensor bank 1 activity")

## P1278
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Slow Response
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1279 — FSM groups both under A/F sensor 1 without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1279
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Slow Response
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1278.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1281
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 counterpart of P1271.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1282
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Voltage High
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 counterpart of P1272.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1286
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Activity
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 counterpart of P1276.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1288
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Slow Response
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank 2 counterpart of P1278/P1279.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1289
- Description: Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Slow Response
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1288.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/F sensor 1" group); MyAirbags/UpFix factory DTC list

## P1421
- Description: Cold Start Control
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "COLD START CONTROL P1421"); 2008 Nissan Sentra FSM, EC section (same index entry)

## P1442
- Description: Evaporative Emission (EVAP) Canister Purge System — Small Leak Detected
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1443
- Description: Evaporative Emission (EVAP) Canister Purge Control System — Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1456
- Description: Evaporative Emission (EVAP) Canister Purge System — Very Small Leak Detected
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Finer leak threshold than P1440/P1442 (small leak).
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1480
- Description: Engine Coolant Blower Motor Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Cooling fan control circuit; pairs with P1900 (blower motor circuit).
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1551
- Description: Battery Current Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: One of five codes (P1550–P1554) the FSM groups under "BAT CURRENT SENSOR"; sub-conditions (low/high/performance) are on the diagnosis pages, not the index.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "BAT CURRENT SENSOR P1551"); priority chart ("P1550 P1551 P1552 P1553 P1554 Battery current sensor")

## P1552
- Description: Battery Current Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1551.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "BAT CURRENT SENSOR P1552")

## P1553
- Description: Battery Current Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1551.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "BAT CURRENT SENSOR P1553")

## P1554
- Description: Battery Current Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1551.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "BAT CURRENT SENSOR P1554")

## P1564
- Description: ASCD Steering Switch
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Automatic speed control device (cruise control) steering switch circuit.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "ASCD SW P1564"); 2008 Nissan Sentra FSM, EC section (same); 2005 Nissan Titan FSM (priority chart: "P1564 ASCD steering switch")

## P1568
- Description: Cruise Control Master Switch Signal Out of Specification
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1572
- Description: ASCD Brake Switch
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Automatic speed control device brake switch circuit.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "ASCD BRAKE SW P1572"); 2005 Nissan Titan FSM (priority chart: "P1572 ASCD brake switch")

## P1574
- Description: ASCD Vehicle Speed Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Automatic speed control device vehicle speed sensor signal.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "ASCD VHL SPD SEN P1574"); 2005 Nissan Titan FSM (priority chart: "P1574 ASCD vehicle speed sensor")

## P1700
- Description: CVT Shift Control Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2008 Sentra/Altima CVT DTC indexes)

## P1715
- Description: Input Pulley Speed Sensor (CVT)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: CVT input (primary) pulley speed sensor circuit.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "IN PULY SPEED P1715"); 2008 Nissan Sentra FSM, EC section (same)

## P1716
- Description: AT Turbine Revolution Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Automatic transmission turbine (input) revolution sensor.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1720
- Description: Vehicle Speed Sensor (VSS) Signal Variation
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan and 2008 Altima FSM indexes)

## P1730
- Description: AT Fail-Safe Function Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Automatic transmission fail-safe control circuit.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list ("AT fail safe function circuit malfunction")

## P1740
- Description: Lock-Up Select Solenoid Valve Circuit (CVT)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: CVT lock-up select solenoid valve circuit.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "LU-SLCT SOL/CIRC P1740"); 2008 Nissan Sentra FSM, EC section (same)

## P1752
- Description: AT Input Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1752 and P1754 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1754
- Description: AT Input Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1752.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1757
- Description: AT Front Brake Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1757 and P1759 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1759
- Description: AT Front Brake Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1757.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1762
- Description: AT Direct Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1762 and P1764 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1764
- Description: AT Direct Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1762.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1767
- Description: AT High and Low Reverse Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1767 and P1769 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1769
- Description: AT High and Low Reverse Clutch Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1767.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1772
- Description: AT Low Coast Brake Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Note: the source list gives P1772 and P1774 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1774
- Description: AT Low Coast Brake Solenoid Valve Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See P1772.
- Grade: [A]
- Evidence: 2005 Nissan Titan FSM, EC section (priority chart: "A/T related sensors and solenoid valves" group); MyAirbags/UpFix factory DTC list

## P1775
- Description: Torque Converter Clutch Solenoid — Voltage Low
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan FSM A/T group)

## P1776
- Description: Torque Converter Clutch Solenoid — Converter Slip During Lock Condition
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan FSM A/T group)

## P1777
- Description: CVT Step Motor Circuit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: CVT step motor circuit fault.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "STEP MOTOR CIRC P1777"); 2008 Nissan Sentra FSM, EC section (same)

## P1778
- Description: CVT Step Motor Function
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: CVT step motor mechanical/functional fault.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "STEP MOTOR FNCT P1778"); 2008 Nissan Sentra FSM, EC section (same)

## P1780
- Description: AT Shift Change Signal Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source; absent from 2005 Titan FSM A/T group)

## P1800
- Description: Intake Manifold Air Control Solenoid Circuit Malfunction
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

## P1805
- Description: Brake Switch Circuit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Brake (stop lamp) switch circuit input to ECM.
- Grade: [A]
- Evidence: 2008 Nissan Altima FSM, EC section (DTC index: "BRAKE SW/CIRCUIT P1805"); 2008 Nissan Sentra FSM, EC section (same); 2005 Nissan Titan FSM (priority chart: "P1805 Brake switch")

## P1900
- Description: Engine Coolant Blower Motor Circuit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Cooling fan/blower motor circuit; pairs with P1480 (blower motor control circuit).
- Grade: [C]
- Evidence: MyAirbags/UpFix Nissan/Infiniti factory DTC list (single source)

---

## B-codes (Nissan-specific)

## B1017
- Description: Occupant Classification System Control Unit [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: OCS control unit malfunctioning; FSM repair order: replace RH front seat cushion/OCS control unit assembly (do not disassemble the cushion).
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section (CONSULT-II diagnostic code chart: "OCCUPANT SENS C/U [UNIT FAIL] [B1017], [B1020] or [B1021]"); 2010 Nissan Altima SRC section (same grouping)

## B1018
- Description: Occupant Classification Sensor [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: damaged wiring under passenger seat; poor connector contact; failed OCS sensor mat in seat cushion
- Diagnostic notes: OCS sensor mat malfunctioning. Check wiring under the seat, unplug/clean/reconnect; the sensor is inside the seat cushion and is not separately serviceable — cushion assembly replacement is the FSM repair.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("OCCUPANT SENS [UNIT FAIL] [B1018]"); 2010 Nissan Altima SRC section (same); YouTube Nissan B1018 diagnosis walkthrough (Sentra/Altima/Maxima/Rogue/Murano/Leaf/Titan/Versa/Cube/Juke)

## B1019
- Description: Belt Tension Sensor [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — 2007 Xterra FSM lists B1019 as "BELT TENSION SENS [UNIT FAIL]" (belt tension sensor malfunctioning; repair: replace RH front seat belt assembly), while the 2010 Altima SRC section lists B1019 as "OCCUPANT SENS [OTHER FAIL]" (OCS malfunctioning). Meaning appears model/year-dependent; verify against the specific vehicle's FSM.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section vs 2010 Nissan Altima SRC section (conflicting definitions documented)

## B1020
- Description: Occupant Classification System Control Unit [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Grouped with B1017/B1021 in the FSM chart; same OCS control unit diagnosis.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section (CONSULT-II diagnostic code chart: "[B1017], [B1020] or [B1021]")

## B1021
- Description: Occupant Classification System Control Unit [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Grouped with B1017/B1020 in the FSM chart; same OCS control unit diagnosis.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section (CONSULT-II diagnostic code chart: "[B1017], [B1020] or [B1021]")

## B1022
- Description: Occupant Classification System Control Unit [Communication Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Communication between the OCS control unit and the air bag diagnosis sensor unit is interrupted; check harness connections before replacing units.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("OCCUPANT SENS C/U [COMM FAIL] [B1022]"); 2010 Nissan Altima SRC section (same)

## B1023
- Description: Front Passenger Air Bag OFF Indicator Circuit
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Front passenger air bag OFF indicator malfunctioning; FSM repair order: check harness, replace harness, replace the indicator, replace air bag diagnosis sensor unit.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("PASS A/B INDCTR CKT [B1023]"); 2010 Nissan Altima SRC section (same)

## B1033
- Description: Crash Zone Sensor [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Crash zone sensor internal failure; FSM repair order: check harness, replace harness, replace crash zone sensor, replace air bag diagnosis sensor unit.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("CRASH ZONE SEN [UNIT FAIL] [B1033] or [B1034]")

## B1034
- Description: Crash Zone Sensor [Unit Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B1033.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("CRASH ZONE SEN [UNIT FAIL] [B1033] or [B1034]")

## B1035
- Description: Crash Zone Sensor [Communication Fail]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Crash zone sensor communication failure with air bag diagnosis sensor unit.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("CRASH ZONE SEN [COMM FAIL] [B1035]")

## B1049
- Description: Driver Air Bag Module [Open]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: open in driver air bag module circuit including spiral cable (clock spring); damaged harness; faulty module
- Diagnostic notes: CONFLICT — the 2007 Xterra FSM CONSULT-II chart places B1049/B1054 under DRIVER AIRBAG MODULE [OPEN] (circuit open including the spiral cable), while community sources (JustAnswer) variously describe B1049 as a front-passenger airbag/OCS/pretensioner fault. FSM repair order: visually check harness, replace harness if damaged, replace driver air bag module, replace spiral cable, replace air bag diagnosis sensor unit. Trust the FSM for the specific vehicle.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [OPEN] [B1049] or [B1054]"); conflicting JustAnswer community descriptions noted

## B1050
- Description: Driver Air Bag Module [VB-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Driver air bag module circuit shorted to some power supply circuit (including spiral cable).
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [VB-SHORT] [B1050] or [B1055]")

## B1051
- Description: Driver Air Bag Module [GND-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Driver air bag module circuit shorted to ground (including spiral cable).
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [GND-SHORT] [B1051] or [B1056]")

## B1052
- Description: Driver Air Bag Module [Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Driver air bag module circuits shorted to each other.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [SHORT] [B1052] or [B1057]")

## B1054
- Description: Driver Air Bag Module [Open]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage (dual-stage inflator) counterpart of B1049; see B1049 notes and conflict.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [OPEN] [B1049] or [B1054]")

## B1055
- Description: Driver Air Bag Module [VB-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1050.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [VB-SHORT] [B1050] or [B1055]")

## B1056
- Description: Driver Air Bag Module [GND-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1051.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [GND-SHORT] [B1051] or [B1056]")

## B1057
- Description: Driver Air Bag Module [Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1052. Note: B1053 is skipped in this scheme (stage 1 = B1049–B1052, stage 2 = B1054–B1057).
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("DRIVER AIRBAG MODULE [SHORT] [B1052] or [B1057]")

## B1065
- Description: Front Passenger Air Bag Module [Open]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Front passenger air bag module circuit open; FSM repair order: check harness, replace harness, replace module, replace diagnosis sensor unit.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [OPEN] [B1065] or [B1070]")

## B1066
- Description: Front Passenger Air Bag Module [VB-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Front passenger air bag module circuit shorted to some power supply circuit.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [VB-SHORT] [B1066] or [B1071]")

## B1067
- Description: Front Passenger Air Bag Module [GND-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Front passenger air bag module circuit shorted to ground.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [GND-SHORT] [B1067] or [B1072]")

## B1068
- Description: Front Passenger Air Bag Module [Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Front passenger air bag module circuits shorted to each other.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [SHORT] [B1068] or [B1073]")

## B1070
- Description: Front Passenger Air Bag Module [Open]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1065.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [OPEN] [B1065] or [B1070]")

## B1071
- Description: Front Passenger Air Bag Module [VB-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1066.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [VB-SHORT] [B1066] or [B1071]")

## B1072
- Description: Front Passenger Air Bag Module [GND-Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1067.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [GND-SHORT] [B1067] or [B1072]")

## B1073
- Description: Front Passenger Air Bag Module [Short]
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second-stage counterpart of B1068.
- Grade: [A]
- Evidence: 2007 Nissan Xterra FSM, SRS section ("ASSIST A/B MODULE [SHORT] [B1068] or [B1073]")

## B2108
- Description: Steering Lock Relay ON
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: faulty IPDM E/R (relay stuck ON)
- Diagnostic notes: IPDM E/R detects the steering lock relay stuck at ON for ~1 second even though the BCM commands it OFF. Check 10A fuse No. 40 in IPDM E/R; if the code is current, replace IPDM E/R.
- Grade: [A]
- Evidence: 2009 Nissan Altima FSM, SEC section (DTC logic: "STRG LCK RELAY ON [B2108]")

## B2109
- Description: Steering Lock Relay
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Steering lock relay ON signal transmitted from BCM to IPDM E/R via CAN; IPDM E/R turns the relay ON and reports steering release to BCM. (Coupe variant in source.)
- Grade: [A]
- Evidence: 2009 Nissan Altima FSM, SEC section ("B2109 STEERING LOCK RELAY [COUPE]")

## B210B
- Description: Starter Control Relay — Stuck ON
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: faulty IPDM E/R; harness/connector faults in starter control relay circuit
- Diagnostic notes: IPDM E/R detects the starter control relay stuck in the ON position for 1 second or more (comparing BCM CAN signals against IPDM E/R inputs). If current, replace IPDM E/R.
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (DTC logic: "START CONT RLY ON [B210B]")

## B210C
- Description: Starter Control Relay — Stuck OFF (Circuit)
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: faulty IPDM E/R; faulty BCM; low IPDM E/R supply voltage (~7–8V); harness faults
- Diagnostic notes: IPDM E/R detects the starter control relay stuck in the OFF position for 1 second or more. May set spuriously on low IPDM E/R supply voltage.
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (DTC logic: "STR CONT RLY OFF CIRC [B210C]")

## B210D
- Description: Starter Relay — Stuck ON (Circuit)
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: harness/connectors (starter motor relay control circuit open/shorted); faulty IPDM E/R; faulty BCM
- Diagnostic notes: IPDM E/R detects the starter relay stuck in the ON position for 5 seconds or more.
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (DTC logic: "STARTER RLY ON CIRC [B210D]")

## B210E
- Description: Starter Relay — Stuck OFF
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: faulty IPDM E/R; faulty BCM; low battery/IPDM E/R supply voltage
- Diagnostic notes: IPDM E/R detects the starter relay stuck in the OFF position for 5 seconds or more. Diagnose B2605 first if displayed together.
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (DTC logic: "STARTER RELAY OFF [B210E]")

## B210F
- Description: Shift Position / Clutch Interlock Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: harness/connectors (CAN line or transmission range switch circuit open/shorted); faulty transmission range switch; faulty IPDM E/R; faulty BCM
- Diagnostic notes: IPDM E/R detects a mismatch between the hardwired P/N position signal from the transmission range switch and the P/N signal received from BCM via CAN.
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (DTC logic: "INTRLCK/PNP SW ON [B210F]")

## B2110
- Description: Shift Position / Clutch Interlock Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Pairs with B210F in the SEC diagnosis section (shift position/clutch interlock switch circuit).
- Grade: [A]
- Evidence: 2014 Nissan Note FSM, SEC section (contents: "B2110 SHIFT POSITION/CLUTCH INTERLOCK SWITCH")

## B2555
- Description: Stop Lamp
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Stop lamp switch circuit monitored by BCM.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2555: STOP LAMP"); 2014 Nissan Note FSM, SEC section (same)

## B2556
- Description: Push-Button Ignition Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Push-button ignition switch circuit monitored by BCM.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2556: PUSH-BTN IGN SW"); 2014 Nissan Note FSM, SEC section (same)

## B2557
- Description: Vehicle Speed
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Vehicle speed signal monitored by BCM.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2557: VEHICLE SPEED"); 2014 Nissan Note FSM, SEC section (same)

## B2562
- Description: Low Voltage
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: low battery voltage; charging system fault
- Diagnostic notes: BCM low-voltage detection; check battery and charging system first (also appears in BCM priority chart position 1).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2562: LOW VOLTAGE")

## B2601
- Description: Shift Position
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Shift position signal monitored by BCM (one of B2601/B2602/B2603 shift-position family).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2601: SHIFT POSITION"); 2014 Nissan Note FSM, SEC section (same)

## B2602
- Description: Shift Position
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B2601.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2602: SHIFT POSITION"); 2014 Nissan Note FSM, SEC section (same)

## B2603
- Description: Shift Position Status
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Shift position status signal.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2603: SHIFT POSI STATUS"); 2014 Nissan Note FSM, SEC section (same)

## B2604
- Description: PNP/Clutch Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Park/neutral position (CVT) / clutch interlock (M/T) switch signal.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2604: PNP/CLUTCH SW"); 2014 Nissan Note FSM, SEC section ("B2604 SHIFT POSITION")

## B2605
- Description: PNP/Clutch Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B2604. Diagnose B2605 before B210E when both are displayed.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2605: PNP/CLUTCH SW"); 2014 Nissan Note FSM, SEC section ("B2605 SHIFT POSITION")

## B2614
- Description: BCM (Accessory Relay Circuit)
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: accessory relay circuit open/shorted; faulty BCM; faulty accessory relay; harness/connectors
- Diagnostic notes: BCM requests accessory relay operation but gets no response for 2+ seconds. (PCS section: power distribution system.)
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2614: BCM"); Juke PCS section (DTC logic: "B2614 ACC RELAY CIRCUIT")

## B2615
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault (one of the B2614/B2615/B2616/B2618 BCM group; B2617 not used).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2615: BCM")

## B2616
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault; see B2615.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2616: BCM")

## B2618
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault; see B2615.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2618: BCM")

## B261A
- Description: Push-Button Ignition Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Push-button ignition switch circuit (PCS/power distribution context).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B261A: PUSH-BTN IGN SW")

## B261F
- Description: ASCD Cancel / Clutch Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ASCD cancel/clutch switch circuit.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B261F: ASCD CNCL/CLTCH SW"); 2014 Nissan Note FSM, SEC section ("B261F ASCD CLUTCH SWITCH")

## B2620
- Description: Neutral Switch (Park/Neutral Position Switch)
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Listed as "NEUTRAL SW" in the Juke index and "PARK/NEUTRAL POSITION SWITCH" in the Note SEC.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2620: NEUTRAL SW"); 2014 Nissan Note FSM, SEC section ("B2620 PARK/NEUTRAL POSITION SWITCH")

## B2621
- Description: Inside Key Antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Intelligent Key inside antenna circuit (door lock / key system).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2621: INSIDE ANTENNA")

## B2622
- Description: Inside Key Antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B2621 (second inside-antenna channel).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2622: INSIDE ANTENNA")

## B2626
- Description: Outside Key Antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Intelligent Key outside antenna circuit.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2626: OUTSIDE ANTENNA")

## B2627
- Description: Outside Key Antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B2626 (second outside-antenna channel).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2627: OUTSIDE ANTENNA")

## B2628
- Description: Outside Key Antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See B2626 (third outside-antenna channel).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B2628: OUTSIDE ANTENNA")

## B26E8
- Description: Clutch Interlock Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Clutch interlock switch circuit (M/T models).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26E8: CLUTCH SW"); 2014 Nissan Note FSM, SEC section ("B26E8 CLUTCH INTERLOCK SWITCH")

## B26F2
- Description: Ignition Relay ON
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Fail-safe: inhibit engine cranking. Ignition switch ON signal (CAN, from BCM) stuck OFF/ON mismatch.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F2: IGN RELAY ON"; fail-safe chart: "Inhibit engine cranking")

## B26F3
- Description: Starter Control Relay ON
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Starter control relay stuck ON.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F3: START CONT RLY ON"); 2014 Nissan Note FSM, SEC section ("B26F3 STARTER CONTROL RELAY")

## B26F4
- Description: Starter Control Relay OFF
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Starter control relay stuck OFF.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F4: START CONT RLY OFF"); 2014 Nissan Note FSM, SEC section ("B26F4 STARTER CONTROL RELAY")

## B26F6
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault (one of the B26F6/B26F7/B26F8 BCM group).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F6: BCM")

## B26F7
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault; see B26F6.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F7: BCM"); 2014 Nissan Note FSM, SEC section ("B26F7 BCM")

## B26F8
- Description: BCM
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM internal fault; see B26F6.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F8: BCM")

## B26F9
- Description: Crank Request Circuit — Short
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Crank request circuit shorted.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26F9: CRANK REQ CIR SHORT")

## B26FA
- Description: Crank Request Circuit — Open
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Crank request circuit open.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26FA: CRANK REQ CIR OPEN")

## B26FB
- Description: Clutch Switch
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Clutch switch circuit.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26FB: CLUTCH SWITCH"); 2014 Nissan Note FSM, SEC section ("B26FB CLUTCH SWITCH")

## B26FC
- Description: Key Registration
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Key registration fault (Intelligent Key / NATS key registration).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "B26FC: KEY REGISTRATION"); 2014 Nissan Note FSM, SEC section ("B26FC KEY REGISTRATION")

---

## C-codes (Nissan-specific)

## C1113
- Description: G-Sensor
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS/VDC G-sensor circuit.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1113 G-SENSOR"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1113 G-SENSOR")

## C1114
- Description: Main Relay
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator main relay circuit.
- Grade: [A]
- Evidence: Nissan BRC section FSM excerpt via scribd (DTC index: "MAIN RELAY [C1114]")

## C1115
- Description: ABS Sensor [Abnormal Signal]
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: incorrect (non-specified) tires fitted; wheel sensor / sensor rotor issues; ABS module ground faults
- Diagnostic notes: Set when a wheel-speed difference vs the other wheels is detected while driving (e.g., wrong-size tires). Inspect sensor connectors for corrosion/damage, clean sensor rings, check harness and module grounds.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1115 ABS SENSOR [ABNORMAL SIGNAL]"); 2015 Nissan QX60 BRC section via manuals.plus (fail-safe description); JustAnswer (2012 Pathfinder C1115 pinpoint guidance)

## C1116
- Description: Stop Lamp Switch
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Stop lamp switch signal not input when the brake pedal operates.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1116 STOP LAMP SW"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1116 STOP LAMP SW"); 2015 Nissan QX60 BRC section via manuals.plus

## C1120
- Description: Front LH IN ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in front LH ABS IN (inlet) solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1120 FR LH IN ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart); 2015 Nissan QX60 BRC section via manuals.plus

## C1121
- Description: Front LH OUT ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in front LH ABS OUT (outlet) solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1121 FR LH OUT ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1122
- Description: Front RH IN ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in front RH ABS IN solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1122 FR RH IN ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1123
- Description: Front RH OUT ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in front RH ABS OUT solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1123 FR RH OUT ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1124
- Description: Rear LH IN ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in rear LH ABS IN solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1124 RR LH IN ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1125
- Description: Rear LH OUT ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in rear LH ABS OUT solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1125 RR LH OUT ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1126
- Description: Rear RH IN ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in rear RH ABS IN solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1126 RR RH IN ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1127
- Description: Rear RH OUT ABS Solenoid Valve
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Malfunction detected in rear RH ABS OUT solenoid valve.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1127 RR RH OUT ABS SOL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1130
- Description: Engine Signal 1
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: failed ABS actuator; ABS module wiring short/open; ABS module with mismatched/unprogrammed VIN
- Diagnostic notes: Malfunction detected in ECM system as seen by the ABS actuator and electric unit (control unit). Community reports treat it as an ABS control unit failure code.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1130 ENGINE SIGNAL 1"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1130 ENGINE SIGNAL 1"); JustAnswer (C1130 = ABS actuator and electric unit failure; causes list)

## C1131
- Description: Engine Signal 2
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Engine signal 2 as seen by the ABS control unit.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1131 ENGINE SIGNAL 2")

## C1132
- Description: Engine Signal 3
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Engine signal 3 as seen by the ABS control unit.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1132 ENGINE SIGNAL 3")

## C1133
- Description: Engine Signal 4
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Engine signal 4 as seen by the ABS control unit. (Note: the Armada index skips from ENGINE SIGNAL 4 to ENGINE SIGNAL 6.)
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1133 ENGINE SIGNAL 4")

## C1136
- Description: Engine Signal 6
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Engine signal 6 as seen by the ABS control unit. (ENGINE SIGNAL 5 not listed in the index.)
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1136 ENGINE SIGNAL 6")

## C1140
- Description: Actuator Relay
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator relay circuit.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1140 ACTUATOR RLY"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1140 ACTUATOR RLY")

## C1142
- Description: Pressure Sensor Circuit
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS pressure sensor circuit.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1142 PRESS SEN CIRCUIT")

## C1143
- Description: Steering Angle Sensor Circuit
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Steering angle sensor circuit fault (VDC).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1143 ST ANG SEN CIRCUIT"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1144
- Description: Steering Angle Sensor Signal
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Steering angle sensor signal fault (VDC).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1144 ST ANG SEN SIGNAL"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1145
- Description: Yaw Rate Sensor
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Yaw rate sensor fault (VDC).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1145 YAW RATE SENSOR"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1146
- Description: Side G-Sensor Circuit
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Side (lateral) G-sensor circuit fault (VDC).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1146 SIDE G-SEN CIRCUIT"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1155
- Description: Brake Fluid Level Low
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low brake fluid; brake fluid level switch/sensor fault
- Diagnostic notes: Brake fluid level low detection.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1155 BR FLUID LEVEL LOW"); 2016 Nissan Juke FSM, BRC section (priority chart)

## C1156
- Description: Steering Angle Sensor Communication Circuit
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Steering angle sensor communication circuit fault.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1156 ST ANG SEN COM CIR")

## C1160
- Description: Decel G-Sensor Set (Not Calibrated)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Deceleration G-sensor neutral position not set/calibrated.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1160 DECEL G SEN SET")

## C1163
- Description: Steering Angle Sensor Safe (Neutral Position Not Learned)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Steering angle sensor safe/neutral position not established.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1163 ST ANGL SEN SAFE")

## C1164
- Description: Cut Valve 1 (CV1)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator cut valve 1 (VDC/TCS hydraulic circuit).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1164 CV1"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1164 CV 1")

## C1165
- Description: Cut Valve 2 (CV2)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator cut valve 2.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1165 CV2"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1165 CV 2")

## C1166
- Description: Suction Valve 1 (SV1)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator suction valve 1.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1166 SV1"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1166 SV 1")

## C1167
- Description: Suction Valve 2 (SV2)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS actuator suction valve 2.
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1167 SV2"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1167 SV 2")

## C1170
- Description: Variant Coding
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: ABS control unit variant coding mismatch (incorrect coding for the vehicle).
- Grade: [A]
- Evidence: 2011 Nissan Armada FSM, BRC section (DTC index: "C1170 VARIANT CODING"); 2016 Nissan Juke FSM, BRC section (priority chart: "C1170 VARIANT CODING")

## C1176
- Description: Stop Lamp Switch 2
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Second stop lamp switch signal circuit.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BRC section (priority chart: "C1176 STOP LAMP SW2")

## C1704
- Description: Low Tire Pressure — Front LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low tire inflation pressure (at or below ~182–189 kPa / ~26–27 psi depending on model)
- Diagnostic notes: TPMS low-pressure warning. Check and adjust all tire pressures to specification, then drive at 40 km/h (25 MPH) or more for ~10 minutes and re-run BCM self-diagnosis.
- Grade: [A]
- Evidence: Nissan WT section FSM excerpts — 2012 QX (rmccurdy.com), WT.fm via documents.cdn.ifixit.com, Nissan Versa N17 via niveguide.com (DTC logic: "C1704 LOW PRESSURE FL"); 2016 Nissan Juke FSM, BCS section (DTC index: same)

## C1705
- Description: Low Tire Pressure — Front RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low tire inflation pressure
- Diagnostic notes: See C1704.
- Grade: [A]
- Evidence: Nissan WT section FSM excerpts (DTC logic: "C1705 LOW PRESSURE FR"); 2016 Nissan Juke FSM, BCS section (DTC index)

## C1706
- Description: Low Tire Pressure — Rear RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low tire inflation pressure
- Diagnostic notes: See C1704.
- Grade: [A]
- Evidence: Nissan WT section FSM excerpts (DTC logic: "C1706 LOW PRESSURE RR"); 2016 Nissan Juke FSM, BCS section (DTC index)

## C1707
- Description: Low Tire Pressure — Rear LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low tire inflation pressure
- Diagnostic notes: See C1704.
- Grade: [A]
- Evidence: Nissan WT section FSM excerpts (DTC logic: "C1707 LOW PRESSURE RL"); 2016 Nissan Juke FSM, BCS section (DTC index)

## C1708
- Description: Tire Pressure Transmitter — No Data, Front LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: No data received from the front LH tire pressure transmitter (ID registration or transmitter fault).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1708: [NO DATA] FL")

## C1709
- Description: Tire Pressure Transmitter — No Data, Front RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1708 (front RH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1709: [NO DATA] FR")

## C1710
- Description: Tire Pressure Transmitter — No Data, Rear RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1708 (rear RH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1710: [NO DATA] RR")

## C1711
- Description: Tire Pressure Transmitter — No Data, Rear LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1708 (rear LH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1711: [NO DATA] RL")

## C1716
- Description: Tire Pressure Transmitter — Pressure Data Error, Front LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Pressure data error from the front LH transmitter.
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1716: [PRESSDATA ERR] FL")

## C1717
- Description: Tire Pressure Transmitter — Pressure Data Error, Front RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1716 (front RH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1717: [PRESSDATA ERR] FR")

## C1718
- Description: Tire Pressure Transmitter — Pressure Data Error, Rear RH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1716 (rear RH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1718: [PRESSDATA ERR] RR")

## C1719
- Description: Tire Pressure Transmitter — Pressure Data Error, Rear LH
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: See C1716 (rear LH).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1719: [PRESSDATA ERR] RL")

## C1729
- Description: Vehicle Speed Signal Error (TPMS)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Vehicle speed signal error as seen by the tire pressure monitoring function (BCM).
- Grade: [A]
- Evidence: 2016 Nissan Juke FSM, BCS section (DTC index: "C1729: VHCL SPEED SIG ERR")

---

## U-codes (Nissan-specific)

No NEW Nissan-specific U1xxx codes were verified in this research pass. The
Nissan FSM sections checked (2008 Altima/Sentra EC, 2005 Titan EC, 2016 Juke
BCS, 2014 Note SEC) document only U1000, U1001, U1002, and U1010 (all already
in v1.2.1), plus U0415 (a generic SAE J2012 code, excluded per project rules).
Targeted searches for U1003+, U1011+, U1100-series, and U1110-series
Nissan-specific codes returned no verifiable Nissan sources. If Nissan uses
additional manufacturer-specific U-codes on newer models, they were not found
in the FSM excerpts and DTC databases consulted here.

---

## Coverage notes

### Counts
- New P-codes: 89 (51 grade A, 4 grade B, 34 grade C)
- New B-codes: 66 (all grade A)
- New C-codes: 46 (all grade A)
- New U-codes: 0 (none verified; see above)
- Total new codes: 201 (not in the v1.2.1 set of 73)

### Grade distribution
- A (FSM/TSB text): 163
- B (DTC database / multi-source): 4
- C (single community source): 34

### Conflicts found (reported inline above)
1. **P1550 (already in v1.2.1):** v1.2.1 lists P1550 as "TCC Solenoid Valve"
   (sr20-forum.com, SR20-era list), but the 2008 Altima FSM EC index lists
   P1550–P1554 as "BAT CURRENT SENSOR" (battery current sensor). The meaning
   is model/year-dependent; the integrator may want a year-split note on the
   existing P1550 entry.
2. **B1019:** 2007 Xterra FSM = "BELT TENSION SENS [UNIT FAIL]"; 2010 Altima
   SRC = "OCCUPANT SENS [OTHER FAIL]". Model/year-dependent.
3. **B1049/B1054:** 2007 Xterra FSM = DRIVER AIRBAG MODULE [OPEN] (incl. spiral
   cable), while community sources (JustAnswer) describe B1049 as
   front-passenger airbag/OCS/pretensioner faults. FSM wins per-vehicle.
4. **P1166/P1167, P1169/P1170, P1225/P1226, P1278/P1279, P1288/P1289,
   P1752/P1754, P1757/P1759, P1762/P1764, P1767/P1769, P1772/P1774:** source
   lists give paired codes identical descriptions; the FSMs group them without
   distinguishing sub-conditions. The distinct detection conditions live on
   the FSM diagnosis pages not excerpted here.

### Codes deliberately excluded (do not add without better evidence)
- **P1150, P1155, P1160** ("turbocharger wastegate" variants) — appear in the
  MyAirbags/UpFix list but are not Nissan codes (VW/Audi-style definitions);
  no Nissan FSM or DTC database corroborates them for Nissan/Infiniti.
- **P1243** ("supercharger bypass valve") — Ford-style code in the same list;
  no Nissan source found.
- **P1163** — entry truncated in the source list ("Heated oxygen sensor
  (HO2S)" with no bank/condition); a 2002 Frontier case confirms the code
  exists, but no reliable description was found. Thin area.
- **P1275, P1277** — in the MyAirbags/UpFix list ("A/F sensor 1 response
  time" / "slow response") but ABSENT from the 2005 Titan FSM's complete
  A/F sensor 1 family list (P1271/P1272/P1273/P1274/P1276/P1278/P1279/…);
  likely not real Nissan codes. Excluded.
- **P1089–P1093** — documented as Subaru (tumble generated valve) codes in
  the one detailed source found; no Nissan source. Do not confuse with
  Nissan's P-code space.
- **U0415** — appears in the 2016 Juke BCM index but is a generic SAE J2012
  code (belongs in dtc-generic.md, not here).

### Thin / unverified areas (searched, nothing verifiable found)
- **P1077/P1078** (exhaust valve timing, VQ37VHR): no source found.
- **B2015**: no source found.
- **B2111–B2115**: not in the 2014 Note / 2009 Altima SEC sections checked.
- **B2194, B2197, B2199**: no source found (Juke/Note indexes skip them).
- **B26F0, B26F5**: not in the Juke/Note indexes.
- **B2623, B2630, B2631** (sunload sensor): no source found.
- **B2609** (reported as steering-lock related on a GT-R35, single JustAnswer
  mention): too thin to include; candidate for a future pass.
- **C1112**: skipped in the Armada/Juke BRC indexes (C1111 → C1113).
- **Nissan-specific U1xxx beyond U1000/U1001/U1002/U1010**: none found.
- **Nissan-specific P2xxx**: none found — Nissan's manufacturer-specific
  powertrain codes live in P1xxx; P2xxx on Nissan are the generic SAE set.
- SRS codes **B1024–B1032, B1036–B1048** and side/curtain module codes
  (B1081–B1153) exist in FSMs but were outside this pass's target ranges.

### Source list (for the integrator's provenance field)
- 2008 Nissan Altima FSM, EC section (boredmder.com) — P-code DTC index,
  QR25DE/VQ35DE
- 2005 Nissan Titan FSM, EC section (scribd excerpt) — P-code DTC Inspection
  Priority Chart and fail-safe chart, VK56DE
- 2008 Nissan Sentra FSM, EC section (slideshare excerpt) — P-code DTC index
  (cross-check for P0850/P1225/P1226/P1421/P1564/P1572/P1574/P1715/P1740/
  P1777/P1778/P1805)
- 2007 Nissan Xterra FSM, SRS section (manuals.plus) — B-code CONSULT-II
  diagnostic code chart
- 2010 Nissan Altima SRC section (scribd excerpt) — B-code cross-check
  (B1017–B1023) and B1019 conflict source
- 2016 Nissan Juke FSM, BCS section (scribd excerpt) — B-code and C-code
  (TPMS) DTC index
- 2014 Nissan Note FSM, SEC section (scribd excerpt) — B210B–B2110,
  B2555–B2605, B26E8–B26FC DTC logic
- 2009 Nissan Altima FSM, SEC section (jdmfsm.info search excerpt) —
  B2108/B2109 DTC logic
- 2011 Nissan Armada FSM, BRC section (slideshare excerpt) — C-code DTC index
- 2016 Nissan Juke / 2015 QX60 BRC sections (scribd / manuals.plus excerpts)
  — C-code cross-checks
- Nissan WT section FSM excerpts (rmccurdy.com 2012 QX; documents.cdn.ifixit.com;
  niveguide.com Versa N17) — C1704–C1707 TPMS DTC logic
- eobdcode.com (Nissan P1032/P1110/P1143/P1144 pages), carobdcode.com
  (P1143/P1144), dtcsearch.com (P1144), swirlzcupcakes.com (P1111)
- MyAirbags/UpFix "Nissan/Infiniti Factory DTC Code Definitions" list
  (blog.myairbags.com / blog.upfix.com, 2016/2023) — single-source (C) basis
  for the unverified P-codes; known to contain some non-Nissan contamination
  (see exclusions above)
- JustAnswer Nissan technician threads (P1065, P1143/P1163, B1018, B1049/B1054,
  C1115, C1130) — community corroboration only
