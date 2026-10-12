# DTC catalog

Diagnostic trouble codes: SAE J2012 generic codes plus manufacturer-specific codes for the covered makes. Grade B/C: community and aftermarket sources — verify safety-critical diagnoses against factory service information.

## bmw — 45 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| 29CD | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29CE | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29CF | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29D0 | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29D1 | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29D2 | Misfire cylinder 1 / 2 / 3 / 4 / 5 / 6 | P | manufacturer | [C] | spark plug; ignition coil; injector; carbon buildup (N54 direct injection) | Per-cylinder misfire codes; N54 engine. Read companion fuel-mixture codes (29E0/29E1) before condemning ignition parts. |
| 29E0 | Fuel Mixture Control 1 / 2 | P | manufacturer | [C] | — | — |
| 29E1 | Fuel Mixture Control 1 / 2 | P | manufacturer | [C] | — | — |
| 29E2 | Fuel injection rail — pressure sensor signal | P | manufacturer | [C] | high-pressure fuel rail sensor; wiring | N54 direct-injection high-pressure side. |
| 2A7C | Intake VANOS solenoid fault | P | manufacturer | [C] | faulty or dirty intake VANOS solenoid; infrequent oil changes | A BMW technician (JustAnswer) notes the solenoids can be removed and cleaned as a first step; proper testing needs a BMW-specific scan tool. Solenoid electrical connectors can be swapped by mistake on reinstallation — verify routing. |
| 2A82 | VANOS intake — stiff; jammed mechanically | P | manufacturer | [A] | insufficient oil pressure supply to the intake VANOS adjustment unit; sticking VANOS solenoid; oil passages restricted | BMW SIB 11 02 08: faults set when the camshaft is "late" or does not reach target position in the specified time under all engine conditions; engine power may be reduced with a check-control message. Check oil quality/level and pressure before replacing solenoids. N52/N54 engines. |
| 2A87 | VANOS exhaust — stiff; jammed mechanically | P | manufacturer | [A] | insufficient oil pressure to the exhaust VANOS unit; sticking exhaust VANOS solenoid | Exhaust-side companion to 2A82 — same SIB, same diagnostic path. Tool32 MSD80 list phrases it as "outlet-Vanos variable cam control test, mechanics". N52/N54. |
| 2A94 | Crankshaft sensor — signal / synchronisation | P | manufacturer | [B] | crankshaft position sensor; wiring; trigger wheel damage | From the Tool32 MSD80 fault table. |
| 2A95 | Crankshaft sensor — signal / synchronisation | P | manufacturer | [B] | crankshaft position sensor; wiring; trigger wheel damage | From the Tool32 MSD80 fault table. |
| 2A98 | Crankshaft – inlet camshaft correlation / crankshaft – outlet camshaft correlation | P | manufacturer | [B] | timing chain stretch/jump; VANOS fault; sensor faults | Correlation codes point at mechanical timing rather than a single sensor. |
| 2A99 | Crankshaft – inlet camshaft correlation / crankshaft – outlet camshaft correlation | P | manufacturer | [B] | timing chain stretch/jump; VANOS fault; sensor faults | Correlation codes point at mechanical timing rather than a single sensor. |
| 2A9A | Camshaft sensor inlet — signal / camshaft sensor outlet — signal | P | manufacturer | [B] | camshaft position sensor; wiring | See 2A94. |
| 2A9B | Camshaft sensor inlet — signal / camshaft sensor outlet — signal | P | manufacturer | [B] | camshaft position sensor; wiring | See 2A94. |
| 2AAF | Fuel pump plausibility | P | manufacturer | [C] | low-pressure fuel pump delivery vs demand mismatch | N54; often accompanies HPFP issues. |
| 2B3A | DMTL pump fault (diagnosis module for tank leakage) | P | manufacturer | [C] | failed DMTL pump (in left rear fender liner); wiring | EVAP leak-detection pump; common failure, ~1 hour replacement per the technician source. The N54 CAN DME list phrases it "DMTL diagnosis module tank leakage, system failure". |
| 3100 | Boost pressure control — deactivation; boost pressure buildup prohibited | P | manufacturer | [B] | set as a consequential fault when VANOS or charge-air faults are present — not a root cause | INFORMATIONAL per BMW SIB 11 02 08 (listed as a secondary fault to 2A82/2A87, alongside 120408 "charge-air pressure control, cutout"). Do not chase as a turbo fault; fix the primary code first. N54. |
| 931D | KOMBI: Undervoltage or overvoltage | B | manufacturer | [C] | battery; alternator/charging system | Voltage faults cascade into many body codes — address charging system before chasing the others. |
| 93C3 | MRS: Seat-occupancy detector, passenger | B | manufacturer | [C] | passenger occupancy sensor mat; wiring under seat | SRS system — observe airbag safety precautions (battery disconnect, wait time) before probing. |
| 9CB5 | FRM: Battery exhausted (exhaustive-discharge protection: deactivation) | B | manufacturer | [C] | weak/dead battery; FRM load-shedding active | FRM shuts down lighting outputs to protect the battery — check battery/charging first; the lighting faults (A8AA/A8AC/A8B7…) are consequences. |
| A559 | KOMBI: Power supply switched off — closed-circuit current cutoff relay | B | manufacturer | [C] | parasitic drain countermeasure; battery rundown | Set when the car cuts terminal 30g loads due to low battery. |
| P1014 | Valvetronic reference — eccentric shaft sensor parity error | P | manufacturer | [C] | valvetronic eccentric shaft sensor shorted or poor electrical connection; valvetronic system electrical fault | Check-engine light on; valvetronic system is complex — professional diagnosis recommended per the source. |
| P1083 | Fuel Control Mixture Lean (Bank 1 Sensor 1) | P | manufacturer | [C] | — | — |
| P1084 | Fuel Control Mixture Rich (Bank 1 Sensor 1) | P | manufacturer | [C] | — | See P1083. |
| P1085 | Fuel Control Mixture Lean (Bank 2 Sensor 1) | P | manufacturer | [C] | — | See P1083. |
| P1086 | Fuel Control Mixture Rich (Bank 2 Sensor 1) | P | manufacturer | [C] | — | See P1083. |
| P1087 | O2 Sensor Circuit Slow Response in Lean Control Range (Bank 1 Sensor 1) | P | manufacturer | [C] | aging O2 sensor | Slow-response code — sensor still functions but is lazy. |
| P1088 | O2 Sensor Circuit Slow Response in Rich Control Range (Bank 1 Sensor 1) | P | manufacturer | [C] | aging O2 sensor | See P1087. |
| P1090 | Pre-Catalyst Fuel Trim Too Lean Bank 1 | P | manufacturer | [C] | — | Fuel-trim extreme — check for intake leaks before condemning sensors. |
| P1091 | Pre-Catalyst Fuel Trim Too Rich Bank 1 | P | manufacturer | [C] | — | See P1090. |
| P1092 | Pre-Catalyst Fuel Trim Too Lean Bank 2 | P | manufacturer | [C] | — | See P1090. |
| P1093 | Pre-Catalyst Fuel Trim Too Rich Bank 2 | P | manufacturer | [C] | — | See P1090. |
| P1111 | Engine Coolant Temperature Radiator Outlet Sensor Low Input | P | manufacturer | [C] | radiator outlet temp sensor circuit low | BMW uses a separate radiator-outlet temp sensor in addition to the engine coolant sensor. |
| P1112 | Engine Coolant Temperature Radiator Outlet Sensor High Input | P | manufacturer | [C] | radiator outlet temp sensor circuit high | See P1111. |
| P1115 | Coolant Temperature Sensor Plausibility | P | manufacturer | [C] | — | Plausibility code — compares redundant temp sensors; check both before replacing either. |
| P1120 | Pedal Position Sensor Circuit | P | manufacturer | [C] | — | — |
| P1121 | Pedal Position 1 Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1132 | O2 Sensor Heater Control Circuit (Bank 1 Sensor 1) | P | manufacturer | [C] | open/short in heater circuit; failed heater element | Check heater resistance at the sensor connector first. |
| P1133 | O2 Sensor Heater Control Circuit (Bank 2 Sensor 1) | P | manufacturer | [C] | open/short in heater circuit; failed heater element | See P1132. |
| P1318 | Camshaft Position Sensor 'B' Circuit Signal Duration after Initialization (Bank 1) | P | manufacturer | [C] | camshaft position sensor B (exhaust); wiring | BMW-specific code — generic scanners list no definition. Often appears with P0340/P0365. |
| P1339 | Camshaft Position Sensor 'B' Faulty Phase Position (Bank 1) | P | manufacturer | [C] | camshaft sensor B; timing/phase issue | See P1318. |

## ford — 182 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1202 | Fuel Pump and Sender Unit / Fuel Level Sensor Open Circuit | B | manufacturer | [C] | — | SCP-era body code (reported as 9202 in the older hex listing). |
| B1204 | Fuel Pump and Sender Unit / Fuel Level Sensor Short to Ground | B | manufacturer | [C] | — | — |
| B1213 | Anti-Theft Number of Programmed Keys Is Below Minimum | B | manufacturer | [B] | keys erased, PATS module replaced without key programming | Companion to P1260/P1269 — program the minimum key count with |
| B1231 | Crash Detected | B | manufacturer | [C] | actual collision event, RCM fault, battery disconnect with | Set by the restraints control module on crash input; can also |
| B1317 | Battery Voltage High (greater than ~16V) | B | manufacturer | [B] | overcharging alternator, voltage regulator fault | — |
| B1318 | Battery Voltage Low (less than ~10V) | B | manufacturer | [B] | discharged/failed battery (lost cell, low electrolyte), faulty | Extremely common "ghost" code — low system voltage during |
| B1342 | ECU Is Defective / ECU Internal Fault | B | manufacturer | [B] | — | CONFLICT — the older scribd Ford-Error-Codes listing attaches |
| B1359 | Ignition Run/Accessory Circuit Failure | B | manufacturer | [B] | — | B1351–B1366 cover the ignition key-in/run/start circuit family. |
| B2477 | Module Configuration Failure | B | manufacturer | [C] | — | — |
| C1100 | ABS Pump Switch Circuit Failure | C | manufacturer | [B] | — | C1100–C1115 cover the ABS pump/motor relay and power-relay circuits. |
| C1145 | Right Front Wheel Speed Sensor Input Circuit Failure | C | manufacturer | [B] | — | C1145–C1237 is the wheel-speed-sensor family: input circuit |
| C1155 | Left Front Wheel Speed Sensor Input Circuit Failure | C | manufacturer | [B] | — | — |
| C1165 | Right Rear Wheel Speed Sensor Input Circuit Failure | C | manufacturer | [B] | — | — |
| C1175 | Left Rear Wheel Speed Sensor Input Circuit Failure | C | manufacturer | [B] | — | — |
| C1233 | Left Front Wheel Speed Sensor Input Signal Missing | C | manufacturer | [B] | — | "Signal missing" subgroup (C1233–C1237, one per corner plus |
| C1284 | Oil Pressure Switch Failure | C | manufacturer | [B] | — | — |
| C1414 | Incorrect Module Design Level (fault PIDs may be available) | C | manufacturer | [B] | wrong module hardware/software level for the vehicle | Ford's note: additional fault PIDs may be available — check |
| C1415 | Incorrect Module Configuration | C | manufacturer | [B] | — | Companion to B2477 — configure with As-Built data. |
| P1000 | OBD-II Monitor Testing Incomplete | P | manufacturer | [B] | battery disconnected, KAM cleared, DTCs cleared with scan tool | Cannot be cleared with a scan tool — self-clears after a full |
| P1001 | KOER Test Cannot Be Completed | P | manufacturer | [B] | test aborted (see also P127A/P127B aborted-KOER codes) | — |
| P1100 | Mass Air Flow Sensor Circuit Intermittent | P | manufacturer | [B] | — | — |
| P1101 | Mass Air Flow Sensor Out of Self-Test Range | P | manufacturer | [B] | dirty/faulty MAF sensor, air intake leak | KOEO self-test artifact class — the MAF reading was outside |
| P1116 | Engine Coolant Temperature Sensor Out of Self-Test Range | P | manufacturer | [B] | engine not at expected temperature during test, ECT sensor fault | Self-test-range class — run the test on a fully warmed engine. |
| P1117 | Engine Coolant Temperature Sensor Circuit Intermittent | P | manufacturer | [B] | — | — |
| P1120 | Throttle Position Sensor Out of Range (RATCH too low) | P | manufacturer | [B] | — | — |
| P1121 | Throttle Position Sensor Inconsistent with MAF / MAP Sensor | P | manufacturer | [B] | — | Rationality check between TP and airflow — check both sensors, |
| P1124 | Throttle Position Sensor Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class. |
| P1125 | Throttle Position Sensor Circuit Intermittent | P | manufacturer | [B] | — | — |
| P1127 | Exhaust Not Warm Enough, Downstream HO2S Not Tested | P | manufacturer | [B] | short KOER run, exhaust not at operating temperature | KOER quirk — the downstream O2 monitor is skipped when the |
| P1130 | Lack of HO2S11 Switches — Fuel Trim at Limit (Bank 1) | P | manufacturer | [B] | same family as P1131 (lean-side causes) driven to the fuel-trim limit | The O2 sensor has hit its compensation limit — it is reporting |
| P1131 | Lack of HO2S11 Switch — Sensor Indicates Lean (Bank 1) | P | manufacturer | [B] | air intake leak after the MAF, vacuum/PCV hose leaks, base engine | Classic Ford lean code — usually NOT the sensor itself; the |
| P1132 | Lack of HO2S11 Switch — Sensor Indicates Rich (Bank 1) | P | manufacturer | [B] | — | Mirror of P1131 for the rich side. |
| P1137 | Lack of HO2S12 Switch — Sensor Indicates Lean (Bank 1, downstream) | P | manufacturer | [B] | — | — |
| P1138 | Lack of HO2S12 Switch — Sensor Indicates Rich (Bank 1, downstream) | P | manufacturer | [B] | — | — |
| P1150 | Lack of HO2S21 Switches — Adaptive Fuel at Limit (Bank 2) | P | manufacturer | [B] | bank-2 equivalents of the P1130 family | — |
| P1151 | Lack of HO2S21 Switch — Sensor Indicates Lean (Bank 2) | P | manufacturer | [B] | air intake system leaking, vacuum hoses leaking/damaged, air | Same as P1131, opposite bank. Ford-tech guidance: these codes |
| P1152 | Lack of HO2S21 Switch — Sensor Indicates Rich (Bank 2) | P | manufacturer | [B] | — | Mirror of P1131 for bank 2 rich side. |
| P1157 | Lack of HO2S22 Switch — Sensor Indicates Lean (Bank 2, downstream) | P | manufacturer | [B] | — | — |
| P1158 | Lack of HO2S22 Switch — Sensor Indicates Rich (Bank 2, downstream) | P | manufacturer | [B] | — | — |
| P115A | Low Fuel Level — Forced Limited Power | P | manufacturer | [B] | fuel level genuinely low | Strategy code, not a circuit fault — the PCM limits power to |
| P115B | Low Fuel Level — Forced Engine Shutdown | P | manufacturer | [B] | fuel level critically low | Strategy code — PCM shuts the engine down to protect the pump. |
| P1220 | Series Throttle Control System Fault | P | manufacturer | [B] | — | — |
| P1224 | Throttle Position Sensor B Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class (TP sensor B). |
| P1230 | Fuel Pump Low Speed Malfunction | P | manufacturer | [B] | — | — |
| P1231 | Fuel Pump Secondary Circuit Low / High Speed | P | manufacturer | [B] | — | — |
| P1232 | Fuel Pump Speed Primary Circuit Fault (two-speed fuel pump) | P | manufacturer | [B] | — | — |
| P1233 | Fuel Pump Driver Module Off-Line | P | manufacturer | [A] | FPDM lost power, tripped inertia fuel shutoff switch, failed | Per the Ford 2004 OBD System Operation Summary: Electronic |
| P1234 | Fuel Pump Driver Module Off-Line | P | manufacturer | [B] | — | Same description as P1233 in Ford's chart (duplicate code — |
| P1235 | Fuel Pump Control Out of Range | P | manufacturer | [B] | — | — |
| P1236 | Fuel Pump Control Out of Range | P | manufacturer | [B] | — | — |
| P1237 | Fuel Pump Secondary Circuit Fault (Fuel Pump Driver Module) | P | manufacturer | [B] | — | — |
| P1238 | Fuel Pump Primary Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1244 | Generator Load Input High | P | manufacturer | [B] | — | — |
| P1245 | Generator Load Input Low | P | manufacturer | [B] | — | — |
| P1246 | Generator Load Input Circuit Fault | P | manufacturer | [B] | — | — |
| P1247 | Turbo Boost Pressure Low | P | manufacturer | [B] | — | — |
| P1248 | Turbo Boost Pressure Not Detected | P | manufacturer | [B] | — | — |
| P1249 | Wastegate Control Valve Performance | P | manufacturer | [B] | — | — |
| P1250 | Lack of Power to FPRC Solenoid (Fuel Pressure Regulator Control) | P | manufacturer | [B] | — | CONFLICT — the 2008 Ford chart phrases it "SOLENOID (PRC) — |
| P1260 | Theft Detected — Engine Disabled | P | manufacturer | [B] | — | — |
| P1261 | Cylinder #1 High to Low Side Short (injector) | P | manufacturer | [B] | — | P1261–P1268 cover cylinders 1–8 high-to-low side injector |
| P1269 | Immobilizer Code Not Programmed | P | manufacturer | [B] | PATS key/PATS module not programmed to the PCM | Program keys with a PATS-capable tool; check B1213 (key count |
| P1270 | Engine RPM or Vehicle Speed Limiter Reached | P | manufacturer | [B] | not documented (strategy/event code) | Informational — set when the limiter intervened, not a fault. |
| P1285 | Cylinder Head Overtemperature Detected | P | manufacturer | [B] | — | Precursor to P1299 fail-safe cooling. |
| P1288 | Cylinder Head Temperature Sensor Out of Self-Test Range | P | manufacturer | [B] | faulty CHT sensor (most common per field reports), actual | Self-test-range class — but ALSO sets for genuine overheat |
| P1289 | Cylinder Head Temperature Sensor Signal Greater Than Self-Test Range (high input) | P | manufacturer | [B] | — | — |
| P1290 | Cylinder Head Temperature Sensor Signal Less Than Self-Test Range (low input) | P | manufacturer | [B] | — | — |
| P1299 | Cylinder Head Temperature Sensor Detected Engine Overheating Condition (fail-safe cooling active) | P | manufacturer | [B] | genuine overheating (low coolant, thermostat, water pump), | Fail-safe cooling strategy — the PCM alternately disables fuel |
| P1309 | Misfire Detection Monitor Not Enabled | P | manufacturer | [B] | — | — |
| P1351 | Ignition Diagnostic Monitor (IDM) Circuit Input Fault | P | manufacturer | [B] | — | P1351–P1364 cover IDM and ignition coil primary/secondary |
| P1356 | Loss of Ignition Diagnostic Module Input to PCM (PIP signal present while IDM indicates engine not turning) | P | manufacturer | [B] | — | — |
| P1359 | Spark Output (SAW) Circuit Fault | P | manufacturer | [B] | — | — |
| P1380 | Variable Cam Timing Solenoid Circuit Fault (short or open) | P | manufacturer | [B] | — | P1380–P1388 cover VCT solenoid circuits and over-advanced / |
| P1381 | Variable Cam Timing Over-Advanced (Bank A) | P | manufacturer | [B] | — | — |
| P1383 | Variable Cam Timing Over-Retarded (Bank A) | P | manufacturer | [B] | — | — |
| P1390 | Octane Adjust Out of Self-Test Range | P | manufacturer | [B] | — | Relates to Ford's octane-adjust feature (2008 chart notes the |
| P1400 | DPFE Sensor Circuit Low Voltage Detected | P | manufacturer | [B] | DPFE sensor fault, DPFE hose faults, wiring | The DPFE (Differential Pressure Feedback EGR) sensor and its |
| P1401 | DPFE Sensor Circuit High Voltage Detected | P | manufacturer | [B] | DPFE sensor fault, wiring | — |
| P1403 | DPFE Sensor Hoses Reversed | P | manufacturer | [B] | hoses swapped during service | Check the upstream/downstream hose routing at the DPFE sensor |
| P1405 | DPFE Sensor Upstream Hose — Plugged or Open | P | manufacturer | [B] | — | — |
| P1406 | DPFE Sensor Downstream Hose Off or Plugged | P | manufacturer | [B] | — | — |
| P1407 | EGR No Flow Detected | P | manufacturer | [B] | — | — |
| P1408 | EGR Flow Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class for EGR flow. |
| P1409 | EGR Vacuum Regulator (EVR) Circuit Fault | P | manufacturer | [B] | — | CONFLICT — the stdrivers Ford OBD-II list shows P1409 twice |
| P1411 | Secondary Air Injection — Incorrect Downstream Flow Detected | P | manufacturer | [B] | — | — |
| P1413 | Secondary Air Injection System Monitor Circuit Low Voltage | P | manufacturer | [B] | — | — |
| P1414 | Secondary Air Injection System Monitor Circuit High Voltage | P | manufacturer | [B] | — | — |
| P1442 | Secondary Air Injection System Monitor Circuit High Voltage | P | manufacturer | [B] | — | CONFLICT — generic OBD-II references assign P1442 to EVAP |
| P1443 | EVAP Purge Control Solenoid / Purge Control Valve Fault | P | manufacturer | [B] | faulty canister purge flow sensor / purge solenoid, carbon-clogged | Classic Ford EVAP code (1990s–2000s). On older models the |
| P1444 | EVAP Purge Flow Sensor Circuit Low Input | P | manufacturer | [B] | — | — |
| P1445 | EVAP Purge Flow Sensor Circuit High Input | P | manufacturer | [B] | — | — |
| P1450 | Unable to Bleed Up Fuel Tank Vacuum (EVAP) | P | manufacturer | [B] | stuck-open canister purge valve/solenoid (most common), | The stuck-open purge valve classically causes hard starting |
| P1451 | EVAP Control System Canister Vent Solenoid Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1452 | Unable to Bleed Up Fuel Tank Vacuum (EVAP) | P | manufacturer | [B] | — | Same description as P1450 in Ford's chart. |
| P1455 | EVAP System — Substantial Leak or Blockage Detected (gross leak / no flow) | P | manufacturer | [B] | — | — |
| P1460 | Wide Open Throttle A/C Cutoff (WAC) Circuit Fault | P | manufacturer | [B] | — | — |
| P1461 | A/C Pressure Sensor Circuit Low Input | P | manufacturer | [B] | — | — |
| P1462 | A/C Pressure Sensor Circuit High Input | P | manufacturer | [B] | — | — |
| P1463 | A/C Pressure Sensor — Insufficient Pressure Change | P | manufacturer | [B] | — | — |
| P1464 | A/C Switch On During Self-Test | P | manufacturer | [B] | operator left A/C on during KOEO/KOER | Test-procedure artifact — switch the A/C off and rerun the |
| P1469 | Low Air Conditioning Cycling Period | P | manufacturer | [B] | — | — |
| P1473 | Fan Secondary Monitor Circuit High with Fans Off | P | manufacturer | [B] | — | P1473–P1484 cover the cooling-fan primary/secondary monitor |
| P1474 | Low Fan Control Primary Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1479 | High Fan Control Primary Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1480 | Fan Secondary Monitor Circuit Low with Low Fan On | P | manufacturer | [B] | — | — |
| P1481 | Fan Secondary Monitor Circuit Low with High Fan On | P | manufacturer | [B] | — | — |
| P1500 | Vehicle Speed Sensor Intermittent | P | manufacturer | [B] | — | P1500–P1503 cover VSS intermittent/malfunction variants. |
| P1504 | Idle Air Control Circuit Malfunction | P | manufacturer | [B] | — | P1504–P1509 cover IAC circuit/adaptive-clip/over/under-speed faults. |
| P1506 | Idle Air Control Over-Speed Error | P | manufacturer | [B] | — | — |
| P1507 | Idle Air Control Under-Speed Error | P | manufacturer | [B] | — | — |
| P1512 | Intake Manifold Runner Control Stuck Closed (Bank 1) | P | manufacturer | [B] | — | P1512–P1520/P1537/P1538 cover the IMRC stuck-open/closed and |
| P1518 | Intake Manifold Runner Control Stuck Open (Bank 1) | P | manufacturer | [B] | — | — |
| P1520 | Intake Manifold Runner Control Circuit Fault | P | manufacturer | [B] | — | — |
| P1530 | A/C System Fault (A/C clutch circuit open or short) | P | manufacturer | [B] | — | — |
| P1537 | Intake Manifold Runner Control Stuck Open (Bank 1) | P | manufacturer | [B] | — | — |
| P1538 | Intake Manifold Runner Control Stuck Open (Bank 2) | P | manufacturer | [B] | — | — |
| P1550 | Power Steering Pressure Sensor/Switch Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class — cycle the steering during KOER (part |
| P1600 | Loss of KAM (Keep Alive Memory) Power | P | manufacturer | [B] | battery disconnected, KAM fuse open, PCM power interruption | Expected after any battery disconnect — clear and retest. |
| P1602 | Immobilizer Module – PCM Communication Fault | P | manufacturer | [B] | — | PATS network fault class — see also U-codes (U1262 SCP). |
| P1605 | PCM Keep Alive Memory Test Error | P | manufacturer | [B] | — | — |
| P1610 | PCM Reprogramming Error / Immobilizer Code Words Do Not Match | P | manufacturer | [B] | interrupted module programming, PATS code-word mismatch | P1610–P1624 cover PCM/PATS reprogramming errors and |
| P1625 | Voltage to Vehicle Load Control Module Fan Circuit Not Detected | P | manufacturer | [B] | — | — |
| P1632 | Smart Alternator Fault (sensor/circuit) | P | manufacturer | [B] | smart-charge alternator circuit fault, wiring | — |
| P1633 | Power Supply to the KAM Fuse (KAPWR circuit) | P | manufacturer | [B] | KAM fuse open, KAPWR circuit fault | — |
| P1635 | Tire / Axle Out of Acceptable Range | P | manufacturer | [B] | — | — |
| P1639 | PCM Vehicle Identification Block Corrupted or Not Programmed | P | manufacturer | [B] | — | — |
| P1640 | Powertrain DTCs Available in Another Control Module | P | manufacturer | [B] | — | Pointer code — query the other powertrain module (e.g. TCM) |
| P1650 | Power Steering Pressure Switch Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class (see P1550). |
| P1651 | Power Steering Pressure Switch Input Fault | P | manufacturer | [B] | — | — |
| P1700 | Transmission Failed to Engage Neutral / Transmission Control System Malfunction | P | manufacturer | [B] | internal transmission fault, TCM fault/communication | Generic transmission pointer on older Fords — often accompanied |
| P1701 | Reverse Engagement Error | P | manufacturer | [B] | — | — |
| P1702 | Transmission Range Sensor Circuit Intermittent | P | manufacturer | [B] | — | — |
| P1703 | Brake Switch Out of Self-Test Range | P | manufacturer | [B] | faulty brake switch signal, water/corrosion damage to switch or wiring | Self-test-range class — the BOO (brake on/off) input must |
| P1704 | Digital Transmission Range Sensor Failed to Transition State | P | manufacturer | [B] | — | — |
| P1705 | Manual Lever Position / Transmission Range Sensor Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class. |
| P1709 | Park/Neutral Position Switch Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class. |
| P1711 | Transmission Fluid Temperature Sensor Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class. |
| P1728 | Transmission Slip Fault | P | manufacturer | [B] | — | — |
| P1729 | 4x4 Low Switch Error / Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1740 | Torque Converter Clutch System — Performance or Mechanically Stuck Off | P | manufacturer | [B] | TCC solenoid electrical fault or contamination, low/dirty | TCC slip is evaluated functionally under steady-state lockup. |
| P1741 | Torque Converter Clutch Control Error | P | manufacturer | [B] | — | — |
| P1742 | Torque Converter Clutch Solenoid Failed On | P | manufacturer | [B] | — | Companion to P1743 (both listed as "failed on" in Ford's chart). |
| P1743 | Torque Converter Clutch Solenoid Failed On | P | manufacturer | [B] | — | — |
| P1744 | Torque Converter Clutch System Stuck in Off Position (performance) | P | manufacturer | [B] | low transmission fluid, contaminated fluid, damaged/malfunctioning | The TCC solenoid is checked functionally: if converter slip |
| P1746 | Electronic Pressure Control Solenoid — Open Circuit | P | manufacturer | [B] | — | P1746–P1749/P1760 cover EPC solenoid open/short/failed-low faults. |
| P1747 | Electronic Pressure Control Solenoid — Short Circuit | P | manufacturer | [B] | — | — |
| P1749 | Electronic Pressure Control Solenoid Failed Low | P | manufacturer | [B] | — | — |
| P1751 | Shift Solenoid #1 Performance / Functional Fault | P | manufacturer | [B] | — | — |
| P1754 | Coast Clutch Solenoid Circuit Malfunction / Electrical Fault | P | manufacturer | [B] | — | — |
| P1756 | Shift Solenoid #2 Performance / Functional Fault | P | manufacturer | [B] | — | — |
| P1760 | Electronic Pressure Control Solenoid Short Circuit | P | manufacturer | [B] | — | — |
| P1762 | Overdrive Band Failed Off | P | manufacturer | [B] | — | — |
| P1780 | Transmission Control Switch / Overdrive Cancel Circuit Out of Self-Test Range | P | manufacturer | [B] | misaligned/faulty transmission range sensor (TRS), O/D cancel | Self-test-range class. Inspect the TRS on the transmission |
| P1781 | 4x4 Low Switch Out of Self-Test Range | P | manufacturer | [B] | — | Self-test-range class. |
| P1783 | Transmission Over-Temperature Condition | P | manufacturer | [B] | — | — |
| P1784 | Transmission Mechanical Failure — First and Reverse | P | manufacturer | [B] | — | Internal mechanical fault class (P1784–P1787). |
| P1785 | Transmission Mechanical Failure — First and Second | P | manufacturer | [B] | — | — |
| P1786 | 3-2 Downshift Error | P | manufacturer | [B] | — | — |
| P1787 | 2-1 Downshift Error | P | manufacturer | [B] | — | — |
| P1788 | Coast Clutch Solenoid Open Circuit | P | manufacturer | [B] | — | — |
| P1789 | Coast Clutch Solenoid Short Circuit | P | manufacturer | [B] | — | — |
| P1800 | Transmission Clutch Interlock Safety Switch Circuit Failure | P | manufacturer | [B] | — | P1800–P1803 cover the clutch-interlock safety switch circuits |
| P1804 | Four Wheel Drive High Indicator Circuit Failure | P | manufacturer | [B] | — | P1804–P1899 cover the 4WD transfer-case family: high/low |
| P1812 | Four Wheel Drive Mode Select Circuit Failure | P | manufacturer | [B] | — | — |
| P1828 | Transmission Transfer Case High-to-Low Shift Relay Coil Circuit Failure | P | manufacturer | [B] | — | — |
| P1838 | Transmission Transfer Case Shift Motor Circuit Failure | P | manufacturer | [B] | — | — |
| P1867 | Transmission Transfer Case Contact Plate General Circuit Failure | P | manufacturer | [B] | — | Representative of the P1846–P1865 contact-plate A–D circuit family. |
| P1900 | Output Shaft Speed Sensor Intermittent | P | manufacturer | [B] | — | — |
| P1901 | Turbine Shaft Speed Sensor Intermittent | P | manufacturer | [B] | — | — |
| P1A00 | Transmission Generator Brake Failure (hybrid) | P | manufacturer | [B] | — | P1A00–P1A15 are Ford hybrid (Escape Hybrid eCVT) codes: |
| P1A0C | Hybrid Powertrain Control Module — Engine Disabled | P | manufacturer | [B] | — | — |
| U0100 | Lost Communication with ECM / PCM | U | manufacturer | [B] | CAN wiring fault, PCM power/ground fault, failed PCM, gateway fault | The foundational CAN-era network code. When multiple U-codes |
| U0101 | Lost Communication with TCM | U | manufacturer | [B] | — | — |
| U0121 | Lost Communication with ABS Control Module | U | manufacturer | [B] | — | — |
| U0140 | Lost Communication with BCM | U | manufacturer | [B] | — | — |
| U0155 | Lost Communication with Instrument Panel Cluster (IPC) Control Module | U | manufacturer | [B] | — | — |
| U1262 | SCP (J1850) Data Link Fault / Communication Bus Fault | U | manufacturer | [B] | — | — |
| U1451 | Anti-Theft Status Signal Missing — Engine Disabled | U | manufacturer | [B] | — | PATS network status code — companion to P1260. |
| U1900 | SCP (J1850) Communication Bus Fault | U | manufacturer | [B] | instrument-cluster solder-joint failure (Focus Mk2-era), | Field quirk (Focus Mk2): both communication buses route |
| U2012 | CAN Communication Bus Fault (missing messages) | U | manufacturer | [B] | — | — |
| U2023 | Fault Received from External Node | U | manufacturer | [B] | — | — |
| U3000 | Control Module (general module fault) | U | manufacturer | [B] | — | Generic module-fault pointer; U3001–U3011 refine it (improper |

## generic — 2098 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B0001 | PCM Discrete Input Speed Signal Error | B | generic | [C] | — | — |
| B0004 | PCM Discrete Input Speed Signal Not Present | B | generic | [C] | — | — |
| B0005 | In Park Switch Circuit Malfunction | B | generic | [C] | — | — |
| B0016 | RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Resistance Low | B | generic | [C] | — | — |
| B0017 | RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Open | B | generic | [C] | — | — |
| B0018 | RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0022 | LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Resistance Low | B | generic | [C] | — | — |
| B0024 | LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0026 | LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Open | B | generic | [C] | — | — |
| B0028 | RF/Passenger Side Deployment Loop Resistance Low | B | generic | [C] | — | — |
| B0029 | RF/Passenger Side Deployment Loop Open | B | generic | [C] | — | — |
| B0030 | RF/Passenger Side Deployment Loop Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0035 | ADS Closed/Shorted to Ground | B | generic | [C] | — | — |
| B0036 | ADS Open/Missing/Shorted to Battery | B | generic | [C] | — | — |
| B0037 | AUX switch closed/shorted to ground | B | generic | [C] | — | — |
| B0038 | AUX switch open/shorted to battery | B | generic | [C] | — | — |
| B0040 | LF/Driver Side Deployment Loop Resistance Low | B | generic | [C] | — | — |
| B0041 | LF/Driver Side Deployment Loop Open | B | generic | [C] | — | — |
| B0045 | LF Side Deploy Loop Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0051 | Deployment Commanded | B | generic | [C] | — | — |
| B0053 | Deployment Commanded with Loop Malfunctions Present | B | generic | [C] | — | — |
| B0057 | RF/Passenger Pretensioner Deployment Loop Resistance Low | B | generic | [C] | — | — |
| B0058 | RF/Passenger Pretensioner Deployment Loop Open | B | generic | [C] | — | — |
| B0059 | RF/Passenger Pretensioner Deployment Loop Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0064 | LF/Driver Pretensioner Deployment Loop Resistance Low | B | generic | [C] | — | — |
| B0065 | LF/Driver Pretensioner Deployment Loop Open | B | generic | [C] | — | — |
| B0066 | LF/Driver Pretensioner Deployment Loop Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0073 | Supplemental Deployment Loop #1 Resistance Low | B | generic | [C] | — | — |
| B0074 | Supplemental Deployment Loop #1 Open | B | generic | [C] | — | — |
| B0075 | Supplemental Deployment Loop #1 Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0077 | LF/Driver SIS Malfunction | B | generic | [C] | — | — |
| B0078 | RF/Passenger SIS Malfunction | B | generic | [C] | — | — |
| B0079 | Incorrect LF/Driver SIS Installed | B | generic | [C] | — | — |
| B0080 | Discard LF/Driver SIS | B | generic | [C] | — | — |
| B0081 | Incorrect RF/Passenger SIS Installed | B | generic | [C] | — | — |
| B0082 | Discard RF/Passenger SIS | B | generic | [C] | — | — |
| B0086 | Supplemental Deployment Loop #2 Resistance Low | B | generic | [C] | — | — |
| B0087 | Supplemental Deployment Loop #2 Open | B | generic | [C] | — | — |
| B0088 | Supplemental Deployment Loop #2 Short to Ground/Voltage Out of Range | B | generic | [C] | — | — |
| B0090 | Active switch voltage out of range | B | generic | [C] | — | — |
| B0091 | Active switch: wrong state | B | generic | [C] | — | — |
| B0092 | PPS passenger detection error | B | generic | [C] | — | — |
| B0093 | PPS/CPS self-test malfunction | B | generic | [C] | — | — |
| B0094 | CPS childseat detection error | B | generic | [C] | — | — |
| B0095 | SDM-PPS/CPS mismatch malfunction | B | generic | [C] | — | — |
| C0000 | Vehicle Speed Information Circuit Malfunction | C | generic | [C] | — | — |
| C0035 | Left Front Wheel Speed Circuit Malfunction | C | generic | [C] | — | — |
| C0040 | Right Front Wheel Speed Circuit Malfunction | C | generic | [C] | — | — |
| C0041 | Right Front Wheel Speed Sensor Circuit Range/Performance (EBCM) | C | generic | [C] | — | — |
| C0045 | Left Rear Wheel Speed Circuit Malfunction | C | generic | [C] | — | — |
| C0046 | Left Rear Wheel Speed Sensor Circuit Range/Performance (EBCM) | C | generic | [C] | — | — |
| C0050 | Right Rear Wheel Speed Circuit Malfunction | C | generic | [C] | — | — |
| C0051 | LF Wheel Speed Sensor Circuit Range/Performance (EBCM) | C | generic | [C] | — | — |
| C0060 | Left Front ABS Solenoid #1 Circuit Malfunction | C | generic | [C] | — | — |
| C0065 | Left Front ABS Solenoid #2 Circuit Malfunction | C | generic | [C] | — | — |
| C0070 | Right Front ABS Solenoid #1 Circuit Malfunction | C | generic | [C] | — | — |
| C0075 | Right Front ABS Solenoid #2 Circuit Malfunction | C | generic | [C] | — | — |
| C0080 | Left Rear ABS Solenoid #1 Circuit Malfunction | C | generic | [C] | — | — |
| C0085 | Left Rear ABS Solenoid #2 Circuit Malfunction | C | generic | [C] | — | — |
| C0090 | Right Rear ABS Solenoid #1 Circuit Malfunction | C | generic | [C] | — | — |
| C0095 | Right Rear ABS Solenoid #2 Circuit Malfunction | C | generic | [C] | — | — |
| C0110 | Pump Motor Circuit Malfunction | C | generic | [C] | — | — |
| C0121 | Valve Relay Circuit Malfunction | C | generic | [C] | — | — |
| C0128 | Low Brake Fluid Circuit Low | C | generic | [C] | — | — |
| P0001 | Fuel Volume Regulator Control Circuit/Open | P | generic | [C] | — | — |
| P0002 | Fuel Volume Regulator Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0003 | Fuel Volume Regulator Control Circuit Low | P | generic | [C] | — | — |
| P0004 | Fuel Volume Regulator Control Circuit High | P | generic | [C] | — | — |
| P0005 | Fuel Shutoff Valve Control Circuit/Open | P | generic | [C] | — | — |
| P0006 | Fuel Shutoff Valve Control Circuit Low | P | generic | [C] | — | — |
| P0007 | Fuel Shutoff Valve Control Circuit High | P | generic | [C] | — | — |
| P0008 | Engine Position System Performance (Bank 1) | P | generic | [C] | — | — |
| P0009 | Engine Position System Performance (Bank 2) | P | generic | [C] | — | — |
| P0010 | A Camshaft Position Actuator Circuit (Bank 1) | P | generic | [C] | — | — |
| P0011 | A Camshaft Position - Timing Over-Advanced or System Performance (Bank 1) | P | generic | [B] | low, dirty, or wrong-viscosity engine oil (leading cause - VVT is hydraulically actuated); stuck oil control valve (OCV)/VVT solenoid; failed camshaft phaser; sludged oil passages; stretched timing chain; faulty camshaft position sensor | Change oil and filter with the exact specified viscosity first - resolves many cases; then remove and test the oil control valve (clean or replace); if symptoms persist, evaluate cam phaser and timing chain |
| P0012 | A Camshaft Position - Timing Over-Retarded (Bank 1) | P | generic | [C] | — | — |
| P0013 | B Camshaft Position - Actuator Circuit (Bank 1) | P | generic | [C] | — | — |
| P0014 | B Camshaft Position - Timing Over-Advanced or System Performance (Bank 1) | P | generic | [C] | — | — |
| P0015 | B Camshaft Position - Timing Over-Retarded (Bank 1) | P | generic | [C] | — | — |
| P0016 | Crankshaft Position - Camshaft Position Correlation (Bank 1 Sensor A) | P | generic | [C] | — | — |
| P0017 | Crankshaft Position - Camshaft Position Correlation (Bank 1 Sensor B) | P | generic | [C] | — | — |
| P0018 | Crankshaft Position - Camshaft Position Correlation (Bank 2 Sensor A) | P | generic | [C] | — | — |
| P0019 | Crankshaft Position - Camshaft Position Correlation (Bank 2 Sensor B) | P | generic | [C] | — | — |
| P0020 | A Camshaft Position Actuator Circuit (Bank 2) | P | generic | [C] | — | — |
| P0021 | A Camshaft Position - Timing Over-Advanced or System Performance (Bank 2) | P | generic | [C] | — | — |
| P0022 | A Camshaft Position - Timing Over-Retarded (Bank 2) | P | generic | [C] | — | — |
| P0023 | B Camshaft Position - Actuator Circuit (Bank 2) | P | generic | [C] | — | — |
| P0024 | B Camshaft Position - Timing Over-Advanced or System Performance (Bank 2) | P | generic | [C] | — | — |
| P0025 | B Camshaft Position - Timing Over-Retarded (Bank 2) | P | generic | [C] | — | — |
| P0026 | Intake Valve Control Solenoid Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P0027 | Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P0028 | Intake Valve Control Solenoid Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P0029 | Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P0030 | HO2S Heater Control Circuit (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0031 | HO2S Heater Control Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0032 | HO2S Heater Control Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0033 | Turbo Charger Bypass Valve Control Circuit | P | generic | [C] | — | — |
| P0034 | Turbo Charger Bypass Valve Control Circuit Low | P | generic | [C] | — | — |
| P0035 | Turbo Charger Bypass Valve Control Circuit High | P | generic | [C] | — | — |
| P0036 | HO2S Heater Control Circuit (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P0037 | HO2S Heater Control Circuit Low (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P0038 | HO2S Heater Control Circuit High (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P0039 | Turbo/Super Charger Bypass Valve Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0040 | O2 Sensor Signals Swapped Bank 1 Sensor 1 / Bank 2 Sensor 1 | P | generic | [C] | — | — |
| P0041 | O2 Sensor Signals Swapped Bank 1 Sensor 2 / Bank 2 Sensor 2 | P | generic | [C] | — | — |
| P0042 | HO2S Heater Control Circuit (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P0043 | HO2S Heater Control Circuit Low (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P0044 | HO2S Heater Control Circuit High (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P0045 | Turbo/Super Charger Boost Control Solenoid Circuit/Open | P | generic | [C] | — | — |
| P0046 | Turbo/Super Charger Boost Control Solenoid Circuit Range/Performance | P | generic | [C] | — | — |
| P0047 | Turbo/Super Charger Boost Control Solenoid Circuit Low | P | generic | [C] | — | — |
| P0048 | Turbo/Super Charger Boost Control Solenoid Circuit High | P | generic | [C] | — | — |
| P0049 | Turbo/Super Charger Turbine Overspeed | P | generic | [C] | — | — |
| P0050 | HO2S Heater Control Circuit (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0051 | HO2S Heater Control Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0052 | HO2S Heater Control Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0053 | HO2S Heater Resistance (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0054 | HO2S Heater Resistance (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P0055 | HO2S Heater Resistance (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P0056 | HO2S Heater Control Circuit (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P0057 | HO2S Heater Control Circuit Low (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P0058 | HO2S Heater Control Circuit High (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P0059 | HO2S Heater Resistance (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0060 | HO2S Heater Resistance (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P0061 | HO2S Heater Resistance (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P0062 | HO2S Heater Control Circuit (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P0063 | HO2S Heater Control Circuit Low (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P0064 | HO2S Heater Control Circuit High (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P0065 | Air Assisted Injector Control Range/Performance | P | generic | [C] | — | — |
| P0066 | Air Assisted Injector Control Circuit or Circuit Low | P | generic | [C] | — | — |
| P0067 | Air Assisted Injector Control Circuit High | P | generic | [C] | — | — |
| P0068 | MAP/MAF - Throttle Position Correlation | P | generic | [C] | — | — |
| P0069 | Manifold Absolute Pressure - Barometric Pressure Correlation | P | generic | [C] | — | — |
| P0070 | Ambient Air Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0071 | Ambient Air Temperature Sensor Range/Performance | P | generic | [C] | — | — |
| P0072 | Ambient Air Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0073 | Ambient Air Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0074 | Ambient Air Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0075 | Intake Valve Control Solenoid Circuit (Bank 1) | P | generic | [C] | — | — |
| P0076 | Intake Valve Control Solenoid Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P0077 | Intake Valve Control Solenoid Circuit High (Bank 1) | P | generic | [C] | — | — |
| P0078 | Exhaust Valve Control Solenoid Circuit (Bank 1) | P | generic | [C] | — | — |
| P0079 | Exhaust Valve Control Solenoid Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P0080 | Exhaust Valve Control Solenoid Circuit High (Bank 1) | P | generic | [C] | — | — |
| P0081 | Intake Valve Control Solenoid Circuit (Bank 2) | P | generic | [C] | — | — |
| P0082 | Intake Valve Control Solenoid Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P0083 | Intake Valve Control Solenoid Circuit High (Bank 2) | P | generic | [C] | — | — |
| P0084 | Exhaust Valve Control Solenoid Circuit (Bank 2) | P | generic | [C] | — | — |
| P0085 | Exhaust Valve Control Solenoid Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P0086 | Exhaust Valve Control Solenoid Circuit High (Bank 2) | P | generic | [C] | — | — |
| P0087 | Fuel Rail/System Pressure - Too Low | P | generic | [C] | — | — |
| P0088 | Fuel Rail/System Pressure - Too High | P | generic | [C] | — | — |
| P0089 | Fuel Pressure Regulator 1 Performance | P | generic | [C] | — | — |
| P0090 | Fuel Pressure Regulator 1 Control Circuit | P | generic | [C] | — | — |
| P0091 | Fuel Pressure Regulator 1 Control Circuit Low | P | generic | [C] | — | — |
| P0092 | Fuel Pressure Regulator 1 Control Circuit High | P | generic | [C] | — | — |
| P0093 | Fuel System Leak Detected - Large Leak | P | generic | [C] | — | — |
| P0094 | Fuel System Leak Detected - Small Leak | P | generic | [C] | — | — |
| P0095 | Intake Air Temperature Sensor 2 Circuit | P | generic | [C] | — | — |
| P0096 | Intake Air Temperature Sensor 2 Circuit Range/Performance | P | generic | [C] | — | — |
| P0097 | Intake Air Temperature Sensor 2 Circuit Low | P | generic | [C] | — | — |
| P0098 | Intake Air Temperature Sensor 2 Circuit High | P | generic | [C] | — | — |
| P0099 | Intake Air Temperature Sensor 2 Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P0100 | Mass or Volume Air Flow Circuit Malfunction | P | generic | [B] | disconnected MAF electrical plug; damaged wiring at the plug; defective or damaged MAF sensor; corroded or loose electrical terminals in MAF circuit | Inspect MAF connector and wiring first before replacing the sensor |
| P0101 | Mass or Volume Air Flow Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0102 | Mass or Volume Air Flow Circuit Low Input | P | generic | [B] | — | — |
| P0103 | Mass or Volume Air Flow Circuit High Input | P | generic | [B] | — | — |
| P0104 | Mass or Volume Air Flow Circuit Intermittent | P | generic | [B] | — | — |
| P0105 | Manifold Absolute Pressure/Barometric Pressure Circuit Malfunction | P | generic | [B] | — | — |
| P0106 | Manifold Absolute Pressure/Barometric Pressure Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0107 | Manifold Absolute Pressure/Barometric Pressure Circuit Low Input | P | generic | [B] | — | — |
| P0108 | Manifold Absolute Pressure/Barometric Pressure Circuit High Input | P | generic | [B] | — | — |
| P0109 | Manifold Absolute Pressure/Barometric Pressure Circuit Intermittent | P | generic | [B] | — | — |
| P0110 | Intake Air Temperature Circuit Malfunction | P | generic | [B] | — | — |
| P0111 | Intake Air Temperature Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0112 | Intake Air Temperature Circuit Low Input | P | generic | [B] | — | — |
| P0113 | Intake Air Temperature Circuit High Input | P | generic | [B] | — | — |
| P0114 | Intake Air Temperature Circuit Intermittent | P | generic | [B] | — | — |
| P0115 | Engine Coolant Temperature Circuit Malfunction | P | generic | [B] | — | — |
| P0116 | Engine Coolant Temperature Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0117 | Engine Coolant Temperature Circuit Low Input | P | generic | [B] | — | — |
| P0118 | Engine Coolant Temperature Circuit High Input | P | generic | [B] | — | — |
| P0119 | Engine Coolant Temperature Circuit Intermittent | P | generic | [B] | — | — |
| P0120 | Throttle Position Sensor/Switch A Circuit Malfunction | P | generic | [B] | — | — |
| P0121 | Throttle Position Sensor/Switch A Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0122 | Throttle Position Sensor/Switch A Circuit Low Input | P | generic | [B] | — | — |
| P0123 | Throttle Position Sensor/Switch A Circuit High Input | P | generic | [B] | — | — |
| P0124 | Throttle Position Sensor/Switch A Circuit Intermittent | P | generic | [B] | — | — |
| P0125 | Insufficient Coolant Temperature for Closed Loop Fuel Control | P | generic | [B] | — | — |
| P0126 | Insufficient Coolant Temperature for Stable Operation | P | generic | [B] | — | — |
| P0127 | Intake Air Temperature Too High | P | generic | [C] | — | — |
| P0128 | Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature) | P | generic | [B] | thermostat stuck open | ECT never reaches regulating temperature; check thermostat operation |
| P0129 | Barometric Pressure Low | P | generic | [C] | — | — |
| P0130 | O2 Sensor Circuit Malfunction (Bank 1 Sensor 1) | P | generic | [B] | B1S1 oxygen sensor not showing proper activity; wiring fault | ECM changes fuel management strategy when set; fuel economy will suffer |
| P0131 | O2 Sensor Circuit Low Voltage (Bank 1 Sensor 1) | P | generic | [B] | — | — |
| P0132 | O2 Sensor Circuit High Voltage (Bank 1 Sensor 1) | P | generic | [B] | — | — |
| P0133 | O2 Sensor Circuit Slow Response (Bank 1 Sensor 1) | P | generic | [B] | — | — |
| P0134 | O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1) | P | generic | [B] | — | — |
| P0135 | O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1) | P | generic | [B] | — | — |
| P0136 | O2 Sensor Circuit Malfunction (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0137 | O2 Sensor Circuit Low Voltage (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0138 | O2 Sensor Circuit High Voltage (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0139 | O2 Sensor Circuit Slow Response (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0140 | O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0141 | O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2) | P | generic | [B] | — | — |
| P0142 | O2 Sensor Circuit Malfunction (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0143 | O2 Sensor Circuit Low Voltage (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0144 | O2 Sensor Circuit High Voltage (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0145 | O2 Sensor Circuit Slow Response (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0146 | O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0147 | O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 3) | P | generic | [B] | — | — |
| P0148 | Fuel Delivery Error | P | generic | [C] | — | — |
| P0149 | Fuel Timing Error | P | generic | [C] | — | — |
| P0150 | O2 Sensor Circuit Malfunction (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0151 | O2 Sensor Circuit Low Voltage (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0152 | O2 Sensor Circuit High Voltage (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0153 | O2 Sensor Circuit Slow Response (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0154 | O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0155 | O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 1) | P | generic | [B] | — | — |
| P0156 | O2 Sensor Circuit Malfunction (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0157 | O2 Sensor Circuit Low Voltage (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0158 | O2 Sensor Circuit High Voltage (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0159 | O2 Sensor Circuit Slow Response (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0160 | O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0161 | O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 2) | P | generic | [B] | — | — |
| P0162 | O2 Sensor Circuit Malfunction (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0163 | O2 Sensor Circuit Low Voltage (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0164 | O2 Sensor Circuit High Voltage (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0165 | O2 Sensor Circuit Slow Response (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0166 | O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0167 | O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 3) | P | generic | [B] | — | — |
| P0168 | Fuel Temperature Too High | P | generic | [C] | — | — |
| P0169 | Incorrect Fuel Composition | P | generic | [C] | — | — |
| P0170 | Fuel Trim Malfunction (Bank 1) | P | generic | [B] | oxygen sensor feedback driving trim out of range | Check whether O2 sensors are calling for more or less fuel (positive vs negative trim) |
| P0171 | System too Lean (Bank 1) | P | generic | [B] | vacuum leaks; faulty MAF sensor; weak fuel pump | Compare fuel trims at idle vs under load - vacuum leaks show at idle, fuel delivery issues show under load |
| P0172 | System too Rich (Bank 1) | P | generic | [B] | — | — |
| P0173 | Fuel Trim Malfunction (Bank 2) | P | generic | [B] | — | — |
| P0174 | System too Lean (Bank 2) | P | generic | [B] | — | — |
| P0175 | System too Rich (Bank 2) | P | generic | [B] | — | — |
| P0176 | Fuel Composition Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0177 | Fuel Composition Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0178 | Fuel Composition Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0179 | Fuel Composition Sensor Circuit High Input | P | generic | [B] | — | — |
| P0180 | Fuel Temperature Sensor A Circuit Malfunction | P | generic | [B] | — | — |
| P0181 | Fuel Temperature Sensor A Circuit Range/Performance | P | generic | [B] | — | — |
| P0182 | Fuel Temperature Sensor A Circuit Low Input | P | generic | [B] | — | — |
| P0183 | Fuel Temperature Sensor A Circuit High Input | P | generic | [B] | — | — |
| P0184 | Fuel Temperature Sensor A Circuit Intermittent | P | generic | [B] | — | — |
| P0185 | Fuel Temperature Sensor B Circuit Malfunction | P | generic | [B] | — | — |
| P0186 | Fuel Temperature Sensor B Circuit Range/Performance | P | generic | [B] | — | — |
| P0187 | Fuel Temperature Sensor B Circuit Low Input | P | generic | [B] | — | — |
| P0188 | Fuel Temperature Sensor B Circuit High Input | P | generic | [B] | — | — |
| P0189 | Fuel Temperature Sensor B Circuit Intermittent | P | generic | [B] | — | — |
| P0190 | Fuel Rail Pressure Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0191 | Fuel Rail Pressure Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0192 | Fuel Rail Pressure Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0193 | Fuel Rail Pressure Sensor Circuit High Input | P | generic | [B] | — | — |
| P0194 | Fuel Rail Pressure Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0195 | Engine Oil Temperature Sensor Malfunction | P | generic | [B] | — | — |
| P0196 | Engine Oil Temperature Sensor Range/Performance | P | generic | [B] | — | — |
| P0197 | Engine Oil Temperature Sensor Low | P | generic | [B] | — | — |
| P0198 | Engine Oil Temperature Sensor High | P | generic | [B] | — | — |
| P0199 | Engine Oil Temperature Sensor Intermittent | P | generic | [B] | — | — |
| P0200 | Injector Circuit Malfunction | P | generic | [B] | — | — |
| P0201 | Injector Circuit Malfunction - Cylinder 1 | P | generic | [B] | — | — |
| P0202 | Injector Circuit Malfunction - Cylinder 2 | P | generic | [B] | — | — |
| P0203 | Injector Circuit Malfunction - Cylinder 3 | P | generic | [B] | — | — |
| P0204 | Injector Circuit Malfunction - Cylinder 4 | P | generic | [B] | — | — |
| P0205 | Injector Circuit Malfunction - Cylinder 5 | P | generic | [B] | — | — |
| P0206 | Injector Circuit Malfunction - Cylinder 6 | P | generic | [B] | — | — |
| P0207 | Injector Circuit Malfunction - Cylinder 7 | P | generic | [B] | — | — |
| P0208 | Injector Circuit Malfunction - Cylinder 8 | P | generic | [B] | — | — |
| P0209 | Injector Circuit Malfunction - Cylinder 9 | P | generic | [B] | — | — |
| P0210 | Injector Circuit Malfunction - Cylinder 10 | P | generic | [B] | — | — |
| P0211 | Injector Circuit Malfunction - Cylinder 11 | P | generic | [B] | — | — |
| P0212 | Injector Circuit Malfunction - Cylinder 12 | P | generic | [B] | — | — |
| P0213 | Cold Start Injector 1 Malfunction | P | generic | [B] | — | — |
| P0214 | Cold Start Injector 2 Malfunction | P | generic | [B] | — | — |
| P0215 | Engine Shutoff Solenoid Malfunction | P | generic | [B] | — | — |
| P0216 | Injection Timing Control Circuit Malfunction | P | generic | [B] | — | — |
| P0217 | Engine Coolant Over Temperature Condition | P | generic | [C] | — | — |
| P0218 | Transmission Over Temperature Condition | P | generic | [B] | — | — |
| P0219 | Engine Overspeed Condition | P | generic | [B] | — | — |
| P0220 | Throttle/Petal Position Sensor/Switch B Circuit Malfunction | P | generic | [B] | — | — |
| P0221 | Throttle/Petal Position Sensor/Switch B Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0222 | Throttle/Petal Position Sensor/Switch B Circuit Low Input | P | generic | [B] | — | — |
| P0223 | Throttle/Petal Position Sensor/Switch B Circuit High Input | P | generic | [B] | — | — |
| P0224 | Throttle/Petal Position Sensor/Switch B Circuit Intermittent | P | generic | [B] | — | — |
| P0225 | Throttle/Petal Position Sensor/Switch C Circuit Malfunction | P | generic | [B] | — | — |
| P0226 | Throttle/Petal Position Sensor/Switch C Circuit Range/Performance Problem | P | generic | [B] | — | — |
| P0227 | Throttle/Petal Position Sensor/Switch C Circuit Low Input | P | generic | [B] | — | — |
| P0228 | Throttle/Petal Position Sensor/Switch C Circuit High Input | P | generic | [B] | — | — |
| P0229 | Throttle/Petal Position Sensor/Switch C Circuit Intermittent | P | generic | [B] | — | — |
| P0230 | Fuel Pump Primary Circuit Malfunction | P | generic | [B] | — | — |
| P0231 | Fuel Pump Secondary Circuit Low | P | generic | [B] | — | — |
| P0232 | Fuel Pump Secondary Circuit High | P | generic | [B] | — | — |
| P0233 | Fuel Pump Secondary Circuit Intermittent | P | generic | [B] | — | — |
| P0234 | Engine Overboost Condition | P | generic | [B] | — | — |
| P0235 | Turbocharger Boost Sensor A Circuit Malfunction | P | generic | [B] | — | — |
| P0236 | Turbocharger Boost Sensor A Circuit Range/Performance | P | generic | [B] | — | — |
| P0237 | Turbocharger Boost Sensor A Circuit Low | P | generic | [B] | — | — |
| P0238 | Turbocharger Boost Sensor A Circuit High | P | generic | [B] | — | — |
| P0239 | Turbocharger Boost Sensor B Malfunction | P | generic | [B] | — | — |
| P0240 | Turbocharger Boost Sensor B Circuit Range/Performance | P | generic | [B] | — | — |
| P0241 | Turbocharger Boost Sensor B Circuit Low | P | generic | [B] | — | — |
| P0242 | Turbocharger Boost Sensor B Circuit High | P | generic | [B] | — | — |
| P0243 | Turbocharger Wastegate Solenoid A Malfunction | P | generic | [B] | — | — |
| P0244 | Turbocharger Wastegate Solenoid A Range/Performance | P | generic | [B] | — | — |
| P0245 | Turbocharger Wastegate Solenoid A Low | P | generic | [B] | — | — |
| P0246 | Turbocharger Wastegate Solenoid A High | P | generic | [B] | — | — |
| P0247 | Turbocharger Wastegate Solenoid B Malfunction | P | generic | [B] | — | — |
| P0248 | Turbocharger Wastegate Solenoid B Range/Performance | P | generic | [B] | — | — |
| P0249 | Turbocharger Wastegate Solenoid B Low | P | generic | [B] | — | — |
| P0250 | Turbocharger Wastegate Solenoid B High | P | generic | [B] | — | — |
| P0251 | Injection Pump Fuel Metering Control "A" Malfunction (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0252 | Injection Pump Fuel Metering Control "A" Range/Performance (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0253 | Injection Pump Fuel Metering Control "A" Low (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0254 | Injection Pump Fuel Metering Control "A" High (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0255 | Injection Pump Fuel Metering Control "A" Intermittent (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0256 | Injection Pump Fuel Metering Control "B" Malfunction (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0257 | Injection Pump Fuel Metering Control "B" Range/Performance (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0258 | Injection Pump Fuel Metering Control "B" Low (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0259 | Injection Pump Fuel Metering Control "B" High (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0260 | Injection Pump Fuel Metering Control "B" Intermittent (Cam/Rotor/Injector) | P | generic | [B] | — | — |
| P0261 | Cylinder 1 Injector Circuit Low | P | generic | [B] | — | — |
| P0262 | Cylinder 1 Injector Circuit High | P | generic | [B] | — | — |
| P0263 | Cylinder 1 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0264 | Cylinder 2 Injector Circuit Low | P | generic | [B] | — | — |
| P0265 | Cylinder 2 Injector Circuit High | P | generic | [B] | — | — |
| P0266 | Cylinder 2 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0267 | Cylinder 3 Injector Circuit Low | P | generic | [B] | — | — |
| P0268 | Cylinder 3 Injector Circuit High | P | generic | [B] | — | — |
| P0269 | Cylinder 3 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0270 | Cylinder 4 Injector Circuit Low | P | generic | [B] | — | — |
| P0271 | Cylinder 4 Injector Circuit High | P | generic | [B] | — | — |
| P0272 | Cylinder 4 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0273 | Cylinder 5 Injector Circuit Low | P | generic | [B] | — | — |
| P0274 | Cylinder 5 Injector Circuit High | P | generic | [B] | — | — |
| P0275 | Cylinder 5 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0276 | Cylinder 6 Injector Circuit Low | P | generic | [B] | — | — |
| P0277 | Cylinder 6 Injector Circuit High | P | generic | [B] | — | — |
| P0278 | Cylinder 6 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0279 | Cylinder 7 Injector Circuit Low | P | generic | [B] | — | — |
| P0280 | Cylinder 7 Injector Circuit High | P | generic | [B] | — | — |
| P0281 | Cylinder 7 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0282 | Cylinder 8 Injector Circuit Low | P | generic | [B] | — | — |
| P0283 | Cylinder 8 Injector Circuit High | P | generic | [B] | — | — |
| P0284 | Cylinder 8 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0285 | Cylinder 9 Injector Circuit Low | P | generic | [B] | — | — |
| P0286 | Cylinder 9 Injector Circuit High | P | generic | [B] | — | — |
| P0287 | Cylinder 9 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0288 | Cylinder 10 Injector Circuit Low | P | generic | [B] | — | — |
| P0289 | Cylinder 10 Injector Circuit High | P | generic | [B] | — | — |
| P0290 | Cylinder 10 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0291 | Cylinder 11 Injector Circuit Low | P | generic | [B] | — | — |
| P0292 | Cylinder 11 Injector Circuit High | P | generic | [B] | — | — |
| P0293 | Cylinder 11 Contribution/Balance Fault | P | generic | [B] | — | — |
| P0294 | Cylinder 12 Injector Circuit Low | P | generic | [B] | — | — |
| P0295 | Cylinder 12 Injector Circuit High | P | generic | [B] | — | — |
| P0296 | Cylinder 12 Contribution/Range Fault | P | generic | [B] | — | — |
| P0297 | Vehicle Overspeed Condition | P | generic | [C] | — | — |
| P0298 | Engine Oil Over Temperature | P | generic | [C] | — | — |
| P0299 | Turbo/Super Charger Underboost | P | generic | [C] | — | — |
| P0300 | Random/Multiple Cylinder Misfire Detected | P | generic | [B] | worn spark plugs; faulty ignition coil(s); vacuum leak; low fuel pressure | Check freeze-frame for the conditions when set; mode $06 misfire counters per cylinder narrow it to the offending cylinder(s) |
| P0301 | Cylinder 1 Misfire Detected | P | generic | [B] | — | — |
| P0302 | Cylinder 2 Misfire Detected | P | generic | [B] | — | — |
| P0303 | Cylinder 3 Misfire Detected | P | generic | [B] | bad ignition coil; worn spark plug; faulty fuel injector; valve train issue | Swap coil/plug to another cylinder to see if the misfire follows the part |
| P0304 | Cylinder 4 Misfire Detected | P | generic | [B] | bad ignition coil; worn spark plug; faulty fuel injector; valve train issue | Swap coil/plug to another cylinder to see if the misfire follows the part |
| P0305 | Cylinder 5 Misfire Detected | P | generic | [B] | — | — |
| P0306 | Cylinder 6 Misfire Detected | P | generic | [B] | — | — |
| P0307 | Cylinder 7 Misfire Detected | P | generic | [B] | — | — |
| P0308 | Cylinder 8 Misfire Detected | P | generic | [B] | — | — |
| P0309 | Cylinder 9 Misfire Detected | P | generic | [B] | — | — |
| P0310 | Cylinder 10 Misfire Detected | P | generic | [B] | — | — |
| P0311 | Cylinder 11 Misfire Detected | P | generic | [B] | — | — |
| P0312 | Cylinder 12 Misfire Detected | P | generic | [B] | — | — |
| P0313 | Misfire Detected with Low Fuel | P | generic | [C] | — | — |
| P0314 | Single Cylinder Misfire (Cylinder not Specified) | P | generic | [C] | — | — |
| P0315 | Crankshaft Position System Variation Not Learned | P | generic | [C] | — | — |
| P0316 | Engine Misfire Detected on Startup (First 1000 Revolutions) | P | generic | [C] | — | — |
| P0317 | Rough Road Hardware Not Present | P | generic | [C] | — | — |
| P0318 | Rough Road Sensor "A" Signal Circuit | P | generic | [C] | — | — |
| P0319 | Rough Road Sensor "B" Signal Circuit | P | generic | [C] | — | — |
| P0320 | Ignition/Distributor Engine Speed Input Circuit Malfunction | P | generic | [B] | — | — |
| P0321 | Ignition/Distributor Engine Speed Input Circuit Range/Performance | P | generic | [B] | — | — |
| P0322 | Ignition/Distributor Engine Speed Input Circuit No Signal | P | generic | [B] | — | — |
| P0323 | Ignition/Distributor Engine Speed Input Circuit Intermittent | P | generic | [B] | — | — |
| P0324 | Knock Control System Error | P | generic | [C] | — | — |
| P0325 | Knock Sensor 1 Circuit Malfunction (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0326 | Knock Sensor 1 Circuit Range/Performance (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0327 | Knock Sensor 1 Circuit Low Input (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0328 | Knock Sensor 1 Circuit High Input (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0329 | Knock Sensor 1 Circuit Intermittent (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0330 | Knock Sensor 2 Circuit Malfunction (Bank 2) | P | generic | [B] | — | — |
| P0331 | Knock Sensor 2 Circuit Range/Performance (Bank 2) | P | generic | [B] | — | — |
| P0332 | Knock Sensor 2 Circuit Low Input (Bank 2) | P | generic | [B] | — | — |
| P0333 | Knock Sensor 2 Circuit High Input (Bank 2) | P | generic | [B] | — | — |
| P0334 | Knock Sensor 2 Circuit Intermittent (Bank 2) | P | generic | [B] | — | — |
| P0335 | Crankshaft Position Sensor A Circuit Malfunction | P | generic | [B] | — | — |
| P0336 | Crankshaft Position Sensor A Circuit Range/Performance | P | generic | [B] | — | — |
| P0337 | Crankshaft Position Sensor A Circuit Low Input | P | generic | [B] | — | — |
| P0338 | Crankshaft Position Sensor A Circuit High Input | P | generic | [B] | — | — |
| P0339 | Crankshaft Position Sensor A Circuit Intermittent | P | generic | [B] | — | — |
| P0340 | Camshaft Position Sensor A Circuit Malfunction (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0341 | Camshaft Position Sensor A Circuit Range/Performance (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0342 | Camshaft Position Sensor A Circuit Low Input (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0343 | Camshaft Position Sensor A Circuit High Input (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0344 | Camshaft Position Sensor A Circuit Intermittent (Bank 1 or Single Sensor) | P | generic | [B] | — | — |
| P0345 | Camshaft Position Sensor A Circuit Malfunction (Bank 2) | P | generic | [B] | — | — |
| P0346 | Camshaft Position Sensor A Circuit Range/Performance (Bank 2) | P | generic | [B] | — | — |
| P0347 | Camshaft Position Sensor A Circuit Low Input (Bank 2) | P | generic | [B] | — | — |
| P0348 | Camshaft Position Sensor A Circuit High Input (Bank 2) | P | generic | [B] | — | — |
| P0349 | Camshaft Position Sensor A Circuit Intermittent (Bank 2) | P | generic | [B] | — | — |
| P0350 | Ignition Coil Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0351 | Ignition Coil A Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0352 | Ignition Coil B Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0353 | Ignition Coil C Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0354 | Ignition Coil D Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0355 | Ignition Coil E Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0356 | Ignition Coil F Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0357 | Ignition Coil G Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0358 | Ignition Coil H Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0359 | Ignition Coil I Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0360 | Ignition Coil J Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0361 | Ignition Coil K Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0362 | Ignition Coil L Primary/Secondary Circuit Malfunction | P | generic | [B] | — | — |
| P0363 | Misfire Detected - Fueling Disabled | P | generic | [C] | — | — |
| P0364 | Reserved | P | generic | [C] | — | — |
| P0365 | Camshaft Position Sensor "B" Circuit (Bank 1) | P | generic | [C] | — | — |
| P0366 | Camshaft Position Sensor "B" Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P0367 | Camshaft Position Sensor "B" Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P0368 | Camshaft Position Sensor "B" Circuit High (Bank 1) | P | generic | [C] | — | — |
| P0369 | Camshaft Position Sensor "B" Circuit Intermittent (Bank 1) | P | generic | [C] | — | — |
| P0370 | Timing Reference High Resolution Signal A Malfunction | P | generic | [B] | — | — |
| P0371 | Timing Reference High Resolution Signal A Too Many Pulses | P | generic | [B] | — | — |
| P0372 | Timing Reference High Resolution Signal A Too Few Pulses | P | generic | [B] | — | — |
| P0373 | Timing Reference High Resolution Signal A Intermittent/Erratic Pulses | P | generic | [B] | — | — |
| P0374 | Timing Reference High Resolution Signal A No Pulses | P | generic | [B] | — | — |
| P0375 | Timing Reference High Resolution Signal B Malfunction | P | generic | [B] | — | — |
| P0376 | Timing Reference High Resolution Signal B Too Many Pulses | P | generic | [B] | — | — |
| P0377 | Timing Reference High Resolution Signal B Too Few Pulses | P | generic | [B] | — | — |
| P0378 | Timing Reference High Resolution Signal B Intermittent/Erratic Pulses | P | generic | [B] | — | — |
| P0379 | Timing Reference High Resolution Signal B No Pulses | P | generic | [B] | — | — |
| P0380 | Glow Plug/Heater Circuit "A" Malfunction | P | generic | [B] | — | — |
| P0381 | Glow Plug/Heater Indicator Circuit Malfunction | P | generic | [B] | — | — |
| P0382 | Glow Plug/Heater Circuit "B" Malfunction | P | generic | [B] | — | — |
| P0385 | Crankshaft Position Sensor B Circuit Malfunction | P | generic | [B] | — | — |
| P0386 | Crankshaft Position Sensor B Circuit Range/Performance | P | generic | [B] | — | — |
| P0387 | Crankshaft Position Sensor B Circuit Low Input | P | generic | [B] | — | — |
| P0388 | Crankshaft Position Sensor B Circuit High Input | P | generic | [B] | — | — |
| P0389 | Crankshaft Position Sensor B Circuit Intermittent | P | generic | [B] | — | — |
| P0390 | Camshaft Position Sensor "B" Circuit (Bank 2) | P | generic | [C] | — | — |
| P0391 | Camshaft Position Sensor "B" Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P0392 | Camshaft Position Sensor "B" Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P0393 | Camshaft Position Sensor "B" Circuit High (Bank 2) | P | generic | [C] | — | — |
| P0394 | Camshaft Position Sensor "B" Circuit Intermittent (Bank 2) | P | generic | [C] | — | — |
| P0400 | Exhaust Gas Recirculation Flow Malfunction | P | generic | [B] | — | — |
| P0401 | Exhaust Gas Recirculation Flow Insufficient Detected | P | generic | [B] | clogged EGR valve or EGR passages | Inspect and clean the EGR valve; use a scan tool to monitor EGR sensor readings |
| P0402 | Exhaust Gas Recirculation Flow Excessive Detected | P | generic | [B] | — | — |
| P0403 | Exhaust Gas Recirculation Circuit Malfunction | P | generic | [B] | — | — |
| P0404 | Exhaust Gas Recirculation Circuit Range/Performance | P | generic | [B] | — | — |
| P0405 | Exhaust Gas Recirculation Sensor A Circuit Low | P | generic | [B] | — | — |
| P0406 | Exhaust Gas Recirculation Sensor A Circuit High | P | generic | [B] | — | — |
| P0407 | Exhaust Gas Recirculation Sensor B Circuit Low | P | generic | [B] | — | — |
| P0408 | Exhaust Gas Recirculation Sensor B Circuit High | P | generic | [B] | — | — |
| P0410 | Secondary Air Injection System Malfunction | P | generic | [B] | — | — |
| P0411 | Secondary Air Injection System Incorrect Flow Detected | P | generic | [B] | — | — |
| P0412 | Secondary Air Injection System Switching Valve A Circuit Malfunction | P | generic | [B] | — | — |
| P0413 | Secondary Air Injection System Switching Valve A Circuit Open | P | generic | [B] | — | — |
| P0414 | Secondary Air Injection System Switching Valve A Circuit Shorted | P | generic | [B] | — | — |
| P0415 | Secondary Air Injection System Switching Valve B Circuit Malfunction | P | generic | [B] | — | — |
| P0416 | Secondary Air Injection System Switching Valve B Circuit Open | P | generic | [B] | — | — |
| P0417 | Secondary Air Injection System Switching Valve B Circuit Shorted | P | generic | [B] | — | — |
| P0418 | Secondary Air Injection System Relay "A" Circuit Malfunction | P | generic | [B] | — | — |
| P0419 | Secondary Air Injection System Relay "B" Circuit Malfunction | P | generic | [B] | — | — |
| P0420 | Catalyst System Efficiency Below Threshold (Bank 1) | P | generic | [B] | failing catalytic converter; inefficient oxygen sensor; exhaust leak | Compare upstream vs downstream O2 sensor waveforms before condemning the converter |
| P0421 | Warm Up Catalyst Efficiency Below Threshold (Bank 1) | P | generic | [B] | — | — |
| P0422 | Main Catalyst Efficiency Below Threshold (Bank 1) | P | generic | [B] | — | — |
| P0423 | Heated Catalyst Efficiency Below Threshold (Bank 1) | P | generic | [B] | — | — |
| P0424 | Heated Catalyst Temperature Below Threshold (Bank 1) | P | generic | [B] | — | — |
| P0425 | Catalyst Temperature Sensor (Bank 1) | P | generic | [C] | — | — |
| P0426 | Catalyst Temperature Sensor Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P0427 | Catalyst Temperature Sensor Low (Bank 1) | P | generic | [C] | — | — |
| P0428 | Catalyst Temperature Sensor High (Bank 1) | P | generic | [C] | — | — |
| P0429 | Catalyst Heater Control Circuit (Bank 1) | P | generic | [C] | — | — |
| P0430 | Catalyst System Efficiency Below Threshold (Bank 2) | P | generic | [B] | — | — |
| P0431 | Warm Up Catalyst Efficiency Below Threshold (Bank 2) | P | generic | [B] | — | — |
| P0432 | Main Catalyst Efficiency Below Threshold (Bank 2) | P | generic | [B] | — | — |
| P0433 | Heated Catalyst Efficiency Below Threshold (Bank 2) | P | generic | [B] | — | — |
| P0434 | Heated Catalyst Temperature Below Threshold (Bank 2) | P | generic | [B] | — | — |
| P0435 | Catalyst Temperature Sensor (Bank 2) | P | generic | [C] | — | — |
| P0436 | Catalyst Temperature Sensor Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P0437 | Catalyst Temperature Sensor Low (Bank 2) | P | generic | [C] | — | — |
| P0438 | Catalyst Temperature Sensor High (Bank 2) | P | generic | [C] | — | — |
| P0439 | Catalyst Heater Control Circuit (Bank 2) | P | generic | [C] | — | — |
| P0440 | Evaporative Emission Control System Malfunction | P | generic | [B] | — | — |
| P0441 | Evaporative Emission Control System Incorrect Purge Flow | P | generic | [B] | — | — |
| P0442 | Evaporative Emission Control System Leak Detected (small leak) | P | generic | [B] | loose or damaged gas cap; small EVAP system leak | Check the gas cap first; smoke-test the EVAP system to find the leak |
| P0443 | Evaporative Emission Control System Purge Control Valve Circuit | P | generic | [B] | — | — |
| P0444 | Evaporative Emission Control System Purge Control Valve Circuit Open | P | generic | [B] | — | — |
| P0445 | Evaporative Emission Control System Purge Control Valve Circuit Shorted | P | generic | [B] | — | — |
| P0446 | Evaporative Emission Control System Vent Control Circuit Malfunction | P | generic | [B] | EVAP canister vent solenoid/valve fault; wiring fault | Test the vent valve/solenoid circuit per the service manual |
| P0447 | Evaporative Emission Control System Vent Control Circuit Open | P | generic | [B] | — | — |
| P0448 | Evaporative Emission Control System Vent Control Circuit Shorted | P | generic | [B] | — | — |
| P0449 | Evaporative Emission Control System Vent Valve/Solenoid Circuit Malfunction | P | generic | [B] | — | — |
| P0450 | Evaporative Emission Control System Pressure Sensor Malfunction | P | generic | [B] | — | — |
| P0451 | Evaporative Emission Control System Pressure Sensor Range/Performance | P | generic | [B] | — | — |
| P0452 | Evaporative Emission Control System Pressure Sensor Low Input | P | generic | [B] | — | — |
| P0453 | Evaporative Emission Control System Pressure Sensor High Input | P | generic | [B] | — | — |
| P0454 | Evaporative Emission Control System Pressure Sensor Intermittent | P | generic | [B] | — | — |
| P0455 | Evaporative Emission Control System Leak Detected (gross leak) | P | generic | [B] | — | — |
| P0456 | Evaporative Emission Control System Leak Detected (very small leak) | P | generic | [C] | — | — |
| P0457 | Evaporative Emission Control System Leak Detected (fuel cap loose/off) | P | generic | [C] | — | — |
| P0458 | Evaporative Emission System Purge Control Valve Circuit Low | P | generic | [C] | — | — |
| P0459 | Evaporative Emission System Purge Control Valve Circuit High | P | generic | [C] | — | — |
| P0460 | Fuel Level Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0461 | Fuel Level Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0462 | Fuel Level Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0463 | Fuel Level Sensor Circuit High Input | P | generic | [B] | — | — |
| P0464 | Fuel Level Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0465 | Purge Flow Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0466 | Purge Flow Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0467 | Purge Flow Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0468 | Purge Flow Sensor Circuit High Input | P | generic | [B] | — | — |
| P0469 | Purge Flow Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0470 | Exhaust Pressure Sensor Malfunction | P | generic | [B] | — | — |
| P0471 | Exhaust Pressure Sensor Range/Performance | P | generic | [B] | — | — |
| P0472 | Exhaust Pressure Sensor Low | P | generic | [B] | — | — |
| P0473 | Exhaust Pressure Sensor High | P | generic | [B] | — | — |
| P0474 | Exhaust Pressure Sensor Intermittent | P | generic | [B] | — | — |
| P0475 | Exhaust Pressure Control Valve Malfunction | P | generic | [B] | — | — |
| P0476 | Exhaust Pressure Control Valve Range/Performance | P | generic | [B] | — | — |
| P0477 | Exhaust Pressure Control Valve Low | P | generic | [B] | — | — |
| P0478 | Exhaust Pressure Control Valve High | P | generic | [B] | — | — |
| P0479 | Exhaust Pressure Control Valve Intermittent | P | generic | [B] | — | — |
| P0480 | Cooling Fan 1 Control Circuit Malfunction | P | generic | [B] | — | — |
| P0481 | Cooling Fan 2 Control Circuit Malfunction | P | generic | [B] | — | — |
| P0482 | Cooling Fan 3 Control Circuit Malfunction | P | generic | [B] | — | — |
| P0483 | Cooling Fan Rationality Check Malfunction | P | generic | [B] | — | — |
| P0484 | Cooling Fan Circuit Over Current | P | generic | [B] | — | — |
| P0485 | Cooling Fan Power/Ground Circuit Malfunction | P | generic | [B] | — | — |
| P0486 | Exhaust Gas Recirculation Sensor B Circuit | P | generic | [C] | — | — |
| P0487 | Exhaust Gas Recirculation Throttle Position Control Circuit | P | generic | [C] | — | — |
| P0488 | Exhaust Gas Recirculation Throttle Position Control Range/Performance | P | generic | [C] | — | — |
| P0489 | Exhaust Gas Recirculation Control Circuit Low | P | generic | [C] | — | — |
| P0490 | Exhaust Gas Recirculation Control Circuit High | P | generic | [C] | — | — |
| P0491 | Secondary Air Injection System (Bank 1) | P | generic | [C] | — | — |
| P0492 | Secondary Air Injection System (Bank 2) | P | generic | [C] | — | — |
| P0493 | Fan Overspeed | P | generic | [C] | — | — |
| P0494 | Fan Speed Low | P | generic | [C] | — | — |
| P0495 | Fan Speed High | P | generic | [C] | — | — |
| P0496 | Evaporative Emission System High Purge Flow | P | generic | [C] | — | — |
| P0497 | Evaporative Emission System Low Purge Flow | P | generic | [C] | — | — |
| P0498 | Evaporative Emission System Vent Valve Control Circuit Low | P | generic | [C] | — | — |
| P0499 | Evaporative Emission System Vent Valve Control Circuit High | P | generic | [C] | — | — |
| P0500 | Vehicle Speed Sensor Malfunction | P | generic | [B] | faulty vehicle speed sensor; wiring fault | May affect cruise control and speedometer readings; check sensor signal with a scan tool |
| P0501 | Vehicle Speed Sensor Range/Performance | P | generic | [B] | — | — |
| P0502 | Vehicle Speed Sensor Low Input | P | generic | [B] | — | — |
| P0503 | Vehicle Speed Sensor Intermittent/Erratic/High | P | generic | [B] | — | — |
| P0504 | Brake Switch A/B Correlation | P | generic | [C] | — | — |
| P0505 | Idle Control System Malfunction | P | generic | [B] | — | — |
| P0506 | Idle Control System RPM Lower Than Expected | P | generic | [B] | — | — |
| P0507 | Idle Control System RPM Higher Than Expected | P | generic | [B] | — | — |
| P0508 | Idle Air Control System Circuit Low | P | generic | [C] | — | — |
| P0509 | Idle Air Control System Circuit High | P | generic | [C] | — | — |
| P0510 | Closed Throttle Position Switch Malfunction | P | generic | [B] | — | — |
| P0511 | Idle Air Control Circuit | P | generic | [C] | — | — |
| P0512 | Starter Request Circuit | P | generic | [C] | — | — |
| P0513 | Incorrect Immobilizer Key | P | generic | [C] | — | — |
| P0514 | Battery Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0515 | Battery Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0516 | Battery Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0517 | Battery Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0518 | Idle Air Control Circuit Intermittent | P | generic | [C] | — | — |
| P0519 | Idle Air Control System Performance | P | generic | [C] | — | — |
| P0520 | Engine Oil Pressure Sensor/Switch Circuit Malfunction | P | generic | [B] | — | — |
| P0521 | Engine Oil Pressure Sensor/Switch Circuit Range/Performance | P | generic | [B] | — | — |
| P0522 | Engine Oil Pressure Sensor/Switch Circuit Low Voltage | P | generic | [B] | — | — |
| P0523 | Engine Oil Pressure Sensor/Switch Circuit High Voltage | P | generic | [B] | — | — |
| P0524 | Engine Oil Pressure Too Low | P | generic | [C] | — | — |
| P0525 | Cruise Control Servo Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0526 | Fan Speed Sensor Circuit | P | generic | [C] | — | — |
| P0527 | Fan Speed Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0528 | Fan Speed Sensor Circuit No Signal | P | generic | [C] | — | — |
| P0529 | Fan Speed Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0530 | A/C Refrigerant Pressure Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0531 | A/C Refrigerant Pressure Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0532 | A/C Refrigerant Pressure Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0533 | A/C Refrigerant Pressure Sensor Circuit High Input | P | generic | [B] | — | — |
| P0534 | Air Conditioner Refrigerant Charge Loss | P | generic | [B] | — | — |
| P0535 | A/C Evaporator Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0536 | A/C Evaporator Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0537 | A/C Evaporator Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0538 | A/C Evaporator Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0539 | A/C Evaporator Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0540 | Intake Air Heater A Circuit | P | generic | [C] | — | — |
| P0541 | Intake Air Heater A Circuit Low | P | generic | [C] | — | — |
| P0542 | Intake Air Heater A Circuit High | P | generic | [C] | — | — |
| P0543 | Intake Air Heater A Circuit Open | P | generic | [C] | — | — |
| P0544 | Exhaust Gas Temperature Sensor Circuit (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0545 | Exhaust Gas Temperature Sensor Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0546 | Exhaust Gas Temperature Sensor Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P0547 | Exhaust Gas Temperature Sensor Circuit (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0548 | Exhaust Gas Temperature Sensor Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0549 | Exhaust Gas Temperature Sensor Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P0550 | Power Steering Pressure Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0551 | Power Steering Pressure Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0552 | Power Steering Pressure Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0553 | Power Steering Pressure Sensor Circuit High Input | P | generic | [B] | — | — |
| P0554 | Power Steering Pressure Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0555 | Brake Booster Pressure Sensor Circuit | P | generic | [C] | — | — |
| P0556 | Brake Booster Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0557 | Brake Booster Pressure Sensor Circuit Low Input | P | generic | [C] | — | — |
| P0558 | Brake Booster Pressure Sensor Circuit High Input | P | generic | [C] | — | — |
| P0559 | Brake Booster Pressure Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0560 | System Voltage Malfunction | P | generic | [B] | — | — |
| P0561 | System Voltage Unstable | P | generic | [B] | — | — |
| P0562 | System Voltage Low | P | generic | [B] | — | — |
| P0563 | System Voltage High | P | generic | [B] | — | — |
| P0564 | Cruise Control Multi-Function Input A Circuit | P | generic | [C] | — | — |
| P0565 | Cruise Control On Signal Malfunction | P | generic | [B] | — | — |
| P0566 | Cruise Control Off Signal Malfunction | P | generic | [B] | — | — |
| P0567 | Cruise Control Resume Signal Malfunction | P | generic | [B] | — | — |
| P0568 | Cruise Control Set Signal Malfunction | P | generic | [B] | — | — |
| P0569 | Cruise Control Coast Signal Malfunction | P | generic | [B] | — | — |
| P0570 | Cruise Control Accel Signal Malfunction | P | generic | [B] | — | — |
| P0571 | Cruise Control/Brake Switch A Circuit Malfunction | P | generic | [B] | — | — |
| P0572 | Cruise Control/Brake Switch A Circuit Low | P | generic | [B] | — | — |
| P0573 | Cruise Control/Brake Switch A Circuit High | P | generic | [B] | — | — |
| P0574 | Cruise Control System - Vehicle Speed Too High | P | generic | [C] | — | — |
| P0575 | Cruise Control Input Circuit | P | generic | [C] | — | — |
| P0576 | Cruise Control Input Circuit Low | P | generic | [C] | — | — |
| P0577 | Cruise Control Input Circuit High | P | generic | [C] | — | — |
| P0578 | Cruise Control Multi-Function Input A Circuit Stuck | P | generic | [C] | — | — |
| P0579 | Cruise Control Multi-Function Input A Circuit Range/Performance | P | generic | [C] | — | — |
| P0580 | Cruise Control Multi-Function Input A Circuit Low | P | generic | [C] | — | — |
| P0581 | Cruise Control Multi-Function Input A Circuit High | P | generic | [C] | — | — |
| P0582 | Cruise Control Vacuum Control Circuit/Open | P | generic | [C] | — | — |
| P0583 | Cruise Control Vacuum Control Circuit Low | P | generic | [C] | — | — |
| P0584 | Cruise Control Vacuum Control Circuit High | P | generic | [C] | — | — |
| P0585 | Cruise Control Multi-Function Input A/B Correlation | P | generic | [C] | — | — |
| P0586 | Cruise Control Vent Control Circuit/Open | P | generic | [C] | — | — |
| P0587 | Cruise Control Vent Control Circuit Low | P | generic | [C] | — | — |
| P0588 | Cruise Control Vent Control Circuit High | P | generic | [C] | — | — |
| P0589 | Cruise Control Multi-Function Input B Circuit | P | generic | [C] | — | — |
| P0590 | Cruise Control Multi-Function Input B Circuit Stuck | P | generic | [C] | — | — |
| P0591 | Cruise Control Multi-Function Input B Circuit Range/Performance | P | generic | [C] | — | — |
| P0592 | Cruise Control Multi-Function Input B Circuit Low | P | generic | [C] | — | — |
| P0593 | Cruise Control Multi-Function Input B Circuit High | P | generic | [C] | — | — |
| P0594 | Cruise Control Servo Control Circuit/Open | P | generic | [C] | — | — |
| P0595 | Cruise Control Servo Control Circuit Low | P | generic | [C] | — | — |
| P0596 | Cruise Control Servo Control Circuit High | P | generic | [C] | — | — |
| P0597 | Thermostat Heater Control Circuit/Open | P | generic | [C] | — | — |
| P0598 | Thermostat Heater Control Circuit Low | P | generic | [C] | — | — |
| P0599 | Thermostat Heater Control Circuit High | P | generic | [C] | — | — |
| P0600 | Serial Communication Link Malfunction | P | generic | [B] | — | — |
| P0601 | Internal Control Module Memory Check Sum Error | P | generic | [B] | — | — |
| P0602 | Control Module Programming Error | P | generic | [B] | — | — |
| P0603 | Internal Control Module Keep Alive Memory (KAM) Error | P | generic | [B] | — | — |
| P0604 | Internal Control Module Random Access Memory (RAM) Error | P | generic | [B] | — | — |
| P0605 | Internal Control Module Read Only Memory (ROM) Error | P | generic | [B] | — | — |
| P0606 | PCM Processor Fault | P | generic | [B] | — | — |
| P0607 | Control Module Performance | P | generic | [C] | — | — |
| P0608 | Control Module VSS Output "A" Malfunction | P | generic | [B] | — | — |
| P0609 | Control Module VSS Output "B" Malfunction | P | generic | [B] | — | — |
| P0610 | Control Module Vehicle Options Error | P | generic | [C] | — | — |
| P0611 | Fuel Injector Control Module Performance | P | generic | [C] | — | — |
| P0612 | Fuel Injector Control Module Relay Control | P | generic | [C] | — | — |
| P0613 | TCM Processor | P | generic | [C] | — | — |
| P0614 | ECM / TCM Incompatible | P | generic | [C] | — | — |
| P0615 | Starter Relay Circuit | P | generic | [C] | — | — |
| P0616 | Starter Relay Circuit Low | P | generic | [C] | — | — |
| P0617 | Starter Relay Circuit High | P | generic | [C] | — | — |
| P0618 | Alternative Fuel Control Module KAM Error | P | generic | [C] | — | — |
| P0619 | Alternative Fuel Control Module RAM/ROM Error | P | generic | [C] | — | — |
| P0620 | Generator Control Circuit Malfunction | P | generic | [B] | — | — |
| P0621 | Generator Lamp "L" Control Circuit Malfunction | P | generic | [B] | — | — |
| P0622 | Generator Field "F" Control Circuit Malfunction | P | generic | [B] | — | — |
| P0623 | Generator Lamp Control Circuit | P | generic | [C] | — | — |
| P0624 | Fuel Cap Lamp Control Circuit | P | generic | [C] | — | — |
| P0625 | Generator Field/F Terminal Circuit Low | P | generic | [C] | — | — |
| P0626 | Generator Field/F Terminal Circuit High | P | generic | [C] | — | — |
| P0627 | Fuel Pump A Control Circuit /Open | P | generic | [C] | — | — |
| P0628 | Fuel Pump A Control Circuit Low | P | generic | [C] | — | — |
| P0629 | Fuel Pump A Control Circuit High | P | generic | [C] | — | — |
| P0630 | VIN Not Programmed or Incompatible - ECM/PCM | P | generic | [C] | — | — |
| P0631 | VIN Not Programmed or Incompatible - TCM | P | generic | [C] | — | — |
| P0632 | Odometer Not Programmed - ECM/PCM | P | generic | [C] | — | — |
| P0633 | Immobilizer Key Not Programmed - ECM/PCM | P | generic | [C] | — | — |
| P0634 | PCM/ECM/TCM Internal Temperature Too High | P | generic | [C] | — | — |
| P0635 | Power Steering Control Circuit | P | generic | [C] | — | — |
| P0636 | Power Steering Control Circuit Low | P | generic | [C] | — | — |
| P0637 | Power Steering Control Circuit High | P | generic | [C] | — | — |
| P0638 | Throttle Actuator Control Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P0639 | Throttle Actuator Control Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P0640 | Intake Air Heater Control Circuit | P | generic | [C] | — | — |
| P0641 | Sensor Reference Voltage A Circuit/Open | P | generic | [C] | — | — |
| P0642 | Sensor Reference Voltage A Circuit Low | P | generic | [C] | — | — |
| P0643 | Sensor Reference Voltage A Circuit High | P | generic | [C] | — | — |
| P0644 | Driver Display Serial Communication Circuit | P | generic | [C] | — | — |
| P0645 | A/C Clutch Relay Control Circuit | P | generic | [C] | — | — |
| P0646 | A/C Clutch Relay Control Circuit Low | P | generic | [C] | — | — |
| P0647 | A/C Clutch Relay Control Circuit High | P | generic | [C] | — | — |
| P0648 | Immobilizer Lamp Control Circuit | P | generic | [C] | — | — |
| P0649 | Speed Control Lamp Control Circuit | P | generic | [C] | — | — |
| P0650 | Malfunction Indicator Lamp (MIL) Control Circuit Malfunction | P | generic | [B] | — | — |
| P0651 | Sensor Reference Voltage B Circuit/Open | P | generic | [C] | — | — |
| P0652 | Sensor Reference Voltage B Circuit Low | P | generic | [C] | — | — |
| P0653 | Sensor Reference Voltage B Circuit High | P | generic | [C] | — | — |
| P0654 | Engine RPM Output Circuit Malfunction | P | generic | [B] | — | — |
| P0655 | Engine Hot Lamp Output Control Circuit Malfunction | P | generic | [B] | — | — |
| P0656 | Fuel Level Output Circuit Malfunction | P | generic | [B] | — | — |
| P0657 | Actuator Supply Voltage Circuit/Open | P | generic | [C] | — | — |
| P0658 | Actuator Supply Voltage Circuit Low | P | generic | [C] | — | — |
| P0659 | Actuator Supply Voltage Circuit High | P | generic | [C] | — | — |
| P0660 | Intake Manifold Tuning Valve Control Circuit/Open (Bank 1) | P | generic | [C] | — | — |
| P0661 | Intake Manifold Tuning Valve Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P0662 | Intake Manifold Tuning Valve Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P0663 | Intake Manifold Tuning Valve Control Circuit/Open (Bank 2) | P | generic | [C] | — | — |
| P0664 | Intake Manifold Tuning Valve Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P0665 | Intake Manifold Tuning Valve Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P0666 | PCM/ECM/TCM Internal Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0667 | PCM/ECM/TCM Internal Temperature Sensor Range/Performance | P | generic | [C] | — | — |
| P0668 | PCM/ECM/TCM Internal Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0669 | PCM/ECM/TCM Internal Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0670 | Glow Plug Module Control Circuit | P | generic | [C] | — | — |
| P0671 | Cylinder 1 Glow Plug Circuit | P | generic | [C] | — | — |
| P0672 | Cylinder 2 Glow Plug Circuit | P | generic | [C] | — | — |
| P0673 | Cylinder 3 Glow Plug Circuit | P | generic | [C] | — | — |
| P0674 | Cylinder 4 Glow Plug Circuit | P | generic | [C] | — | — |
| P0675 | Cylinder 5 Glow Plug Circuit | P | generic | [C] | — | — |
| P0676 | Cylinder 6 Glow Plug Circuit | P | generic | [C] | — | — |
| P0677 | Cylinder 7 Glow Plug Circuit | P | generic | [C] | — | — |
| P0678 | Cylinder 8 Glow Plug Circuit | P | generic | [C] | — | — |
| P0679 | Cylinder 9 Glow Plug Circuit | P | generic | [C] | — | — |
| P0680 | Cylinder 10 Glow Plug Circuit | P | generic | [C] | — | — |
| P0681 | Cylinder 11 Glow Plug Circuit | P | generic | [C] | — | — |
| P0682 | Cylinder 12 Glow Plug Circuit | P | generic | [C] | — | — |
| P0683 | Glow Plug Control Module to PCM Communication Circuit | P | generic | [C] | — | — |
| P0684 | Glow Plug Control Module to PCM Communication Circuit Range/Performance | P | generic | [C] | — | — |
| P0685 | ECM/PCM Power Relay Control Circuit/Open | P | generic | [C] | — | — |
| P0686 | ECM/PCM Power Relay Control Circuit Low | P | generic | [C] | — | — |
| P0687 | ECM/PCM Power Relay Control Circuit High | P | generic | [C] | — | — |
| P0688 | ECM/PCM Power Relay Sense Circuit /Open | P | generic | [C] | — | — |
| P0689 | ECM/PCM Power Relay Sense Circuit Low | P | generic | [C] | — | — |
| P0690 | ECM/PCM Power Relay Sense Circuit High | P | generic | [C] | — | — |
| P0691 | Fan 1 Control Circuit Low | P | generic | [C] | — | — |
| P0692 | Fan 1 Control Circuit High | P | generic | [C] | — | — |
| P0693 | Fan 2 Control Circuit Low | P | generic | [C] | — | — |
| P0694 | Fan 2 Control Circuit High | P | generic | [C] | — | — |
| P0695 | Fan 3 Control Circuit Low | P | generic | [C] | — | — |
| P0696 | Fan 3 Control Circuit High | P | generic | [C] | — | — |
| P0697 | Sensor Reference Voltage C Circuit/Open | P | generic | [C] | — | — |
| P0698 | Sensor Reference Voltage C Circuit Low | P | generic | [C] | — | — |
| P0699 | Sensor Reference Voltage C Circuit High | P | generic | [C] | — | — |
| P0700 | Transmission Control System (MIL Request) Malfunction | P | generic | [B] | — | — |
| P0701 | Transmission Control System Range/Performance | P | generic | [B] | — | — |
| P0702 | Transmission Control System Electrical | P | generic | [B] | — | — |
| P0703 | Torque Converter/Brake Switch B Circuit Malfunction | P | generic | [B] | — | — |
| P0704 | Clutch Switch Input Circuit Malfunction | P | generic | [B] | — | — |
| P0705 | Transmission Range Sensor Circuit malfunction (PRNDL Input) | P | generic | [B] | — | — |
| P0706 | Transmission Range Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0707 | Transmission Range Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0708 | Transmission Range Sensor Circuit High Input | P | generic | [B] | — | — |
| P0709 | Transmission Range Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0710 | Transmission Fluid Temperature Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0711 | Transmission Fluid Temperature Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0712 | Transmission Fluid Temperature Sensor Circuit Low Input | P | generic | [B] | — | — |
| P0713 | Transmission Fluid Temperature Sensor Circuit High Input | P | generic | [B] | — | — |
| P0714 | Transmission Fluid Temperature Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0715 | Input/Turbine Speed Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0716 | Input/Turbine Speed Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0717 | Input/Turbine Speed Sensor Circuit No Signal | P | generic | [B] | — | — |
| P0718 | Input/Turbine Speed Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0719 | Torque Converter/Brake Switch B Circuit Low | P | generic | [B] | — | — |
| P0720 | Output Speed Sensor Circuit Malfunction | P | generic | [B] | — | — |
| P0721 | Output Speed Sensor Circuit Range/Performance | P | generic | [B] | — | — |
| P0722 | Output Speed Sensor Circuit No Signal | P | generic | [B] | — | — |
| P0723 | Output Speed Sensor Circuit Intermittent | P | generic | [B] | — | — |
| P0724 | Torque Converter/Brake Switch B Circuit High | P | generic | [B] | — | — |
| P0725 | Engine Speed input Circuit Malfunction | P | generic | [B] | — | — |
| P0726 | Engine Speed Input Circuit Range/Performance | P | generic | [B] | — | — |
| P0727 | Engine Speed Input Circuit No Signal | P | generic | [B] | — | — |
| P0728 | Engine Speed Input Circuit Intermittent | P | generic | [B] | — | — |
| P0729 | Gear 6 Incorrect Ratio | P | generic | [C] | — | — |
| P0730 | Incorrect Gear Ratio | P | generic | [B] | — | — |
| P0731 | Gear 1 Incorrect ratio | P | generic | [B] | — | — |
| P0732 | Gear 2 Incorrect ratio | P | generic | [B] | — | — |
| P0733 | Gear 3 Incorrect ratio | P | generic | [B] | — | — |
| P0734 | Gear 4 Incorrect ratio | P | generic | [B] | — | — |
| P0735 | Gear 5 Incorrect ratio | P | generic | [B] | — | — |
| P0736 | Reverse incorrect gear ratio | P | generic | [B] | — | — |
| P0737 | TCM Engine Speed Output Circuit | P | generic | [C] | — | — |
| P0738 | TCM Engine Speed Output Circuit Low | P | generic | [C] | — | — |
| P0739 | TCM Engine Speed Output Circuit High | P | generic | [C] | — | — |
| P0740 | Torque Converter Clutch Circuit Malfunction | P | generic | [B] | — | — |
| P0741 | Torque Converter Clutch Circuit Performance or Stuck Off | P | generic | [B] | — | — |
| P0742 | Torque Converter Clutch Circuit Stuck On | P | generic | [B] | — | — |
| P0743 | Torque Converter Clutch Circuit Electrical | P | generic | [B] | — | — |
| P0744 | Torque Converter Clutch Circuit Intermittent | P | generic | [B] | — | — |
| P0745 | Pressure Control Solenoid Malfunction | P | generic | [B] | — | — |
| P0746 | Pressure Control Solenoid Performance or Stuck Off | P | generic | [B] | — | — |
| P0747 | Pressure Control Solenoid Stuck On | P | generic | [B] | — | — |
| P0748 | Pressure Control Solenoid Electrical | P | generic | [B] | — | — |
| P0749 | Pressure Control Solenoid Intermittent | P | generic | [B] | — | — |
| P0750 | Shift Solenoid A Malfunction | P | generic | [B] | — | — |
| P0751 | Shift Solenoid A Performance or Stuck Off | P | generic | [B] | — | — |
| P0752 | Shift Solenoid A Stuck On | P | generic | [B] | — | — |
| P0753 | Shift Solenoid A Electrical | P | generic | [B] | — | — |
| P0754 | Shift Solenoid A Intermittent | P | generic | [B] | — | — |
| P0755 | Shift Solenoid B Malfunction | P | generic | [B] | — | — |
| P0756 | Shift Solenoid B Performance or Stuck Off | P | generic | [B] | — | — |
| P0757 | Shift Solenoid B Stuck On | P | generic | [B] | — | — |
| P0758 | Shift Solenoid B Electrical | P | generic | [B] | — | — |
| P0759 | Shift Solenoid B Intermittent | P | generic | [B] | — | — |
| P0760 | Shift Solenoid C Malfunction | P | generic | [B] | — | — |
| P0761 | Shift Solenoid C Performance or Stuck Off | P | generic | [B] | — | — |
| P0762 | Shift Solenoid C Stuck On | P | generic | [B] | — | — |
| P0763 | Shift Solenoid C Electrical | P | generic | [B] | — | — |
| P0764 | Shift Solenoid C Intermittent | P | generic | [B] | — | — |
| P0765 | Shift Solenoid D Malfunction | P | generic | [B] | — | — |
| P0766 | Shift Solenoid D Performance or Stuck Off | P | generic | [B] | — | — |
| P0767 | Shift Solenoid D Stuck On | P | generic | [B] | — | — |
| P0768 | Shift Solenoid D Electrical | P | generic | [B] | — | — |
| P0769 | Shift Solenoid D Intermittent | P | generic | [B] | — | — |
| P0770 | Shift Solenoid E Malfunction | P | generic | [B] | — | — |
| P0771 | Shift Solenoid E Performance or Stuck Off | P | generic | [B] | — | — |
| P0772 | Shift Solenoid E Stuck On | P | generic | [B] | — | — |
| P0773 | Shift Solenoid E Electrical | P | generic | [B] | — | — |
| P0774 | Shift Solenoid E Intermittent | P | generic | [B] | — | — |
| P0775 | Pressure Control Solenoid B | P | generic | [C] | — | — |
| P0776 | Pressure Control Solenoid B Performance or Stuck Off | P | generic | [C] | — | — |
| P0777 | Pressure Control Solenoid B Stuck on | P | generic | [C] | — | — |
| P0778 | Pressure Control Solenoid B Electrical | P | generic | [C] | — | — |
| P0779 | Pressure Control Solenoid B Intermittent | P | generic | [C] | — | — |
| P0780 | Shift Malfunction | P | generic | [B] | — | — |
| P0781 | 1-2 Shift Malfunction | P | generic | [B] | — | — |
| P0782 | 2-3 Shift Malfunction | P | generic | [B] | — | — |
| P0783 | 3-4 Shift Malfunction | P | generic | [B] | — | — |
| P0784 | 4-5 Shift Malfunction | P | generic | [B] | — | — |
| P0785 | Shift/Timing Solenoid Malfunction | P | generic | [B] | — | — |
| P0786 | Shift/Timing Solenoid Range/Performance | P | generic | [B] | — | — |
| P0787 | Shift/Timing Solenoid Low | P | generic | [B] | — | — |
| P0788 | Shift/Timing Solenoid High | P | generic | [B] | — | — |
| P0789 | Shift/Timing Solenoid Intermittent | P | generic | [B] | — | — |
| P0790 | Normal/Performance Switch Circuit Malfunction | P | generic | [B] | — | — |
| P0791 | Intermediate Shaft Speed Sensor A Circuit | P | generic | [C] | — | — |
| P0792 | Intermediate Shaft Speed Sensor A Circuit Range/Performance | P | generic | [C] | — | — |
| P0793 | Intermediate Shaft Speed Sensor A Circuit No Signal | P | generic | [C] | — | — |
| P0794 | Intermediate Shaft Speed Sensor A Circuit Intermittent | P | generic | [C] | — | — |
| P0795 | Pressure Control Solenoid C | P | generic | [C] | — | — |
| P0796 | Pressure Control Solenoid C Performance or Stuck Off | P | generic | [C] | — | — |
| P0797 | Pressure Control Solenoid C Stuck on | P | generic | [C] | — | — |
| P0798 | Pressure Control Solenoid C Electrical | P | generic | [C] | — | — |
| P0799 | Pressure Control Solenoid C Intermittent | P | generic | [C] | — | — |
| P0800 | Transfer Case Control System (MIL Request) | P | generic | [C] | — | — |
| P0801 | Reverse Inhibit Control Circuit Malfunction | P | generic | [B] | — | — |
| P0802 | Transmission Control System MIL Request Circuit/Open | P | generic | [C] | — | — |
| P0803 | 1-4 Upshift (Skip Shift) Solenoid Control Circuit Malfunction | P | generic | [B] | — | — |
| P0804 | 1-4 Upshift (Skip Shift) Lamp Control Circuit Malfunction | P | generic | [C] | — | — |
| P0805 | Clutch Position Sensor Circuit | P | generic | [C] | — | — |
| P0806 | Clutch Position Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0807 | Clutch Position Sensor Circuit Low | P | generic | [C] | — | — |
| P0808 | Clutch Position Sensor Circuit High | P | generic | [C] | — | — |
| P0809 | Clutch Position Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0810 | Clutch Position Control Error | P | generic | [C] | — | — |
| P0811 | Excessive Clutch Slippage | P | generic | [C] | — | — |
| P0812 | Reverse Input Circuit | P | generic | [C] | — | — |
| P0813 | Reverse Output Circuit | P | generic | [C] | — | — |
| P0814 | Transmission Range Display Circuit | P | generic | [C] | — | — |
| P0815 | Upshift Switch Circuit | P | generic | [C] | — | — |
| P0816 | Downshift Switch Circuit | P | generic | [C] | — | — |
| P0817 | Starter Disable Circuit | P | generic | [C] | — | — |
| P0818 | Driveline Disconnect Switch Input Circuit | P | generic | [C] | — | — |
| P0819 | Up and Down Shift Switch to Transmission Range Correlation | P | generic | [C] | — | — |
| P0820 | Gear Lever X-Y Position Sensor Circuit | P | generic | [C] | — | — |
| P0821 | Gear Lever X Position Circuit | P | generic | [C] | — | — |
| P0822 | Gear Lever Y Position Circuit | P | generic | [C] | — | — |
| P0823 | Gear Lever X Position Circuit Intermittent | P | generic | [C] | — | — |
| P0824 | Gear Lever Y Position Circuit Intermittent | P | generic | [C] | — | — |
| P0825 | Gear Lever Push-Pull Switch (Shift Anticipate) | P | generic | [C] | — | — |
| P0826 | Up and Down Shift Switch Circuit | P | generic | [C] | — | — |
| P0827 | Up and Down Shift Switch Circuit Low | P | generic | [C] | — | — |
| P0828 | Up and Down Shift Switch Circuit High | P | generic | [C] | — | — |
| P0829 | 5-6 Shift | P | generic | [C] | — | — |
| P0830 | Clutch Pedal Switch A Circuit | P | generic | [C] | — | — |
| P0831 | Clutch Pedal Switch A Circuit Low | P | generic | [C] | — | — |
| P0832 | Clutch Pedal Switch A Circuit High | P | generic | [C] | — | — |
| P0833 | Clutch Pedal Switch B Circuit | P | generic | [C] | — | — |
| P0834 | Clutch Pedal Switch B Circuit Low | P | generic | [C] | — | — |
| P0835 | Clutch Pedal Switch B Circuit High | P | generic | [C] | — | — |
| P0836 | Four Wheel Drive (4WD) Switch Circuit | P | generic | [C] | — | — |
| P0837 | Four Wheel Drive (4WD) Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P0838 | Four Wheel Drive (4WD) Switch Circuit Low | P | generic | [C] | — | — |
| P0839 | Four Wheel Drive (4WD) Switch Circuit High | P | generic | [C] | — | — |
| P0840 | Transmission Fluid Pressure Sensor/Switch A Circuit | P | generic | [C] | — | — |
| P0841 | Transmission Fluid Pressure Sensor/Switch A Circuit Range/Performance | P | generic | [C] | — | — |
| P0842 | Transmission Fluid Pressure Sensor/Switch A Circuit Low | P | generic | [C] | — | — |
| P0843 | Transmission Fluid Pressure Sensor/Switch A Circuit High | P | generic | [C] | — | — |
| P0844 | Transmission Fluid Pressure Sensor/Switch A Circuit Intermittent | P | generic | [C] | — | — |
| P0845 | Transmission Fluid Pressure Sensor/Switch B Circuit | P | generic | [C] | — | — |
| P0846 | Transmission Fluid Pressure Sensor/Switch B Circuit Range/Performance | P | generic | [C] | — | — |
| P0847 | Transmission Fluid Pressure Sensor/Switch B Circuit Low | P | generic | [C] | — | — |
| P0848 | Transmission Fluid Pressure Sensor/Switch B Circuit High | P | generic | [C] | — | — |
| P0849 | Transmission Fluid Pressure Sensor/Switch B Circuit Intermittent | P | generic | [C] | — | — |
| P0850 | Park/Neutral Switch Input Circuit | P | generic | [C] | — | — |
| P0851 | Park/Neutral Switch Input Circuit Low | P | generic | [C] | — | — |
| P0852 | Park/Neutral Switch Input Circuit High | P | generic | [C] | — | — |
| P0853 | Drive Switch Input Circuit | P | generic | [C] | — | — |
| P0854 | Drive Switch Input Circuit Low | P | generic | [C] | — | — |
| P0855 | Drive Switch Input Circuit High | P | generic | [C] | — | — |
| P0856 | Traction Control Input Signal | P | generic | [C] | — | — |
| P0857 | Traction Control Input Signal Range/Performance | P | generic | [C] | — | — |
| P0858 | Traction Control Input Signal Low | P | generic | [C] | — | — |
| P0859 | Traction Control Input Signal High | P | generic | [C] | — | — |
| P0860 | Gear Shift Module Communication Circuit | P | generic | [C] | — | — |
| P0861 | Gear Shift Module Communication Circuit Low | P | generic | [C] | — | — |
| P0862 | Gear Shift Module Communication Circuit High | P | generic | [C] | — | — |
| P0863 | TCM Communication Circuit | P | generic | [C] | — | — |
| P0864 | TCM Communication Circuit Range/Performance | P | generic | [C] | — | — |
| P0865 | TCM Communication Circuit Low | P | generic | [C] | — | — |
| P0866 | TCM Communication Circuit High | P | generic | [C] | — | — |
| P0867 | Transmission Fluid Pressure | P | generic | [C] | — | — |
| P0868 | Transmission Fluid Pressure Low | P | generic | [C] | — | — |
| P0869 | Transmission Fluid Pressure High | P | generic | [C] | — | — |
| P0870 | Transmission Fluid Pressure Sensor/Switch C Circuit | P | generic | [C] | — | — |
| P0871 | Transmission Fluid Pressure Sensor/Switch C Circuit Range/Performance | P | generic | [C] | — | — |
| P0872 | Transmission Fluid Pressure Sensor/Switch C Circuit Low | P | generic | [C] | — | — |
| P0873 | Transmission Fluid Pressure Sensor/Switch C Circuit High | P | generic | [C] | — | — |
| P0874 | Transmission Fluid Pressure Sensor/Switch C Circuit Intermittent | P | generic | [C] | — | — |
| P0875 | Transmission Fluid Pressure Sensor/Switch D Circuit | P | generic | [C] | — | — |
| P0876 | Transmission Fluid Pressure Sensor/Switch D Circuit Range/Performance | P | generic | [C] | — | — |
| P0877 | Transmission Fluid Pressure Sensor/Switch D Circuit Low | P | generic | [C] | — | — |
| P0878 | Transmission Fluid Pressure Sensor/Switch D Circuit High | P | generic | [C] | — | — |
| P0879 | Transmission Fluid Pressure Sensor/Switch D Circuit Intermittent | P | generic | [C] | — | — |
| P0880 | TCM Power Input Signal | P | generic | [C] | — | — |
| P0881 | TCM Power Input Signal Range/Performance | P | generic | [C] | — | — |
| P0882 | TCM Power Input Signal Low | P | generic | [C] | — | — |
| P0883 | TCM Power Input Signal High | P | generic | [C] | — | — |
| P0884 | TCM Power Input Signal Intermittent | P | generic | [C] | — | — |
| P0885 | TCM Power Relay Control Circuit/Open | P | generic | [C] | — | — |
| P0886 | TCM Power Relay Control Circuit Low | P | generic | [C] | — | — |
| P0887 | TCM Power Relay Control Circuit High | P | generic | [C] | — | — |
| P0888 | TCM Power Relay Sense Circuit | P | generic | [C] | — | — |
| P0889 | TCM Power Relay Sense Circuit Range/Performance | P | generic | [C] | — | — |
| P0890 | TCM Power Relay Sense Circuit Low | P | generic | [C] | — | — |
| P0891 | TCM Power Relay Sense Circuit High | P | generic | [C] | — | — |
| P0892 | TCM Power Relay Sense Circuit Intermittent | P | generic | [C] | — | — |
| P0893 | Multiple Gears Engaged | P | generic | [C] | — | — |
| P0894 | Transmission Component Slipping | P | generic | [C] | — | — |
| P0895 | Shift Time Too Short | P | generic | [C] | — | — |
| P0896 | Shift Time Too Long | P | generic | [C] | — | — |
| P0897 | Transmission Fluid Deteriorated | P | generic | [C] | — | — |
| P0898 | Transmission Control System MIL Request Circuit Low | P | generic | [C] | — | — |
| P0899 | Transmission Control System MIL Request Circuit High | P | generic | [C] | — | — |
| P0900 | Clutch Actuator Circuit/Open | P | generic | [C] | — | — |
| P0901 | Clutch Actuator Circuit Range/Performance | P | generic | [C] | — | — |
| P0902 | Clutch Actuator Circuit Low | P | generic | [C] | — | — |
| P0903 | Clutch Actuator Circuit High | P | generic | [C] | — | — |
| P0904 | Gate Select Position Circuit | P | generic | [C] | — | — |
| P0905 | Gate Select Position Circuit Range/Performance | P | generic | [C] | — | — |
| P0906 | Gate Select Position Circuit Low | P | generic | [C] | — | — |
| P0907 | Gate Select Position Circuit High | P | generic | [C] | — | — |
| P0908 | Gate Select Position Circuit Intermittent | P | generic | [C] | — | — |
| P0909 | Gate Select Control Error | P | generic | [C] | — | — |
| P0910 | Gate Select Actuator Circuit/Open | P | generic | [C] | — | — |
| P0911 | Gate Select Actuator Circuit Range/Performance | P | generic | [C] | — | — |
| P0912 | Gate Select Actuator Circuit Low | P | generic | [C] | — | — |
| P0913 | Gate Select Actuator Circuit High | P | generic | [C] | — | — |
| P0914 | Gear Shift Position Circuit | P | generic | [C] | — | — |
| P0915 | Gear Shift Position Circuit Range/Performance | P | generic | [C] | — | — |
| P0916 | Gear Shift Position Circuit Low | P | generic | [C] | — | — |
| P0917 | Gear Shift Position Circuit High | P | generic | [C] | — | — |
| P0918 | Gear Shift Position Circuit Intermittent | P | generic | [C] | — | — |
| P0919 | Gear Shift Position Control Error | P | generic | [C] | — | — |
| P0920 | Gear Shift Forward Actuator Circuit/Open | P | generic | [C] | — | — |
| P0921 | Gear Shift Forward Actuator Circuit Range/Performance | P | generic | [C] | — | — |
| P0922 | Gear Shift Forward Actuator Circuit Low | P | generic | [C] | — | — |
| P0923 | Gear Shift Forward Actuator Circuit High | P | generic | [C] | — | — |
| P0924 | Gear Shift Reverse Actuator Circuit/Open | P | generic | [C] | — | — |
| P0925 | Gear Shift Reverse Actuator Circuit Range/Performance | P | generic | [C] | — | — |
| P0926 | Gear Shift Reverse Actuator Circuit Low | P | generic | [C] | — | — |
| P0927 | Gear Shift Reverse Actuator Circuit High | P | generic | [C] | — | — |
| P0928 | Gear Shift Lock Solenoid Control Circuit/Open | P | generic | [C] | — | — |
| P0929 | Gear Shift Lock Solenoid Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0930 | Gear Shift Lock Solenoid Control Circuit Low | P | generic | [C] | — | — |
| P0931 | Gear Shift Lock Solenoid Control Circuit High | P | generic | [C] | — | — |
| P0932 | Hydraulic Pressure Sensor Circuit | P | generic | [C] | — | — |
| P0933 | Hydraulic Pressure Sensor Range/Performance | P | generic | [C] | — | — |
| P0934 | Hydraulic Pressure Sensor Circuit Low | P | generic | [C] | — | — |
| P0935 | Hydraulic Pressure Sensor Circuit High | P | generic | [C] | — | — |
| P0936 | Hydraulic Pressure Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0937 | Hydraulic Oil Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0938 | Hydraulic Oil Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0939 | Hydraulic Oil Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0940 | Hydraulic Oil Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0941 | Hydraulic Oil Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0942 | Hydraulic Pressure Unit | P | generic | [C] | — | — |
| P0943 | Hydraulic Pressure Unit Cycling Period Too Short | P | generic | [C] | — | — |
| P0944 | Hydraulic Pressure Unit Loss of Pressure | P | generic | [C] | — | — |
| P0945 | Hydraulic Pump Relay Circuit/Open | P | generic | [C] | — | — |
| P0946 | Hydraulic Pump Relay Circuit Range/Performance | P | generic | [C] | — | — |
| P0947 | Hydraulic Pump Relay Circuit Low | P | generic | [C] | — | — |
| P0948 | Hydraulic Pump Relay Circuit High | P | generic | [C] | — | — |
| P0949 | Auto Shift Manual Adaptive Learning Not Complete | P | generic | [C] | — | — |
| P0950 | Auto Shift Manual Control Circuit | P | generic | [C] | — | — |
| P0951 | Auto Shift Manual Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0952 | Auto Shift Manual Control Circuit Low | P | generic | [C] | — | — |
| P0953 | Auto Shift Manual Control Circuit High | P | generic | [C] | — | — |
| P0954 | Auto Shift Manual Control Circuit Intermittent | P | generic | [C] | — | — |
| P0955 | Auto Shift Manual Mode Circuit | P | generic | [C] | — | — |
| P0956 | Auto Shift Manual Mode Circuit Range/Performance | P | generic | [C] | — | — |
| P0957 | Auto Shift Manual Mode Circuit Low | P | generic | [C] | — | — |
| P0958 | Auto Shift Manual Mode Circuit High | P | generic | [C] | — | — |
| P0959 | Auto Shift Manual Mode Circuit Intermittent | P | generic | [C] | — | — |
| P0960 | Pressure Control Solenoid A Control Circuit/Open | P | generic | [C] | — | — |
| P0961 | Pressure Control Solenoid A Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0962 | Pressure Control Solenoid A Control Circuit Low | P | generic | [C] | — | — |
| P0963 | Pressure Control Solenoid A Control Circuit High | P | generic | [C] | — | — |
| P0964 | Pressure Control Solenoid B Control Circuit/Open | P | generic | [C] | — | — |
| P0965 | Pressure Control Solenoid B Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0966 | Pressure Control Solenoid B Control Circuit Low | P | generic | [C] | — | — |
| P0967 | Pressure Control Solenoid B Control Circuit High | P | generic | [C] | — | — |
| P0968 | Pressure Control Solenoid C Control Circuit/Open | P | generic | [C] | — | — |
| P0969 | Pressure Control Solenoid C Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0970 | Pressure Control Solenoid C Control Circuit Low | P | generic | [C] | — | — |
| P0971 | Pressure Control Solenoid C Control Circuit High | P | generic | [C] | — | — |
| P0972 | Shift Solenoid A Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0973 | Shift Solenoid A Control Circuit Low | P | generic | [C] | — | — |
| P0974 | Shift Solenoid A Control Circuit High | P | generic | [C] | — | — |
| P0975 | Shift Solenoid B Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0976 | Shift Solenoid B Control Circuit Low | P | generic | [C] | — | — |
| P0977 | Shift Solenoid B Control Circuit High | P | generic | [C] | — | — |
| P0978 | Shift Solenoid C Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0979 | Shift Solenoid C Control Circuit Low | P | generic | [C] | — | — |
| P0980 | Shift Solenoid C Control Circuit High | P | generic | [C] | — | — |
| P0981 | Shift Solenoid D Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0982 | Shift Solenoid D Control Circuit Low | P | generic | [C] | — | — |
| P0983 | Shift Solenoid D Control Circuit High | P | generic | [C] | — | — |
| P0984 | Shift Solenoid E Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0985 | Shift Solenoid E Control Circuit Low | P | generic | [C] | — | — |
| P0986 | Shift Solenoid E Control Circuit High | P | generic | [C] | — | — |
| P0987 | Transmission Fluid Pressure Sensor/Switch E Circuit | P | generic | [C] | — | — |
| P0988 | Transmission Fluid Pressure Sensor/Switch E Circuit Range/Performance | P | generic | [C] | — | — |
| P0989 | Transmission Fluid Pressure Sensor/Switch E Circuit Low | P | generic | [C] | — | — |
| P0990 | Transmission Fluid Pressure Sensor/Switch E Circuit High | P | generic | [C] | — | — |
| P0991 | Transmission Fluid Pressure Sensor/Switch E Intermittent | P | generic | [C] | — | — |
| P0992 | Transmission Fluid Pressure Sensor/Switch F Circuit | P | generic | [C] | — | — |
| P0993 | Transmission Fluid Pressure Sensor/Switch F Circuit Range/Performance | P | generic | [C] | — | — |
| P0994 | Transmission Fluid Pressure Sensor/Switch F Circuit Low | P | generic | [C] | — | — |
| P0995 | Transmission Fluid Pressure Sensor/Switch F Circuit High | P | generic | [C] | — | — |
| P0996 | Transmission Fluid Pressure Sensor/Switch F Intermittent | P | generic | [C] | — | — |
| P0997 | Shift Solenoid F Control Circuit Range/Performance | P | generic | [C] | — | — |
| P0998 | Shift Solenoid F Control Circuit Low | P | generic | [C] | — | — |
| P0999 | Shift Solenoid F Control Circuit High | P | generic | [C] | — | — |
| P0A00 | Motor Electronics Coolant Temperature Sensor Circuit | P | generic | [C] | — | — |
| P0A01 | Motor Electronics Coolant Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0A02 | Motor Electronics Coolant Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P0A03 | Motor Electronics Coolant Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P0A04 | Motor Electronics Coolant Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0A05 | Motor Electronics Coolant Pump Control Circuit/Open | P | generic | [C] | — | — |
| P0A06 | Motor Electronics Coolant Pump Control Circuit Low | P | generic | [C] | — | — |
| P0A07 | Motor Electronics Coolant Pump Control Circuit High | P | generic | [C] | — | — |
| P0A08 | DC/DC Converter Status Circuit | P | generic | [C] | — | — |
| P0A09 | DC/DC Converter Status Circuit Low Input | P | generic | [C] | — | — |
| P0A10 | DC/DC Converter Status Circuit High Input | P | generic | [C] | — | — |
| P0A11 | DC/DC Converter Enable Circuit/Open | P | generic | [C] | — | — |
| P0A12 | DC/DC Converter Enable Circuit Low | P | generic | [C] | — | — |
| P0A13 | DC/DC Converter Enable Circuit High | P | generic | [C] | — | — |
| P0A14 | Engine Mount Control Circuit/Open | P | generic | [C] | — | — |
| P0A15 | Engine Mount Control Circuit Low | P | generic | [C] | — | — |
| P0A16 | Engine Mount Control Circuit High | P | generic | [C] | — | — |
| P0A17 | Motor Torque Sensor Circuit | P | generic | [C] | — | — |
| P0A18 | Motor Torque Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0A19 | Motor Torque Sensor Circuit Low | P | generic | [C] | — | — |
| P0A20 | Motor Torque Sensor Circuit High | P | generic | [C] | — | — |
| P0A21 | Motor Torque Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0A22 | Generator Torque Sensor Circuit | P | generic | [C] | — | — |
| P0A23 | Generator Torque Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P0A24 | Generator Torque Sensor Circuit Low | P | generic | [C] | — | — |
| P0A25 | Generator Torque Sensor Circuit High | P | generic | [C] | — | — |
| P0A26 | Generator Torque Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P0A27 | Battery Power Off Circuit | P | generic | [C] | — | — |
| P0A28 | Battery Power Off Circuit Low | P | generic | [C] | — | — |
| P0A29 | Battery Power Off Circuit High | P | generic | [C] | — | — |
| P2000 | NOx Trap Efficiency Below Threshold (Bank 1) | P | generic | [C] | — | — |
| P2001 | NOx Trap Efficiency Below Threshold (Bank 2) | P | generic | [C] | — | — |
| P2002 | Particulate Trap Efficiency Below Threshold (Bank 1) | P | generic | [B] | excessive soot accumulation in the diesel particulate filter (DPF); failed or inhibited DPF regeneration; faulty DPF differential pressure sensor | Inspect and clean the DPF; monitor DPF sensor readings with a scan tool; perform/verify regeneration cycles; check engine oil for fuel dilution from repeated regen attempts |
| P2003 | Particulate Trap Efficiency Below Threshold (Bank 2) | P | generic | [C] | — | — |
| P2004 | Intake Manifold Runner Control Stuck Open (Bank 1) | P | generic | [C] | — | — |
| P2005 | Intake Manifold Runner Control Stuck Open (Bank 2) | P | generic | [C] | — | — |
| P2006 | Intake Manifold Runner Control Stuck Closed (Bank 1) | P | generic | [C] | — | — |
| P2007 | Intake Manifold Runner Control Stuck Closed (Bank 2) | P | generic | [C] | — | — |
| P2008 | Intake Manifold Runner Control Circuit/Open (Bank 1) | P | generic | [C] | — | — |
| P2009 | Intake Manifold Runner Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2010 | Intake Manifold Runner Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2011 | Intake Manifold Runner Control Circuit/Open (Bank 2) | P | generic | [C] | — | — |
| P2012 | Intake Manifold Runner Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2013 | Intake Manifold Runner Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2014 | Intake Manifold Runner Position Sensor/Switch Circuit (Bank 1) | P | generic | [C] | — | — |
| P2015 | Intake Manifold Runner Position Sensor/Switch Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P2016 | Intake Manifold Runner Position Sensor/Switch Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2017 | Intake Manifold Runner Position Sensor/Switch Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2018 | Intake Manifold Runner Position Sensor/Switch Circuit Intermittent (Bank 1) | P | generic | [C] | — | — |
| P2019 | Intake Manifold Runner Position Sensor/Switch Circuit (Bank 2) | P | generic | [C] | — | — |
| P2020 | Intake Manifold Runner Position Sensor/Switch Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P2021 | Intake Manifold Runner Position Sensor/Switch Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2022 | Intake Manifold Runner Position Sensor/Switch Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2023 | Intake Manifold Runner Position Sensor/Switch Circuit Intermittent (Bank 2) | P | generic | [C] | — | — |
| P2024 | Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit | P | generic | [C] | — | — |
| P2025 | Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Performance | P | generic | [C] | — | — |
| P2026 | Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit Low Voltage | P | generic | [C] | — | — |
| P2027 | Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit High Voltage | P | generic | [C] | — | — |
| P2028 | Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2029 | Fuel Fired Heater Disabled | P | generic | [C] | — | — |
| P2030 | Fuel Fired Heater Performance | P | generic | [C] | — | — |
| P2031 | Exhaust Gas Temperature Sensor Circuit (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2032 | Exhaust Gas Temperature Sensor Circuit Low (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2033 | Exhaust Gas Temperature Sensor Circuit High (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2034 | Exhaust Gas Temperature Sensor Circuit (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2035 | Exhaust Gas Temperature Sensor Circuit Low (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2036 | Exhaust Gas Temperature Sensor Circuit High (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2037 | Reductant Injection Air Pressure Sensor Circuit | P | generic | [C] | — | — |
| P2038 | Reductant Injection Air Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2039 | Reductant Injection Air Pressure Sensor Circuit Low Input | P | generic | [C] | — | — |
| P2040 | Reductant Injection Air Pressure Sensor Circuit High Input | P | generic | [C] | — | — |
| P2041 | Reductant Injection Air Pressure Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2042 | Reductant Temperature Sensor Circuit | P | generic | [C] | — | — |
| P2043 | Reductant Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2044 | Reductant Temperature Sensor Circuit Low Input | P | generic | [C] | — | — |
| P2045 | Reductant Temperature Sensor Circuit High Input | P | generic | [C] | — | — |
| P2046 | Reductant Temperature Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2047 | Reductant Injector Circuit/Open (Bank 1 Unit 1) | P | generic | [C] | — | — |
| P2048 | Reductant Injector Circuit Low (Bank 1 Unit 1) | P | generic | [C] | — | — |
| P2049 | Reductant Injector Circuit High (Bank 1 Unit 1) | P | generic | [C] | — | — |
| P2050 | Reductant Injector Circuit/Open (Bank 2 Unit 1) | P | generic | [C] | — | — |
| P2051 | Reductant Injector Circuit Low (Bank 2 Unit 1) | P | generic | [C] | — | — |
| P2052 | Reductant Injector Circuit High (Bank 2 Unit 1) | P | generic | [C] | — | — |
| P2053 | Reductant Injector Circuit/Open (Bank 1 Unit 2) | P | generic | [C] | — | — |
| P2054 | Reductant Injector Circuit Low (Bank 1 Unit 2) | P | generic | [C] | — | — |
| P2055 | Reductant Injector Circuit High (Bank 1 Unit 2) | P | generic | [C] | — | — |
| P2056 | Reductant Injector Circuit/Open (Bank 2 Unit 2) | P | generic | [C] | — | — |
| P2057 | Reductant Injector Circuit Low (Bank 2 Unit 2) | P | generic | [C] | — | — |
| P2058 | Reductant Injector Circuit High (Bank 2 Unit 2) | P | generic | [C] | — | — |
| P2059 | Reductant Injection Air Pump Control Circuit/Open | P | generic | [C] | — | — |
| P2060 | Reductant Injection Air Pump Control Circuit Low | P | generic | [C] | — | — |
| P2061 | Reductant Injection Air Pump Control Circuit High | P | generic | [C] | — | — |
| P2062 | Reductant Supply Control Circuit/Open | P | generic | [C] | — | — |
| P2063 | Reductant Supply Control Circuit Low | P | generic | [C] | — | — |
| P2064 | Reductant Supply Control Circuit High | P | generic | [C] | — | — |
| P2065 | Fuel Level Sensor B Circuit | P | generic | [C] | — | — |
| P2066 | Fuel Level Sensor B Performance | P | generic | [C] | — | — |
| P2067 | Fuel Level Sensor B Circuit Low | P | generic | [C] | — | — |
| P2068 | Fuel Level Sensor B Circuit High | P | generic | [C] | — | — |
| P2069 | Fuel Level Sensor B Circuit Intermittent | P | generic | [C] | — | — |
| P2070 | Intake Manifold Tuning (IMT) Valve Stuck Open | P | generic | [C] | — | — |
| P2071 | Intake Manifold Tuning (IMT) Valve Stuck Closed | P | generic | [C] | — | — |
| P2075 | Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit | P | generic | [C] | — | — |
| P2076 | Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2077 | Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Low | P | generic | [C] | — | — |
| P2078 | Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit High | P | generic | [C] | — | — |
| P2079 | Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Intermittent | P | generic | [C] | — | — |
| P2080 | Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2081 | Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2082 | Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2083 | Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2084 | Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2085 | Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2086 | Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2087 | Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2088 | A Camshaft Position Actuator Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2089 | A Camshaft Position Actuator Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2090 | B Camshaft Position Actuator Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2091 | B Camshaft Position Actuator Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2092 | A Camshaft Position Actuator Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2093 | A Camshaft Position Actuator Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2094 | B Camshaft Position Actuator Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2095 | B Camshaft Position Actuator Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2096 | Post Catalyst Fuel Trim System Too Lean (Bank 1) | P | generic | [C] | — | — |
| P2097 | Post Catalyst Fuel Trim System Too Rich (Bank 1) | P | generic | [C] | — | — |
| P2098 | Post Catalyst Fuel Trim System Too Lean (Bank 2) | P | generic | [C] | — | — |
| P2099 | Post Catalyst Fuel Trim System Too Rich (Bank 2) | P | generic | [C] | — | — |
| P2100 | Throttle Actuator Control Motor Circuit/Open | P | generic | [C] | — | — |
| P2101 | Throttle Actuator Control Motor Circuit Range/Performance | P | generic | [C] | — | — |
| P2102 | Throttle Actuator Control Motor Circuit Low | P | generic | [C] | — | — |
| P2103 | Throttle Actuator Control Motor Circuit High | P | generic | [C] | — | — |
| P2104 | Throttle Actuator Control System - Forced Idle | P | generic | [C] | — | — |
| P2105 | Throttle Actuator Control System - Forced Engine Shutdown | P | generic | [C] | — | — |
| P2106 | Throttle Actuator Control System - Forced Limited Power | P | generic | [C] | — | — |
| P2107 | Throttle Actuator Control Module Processor | P | generic | [C] | — | — |
| P2108 | Throttle Actuator Control Module Performance | P | generic | [C] | — | — |
| P2109 | Throttle/Pedal Position Sensor A Minimum Stop Performance | P | generic | [C] | — | — |
| P2110 | Throttle Actuator Control System - Forced Limited RPM | P | generic | [C] | — | — |
| P2111 | Throttle Actuator Control System - Stuck Open | P | generic | [C] | — | — |
| P2112 | Throttle Actuator Control System - Stuck Closed | P | generic | [C] | — | — |
| P2113 | Throttle/Pedal Position Sensor B Minimum Stop Performance | P | generic | [C] | — | — |
| P2114 | Throttle/Pedal Position Sensor C Minimum Stop Performance | P | generic | [C] | — | — |
| P2115 | Throttle/Pedal Position Sensor D Minimum Stop Performance | P | generic | [C] | — | — |
| P2116 | Throttle/Pedal Position Sensor E Minimum Stop Performance | P | generic | [C] | — | — |
| P2117 | Throttle/Pedal Position Sensor F Minimum Stop Performance | P | generic | [C] | — | — |
| P2118 | Throttle Actuator Control Motor Current Range/Performance | P | generic | [C] | — | — |
| P2119 | Throttle Actuator Control Throttle Body Range/Performance | P | generic | [C] | — | — |
| P2120 | Throttle/Pedal Position Sensor/Switch D Circuit | P | generic | [C] | — | — |
| P2121 | Throttle/Pedal Position Sensor/Switch D Circuit Range/Performance | P | generic | [C] | — | — |
| P2122 | Throttle/Pedal Position Sensor/Switch D Circuit Low Input | P | generic | [C] | — | — |
| P2123 | Throttle/Pedal Position Sensor/Switch D Circuit High Input | P | generic | [C] | — | — |
| P2124 | Throttle/Pedal Position Sensor/Switch D Circuit Intermittent | P | generic | [C] | — | — |
| P2125 | Throttle/Pedal Position Sensor/Switch E Circuit | P | generic | [C] | — | — |
| P2126 | Throttle/Pedal Position Sensor/Switch E Circuit Range/Performance | P | generic | [C] | — | — |
| P2127 | Throttle/Pedal Position Sensor/Switch E Circuit Low Input | P | generic | [C] | — | — |
| P2128 | Throttle/Pedal Position Sensor/Switch E Circuit High Input | P | generic | [C] | — | — |
| P2129 | Throttle/Pedal Position Sensor/Switch E Circuit Intermittent | P | generic | [C] | — | — |
| P2130 | Throttle/Pedal Position Sensor/Switch F Circuit | P | generic | [C] | — | — |
| P2131 | Throttle/Pedal Position Sensor/Switch F Circuit Range/Performance | P | generic | [C] | — | — |
| P2132 | Throttle/Pedal Position Sensor/Switch F Circuit Low Input | P | generic | [C] | — | — |
| P2133 | Throttle/Pedal Position Sensor/Switch F Circuit High Input | P | generic | [C] | — | — |
| P2134 | Throttle/Pedal Position Sensor/Switch F Circuit Intermittent | P | generic | [C] | — | — |
| P2135 | Throttle/Pedal Position Sensor/Switch "A" /"B" Voltage Correlation | P | generic | [C] | — | — |
| P2136 | Throttle/Pedal Position Sensor/Switch "A" /"C" Voltage Correlation | P | generic | [C] | — | — |
| P2137 | Throttle/Pedal Position Sensor/Switch "B" /"C" Voltage Correlation | P | generic | [C] | — | — |
| P2138 | Throttle/Pedal Position Sensor/Switch "D" /"E" Voltage Correlation | P | generic | [C] | — | — |
| P2139 | Throttle/Pedal Position Sensor/Switch "D" /"F" Voltage Correlation | P | generic | [C] | — | — |
| P2140 | Throttle/Pedal Position Sensor/Switch "E" /"F" Voltage Correlation | P | generic | [C] | — | — |
| P2141 | Exhaust Gas Recirculation Throttle Control Circuit Low | P | generic | [C] | — | — |
| P2142 | Exhaust Gas Recirculation Throttle Control Circuit High | P | generic | [C] | — | — |
| P2143 | Exhaust Gas Recirculation Vent Control Circuit/Open | P | generic | [C] | — | — |
| P2144 | Exhaust Gas Recirculation Vent Control Circuit Low | P | generic | [C] | — | — |
| P2145 | Exhaust Gas Recirculation Vent Control Circuit High | P | generic | [C] | — | — |
| P2146 | Fuel Injector Group "A" Supply Voltage Circuit/Open | P | generic | [C] | — | — |
| P2147 | Fuel Injector Group "A" Supply Voltage Circuit Low | P | generic | [C] | — | — |
| P2148 | Fuel Injector Group "A" Supply Voltage Circuit High | P | generic | [C] | — | — |
| P2149 | Fuel Injector Group "B" Supply Voltage Circuit/Open | P | generic | [C] | — | — |
| P2150 | Fuel Injector Group "B" Supply Voltage Circuit Low | P | generic | [C] | — | — |
| P2151 | Fuel Injector Group "B" Supply Voltage Circuit High | P | generic | [C] | — | — |
| P2152 | Fuel Injector Group "C" Supply Voltage Circuit/Open | P | generic | [C] | — | — |
| P2153 | Fuel Injector Group "C" Supply Voltage Circuit Low | P | generic | [C] | — | — |
| P2154 | Fuel Injector Group "C" Supply Voltage Circuit High | P | generic | [C] | — | — |
| P2155 | Fuel Injector Group "D" Supply Voltage Circuit/Open | P | generic | [C] | — | — |
| P2156 | Fuel Injector Group "D" Supply Voltage Circuit Low | P | generic | [C] | — | — |
| P2157 | Fuel Injector Group "D" Supply Voltage Circuit High | P | generic | [C] | — | — |
| P2158 | Vehicle Speed Sensor "B" | P | generic | [C] | — | — |
| P2159 | Vehicle Speed Sensor "B" Range/Performance | P | generic | [C] | — | — |
| P2160 | Vehicle Speed Sensor "B" Circuit Low | P | generic | [C] | — | — |
| P2161 | Vehicle Speed Sensor "B" Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2162 | Vehicle Speed Sensor "A" / "B" Correlation | P | generic | [C] | — | — |
| P2163 | Throttle/Pedal Position Sensor "A" Maximum Stop Performance | P | generic | [C] | — | — |
| P2164 | Throttle/Pedal Position Sensor "B" Maximum Stop Performance | P | generic | [C] | — | — |
| P2165 | Throttle/Pedal Position Sensor "C" Maximum Stop Performance | P | generic | [C] | — | — |
| P2166 | Throttle/Pedal Position Sensor "D" Maximum Stop Performance | P | generic | [C] | — | — |
| P2167 | Throttle/Pedal Position Sensor "E" Maximum Stop Performance | P | generic | [C] | — | — |
| P2168 | Throttle/Pedal Position Sensor "F" Maximum Stop Performance | P | generic | [C] | — | — |
| P2169 | Exhaust Pressure Regulator Vent Solenoid Control Circuit/Open | P | generic | [C] | — | — |
| P2170 | Exhaust Pressure Regulator Vent Solenoid Control Circuit Low | P | generic | [C] | — | — |
| P2171 | Exhaust Pressure Regulator Vent Solenoid Control Circuit High | P | generic | [C] | — | — |
| P2172 | Throttle Actuator Control System - Sudden High Airflow Detected | P | generic | [C] | — | — |
| P2173 | Throttle Actuator Control System - High Airflow Detected | P | generic | [C] | — | — |
| P2174 | Throttle Actuator Control System - Sudden Low Airflow Detected | P | generic | [C] | — | — |
| P2175 | Throttle Actuator Control System - Low Airflow Detected | P | generic | [C] | — | — |
| P2176 | Throttle Actuator Control System - Idle Position Not Learned | P | generic | [C] | — | — |
| P2177 | System Too Lean Off Idle (Bank 1) | P | generic | [C] | — | — |
| P2178 | System Too Rich Off Idle (Bank 1) | P | generic | [C] | — | — |
| P2179 | System Too Lean Off Idle (Bank 2) | P | generic | [C] | — | — |
| P2180 | System Too Rich Off Idle (Bank 2) | P | generic | [C] | — | — |
| P2181 | Cooling System Performance | P | generic | [C] | — | — |
| P2182 | Engine Coolant Temperature Sensor 2 Circuit | P | generic | [C] | — | — |
| P2183 | Engine Coolant Temperature Sensor 2 Circuit Range/Performance | P | generic | [C] | — | — |
| P2184 | Engine Coolant Temperature Sensor 2 Circuit Low | P | generic | [C] | — | — |
| P2185 | Engine Coolant Temperature Sensor 2 Circuit High | P | generic | [C] | — | — |
| P2186 | Engine Coolant Temperature Sensor 2 Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2187 | System Too Lean at Idle (Bank 1) | P | generic | [C] | — | — |
| P2188 | System Too Rich at Idle (Bank 1) | P | generic | [C] | — | — |
| P2189 | System Too Lean at Idle (Bank 2) | P | generic | [C] | — | — |
| P2190 | System Too Rich at Idle (Bank 2) | P | generic | [C] | — | — |
| P2191 | System Too Lean at Higher Load (Bank 1) | P | generic | [C] | — | — |
| P2192 | System Too Rich at Higher Load (Bank 1) | P | generic | [C] | — | — |
| P2193 | System Too Lean at Higher Load (Bank 2) | P | generic | [C] | — | — |
| P2194 | System Too Rich at Higher Load (Bank 2) | P | generic | [C] | — | — |
| P2195 | O2 Sensor Signal Stuck Lean (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2196 | O2 Sensor Signal Stuck Rich (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2197 | O2 Sensor Signal Stuck Lean (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2198 | O2 Sensor Signal Stuck Rich (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2199 | Intake Air Temperature Sensor 1 / 2 Correlation | P | generic | [C] | — | — |
| P2200 | NOx Sensor Circuit (Bank 1) | P | generic | [C] | — | — |
| P2201 | NOx Sensor Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P2202 | NOx Sensor Circuit Low Input (Bank 1) | P | generic | [C] | — | — |
| P2203 | NOx Sensor Circuit High Input (Bank 1) | P | generic | [C] | — | — |
| P2204 | NOx Sensor Circuit Intermittent Input (Bank 1) | P | generic | [C] | — | — |
| P2205 | NOx Sensor Heater Control Circuit/Open (Bank 1) | P | generic | [C] | — | — |
| P2206 | NOx Sensor Heater Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2207 | NOx Sensor Heater Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2208 | NOx Sensor Heater Sense Circuit (Bank 1) | P | generic | [C] | — | — |
| P2209 | NOx Sensor Heater Sense Circuit Range/Performance (Bank 1) | P | generic | [C] | — | — |
| P2210 | NOx Sensor Heater Sense Circuit Low Input (Bank 1) | P | generic | [C] | — | — |
| P2211 | NOx Sensor Heater Sense Circuit High Input (Bank 1) | P | generic | [C] | — | — |
| P2212 | NOx Sensor Heater Sense Circuit Intermittent (Bank 1) | P | generic | [C] | — | — |
| P2213 | NOx Sensor Circuit (Bank 2) | P | generic | [C] | — | — |
| P2214 | NOx Sensor Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P2215 | NOx Sensor Circuit Low Input (Bank 2) | P | generic | [C] | — | — |
| P2216 | NOx Sensor Circuit High Input (Bank 2) | P | generic | [C] | — | — |
| P2217 | NOx Sensor Circuit Intermittent Input (Bank 2) | P | generic | [C] | — | — |
| P2218 | NOx Sensor Heater Control Circuit/Open (Bank 2) | P | generic | [C] | — | — |
| P2219 | NOx Sensor Heater Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2220 | NOx Sensor Heater Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2221 | NOx Sensor Heater Sense Circuit (Bank 2) | P | generic | [C] | — | — |
| P2222 | NOx Sensor Heater Sense Circuit Range/Performance (Bank 2) | P | generic | [C] | — | — |
| P2223 | NOx Sensor Heater Sense Circuit Low Input (Bank 2) | P | generic | [C] | — | — |
| P2224 | NOx Sensor Heater Sense Circuit High Input (Bank 2) | P | generic | [C] | — | — |
| P2225 | NOx Sensor Heater Sense Circuit Intermittent (Bank 2) | P | generic | [C] | — | — |
| P2226 | Barometric Pressure Circuit | P | generic | [C] | — | — |
| P2227 | Barometric Pressure Circuit Range/Performance | P | generic | [C] | — | — |
| P2228 | Barometric Pressure Circuit Low | P | generic | [C] | — | — |
| P2229 | Barometric Pressure Circuit High | P | generic | [C] | — | — |
| P2230 | Barometric Pressure Circuit Intermittent | P | generic | [C] | — | — |
| P2231 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2232 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2233 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P2234 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2235 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2236 | O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P2237 | O2 Sensor Positive Current Circuit/Open (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2238 | O2 Sensor Positive Current Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2239 | O2 Sensor Positive Current Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2240 | O2 Sensor Positive Current Circuit/Open (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2241 | O2 Sensor Positive Current Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2242 | O2 Sensor Positive Current Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2243 | O2 Sensor Reference Voltage Circuit/Open (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2244 | O2 Sensor Reference Voltage Performance (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2245 | O2 Sensor Reference Voltage Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2246 | O2 Sensor Reference Voltage Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2247 | O2 Sensor Reference Voltage Circuit/Open (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2248 | O2 Sensor Reference Voltage Performance (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2249 | O2 Sensor Reference Voltage Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2250 | O2 Sensor Reference Voltage Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2251 | O2 Sensor Negative Current Control Circuit/Open (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2252 | O2 Sensor Negative Current Control Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2253 | O2 Sensor Negative Current Control Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2254 | O2 Sensor Negative Current Control Circuit/Open (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2255 | O2 Sensor Negative Current Control Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2256 | O2 Sensor Negative Current Control Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2257 | Secondary Air Injection System Control "A" Circuit Low | P | generic | [C] | — | — |
| P2258 | Secondary Air Injection System Control "A" Circuit High | P | generic | [C] | — | — |
| P2259 | Secondary Air Injection System Control "B" Circuit Low | P | generic | [C] | — | — |
| P2260 | Secondary Air Injection System Control "B" Circuit High | P | generic | [C] | — | — |
| P2261 | Turbo/Super Charger Bypass Valve - Mechanical | P | generic | [C] | — | — |
| P2262 | Turbo Boost Pressure Not Detected - Mechanical | P | generic | [C] | — | — |
| P2263 | Turbo/Super Charger Boost System Performance | P | generic | [C] | — | — |
| P2264 | Water in Fuel Sensor Circuit | P | generic | [C] | — | — |
| P2265 | Water in Fuel Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2266 | Water in Fuel Sensor Circuit Low | P | generic | [C] | — | — |
| P2267 | Water in Fuel Sensor Circuit High | P | generic | [C] | — | — |
| P2268 | Water in Fuel Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2269 | Water in Fuel Condition | P | generic | [C] | — | — |
| P2270 | O2 Sensor Signal Stuck Lean (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2271 | O2 Sensor Signal Stuck Rich (Bank 1 Sensor 2) | P | generic | [C] | — | — |
| P2272 | O2 Sensor Signal Stuck Lean (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2273 | O2 Sensor Signal Stuck Rich (Bank 2 Sensor 2) | P | generic | [C] | — | — |
| P2274 | O2 Sensor Signal Stuck Lean (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P2275 | O2 Sensor Signal Stuck Rich (Bank 1 Sensor 3) | P | generic | [C] | — | — |
| P2276 | O2 Sensor Signal Stuck Lean (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P2277 | O2 Sensor Signal Stuck Rich (Bank 2 Sensor 3) | P | generic | [C] | — | — |
| P2278 | O2 Sensor Signals Swapped Bank 1 Sensor 3 / Bank 2 Sensor 3 | P | generic | [C] | — | — |
| P2279 | Intake Air System Leak | P | generic | [C] | — | — |
| P2280 | Air Flow Restriction / Air Leak Between Air Filter and MAF | P | generic | [C] | — | — |
| P2281 | Air Leak Between MAF and Throttle Body | P | generic | [C] | — | — |
| P2282 | Air Leak Between Throttle Body and Intake Valves | P | generic | [C] | — | — |
| P2283 | Injector Control Pressure Sensor Circuit | P | generic | [C] | — | — |
| P2284 | Injector Control Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2285 | Injector Control Pressure Sensor Circuit Low | P | generic | [C] | — | — |
| P2286 | Injector Control Pressure Sensor Circuit High | P | generic | [C] | — | — |
| P2287 | Injector Control Pressure Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2288 | Injector Control Pressure Too High | P | generic | [C] | — | — |
| P2289 | Injector Control Pressure Too High - Engine Off | P | generic | [C] | — | — |
| P2290 | Injector Control Pressure Too Low | P | generic | [C] | — | — |
| P2291 | Injector Control Pressure Too Low - Engine Cranking | P | generic | [C] | — | — |
| P2292 | Injector Control Pressure Erratic | P | generic | [C] | — | — |
| P2293 | Fuel Pressure Regulator 2 Performance | P | generic | [C] | — | — |
| P2294 | Fuel Pressure Regulator 2 Control Circuit | P | generic | [C] | — | — |
| P2295 | Fuel Pressure Regulator 2 Control Circuit Low | P | generic | [C] | — | — |
| P2296 | Fuel Pressure Regulator 2 Control Circuit High | P | generic | [C] | — | — |
| P2297 | O2 Sensor Out of Range During Deceleration (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2298 | O2 Sensor Out of Range During Deceleration (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2299 | Brake Pedal Position / Accelerator Pedal Position Incompatible | P | generic | [C] | — | — |
| P2300 | Ignition Coil "A" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2301 | Ignition Coil "A" Primary Control Circuit High | P | generic | [C] | — | — |
| P2302 | Ignition Coil "A" Secondary Circuit | P | generic | [C] | — | — |
| P2303 | Ignition Coil "B" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2304 | Ignition Coil "B" Primary Control Circuit High | P | generic | [C] | — | — |
| P2305 | Ignition Coil "B" Secondary Circuit | P | generic | [C] | — | — |
| P2306 | Ignition Coil "C" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2307 | Ignition Coil "C" Primary Control Circuit High | P | generic | [C] | — | — |
| P2308 | Ignition Coil "C" Secondary Circuit | P | generic | [C] | — | — |
| P2309 | Ignition Coil "D" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2310 | Ignition Coil "D" Primary Control Circuit High | P | generic | [C] | — | — |
| P2311 | Ignition Coil "D" Secondary Circuit | P | generic | [C] | — | — |
| P2312 | Ignition Coil "E" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2313 | Ignition Coil "E" Primary Control Circuit High | P | generic | [C] | — | — |
| P2314 | Ignition Coil "E" Secondary Circuit | P | generic | [C] | — | — |
| P2315 | Ignition Coil "F" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2316 | Ignition Coil "F" Primary Control Circuit High | P | generic | [C] | — | — |
| P2317 | Ignition Coil "F" Secondary Circuit | P | generic | [C] | — | — |
| P2318 | Ignition Coil "G" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2319 | Ignition Coil "G" Primary Control Circuit High | P | generic | [C] | — | — |
| P2320 | Ignition Coil "G" Secondary Circuit | P | generic | [C] | — | — |
| P2321 | Ignition Coil "H" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2322 | Ignition Coil "H" Primary Control Circuit High | P | generic | [C] | — | — |
| P2323 | Ignition Coil "H" Secondary Circuit | P | generic | [C] | — | — |
| P2324 | Ignition Coil "I" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2325 | Ignition Coil "I" Primary Control Circuit High | P | generic | [C] | — | — |
| P2326 | Ignition Coil "I" Secondary Circuit | P | generic | [C] | — | — |
| P2327 | Ignition Coil "J" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2328 | Ignition Coil "J" Primary Control Circuit High | P | generic | [C] | — | — |
| P2329 | Ignition Coil "J" Secondary Circuit | P | generic | [C] | — | — |
| P2330 | Ignition Coil "K" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2331 | Ignition Coil "K" Primary Control Circuit High | P | generic | [C] | — | — |
| P2332 | Ignition Coil "K" Secondary Circuit | P | generic | [C] | — | — |
| P2333 | Ignition Coil "L" Primary Control Circuit Low | P | generic | [C] | — | — |
| P2334 | Ignition Coil "L" Primary Control Circuit High | P | generic | [C] | — | — |
| P2335 | Ignition Coil "L" Secondary Circuit | P | generic | [C] | — | — |
| P2336 | Cylinder #1 Above Knock Threshold | P | generic | [C] | — | — |
| P2337 | Cylinder #2 Above Knock Threshold | P | generic | [C] | — | — |
| P2338 | Cylinder #3 Above Knock Threshold | P | generic | [C] | — | — |
| P2339 | Cylinder #4 Above Knock Threshold | P | generic | [C] | — | — |
| P2340 | Cylinder #5 Above Knock Threshold | P | generic | [C] | — | — |
| P2341 | Cylinder #6 Above Knock Threshold | P | generic | [C] | — | — |
| P2342 | Cylinder #7 Above Knock Threshold | P | generic | [C] | — | — |
| P2343 | Cylinder #8 Above Knock Threshold | P | generic | [C] | — | — |
| P2344 | Cylinder #9 Above Knock Threshold | P | generic | [C] | — | — |
| P2345 | Cylinder #10 Above Knock Threshold | P | generic | [C] | — | — |
| P2346 | Cylinder #11 Above Knock Threshold | P | generic | [C] | — | — |
| P2347 | Cylinder #12 Above Knock Threshold | P | generic | [C] | — | — |
| P2400 | Evaporative Emission System Leak Detection Pump Control Circuit/Open | P | generic | [C] | — | — |
| P2401 | Evaporative Emission System Leak Detection Pump Control Circuit Low | P | generic | [C] | — | — |
| P2402 | Evaporative Emission System Leak Detection Pump Control Circuit High | P | generic | [C] | — | — |
| P2403 | Evaporative Emission System Leak Detection Pump Sense Circuit/Open | P | generic | [C] | — | — |
| P2404 | Evaporative Emission System Leak Detection Pump Sense Circuit Range/Performance | P | generic | [C] | — | — |
| P2405 | Evaporative Emission System Leak Detection Pump Sense Circuit Low | P | generic | [C] | — | — |
| P2406 | Evaporative Emission System Leak Detection Pump Sense Circuit High | P | generic | [C] | — | — |
| P2407 | Evaporative Emission System Leak Detection Pump Sense Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2408 | Fuel Cap Sensor/Switch Circuit | P | generic | [C] | — | — |
| P2409 | Fuel Cap Sensor/Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2410 | Fuel Cap Sensor/Switch Circuit Low | P | generic | [C] | — | — |
| P2411 | Fuel Cap Sensor/Switch Circuit High | P | generic | [C] | — | — |
| P2412 | Fuel Cap Sensor/Switch Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2413 | Exhaust Gas Recirculation System Performance | P | generic | [C] | — | — |
| P2414 | O2 Sensor Exhaust Sample Error (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2415 | O2 Sensor Exhaust Sample Error (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2416 | O2 Sensor Signals Swapped Bank 1 Sensor 2 / Bank 1 Sensor 3 | P | generic | [C] | — | — |
| P2417 | O2 Sensor Signals Swapped Bank 2 Sensor 2 / Bank 2 Sensor 3 | P | generic | [C] | — | — |
| P2418 | Evaporative Emission System Switching Valve Control Circuit/Open | P | generic | [C] | — | — |
| P2419 | Evaporative Emission System Switching Valve Control Circuit Low | P | generic | [C] | — | — |
| P2420 | Evaporative Emission System Switching Valve Control Circuit High | P | generic | [C] | — | — |
| P2421 | Evaporative Emission System Vent Valve Stuck Open | P | generic | [C] | — | — |
| P2422 | Evaporative Emission System Vent Valve Stuck Closed | P | generic | [C] | — | — |
| P2423 | HC Adsorption Catalyst Efficiency Below Threshold (Bank 1) | P | generic | [C] | — | — |
| P2424 | HC Adsorption Catalyst Efficiency Below Threshold (Bank 2) | P | generic | [C] | — | — |
| P2425 | Exhaust Gas Recirculation Cooling Valve Control Circuit/Open | P | generic | [C] | — | — |
| P2426 | Exhaust Gas Recirculation Cooling Valve Control Circuit Low | P | generic | [C] | — | — |
| P2427 | Exhaust Gas Recirculation Cooling Valve Control Circuit High | P | generic | [C] | — | — |
| P2428 | Exhaust Gas Temperature Too High | P | generic | [C] | — | — |
| P2429 | Exhaust Gas Temperature Too High | P | generic | [C] | — | — |
| P2430 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit | P | generic | [C] | — | — |
| P2431 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2432 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Low | P | generic | [C] | — | — |
| P2433 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit High | P | generic | [C] | — | — |
| P2434 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2435 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit | P | generic | [C] | — | — |
| P2436 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2437 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Low | P | generic | [C] | — | — |
| P2438 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit High | P | generic | [C] | — | — |
| P2439 | Secondary Air Injection System Air Flow/Pressure Sensor Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2440 | Secondary Air Injection System Switching Valve Stuck Open | P | generic | [C] | — | — |
| P2441 | Secondary Air Injection System Switching Valve Stuck Closed | P | generic | [C] | — | — |
| P2442 | Secondary Air Injection System Switching Valve Stuck Open | P | generic | [C] | — | — |
| P2443 | Secondary Air Injection System Switching Valve Stuck Closed | P | generic | [C] | — | — |
| P2444 | Secondary Air Injection System Pump Stuck On | P | generic | [C] | — | — |
| P2445 | Secondary Air Injection System Pump Stuck Off | P | generic | [C] | — | — |
| P2446 | Secondary Air Injection System Pump Stuck On | P | generic | [C] | — | — |
| P2447 | Secondary Air Injection System Pump Stuck Off | P | generic | [C] | — | — |
| P2500 | Generator Lamp/L-Terminal Circuit Low | P | generic | [C] | — | — |
| P2501 | Generator Lamp/L-Terminal Circuit High | P | generic | [C] | — | — |
| P2502 | Charging System Voltage | P | generic | [C] | — | — |
| P2503 | Charging System Voltage Low | P | generic | [C] | — | — |
| P2504 | Charging System Voltage High | P | generic | [C] | — | — |
| P2505 | ECM/PCM Power Input Signal | P | generic | [C] | — | — |
| P2506 | ECM/PCM Power Input Signal Range Performance | P | generic | [C] | — | — |
| P2507 | ECM/PCM Power Input Signal Low | P | generic | [C] | — | — |
| P2508 | ECM/PCM Power Input Signal High | P | generic | [C] | — | — |
| P2509 | ECM/PCM Power Input Signal Intermittent | P | generic | [C] | — | — |
| P2510 | ECM/PCM Power Relay Sense Circuit Range/Performance | P | generic | [C] | — | — |
| P2511 | ECM/PCM Power Relay Sense Circuit Intermittent | P | generic | [C] | — | — |
| P2512 | Event Data Recorder Request Circuit/Open | P | generic | [C] | — | — |
| P2513 | Event Data Recorder Request Circuit Low | P | generic | [C] | — | — |
| P2514 | Event Data Recorder Request Circuit High | P | generic | [C] | — | — |
| P2515 | A/C Refrigerant Pressure Sensor "B" Circuit | P | generic | [C] | — | — |
| P2516 | A/C Refrigerant Pressure Sensor "B" Circuit Range/Performance | P | generic | [C] | — | — |
| P2517 | A/C Refrigerant Pressure Sensor "B" Circuit Low | P | generic | [C] | — | — |
| P2518 | A/C Refrigerant Pressure Sensor "B" Circuit High | P | generic | [C] | — | — |
| P2519 | A/C Request "A" Circuit | P | generic | [C] | — | — |
| P2520 | A/C Request "A" Circuit Low | P | generic | [C] | — | — |
| P2521 | A/C Request "A" Circuit High | P | generic | [C] | — | — |
| P2522 | A/C Request "B" Circuit | P | generic | [C] | — | — |
| P2523 | A/C Request "B" Circuit Low | P | generic | [C] | — | — |
| P2524 | A/C Request "B" Circuit High | P | generic | [C] | — | — |
| P2525 | Vacuum Reservoir Pressure Sensor Circuit | P | generic | [C] | — | — |
| P2526 | Vacuum Reservoir Pressure Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2527 | Vacuum Reservoir Pressure Sensor Circuit Low | P | generic | [C] | — | — |
| P2528 | Vacuum Reservoir Pressure Sensor Circuit High | P | generic | [C] | — | — |
| P2529 | Vacuum Reservoir Pressure Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2530 | Ignition Switch Run Position Circuit | P | generic | [C] | — | — |
| P2531 | Ignition Switch Run Position Circuit Low | P | generic | [C] | — | — |
| P2532 | Ignition Switch Run Position Circuit High | P | generic | [C] | — | — |
| P2533 | Ignition Switch Run/Start Position Circuit | P | generic | [C] | — | — |
| P2534 | Ignition Switch Run/Start Position Circuit Low | P | generic | [C] | — | — |
| P2535 | Ignition Switch Run/Start Position Circuit High | P | generic | [C] | — | — |
| P2536 | Ignition Switch Accessory Position Circuit | P | generic | [C] | — | — |
| P2537 | Ignition Switch Accessory Position Circuit Low | P | generic | [C] | — | — |
| P2538 | Ignition Switch Accessory Position Circuit High | P | generic | [C] | — | — |
| P2539 | Low Pressure Fuel System Sensor Circuit | P | generic | [C] | — | — |
| P2540 | Low Pressure Fuel System Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2541 | Low Pressure Fuel System Sensor Circuit Low | P | generic | [C] | — | — |
| P2542 | Low Pressure Fuel System Sensor Circuit High | P | generic | [C] | — | — |
| P2543 | Low Pressure Fuel System Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2544 | Torque Management Request Input Signal "A" | P | generic | [C] | — | — |
| P2545 | Torque Management Request Input Signal "A" Range/Performance | P | generic | [C] | — | — |
| P2546 | Torque Management Request Input Signal "A" Low | P | generic | [C] | — | — |
| P2547 | Torque Management Request Input Signal "A" High | P | generic | [C] | — | — |
| P2548 | Torque Management Request Input Signal "B" | P | generic | [C] | — | — |
| P2549 | Torque Management Request Input Signal "B" Range/Performance | P | generic | [C] | — | — |
| P2550 | Torque Management Request Input Signal "B" Low | P | generic | [C] | — | — |
| P2551 | Torque Management Request Input Signal "B" High | P | generic | [C] | — | — |
| P2552 | Throttle/Fuel Inhibit Circuit | P | generic | [C] | — | — |
| P2553 | Throttle/Fuel Inhibit Circuit Range/Performance | P | generic | [C] | — | — |
| P2554 | Throttle/Fuel Inhibit Circuit Low | P | generic | [C] | — | — |
| P2555 | Throttle/Fuel Inhibit Circuit High | P | generic | [C] | — | — |
| P2556 | Engine Coolant Level Sensor/Switch Circuit | P | generic | [C] | — | — |
| P2557 | Engine Coolant Level Sensor/Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2558 | Engine Coolant Level Sensor/Switch Circuit Low | P | generic | [C] | — | — |
| P2559 | Engine Coolant Level Sensor/Switch Circuit High | P | generic | [C] | — | — |
| P2560 | Engine Coolant Level Low | P | generic | [C] | — | — |
| P2561 | A/C Control Module Requested MIL Illumination | P | generic | [C] | — | — |
| P2562 | Turbocharger Boost Control Position Sensor Circuit | P | generic | [C] | — | — |
| P2563 | Turbocharger Boost Control Position Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2564 | Turbocharger Boost Control Position Sensor Circuit Low | P | generic | [C] | — | — |
| P2565 | Turbocharger Boost Control Position Sensor Circuit High | P | generic | [C] | — | — |
| P2566 | Turbocharger Boost Control Position Sensor Circuit Intermittent | P | generic | [C] | — | — |
| P2567 | Direct Ozone Reduction Catalyst Temperature Sensor Circuit | P | generic | [C] | — | — |
| P2568 | Direct Ozone Reduction Catalyst Temperature Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2569 | Direct Ozone Reduction Catalyst Temperature Sensor Circuit Low | P | generic | [C] | — | — |
| P2570 | Direct Ozone Reduction Catalyst Temperature Sensor Circuit High | P | generic | [C] | — | — |
| P2571 | Direct Ozone Reduction Catalyst Temperature Sensor Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2572 | Direct Ozone Reduction Catalyst Deterioration Sensor Circuit | P | generic | [C] | — | — |
| P2573 | Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Range/Performance | P | generic | [C] | — | — |
| P2574 | Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Low | P | generic | [C] | — | — |
| P2575 | Direct Ozone Reduction Catalyst Deterioration Sensor Circuit High | P | generic | [C] | — | — |
| P2576 | Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2577 | Direct Ozone Reduction Catalyst Efficiency Below Threshold | P | generic | [C] | — | — |
| P2600 | Coolant Pump Control Circuit/Open | P | generic | [C] | — | — |
| P2601 | Coolant Pump Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2602 | Coolant Pump Control Circuit Low | P | generic | [C] | — | — |
| P2603 | Coolant Pump Control Circuit High | P | generic | [C] | — | — |
| P2604 | Intake Air Heater "A" Circuit Range/Performance | P | generic | [C] | — | — |
| P2605 | Intake Air Heater "A" Circuit/Open | P | generic | [C] | — | — |
| P2606 | Intake Air Heater "B" Circuit Range/Performance | P | generic | [C] | — | — |
| P2607 | Intake Air Heater "B" Circuit Low | P | generic | [C] | — | — |
| P2608 | Intake Air Heater "B" Circuit High | P | generic | [C] | — | — |
| P2609 | Intake Air Heater System Performance | P | generic | [C] | — | — |
| P2610 | ECM/PCM Internal Engine Off Timer Performance | P | generic | [C] | — | — |
| P2611 | A/C Refrigerant Distribution Valve Control Circuit/Open | P | generic | [C] | — | — |
| P2612 | A/C Refrigerant Distribution Valve Control Circuit Low | P | generic | [C] | — | — |
| P2613 | A/C Refrigerant Distribution Valve Control Circuit High | P | generic | [C] | — | — |
| P2614 | Camshaft Position Signal Output Circuit/Open | P | generic | [C] | — | — |
| P2615 | Camshaft Position Signal Output Circuit Low | P | generic | [C] | — | — |
| P2616 | Camshaft Position Signal Output Circuit High | P | generic | [C] | — | — |
| P2617 | Crankshaft Position Signal Output Circuit/Open | P | generic | [C] | — | — |
| P2618 | Crankshaft Position Signal Output Circuit Low | P | generic | [C] | — | — |
| P2619 | Crankshaft Position Signal Output Circuit High | P | generic | [C] | — | — |
| P2620 | Throttle Position Output Circuit/Open | P | generic | [C] | — | — |
| P2621 | Throttle Position Output Circuit Low | P | generic | [C] | — | — |
| P2622 | Throttle Position Output Circuit High | P | generic | [C] | — | — |
| P2623 | Injector Control Pressure Regulator Circuit/Open | P | generic | [C] | — | — |
| P2624 | Injector Control Pressure Regulator Circuit Low | P | generic | [C] | — | — |
| P2625 | Injector Control Pressure Regulator Circuit High | P | generic | [C] | — | — |
| P2626 | O2 Sensor Pumping Current Trim Circuit/Open (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2627 | O2 Sensor Pumping Current Trim Circuit Low (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2628 | O2 Sensor Pumping Current Trim Circuit High (Bank 1 Sensor 1) | P | generic | [C] | — | — |
| P2629 | O2 Sensor Pumping Current Trim Circuit/Open (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2630 | O2 Sensor Pumping Current Trim Circuit Low (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2631 | O2 Sensor Pumping Current Trim Circuit High (Bank 2 Sensor 1) | P | generic | [C] | — | — |
| P2632 | Fuel Pump "B" Control Circuit/Open | P | generic | [C] | — | — |
| P2633 | Fuel Pump "B" Control Circuit Low | P | generic | [C] | — | — |
| P2634 | Fuel Pump "B" Control Circuit High | P | generic | [C] | — | — |
| P2635 | Fuel Pump "A" Low Flow/Performance | P | generic | [C] | — | — |
| P2636 | Fuel Pump "B" Low Flow/Performance | P | generic | [C] | — | — |
| P2637 | Torque Management Feedback Signal "A" | P | generic | [C] | — | — |
| P2638 | Torque Management Feedback Signal "A" Range/Performance | P | generic | [C] | — | — |
| P2639 | Torque Management Feedback Signal "A" Low | P | generic | [C] | — | — |
| P2640 | Torque Management Feedback Signal "A" High | P | generic | [C] | — | — |
| P2641 | Torque Management Feedback Signal "B" | P | generic | [C] | — | — |
| P2642 | Torque Management Feedback Signal "B" Range/Performance | P | generic | [C] | — | — |
| P2643 | Torque Management Feedback Signal "B" Low | P | generic | [C] | — | — |
| P2644 | Torque Management Feedback Signal "B" High | P | generic | [C] | — | — |
| P2645 | A Rocker Arm Actuator Control Circuit/Open (Bank 1) | P | generic | [C] | — | — |
| P2646 | A Rocker Arm Actuator System Performance or Stuck Off (Bank 1) | P | generic | [C] | — | — |
| P2647 | A Rocker Arm Actuator System Stuck On (Bank 1) | P | generic | [C] | — | — |
| P2648 | A Rocker Arm Actuator Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2649 | A Rocker Arm Actuator Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2650 | B Rocker Arm Actuator Control Circuit/Open (Bank 1) | P | generic | [C] | — | — |
| P2651 | B Rocker Arm Actuator System Performance or Stuck Off (Bank 1) | P | generic | [C] | — | — |
| P2652 | B Rocker Arm Actuator System Stuck On (Bank 1) | P | generic | [C] | — | — |
| P2653 | B Rocker Arm Actuator Control Circuit Low (Bank 1) | P | generic | [C] | — | — |
| P2654 | B Rocker Arm Actuator Control Circuit High (Bank 1) | P | generic | [C] | — | — |
| P2655 | A Rocker Arm Actuator Control Circuit/Open (Bank 2) | P | generic | [C] | — | — |
| P2656 | A Rocker Arm Actuator System Performance or Stuck Off (Bank 2) | P | generic | [C] | — | — |
| P2657 | A Rocker Arm Actuator System Stuck On (Bank 2) | P | generic | [C] | — | — |
| P2658 | A Rocker Arm Actuator Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2659 | A Rocker Arm Actuator Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2660 | B Rocker Arm Actuator Control Circuit/Open (Bank 2) | P | generic | [C] | — | — |
| P2661 | B Rocker Arm Actuator System Performance or Stuck Off (Bank 2) | P | generic | [C] | — | — |
| P2662 | B Rocker Arm Actuator System Stuck On (Bank 2) | P | generic | [C] | — | — |
| P2663 | B Rocker Arm Actuator Control Circuit Low (Bank 2) | P | generic | [C] | — | — |
| P2664 | B Rocker Arm Actuator Control Circuit High (Bank 2) | P | generic | [C] | — | — |
| P2665 | Fuel Shutoff Valve "B" Control Circuit/Open | P | generic | [C] | — | — |
| P2666 | Fuel Shutoff Valve "B" Control Circuit Low | P | generic | [C] | — | — |
| P2667 | Fuel Shutoff Valve "B" Control Circuit High | P | generic | [C] | — | — |
| P2668 | Fuel Mode Indicator Lamp Control Circuit | P | generic | [C] | — | — |
| P2669 | Actuator Supply Voltage "B" Circuit /Open | P | generic | [C] | — | — |
| P2670 | Actuator Supply Voltage "B" Circuit Low | P | generic | [C] | — | — |
| P2671 | Actuator Supply Voltage "B" Circuit High | P | generic | [C] | — | — |
| P2700 | Transmission Friction Element "A" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2701 | Transmission Friction Element "B" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2702 | Transmission Friction Element "C" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2703 | Transmission Friction Element "D" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2704 | Transmission Friction Element "E" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2705 | Transmission Friction Element "F" Apply Time Range/Performance | P | generic | [C] | — | — |
| P2706 | Shift Solenoid "F" | P | generic | [C] | — | — |
| P2707 | Shift Solenoid "F" Performance or Stuck Off | P | generic | [C] | — | — |
| P2708 | Shift Solenoid "F" Stuck On | P | generic | [C] | — | — |
| P2709 | Shift Solenoid "F" Electrical | P | generic | [C] | — | — |
| P2710 | Shift Solenoid "F" Intermittent | P | generic | [C] | — | — |
| P2711 | Unexpected Mechanical Gear Disengagement | P | generic | [C] | — | — |
| P2712 | Hydraulic Power Unit Leakage | P | generic | [C] | — | — |
| P2713 | Pressure Control Solenoid "D" | P | generic | [C] | — | — |
| P2714 | Pressure Control Solenoid "D" Performance or Stuck Off | P | generic | [C] | — | — |
| P2715 | Pressure Control Solenoid "D" Stuck On | P | generic | [C] | — | — |
| P2716 | Pressure Control Solenoid "D" Electrical | P | generic | [C] | — | — |
| P2717 | Pressure Control Solenoid "D" Intermittent | P | generic | [C] | — | — |
| P2718 | Pressure Control Solenoid "D" Control Circuit/Open | P | generic | [C] | — | — |
| P2719 | Pressure Control Solenoid "D" Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2720 | Pressure Control Solenoid "D" Control Circuit Low | P | generic | [C] | — | — |
| P2721 | Pressure Control Solenoid "D" Control Circuit High | P | generic | [C] | — | — |
| P2722 | Pressure Control Solenoid "E" | P | generic | [C] | — | — |
| P2723 | Pressure Control Solenoid "E" Performance or Stuck Off | P | generic | [C] | — | — |
| P2724 | Pressure Control Solenoid "E" Stuck On | P | generic | [C] | — | — |
| P2725 | Pressure Control Solenoid "E" Electrical | P | generic | [C] | — | — |
| P2726 | Pressure Control Solenoid "E" Intermittent | P | generic | [C] | — | — |
| P2727 | Pressure Control Solenoid "E" Control Circuit/Open | P | generic | [C] | — | — |
| P2728 | Pressure Control Solenoid "E" Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2729 | Pressure Control Solenoid "E" Control Circuit Low | P | generic | [C] | — | — |
| P2730 | Pressure Control Solenoid "E" Control Circuit High | P | generic | [C] | — | — |
| P2731 | Pressure Control Solenoid "F" | P | generic | [C] | — | — |
| P2732 | Pressure Control Solenoid "F" Performance or Stuck Off | P | generic | [C] | — | — |
| P2733 | Pressure Control Solenoid "F" Stuck On | P | generic | [C] | — | — |
| P2734 | Pressure Control Solenoid "F" Electrical | P | generic | [C] | — | — |
| P2735 | Pressure Control Solenoid "F" Intermittent | P | generic | [C] | — | — |
| P2736 | Pressure Control Solenoid "F" Control Circuit/Open | P | generic | [C] | — | — |
| P2737 | Pressure Control Solenoid "F" Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2738 | Pressure Control Solenoid "F" Control Circuit Low | P | generic | [C] | — | — |
| P2739 | Pressure Control Solenoid "F" Control Circuit High | P | generic | [C] | — | — |
| P2740 | Transmission Fluid Temperature Sensor "B" Circuit | P | generic | [C] | — | — |
| P2741 | Transmission Fluid Temperature Sensor "B" Circuit Range/Performance | P | generic | [C] | — | — |
| P2742 | Transmission Fluid Temperature Sensor "B" Circuit Low | P | generic | [C] | — | — |
| P2743 | Transmission Fluid Temperature Sensor "B" Circuit High | P | generic | [C] | — | — |
| P2744 | Transmission Fluid Temperature Sensor "B" Circuit Intermittent | P | generic | [C] | — | — |
| P2745 | Intermediate Shaft Speed Sensor "B" Circuit | P | generic | [C] | — | — |
| P2746 | Intermediate Shaft Speed Sensor "B" Circuit Range/Performance | P | generic | [C] | — | — |
| P2747 | Intermediate Shaft Speed Sensor "B" Circuit No Signal | P | generic | [C] | — | — |
| P2748 | Intermediate Shaft Speed Sensor "B" Circuit Intermittent | P | generic | [C] | — | — |
| P2749 | Intermediate Shaft Speed Sensor "C" Circuit | P | generic | [C] | — | — |
| P2750 | Intermediate Shaft Speed Sensor "C" Circuit Range/Performance | P | generic | [C] | — | — |
| P2751 | Intermediate Shaft Speed Sensor "C" Circuit No Signal | P | generic | [C] | — | — |
| P2752 | Intermediate Shaft Speed Sensor "C" Circuit Intermittent | P | generic | [C] | — | — |
| P2753 | Transmission Fluid Cooler Control Circuit/Open | P | generic | [C] | — | — |
| P2754 | Transmission Fluid Cooler Control Circuit Low | P | generic | [C] | — | — |
| P2755 | Transmission Fluid Cooler Control Circuit High | P | generic | [C] | — | — |
| P2756 | Torque Converter Clutch Pressure Control Solenoid | P | generic | [C] | — | — |
| P2757 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Performance or Stuck Off | P | generic | [C] | — | — |
| P2758 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Stuck on | P | generic | [C] | — | — |
| P2759 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Electrical | P | generic | [C] | — | — |
| P2760 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Intermittent | P | generic | [C] | — | — |
| P2761 | Torque Converter Clutch Pressure Control Solenoid Control Circuit/Open | P | generic | [C] | — | — |
| P2762 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2763 | Torque Converter Clutch Pressure Control Solenoid Control Circuit Low | P | generic | [C] | — | — |
| P2764 | Torque Converter Clutch Pressure Control Solenoid Control Circuit High | P | generic | [C] | — | — |
| P2765 | Input/Turbine Speed Sensor "B" Circuit | P | generic | [C] | — | — |
| P2766 | Input/Turbine Speed Sensor "B" Circuit Range/Performance | P | generic | [C] | — | — |
| P2767 | Input/Turbine Speed Sensor "B" Circuit No Signal | P | generic | [C] | — | — |
| P2768 | Input/Turbine Speed Sensor "B" Circuit Intermittent | P | generic | [C] | — | — |
| P2769 | Torque Converter Clutch Circuit Low | P | generic | [C] | — | — |
| P2770 | Torque Converter Clutch Circuit High | P | generic | [C] | — | — |
| P2771 | Four Wheel Drive (4WD) Low Switch Circuit | P | generic | [C] | — | — |
| P2772 | Four Wheel Drive (4WD) Low Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2773 | Four Wheel Drive (4WD) Low Switch Circuit Low | P | generic | [C] | — | — |
| P2774 | Four Wheel Drive (4WD) Low Switch Circuit High | P | generic | [C] | — | — |
| P2775 | Upshift Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2776 | Upshift Switch Circuit Low | P | generic | [C] | — | — |
| P2777 | Upshift Switch Circuit High | P | generic | [C] | — | — |
| P2778 | Upshift Switch Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2779 | Downshift Switch Circuit Range/Performance | P | generic | [C] | — | — |
| P2780 | Downshift Switch Circuit Low | P | generic | [C] | — | — |
| P2781 | Downshift Switch Circuit High | P | generic | [C] | — | — |
| P2782 | Downshift Switch Circuit Intermittent/Erratic | P | generic | [C] | — | — |
| P2783 | Torque Converter Temperature Too High | P | generic | [C] | — | — |
| P2784 | Input/Turbine Speed Sensor "A"/"B" Correlation | P | generic | [C] | — | — |
| P2785 | Clutch Actuator Temperature Too High | P | generic | [C] | — | — |
| P2786 | Gear Shift Actuator Temperature Too High | P | generic | [C] | — | — |
| P2787 | Clutch Temperature Too High | P | generic | [C] | — | — |
| P2788 | Auto Shift Manual Adaptive Learning at Limit | P | generic | [C] | — | — |
| P2789 | Clutch Adaptive Learning at Limit | P | generic | [C] | — | — |
| P2790 | Gate Select Direction Circuit | P | generic | [C] | — | — |
| P2791 | Gate Select Direction Circuit Low | P | generic | [C] | — | — |
| P2792 | Gate Select Direction Circuit High | P | generic | [C] | — | — |
| P2793 | Gear Shift Direction Circuit | P | generic | [C] | — | — |
| P2794 | Gear Shift Direction Circuit Low | P | generic | [C] | — | — |
| P2795 | Gear Shift Direction Circuit High | P | generic | [C] | — | — |
| P2821 | Pressure Control Solenoid J Stuck On | P | generic | [C] | — | — |
| P2822 | Pressure Control Solenoid J Electrical | P | generic | [C] | — | — |
| P2823 | Pressure Control Solenoid J Intermittent | P | generic | [C] | — | — |
| P2824 | Pressure Control Solenoid J Control Circuit / Open | P | generic | [C] | — | — |
| P2825 | Pressure Control Solenoid J Control Circuit Range/Performance | P | generic | [C] | — | — |
| P2826 | Pressure Control Solenoid J Control Circuit Low | P | generic | [C] | — | — |
| P2827 | Pressure Control Solenoid J Control Circuit High | P | generic | [C] | — | — |
| P2828 | Pressure Control Solenoid K | P | generic | [C] | — | — |
| P2829 | Pressure Control Solenoid K Performance or Stuck Off | P | generic | [C] | — | — |
| P2830 | Pressure Control Solenoid K Control Circuit High | P | generic | [C] | — | — |
| P2A00 | O2 Sensor Circuit Range/Performance Bank 1 Sensor 1 | P | generic | [C] | — | — |
| P2A01 | O2 Sensor Circuit Range/Performance Bank 1 Sensor 2 | P | generic | [C] | — | — |
| P2A02 | O2 Sensor Circuit Range/Performance Bank 1 Sensor 3 | P | generic | [C] | — | — |
| P2A03 | O2 Sensor Circuit Range/Performance Bank 2 Sensor 1 | P | generic | [C] | — | — |
| P2A04 | O2 Sensor Circuit Range/Performance Bank 2 Sensor 2 | P | generic | [C] | — | — |
| P2A05 | O2 Sensor Circuit Range/Performance Bank 2 Sensor 3 | P | generic | [C] | — | — |
| P3400 | Cylinder Deactivation System | P | generic | [B] | — | — |
| P3401 | Cylinder 1 Deactivation/Intake Valve Control Circuit/Open | P | generic | [B] | — | — |
| P3402 | Cylinder 1 Deactivation/Intake Valve Control Performance | P | generic | [B] | — | — |
| P3403 | Cylinder 1 Deactivation/Intake Valve Control Circuit Low | P | generic | [B] | — | — |
| P3404 | Cylinder 1 Deactivation/Intake Valve Control Circuit High | P | generic | [B] | — | — |
| P3405 | Cylinder 1 Exhaust Valve Control Circuit/Open | P | generic | [B] | — | — |
| P3406 | Cylinder 1 Exhaust Valve Control Performance | P | generic | [B] | — | — |
| P3407 | Cylinder 1 Exhaust Valve Control Circuit Low | P | generic | [B] | — | — |
| P3408 | Cylinder 1 Exhaust Valve Control Circuit High | P | generic | [B] | — | — |
| P3409 | Cylinder 2 Deactivation/Intake Valve Control Circuit/Open | P | generic | [B] | — | — |
| P3410 | Cylinder 2 Deactivation/Intake Valve Control Performance | P | generic | [B] | — | — |
| P3411 | Cylinder 2 Deactivation/Intake Valve Control Circuit Low | P | generic | [B] | — | — |
| P3412 | Cylinder 2 Deactivation/Intake Valve Control Circuit High | P | generic | [B] | — | — |
| P3413 | Cylinder 2 Exhaust Valve Control Circuit/Open | P | generic | [B] | — | — |
| P3414 | Cylinder 2 Exhaust Valve Control Performance | P | generic | [B] | — | — |
| P3415 | Cylinder 2 Exhaust Valve Control Circuit Low | P | generic | [B] | — | — |
| P3416 | Cylinder 2 Exhaust Valve Control Circuit High | P | generic | [B] | — | — |
| P3417 | Cylinder 3 Deactivation/Intake Valve Control Circuit/Open | P | generic | [B] | — | — |
| P3418 | Cylinder 3 Deactivation/Intake Valve Control Performance | P | generic | [B] | — | — |
| P3419 | Cylinder 3 Deactivation/Intake Valve Control Circuit Low | P | generic | [B] | — | — |
| P3420 | Cylinder 3 Deactivation/Intake Valve Control Circuit High | P | generic | [B] | — | — |
| P3421 | Cylinder 3 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3422 | Cylinder 3 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3423 | Cylinder 3 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3424 | Cylinder 3 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3425 | Cylinder 4 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3426 | Cylinder 4 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3427 | Cylinder 4 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3428 | Cylinder 4 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3429 | Cylinder 4 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3430 | Cylinder 4 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3431 | Cylinder 4 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3432 | Cylinder 4 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3433 | Cylinder 5 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3434 | Cylinder 5 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3435 | Cylinder 5 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3436 | Cylinder 5 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3437 | Cylinder 5 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3438 | Cylinder 5 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3439 | Cylinder 5 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3440 | Cylinder 5 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3441 | Cylinder 6 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3442 | Cylinder 6 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3443 | Cylinder 6 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3444 | Cylinder 6 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3445 | Cylinder 6 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3446 | Cylinder 6 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3447 | Cylinder 6 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3448 | Cylinder 6 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3449 | Cylinder 7 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3450 | Cylinder 7 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3451 | Cylinder 7 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3452 | Cylinder 7 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3453 | Cylinder 7 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3454 | Cylinder 7 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3455 | Cylinder 7 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3456 | Cylinder 7 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3457 | Cylinder 8 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3458 | Cylinder 8 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3459 | Cylinder 8 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3460 | Cylinder 8 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3461 | Cylinder 8 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3462 | Cylinder 8 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3463 | Cylinder 8 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3464 | Cylinder 8 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3465 | Cylinder 9 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3466 | Cylinder 9 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3467 | Cylinder 9 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3468 | Cylinder 9 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3469 | Cylinder 9 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3470 | Cylinder 9 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3471 | Cylinder 9 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3472 | Cylinder 9 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3473 | Cylinder 10 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3474 | Cylinder 10 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3475 | Cylinder 10 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3476 | Cylinder 10 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3477 | Cylinder 10 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3478 | Cylinder 10 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3479 | Cylinder 10 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3480 | Cylinder 10 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3481 | Cylinder 11 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3482 | Cylinder 11 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3483 | Cylinder 11 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3484 | Cylinder 11 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3485 | Cylinder 11 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3486 | Cylinder 11 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3487 | Cylinder 11 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3488 | Cylinder 11 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| P3489 | Cylinder 12 Deactivation/Intake Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3490 | Cylinder 12 Deactivation/Intake Valve Control Performance | P | generic | [C] | — | — |
| P3491 | Cylinder 12 Deactivation/Intake Valve Control Circuit Low | P | generic | [C] | — | — |
| P3492 | Cylinder 12 Deactivation/Intake Valve Control Circuit High | P | generic | [C] | — | — |
| P3493 | Cylinder 12 Exhaust Valve Control Circuit/Open | P | generic | [C] | — | — |
| P3494 | Cylinder 12 Exhaust Valve Control Performance | P | generic | [C] | — | — |
| P3495 | Cylinder 12 Exhaust Valve Control Circuit Low | P | generic | [C] | — | — |
| P3496 | Cylinder 12 Exhaust Valve Control Circuit High | P | generic | [C] | — | — |
| U0001 | High Speed CAN Communication Bus | U | generic | [B] | — | — |
| U0002 | High Speed CAN Communication Bus Performance | U | generic | [B] | — | — |
| U0003 | High Speed CAN Communication Bus (+) Open | U | generic | [B] | — | — |
| U0004 | High Speed CAN Communication Bus (+) Low | U | generic | [B] | — | — |
| U0005 | High Speed CAN Communication Bus (+) High | U | generic | [B] | — | — |
| U0006 | High Speed CAN Communication Bus (-) Open | U | generic | [B] | — | — |
| U0007 | High Speed CAN Communication Bus (-) Low | U | generic | [B] | — | — |
| U0008 | High Speed CAN Communication Bus (-) High | U | generic | [B] | — | — |
| U0009 | High Speed CAN Communication Bus (-) shorted to Bus (+) | U | generic | [B] | — | — |
| U0010 | Medium Speed CAN Communication Bus | U | generic | [B] | — | — |
| U0011 | Medium Speed CAN Communication Bus Performance | U | generic | [B] | — | — |
| U0012 | Medium Speed CAN Communication Bus (+) Open | U | generic | [B] | — | — |
| U0013 | Medium Speed CAN Communication Bus (+) Low | U | generic | [B] | — | — |
| U0014 | Medium Speed CAN Communication Bus (+) High | U | generic | [B] | — | — |
| U0015 | Medium Speed CAN Communication Bus (-) Open | U | generic | [B] | — | — |
| U0016 | Medium Speed CAN Communication Bus (-) Low | U | generic | [B] | — | — |
| U0017 | Medium Speed CAN Communication Bus (-) High | U | generic | [B] | — | — |
| U0018 | Medium Speed CAN Communication Bus (-) shorted to Bus (+) | U | generic | [B] | — | — |
| U0019 | Low Speed CAN Communication Bus | U | generic | [B] | — | — |
| U0020 | Low Speed CAN Communication Bus Performance | U | generic | [B] | — | — |
| U0021 | Low Speed CAN Communication Bus (+) Open | U | generic | [B] | — | — |
| U0022 | Low Speed CAN Communication Bus (+) Low | U | generic | [B] | — | — |
| U0023 | Low Speed CAN Communication Bus (+) High | U | generic | [B] | — | — |
| U0024 | Low Speed CAN Communication Bus (-) Open | U | generic | [B] | — | — |
| U0025 | Low Speed CAN Communication Bus (-) Low | U | generic | [B] | — | — |
| U0026 | Low Speed CAN Communication Bus (-) High | U | generic | [B] | — | — |
| U0027 | Low Speed CAN Communication Bus (-) shorted to Bus (+) | U | generic | [B] | — | — |
| U0028 | Vehicle Communication Bus A | U | generic | [B] | — | — |
| U0029 | Vehicle Communication Bus A Performance | U | generic | [B] | — | — |
| U0030 | Vehicle Communication Bus A (+) Open | U | generic | [B] | — | — |
| U0031 | Vehicle Communication Bus A (+) Low | U | generic | [B] | — | — |
| U0032 | Vehicle Communication Bus A (+) High | U | generic | [B] | — | — |
| U0033 | Vehicle Communication Bus A (-) Open | U | generic | [B] | — | — |
| U0034 | Vehicle Communication Bus A (-) Low | U | generic | [B] | — | — |
| U0035 | Vehicle Communication Bus A (-) High | U | generic | [B] | — | — |
| U0036 | Vehicle Communication Bus A (-) shorted to Bus A (+) | U | generic | [B] | — | — |
| U0037 | Vehicle Communication Bus B | U | generic | [B] | — | — |
| U0038 | Vehicle Communication Bus B Performance | U | generic | [B] | — | — |
| U0039 | Vehicle Communication Bus B (+) Open | U | generic | [B] | — | — |
| U0040 | Vehicle Communication Bus B (+) Low | U | generic | [B] | — | — |
| U0041 | Vehicle Communication Bus B (+) High | U | generic | [B] | — | — |
| U0042 | Vehicle Communication Bus B (-) Open | U | generic | [B] | — | — |
| U0043 | Vehicle Communication Bus B (-) Low | U | generic | [B] | — | — |
| U0044 | Vehicle Communication Bus B (-) High | U | generic | [B] | — | — |
| U0045 | Vehicle Communication Bus B (-) shorted to Bus B (+) | U | generic | [B] | — | — |
| U0046 | Vehicle Communication Bus C | U | generic | [B] | — | — |
| U0047 | Vehicle Communication Bus C Performance | U | generic | [B] | — | — |
| U0048 | Vehicle Communication Bus C (+) Open | U | generic | [B] | — | — |
| U0049 | Vehicle Communication Bus C (+) Low | U | generic | [B] | — | — |
| U0050 | Vehicle Communication Bus C (+) High | U | generic | [B] | — | — |
| U0051 | Vehicle Communication Bus C (-) Open | U | generic | [B] | — | — |
| U0052 | Vehicle Communication Bus C (-) Low | U | generic | [B] | — | — |
| U0053 | Vehicle Communication Bus C (-) High | U | generic | [B] | — | — |
| U0054 | Vehicle Communication Bus C (-) shorted to Bus C (+) | U | generic | [B] | — | — |
| U0055 | Vehicle Communication Bus D | U | generic | [B] | — | — |
| U0056 | Vehicle Communication Bus D Performance | U | generic | [B] | — | — |
| U0057 | Vehicle Communication Bus D (+) Open | U | generic | [B] | — | — |
| U0058 | Vehicle Communication Bus D (+) Low | U | generic | [B] | — | — |
| U0059 | Vehicle Communication Bus D (+) High | U | generic | [B] | — | — |
| U0060 | Vehicle Communication Bus D (-) Open | U | generic | [B] | — | — |
| U0061 | Vehicle Communication Bus D (-) Low | U | generic | [B] | — | — |
| U0062 | Vehicle Communication Bus D (-) High | U | generic | [B] | — | — |
| U0063 | Vehicle Communication Bus D (-) shorted to Bus D (+) | U | generic | [B] | — | — |
| U0064 | Vehicle Communication Bus E | U | generic | [B] | — | — |
| U0065 | Vehicle Communication Bus E Performance | U | generic | [B] | — | — |
| U0066 | Vehicle Communication Bus E (+) Open | U | generic | [B] | — | — |
| U0067 | Vehicle Communication Bus E (+) Low | U | generic | [B] | — | — |
| U0068 | Vehicle Communication Bus E (+) High | U | generic | [B] | — | — |
| U0069 | Vehicle Communication Bus E (-) Open | U | generic | [B] | — | — |
| U0070 | Vehicle Communication Bus E (-) Low | U | generic | [B] | — | — |
| U0071 | Vehicle Communication Bus E (-) High | U | generic | [B] | — | — |
| U0072 | Vehicle Communication Bus E (-) shorted to Bus E (+) | U | generic | [B] | — | — |
| U0073 | Control Module Communication Bus Off | U | generic | [B] | intermittent short on CAN data circuits (GM: circuits 2500/2501); backed-out terminal in transmission harness connections (GM TSB 08-07-30-021) | If stored as history only, follow the service manual "Testing for Electrical Intermittents" procedure; the affected BCM may stay offline ~20 minutes until timeout. CONFLICT: scribd "Control Module U Code List" words this as "Control Module Communication Bus A Off" - the two-source wording is used here (see Coverage notes) |
| U0100 | Lost Communication With ECM/PCM "A" | U | generic | [B] | wiring faults; corroded connectors; faulty ECM/PCM | Inspect wiring harnesses and connectors for damage or corrosion; use a scan tool to identify the non-communicating module |
| U0101 | Lost Communication with TCM | U | generic | [B] | wiring faults; corroded connectors; faulty TCM | Inspect wiring harnesses and connectors; check for related U-codes pointing at the same bus segment |
| U0102 | Lost Communication with Transfer Case Control Module | U | generic | [B] | — | — |
| U0103 | Lost Communication With Gear Shift Module | U | generic | [B] | — | — |
| U0104 | Lost Communication With Cruise Control Module | U | generic | [B] | — | — |
| U0105 | Lost Communication With Fuel Injector Control Module | U | generic | [B] | — | — |
| U0106 | Lost Communication With Glow Plug Control Module | U | generic | [B] | — | — |
| U0107 | Lost Communication With Throttle Actuator Control Module | U | generic | [B] | — | — |
| U0108 | Lost Communication With Alternative Fuel Control Module | U | generic | [B] | — | — |
| U0109 | Lost Communication With Fuel Pump Control Module | U | generic | [B] | — | — |
| U0110 | Lost Communication With Drive Motor Control Module | U | generic | [B] | — | — |
| U0111 | Lost Communication With Battery Energy Control Module A | U | generic | [B] | — | — |
| U0112 | Lost Communication With Battery Energy Control Module B | U | generic | [B] | — | — |
| U0113 | Lost Communication With Emissions Critical Control Information | U | generic | [B] | — | — |
| U0114 | Lost Communication With Four-Wheel Drive Clutch Control Module | U | generic | [B] | — | — |
| U0115 | Lost Communication With ECM/PCM B | U | generic | [B] | — | — |
| U0121 | Lost Communication With Anti-Lock Brake System (ABS) Control Module | U | generic | [B] | — | — |
| U0122 | Lost Communication With Vehicle Dynamics Control Module | U | generic | [B] | — | — |
| U0123 | Lost Communication With Yaw Rate Sensor Module | U | generic | [B] | — | — |
| U0124 | Lost Communication With Lateral Acceleration Sensor Module | U | generic | [B] | — | — |
| U0125 | Lost Communication With Multi-axis Acceleration Sensor Module | U | generic | [B] | — | — |
| U0126 | Lost Communication With Steering Angle Sensor Module | U | generic | [B] | — | — |
| U0127 | Lost Communication With Tire Pressure Monitor Module | U | generic | [B] | — | — |
| U0128 | Lost Communication With Park Brake Control Module | U | generic | [B] | — | — |
| U0129 | Lost Communication With Brake System Control Module | U | generic | [B] | — | — |
| U0130 | Lost Communication With Steering Effort Control Module | U | generic | [B] | — | — |
| U0131 | Lost Communication With Power Steering Control Module | U | generic | [B] | — | — |
| U0132 | Lost Communication With Ride Level Control Module | U | generic | [B] | — | — |
| U0140 | Lost Communication With Body Control Module | U | generic | [B] | — | — |
| U0141 | Lost Communication With Body Control Module A | U | generic | [B] | — | — |
| U0142 | Lost Communication With Body Control Module B | U | generic | [B] | — | — |
| U0143 | Lost Communication With Body Control Module C | U | generic | [B] | — | — |
| U0144 | Lost Communication With Body Control Module D | U | generic | [B] | — | — |
| U0145 | Lost Communication With Body Control Module E | U | generic | [B] | — | — |
| U0146 | Lost Communication With Gateway A | U | generic | [B] | — | — |
| U0147 | Lost Communication With Gateway B | U | generic | [B] | — | — |
| U0148 | Lost Communication With Gateway C | U | generic | [B] | — | — |
| U0149 | Lost Communication With Gateway D | U | generic | [B] | — | — |
| U0150 | Lost Communication With Gateway E | U | generic | [B] | — | — |
| U0151 | Lost Communication With Restraints Control Module | U | generic | [B] | — | — |
| U0152 | Lost Communication With Side Restraints Control Module (Left) | U | generic | [B] | — | — |
| U0153 | Lost Communication With Side Restraints Control Module (Right) | U | generic | [B] | — | — |
| U0154 | Lost Communication With Restraints Occupant Sensing Control Module | U | generic | [B] | — | — |
| U0155 | Lost Communication With Instrument Panel Cluster (IPC) Control Module | U | generic | [B] | — | — |
| U0156 | Lost Communication With Information Center A | U | generic | [B] | — | — |
| U0157 | Lost Communication With Information Center B | U | generic | [B] | — | — |
| U0158 | Lost Communication With Head Up Display | U | generic | [B] | — | — |
| U0159 | Lost Communication With Parking Assist Control Module | U | generic | [B] | — | — |
| U0160 | Lost Communication With Audible Alert Control Module | U | generic | [B] | — | — |
| U0161 | Lost Communication With Compass Module | U | generic | [B] | — | — |
| U0162 | Lost Communication With Navigation Display Module | U | generic | [B] | — | — |
| U0163 | Lost Communication With Navigation Control Module | U | generic | [B] | — | — |
| U0164 | Lost Communication With HVAC Control Module | U | generic | [B] | — | — |
| U0165 | Lost Communication With HVAC Control Module (Rear) | U | generic | [B] | — | — |
| U0166 | Lost Communication With Auxiliary Heater Control Module | U | generic | [B] | — | — |
| U0167 | Lost Communication With Vehicle Immobilizer Control Module | U | generic | [B] | — | — |
| U0168 | Lost Communication With Vehicle Security Control Module | U | generic | [B] | — | — |
| U0169 | Lost Communication With Sunroof Control Module | U | generic | [B] | — | — |
| U0170 | Lost Communication With "Restraints System Sensor A" | U | generic | [B] | — | — |
| U0171 | Lost Communication With "Restraints System Sensor B" | U | generic | [B] | — | — |
| U0172 | Lost Communication With "Restraints System Sensor C" | U | generic | [B] | — | — |
| U0173 | Lost Communication With "Restraints System Sensor D" | U | generic | [B] | — | — |
| U0174 | Lost Communication With "Restraints System Sensor E" | U | generic | [B] | — | — |
| U0175 | Lost Communication With "Restraints System Sensor F" | U | generic | [B] | — | — |
| U0176 | Lost Communication With "Restraints System Sensor G" | U | generic | [B] | — | — |
| U0177 | Lost Communication With "Restraints System Sensor H" | U | generic | [B] | — | — |
| U0178 | Lost Communication With "Restraints System Sensor I" | U | generic | [B] | — | — |
| U0179 | Lost Communication With "Restraints System Sensor J" | U | generic | [B] | — | — |
| U0180 | Lost Communication With Automatic Lighting Control Module | U | generic | [B] | — | — |
| U0181 | Lost Communication With Headlamp Leveling Control Module | U | generic | [B] | — | — |
| U0182 | Lost Communication With Lighting Control Module (Front) | U | generic | [B] | — | — |
| U0183 | Lost Communication With Lighting Control Module (Rear) | U | generic | [B] | — | — |
| U0184 | Lost Communication With Radio | U | generic | [B] | — | — |
| U0185 | Lost Communication With Antenna Control Module | U | generic | [B] | — | — |
| U0186 | Lost Communication With Audio Amplifier | U | generic | [B] | — | — |
| U0187 | Lost Communication With Digital Disc Player/Changer Module A | U | generic | [B] | — | — |
| U0188 | Lost Communication With Digital Disc Player/Changer Module B | U | generic | [B] | — | — |
| U0189 | Lost Communication With Digital Disc Player/Changer Module C | U | generic | [B] | — | — |
| U0190 | Lost Communication With Digital Disc Player/Changer Module D | U | generic | [B] | — | — |
| U0191 | Lost Communication With Television | U | generic | [B] | — | — |
| U0192 | Lost Communication With Personal Computer | U | generic | [B] | — | — |
| U0193 | Lost Communication With "Digital Audio Control Module A" | U | generic | [B] | — | — |
| U0194 | Lost Communication With "Digital Audio Control Module B" | U | generic | [B] | — | — |
| U0195 | Lost Communication With Subscription Entertainment Receiver Module | U | generic | [B] | — | — |
| U0196 | Lost Communication With Rear Seat Entertainment Control Module | U | generic | [B] | — | — |
| U0197 | Lost Communication With Telephone Control Module | U | generic | [B] | — | — |
| U0198 | Lost Communication With Telematic Control Module | U | generic | [B] | — | — |
| U0199 | Lost Communication With "Door Control Module A" | U | generic | [B] | — | — |
| U0200 | Lost Communication With "Door Control Module B" | U | generic | [B] | — | — |
| U0201 | Lost Communication With "Door Control Module C" | U | generic | [B] | — | — |
| U0202 | Lost Communication With "Door Control Module D" | U | generic | [B] | — | — |
| U0203 | Lost Communication With "Door Control Module E" | U | generic | [B] | — | — |
| U0204 | Lost Communication With "Door Control Module F" | U | generic | [B] | — | — |
| U0205 | Lost Communication With "Door Control Module G" | U | generic | [B] | — | — |
| U0206 | Lost Communication With Folding Top Control Module | U | generic | [B] | — | — |
| U0207 | Lost Communication With Movable Roof Control Module | U | generic | [B] | — | — |
| U0208 | Lost Communication With "Seat Control Module A" | U | generic | [B] | — | — |
| U0209 | Lost Communication With "Seat Control Module B" | U | generic | [B] | — | — |
| U0210 | Lost Communication With "Seat Control Module C" | U | generic | [B] | — | — |
| U0211 | Lost Communication With "Seat Control Module D" | U | generic | [B] | — | — |
| U0212 | Lost Communication With Steering Column Control Module | U | generic | [B] | — | — |
| U0213 | Lost Communication With Mirror Control Module | U | generic | [B] | — | — |
| U0214 | Lost Communication With Remote Function Actuation | U | generic | [B] | — | — |
| U0215 | Lost Communication With "Door Switch A" | U | generic | [B] | — | — |
| U0216 | Lost Communication With "Door Switch B" | U | generic | [B] | — | — |
| U0217 | Lost Communication With "Door Switch C" | U | generic | [B] | — | — |
| U0218 | Lost Communication With "Door Switch D" | U | generic | [B] | — | — |
| U0219 | Lost Communication With "Door Switch E" | U | generic | [B] | — | — |
| U0220 | Lost Communication With "Door Switch F" | U | generic | [B] | — | — |
| U0221 | Lost Communication With "Door Switch G" | U | generic | [B] | — | — |
| U0222 | Lost Communication With "Door Window Motor A" | U | generic | [B] | — | — |
| U0223 | Lost Communication With "Door Window Motor B" | U | generic | [B] | — | — |
| U0224 | Lost Communication With "Door Window Motor C" | U | generic | [B] | — | — |
| U0225 | Lost Communication With "Door Window Motor D" | U | generic | [B] | — | — |
| U0226 | Lost Communication With "Door Window Motor E" | U | generic | [B] | — | — |
| U0227 | Lost Communication With "Door Window Motor F" | U | generic | [B] | — | — |
| U0228 | Lost Communication With "Door Window Motor G" | U | generic | [B] | — | — |
| U0229 | Lost Communication With Heated Steering Wheel Module | U | generic | [B] | — | — |
| U0230 | Lost Communication With Rear Gate Module | U | generic | [B] | — | — |
| U0231 | Lost Communication With Rain Sensing Module | U | generic | [B] | — | — |
| U0232 | Lost Communication With Side Obstacle Detection Control Module (Left) | U | generic | [B] | — | — |
| U0233 | Lost Communication With Side Obstacle Detection Control Module (Right) | U | generic | [B] | — | — |
| U0234 | Lost Communication With Convenience Recall Module | U | generic | [B] | — | — |
| U0235 | Lost Communication With Cruise Control Front Distance Range Sensor | U | generic | [B] | — | — |
| U0300 | Internal Control Module Software Incompatibility | U | generic | [B] | — | — |
| U0301 | Software Incompatibility with ECM/PCM | U | generic | [B] | — | — |
| U0302 | Software Incompatibility with Transmission Control Module | U | generic | [B] | — | — |
| U0303 | Software Incompatibility with Transfer Case Control Module | U | generic | [B] | — | — |
| U0304 | Software Incompatibility with Gear Shift Control Module | U | generic | [B] | — | — |
| U0305 | Software Incompatibility with Cruise Control Module | U | generic | [B] | — | — |
| U0306 | Software Incompatibility with Fuel Injector Control Module | U | generic | [B] | — | — |
| U0307 | Software Incompatibility with Glow Plug Control Module | U | generic | [B] | — | — |
| U0308 | Software Incompatibility with Throttle Actuator Control Module | U | generic | [B] | — | — |
| U0309 | Software Incompatibility with Alternative Fuel Control Module | U | generic | [B] | — | — |
| U0310 | Software Incompatibility with Fuel Pump Control Module | U | generic | [B] | — | — |
| U0311 | Software Incompatibility with Drive Motor Control Module | U | generic | [B] | — | — |
| U0312 | Software Incompatibility with Battery Energy Control Module A | U | generic | [B] | — | — |
| U0313 | Software Incompatibility with Battery Energy Control Module B | U | generic | [B] | — | — |
| U0314 | Software Incompatibility with Four-Wheel Drive Clutch Control Module | U | generic | [B] | — | — |
| U0315 | Software Incompatibility with Anti-Lock Brake System Control Module | U | generic | [B] | — | — |
| U0316 | Software Incompatibility with Vehicle Dynamics Control Module | U | generic | [B] | — | — |
| U0317 | Software Incompatibility with Park Brake Control Module | U | generic | [B] | — | — |
| U0318 | Software Incompatibility with Brake System Control Module | U | generic | [B] | — | — |
| U0319 | Software Incompatibility with Steering Effort Control Module | U | generic | [B] | — | — |
| U0320 | Software Incompatibility with Power Steering Control Module | U | generic | [B] | — | — |
| U0321 | Software Incompatibility with Ride Level Control Module | U | generic | [B] | — | — |
| U0322 | Software Incompatibility with Body Control Module | U | generic | [B] | — | — |
| U0323 | Software Incompatibility with Instrument Panel Control Module | U | generic | [B] | — | — |
| U0324 | Software Incompatibility with HVAC Control Module | U | generic | [B] | — | — |
| U0325 | Software Incompatibility with Auxiliary Heater Control Module | U | generic | [B] | — | — |
| U0326 | Software Incompatibility with Vehicle Immobilizer Control Module | U | generic | [B] | — | — |
| U0327 | Software Incompatibility with Vehicle Security Control Module | U | generic | [B] | — | — |
| U0328 | Software Incompatibility with Steering Angle Sensor Module | U | generic | [B] | — | — |
| U0329 | Software Incompatibility with Steering Column Control Module | U | generic | [B] | — | — |
| U0330 | Software Incompatibility with Tire Pressure Monitor Module | U | generic | [B] | — | — |
| U0331 | Software Incompatibility with Body Control Module A | U | generic | [B] | — | — |
| U0400 | Invalid Data Received | U | generic | [B] | — | — |
| U0401 | Invalid Data Received From ECM/PCM | U | generic | [B] | — | — |
| U0402 | Invalid Data Received From Transmission Control Module | U | generic | [B] | — | — |
| U0403 | Invalid Data Received From Transfer Case Control Module | U | generic | [B] | — | — |
| U0404 | Invalid Data Received From Gear Shift Control Module | U | generic | [B] | — | — |
| U0405 | Invalid Data Received From Cruise Control Module | U | generic | [B] | — | — |
| U0406 | Invalid Data Received From Fuel Injector Control Module | U | generic | [B] | — | — |
| U0407 | Invalid Data Received From Glow Plug Control Module | U | generic | [B] | — | — |
| U0408 | Invalid Data Received From Throttle Actuator Control Module | U | generic | [B] | — | — |
| U0409 | Invalid Data Received From Alternative Fuel Control Module | U | generic | [B] | — | — |
| U0410 | Invalid Data Received From Fuel Pump Control Module | U | generic | [B] | — | — |
| U0411 | Invalid Data Received From Drive Motor Control Module | U | generic | [B] | — | — |
| U0412 | Invalid Data Received From Battery Energy Control Module A | U | generic | [B] | — | — |
| U0413 | Invalid Data Received From Battery Energy Control Module B | U | generic | [B] | — | — |
| U0414 | Invalid Data Received From Four-Wheel Drive Clutch Control Module | U | generic | [B] | — | — |
| U0415 | Invalid Data Received From Anti-Lock Brake System Control Module | U | generic | [B] | — | — |
| U0416 | Invalid Data Received From Vehicle Dynamics Control Module | U | generic | [B] | — | — |
| U0417 | Invalid Data Received From Park Brake Control Module | U | generic | [B] | — | — |
| U0418 | Invalid Data Received From Brake System Control Module | U | generic | [B] | — | — |
| U0419 | Invalid Data Received From Steering Effort Control Module | U | generic | [B] | — | — |
| U0420 | Invalid Data Received From Power Steering Control Module | U | generic | [B] | — | — |
| U0421 | Invalid Data Received From Ride Level Control Module | U | generic | [B] | — | — |
| U0422 | Invalid Data Received From Body Control Module | U | generic | [B] | — | — |
| U0423 | Invalid Data Received From Instrument Panel Control Module | U | generic | [B] | — | — |
| U0424 | Invalid Data Received From HVAC Control Module | U | generic | [B] | — | — |
| U0425 | Invalid Data Received From Auxiliary Heater Control Module | U | generic | [B] | — | — |
| U0426 | Invalid Data Received From Vehicle Immobilizer Control Module | U | generic | [B] | — | — |
| U0427 | Invalid Data Received From Vehicle Security Control Module | U | generic | [B] | — | — |
| U0428 | Invalid Data Received From Steering Angle Sensor Module | U | generic | [B] | — | — |
| U0429 | Invalid Data Received From Steering Column Control Module | U | generic | [B] | — | — |
| U0430 | Invalid Data Received From Tire Pressure Monitor Module | U | generic | [B] | — | — |
| U0431 | Invalid Data Received From Body Control Module A | U | generic | [B] | — | — |

## gm — 107 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1001 | Option Configuration Error | B | manufacturer | [B] | SDM or BCM replaced without VIN programming; VIN mismatch between SDM (inflatable restraint sensing and diagnostic module) and BCM | The SDM stores the restraint ID from the VIN plus the last 4 digits of the SDM part number; at key-on it compares against the BCM over GMLAN. Mismatch sets B1001 and lights the airbag lamp; the code returns every power cycle until fixed. Fix: with a capable scan tool, run "Setup New BCM" / program the VIN into the SDM so both modules agree. Some vehicles require dealer programming. |
| B1325 | Device Power / module communication fault (seen as radio-module communication fault on 2015 Silverado/Sierra) | B | manufacturer | [C] | Radio module wiring harness damage or loose pins; faulty radio module; BCM communication fault; low system voltage | Technician reports on 2015 Silverado/Sierra pair B1325 with U0164 (lost communication with HVAC/radio network). Inspect radio harness connectors for corrosion; check BCM for related faults; battery-disconnect reset; reprogram or replace the module if wiring is sound. Descriptor varies by module — verify per model SI. |
| C0161 | Antilock Brake System (ABS)/Traction Control System (TCS) Brake Switch Circuit | C | manufacturer | [B] | — | EBCM code. Verify brake switch input to the EBCM before replacing the module. |
| C0240 | Powertrain Control Module (PCM) Traction Control Not Allowed | C | manufacturer | [B] | — | Informational — the PCM is refusing torque reduction; diagnose the PCM-side DTCs first. |
| C0242 | Powertrain Control Module (PCM) Indicated TCS Malfunction | C | manufacturer | [B] | not documented (fault is in the ECM/PCM, not the EBCM) | GM SI circuit description: "When certain PCM DTCs are set, the PCM will not be able to perform the torque reduction for traction control. A serial data message is sent to the EBCM indicating that traction control is not allowed." The EBCM then deactivates traction control. This is an INFORMATION code — the fault is in the ECM; diagnose ECM DTCs, not the EBCM. |
| C0252 | Vehicle Stability Enhancement System (VSES) Sensors Uncorrelated | C | manufacturer | [B] | — | — |
| C0267 | Low Brake Fluid Indicated | C | manufacturer | [B] | — | Check brake fluid level and the fluid-level sensor circuit first — this is a level indication, not necessarily an EBCM fault. |
| C0281 | Dynamic Rear Proportioning (DRP) Performance | C | manufacturer | [B] | — | — |
| C0550 | Electronic Control Unit (ECU) Performance | C | manufacturer | [B] | — | Internal EBCM performance fault — typically requires EBCM replacement/programming after ruling out power/ground. |
| C0551 | Option Configuration Error | C | manufacturer | [B] | — | EBCM-side analog of B1001 — module configuration/VIN mismatch; programming required. |
| C0561 | System Disabled Information Stored | C | manufacturer | [B] | — | Informational — another module has disabled the system; read the disabling module's codes. |
| C0569 | System Configuration Error | C | manufacturer | [B] | — | — |
| C1100 | Base Brake System Pressure Sensor 2 | C | manufacturer | [B] | — | — |
| P1101 | Intake Air Flow System Performance | P | manufacturer | [A] | Vacuum/air leaks in intake tract; clogged PCV system or valve; dirty or faulty MAF sensor; restricted air filter; faulty/leaking charge-air (intercooler) tubes on turbo engines; faulty boost pressure or MAP sensor | GM SI (Document ID 3355356, 2018 Malibu 2.0L Turbo): "The ECM compares the actual air flow based on throttle position (TP) to a calculated airflow based on MAP sensor and MAF." Sets when actual airflow exceeds calculated. Review PIP5402D / 20-NA-047 for leak checks; verify boost and MAP sensors agree KOEO; MAF should read approx 3 g/s (2000-2500 Hz) at idle. Common on 1.4L LE2 / 1.5L LFV turbo engines. |
| P1174 | Fuel Trim Cylinder Balance Bank 1 | P | manufacturer | [B] | Clogged fuel injectors (Multec 2 injectors, 2000-2008 models); vacuum leaks; aged O2 sensors; MAF issues | GM TSB 04-06-04-047G (US) / 05-06-04-022D (Canada): "Various Driveability Symptoms Due to Clogged Fuel Injectors" — MIL with P1174/P1175 (+ P0171/P0172/P0174/P0300) on 2000-2008 GM cars/light trucks. GM recommends testing with Active Fuel Injector Tester AFIT CH-47976. CONFLICT: an EOBD overview document lists P1174 as "Injection pump cam ring position sensor" — that reading belongs to the diesel (Duramax/Isuzu) context, not gasoline GM. Report both; use the TSB meaning on gasoline vehicles. |
| P1175 | Fuel Trim Cylinder Balance Bank 2 | P | manufacturer | [B] | Same as P1174 (clogged injectors, vacuum leaks, O2/MAF issues), bank 2 | Covered by the same GM TSB 04-06-04-047G as P1174. Diagnose both banks together; a both-banks fault points to something common (intake leak, MAF, fuel pressure). |
| P1258 | Engine Coolant Overtemperature - Protection Mode Active | P | manufacturer | [A] | Cooling system fault (thermostat, water pump, low coolant, cooling fans, restricted radiator); faulty ECT sensor (rule out P0116/P0117/P0118/P0128 first) | GM SI: Type A DTC. ECM monitors ECT; sets when coolant exceeds ~131-136 C for several seconds (threshold varies by model/calibration, e.g. 131 C for 7 s on Enclave LZ4/LY7, 136 C for 1 s or 10 s cumulative on CTS). Action: ECM alternately disables groups of cylinders (fuel injectors OFF) to cool the engine — "Overheated Engine Protection Operating Mode"; coolant lamp + DIC message. Diagnose the cooling system, not the code. |
| P1516 | Throttle Actuator Control (TAC) Module Throttle Actuator Position Performance | P | manufacturer | [A] | Carbon buildup on throttle plate/bore; faulty TAC module or throttle body; TAC motor wiring open/shorted; poor connector contact; high resistance in TP sensor circuits; ECM fault | GM-ONLY code (same number means different things on other makes). GM SI: sets when actual vs desired throttle position differs by more than 7.5% for 30 s (values vary by model). Type A DTC; ECM commands Reduced Engine Power mode and sets P2106/P2110. Clearing the code restores power only if it is the sole fault. Check throttle body for carbon/ice holding the blade open before replacing parts. |
| P1629 | Anti-theft cranking signal error / Passkey cranking error | P | manufacturer | [B] | — | — |
| P1630 | System voltage too high/too low, or ECM immobilizer learning mode (Cavalier and Monte Carlo only) | P | manufacturer | [B] | — | Immobilizer-learning usage is model-specific (Cavalier/Monte Carlo). |
| P1631 | Anti-theft password incorrect (also listed as: Oxygen sensor #1 slow response on some models) | P | manufacturer | [C] | — | CONFLICT between the two transcribed lists on this code (theft-deterrent vs O2 sensor) — reported, not resolved; verify per model. |
| P1632 | Anti-theft fuel disable signal received | P | manufacturer | [B] | — | — |
| P1633 | Ignition power circuit low voltage | P | manufacturer | [B] | — | — |
| P1634 | Ignition power circuit low voltage | P | manufacturer | [B] | — | — |
| P1635 | 5 volt reference voltage to sensors low | P | manufacturer | [B] | — | — |
| P1637 | Generator L-Terminal Circuit | P | manufacturer | [A] | Loose or corroded connections at alternator or PCM; faulty voltage regulator; open/grounded L-terminal wire (generator will not operate if L wire is open or grounded); PCM fault | GM SI (1999 Corvette): the L (lamp) terminal enables generator operation after engine start and reports internal faults (regulator grounds L on internal fault). Scan tool: L terminal should read Inactive KOEO and Active with engine running. DTCs P1637 and P1638 may set together; the L-terminal circuit can cause P1638 to set. One diagnostic table covers both. |
| P1638 | Generator F-Terminal Circuit | P | manufacturer | [A] | Faulty voltage regulator; open/shorted field winding; wiring fault on F-terminal circuit; wrong/clone alternator (field duty cycle out of range); PCM fault | GM SI: PCM monitors generator field duty cycle (PWM) on the F terminal — expects ~0% KOEO and 5-100% with engine running. Out-of-range PWM sets the code; PCM then sends a Class 2 message to illuminate "Charge System Fault" and may turn the alternator off. Scan tool: F terminal should read 10-40% KOEO, >5% running. |
| P1639 | PCM 5 volt reference voltage low | P | manufacturer | [B] | — | — |
| P1641 | EVAP fuel tank pressure sensor circuit voltage high, or fan 1 relay control circuit, or MIL light circuit, or A/C compressor clutch relay circuit | P | manufacturer | [B] | — | Multi-use output-driver code; the meaning depends on model/year — verify per model SI. |
| P1642 | Fan control relay, or vehicle speed sensor output, or secondary air injection relay fault | P | manufacturer | [B] | — | Multi-use output-driver code; verify per model SI. |
| P1644 | Throttle position sensor circuit, or traction control fault | P | manufacturer | [B] | — | — |
| P1645 | Boost control solenoid circuit, or EVAP solenoid output circuit | P | manufacturer | [B] | — | — |
| P1650 | Quad driver module (QDM) 1 circuit | P | manufacturer | [B] | — | — |
| P1651 | Quad driver module (QDM) 2 circuit | P | manufacturer | [B] | — | — |
| P1652 | Quad driver module (QDM) 3 circuit | P | manufacturer | [B] | — | — |
| P1653 | Quad driver module (QDM) 4 circuit | P | manufacturer | [B] | — | — |
| P1654 | Quad driver module (QDM) 5 circuit | P | manufacturer | [B] | — | — |
| P1655 | Quad driver module (QDM) 6 circuit | P | manufacturer | [B] | — | — |
| P1656 | Driver 4 line 1 | P | manufacturer | [B] | — | — |
| P1657 | Driver 4 line 2 | P | manufacturer | [B] | — | — |
| P1658 | Driver 4 line 3 | P | manufacturer | [B] | — | — |
| P1660 | Driver 4 line 4 | P | manufacturer | [B] | — | — |
| P1661 | Driver 4 line 5 | P | manufacturer | [B] | — | — |
| P1662 | Driver 4 line 6 | P | manufacturer | [B] | — | — |
| P1663 | Driver 4 line 7 | P | manufacturer | [B] | — | — |
| P1664 | Skip shift 1-4 upshift lamp control circuit (also: oil lamp control circuit on Caprice/Fleetwood/Roadmaster) | P | manufacturer | [B] | — | — |
| P1665 | Driver 3 line 6 (also listed as: EVAP vent valve solenoid control circuit, 1998) | P | manufacturer | [B] | — | Year-dependent meaning — verify per model. |
| P1666 | Driver 3 line 6 | P | manufacturer | [C] | — | — |
| P1667 | Reverse inhibitor solenoid control circuit (1996-97) / fuel pump speed control circuit (1998) | P | manufacturer | [B] | — | Year-dependent meaning — verify per model. |
| P1669 | ABS unit expected | P | manufacturer | [C] | — | — |
| P1670 | Quad driver module (QDM) 4 circuit | P | manufacturer | [B] | — | — |
| P1671 | MIL control circuit / oil change lamp control circuit | P | manufacturer | [B] | — | — |
| P1672 | Low engine oil level lamp circuit | P | manufacturer | [B] | — | — |
| P1673 | Engine hot lamp control circuit | P | manufacturer | [B] | — | — |
| P1674 | Tachometer control circuit | P | manufacturer | [B] | — | — |
| P1675 | EVAP vent solenoid control circuit | P | manufacturer | [B] | — | — |
| P1676 | EVAP canister purge solenoid control circuit | P | manufacturer | [B] | — | — |
| P1677 | Powertrain control module fault (quad driver 4) | P | manufacturer | [B] | — | — |
| P1680 | Driver 5 (powertrain control module fault) | P | manufacturer | [B] | — | — |
| P1681 | Driver 5 line 1 | P | manufacturer | [B] | — | — |
| P1682 | Ignition 1 Switch Circuit 2 | P | manufacturer | [B] | Bad relay or blown fuse (ECM/IGN circuits); faulty ignition switch; open/short in ignition-1 wiring; faulty underhood fuse block; ECM fault | GM SI circuit description: two ignition-1 voltage circuits feed the ECM (one via powertrain relay for TAC circuits, one via run/crank relay or ignition switch for remaining circuits). Code sets on a voltage difference between the two circuits (>~3 V reported on some models). Test B+ at both ECM ignition feeds (e.g. C1-19 on some models); swap relays and check fuses before condemning the ECM. Model-year variation exists in which relays feed the two circuits — verify against the model SI. |
| P1683 | Driver 5 line 3 | P | manufacturer | [B] | — | — |
| P1684 | Driver 5 line 4 | P | manufacturer | [B] | — | — |
| P1685 | Driver 5 line 5 | P | manufacturer | [B] | — | — |
| P1686 | Driver 5 line 6 | P | manufacturer | [B] | — | — |
| P1687 | Driver 5 line 7 | P | manufacturer | [B] | — | — |
| P1689 | Traction control system delivered torque control circuit | P | manufacturer | [B] | — | Related to C0244 (PWM delivered torque) on the EBCM side. |
| P1690 | ECM loop overrun | P | manufacturer | [B] | — | — |
| P1691 | Coolant gauge circuit low voltage | P | manufacturer | [B] | — | — |
| P1692 | Coolant gauge circuit high voltage | P | manufacturer | [B] | — | — |
| P1693 | Tachometer circuit low voltage | P | manufacturer | [B] | — | — |
| P1694 | Tachometer circuit high voltage | P | manufacturer | [B] | — | — |
| P1695 | Remote keyless entry circuit low | P | manufacturer | [B] | — | — |
| P1696 | Remote keyless entry circuit high | P | manufacturer | [B] | — | — |
| P1700 | Malfunction indicator lamp requested by transmission control module | P | manufacturer | [B] | not documented (informational — check TCM for underlying codes) | Informational; scan the TCM for the underlying fault. |
| P1701 | Malfunction indicator lamp request circuit | P | manufacturer | [B] | — | — |
| P1740 | Torque control/management request circuit | P | manufacturer | [B] | — | — |
| P1743 | TP signal from ECM | P | manufacturer | [B] | — | — |
| P1760 | Transmission control module supply voltage interrupted | P | manufacturer | [B] | — | — |
| P1779 | Engine torque delivered to TCM signal | P | manufacturer | [C] | — | — |
| P1780 | Park/neutral position switch circuit | P | manufacturer | [B] | — | — |
| P1781 | Engine torque signal circuit | P | manufacturer | [B] | — | — |
| P1790 | Transmission control module checksum | P | manufacturer | [B] | — | Internal TCM fault indicator — typically requires TCM replacement/reprogramming. |
| P1791 | Transmission control module loop | P | manufacturer | [C] | — | — |
| P1792 | ECM to transmission control module engine coolant signal | P | manufacturer | [B] | — | — |
| P1793 | Transmission control module stack overrun | P | manufacturer | [C] | — | Internal TCM fault indicator. |
| P1795 | CAN bus - throttle body position | P | manufacturer | [C] | — | — |
| P1800 | ECM to transmission control module engine coolant signal | P | manufacturer | [B] | — | — |
| P1801 | Performance selector switch failure | P | manufacturer | [C] | — | — |
| P1804 | Ground control relay | P | manufacturer | [C] | — | — |
| P1810 | ATF pressure manual valve position switch malfunction | P | manufacturer | [B] | — | Per GM SI diagnostic aids for P1870, a TFP manual valve position switch malfunction can set P1870 — diagnose P1810 first when both appear. |
| P1811 | Maximum Adapt and Long Shift | P | manufacturer | [A] | Pressure control solenoid failure; debris/wear in valve body (torque signal regulator valve or actuator feed limit valve sticking); worn/sticking line boost valve and sleeve; PCM/TCM calibration | Classic 4T65E code. GM SI: shift taking longer than 0.65 s with adapt at its limit increments a counter; counter = 2 in one trip sets the code (Type C — MIL does NOT light; harsh shifts are the symptom). When set, PCM commands maximum line pressure and disables adapts — the bang-shifting is the protection strategy, not the root fault. GM TSB 08-07-30-013 (2007 Terraza/Uplander/Montana SV6/Relay): FALSE P1811 — reprogram TCM with updated calibration (PN 24247599), do NOT replace TCM/valve body/solenoids for that concern. Watch TAP (Transaxle Adaptive Pressure) cells on a scan tool to find the slipping element. |
| P1812 | TOT (transmission oil temperature) condition | P | manufacturer | [C] | — | — |
| P1814 | Torque converter clutch (TCC) overstress | P | manufacturer | [C] | — | — |
| P1860 | TCC PWM Solenoid Circuit Electrical | P | manufacturer | [A] | Open or short in TCC PWM solenoid circuit; faulty TCC PWM solenoid valve; wiring harness fault; PCM fault | GM SI: PCM provides a ground path (circuit 418) for the TCC PWM solenoid that smooths TCC apply. Sets on continuous open/short detected via voltage feedback vs commanded duty cycle (command ON/voltage stays B+, or command OFF/voltage stays 0 V). Type varies by model/year (A, B, C, or D). Diagnostic cascade: P1860 can cause P1870 to set — always diagnose the electrical code first. |
| P1870 | Transmission Component Slipping | P | manufacturer | [A] | Worn TCC clutch; faulty TCC PWM solenoid (see P1860); sticking shift valves or contamination; TFP manual valve position switch malfunction (P1810); internal transmission failure; low/dirty fluid | GM SI: PCM computes TCC slip from engine speed vs transmission output speed; sets when slip is excessive (e.g. 200-1500 RPM for 8 s, 3 occurrences, on 1997 4T60-E; 90-500 RPM for 10 s on later trucks). Type B (MIL after 2 trips). Actions: inhibits TCC, commands max line pressure, inhibits 4th in hot mode, freezes adapts. Diagnostic aids: a TFP switch fault or shift-solenoid mechanical fault can set P1870; diagnose engine DTCs and electrical trans codes first. |
| P1E00 | Hybrid/EV Powertrain Control Module Requested MIL Illumination (informational) | P | manufacturer | [C] | not documented (code is informational — the root fault is whatever is stored in the hybrid control module) | Seen on Chevrolet Volt / Malibu Eco alongside hybrid codes (e.g. P0AFA, P1AF0/P1AF2). Volt community reports these secured high-voltage DTCs cannot be cleared with a generic OBD-II reader; they require a dealer-level tool (GDS2) and in some cases HPCM2 reprogramming (SPS2). Always scan the hybrid/EV powertrain control module for the underlying codes rather than diagnosing P1E00 itself. |
| P2176 | Throttle Actuator Control System - Minimum Throttle Position Not Learned | P | manufacturer | [B] | Faulty TAC module/throttle body; TAC harness open/shorted or poor connection; throttle plate sticking from carbon buildup; ECM fault | GM SI: sets when both TP sensors read above 0.95 V during the minimum-learn procedure (learn runs once per ignition cycle). Type A; commands Reduced Engine Power and sets P2106/P2110. Diagnostic aid: high resistance in TP circuits, or the blade held open (ice in bore). After throttle body service, perform the idle/minimum-position learn procedure. |
| U0073 | Control Module Communication Bus A Off | U | manufacturer | [A] | Backed-out terminals in the transmission 16-way electrical connector (GM-documented pattern failure); short between HS GMLAN (+) and (-); any HS GMLAN circuit shorted to ground or voltage; module internal fault shorting the bus; open in HS GMLAN circuits | GM bulletin (Cadillac XLR 2007 / Silverado 2008-2009, doc 2186567): intermittent no-crank, IPC gauge fluctuation, door-lock cycling, transmission no-shift with U0073/U0100/U0101/U0102/U0121/U0140 — cause was a terminal for the High Speed GMLAN serial data bus backed out of the transmission connector. "Do NOT replace BCM, ECM, EBCM, TCM, TCCM or wiring harness before checking terminals in transmission connector." HS GMLAN uses two 120-ohm terminators in parallel (BCM + ECM); 60 ohms across the bus is normal, ~120 ohms indicates an open. |
| U0100 | Lost Communication With ECM/PCM | U | manufacturer | [A] | Same GMLAN bus faults as U0073; blown fuse / dead OBD-II port power; bad ground; faulty ECM | Appears in the GM TSB set above (transmission-connector terminal pattern failure). Generic scanners often surface U0100 when the real fault is bus-wide — check the full U-code set before condemning the ECM. |
| U0101 | Lost Communication With TCM | U | manufacturer | [A] | TCM not powering up (blown fuse, bad relay, wiring); GMLAN bus fault; faulty TCM | In the GM TSB set above. Diesel/truck community note: U2106-family symptoms (no PRNDL underline, harsh 3rd-gear limp) point to the TCM not powering up rather than a dead TCM. |
| U0102 | Lost Communication With Transfer Case Control Module | U | manufacturer | [A] | GMLAN bus fault; transfer case control module power/ground fault | In the GM TSB set above. |
| U0121 | Lost Communication With Anti-Lock Brake System (ABS) Control Module | U | manufacturer | [A] | GMLAN bus fault; EBCM power/ground fault | In the GM TSB set above. |
| U0140 | Lost Communication With Body Control Module | U | manufacturer | [A] | GMLAN bus fault; BCM power/ground fault | In the GM TSB set above. |
| U2100 | CAN-BUS Communication (bus-off condition) | U | manufacturer | [B] | Total or partial loss of high-speed GMLAN serial data (shorts, opens, module internal fault) | GM SI: "When a module detects a bus-off condition a DTC U0001 or U2100 will be set. These DTCs can be retrieved as history only." Engine will not start with a total HS GMLAN failure while not running. HS GMLAN modules: BCM, OnStar (communication interface module), EBCM, ESC, ECM, TCM. |
| U2105 | Lost Communication With Transmission Control Module (Silverado 2003 context) | U | manufacturer | [C] | TCM wiring/connector damage or corrosion; low system voltage | Single technician source (2003 Silverado 2500HD). Check TCM-PCM harness and battery/charging system; clear and retest. |
| U2106 | Lost Communication With Engine Control Module | U | manufacturer | [C] | ECM connectors/wiring corrosion or damage; blown fuses/relays; faulty ECM | Diesel-forum and technician reports (2004 6.6L): inspect ECM connectors and fuses; battery-disconnect reset may clear. Often accompanies TCM power issues — verify TCM is powering up (PRNDL display, shift behavior) before condemning the ECM. |

## honda — 465 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| ABS-11 | Wheel sensor — open, short to body ground, or short to power (11 = right-front, 13 = left-front, 15 = right-rear, 17 = left-rear) | C | manufacturer | [A] | faulty wheel sensor; wiring open/short | ABS indicator stays on until ignition off for these codes. Corroborated by CR-V owner thread: 15 = right rear wheel sensor, 17 = left rear wheel sensor, 54 = fail-safe relay. |
| ABS-12 | Wheel sensor — electrical noise / intermittent interruption (12 = right-front, 14 = left-front, 16 = right-rear, 18 = left-rear) | C | manufacturer | [A] | faulty wheel sensor pulse signal; damaged pulser ring; electrical noise | corroborated by s2ki S2000 thread: 12 = faulty right front wheel sensor pulse signal, 14 = left front, 16 = right rear, 18 = left rear |
| ABS-13 | Wheel sensor — open, short to body ground, or short to power (11 = right-front, 13 = left-front, 15 = right-rear, 17 = left-rear) | C | manufacturer | [A] | faulty wheel sensor; wiring open/short | ABS indicator stays on until ignition off for these codes. Corroborated by CR-V owner thread: 15 = right rear wheel sensor, 17 = left rear wheel sensor, 54 = fail-safe relay. |
| ABS-14 | Wheel sensor — electrical noise / intermittent interruption (12 = right-front, 14 = left-front, 16 = right-rear, 18 = left-rear) | C | manufacturer | [A] | faulty wheel sensor pulse signal; damaged pulser ring; electrical noise | corroborated by s2ki S2000 thread: 12 = faulty right front wheel sensor pulse signal, 14 = left front, 16 = right rear, 18 = left rear |
| ABS-15 | Wheel sensor — open, short to body ground, or short to power (11 = right-front, 13 = left-front, 15 = right-rear, 17 = left-rear) | C | manufacturer | [A] | faulty wheel sensor; wiring open/short | ABS indicator stays on until ignition off for these codes. Corroborated by CR-V owner thread: 15 = right rear wheel sensor, 17 = left rear wheel sensor, 54 = fail-safe relay. |
| ABS-16 | Wheel sensor — electrical noise / intermittent interruption (12 = right-front, 14 = left-front, 16 = right-rear, 18 = left-rear) | C | manufacturer | [A] | faulty wheel sensor pulse signal; damaged pulser ring; electrical noise | corroborated by s2ki S2000 thread: 12 = faulty right front wheel sensor pulse signal, 14 = left front, 16 = right rear, 18 = left rear |
| ABS-17 | Wheel sensor — open, short to body ground, or short to power (11 = right-front, 13 = left-front, 15 = right-rear, 17 = left-rear) | C | manufacturer | [A] | faulty wheel sensor; wiring open/short | ABS indicator stays on until ignition off for these codes. Corroborated by CR-V owner thread: 15 = right rear wheel sensor, 17 = left rear wheel sensor, 54 = fail-safe relay. |
| ABS-18 | Wheel sensor — electrical noise / intermittent interruption (12 = right-front, 14 = left-front, 16 = right-rear, 18 = left-rear) | C | manufacturer | [A] | faulty wheel sensor pulse signal; damaged pulser ring; electrical noise | corroborated by s2ki S2000 thread: 12 = faulty right front wheel sensor pulse signal, 14 = left front, 16 = right rear, 18 = left rear |
| ABS-21 | Pulser — 21 = right-front, 22 = left-front, 23 = right-rear, 24 = left-rear | C | manufacturer | [A] | — | — |
| ABS-22 | Pulser — 21 = right-front, 22 = left-front, 23 = right-rear, 24 = left-rear | C | manufacturer | [A] | — | — |
| ABS-23 | Pulser — 21 = right-front, 22 = left-front, 23 = right-rear, 24 = left-rear | C | manufacturer | [A] | — | — |
| ABS-24 | Pulser — 21 = right-front, 22 = left-front, 23 = right-rear, 24 = left-rear | C | manufacturer | [A] | — | — |
| ABS-31 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-32 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-33 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-34 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-35 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-36 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-37 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-38 | Solenoid (short to body ground / short to wire) | C | manufacturer | [A] | — | individual solenoid (inlet/outlet per wheel) assignment not documented in sources found |
| ABS-41 | Wheel lock | C | manufacturer | [A] | — | listed in the Acura 3.5 RL manual index; not present in the Honda brake-guide excerpt found |
| ABS-42 | Wheel lock | C | manufacturer | [A] | — | listed in the Acura 3.5 RL manual index; not present in the Honda brake-guide excerpt found |
| ABS-43 | Wheel lock | C | manufacturer | [A] | — | listed in the Acura 3.5 RL manual index; not present in the Honda brake-guide excerpt found |
| ABS-44 | Wheel lock | C | manufacturer | [A] | — | listed in the Acura 3.5 RL manual index; not present in the Honda brake-guide excerpt found |
| ABS-51 | Motor lock | C | manufacturer | [A] | — | — |
| ABS-52 | Motor stuck OFF | C | manufacturer | [A] | — | — |
| ABS-53 | Motor stuck ON | C | manufacturer | [A] | — | — |
| ABS-54 | ABS fail-safe relay | C | manufacturer | [A] | faulty fail-safe relay | corroborated by CR-V owner thread (code 54 = fail-safe relay, often set alongside wheel-sensor codes) |
| ABS-61 | Low IG1 voltage | C | manufacturer | [A] | low battery/system voltage | — |
| ABS-62 | High IG1 voltage | C | manufacturer | [A] | charging system overvoltage | — |
| ABS-81 | Central Processing Unit (CPU) diagnosis; ROM/RAM diagnosis | C | manufacturer | [A] | faulty ABS control unit | — |
| P1009 | Camshaft Position (CMP) Sensor, Intake/Front, Bank 1 — Circuit Malfunction / Timing Over-Advanced / System Performance | P | manufacturer | [C] | wiring; valve timing; engine mechanical fault; CMP actuator; ECM | — |
| P1020 | Valve Position Control Circuit — Valve Stuck Off | P | manufacturer | [C] | oil level; wiring; VTEC solenoid valve assembly; rocker-arm oil pressure sensor; ECM | — |
| P1021 | Valve Position Control Circuit — Valve Stuck On | P | manufacturer | [C] | oil level; wiring; VTEC solenoid valve assembly; rocker-arm oil pressure sensor | — |
| P1024 | Valve Position Control Circuit — Valve Sticking On | P | manufacturer | [C] | wiring; rocker arm assembly | — |
| P1025 | Valve Position Control Circuit — Valve Sticking Off | P | manufacturer | [C] | MAP sensor; rocker arm assembly | — |
| P1026 | Valve Position Control Circuit — Valve Stuck On | P | manufacturer | [C] | rocker arm assembly | — |
| P1103 | Mass Airflow Sensor Higher Than Expected | P | manufacturer | [C] | — | — |
| P1106 | Barometric Pressure (BARO) Sensor Circuit Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1107 | Barometric Pressure (BARO) Sensor Circuit Low Input | P | manufacturer | [C] | — | — |
| P1108 | Barometric Pressure (BARO) Sensor Circuit High Input | P | manufacturer | [C] | — | — |
| P1109 | Barometric Pressure (BARO) Sensor — Circuit Malfunction, Out of Range | P | manufacturer | [C] | wiring; ECM programming; ECM | — |
| P1111 | Intake Air Temperature (IAT) Sensor — Circuit/Intermittent Voltage High | P | manufacturer | [C] | wiring; IAT sensor | — |
| P1112 | Intake Air Temperature (IAT) Sensor — Circuit/Intermittent Voltage Low | P | manufacturer | [C] | wiring; IAT sensor | — |
| P1114 | Engine Coolant Temperature (ECT) Sensor — Circuit/Intermittent Voltage High | P | manufacturer | [C] | wiring; ECT sensor | — |
| P1115 | Engine Coolant Temperature (ECT) Sensor — Circuit/Intermittent Voltage High | P | manufacturer | [C] | wiring; ECT sensor | source lists P1114 and P1115 with near-identical descriptions; treated as listed, possible transcription duplication |
| P1116 | Engine Coolant Temperature (ECT) Sensor — Range/Performance Problem | P | manufacturer | [C] | wiring; ECT sensor 1; ECT sensor 2 | — |
| P1120 | Throttle Motor Position Sensor 1 — Circuit Malfunction | P | manufacturer | [C] | wiring open/short to ground/short to positive; throttle control unit; ECM | — |
| P1121 | Throttle Position (TP) Sensor Lower Than Expected | P | manufacturer | [B] | — | — |
| P1122 | Throttle Position (TP) Sensor Higher Than Expected | P | manufacturer | [B] | — | — |
| P1125 | Throttle Position (TP) Motor — Fail-Safe Mode | P | manufacturer | [C] | wiring; TP sensor; TP motor; mechanical fault; ECM | — |
| P1128 | Manifold Absolute Pressure (MAP) Sensor Circuit Lower Than Expected | P | manufacturer | [B] | — | — |
| P1129 | Manifold Absolute Pressure (MAP) Sensor Circuit Higher Than Expected | P | manufacturer | [B] | — | — |
| P1130 | Heated Oxygen Sensor (HO2S) 2/3 — Faulty Components | P | manufacturer | [C] | HO2S 2; HO2S 3 | — |
| P1133 | Heated Oxygen Sensor (HO2S), RH Front — Insufficient Switching | P | manufacturer | [C] | exhaust system; wiring; HO2S; ECM | — |
| P1134 | Heated Oxygen Sensor (HO2S), RH Front — Slow Operation | P | manufacturer | [C] | exhaust system; wiring; HO2S; ECM | — |
| P1149 | Primary Heated Oxygen Sensor (Sensor 1) Circuit Range/Performance Problem | P | manufacturer | [B] | — | — |
| P1153 | Heated Oxygen Sensor (HO2S), LH Front — Insufficient Switching | P | manufacturer | [C] | exhaust system; wiring; HO2S; ECM | — |
| P1154 | Heated Oxygen Sensor (HO2S), LH Front — Slow Operation | P | manufacturer | [C] | exhaust system; wiring; HO2S; ECM | — |
| P1157 | Air/Fuel Ratio (A/F) Sensor (Sensor 1) Range/Performance Problem | P | manufacturer | [B] | — | — |
| P1158 | Air/Fuel Ratio (A/F) Sensor (Sensor 1) Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1159 | Air/Fuel Ratio (A/F) Sensor (Sensor 1) Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1162 | Primary Heated Oxygen Sensor (No. 1) Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1163 | Primary Heated Oxygen Sensor (No. 1) Circuit Slow Response | P | manufacturer | [B] | — | — |
| P1164 | Primary Heated Oxygen Sensor (No. 1) Circuit Range/Performance | P | manufacturer | [B] | — | — |
| P1165 | Primary Heated Oxygen Sensor (No. 1) Circuit Range/Performance | P | manufacturer | [B] | — | — |
| P1166 | Primary Heated Oxygen Sensor (No. 1) Heater System Electrical | P | manufacturer | [B] | — | — |
| P1167 | Primary Heated Oxygen Sensor (No. 1) Heater System | P | manufacturer | [B] | — | — |
| P1168 | Primary Heated Oxygen Sensor (No. 1) LABEL Circuit Low Input | P | manufacturer | [B] | — | — |
| P1169 | Primary Heated Oxygen Sensor (No. 1) LABEL Circuit High Input | P | manufacturer | [B] | — | — |
| P1171 | Heated Oxygen Sensor (HO2S) 1 — Circuit Malfunction | P | manufacturer | [C] | wiring; HO2S; ECM | — |
| P1172 | Heated Oxygen Sensor (HO2S) 1, Bank 1 — Out of Range, High | P | manufacturer | [C] | wiring; HO2S | — |
| P1174 | Heated Oxygen Sensor (HO2S) 2, Bank 2 — Out of Range, High | P | manufacturer | [C] | wiring; HO2S | — |
| P1182 | Fuel Temperature Sensor Circuit Low Voltage | P | manufacturer | [A] | wiring short to ground; fuel temperature sensor (per ninjafix.in) | — |
| P1183 | Fuel Temperature Sensor Circuit High Voltage | P | manufacturer | [A] | wiring short to positive; fuel temperature sensor (per ninjafix.in) | — |
| P1187 | Fuel Tank Temperature Sensor — Low Input | P | manufacturer | [C] | wiring short to ground; fuel tank temperature sensor; ECM | — |
| P1188 | Fuel Tank Temperature Sensor — High Input | P | manufacturer | [C] | wiring short to positive; fuel tank temperature sensor; ECM | — |
| P1192 | Fuel Tank Pressure Sensor — Low Input | P | manufacturer | [C] | wiring short to ground; fuel tank pressure sensor | — |
| P1193 | Fuel Tank Pressure Sensor — High Input | P | manufacturer | [C] | wiring short to positive; fuel tank pressure sensor | — |
| P1201 | Cylinder 1 Misfire | P | manufacturer | [B] | — | Honda-specific per-cylinder misfire code; sources direct readers to compare with generic P0301. ninjafix.in variant wording: "Fuel System Failure Caused No. 1 Cylinder Misfire". |
| P1202 | Cylinder 2 Misfire | P | manufacturer | [B] | — | compare with generic P0302 |
| P1203 | Cylinder 3 Misfire | P | manufacturer | [B] | — | compare with generic P0303 |
| P1204 | Cylinder 4 Misfire | P | manufacturer | [B] | — | compare with generic P0304 |
| P1205 | Cylinder 5 Misfire | P | manufacturer | [B] | — | compare with generic P0305 |
| P1206 | Cylinder 6 Misfire | P | manufacturer | [B] | — | compare with generic P0306 |
| P1220 | Throttle Motor Position Sensor 2 — Circuit Malfunction | P | manufacturer | [C] | wiring open/short to ground/short to positive; throttle control unit; ECM | — |
| P1221 | Throttle Motor Position Sensor 1/2 — Signal Variation | P | manufacturer | [C] | wiring; throttle control unit; ECM | — |
| P1241 | Throttle Vent Control Motor Circuit 1 Malfunction | P | manufacturer | [B] | — | ninjafix.in variant wording: "Throttle Valve Control Motor Circuit 1 Malfunction" |
| P1242 | Throttle Vent Control Motor Circuit 2 Malfunction | P | manufacturer | [B] | — | ninjafix.in variant wording: "Throttle Valve Control Motor Circuit 2 Malfunction" |
| P1243 | Throttle Position Insufficient | P | manufacturer | [B] | — | — |
| P1244 | Closed Throttle Position Insufficient | P | manufacturer | [B] | — | — |
| P1246 | Accelerator Position Sensor 1 Circuit Malfunction | P | manufacturer | [B] | — | ninjafix.in variant wording: "Accelerator Pedal Position Sensor 1 Circuit Malfunction" |
| P1247 | Accelerator Position Sensor 2 Circuit Malfunction | P | manufacturer | [B] | — | ninjafix.in variant wording: "Accelerator Pedal Position Sensor 2 Circuit Malfunction" |
| P1248 | Accelerator Position Sensors 1 & 2 Improper Correlation | P | manufacturer | [B] | — | ninjafix.in variant wording: "Accelerator Pedal Position Sensor 1 and 2 Incorrect correlation" |
| P1253 | VTEC System Malfunction | P | manufacturer | [B] | — | — |
| P1257 | VTEC System Malfunction | P | manufacturer | [B] | — | — |
| P1258 | VTEC System Malfunction | P | manufacturer | [B] | — | — |
| P1259 | VTEC System Malfunction (Rear Bank / Bank 1) | P | manufacturer | [B] | low engine oil level; dirty/degraded oil; faulty VTEC solenoid (spool valve assembly); faulty VTEC oil pressure switch; wiring fault to solenoid/switch | If the code sets at or below ~4000 RPM it tends to be wiring/switch; above ~4000 RPM it tends to be oil-related (Honda master tech guidance). Check oil level and condition FIRST — VTEC is hydraulically actuated. On 1998-2002 Accord the fix was commonly the VTEC spool valve assembly. |
| P1271 | Accelerator Pedal Position (APP) Sensor 1/2 — Signal Variation | P | manufacturer | [C] | wiring; APP sensor; ECM | — |
| P1272 | Accelerator Pedal Position (APP) Sensor 2/3 — Signal Variation | P | manufacturer | [C] | wiring; APP sensor; ECM | — |
| P1273 | Accelerator Pedal Position (APP) Sensor 1/3 — Signal Variation | P | manufacturer | [C] | wiring; APP sensor; ECM | — |
| P1275 | Accelerator Pedal Position (APP) Sensor 1 — Circuit Malfunction | P | manufacturer | [C] | wiring open/short to ground/short to positive; APP sensor; ECM | — |
| P1279 | VTEC System Malfunction, Front Bank (Bank 2) | P | manufacturer | [C] | — | — |
| P1280 | Accelerator Pedal Position (APP) Sensor 2 — Circuit Malfunction | P | manufacturer | [C] | wiring open/short to ground/short to positive; APP sensor; ECM | — |
| P1285 | Accelerator Pedal Position (APP) Sensor 3 — Circuit Malfunction | P | manufacturer | [C] | wiring; APP sensor; ECM | — |
| P1286 | Oil Pressure Sensor, Rocker Arm — Signal Stuck Low | P | manufacturer | [C] | oil level; wiring; VTEC system oil line; rocker-arm oil pressure sensor | — |
| P1287 | Oil Pressure Switch, Rocker Arm — Circuit High Voltage | P | manufacturer | [C] | oil level; wiring; rocker-arm oil pressure switch; ECM programming; ECM | — |
| P1288 | Oil Pressure Switch, Rocker Arm — Circuit Low Voltage | P | manufacturer | [C] | oil level; wiring; rocker-arm oil pressure switch; ECM programming; ECM | — |
| P1289 | Oil Pressure Sensor, Rocker Arm — Stuck High | P | manufacturer | [C] | oil level; rocker-arm oil pressure sensor | — |
| P128A | Valve Position Control Circuit — Valve Stuck Off | P | manufacturer | [C] | oil level; wiring; engine oil pressure sensor; rocker arm oil control valve | — |
| P128B | Valve Position Control Circuit — Malfunction | P | manufacturer | [C] | oil level; wiring; engine oil pressure sensor; rocker arm oil control valve | — |
| P1290 | Throttle Position (TP) Motor — Forced Idle Mode | P | manufacturer | [C] | wiring; APP sensor; TP motor; mechanical fault; ECM | — |
| P1295 | Throttle Position (TP) Motor — Power Management Mode | P | manufacturer | [C] | wiring; TP sensor; TP motor; MAP sensor; MAF sensor; ECM | — |
| P1297 | Electrical Load Detector (ELD) Circuit Low Input | P | manufacturer | [B] | faulty ELD unit; ELD harness open/shorted; poor electrical connection in ELD circuit | — |
| P1298 | Electrical Load Detector (ELD) Circuit High Input | P | manufacturer | [B] | faulty ELD (faulty solder joint per Honda service bulletin — most common); blown fuse; poor connections/loose terminals at ELD or PCM; open in wire between under-dash fuse/relay box and ELD; faulty PCM (rare) | Honda service bulletin covers this: replace the ELD (P/N 38255-S5A-003); replacement ELDs are now sold separately so the whole under-hood fuse/relay box no longer needs replacement. ELD 3P connector is behind/beneath the under-hood fuse box. Check fuse No. 4 and battery voltage at ELD terminal 1 (BLK/ORN wire) with ignition on. |
| P1299 | Throttle Position (TP) Motor — Forced Engine Shut Down Mode | P | manufacturer | [C] | wiring; TP sensor; TP motor; MAP sensor; MAF sensor; ECM | CONFLICT (cross-make): Ford uses P1299 for "Cylinder Head Over Temperature Protection Active" (Ford powertrain DTC charts). The Honda-specific meaning above is from the Honda fault-code list. |
| P1300 | Multiple Cylinder Misfire Detected | P | manufacturer | [B] | — | Honda-specific random-misfire code distinct from generic P0300; on some models compares against P0301-P0306 cylinder-specific logic. |
| P1301 | Cylinder 1 Misfire | P | manufacturer | [B] | — | compare with generic P0301 |
| P1302 | Cylinder 2 Misfire | P | manufacturer | [B] | — | compare with generic P0302 |
| P1303 | Cylinder 3 Misfire | P | manufacturer | [B] | — | compare with generic P0303 |
| P1304 | Cylinder 4 Misfire | P | manufacturer | [B] | — | compare with generic P0304 |
| P1305 | Cylinder 5 Misfire | P | manufacturer | [B] | — | compare with generic P0305 |
| P1306 | Cylinder 6 Misfire | P | manufacturer | [B] | — | compare with generic P0306 |
| P1310 | Ignition Control Module (ICM) — Diagnosis | P | manufacturer | [C] | wiring; ignition coil(s); ICM; ECM | — |
| P1311 | Ignition Control Module (ICM) — Ignition Coil Secondary Signal, Circuit 1 | P | manufacturer | [C] | wiring; ignition coil(s); ICM; ECM | — |
| P1312 | Ignition Control Module (ICM) — Ignition Coil Secondary Signal, Circuit 2 | P | manufacturer | [C] | wiring; ignition coil(s); ICM; ECM | — |
| P1316 | Spark Plug Voltage Detection Circuit Malfunction, Front Bank | P | manufacturer | [C] | — | — |
| P1317 | Spark Plug Voltage Detection Circuit Malfunction, Rear Bank | P | manufacturer | [C] | — | — |
| P1318 | Spark Plug Voltage Detection Module Reset Circuit Malfunction, Front Bank | P | manufacturer | [C] | — | — |
| P1319 | Spark Plug Voltage Detection Module Reset Circuit Malfunction, Rear Bank | P | manufacturer | [C] | — | — |
| P1324 | Knock Sensor Power Source Circuit Low Voltage | P | manufacturer | [C] | — | — |
| P1326 | Ignition Control Module (ICM) — Combustion Quality Input Signal | P | manufacturer | [C] | wiring; ignition coil(s); ICM; ECM | — |
| P1336 | Crankshaft Position (CKP) Sensor B (CSF Sensor) Intermittent Interruption | P | manufacturer | [B] | — | — |
| P1337 | Crankshaft Position (CKP) Sensor B (CSF Sensor) No Signal | P | manufacturer | [B] | — | — |
| P1340 | Ignition Control Module (ICM) — Cylinder Identification/Synchronization | P | manufacturer | [C] | wiring; ignition coil(s); ICM; ECM | — |
| P1355 | Front Ignition Coil Power Circuit Malfunction | P | manufacturer | [A] | wiring; fuse; ignition coil; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Intake side ignition coil — power supply circuit malfunction" |
| P1356 | Exhaust Side Ignition Coil — Power Supply Circuit Malfunction | P | manufacturer | [C] | wiring; fuse; ignition coil; ECM programming; ECM | — |
| P1359 | Crankshaft Position (CKP)/Top Dead Center (TDC) Sensor Connector Disconnection | P | manufacturer | [B] | — | — |
| P1361 | Intermittent Interruption in Top Dead Center (TDC) 1 Sensor Circuit | P | manufacturer | [B] | TDC sensor inside distributor (1990s models — replace distributor assembly per Honda); TDC sensor sub-harness damage at firewall side of timing cover (2000s models); poor connections/loose terminals between distributor/sensor and ECM/PCM; faulty ECM/PCM (rare) | On distributor-era Hondas the TDC sensor is integral to the distributor — Honda recommends the whole distributor. On 2001+ Civic the sensor sits behind the top timing cover (driver side); inspect the 4-pin sub-harness connector and scope the AC sine wave (Green/Red wires for TDC) while wiggling the harness. Can put the engine in limp mode (3500 RPM limit). |
| P1362 | No Signal in Top Dead Center (TDC) 1 Sensor Circuit | P | manufacturer | [B] | failed TDC sensor; CKP/TDC sensor sub-harness open; distributor ignition housing failure; poor connections/loose terminals between distributor and ECM/PCM; faulty ECM/PCM (rare) | P1361 = intermittent interruption, P1362 = complete signal loss. Check for metal shavings, oil, or rust inside the distributor (rust indicates worn bearings — replace distributor). Voltage checks: ~12V on BLK/YEL wire, ~5V reference on GRN wire with ignition on. |
| P1366 | Intermittent Interruption in Top Dead Center (TDC) 2 Sensor Circuit | P | manufacturer | [B] | — | — |
| P1367 | No Signal in Top Dead Center (TDC) 2 Sensor Circuit | P | manufacturer | [B] | — | — |
| P1380 | ECM/ABS Control Module, Rough Road Signal — Communication Fault | P | manufacturer | [C] | wiring; ABS trouble code(s) stored; ECM | — |
| P1381 | Cylinder Position (CYP) Sensor Intermittent Interruption | P | manufacturer | [B] | — | — |
| P1382 | Cylinder Position (CYP) Sensor No Signal | P | manufacturer | [B] | — | — |
| P1386 | CYP Sensor B Intermittent Interruption | P | manufacturer | [B] | — | ninjafix.in variant wording: "Cylinder Position Sensor 2 Intermittent Interruption" |
| P1387 | CYP Sensor B No Signal | P | manufacturer | [B] | — | ninjafix.in variant wording: "Cylinder Position Sensor Intermittent Interruption" (appears to be a transcription slip for "No Signal"; 5 Star / freeautomechanic / cars-care agree on "No Signal") |
| P1390 | G-Sensor — Intermittent Voltage Low | P | manufacturer | [C] | wiring; G-sensor | — |
| P1391 | G-Sensor — Performance | P | manufacturer | [C] | seal damaged/missing; incorrectly installed; wiring; G-sensor; ECM | — |
| P1392 | G-Sensor — Voltage Low | P | manufacturer | [C] | wiring; G-sensor; ECM | — |
| P1393 | G-Sensor — Voltage High | P | manufacturer | [C] | wiring; G-sensor; ECM | — |
| P1394 | G-Sensor — Intermittent Voltage High | P | manufacturer | [C] | wiring; G-sensor | — |
| P1399 | Random Misfire (Honda-specific; more sensitive than P0300) | P | manufacturer | [B] | ignition components; incorrect valve clearance; vacuum/intake leaks; fuel delivery; engine compression; timing; air/fuel mixture (per Westwood Honda dealer blog) | triggered at far lower crank-speed variation than generic P0300 — PCM "suspects" a misfire (P1399) vs "sure" (P0300). Other makes use P1399 with different definitions. |
| P1404 | Exhaust Gas Recirculation (EGR) Valve — Valve Closed | P | manufacturer | [C] | wiring; EGR valve | — |
| P1406 | Exhaust Gas Recirculation (EGR) Valve Position Sensor — Circuit Problem | P | manufacturer | [C] | wiring; EGR valve/position sensor; ECM | — |
| P1410 | Air Pump Malfunction | P | manufacturer | [A] | wiring; AIR pump relay; AIR pump; ECM (per ninjafix.in) | ninjafix.in variant wording: "Secondary air injection (AIR) pump — malfunction" |
| P1415 | Air Pump Electric Current Sensor Circuit Low Voltage | P | manufacturer | [A] | wiring; AIR pump electrical current sensor; ECM (per ninjafix.in) | ninjafix.in variant wording: "AIR pump electrical current sensor — circuit low" |
| P1416 | Air Pump Electric Current Sensor Circuit High Voltage | P | manufacturer | [A] | wiring; AIR pump electrical current sensor; ECM (per ninjafix.in) | ninjafix.in variant wording: "AIR pump electrical current sensor — circuit high" |
| P1420 | NOx Adsorptive Catalyst System Efficiency Below Threshold | P | manufacturer | [A] | NOx adsorptive three-way catalyst (per ninjafix.in) | ninjafix.in variant wording: "NOx adsorptive catalyst system — efficiency below limit" |
| P1429 | Motor Drive Module — Overheating Signal Circuit Problem | P | manufacturer | [C] | wiring; motor control module (MCM); voltage converter module | — |
| P1430 | Motor Drive Module — Short Circuit Sensor Malfunction | P | manufacturer | [C] | wiring; motor control module (MCM); voltage converter module | — |
| P1431 | Hybrid Battery Pack — Overheating | P | manufacturer | [C] | hybrid battery pack | — |
| P1432 | Battery Cell — Overheating | P | manufacturer | [C] | hybrid battery pack | — |
| P1433 | Hybrid Battery Pack — Deterioration | P | manufacturer | [C] | hybrid battery pack | — |
| P1434 | Voltage Converter Module — High Voltage | P | manufacturer | [C] | stored when battery needs protection from very low temperature; system is OK (per source) | — |
| P1435 | Charge/Discharge Balance Problem | P | manufacturer | [C] | low 12V battery; charging system malfunction | — |
| P1436 | Motor Power Inverter Module — Overheating | P | manufacturer | [C] | motor power inverter module; hybrid battery pack cooling fan duct; hybrid battery pack cover | — |
| P1437 | Motor Power Inverter Module — Short Circuit | P | manufacturer | [C] | wiring; motor power inverter module | — |
| P1438 | Motor Drive Module (MDM) Overheating Signal Circuit; Motor Drive Module (MDM) Overheating | P | manufacturer | [A] | wiring; motor power inverter module fan; fan duct line; voltage converter module; motor power inverter module (per ninjafix.in) | bulletin lists two detection items under P1438 (signal circuit / overheating). ninjafix.in variant wording: "Motor driver module — overheating". |
| P1439 | Motor Drive Module (MDM) Short Circuit Sensor Problem; Motor Drive Module (MDM) Short Circuit | P | manufacturer | [A] | wiring; motor power inverter module (per ninjafix.in) | bulletin lists two detection items under P1439. ninjafix.in variant wording: "Motor driver module — short circuit". |
| P1440 | IMA System Problem | P | manufacturer | [A] | wiring; motor power cable; motor stator; motor power inverter module; motor rotor; MCM programming; MCM (per ninjafix.in) | ninjafix.in variant wording: "Motor power inverter module — output circuit malfunction" |
| P1441 | Evaporative Emission (EVAP) Canister Purge System — Flow Detected | P | manufacturer | [C] | wiring; EVAP solenoid; ECM | — |
| P1442 | Evaporative Emission (EVAP) Canister Purge System — Vacuum Switch Malfunction | P | manufacturer | [C] | wiring; vacuum switch; ECM | — |
| P1443 | High Voltage Contactor/Bypass Contactor — Contactor Stays Activated | P | manufacturer | [C] | wiring; DC-DC converter; hybrid battery pack; motor power inverter module; MCM programming; MCM | — |
| P1444 | High Voltage Short Circuit | P | manufacturer | [C] | motor power inverter module; motor stator; motor power cable assembly; DC-DC converter; power drive unit capacitor; high voltage cable; hybrid battery | — |
| P1445 | Bypass Control Problem | P | manufacturer | [A] | wiring; hybrid battery pack; bypass resistor; DC-DC converter; motor power inverter module; bypass contactor; motor control (per ninjafix.in) | ninjafix.in variant wording: "Bypass contactor malfunction" |
| P1446 | Hybrid Battery Pack — Individual Voltage Input Deviation | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1447 | Hybrid Battery Pack Deviation | P | manufacturer | [C] | hybrid battery pack | — |
| P1448 | Battery Module Overheating | P | manufacturer | [A] | wiring; hybrid battery pack cooling fan; MCM programming; MCM (per ninjafix.in) | ninjafix.in variant wording: "Hybrid battery pack cooling — malfunction" |
| P1449 | Battery Cell Overheating; Battery Module Individual Voltage Input Deviation; Battery Module Deterioration; Battery Module Deviation | P | manufacturer | [A] | hybrid battery pack (per ninjafix.in) | bulletin lists four detection items under P1449. ninjafix.in lists P1449 as "Hybrid battery pack — deterioration". |
| P1454 | Fuel Tank Pressure (FTP) Sensor Range/Performance Problem | P | manufacturer | [A] | wiring; blockage in EVAP canister/filter/vent hoses/drain joint or FTP sensor air tube; EVAP canister vent shut-off valve; fuel tank (per ninjafix.in) | ninjafix.in variant wording: "Fuel tank pressure sensor — circuit range/performance" |
| P1456 | Evaporative Emission (EVAP) Control System Leak Detected (Fuel Tank System) | P | manufacturer | [B] | loose or faulty fuel filler cap (most common — use OEM Honda cap, tighten 3 clicks); leaking EVAP bypass solenoid; leaking two-way valve; leaking ORVR valve on top of fuel tank; leak in fuel tank or tank-side hoses | Honda's EVAP self-test runs the tank-side test (P1456) BEFORE the canister-side test (P1457) — a P1456 must be resolved first. Back-probe the fuel tank pressure sensor (GRN wire): ~2.5V at rest; voltage rises as the tank builds pressure with the engine running and should not fall after shutdown. Clamp the hose between the bypass solenoid/two-way valve assembly and the canister to isolate tank-side vs canister-side leaks. |
| P1457 | Evaporative Emission (EVAP) Control System Leak Detected (EVAP Control Canister System) | P | manufacturer | [B] | faulty EVAP canister vent shut (CVS) valve stuck open — most common (valve lives under the car near the rear axle, corrodes); cracked/rotted EVAP hoses; saturated charcoal canister (from habitual fuel top-offs); faulty fuel cap | Will not affect drivability but fails emissions inspection. A bi-directional scan tool can command the vent (CVS) valve closed while listening for the click; a smoke machine finds the small leaks. Note: the tank-side test (P1456) must pass before the canister-side test runs, so fix P1456 first when both appear. |
| P1459 | Evaporative Emission (EVAP) Purge Flow Switch Malfunction | P | manufacturer | [C] | — | — |
| P145C | Evaporative Emission (EVAP) Canister Purge System — Incorrect Flow | P | manufacturer | [C] | wiring; hose leak/blockage; EVAP canister purge valve; mechanical fault; ECM programming; ECM | — |
| P1460 | Fuel Level Sensor Power Supply Circuit | P | manufacturer | [C] | — | — |
| P1486 | Thermostat Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1491 | Exhaust Gas Recirculation (EGR) Valve Lift Insufficient Detected | P | manufacturer | [B] | faulty EGR valve; clogged EGR ports/passages in intake manifold (carbon buildup — very common on V6 Accord); faulty EGR vacuum regulator/solenoid | Honda TSB covers the V6 Accord: remove the intake manifold, drill out the EGR port, and install a stainless-steel sleeve kit to prevent carbon re-clogging (goodwill/warranty extension applied on some vehicles). Closed-valve lift-sensor voltage is normally 1.1-1.2V on the WHT/BLK wire; manually applying battery voltage to the valve should swing it to ~4.0V. Use OEM EGR parts. |
| P1498 | Exhaust Gas Recirculation (EGR) Valve Lift Sensor High Voltage | P | manufacturer | [B] | faulty EGR valve/position sensor (note: aftermarket EGR valves have caused repeat P1498); EGR harness connector not supplying 5V reference | Check the harness connector to the EGR for 5V reference (measured ~5.1V good). If reference voltage is present and the code returns, suspect the EGR valve itself. |
| P1505 | Positive Crankcase Ventilation (PCV) Air Leakage | P | manufacturer | [A] | vacuum leaks; PCV valve; EVAP canister purge valve; throttle body; intake manifold (per ninjafix.in) | ninjafix.in variant wording: "Intake system — leak detected" |
| P1508 | Idle Air Control (IAC) Valve Circuit Failure | P | manufacturer | [C] | — | — |
| P1509 | Idle Air Control (IAC) Valve Circuit Failure | P | manufacturer | [C] | — | — |
| P1514 | Throttle Position (TP) Sensor / Mass Air Flow (MAF) Sensor — Signal Variation | P | manufacturer | [C] | wiring; TP sensor; MAP sensor; ECM | — |
| P1515 | Throttle Command / Actual Throttle Position — Signal Variation | P | manufacturer | [C] | wiring; throttle valve sticking; throttle control unit; ECM | — |
| P1516 | Throttle Position Motor — Position Performance | P | manufacturer | [C] | throttle valve tight/sticking; TP sensor; wiring; throttle control unit; ECM | — |
| P1519 | Idle Air Control Valve Circuit Failure | P | manufacturer | [C] | — | — |
| P1522 | Brake Booster Pressure Sensor Circuit Low Voltage | P | manufacturer | [A] | wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Brake booster pressure sensor — circuit malfunction, low voltage" |
| P1523 | Brake Booster Pressure Sensor Circuit High Voltage | P | manufacturer | [A] | wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Brake booster pressure sensor — circuit malfunction, high voltage" |
| P1524 | Brake Booster Pressure Sensor Range/Performance Problem | P | manufacturer | [A] | wiring; brake booster pressure sensor; brake booster vacuum line; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Brake booster pressure sensor — range/performance problem" |
| P1541 | Climate Control Unit Signal Circuit Low Voltage | P | manufacturer | [A] | wiring; heater control panel; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Passenger compartment heater standby signal circuit — low input" |
| P1542 | Climate Control Unit Signal Circuit High Voltage | P | manufacturer | [A] | wiring; heater control panel; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Passenger compartment heater standby signal circuit — high input" |
| P1549 | Generator System — High Voltage | P | manufacturer | [C] | wiring; generator; ECM | — |
| P1553 | Hybrid Battery Pack Temperature Sensor 1 — Signal Circuit Low Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1554 | Hybrid Battery Pack Temperature Sensor 1 — Signal Circuit High Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1555 | Hybrid Battery Pack Temperature Sensor 2 — Signal Circuit Low Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1556 | Hybrid Battery Pack Temperature Sensor 2 — Signal Circuit High Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1557 | Hybrid Battery Pack Temperature Sensor 3 — Signal Circuit Low Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1558 | Hybrid Battery Pack Temperature Sensor 3 — Signal Circuit High Input | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1559 | Motor Commutation Sensor A — Circuit Low Input | P | manufacturer | [C] | wiring; motor control module (MCM); motor commutation sensor; drive plate sensor | — |
| P1560 | Motor Commutation Sensor A — Circuit High Input | P | manufacturer | [C] | wiring; motor control module (MCM); motor commutation sensor; drive plate sensor | — |
| P1561 | Motor Commutation Sensor B — Circuit Low Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor commutation sensor | — |
| P1562 | Motor Commutation Sensor B — Circuit High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor commutation sensor | — |
| P1563 | Motor Commutation Sensor C — Circuit Low Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor commutation sensor | — |
| P1564 | Motor Commutation Sensor C — Circuit High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor commutation sensor | — |
| P1565 | Motor Commutation Signal Problem | P | manufacturer | [A] | wiring; motor control module (MCM); motor commutation sensor; MCM (per ninjafix.in) | — |
| P1566 | Motor Commutation Sensor — Signal Problem | P | manufacturer | [C] | wiring; MCM programming; MCM | — |
| P1567 | Cylinder Position Signal Circuit Problem | P | manufacturer | [C] | wiring; MCM programming; MCM; ECM programming; ECM | — |
| P1568 | Battery Module Individual Voltage Input Problem; Battery Module Temperature Signal Circuit Problem; Battery Cell Temperature Signal Circuit Problem | P | manufacturer | [A] | wiring; battery condition monitor module; hybrid battery pack (per ninjafix.in) | bulletin lists three detection items under P1568. ninjafix.in variant wording: "Battery cell — temperature signal circuit malfunction". |
| P1569 | Battery Cell — Temperature Signal Circuit Malfunction | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1570 | Hybrid Battery Pack — Individual Voltage Problem | P | manufacturer | [C] | wiring; hybrid battery pack; MCM programming; MCM | — |
| P1571 | Motor Commutation Sensor — Voltage Input Problem | P | manufacturer | [C] | wiring; MCM programming; MCM | — |
| P1572 | Motor Drive Module (MDM) Temperature Signal Circuit Low Input; Motor Drive Module (MDM) Temperature Signal Circuit High Input | P | manufacturer | [A] | wiring; voltage converter module; motor power inverter module; motor control module (MCM) (per ninjafix.in) | bulletin lists two detection items under P1572 (low/high input). ninjafix.in variant wording: "Motor driver module — temperature signal circuit high". |
| P1573 | DC-DC Converter — Temperature Signal Circuit High Input | P | manufacturer | [C] | wiring; motor control module (MCM); DC-DC converter | — |
| P1574 | Hybrid Battery Pack — Temperature Signal Circuit Malfunction | P | manufacturer | [C] | wiring; hybrid battery pack | — |
| P1575 | Motor Power Inverter Module — Voltage Malfunction | P | manufacturer | [C] | wiring; high voltage contactor; hybrid battery pack; motor control module (MCM) | — |
| P1576 | Motor Drive Module (MDM) Voltage Signal Circuit Low Input | P | manufacturer | [A] | wiring; hybrid battery pack; motor power inverter module; voltage converter module; battery condition monitor module; high voltage contactor (per ninjafix.in) | ninjafix.in variant wording: "Motor driver module — voltage malfunction" |
| P1577 | High Voltage Detection Signal Circuit Problem | P | manufacturer | [A] | wiring; motor control module (MCM); hybrid battery pack (per ninjafix.in) | ninjafix.in variant wording: "High voltage detection signal — circuit problem" |
| P1580 | Battery Current Circuit Problem | P | manufacturer | [A] | wiring; battery current sensor; MCM programming; MCM (per ninjafix.in) | ninjafix.in variant wording: "Battery current sensor — circuit malfunction" |
| P1581 | Motor Power Inverter (MPI) Module Current Signal Circuit Low Input; Motor Power Inverter (MPI) Module Current Signal Circuit High Input; Motor Power Inverter (MPI) Module Current Signal Circuit Problem | P | manufacturer | [A] | wiring; motor power inverter module; hybrid battery pack; MCM programming (per ninjafix.in) | bulletin lists three detection items under P1581. ninjafix.in variant wording: "Motor power inverter module — current signal circuit problem". |
| P1582 | Motor Current U Phase Signal Circuit Low Input; Motor Current U Phase Signal Circuit High Input | P | manufacturer | [A] | wiring; motor control module (MCM); motor current U phase sensor (per ninjafix.in) | bulletin lists two detection items under P1582 (low/high input) |
| P1583 | Motor Current V Phase Signal Circuit Low Input; Motor Current V Phase Signal Circuit High Input | P | manufacturer | [A] | wiring; motor control module (MCM); motor current V phase sensor (per ninjafix.in) | bulletin lists two detection items under P1583 (low/high input) |
| P1584 | Motor Current W Phase Signal Circuit Low Input; Motor Current W Phase Signal Circuit High Input | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1584 as "Brake fluid pressure sensor B — circuit low voltage". The Honda bulletin (A-grade) assigns P1584 to the motor-current W-phase circuit; the bulletin definition is used here. |
| P1585 | Motor Current Signal Circuit Problem | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1585 as "Brake fluid pressure sensor B — circuit range/performance problem". The Honda bulletin (A-grade) definition is used here. |
| P1586 | Motor Power Inverter (MPI) Module Current Signal / Battery Current Signal Circuit Problem | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1586 as "Brake fluid pressure sensor A/B — circuit malfunction". The Honda bulletin (A-grade) definition is used here. |
| P1587 | Motor Power Inverter Module — Current Signal Circuit Low Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor power inverter | — |
| P1588 | Motor Power Inverter Module — Current Signal Circuit High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor power inverter | — |
| P1589 | Motor Power Inverter Module — Current Signal Problem | P | manufacturer | [C] | motor power inverter module current sensor; MCM programming; MCM; motor power inverter | — |
| P1590 | Motor Current U Phase Signal Circuit — Low Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor current U phase | — |
| P1591 | Motor Current U Phase Signal Circuit — High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor current U phase | — |
| P1593 | Motor Current V Phase Signal Circuit — High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor current V phase | — |
| P1594 | Motor Current W Phase Signal Circuit — Low Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor current W phase | — |
| P1595 | Motor Current W Phase Signal Circuit — High Input | P | manufacturer | [C] | wiring; MCM programming; MCM; motor current W phase | — |
| P15A0 | Motor Driver Module — Temperature Signal Circuit Low | P | manufacturer | [C] | wiring; voltage converter module; motor power inverter module; motor control module (MCM) | source renders as "P15AO"; normalized to P15A0 (hex digit) for consistency with the P15Ax family |
| P15A1 | Motor Driver Module — Temperature Signal Circuit High | P | manufacturer | [C] | wiring; voltage converter module; motor power inverter module; motor control module (MCM) | — |
| P15A2 | Motor Driver Module — Voltage Signal Circuit Low Input | P | manufacturer | [C] | wiring; motor control module (MCM); voltage converter module | — |
| P15A3 | Motor Driver Module — Voltage Signal Circuit High Input | P | manufacturer | [C] | wiring; voltage converter module; motor power inverter module; motor control module (MCM) | — |
| P15A4 | A/C Compressor Driver — Relay Stays Activated | P | manufacturer | [C] | wiring; A/C compressor driver; motor power cable; A/C compressor | — |
| P15A5 | Motor Current Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; motor rotor calibration; U/V/W phase motor current sensors; motor power inverter module; motor power cable; motor control | — |
| P15A6 | U Phase Motor Current Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; U phase motor current sensor; MCM programming; MCM | — |
| P15A7 | V Phase Motor Current Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; V phase motor current sensor; MCM programming; MCM | — |
| P15A8 | W Phase Motor Current Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; W phase motor current sensor; MCM programming; MCM | — |
| P15AA | Motor Rotor — Position Not Learned | P | manufacturer | [C] | wiring; motor rotor position sensor | — |
| P15AB | Engine Mounting Control Module — Power Supply Circuit Low Voltage | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P15AC | Engine Mounting Control Module — Internal Circuit Malfunction | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P15AD | Engine Mounting Control Module — Internal Circuit Malfunction | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P15AE | Cylinder Pause Signal Malfunction | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P15AF | Camshaft Position (CMP) Sensor — Signal Malfunction | P | manufacturer | [C] | wiring; engine mounting control module; ECM programming; ECM | — |
| P15B0 | Crankshaft Position (CKP) Sensor — Signal Malfunction | P | manufacturer | [C] | wiring; engine mounting control module; ECM programming; ECM | source renders as "P15BO"; normalized to P15B0 (hex digit) for consistency with the P15Bx family |
| P15B1 | Camshaft Position (CMP) Sensor / Crankshaft Position (CKP) Sensor — Signal Correlation | P | manufacturer | [C] | wiring; engine mounting control module; ECM programming; ECM | — |
| P15B2 | Brake Fluid Pressure Sensor A — Circuit Low Voltage | P | manufacturer | [C] | wiring; brake fluid pressure sensor; ECM programming; ECM | — |
| P15B3 | Brake Fluid Pressure Sensor A — Circuit Range/Performance Problem | P | manufacturer | [C] | wiring; brake fluid pressure sensor; ECM programming; ECM | — |
| P1600 | Integrated Motor Assist System Malfunction | P | manufacturer | [C] | other integrated motor assist codes stored | — |
| P1601 | Integrated Motor Assist — System Malfunction | P | manufacturer | [C] | other integrated motor assist codes stored | — |
| P1605 | CAN Data Bus | P | manufacturer | [C] | ECM programming; ECM | — |
| P1606 | Integrated Motor Assist Controller Area Network Malfunction | P | manufacturer | [C] | ECM programming; ECM | — |
| P1607 | ECM/PCM Internal Circuit Failure A | P | manufacturer | [B] | failed ECM/PCM (bad solder joints / cracked power rectifier reported); weak battery or charging-system fault (low voltage can set it); corroded/loose ECM/PCM powers, grounds, or connector pins | Honda procedure: reset the ECM/PCM (disconnect ~5 minutes), ignition ON 40 seconds, recheck. If P1607 returns, update the ECM/PCM software or substitute a known-good unit — if the symptom clears, replace the original. Rule out battery/charging first (cold-weather P1607 that clears when warm points at solder-joint/connection issues). PCM replacement requires immobilizer reprogramming. |
| P1608 | ECM Internal Circuit Failure B | P | manufacturer | [B] | — | CONFLICT: ninjafix.in lists P1608 as "ECM — internal integrated motor assist controller area network — communication circuit malfunction". The 5 Star Auto Repair definition (paired with P1607 "ECM/PCM Internal Circuit Failure A") is used here; both sources are single-source for this code. |
| P1618 | Engine Control Module (ECM) — Internal Fault | P | manufacturer | [C] | ECM | — |
| P1625 | Engine Control Module (ECM) — Unexpected Reset | P | manufacturer | [C] | interference from non-standard electronics; erase trouble code and re-test | — |
| P1629 | Battery Current Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; motor control module (MCM) programming; MCM | — |
| P1630 | Transmission Control Module | P | manufacturer | [A] | TCM (per ninjafix.in) | ninjafix.in variant wording: "Transmission control module (TCM) processor error" |
| P1633 | Engine Control Module (ECM) Circuit Problem | P | manufacturer | [C] | wiring; motor control module (MCM) programming; MCM | — |
| P1634 | Motor Power Inverter Module — Signal Circuit Malfunction | P | manufacturer | [C] | wiring; motor power inverter module; motor control module (MCM) relay 2; fuse; MCM | — |
| P1635 | Battery Condition Monitor (BCM) Module Problem | P | manufacturer | [A] | wiring; battery condition monitor module (per ninjafix.in) | ninjafix.in variant wording: "Battery condition monitor module — malfunction" |
| P1636 | Motor Power Inverter Module — Internal Circuit Malfunction | P | manufacturer | [C] | wiring; motor power inverter module | — |
| P1637 | Motor Control Module (MCM) — Internal Circuit Malfunction | P | manufacturer | [C] | motor control module (MCM) programming; MCM | — |
| P1638 | Motor Control Module (MCM) — Internal Circuit Malfunction | P | manufacturer | [C] | MCM programming; MCM | — |
| P1639 | MOTB Signal Circuit Malfunction | P | manufacturer | [A] | wiring; MCM; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Motor control module (MCM) — signal circuit malfunction" |
| P1640 | ACTTRQ Motor Torque Signal Circuit Low Input | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming (per ninjafix.in) | ninjafix.in variant wording: "Motor torque signal circuit — low input" |
| P1641 | ACTTRQ Motor Torque Signal Circuit High Input | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming (per ninjafix.in) | ninjafix.in variant wording: "Motor torque signal circuit — high input" |
| P1642 | QBATT Battery Signal Circuit Low Input | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming (per ninjafix.in) | ninjafix.in variant wording: "Battery signal circuit — low input" |
| P1643 | QBATT Battery Signal Circuit High Input | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming (per ninjafix.in) | ninjafix.in variant wording: "Battery signal circuit — high input" |
| P1644 | MOTFSA Signal Malfunction | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction" |
| P1645 | MOTFSB Signal Malfunction | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction" |
| P1646 | MOTSTB Signal Malfunction | P | manufacturer | [A] | wiring; hybrid battery pack; ECM programming; ECM (per ninjafix.in) | ninjafix.in variant wording: "Motor control module (MCM) — signal malfunction" |
| P1647 | Power Command Signal Circuit Low Input; Power Command Signal Circuit High Input; Engine Torque Signal Circuit Low Input; Engine Torque Signal Circuit High Input; Mode Signal Circuit 1 Low Input; Mode Signal Circuit 1 High Input; Mode Signal Circuit 2 Problem | P | manufacturer | [A] | wiring; motor control module (MCM); ECM (per ninjafix.in, which lists P1647 only as "Engine speed signal — circuit problem") | bulletin lists eight detection items under P1647 (two each for power command, engine torque, mode signal 1, plus mode signal 2 problem and engine speed signal circuit problem). ninjafix.in splits several of these into separate codes (P1685/P1686 engine torque, P1689 mode signal 2, P16B3/P16B4 power command, P16B7/P16B8 mode signal 1) — likely a newer model-year split; both attributions are recorded, not reconciled. |
| P1648 | Engine Speed Signal Circuit Problem; Battery Condition Monitor (BCM) Module Communication Signal Circuit Problem | P | manufacturer | [A] | wiring; MCM; battery condition monitor module (per ninjafix.in) | bulletin lists two detection items under P1648. ninjafix.in variant wording: "Motor control module (MCM) — communication signal circuit problem". |
| P1650 | Engine Control Module Quad Driver / Output Driver | P | manufacturer | [C] | wiring; EVAP canister purge valve; intake manifold air control solenoid | — |
| P1655 | SEAF/SEFA/TMA/TMB Signal Line Failure | P | manufacturer | [C] | — | — |
| P1658 | Electronic Throttle System (ETS) Control Relay — On Malfunction | P | manufacturer | [C] | wiring; ETS control relay; ECM programming; ECM | — |
| P1659 | Electronic Throttle System (ETS) Control Relay — Off Malfunction | P | manufacturer | [C] | wiring; fuse; ETS control relay; underhood fusebox/relay plate; ECM programming; ECM | — |
| P165B | Electronic Throttle System (ETS) Relay — Malfunction | P | manufacturer | [C] | wiring; ETS relay; ECM | — |
| P1660 | Automatic Transaxle FI Signal A Circuit Failure | P | manufacturer | [C] | — | — |
| P1671 | A/T FI Data Line No Signal | P | manufacturer | [B] | — | — |
| P1672 | A/T FI Data Line Failure | P | manufacturer | [B] | — | — |
| P1673 | Motor Control Module (MCM) — Relay Stays Activated | P | manufacturer | [C] | wiring; MCM relay 1; MCM programming; MCM | — |
| P1676 | FPTDR Signal Line Failure | P | manufacturer | [C] | — | — |
| P1677 | Traction Control System FI Data Line Failure | P | manufacturer | [B] | — | — |
| P1678 | FPTDR Signal Line Failure | P | manufacturer | [C] | — | — |
| P1679 | RSCD Signal Circuit Malfunction | P | manufacturer | [A] | — | ninjafix.in concurs ("RSCD Signal Circuit Malfunction", no causes listed) |
| P1681 | Automatic Transaxle FI Signal A Low Input | P | manufacturer | [C] | — | — |
| P1682 | Automatic Transaxle FI Signal A High Input | P | manufacturer | [C] | — | — |
| P1683 | Throttle Valve Default Position Spring Performance Problem | P | manufacturer | [A] | wiring; dirty throttle body; throttle body (per ninjafix.in) | ninjafix.in variant wording: "Throttle valve — default position spring performance problem" |
| P1684 | Throttle Valve Return Spring Performance Problem | P | manufacturer | [A] | wiring; dirty throttle body; throttle body (per ninjafix.in) | ninjafix.in variant wording: "Throttle valve — return spring performance problem" |
| P1685 | Engine Torque Signal — Circuit Low Input | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | not in Honda SB 03-020 (which assigns engine-torque low/high to P1647 sub-items); likely a newer split — see P1647 notes |
| P1686 | A/T FI Signal B Circuit Low Voltage | P | manufacturer | [A] | open or short in A/T FI signal B line; TCM fault; PCM fault | SB 03-020 detection item: low voltage in the A/T FI signal B circuit (A/T FI data line between PCM and TCM). Note: an existing single-source list transcribed a different code as 'Automatic Transaxle FI Signal B Low Input' and an OBD list transposes P1686 as a body code (B1686) — CONFLICT recorded, SB 03-020 [A] is preferred. |
| P1687 | Automatic Transaxle FI Signal B High Input | P | manufacturer | [C] | — | — |
| P1689 | Mode Signal Circuit 2 | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | not in Honda SB 03-020 (which assigns mode signal circuit 2 problem to a P1647 sub-item); likely a newer split — see P1647 notes |
| P1690 | Traction Control System STB Line Failure | P | manufacturer | [B] | — | ninjafix.in variant wording: "Traction Control System Circuit Failure" |
| P1696 | Traction Control Fuel Cut Signal Low Input | P | manufacturer | [B] | — | ninjafix.in variant wording: "Traction Control System Voltage Low" |
| P1697 | Traction Control Fuel Cut Signal High Input | P | manufacturer | [B] | — | ninjafix.in variant wording: "Traction Control System Voltage High" |
| P16B3 | Power Command Signal Circuit — Low Input | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | source renders "signaf" (typo for "signal"); likely a newer split of the P1647 sub-items — see P1647 notes |
| P16B4 | Power Command Signal Circuit — High Input | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | likely a newer split of the P1647 sub-items — see P1647 notes |
| P16B7 | Mode Signal Circuit 1 — Low Input | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | likely a newer split of the P1647 sub-items — see P1647 notes |
| P16B8 | Mode Signal Circuit 1 — High Input | P | manufacturer | [C] | wiring; motor control module (MCM); ECM | likely a newer split of the P1647 sub-items — see P1647 notes |
| P16BA | Battery Cell — High Input | P | manufacturer | [C] | wiring; battery condition monitor module; hybrid | — |
| P16BB | Generator System — Low Voltage | P | manufacturer | [C] | wiring; generator; ECM | — |
| P16BC | Generator System — Low Voltage | P | manufacturer | [C] | wiring; generator; ECM | source lists P16BB and P16BC with identical descriptions; treated as listed, possible transcription duplication |
| P16C0 | ECM — Programming Error | P | manufacturer | [C] | ECM programming; ECM | — |
| P16C1 | Motor Control Module (MCM) — Program Not Installed — Battery Condition Monitor Module Program | P | manufacturer | [C] | MCM programming; MCM | — |
| P16C3 | DC-DC Converter Temperature Sensor — Circuit Malfunction | P | manufacturer | [C] | wiring; blocked hybrid battery pack cooling fan duct; hybrid battery pack cooling fan; DC-DC converter | — |
| P16C4 | Engine Mounting Control Actuator — Power Supply Circuit Stuck Off | P | manufacturer | [C] | wiring; fuse; engine mounting control relay; engine mounting control module | — |
| P16C5 | Engine Mounting Control Actuator — Power Supply Circuit Stuck On | P | manufacturer | [C] | wiring; engine mounting control relay; engine mounting control module | — |
| P16C6 | Engine Mounting Control Actuator — High Voltage During Function Test | P | manufacturer | [C] | wiring; engine mounting control module; front, rear engine mountings | — |
| P16C7 | Rear Engine Mounting Actuator Control Circuit — High Current | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P16C8 | Front Engine Mounting Actuator Control Circuit — High Current | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P16C9 | Engine Mounting Control Module — Internal Circuit Malfunction | P | manufacturer | [C] | wiring; engine mounting control module | — |
| P16D5 | CAN Data Bus | P | manufacturer | [C] | ECM programming; ECM | — |
| P16D6 | Integrated Motor Assist Controller Area Network Malfunction | P | manufacturer | [C] | ECM programming; ECM | — |
| P16D7 | ECM — CAN Data Bus — Communication Circuit Malfunction | P | manufacturer | [C] | ECM programming; ECM | — |
| P1705 | Automatic Transaxle Concerns (TCM/Range-switch circuit) | P | manufacturer | [C] | loose terminal on PCM connectors; wire between PCM and transmission range switch shorted (terminals B14/D14/D15/D6/D8/D9 circuits) | Transmission range-switch wiring fault family; inspect PCM connector terminals and range-switch wiring before condemning the transmission. |
| P1706 | TCM A/T Gear Position Switch Circuit Open | P | manufacturer | [C] | — | — |
| P1709 | Problem in Transmission Gear Selection Switch Circuit | P | manufacturer | [A] | wiring; mode switch; TCM (per ninjafix.in) | freeautomechanic.com lists P1709 only as "Automatic Transmission System Malfunction". ninjafix.in variant wording: "AT — Sport shift mode malfunction". The bulletin definition is used here. |
| P1710 | First Hold Switch Circuit Fault Stuck On | P | manufacturer | [C] | — | — |
| P1717 | AT — Gear Selection Malfunction | P | manufacturer | [C] | wiring; range position switch; ECM | — |
| P1730 | Problem in Shift Control System — Shift Solenoid Valve A and D Stuck OFF, Shift Solenoid Valve B Stuck ON, Shift Valves A, B, and D Stuck | P | manufacturer | [A] | transmission fluid; wiring (per ninjafix.in) | ninjafix.in variant wording: "AT — gear shift malfunction" |
| P1731 | Problem in Shift Control System — Shift Solenoid Valve E Stuck ON, Shift Valve E Stuck | P | manufacturer | [A] | transmission fluid; wiring; shift solenoid E; A/T clutch pressure control solenoid A; ECM (per ninjafix.in) | ninjafix.in variant wording: "AT — gear shift malfunction" |
| P1732 | A/T Clutch Pressure Control Solenoid Valve A Stuck OFF | P | manufacturer | [A] | — | ninjafix.in lists P1732 only as "Problem In Shift Control System" |
| P1733 | Problem in Shift Control System — Shift Solenoid Valve B and C Stuck ON, Shift Valves B and C Stuck | P | manufacturer | [A] | transmission fluid; wiring; shift solenoid D; A/T clutch pressure control solenoid C; ECM (per ninjafix.in) | ninjafix.in variant wording: "AT — gear shift malfunction" |
| P1734 | Problem in Shift Control System — Shift Solenoid Valve D Stuck ON, Shift Valve D Stuck | P | manufacturer | [A] | transmission fluid; wiring (per ninjafix.in) | ninjafix.in variant wording: "AT — gear shift malfunction" |
| P1738 | TCM 2nd Clutch Pressure Switch Circuit Malfunction | P | manufacturer | [C] | 2nd clutch pressure switch electrical connection loose (connector under the upper transmission mount, beneath the distributor area); faulty pressure switch; wiring fault | Check that the pressure-switch electrical connection is securely attached before replacing the sensor. CONFLICT: one technician source describes P1738 as a torque-converter-clutch system malfunction instead — reported, not resolved. |
| P1739 | Automatic Transmission System Malfunction (3rd clutch pressure switch circuit — pattern inference, flagged) | P | manufacturer | [C] | — | — |
| P1740 | Problem in 2nd Clutch Pressure Switch Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1740 as "AT — 4th clutch pressure switch" (wiring; range position switch; 4th clutch pressure switch; ECM). The Honda bulletin (A-grade) positional mapping gives 2nd clutch pressure switch circuit; the bulletin definition is used here. |
| P1750 | Problem in 3rd Clutch Pressure Switch Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1750 as "AT — hydraulic system mechanical malfunction" (wiring; shift solenoids; ECM; transmission mechanical fault). The Honda bulletin (A-grade) positional mapping gives 3rd clutch pressure switch circuit; the bulletin definition is used here. |
| P1751 | Problem in 4th Clutch Pressure Switch Circuit; Mechanical Problem in Hydraulic Control System of Shift Solenoid Valve B and A/T Clutch Pressure Control Solenoid Valves A and B | P | manufacturer | [A] | — | bulletin lists P1751 twice with two detection items (4th clutch pressure switch circuit; mechanical/hydraulic problem). CONFLICT: ninjafix.in lists P1751 as "AT — hydraulic system mechanical malfunction" only. |
| P1753 | TCM A/T Lock-Up Solenoid Valve A Fault | P | manufacturer | [C] | — | CONFLICT: the same code list also describes P1753 as "TCM A/T ECT Sensor Circuit Fault" — reported, not resolved; verify against the Honda service manual. |
| P1758 | TCM A/T Lock-Up Solenoid Valve B Fault | P | manufacturer | [C] | — | — |
| P1768 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1773 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1778 | Clutch Pressure Control Solenoid Valve 'C' Circuit | P | manufacturer | [C] | — | — |
| P1785 | Automatic Transaxle Concerns | P | manufacturer | [C] | — | — |
| P1786 | Automatic Transaxle Concerns | P | manufacturer | [C] | — | — |
| P1787 | Automatic Transmission Lock-Up Clutch Malfunction | P | manufacturer | [C] | — | — |
| P1788 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1790 | TCM A/T Throttle Position Sensor Circuit Fault | P | manufacturer | [C] | — | — |
| P1791 | TCM A/T Vehicle Speed Sensor Circuit Fault | P | manufacturer | [C] | — | — |
| P1792 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1793 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1794 | Automatic Transaxle Concerns | P | manufacturer | [B] | — | ninjafix.in variant (V6): "Automatic transmission — BARO signal" (wiring; ECM; TCM) |
| P1795 | Automatic Transmission System Malfunction | P | manufacturer | [C] | — | — |
| P1835 | AT — Kick-Down Switch | P | manufacturer | [C] | wiring; kick-down switch; ECM | — |
| P1850 | AT — Brake Band Solenoid Malfunction | P | manufacturer | [C] | AT trouble code(s) stored | — |
| P1860 | AT — Torque Converter Clutch (TCC) Solenoid Circuit | P | manufacturer | [C] | wiring; TCC solenoid; ECM | — |
| P1870 | Manifold Absolute Pressure Sensor Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1870 as "CVT — poor acceleration" (wiring; shift control linear solenoid; TCM); Honda DTC lists (troublecodes.net Honda list; freeautomechanic.com) list it only as "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here. (GM uses P1870 for transmission component slipping — different make, not applicable.) |
| P1873 | Problem in CVT Speed Change Control Valve Assembly Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1873 as "CVT — poor acceleration" (wiring; PH-PL control linear solenoid; TCM); Honda DTC lists give only "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here. |
| P1876 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve | — |
| P1877 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve | — |
| P1878 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; start clutch control linear solenoid; TCM | — |
| P1879 | Problem in CVT Pulley Pressure Control Valve Assembly Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1879 as "CVT — poor acceleration" (wiring; start clutch control linear solenoid; TCM); Honda DTC lists give only "Automatic Transaxle Concerns". The Honda bulletin (A-grade) definition is used here. |
| P1880 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; start clutch control linear solenoid; TCM | — |
| P1881 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; start clutch control linear solenoid; TCM | — |
| P1882 | Problem in CVT Start Clutch Pressure Control Valve Assembly Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1882 as "Constantly variable transmission (CVT)" (wiring; inhibitor solenoid; TCM). The Honda bulletin (A-grade) definition is used here. |
| P1884 | Problem in Inhibitor Solenoid Circuit | P | manufacturer | [A] | — | CONFLICT: ninjafix.in lists P1884 as "Secondary Gear Speed Sensor 2 Circuit Malfunction". The Honda bulletin (A-grade) definition is used here. |
| P1885 | Problem in CVT Drive Pulley Speed Sensor Circuit | P | manufacturer | [A] | faulty CVT drive pulley speed sensor; wiring fault between sensor and TCM | Honda advanced diagnostics: malfunction detected when drive pulley speed reads lower than the TCM-estimated value (factor 0.53 vs engine speed) for 15 seconds in D/L/R. One drive cycle, MIL on, D indicator blinks. CONFLICT (A-vs-A, recorded not resolved): Honda SB 03-020 [A] maps P1885 to 'Secondary Gear Speed Sensor 2 Circuit Malfunction' (Civic Hybrid). The Insight-CVT advanced-diagnostics mapping above ('Problem in CVT Drive Pulley Speed Sensor Circuit') is also [A]; likely model/generation-dependent. Verify per model. |
| P1886 | Problem in CVT Driven Pulley Speed Sensor Circuit (no signal) | P | manufacturer | [A] | faulty CVT driven pulley speed sensor; wiring fault | Honda advanced diagnostics: no signals from the driven pulley speed sensor for 15 seconds. Drive-pattern retest: hold 600+ RPM in D for 15 seconds, or steady 43-62 mph for 15 seconds. |
| P1888 | CVT Driven Pulley Speed Sensor Circuit | P | manufacturer | [A] | wiring; speed sensor 1; TCM (per ninjafix.in) | ninjafix.in variant wording: "CVT — poor acceleration" (speed sensor 1). Honda DTC lists give only "Automatic Transaxle Concerns". |
| P1889 | CVT Speed Sensor | P | manufacturer | [A] | wiring; speed sensor 2; TCM (per ninjafix.in) | ninjafix.in variant wording: "CVT — poor acceleration" (speed sensor 2) |
| P1890 | Problem in Shift Control System (CVT Speed Control System) | P | manufacturer | [A] | incorrect PCM learning value causing CVT pressure problem (2015-16 Accord/CR-V — Honda product update); CVT belt slip; drive/driven pulley pressure control solenoid fault | Honda product update (service bulletin 16-053, Aug 2016) for 2015-16 Accord and CR-V: incorrect learning value in the PCM can cause CVT belt slip at highway speeds (RPM surge) and set P1890. Repair: update PGM-FI software; if the DTC is already set, replace the transmission AND update software. One drive cycle, MIL on, D indicator blinks. CONFLICT (A-vs-A, recorded not resolved): Honda SB 03-020 [A] maps P1890 to 'Problem in CVT Speed Sensor 2 Circuit' (Civic Hybrid). The Insight-CVT advanced-diagnostics mapping above ('Problem in Shift Control System (CVT Speed Control System)') is also [A]; likely model/generation-dependent. Verify per model. |
| P1892 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P1893 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P1894 | Problem in Start Clutch System | P | manufacturer | [A] | solenoid valve failure; control line open/shorted; ground line open | Honda SB 03-020 detection item [A]. CONFLICT (model/generation-dependent, recorded not resolved): micro-tronik list [C] maps P1894 to 'CVT Drive Pulley Pressure Control Valve Malfunction' (TCM VBU input voltage < 6V for 2 seconds at engine start). SB 03-020 [A] is preferred. |
| P1895 | CVT Speed Change Control Valve Circuit | P | manufacturer | [A] | wiring; drive pulley pressure control valve; TCM (per ninjafix.in) | ninjafix.in variant wording: "CVT — poor acceleration" (drive pulley pressure control valve). The bulletin definition is used here. |
| P1896 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P1897 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P1898 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P1899 | CVT — Poor Acceleration | P | manufacturer | [C] | wiring; drive pulley pressure control valve; TCM | — |
| P2646 | "A" Rocker Arm Actuator System Performance / Stuck Off (Bank 1) | P | manufacturer | [B] | low or dirty engine oil (check FIRST — system is oil-pressure actuated); faulty VTEC/rocker-arm oil pressure switch; faulty rocker-arm oil control solenoid (VTEC solenoid); wiring/connector fault to switch or solenoid; outdated PCM software | Honda factory service bulletin (SB-10052884-2696, July 2013) for 2003-12 Accord L4, 2002-05 Civic Si, 2002-09 CR-V, 2011 CR-Z, 2003-11 Element, 2007-11 Fit: replace the VTEC oil pressure switch (P/N 37250-PNE-G01). Honda's own code meaning: "oil pressure switch circuit, low voltage". After repair, clear with scan tool and drive normally to confirm. |
| P2647 | "A" Rocker Arm Actuator System Stuck On (Bank 1) | P | manufacturer | [B] | faulty VTEC oil pressure switch (circuit high voltage); low/contaminated oil | Companion to P2646: P2646 = oil pressure switch circuit low voltage, P2647 = high voltage. Same TSB switch replacement (P/N 37250-PNE-G01) applies to 2003-05 Accord L4, 2003-05 Element, 2002-05 CR-V per Honda dealer tech guidance. |
| P2648 | "A" Rocker Arm Actuator Control Circuit Low | P | manufacturer | [C] | — | — |
| P2649 | "A" Rocker Arm Actuator Control Circuit High | P | manufacturer | [C] | — | — |
| SRS-1-1 | Open or high resistance in driver's airbag inflator | B | manufacturer | [B] | open in driver's airbag inflator circuit; faulty cable reel; faulty SRS unit | read via SCS connector short, count SRS light flashes; main-code 1-x = driver airbag inflator faults |
| SRS-1-2 | Open or high resistance in driver's airbag inflator | B | manufacturer | [B] | open in driver's airbag inflator circuit; faulty cable reel; faulty SRS unit | read via SCS connector short, count SRS light flashes; main-code 1-x = driver airbag inflator faults |
| SRS-1-3 | Short to another wire or low resistance in driver's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-1-4 | Short to power in driver's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-1-5 | Short to ground in driver's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-10-1 | SRS air bag deployed | B | manufacturer | [B] | airbag(s)/tensioner(s) deployed in a collision — SRS unit must be replaced after deployment | 1999–2002 Acura chart splits deployment codes: 10-1 seat belt pretensioner deployed; 10-2 driver's side air bag deployed; 10-3 pretensioner & driver's side air bag deployed; 10-4 passenger's side air bag deployed; 10-5 pretensioner & passenger's side air bag deployed; 10-6 driver & passenger air bags deployed; 10-7 all deployed. 2003–2011 charts use D1-11/F1-11 style deployment codes instead. |
| SRS-10-3 | Seat belt pretensioner and driver's side air bag deployed | B | manufacturer | [B] | airbag/tensioner deployed in a collision — SRS unit must be replaced | from the 1999–2002 Acura deployment sub-code split (see 10-1 notes); Honda 1988–2002 chart lists only 10-1 |
| SRS-11-1 | Open or high resistance in driver's side airbag module | B | manufacturer | [B] | — | main-code 11-x = driver's side airbag module faults (1999+ charts) |
| SRS-11-2 | Open or high resistance in driver's side airbag module | B | manufacturer | [B] | — | main-code 11-x = driver's side airbag module faults (1999+ charts) |
| SRS-11-3 | Short to another wire or low resistance in driver's side airbag module | B | manufacturer | [B] | — | — |
| SRS-11-4 | Short to power in driver's side airbag module | B | manufacturer | [B] | — | — |
| SRS-11-5 | Short to ground in driver's side airbag module | B | manufacturer | [B] | — | — |
| SRS-12-1 | Open or high resistance in front passenger's side airbag module | B | manufacturer | [B] | — | main-code 12-x = passenger's side airbag module faults (1999+ charts) |
| SRS-12-2 | Open or high resistance in front passenger's side airbag module | B | manufacturer | [B] | — | main-code 12-x = passenger's side airbag module faults (1999+ charts) |
| SRS-12-3 | Short to another wire or low resistance in passenger's side airbag module | B | manufacturer | [B] | — | — |
| SRS-12-4 | Short to power in passenger's side airbag module | B | manufacturer | [B] | — | — |
| SRS-12-5 | Short to ground in passenger's side airbag module | B | manufacturer | [B] | — | — |
| SRS-13-1 | Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts |
| SRS-13-2 | Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts |
| SRS-13-3 | Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts |
| SRS-13-4 | Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts |
| SRS-13-5 | Driver's side impact sensor faults — 13-1/13-2 faulty sensor or SRS unit; 13-3 no signal from sensor; 13-4 faulty power supply to sensor; 13-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts; exact sub-code wording varies slightly between the 1999–2002 and 2003–2011 charts |
| SRS-14-1 | Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts |
| SRS-14-2 | Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts |
| SRS-14-3 | Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts |
| SRS-14-4 | Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts |
| SRS-14-5 | Passenger's side impact sensor faults — 14-1/14-2 faulty sensor or SRS unit; 14-3 no signal / faulty floor harness; 14-4 faulty power supply to sensor; 14-5 faulty safing sensor | B | manufacturer | [B] | — | 1999+ charts |
| SRS-15-1 | Faulty OPDS unit (occupant position detection system) | B | manufacturer | [B] | — | 1999+ charts; some charts add "or OPDS not initialized" |
| SRS-15-2 | Faulty side airbag cutoff indicator circuit | B | manufacturer | [B] | — | — |
| SRS-15-3 | Faulty OPDS sensor | B | manufacturer | [B] | — | — |
| SRS-2-1 | Open in passenger's airbag inflator | B | manufacturer | [B] | — | main-code 2-x = passenger airbag inflator faults |
| SRS-2-2 | Open in passenger's airbag inflator | B | manufacturer | [B] | — | main-code 2-x = passenger airbag inflator faults |
| SRS-2-3 | Short to another wire or low resistance in passenger's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-2-4 | Short to power in passenger's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-2-5 | Short to ground in passenger's airbag inflator | B | manufacturer | [B] | — | — |
| SRS-21-1 | Driver's seat belt buckle tensioner faults — 21-1 open/high resistance; 21-3 short to another wire/low resistance; 21-4 short to ground; 21-5 short to power | B | manufacturer | [B] | — | 1999+ charts; the original poster of the honda-tech thread traced a 21-2 to a seat belt tensioner recall fix |
| SRS-21-3 | Driver's seat belt buckle tensioner faults — 21-1 open/high resistance; 21-3 short to another wire/low resistance; 21-4 short to ground; 21-5 short to power | B | manufacturer | [B] | — | 1999+ charts; the original poster of the honda-tech thread traced a 21-2 to a seat belt tensioner recall fix |
| SRS-21-4 | Driver's seat belt buckle tensioner faults — 21-1 open/high resistance; 21-3 short to another wire/low resistance; 21-4 short to ground; 21-5 short to power | B | manufacturer | [B] | — | 1999+ charts; the original poster of the honda-tech thread traced a 21-2 to a seat belt tensioner recall fix |
| SRS-21-5 | Driver's seat belt buckle tensioner faults — 21-1 open/high resistance; 21-3 short to another wire/low resistance; 21-4 short to ground; 21-5 short to power | B | manufacturer | [B] | — | 1999+ charts; the original poster of the honda-tech thread traced a 21-2 to a seat belt tensioner recall fix |
| SRS-22-1 | Passenger's seat belt buckle tensioner faults — 22-1 open/high resistance; 22-3 short to another wire/low resistance; 22-4 short to ground; 22-5 short to power | B | manufacturer | [B] | — | 1999+ charts |
| SRS-22-3 | Passenger's seat belt buckle tensioner faults — 22-1 open/high resistance; 22-3 short to another wire/low resistance; 22-4 short to ground; 22-5 short to power | B | manufacturer | [B] | — | 1999+ charts |
| SRS-22-4 | Passenger's seat belt buckle tensioner faults — 22-1 open/high resistance; 22-3 short to another wire/low resistance; 22-4 short to ground; 22-5 short to power | B | manufacturer | [B] | — | 1999+ charts |
| SRS-22-5 | Passenger's seat belt buckle tensioner faults — 22-1 open/high resistance; 22-3 short to another wire/low resistance; 22-4 short to ground; 22-5 short to power | B | manufacturer | [B] | — | 1999+ charts |
| SRS-3-1 | Open or high resistance in driver's seat belt tensioner | B | manufacturer | [B] | — | main-code 3-x = driver's seat belt tensioner faults |
| SRS-3-2 | Open or high resistance in driver's seat belt tensioner | B | manufacturer | [B] | — | main-code 3-x = driver's seat belt tensioner faults |
| SRS-3-3 | Short to another wire or low resistance in driver's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-3-4 | Short to power in driver's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-3-5 | Short to ground in driver's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-4-1 | Open or high resistance in front passenger's seat belt tensioner | B | manufacturer | [B] | — | main-code 4-x = front passenger's seat belt tensioner faults |
| SRS-4-2 | Open or high resistance in front passenger's seat belt tensioner | B | manufacturer | [B] | — | main-code 4-x = front passenger's seat belt tensioner faults |
| SRS-4-3 | Short to another wire or low resistance in passenger's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-4-4 | Short to power in passenger's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-4-5 | Short to ground in passenger's seat belt tensioner | B | manufacturer | [B] | — | — |
| SRS-9-1 | SRS failure or indicator light fault | B | manufacturer | [B] | — | 1999–2002 charts word this as "Intermittent SRS failures"; 2003–2011 Civic/CR-V chart: "SRS failure or indicator light" |
| SRS-9-2 | SRS unit internal failure of power supply | B | manufacturer | [B] | faulty SRS power supply | — |
| SRS-9-3 | Faulty driver's seat belt buckle switch | B | manufacturer | [B] | — | — |
| SRS-9-4 | Faulty passenger's seat belt buckle switch | B | manufacturer | [B] | — | — |
| SRS-9-6 | Faulty left-hand front impact sensor | B | manufacturer | [B] | — | 2003–2011 Civic/CR-V/Element/Ridgeline chart only; no 9-5 exists in any chart found — 9-x jumps from 9-4 to 9-6 |
| SRS-9-7 | Faulty right-hand front impact sensor | B | manufacturer | [B] | — | 2003–2011 Civic/CR-V/Element/Ridgeline chart only |
| U0155 | F-CAN Malfunction (Gauge Control Module - ECM/PCM) | U | manufacturer | [A] | open in F-CAN wiring between gauge control module and ECM/PCM (check continuity ECM connector A36/A37 to gauge 36P connector terminals 1/19); faulty gauge control module; poor connections/loose terminals | Honda's descriptor for U0155 is F-CAN-specific (not the generic "lost communication with IPC" text). Honda procedure: clear with HDS, recheck; jump the SCS line; continuity-check the CAN lines; substitute a known-good gauge control module. Remember the gauge module IS the F-CAN/B-CAN gateway on 2006-~2015 models — a dead gateway produces exactly this code plus an OBD-II link error. |
| U1207 | Electric A/C Compressor Not Available for Bus A | U | manufacturer | [B] | — | — |
| U1280 | B-CAN Communication Bus Line Error (BUS-OFF) | U | manufacturer | [A] | — | Honda DTC troubleshooting procedure: clear with HDS, cycle OFF→ON, wait 6+ seconds, recheck; if indicated, go to BCM DTC U1280 troubleshooting (intermittent otherwise). Flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight. |
| U1281 | Auto Light Control Unit Lost Communication with MICU (Body Control Module) | U | manufacturer | [B] | — | flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight |
| U128D | Auto Light Control Unit Lost Communication with MICU (Body Control Module) | U | manufacturer | [B] | — | listed alongside U1281 with near-identical wording in the Honda message; treated as listed |
| U1291 | BCM Lost Communication with Relay Control Module | U | manufacturer | [B] | — | flagged by American Honda TRS as an active-fault BCM DTC of interest on 2018–2020 Accord and 2019–2020 Insight |
| U129E | Body Control Module Not Available for Bus B | U | manufacturer | [B] | — | — |
| U12B4 | Park Pawl Actuator Driver Unit Not Available for Bus A | U | manufacturer | [B] | — | — |
| U1603 | Battery Condition Monitor Module Not Available for Bus A | U | manufacturer | [B] | — | — |
| U1604 | Motor Control Module (PCU) Not Available for Bus A | U | manufacturer | [B] | — | — |
| U1605 | Motor Control Module (PCU) Not Available for Bus A | U | manufacturer | [B] | — | — |
| VSA-11-19 | Right front wheel speed sensor malfunction | C | manufacturer | [C] | faulty wheel speed sensor; damaged wiring | CONFLICT: a 2006 Odyssey case reports 11-1 as a LEFT REAR wheel speed sensor fault — main-code wheel assignment varies by model/generation; do not generalize across models |
| VSA-13-19 | Left front wheel speed sensor malfunction | C | manufacturer | [C] | faulty wheel speed sensor; damaged wiring | model-specific; see 11-19 conflict note |
| VSA-54-3 | Relay 1 stuck on | C | manufacturer | [C] | faulty VSA relay | — |
| VSA-61-1 | Modulator control unit initial IG low voltage | C | manufacturer | [C] | low battery/system voltage; wiring | a 2012 Pilot case reports 61-11 alongside wheel-sensor codes with similar low-voltage context |
| VSA-86-1 | F-CAN bus-OFF malfunction | C | manufacturer | [C] | CAN wiring fault; faulty module pulling the bus down | — |

## hyundai — 440 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1101 | Battery Voltage High | B | manufacturer | [B] | — | reported in SRS, ESP/ABS, and MDPS module contexts — same code, module-dependent Corroborated (CONFIRMED): (multi-source agreement across community DTC databases) |
| B1102 | Battery Voltage Low | B | manufacturer | [A] | poor connection at SRSCM connector, wiring harness open or short, charging system fault, SRSCM internal fault (service manual) [A] | reported in SRS, ESP/ABS, and MDPS module contexts DTC sets when battery voltage stays at or below 9V for more than about 4 seconds; normal operating threshold 9–16V (service manual) [A] Corroborated (CONFIRMED): (Hyundai service manual) |
| B1200 | Humidity Sensor Open (High) | B | manufacturer | [B] | — | full-auto air conditioning (FATC) sensor family Corroborated (CONFIRMED): (multi-source database agreement) |
| B1201 | Humidity Sensor Short (Low) | B | manufacturer | [B] | — | — |
| B1202 | Heater Water Temperature Sensor Open (High) | B | manufacturer | [B] | — | FATC water temp sensor |
| B1203 | Heater Water Temperature Sensor Short (Low) | B | manufacturer | [B] | — | — |
| B1208 | Intake Potentiometer Open (Low) | B | manufacturer | [A] | — | AutoHex pages give detection threshold <0.1V for 0.3s with failsafe "FRE" (AutoHex) [A] Corroborated (CONFIRMED): (AutoHex service-info-derived DTC help) |
| B1209 | Intake Potentiometer Short (High) | B | manufacturer | [B] | — | — |
| B1220 | Vehicle Speed Sensor | B | manufacturer | [B] | — | body-CAN module context |
| B1233 | In-Car Temperature Sensor Short (Low) | B | manufacturer | [B] | — | — |
| B1234 | In-Car Temperature Sensor Open (High) | B | manufacturer | [A] | — | Corroborated (CONFIRMED): (Hyundai shop manuals via charm.li; AutoHex service-info-derived) |
| B1237 | Ambient Temperature Sensor Short (Low) | B | manufacturer | [B] | — | — |
| B1238 | Ambient Temperature Sensor Open (High) | B | manufacturer | [B] | automanual frames it as a break in the outdoor-temperature-controller wiring [B] | — |
| B1241 | Evaporator Sensor Short (Low) | B | manufacturer | [B] | — | — |
| B1242 | Evaporator Sensor Open (High) | B | manufacturer | [B] | — | — |
| B1245 | Air Mix Potentiometer Open (Low) - Driver | B | manufacturer | [B] | — | — |
| B1246 | Air Mix Potentiometer Short (High) - Driver | B | manufacturer | [B] | — | — |
| B1249 | Direction Potentiometer Open (Low) - Driver | B | manufacturer | [B] | — | — |
| B1250 | Direction Potentiometer Short (High) - Driver | B | manufacturer | [B] | — | — |
| B1257 | AQS Sensor Open (High) | B | manufacturer | [B] | — | AQS = air quality sensor |
| B1258 | AQS Sensor Short to Ground | B | manufacturer | [B] | — | — |
| B1259 | AQS Sensor Fault / Defective AQS Sensor | B | manufacturer | [B] | — | — |
| B1264 | Direction Potentiometer Open (Low)-VENT | B | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1265 | Direction Potentiometer Short (High)-VENT | B | manufacturer | [A] | — | . . . |
| B1266 | Direction Potentiometer Open (Low)-Floor | B | manufacturer | [A] | — | . . . |
| B1267 | Direction Potentiometer Short (High)-Floor | B | manufacturer | [A] | — | . . . |
| B1268 | Direction Potentiometer Open (Low)-Defog | B | manufacturer | [A] | — | . . . |
| B1269 | Direction Potentiometer Short (High)-Defog | B | manufacturer | [A] | — | . . . |
| B1301 | Steering Angle Signal Fault | B | manufacturer | [A] | — | body-CAN module context . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1302 | Gearbox Signal Fault-CAN Signal | B | manufacturer | [A] | — | . . . |
| B1303 | Accelerator Pedal Position Signal Error | B | manufacturer | [B] | — | — |
| B1304 | Engine Status Signal Error — wording variant, same meaning (avtotachki). | B | manufacturer | [B] | — | — |
| B1305 | Yaw rate sensor signal error — wording variant, same meaning (avtotachki). | B | manufacturer | [B] | — | — |
| B1306 | Brake pedal signal malfunction — wording variant, same meaning (avtotachki). | B | manufacturer | [B] | — | — |
| B1308 | Lamp Function Signal Fault | B | manufacturer | [A] | — | . . . |
| B1328 | FIS(Front Impact Sensor)-Driver Defect | B | manufacturer | [A] | poor connection at FIS connector, front impact sensor (driver) internal fault, SRSCM fault (MOHAVE/BORREGO service manual) [A] | SRS front impact sensor (driver) . . . Corroborated (CONFIRMED): (Hyundai service manuals) |
| B1329 | FIS(Front Impact Sensor)-Driver Communication error | B | manufacturer | [B] | poor connection, front impact sensor (driver) fault, SRSCM (JustAnswer quoting Hyundai service info) [B] | . . . |
| B1333 | FIS(Front Impact Sensor)-Passenger Defect | B | manufacturer | [A] | — | SRS front impact sensor (passenger) . . . Corroborated (CONFIRMED): (Hyundai TechNet Times / Restraint shop manual) |
| B1334 | FIS(FRONT IMPACT SENSOR)-PASSENGER COMMUNICATION ERROR | B | manufacturer | [A] | — | — |
| B1346 | Driver Airbag Resistance Too High (1st Stage) | B | manufacturer | [A] | open squib circuit; clockspring fault; connector fault | resistance faults are usually wiring/clockspring — check the clockspring and under-seat connectors before the airbag module DAB circuit resistance spec roughly 0.9–6.6/6.7 ohms (field guidance, JustAnswer) [B]; automanual lists B1346 [B] Corroborated (CONFIRMED): (AutoHex service-info-derived; Hyundai shop manuals via charm.li) |
| B1347 | Driver Airbag Resistance too Low (1st stage) | B | manufacturer | [A] | — | . . . |
| B1348 | Driver Airbag Resistance Circuit Short to Ground (1st stage) | B | manufacturer | [A] | — | Corroborated (CONFIRMED): (Hyundai Restraint shop manual) |
| B1349 | Driver Airbag resistance circuit short to Battery (1st stage) | B | manufacturer | [A] | — | . . . |
| B1352 | PAB RESISTANCE-HIGH | B | manufacturer | [A] | — | Corroborated (CONFIRMED): (Hyundai Restraint shop manual) |
| B1353 | Passenger Airbag Resistance too Low (1st stage) | B | manufacturer | [A] | — | — |
| B1354 | Passenger Airbag Resistance Circuit Short to Ground (1st stage) | B | manufacturer | [A] | — | — |
| B1355 | Passenger Airbag Resistance Circuit Short to Battery (1st stage) | B | manufacturer | [A] | — | — |
| B1361 | Pretensioner Front-Driver Resistance too High | B | manufacturer | [A] | — | . . . |
| B1362 | Pretensioner Front-Driver Resistance too Low | B | manufacturer | [A] | — | — |
| B1363 | Pretensioner Front-Driver Resistance Circuit Short to Ground | B | manufacturer | [A] | — | — |
| B1364 | Pretensioner Front-Driver Resistance Circuit Short to Battery | B | manufacturer | [A] | — | — |
| B1367 | Pretensioner Front-Passenger Resistance too High | B | manufacturer | [A] | automanual lists cause guidance for B1367 [B] | — |
| B1368 | Pretensioner Front-Passenger Resistance too Low | B | manufacturer | [A] | — | — |
| B1369 | Pretensioner Front-Passenger Resistance Circuit Short to Ground | B | manufacturer | [A] | — | — |
| B1370 | Pretensioner Front-Passenger Resistance Circuit Short to Battery | B | manufacturer | [A] | — | — |
| B1378 | Side Airbag Front-Driver Resistance too High | B | manufacturer | [A] | — | — |
| B1379 | Side Airbag Front-Driver Resistance too Low | B | manufacturer | [A] | — | — |
| B1380 | Side Airbag Front-Driver Resistance Circuit Short to Ground | B | manufacturer | [A] | — | — |
| B1381 | Side Airbag Front-Driver Resistance Circuit Short to Battery | B | manufacturer | [A] | — | — |
| B1382 | Side Airbag Front-Passenger Resistance too High | B | manufacturer | [A] | — | — |
| B1383 | Side Airbag Front-Passenger Resistance too Low | B | manufacturer | [A] | — | — |
| B1384 | Side Airbag Front-Passenger Resistance Circuit Short to Ground | B | manufacturer | [A] | — | — |
| B1385 | Side Airbag Front-Passenger Resistance Circuit Short to Battery | B | manufacturer | [A] | — | — |
| B1395 | Firing Loops Interconnection Fault | B | manufacturer | [A] | — | SRS firing loops cross-connected — wiring fault Corroborated (CONFIRMED): (Hyundai shop manuals via charm.li) |
| B1400 | SIDE IMPACT SENSOR FRONT-DRIVER DEFECT | B | manufacturer | [A] | — | SIS = side impact sensor Corroborated (CONFIRMED): (Hyundai shop manual via charm.li) |
| B1403 | SIDE IMPACT SENSOR FRONT-PASSENGER DEFECT | B | manufacturer | [A] | — | — |
| B1409 | SIDE IMPACT SENSOR FRONT-DRIVER COMMUNICATION ERROR | B | manufacturer | [A] | — | — |
| B1410 | SIDE IMPACT SENSOR FRONT-PASSENGER COMMUNICATION ERROR | B | manufacturer | [A] | — | — |
| B1473 | Inflatable Curtain Airbag Front-Driver Resistance Too High | B | manufacturer | [A] | — | Corroborated (CONFIRMED): (Hyundai shop manuals via charm.li) |
| B1474 | Inflatable Curtain Airbag Driver Resistance too Low | B | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1475 | Inflatable Curtain Airbag Driver Resistance Circuit Short to Ground | B | manufacturer | [A] | — | Database description is truncated; full text per TechNet Times is "...Resistance Circuit Short to Ground". |
| B1476 | Inflatable Curtain Airbag Driver/Front-Driver Resistance Circuit Short to Battery | B | manufacturer | [A] | — | Database description is truncated; full text per TechNet Times is "...Resistance Circuit Short to Battery". |
| B1477 | Inflatable Curtain Airbag Passenger Resistance too High | B | manufacturer | [A] | — | . . . |
| B1478 | Inflatable Curtain Airbag Passenger Resistance too Low | B | manufacturer | [A] | — | . . . |
| B1479 | Inflatable Curtain Airbag Passenger Resistance Circuit Short to Ground | B | manufacturer | [A] | — | Database description is truncated mid-word; full text per TechNet Times is "...Resistance Circuit Short to Ground". |
| B1480 | Inflatable Curtain Airbag Passenger Resistance Circuit Short to Battery | B | manufacturer | [A] | — | Database description is truncated mid-word; full text per TechNet Times is "...Resistance Circuit Short to Battery". |
| B1527 | Passenger airbag On/Off switch open or short to Battery | B | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1528 | Passenger airbag On/Off switch short or short to Ground | B | manufacturer | [A] | — | . . . |
| B1529 | Passenger airbag On/Off switch defect | B | manufacturer | [A] | — | . . . |
| B1530 | Passenger airbag On/Off switch instability | B | manufacturer | [A] | — | . . . |
| B1603 | CAN Communication Bus Off | B | manufacturer | [A] | — | body-CAN module context . . . TechNet Times shows C-CAN and B-CAN variants of B1603 (bus-off on either network). Module-scoping note: the same code also appears in AFLS/DBL headlamp tables. Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1620 | SRSCM Internal Failure | B | manufacturer | [A] | not documented (replacement of SRSCM is the documented remedy, not a cause) | SRS ECU internal fault . . . Multiple TechNet Times tables pair B1620 with "Internal fault-Replace SRSCM" guidance [A] Corroborated (CONFIRMED): (Hyundai TechNet Times; service-info-derived) |
| B1621 | ECU Hardware Error | B | manufacturer | [A] | — | Module-scoping note: other TechNet Times tables give B1621 as "SRSCM Hardware Fault", "ECU Check Sum Error", "ECU-Failure", or "Sensor Power Error Line ERROR" depending on module/model.. Module-scoping note: other TechNet Times tables give B1621 as "SRSCM Hardware Fault", "ECU Check Sum Error", "ECU-Failure", or "Sensor Power Error Line ERROR" depending on module/model.. Module-scoping note: other TechNet Times tables give B1621 as "SRSCM Hardware Fault", "ECU Check Sum Error", "ECU-Failure", or "Sensor Power Error Line ERROR" depending on module/model.. The database's "ECU Hardware Error" is valid for the SRSCM context; other modules reuse B1621 with different meanings — module context should be recorded with this code. Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1622 | ECU Software Error | B | manufacturer | [A] | — | . . . |
| B1636 | LIN Communication Error Fault | B | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1637 | B1637 "initial problem" — compatible (Hyundai AFLS training documentation, scribd "13-BH-AFLS" Genesis AFLS section; the code list places B1637 in the AFLS(LED) headlamp family). | B | manufacturer | [A] | — | module requires initialization/coding after replacement Corroborated (CONFIRMED): (Hyundai AFLS training/service documentation) |
| B1639 | LIN communication error DBL(Dynamic Bending Light) Left | B | manufacturer | [A] | — | adaptive headlamp LIN sub-bus . . . Pairs with B1640 "LIN communication error DBL(Dynamic Bending Light) Right" in the same TechNet Times table [A] Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1650 | Crash Recorded in 1st Stage Only(Frontal-Replace SRSCM) | B | manufacturer | [A] | DAB or PAB deployment event (AutoHex) [A]; crash event recorded (field reports) [B] | SRS ECU must be replaced after crash recording — it is a one-shot record . . . Remedy is SRSCM replacement (TechNet Times "Replace SRSCM"; Palisade diagnostic report with B1650:00-89 recommending SRSCM replacement; OBDSTAR blog "B1650:00-89 Crash recorded in 1st Stage Only Frontal") [A/B] Corroborated (CONFIRMED): (Hyundai TechNet Times; AutoHex service-info-derived) |
| B1651 | Crash Recorded in Front-Driver Side Airbag(Replace SRSCM) / Driver Side Airbag(DSAB) Crash Recorded | B | manufacturer | [A] | — | . . . Remedy is SRSCM replacement per TechNet Times [A] Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B1652 | Crash Recorded in Front-Passenger Side Airbag(Replace SRSCM) / Passenger Side Air Bag(PSAB) Crash Recorded | B | manufacturer | [A] | — | . . . Remedy is SRSCM replacement per TechNet Times [A] |
| B1655 | Crash Recorded (Side Airbag-Replace SRSCM) | B | manufacturer | [A] | — | . . . Remedy is SRSCM replacement per TechNet Times [A] |
| B1657 | Crash Recorded in Belt Pretensioner only / Crash Recorded-Belt Pretensioner(BPT) Only | B | manufacturer | [A] | — | . . . |
| B1658 | Belt Pretensioner 6 times Deployment | B | manufacturer | [A] | — | . . . |
| B1661 | B1661 "Parameter missing" | B | manufacturer | [A] | — | module variant coding missing — code the module with GDS Corroborated (CONFIRMED): (Hyundai AFLS training/service documentation) |
| B1905 | Sensor Power Supply Fault | B | manufacturer | [A] | — | parking-assist sensor supply Corroborated (CONFIRMED): (Hyundai shop manual via charm.li) |
| B1906 | Front Sensor PWM Signal Fault | B | manufacturer | [C] | — | This is a module-scoping conflict, not a flat contradiction: B1905/B1907/B1908 are corroborated in the AFLS front/rear-sensor context, but B1906 is defined as a rain-sensor fault in the FAM (front area module) context by all three second sources. Hyundai reuses B1906 across modules. The database description should be annotated with its module context (AFLS) rather than overwritten. CONFLICT (recorded, unresolved): carcarehacks, slideshare OBDCodex, and avtotachki all define B1906 as "Rain Sensor Fault 2" (FAM rain-sensor context), while the database says "Front Sensor PWM Signal Fault" (AFLS front-sensor context). carcarehacks Hyundai list, slideshare OBDCodex list, and avtotachki all give "B1906 Rain Sensor Fault 2". None of them corroborate "Front Sensor PWM Signal Fault" for B1906. Preferred: neither overwrites the other; both … |
| B1907 | Front sensor signal fault | B | manufacturer | [B] | — | — |
| B1908 | Rear sensor PWM signal fault | B | manufacturer | [B] | — | — |
| B2406 | Air Mix Motor (Driver) | B | manufacturer | [A] | poor electrical connection, wiring harness open or short, air-mix actuator fault, A/C control module fault (AutoHex) [A] | AutoHex detection condition: actuator does not reach the target position within ~40s [A]; hyundai-forums and a Hyundai service manual excerpt (4x4brasil PDF) discuss B2406 diagnosis [B] Corroborated (CONFIRMED): (AutoHex service-info-derived) |
| B2408 | Intake Motor | B | manufacturer | [A] | — | ru "Intake motor"; HVAC DTC list "B2408 DEFECTIVE INTAKE DOOR MOTOR").. ru "Intake motor"; HVAC DTC list "B2408 DEFECTIVE INTAKE DOOR MOTOR").. ru "Intake motor"; HVAC DTC list "B2408 DEFECTIVE INTAKE DOOR MOTOR").. Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B2417 | Direction Control Motor-Vent | B | manufacturer | [A] | — | plus).. plus).. plus).. Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| B2418 | Direction Control Motor-Floor | B | manufacturer | [A] | — | plus Hyundai DTC table).. plus Hyundai DTC table).. plus Hyundai DTC table).. |
| B2419 | Direction Control Motor-Defog | B | manufacturer | [A] | — | . . . |
| B2500 | Warning Lamp Failure | B | manufacturer | [A] | — | SRS warning lamp circuit . . . Corroborated (CONFIRMED): (Hyundai TechNet Times; automanual) |
| B2505 | Passenger airbag off warning lamp failure | B | manufacturer | [B] | — | Observed in the field with a -00 suffix variant (B250200) on Elantra [B] |
| C1101 | Battery Voltage High | C | manufacturer | [B] | — | reported in ESP/ABS and MDPS module contexts — same code, module-dependent Corroborated (CONFIRMED): (two independent community compilations agree; no service-info source located) |
| C1102 | Battery Voltage Low | C | manufacturer | [A] | — | reported in ESP/ABS and MDPS module contexts . . . Module-scoping note — one TechNet Times table gives C1102 as "ESP2 message timeout" (different module context). Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1103 | General voltage error in the ignition system | C | manufacturer | [B] | — | MDPS ignition voltage supply |
| C1121 | Sensor 1 Battery Voltage Low | C | manufacturer | [A] | depleted TPMS sensor battery | sensor battery is not replaceable separately — replace the sensor and relearn . . . Santa Fe shop manual specifies the low-voltage threshold as the wheel-electronics (WE) sensor battery below ~2.2 Vdc [A] Corroborated (CONFIRMED): (Hyundai shop manuals via charm.li) |
| C1122 | Right Front TPMS Sensor Battery Voltage Low | C | manufacturer | [C] | not documented (same class of causes as C1121 would apply, but not independently documented — treat as INFERRED) | com).. com).. com).. Mapping 2→FR is an extrapolation, not a documented fact. |
| C1123 | Left Rear TPMS Sensor Battery Voltage Low | C | manufacturer | [C] | — | Mapping 3→RL is an extrapolation, not a documented fact. |
| C1124 | Right Rear TPMS Sensor Battery Voltage Low | C | manufacturer | [C] | — | Mapping 4→RR is an extrapolation, not a documented fact. |
| C1126 | C112600 TPMS ECU Battery Voltage Low | C | manufacturer | [B] | — | TPMS module context The TPMS ECU monitors vehicle battery voltage; code sets on low voltage [B] |
| C1127 | C112700 TPMS ECU Battery Voltage High | C | manufacturer | [B] | — | TPMS module context |
| C1200 | Front-left wheel speed sensor circuit fault | C | manufacturer | [B] | — | — |
| C1201 | Front-left wheel speed sensor range/performance fault | C | manufacturer | [B] | — | — |
| C1202 | Front-left wheel speed sensor invalid/no signal | C | manufacturer | [B] | — | — |
| C1203 | Front-right wheel speed sensor circuit fault | C | manufacturer | [B] | — | — |
| C1204 | Front-right wheel speed sensor range/performance fault | C | manufacturer | [B] | — | — |
| C1205 | Front-right wheel speed sensor invalid/no signal | C | manufacturer | [B] | — | — |
| C1206 | Rear-left wheel speed sensor circuit fault | C | manufacturer | [B] | — | — |
| C1207 | Rear-left wheel speed sensor range/performance fault | C | manufacturer | [B] | — | — |
| C1208 | Rear-left wheel speed sensor invalid/no signal | C | manufacturer | [B] | — | — |
| C1209 | Rear-right wheel speed sensor circuit fault | C | manufacturer | [B] | — | — |
| C1210 | Rear-right wheel speed sensor range/performance fault | C | manufacturer | [B] | — | — |
| C1211 | Rear-right wheel speed sensor invalid/no signal | C | manufacturer | [B] | — | — |
| C1213 | Wheel Speed Frequency Error | C | manufacturer | [C] | wheel speed sensor fault, incorrect sensor installation or connection, tone-rotor / wheel-bearing mechanism fault (automanual) [B] | CONFLICT (recorded, unresolved): automanual defines C1213 as a failure or incorrect operation of the traction control controller (not a wheel-speed frequency error). automanual Hyundai error codes gives C1213 a traction-control-controller definition with the listed causes. Preferred: unresolved — the automanual entry is a reputable compilation but the database's "Wheel Speed Frequenc… |
| C1235 | Primary Pressure Sensor-Electrical | C | manufacturer | [A] | — | ESP brake pressure sensor . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1237 | Pressure Sensor - Other Fault | C | manufacturer | [C] | — | . . . The database wording looks like a mangled paraphrase of the TechNet Times entry; recommend aligning to "Primary Pressure Sensor - Signal Fault". CONFLICT (recorded, unresolved): TechNet Times lists C1237 as "Primary Pressure Sensor-Signal" (one table) — the database's "Pressure Sensor - Other Fault" drops "Primary" and replaces "Signal" with "Other Fault", which changes the meaning. TechNet Times lists "C1237 Primary Pressure Sensor-Signal". Preferred: TechNet Times (A-grade) — the database description should be corrected to match it. |
| C1259 | Steering angle sensor signal error | C | manufacturer | [A] | — | MDPS angle sensor Corroborated (CONFIRMED): (HMA technical service bulletin) |
| C1260 | Steering angle sensor (SAS) circuit signal fault | C | manufacturer | [A] | — | ESP steering angle sensor circuit Corroborated (CONFIRMED): (HMA TSB) |
| C1261 | Zero-setting error | C | manufacturer | [A] | — | perform steering angle sensor calibration with GDS after alignment or sensor replacement Zero-point calibration of the steering angle sensor not performed [A] Corroborated (CONFIRMED): (HMA TSB) |
| C1283 | Vehicle yaw controller malfunction — compatible (automanual). | C | manufacturer | [B] | yaw-rate sensor itself, its wiring, or the control block (automanual) [B] | — |
| C1290 | Torque sensor signal error | C | manufacturer | [A] | — | MDPS torque sensor automanual gives a divergent wording for C1290 (steering-angle-sensor damage); the HMA TSB (A-grade) is preferred and matches the database [A] Corroborated (CONFIRMED): (HMA TSB) |
| C1300 | TPMS ECU IRX not responding | C | manufacturer | [A] | — | . . . A second TechNet Times table variant reads "LF/RF External Interference Failure" (different context/variant) [A] Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1312 | RF Channel Fail (LF) | C | manufacturer | [A] | RF interference around the vehicle, SVM coaxial cable connection faults (TSB 23-BE-001H) [A] | . . . TSB specifies a minimum ~75% RF reception rate as the diagnostic criterion [A] Corroborated (CONFIRMED): (HMA TSB) |
| C1313 | RF Channel Fail (RF) | C | manufacturer | [A] | same as C1312 (TSB 23-BE-001H) [A] | . . . same ~75% reception-rate criterion [A] |
| C1314 | RF Channel Fail (LR) | C | manufacturer | [A] | same as C1312 (TSB 23-BE-001H) [A] | . . . same ~75% reception-rate criterion [A] |
| C1315 | RF Channel Fail (RR) | C | manufacturer | [A] | same as C1312 (TSB 23-BE-001H) [A] | . . . same ~75% reception-rate criterion [A] |
| C1322 | C132200 Front Left Sensor Over Temperature | C | manufacturer | [B] | — | — |
| C1503 | TCS/ESC(ESP) Switch Error | C | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1513 | Brake switch fault | C | manufacturer | [B] | brake light switch failure (automanual) [B] | hyundai-forums threads associate this code family with the Hyundai brake-switch recall covering April 2007–July 2011 builds [B] |
| C1603 | Derating (EPS Thermal Protection) | C | manufacturer | [C] | sustained high steering load; high ambient temperature | MDPS thermal protection — assist is reduced, not a hard fault; let the system cool and retest NOT FOUND in 8th-edition TechNet Times listing and no second source located via web search (recorded): description 'Derating (EPS Thermal Protection)' is single-source; kept at grade C. |
| C1604 | ECU Hardware Error | C | manufacturer | [C] | poor module connector contact; internal ECU fault | reported for EPS/MDPS units — check connector quality first; module replacement is the common fix, and in some cases reflashing the unit resolves it Caveat — the TSB table extraction is dense and the row mapping should be verified against the TSB PDF before editing the database. CONFLICT (recorded, unresolved): The HMA MDPS TSB lists "C1604 ECU over/discharge error" — the database's "ECU Hardware Error" is broader/different. HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C1604 ECU over/discharge error". Preferred: the TSB (A-grade) if the row mapping verifies; otherwise keep the database wording. Flag for PDF verification. |
| C1605 | CAN Hardware Error | C | manufacturer | [A] | — | ESP module CAN transceiver fault . . . One TechNet Times table variant reads "CAN Bus OFF" for C1605 (different context) [A] Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1611 | CAN time-out EMS | C | manufacturer | [B] | CAN wiring/connector fault; EMS module power fault | the EPS/ESP module is not receiving engine ECU messages on CAN — check wiring and connectors between the modules |
| C1612 | TCU signal error | C | manufacturer | [A] | — | Corroborated (CONFIRMED): (HMA TSB) |
| C1616 | CAN Bus Off | C | manufacturer | [B] | CAN line open or short; module re-initialization behavior (JustAnswer Tucson thread) [B] | reported in ESP and MDPS contexts A JustAnswer Tucson thread documents ~15 CAN re-initialization attempts before the code sets [B] |
| C1617 | EMS Invalid Engine Speed — compatible (fixya thread quoting Elantra XD TCS service-manual references: "C1617 EMS Invalid Engine Speed"). | C | manufacturer | [B] | — | MDPS received an implausible CAN value |
| C1623 | CAN time out SAS | C | manufacturer | [A] | — | Corroborated (CONFIRMED): (HMA TSB) |
| C1625 | CAN Time-Out ABS/ESP | C | manufacturer | [A] | — | . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C1626 | Implausible Control | C | manufacturer | [A] | — | ESP plausibility check failed . . . |
| C1643 | CAN Time-out Yaw Rate & G Sensor | C | manufacturer | [A] | — | Module-scoping note: another TechNet Times table gives C1643 as "Motor Current Excessive" (MDPS/EPS context).. Module-scoping note: another TechNet Times table gives C1643 as "Motor Current Excessive" (MDPS/EPS context).. Module-scoping note: another TechNet Times table gives C1643 as "Motor Current Excessive" (MDPS/EPS context).. The database description matches the ESC-context variant; record the module context with this code. |
| C1700 | Byte Coding Error | C | manufacturer | [A] | — | MDPS variant coding fault . . . Other TechNet Times tables give C1700 as "Parameter Error" / "Gear Shift Malfunction" (different module contexts) [A] |
| C1702 | Variant Coding Error | C | manufacturer | [C] | module replaced without coding; coding corrupted | code the module variant with GDS after replacement; also seen as a transmission-control-module CAN fault on some applications Corroborated (CONFIRMED): (keep; single community thread) |
| C1704 | ECU fail-safe relay fault | C | manufacturer | [A] | — | MDPS failsafe relay Corroborated (CONFIRMED): (HMA TSB) |
| C1705 | ECU Precharge Circuit Fault | C | manufacturer | [C] | — | Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database. CONFLICT (recorded, unresolved): The HMA MDPS TSB lists "C1705 ECU hardware error" — the database's "ECU Precharge Circuit Fault" is a different, more specific definition. HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C1705 ECU hardware error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification. |
| C2101 | Motor Relay / Motor Relay - Abnormal | C | manufacturer | [A] | — | MDPS motor relay . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C2112 | Valve Relay Error | C | manufacturer | [A] | open or short in the IGN+ power circuit to the valve relay | check the IGN+ feed to the ABS valve relay . . . |
| C2308 | Front Left(FL) Valve (In) / Front-LH Valve error (Inlet Valve) | C | manufacturer | [A] | — | ABS hydraulic valve . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C2312 | Front Left(FL) Valve (Out) / Front-LH Valve error (Outlet Valve) | C | manufacturer | [A] | — | . . . |
| C2316 | Front Right(FR) Valve (In) / Front-RH Valve error (Inlet Valve) | C | manufacturer | [A] | — | . . . |
| C2320 | Front Right(FR) Valve (Out) / Front-RH Valve error (Outlet Valve) | C | manufacturer | [A] | — | . . . |
| C2324 | Rear Left(RL) Valve (In) / Rear-LH Valve error (Inlet Valve) | C | manufacturer | [A] | — | . . . |
| C2328 | Rear Left(RL) Valve (Out) / Rear-LH Valve error (Outlet Valve) | C | manufacturer | [A] | — | . . . |
| C2332 | Rear Right(RR) Valve (In) / Rear-RH Valve error (Inlet Valve) | C | manufacturer | [A] | — | . . . |
| C2336 | Rear Right(RR) Valve (Out) / Rear-RH Valve error (Outlet Valve) | C | manufacturer | [A] | — | . . . |
| C2366 | TC Valve Primary (USV1) Error | C | manufacturer | [A] | — | ESP hydraulic unit valve . . . Module-scoping note — another TechNet Times table gives C2366 as "TC Front Left Valve" (different context) [A] Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C2370 | TC Valve Secondary (USV2) Error | C | manufacturer | [A] | — | . . . Another TechNet Times table gives C2370 as "TC Front Right Valve" (different context) [A] |
| C2372 | Electronic Shuttle Valve Primary (HSV1) Error | C | manufacturer | [A] | — | . . . |
| C2374 | Electronic Shuttle Valve Secondary (HSV2) Error | C | manufacturer | [A] | — | . . . |
| C2400 | Motor signal error — compatible (HMA TSB: "C2400 Motor signal error"; the database wording is broader). | C | manufacturer | [A] | — | MDPS motor Corroborated (CONFIRMED): (HMA TSB) |
| C2401 | Motor circuit error | C | manufacturer | [A] | — | Corroborated (CONFIRMED): (HMA TSB) |
| C2402 | Motor Electrical | C | manufacturer | [A] | traction control motor winding break; water ingress damaging the case | reported for the ESP traction-control motor — dismantle, clean brushes, check the case seal . . . Corroborated (CONFIRMED): (Hyundai TechNet Times) |
| C2412 | Motor Short or Open | C | manufacturer | [C] | — | MDPS motor circuit Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database. CONFLICT (recorded, unresolved): The HMA MDPS TSB lists "C2412 Motor voltage supply error" — the database's "Motor Short or Open" (with a YAML diagnostic note placing it in the MDPS motor circuit) is a different definition. HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C2412 Motor voltage supply error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification. |
| C2413 | Motor Current Fault | C | manufacturer | [C] | — | ). ). ). Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database. CONFLICT (recorded, unresolved): The HMA MDPS TSB lists "C2413 ECU hardware error" — the database's "Motor Current Fault" is a different definition. (Note: TechNet Times separately lists "C2414 Motor Current Fail (current excessive)" — a different code.) HMA TSB gives "C2413 ECU hardware error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification. # Network codes (Uxxx) |
| P1100 | MAP Sensor - Malfunction | P | manufacturer | [C] | — | Hyundai diesel-engine code family (P1100-P1159); code-to-description mapping follows the source list sequence — the source contains internal duplications, treat as [C] |
| P1101 | MAP Sensor - Abnormal | P | manufacturer | [C] | — | — |
| P1102 | MAP Sensor - Low Input | P | manufacturer | [C] | — | — |
| P1103 | MAP Sensor - High Input | P | manufacturer | [C] | — | — |
| P1104 | Air Flow Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1105 | Air Flow Sensor - Abnormal | P | manufacturer | [C] | — | — |
| P1106 | Air Flow Sensor - Low Input | P | manufacturer | [C] | — | — |
| P1107 | Air Flow Sensor - High Input | P | manufacturer | [C] | — | — |
| P1108 | Fuel Pump Circuit - Malfunction | P | manufacturer | [C] | — | — |
| P1110 | Fuel Pump - Stuck On | P | manufacturer | [C] | — | — |
| P1111 | ETS System - Malfunction | P | manufacturer | [C] | — | ETS = Electronic Throttle System (Hyundai diesel) |
| P1112 | Fuel Pump - Electrical Fault | P | manufacturer | [C] | — | — |
| P1113 | Manifold Differential Pressure Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1114 | VGT Actuator - Malfunction | P | manufacturer | [C] | — | VGT = variable geometry turbo (diesel) |
| P1115 | Manifold Differential Pressure Sensor - Abnormal | P | manufacturer | [C] | — | — |
| P1116 | Manifold Differential Pressure Sensor - Low Input | P | manufacturer | [C] | — | — |
| P1118 | Coolant Temperature Input - Abnormal | P | manufacturer | [C] | — | — |
| P1119 | Boost Pressure Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1120 | ETS Motor - Malfunction | P | manufacturer | [C] | — | — |
| P1121 | Inlet Metering Valve Control - Malfunction | P | manufacturer | [C] | — | — |
| P1122 | Electric Governor - Malfunction | P | manufacturer | [C] | — | diesel injection pump governor |
| P1123 | Inlet Metering Valve - Malfunction | P | manufacturer | [C] | — | — |
| P1124 | APS PWM Output Circuit - Malfunction | P | manufacturer | [C] | — | APS = accelerator position sensor |
| P1125 | Throttle Position Input - Abnormal | P | manufacturer | [C] | — | — |
| P1126 | Fuel Pressure Sensor 2 - Malfunction | P | manufacturer | [C] | — | explicit code-description pairing in source (more reliable than the P1100-P1125 sequential mapping) |
| P1127 | Fuel System Rich - Part Load | P | manufacturer | [C] | — | source also pairs P1127 with "Control Sleeve Position Sensor" — conflicting pairing reported, not resolved |
| P1128 | Fuel System Lean - Part Load | P | manufacturer | [C] | — | — |
| P1130 | Start Solenoid - Malfunction | P | manufacturer | [C] | — | — |
| P1131 | Injection Quantity Adjust - Malfunction | P | manufacturer | [C] | — | — |
| P1134 | O2 Sensor Transition Time (Bank 1 Sensor 1) - Malfunction | P | manufacturer | [C] | — | — |
| P1135 | Injection Timing Servo - Malfunction | P | manufacturer | [C] | — | — |
| P1140 | Inlet Air Temperature Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1141 | Slow Duty Solenoid - Malfunction | P | manufacturer | [C] | — | — |
| P1145 | Main Duty Solenoid - Malfunction | P | manufacturer | [C] | — | — |
| P1146 | Idle CO Potentiometer - Malfunction | P | manufacturer | [C] | — | — |
| P1147 | Accelerator Position Sensor (ETS) Circuit - Malfunction | P | manufacturer | [C] | — | — |
| P1150 | Barometric Pressure Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1151 | Accelerator Position Sensor (EMS) Circuit - Malfunction | P | manufacturer | [C] | — | — |
| P1152 | Accelerator Position Circuit - Low Input | P | manufacturer | [C] | — | — |
| P1153 | Accelerator Position Circuit - High Input | P | manufacturer | [C] | — | — |
| P1154 | O2 Sensor Transition Time (Bank 2 Sensor 1) - Malfunction | P | manufacturer | [C] | — | — |
| P1155 | Limp Home Valve - Malfunction | P | manufacturer | [C] | — | — |
| P1159 | Variable Induction System - Malfunction | P | manufacturer | [C] | — | — |
| P1162 | High Pressure Pump & Fuel Line - Malfunction | P | manufacturer | [C] | — | diesel high-pressure fuel system |
| P1166 | O2 Sensor (Bank 1) Control Adaptation at Limit | P | manufacturer | [C] | — | source lists "O2s (B1) Control Adaptation" and "Limit O2s Lambda Control (B1)" for P1166 — same fault, two wordings |
| P1167 | O2 Sensor (Bank 2) Control Adaptation at Limit | P | manufacturer | [C] | — | source lists "O2s (B2) Control Adaptation" and "Limit O2s Lambda Control (B2)" — same fault, two wordings |
| P1168 | O2 Sensor (Bank 1 Sensor 2) Heater Power - Malfunction | P | manufacturer | [C] | — | — |
| P1169 | O2 Sensor (Bank 2 Sensor 2) Heater Power - Malfunction | P | manufacturer | [C] | — | — |
| P1170 | ECM Barometric Pressure Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1171 | ETS Valve Stuck - Open | P | manufacturer | [C] | carbon buildup on throttle plate; faulty ETS motor; wiring fault | clean throttle plate/bore/pivot points first; check connector and harness; throttle body replacement is the common fix (field guidance for the Hyundai ETS family) |
| P1172 | ETS Improper Motor Current | P | manufacturer | [C] | faulty ETS motor; wiring fault | — |
| P1173 | ETS Target Following Malfunction | P | manufacturer | [C] | — | — |
| P1174 | ETS Valve Stuck - Close #1 | P | manufacturer | [C] | — | — |
| P1175 | ETS Valve Stuck - Close #2 | P | manufacturer | [C] | — | — |
| P1176 | ETS Motor Open/Short #1 | P | manufacturer | [C] | — | — |
| P1177 | ETS Motor Open/Short #2 | P | manufacturer | [C] | — | — |
| P1178 | ETS Motor Power - Open | P | manufacturer | [C] | — | — |
| P1179 | ETS Position Feedback Mismatch | P | manufacturer | [C] | — | — |
| P1180 | Fuel Pressure Regulator - Malfunction | P | manufacturer | [C] | — | source pairs P1180 with both "O2 S1 Heater Circuit - Malfunction" and "Fuel Pressure Regulator - Malfunction" — conflicting pairing reported, not resolved; fuel-pressure meaning applies to diesel applications |
| P1181 | Fuel Pressure Monitoring - Malfunction | P | manufacturer | [C] | — | — |
| P1182 | Fuel Pressure Regulator - Short | P | manufacturer | [C] | — | source pairs P1182 with both "O2 S2 Heater Circuit - Malfunction" and "Fuel Pressure Regulator - Short" — conflicting pairing reported, not resolved |
| P1183 | Fuel Pressure Regulator - Open | P | manufacturer | [C] | — | — |
| P1184 | Fuel Pressure Regulator - Power Fault | P | manufacturer | [C] | — | source pairs P1184 with both "O2s No Activity (B1/S2)" and "Fuel Pressure Regulator - Power" — conflicting pairing reported, not resolved |
| P1185 | Fuel Position - Excessive | P | manufacturer | [C] | — | — |
| P1186 | Fuel Pressure - Too Low | P | manufacturer | [B] | clogged fuel filter; fuel pressure sensor or rail pressure sensor fault; damaged sensor wiring/connectors; clogged in-tank pump screen | common on Hyundai/Kia diesels (e.g. Tucson diesel); monitor live fuel pressure with a scan tool — if readings are inconsistent after pump/filter replacement, inspect the sensor harness, then replace the sensor |
| P1187 | Fuel Pressure Regulator Valve - Stuck | P | manufacturer | [C] | regulator valve stuck open or closed; wiring fault | valve stuck in open or closed position per source |
| P1188 | Fuel Pressure - Leakage | P | manufacturer | [C] | — | — |
| P1189 | Governor Deviation | P | manufacturer | [C] | — | — |
| P1190 | Intake Throttle Actuator - Malfunction | P | manufacturer | [C] | — | — |
| P1191 | ETS Limp Home Valve On | P | manufacturer | [C] | — | — |
| P1192 | Limp Home - Target Follow Malfunction | P | manufacturer | [C] | — | — |
| P1193 | ETS Limp Home - Low RPM | P | manufacturer | [C] | — | — |
| P1194 | Limp Home - TPS2 Position Malfunction | P | manufacturer | [C] | — | — |
| P1195 | Limp Home - Target Follow Delay | P | manufacturer | [C] | — | — |
| P1196 | ETS Limp Home - Close Stuck | P | manufacturer | [C] | — | — |
| P1295 | Electronic Throttle Control System Malfunction - Power Management | P | manufacturer | [B] | faulty TPS; TPS harness open/shorted; poor TPS circuit connection; faulty MAF or MAP sensor; faulty PCM/ECM | sets when power management mode is recognized (1 driving cycle, MIL on). If P0638/P0685/P1295/P2106 appear together, check the main relay for an open fault first. If P1295 + P2106 together, check ETC items (TPS, ETC motor); if P1295 + P2104, check APS plus ETC items |
| P1300 | Spark Timing Adjust Signal - Malfunction | P | manufacturer | [C] | — | — |
| P1301 | Injector Specific Data Fault | P | manufacturer | [C] | — | — |
| P1302 | Synchronization Error - CKP/CMP | P | manufacturer | [C] | — | — |
| P1303 | TDC Sensor - Abnormal | P | manufacturer | [C] | — | — |
| P1304 | TDC Sensor - Low Input | P | manufacturer | [C] | — | — |
| P1305 | TDC Sensor - High Input | P | manufacturer | [C] | — | — |
| P1306 | Phase Sensor - Malfunction | P | manufacturer | [C] | — | — |
| P1307 | Phase Sensor - Abnormal | P | manufacturer | [C] | — | — |
| P1308 | Phase Sensor - Low Input | P | manufacturer | [C] | — | — |
| P1309 | Phase Sensor - High Input | P | manufacturer | [C] | — | — |
| P1310 | Ignition Coil 1 - Low Output | P | manufacturer | [A] | — | — |
| P1311 | Ignition Coil 1 - High Output | P | manufacturer | [A] | — | — |
| P1312 | Ignition Coil 2 - Malfunction | P | manufacturer | [A] | — | — |
| P1313 | Ignition Coil 2 - Abnormal | P | manufacturer | [A] | — | — |
| P1314 | Ignition Coil 2 - Low Output | P | manufacturer | [A] | — | — |
| P1315 | Ignition Coil 2 - High Output | P | manufacturer | [A] | — | — |
| P1316 | Ignition Coil 3 - Malfunction | P | manufacturer | [A] | — | — |
| P1317 | Ignition Coil 3 - Abnormal | P | manufacturer | [A] | — | — |
| P1318 | Ignition Coil 3 - Low Output | P | manufacturer | [A] | — | — |
| P1319 | Ignition Coil 3 - High Output | P | manufacturer | [A] | — | — |
| P1320 | Ignition Coil 4 - Malfunction | P | manufacturer | [A] | — | — |
| P1321 | Ignition Coil 4 - Abnormal | P | manufacturer | [A] | — | source also pairs P1321 with "Glow Indicator Lamp - Short" — conflicting pairing reported, not resolved (gasoline vs diesel application) |
| P1322 | Ignition Coil 4 - Low Output | P | manufacturer | [A] | — | source also pairs P1322 with "Glow Indicator Lamp - Open" — conflicting pairing reported, not resolved |
| P1323 | Ignition Coil 4 - High Output | P | manufacturer | [A] | — | — |
| P1324 | Glow Relay - Malfunction | P | manufacturer | [C] | — | diesel glow system |
| P1325 | Glow Relay - Abnormal | P | manufacturer | [C] | — | — |
| P1326 | Glow Relay - Stuck On / Short | P | manufacturer | [C] | — | source lists both "Stuck On" and "Short" wordings |
| P1327 | Glow Relay - Electrical / Open | P | manufacturer | [C] | — | source lists both "Electrical" and "Open" wordings |
| P1330 | Spark Timing Adjust Signal - Malfunction | P | manufacturer | [A] | — | — |
| P1331 | Misfire Detection MF Signal Line #1 - Short | P | manufacturer | [C] | — | MF = misfire detection signal line per cylinder |
| P1332 | Misfire Detection MF Signal Line #2 - Short | P | manufacturer | [C] | — | — |
| P1333 | Misfire Detection MF Signal Line #3 - Short | P | manufacturer | [C] | — | — |
| P1334 | Misfire Detection MF Signal Line #4 - Short | P | manufacturer | [C] | — | — |
| P1335 | Misfire Detection MF Signal Line #5 - Short | P | manufacturer | [C] | — | — |
| P1336 | Misfire Detection MF Signal Line #6 - Short | P | manufacturer | [C] | — | — |
| P1337 | Misfire Detection MF Signal Line #7 - Short | P | manufacturer | [C] | — | — |
| P1338 | Misfire Detection MF Signal Line #8 - Short | P | manufacturer | [C] | — | — |
| P1340 | IFS 2 - Open | P | manufacturer | [C] | — | — |
| P1341 | Ion Sensing Line #1 - Open | P | manufacturer | [C] | — | — |
| P1342 | Ion Sensing Line #2 - Open | P | manufacturer | [C] | — | — |
| P1343 | Ion Sensing Line #3 - Open | P | manufacturer | [C] | — | — |
| P1344 | Ion Sensing Line #4 - Open | P | manufacturer | [C] | — | — |
| P1345 | Ion Sensing Line #5 - Open | P | manufacturer | [C] | — | — |
| P1346 | Ion Sensing Line #6 - Open | P | manufacturer | [C] | — | — |
| P1347 | Ion Sensing Line #7 - Open | P | manufacturer | [C] | — | — |
| P1348 | Ion Sensing Line #8 - Open | P | manufacturer | [C] | — | — |
| P1351 | Misfire Detection MF Signal Line #1 - Open | P | manufacturer | [C] | — | — |
| P1352 | Misfire Detection MF Signal Line #2 - Open | P | manufacturer | [C] | — | — |
| P1353 | Misfire Detection MF Signal Line #3 - Open | P | manufacturer | [C] | — | — |
| P1354 | Misfire Detection MF Signal Line #4 - Open | P | manufacturer | [C] | — | — |
| P1355 | Misfire Detection MF Signal Line #5 - Open | P | manufacturer | [C] | — | — |
| P1372 | Segment Time Incorrect / Segment Time Acquisition Incorrect | P | manufacturer | [A] | — | crankshaft segment timing used by misfire monitor |
| P1386 | Knock Sensor Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1400 | Manifold Differential Pressure Sensor - Malfunction | P | manufacturer | [A] | — | — |
| P1401 | DMTL Performance / DMTL Motor Circuit Malfunction | P | manufacturer | [A] | DMTL pump/motor failure; wiring or connector fault | CONFLICT — TechNet lists DMTL (Diagnostic Module Tank Leakage) meanings, but field reports on early models (2002 Accent) describe P1401 as an EGR system fault (clogged EGR valve, vacuum leaks). Meaning is application/year-dependent; verify against the specific model |
| P1402 | DMTL Motor Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1403 | DMTL Valve Circuit / DMTL Motor Circuit - Malfunction | P | manufacturer | [A] | — | source lists both valve-circuit and motor-circuit wordings |
| P1404 | DMTL Heater Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1405 | EGR Temperature Incorrect | P | manufacturer | [A] | — | — |
| P1406 | Exhaust Gas Temperature Not Plausible (Calculated vs Simulated) | P | manufacturer | [A] | — | — |
| P1415 | Secondary Air Injection Insufficient (Bank 1) | P | manufacturer | [A] | — | — |
| P1416 | Secondary Air Injection - Malfunction / Insufficient Flow (Bank 1) | P | manufacturer | [A] | — | source lists both wordings |
| P1418 | Secondary Air Injection Insufficient (Bank 2) | P | manufacturer | [A] | — | — |
| P1419 | Secondary Air Injection Valve - Malfunction | P | manufacturer | [A] | — | — |
| P1440 | Evaporative System - Vent Circuit Malfunction | P | manufacturer | [A] | — | — |
| P1443 | Evaporative Emission Control System - Leak Detected / Tank Cap Missing | P | manufacturer | [A] | loose or missing fuel cap; EVAP leak | check fuel cap first — the "tank cap missing" variant is the quick win |
| P1458 | A/C Compressor Input Signal - Malfunction | P | manufacturer | [A] | — | — |
| P1500 | Air Conditioning Switch Signal / Vehicle Speed Sensor Signal Circuit - Malfunction | P | manufacturer | [A] | — | CONFLICT — TechNet lists both "Air Conditioning (A/C) Switch" and "Vehicle Speed Sensor Signal Circuit Malfunction" for P1500; application-dependent |
| P1501 | Brake Switch Signal / Battery Temperature Too High | P | manufacturer | [A] | — | CONFLICT — TechNet lists both meanings; application-dependent |
| P1502 | Wheel Speed Sensor Circuit / Vehicle Speed Sensor Signal Circuit / Battery Not Charging | P | manufacturer | [A] | — | CONFLICT — three distinct meanings listed in TechNet; application-dependent |
| P1503 | Accelerator Switch Signal / Cruise Control Malfunction (Control Switch) | P | manufacturer | [A] | — | CONFLICT — two meanings listed; application-dependent |
| P1504 | Inhibitor Switch Signal / Cruise Control Malfunction (Cancel) | P | manufacturer | [A] | — | CONFLICT — two meanings listed; application-dependent |
| P1505 | Idle Speed Control Actuator Signal Low (Coil #1) | P | manufacturer | [A] | — | — |
| P1506 | Idle Speed Control Actuator Signal High (Coil #1) | P | manufacturer | [A] | — | — |
| P1507 | Idle Speed Control Actuator Signal Low (Coil #2) | P | manufacturer | [A] | — | — |
| P1508 | Idle Speed Control Actuator Signal High (Coil #2) | P | manufacturer | [A] | — | — |
| P1509 | MPS - High Input | P | manufacturer | [A] | — | — |
| P1510 | Idle Speed Control Circuit Open/Short | P | manufacturer | [A] | — | TechNet lists several ISC-circuit variants (opening coil high, circuit 1-high, coil 1 signal incorrect, LPG switch line) — application-dependent |
| P1511 | Idle Speed Control Circuit Open/Short | P | manufacturer | [A] | — | source lists "ISC Circuit Open/Short" and "Idle Speed Control Actuator Circuit 1-Low"; application-dependent |
| P1512 | Engine Coolant Temperature Sensor - Low Input | P | manufacturer | [A] | — | — |
| P1513 | ISC Actuator (Open) / Idle Air Control Valve Opening Coil Signal Low | P | manufacturer | [A] | — | multiple ISC-circuit wordings in TechNet; application-dependent |
| P1514 | Oil Temperature Sensor - Malfunction | P | manufacturer | [A] | — | — |
| P1515 | Oil Temperature Sensor - Abnormal / Idle Speed Control Actuator Circuit 1-Low | P | manufacturer | [A] | — | CONFLICT — TechNet lists oil-temperature and ISC-actuator meanings; application-dependent |
| P1516 | Oil Temperature Sensor - Low / Idle Speed Control Actuator Circuit 2-High | P | manufacturer | [A] | — | CONFLICT — TechNet lists oil-temperature and ISC-actuator meanings; application-dependent |
| P1517 | Oil Temperature Sensor - High Input | P | manufacturer | [A] | — | — |
| P1520 | Generator FR Terminal / Alternator Charging Signal - Malfunction | P | manufacturer | [A] | — | source lists both wordings |
| P1521 | Power Steering Switch / Power Steering Pressure Sensor Circuit - Malfunction | P | manufacturer | [A] | — | source lists switch and pressure-sensor wordings |
| P1522 | Sensor Supply Voltage 1 - Low Input | P | manufacturer | [A] | — | — |
| P1523 | ETC Throttle Position Sensor Position Reset Malfunction / Sensor Supply Voltage 1 - High Input | P | manufacturer | [A] | — | CONFLICT — TechNet lists ETC and supply-voltage meanings; one variant notes "not emissions related, service aid only" |
| P1524 | Sensor Supply Voltage 2 - Low Input | P | manufacturer | [A] | — | — |
| P1525 | APS/Boost Pressure Sensor Power / Sensor Supply Voltage 2 - High Input | P | manufacturer | [A] | — | source lists both wordings |
| P1526 | Sensor Supply Voltage 1 - Malfunction | P | manufacturer | [A] | — | — |
| P1527 | Sensor Supply Voltage 2 - Malfunction | P | manufacturer | [A] | — | — |
| P1529 | TCM MIL On Request Signal / Transmission Control System MIL Request | P | manufacturer | [A] | — | — |
| P1530 | Maximum Vehicle Speed Limiting - Malfunction | P | manufacturer | [A] | — | — |
| P1533 | VICS Solenoid Valve 2 Circuit - Malfunction | P | manufacturer | [A] | — | VICS = variable induction control system |
| P1539 | LPI Gas Injection System / IFB ECU - Malfunction | P | manufacturer | [A] | — | LPI = liquid propane injection (Korean domestic market); IFB = interface box |
| P1540 | LPI Gas System - Malfunction / Check IFB ECU | P | manufacturer | [A] | — | — |
| P1545 | A/C Compressor Switch Open/Short | P | manufacturer | [A] | — | — |
| P1550 | Knock Sensor Evaluation IC Error | P | manufacturer | [A] | — | internal ECM knock-evaluation circuit |
| P1552 | ISC Actuator (Close) - Short / Idle Speed Control Actuator Circuit 2-High | P | manufacturer | [A] | — | source lists both wordings |
| P1553 | ISC Actuator (Close) - Open / Idle Speed Control Actuator Circuit 2-Low | P | manufacturer | [A] | — | source lists both wordings |
| P1555 | Idle CO Potentiometer Open/Short | P | manufacturer | [A] | — | — |
| P1560 | Knock Control Serial Port Interface Check (Bank 1) | P | manufacturer | [A] | — | — |
| P1566 | Analog Battery Sensor Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1569 | Fuel Pressure Control Valve Current - Abnormal | P | manufacturer | [A] | — | — |
| P1572 | Cruise Control System - Vehicle Speed Lower Than Target Speed | P | manufacturer | [A] | — | — |
| P1573 | Cruise Control System - Vehicle Speed Too Low | P | manufacturer | [A] | — | — |
| P1586 | MT/AT Encoding Signal Error | P | manufacturer | [A] | — | — |
| P1593 | VICS Solenoid Valve 1 Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1600 | Serial Communication Malfunction (with A/T) / Serial Communication Problem with TCM | P | manufacturer | [A] | — | — |
| P1601 | ECU 'L' Line - Malfunction | P | manufacturer | [A] | — | — |
| P1602 | Serial Communication Problem - TCM / CAN Communication No Signal | P | manufacturer | [A] | — | source lists both serial and CAN wordings — era-dependent |
| P1603 | ECM-TCS/TCU Communication Line - Malfunction / CAN Bus Off | P | manufacturer | [A] | — | multiple wordings (ECM-TCS line, ECU-TCU line, CAN-bus-off) — era-dependent |
| P1604 | Lost Communication with ECM/PCM 'A' (C-CAN) / CAN Bus Off / No ID From ECU | P | manufacturer | [A] | — | — |
| P1605 | Internal Control Module ROM Error (IFB) / Acceleration Sensor Malfunction | P | manufacturer | [A] | — | CONFLICT — two distinct meanings listed; application-dependent |
| P1606 | Vacuum Solenoid Valve Abnormal / Chassis Acceleration Sensor Signal Malfunction | P | manufacturer | [A] | — | CONFLICT — two distinct meanings listed; application-dependent |
| P1607 | Serial Communication Problem with IFB ECU (Timeout) / ECM-ETS Communication Line Malfunction | P | manufacturer | [A] | — | source lists both wordings; application-dependent |
| P1608 | Vacuum Solenoid Valve Electrical / ECM-ETS Communication Line Malfunction | P | manufacturer | [A] | — | CONFLICT — two distinct meanings listed; application-dependent |
| P1609 | Immobilizer Communication - Malfunction | P | manufacturer | [A] | — | SMARTRA immobilizer system |
| P1610 | Non-Immobilizer EMS Connected to an Immobilizer / Immobilizer-SMARTRA Error | P | manufacturer | [A] | — | — |
| P1611 | Ventilation Solenoid Valve Stuck On / ECM-TCM MIL Request Line - Malfunction | P | manufacturer | [A] | — | CONFLICT — EVAP-ventilation and MIL-request meanings listed; application-dependent |
| P1612 | Ventilation Solenoid Valve - Electrical Fault | P | manufacturer | [A] | — | — |
| P1613 | ECM - Malfunction / ECM-ETS Communication Line Malfunction / MIL Request Circuit High | P | manufacturer | [A] | — | multiple wordings — ECM internal fault vs ETS communication line; diagnose per the specific variant the vehicle reports |
| P1614 | ETS ECM Malfunction / ETS ECU Malfunction (EEPROM R/W) | P | manufacturer | [A] | — | — |
| P1615 | P/N Relay - Malfunction / ETS Communication (ETS-EMS) Malfunction | P | manufacturer | [A] | — | CONFLICT — two distinct meanings listed; application-dependent |
| P1616 | Main Relay - Malfunction / Main Relay Control Circuit Malfunction | P | manufacturer | [A] | open main relay; relay control circuit fault | an open main relay with the engine running can set P0638/P0685/P1295/P2106 together — check the relay before chasing throttle codes |
| P1617 | Malfunction Indicator Lamp Power Stage - Malfunction | P | manufacturer | [A] | — | — |
| P1619 | Main Relay - Malfunction | P | manufacturer | [A] | — | — |
| P161B | ECM Torque Calculation Performance | P | manufacturer | [A] | low battery charge; faulty TCM; TCM software; TCM harness open/short; poor TCM circuit connection | seen paired with P1295 on Santa Fe field reports; address TCM-side faults first |
| P1620 | A/C Cut Relay / A/C Compressor Relay - Malfunction | P | manufacturer | [A] | — | source lists cut-relay, compressor-relay-short, and relay open/short wordings |
| P1621 | Fuel Cut Valve - Malfunction / A/C Compressor Relay Circuit Open or Short | P | manufacturer | [A] | — | CONFLICT — two distinct meanings listed; application-dependent |
| P1622 | A/C Control Circuit Fail / A/C Compressor Relay Circuit Malfunction | P | manufacturer | [A] | — | source lists both wordings |
| P1623 | Diagnostic Lamp / MIL Control Circuit / Cooling Fan Relay Circuit - Malfunction | P | manufacturer | [A] | — | multiple wordings; application-dependent |
| P1624 | Cooling Fan Relay (Low) Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1625 | Cooling Fan Relay (High) Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1628 | Vapor Lamp - Malfunction | P | manufacturer | [A] | — | — |
| P1629 | Condenser Fan Relay (High) Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1630 | CAN Bus Off / TCU Communication Line Malfunction | P | manufacturer | [A] | — | source lists CAN-bus-off and TCU-line wordings |
| P1631 | CAN Timeout ECM / Lost Communication with ECM/PCM 'A' (C-CAN) | P | manufacturer | [A] | — | source lists timeout and lost-communication wordings |
| P1632 | CAN Bus Off / ECU-TCS Communication Line Malfunction | P | manufacturer | [A] | — | source lists both wordings |
| P1633 | Battery Overcharge | P | manufacturer | [A] | — | — |
| P1634 | Auxiliary Heater Relay Short or Open | P | manufacturer | [A] | — | — |
| P1635 | Water Heater Relay - Malfunction | P | manufacturer | [A] | — | — |
| P1636 | Voltage Regulator for Injector - Malfunction | P | manufacturer | [A] | — | diesel injector supply voltage |
| P1638 | ECM (Microcontroller) - Malfunction | P | manufacturer | [A] | — | — |
| P1639 | ECM (Monitoring ADC) - Malfunction | P | manufacturer | [A] | — | internal ECM monitoring-circuit fault |
| P1640 | Variable Intake Motor 1 (VIM 1) Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1641 | Variable Intake Motor 2 (VIM 2) Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1642 | Non-Immobilizer ECM Equipped / Immobilizer-BCM Mismatch | P | manufacturer | [A] | — | — |
| P1645 | Booster Voltage - Operating Injector | P | manufacturer | [A] | — | diesel injector booster voltage circuit |
| P1646 | Booster Voltage - Too High | P | manufacturer | [A] | — | — |
| P1647 | Booster Voltage - Too Low | P | manufacturer | [A] | — | — |
| P1650 | Malfunction Indicator Lamp Control Circuit - Malfunction | P | manufacturer | [A] | — | — |
| P1652 | Ignition Switch - Malfunction | P | manufacturer | [A] | — | — |
| P1653 | Error Check After Ignition Off - Malfunction | P | manufacturer | [A] | — | — |
| P1655 | Unused Power Stage B - Malfunction | P | manufacturer | [A] | — | — |
| P1657 | Unused Power Stage C - Malfunction | P | manufacturer | [A] | — | — |
| P1660 | Cruise Control Switch - Malfunction | P | manufacturer | [A] | — | — |
| P1661 | Cruise Control Indicator Lamp - Malfunction | P | manufacturer | [A] | — | — |
| P1670 | Invalid Injector IQA/C2I Data | P | manufacturer | [A] | — | — |
| P1671 | Injector Classification Write Error | P | manufacturer | [A] | — | — |
| P1672 | Fan Relay Malfunction - Low Speed | P | manufacturer | [A] | — | — |
| P1678 | Immobilizer-EMS No Request (EMS Data Line Open) | P | manufacturer | [A] | — | immobilizer data line open — no immobilizer fitted |
| P1679 | Cooling Fan Control 3 Circuit Low / EMS Data Fail | P | manufacturer | [A] | — | CONFLICT — fan-control and EMS-data-fail meanings listed; application-dependent |
| P1688 | Immobilizer Lock | P | manufacturer | [A] | — | — |
| P1689 | Immobilizer - Unregistered Transponder | P | manufacturer | [A] | — | — |
| P1690 | SMARTRA No Response / Immobilizer-SMARTRA No Response | P | manufacturer | [A] | — | — |
| P1691 | Immobilizer Antenna Coil Error | P | manufacturer | [A] | — | — |
| P1692 | Immobilizer Indicator Lamp Error | P | manufacturer | [A] | — | — |
| P1693 | Transponder No Response / Invalid Response | P | manufacturer | [A] | — | — |
| P1694 | EMS Message Error | P | manufacturer | [A] | — | immobilizer-EMS communication message fault |
| P1695 | EMS Memory Error | P | manufacturer | [A] | — | — |
| P1696 | Immobilizer Authentication Fail | P | manufacturer | [A] | — | — |
| P1697 | Hi-Scan Message Error | P | manufacturer | [A] | — | Hi-Scan = Hyundai dealer scan tool (predecessor of GDS) |
| P1698 | Immobilizer Invalid Transponder / Key ID Not Valid | P | manufacturer | [A] | — | — |
| P1699 | Immobilizer - Twice Overtrial | P | manufacturer | [A] | — | — |
| P169A | Immobilizer SMARTRA Authentication Fail | P | manufacturer | [A] | — | — |
| P1700 | Gear Shift Malfunction | P | manufacturer | [A] | — | Hyundai-specific transmission code (not the generic P1700 meaning) |
| P1701 | Throttle Position Sensor (TPS) - Malfunction | P | manufacturer | [A] | — | Hyundai-specific TPS code in the P17xx block |
| P1702 | Throttle Position Sensor (TPS) - Abnormal / Malfunction Adjustment | P | manufacturer | [A] | — | source lists abnormal and adjustment wordings |
| P1703 | Throttle Position Sensor (TPS) - Open/Short | P | manufacturer | [A] | — | source lists "Open/Short (GND)" and "Open or Short" wordings |
| P1704 | Throttle Position Sensor (TPS) - High Input / Short | P | manufacturer | [A] | — | source lists high-input, open-or-short, and short wordings |
| P1706 | Inhibitor Switch - Malfunction | P | manufacturer | [A] | — | transmission range/inhibitor switch |
| P1739 | Transmission Shift Solenoid - Malfunction | P | manufacturer | [C] | shift solenoid fault; ABS wheel speed sensor/wiring fault affecting gear selection | reported on 2008 Kia Sorento with ESC light faults and high-gear starts; inspect ABS wheel speed sensors and wiring — ESC/ABS faults can affect gear selection on this platform |
| U0001 | High-speed CAN communication bus off | U | manufacturer | [A] | CAN wiring short; faulty module pulling the bus down; module power/ground fault | disconnect modules one at a time to isolate a bus-killing module; a single shorted module takes down the whole C-CAN Bus-off condition persisting for ~2 seconds (AutoHex) [A] Corroborated (CONFIRMED): (AutoHex service-info-derived) |
| U1111 | Damage to the battery sensor — compatible (automanual: U1111 indicates battery-sensor damage; the battery warning indicator may illuminate). | U | manufacturer | [B] | battery sensor (battery current/voltage/temperature sensor) fault [B] | battery sensor (IBS) on the negative terminal — check sensor and LIN wiring |
| U1112 | LIN communication error | U | manufacturer | [A] | open or short in the LIN communication line; LIN-communicated modules (battery sensor, etc.); ECM (AutoHex detecting-condition tables) [A] | No corroboration, correction, or conflict to report. Recommend keeping grade [C] and treating the description as single-source.. No corroboration, correction, or conflict to report. Recommend keeping grade [C] and treating the description as single-source.. No corroboration, correction, or conflict to report. Recommend keeping grade [C] and treating the description as single-source.. AutoHex gives enable conditions (IG ON, battery 10–16V / ~11V, engine run time) and diagnosis times of 1–5s depending on model; no MIL [A] Corroborated (CONFIRMED): (AutoHex service-info-derived) |

## mazda — 40 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1041 | Adaptive Front Lighting System (AFS) control module | B | manufacturer | [C] | — | SkyActiv-era code with :54 suffix seen (B1041:54). |
| B1238 | EHPAS control module | B | manufacturer | [B] | — | EHPAS = electro-hydraulic power assist steering (Mazda3 BK era). See also B1342/B2141/B2477 (module/configuration) and C1099/C1278/C1956. |
| B1251 | Cabin temperature sensor | B | manufacturer | [B] | — | HVAC DTCs from the Mazda3 workshop manual table. |
| B1253 | Cabin temperature sensor | B | manufacturer | [B] | — | HVAC DTCs from the Mazda3 workshop manual table. |
| B1260 | Solar radiation sensor | B | manufacturer | [B] | — | HVAC DTCs; B1261 appears in owner Q&A as a real stored code. |
| B1261 | Solar radiation sensor | B | manufacturer | [B] | — | HVAC DTCs; B1261 appears in owner Q&A as a real stored code. |
| B1274 | Airflow mode actuator (potentiometer) | B | manufacturer | [B] | — | HVAC DTCs. |
| B1275 | Airflow mode actuator (potentiometer) | B | manufacturer | [B] | — | HVAC DTCs. |
| B1282 | Air mix actuator (potentiometer) | B | manufacturer | [B] | — | HVAC DTCs. See also B2832/B2834 (motor lock). |
| B1317 | Battery power supply | B | manufacturer | [B] | low/high system voltage to the module | Voltage codes; check charging system before module faults. |
| B1318 | Battery power supply | B | manufacturer | [B] | low/high system voltage to the module | Voltage codes; check charging system before module faults. |
| B1342 | EHPAS control module (internal malfunction) | B | manufacturer | [B] | — | Mazda3 workshop manual cross-references B1342 with C1267/C1730 under DSC. |
| B1352 | Ignition power supply | B | manufacturer | [B] | — | — |
| B2141 | EHPAS control module configuration | B | manufacturer | [B] | module not configured / configuration mismatch | Configuration codes — set after module replacement without coding. |
| B2477 | EHPAS control module configuration | B | manufacturer | [B] | module not configured / configuration mismatch | Configuration codes — set after module replacement without coding. |
| C0061 | DSC HU/CM | C | manufacturer | [C] | — | SkyActiv-era code with :54 suffix seen (C0061:54). |
| C1001 | Forward Sensing Camera (FSC) | C | manufacturer | [C] | — | Seen as C1001:92 and C1001:97 (ADAS camera). |
| C1099 | Electric power steering oil pump (motor) | C | manufacturer | [B] | — | EHPAS pump motor circuit (Mazda3 BK era). |
| C1278 | P/S angle sensor | C | manufacturer | [B] | — | Power-steering angle sensor codes. |
| C1956 | P/S angle sensor | C | manufacturer | [B] | — | Power-steering angle sensor codes. |
| P0126 | Insufficient coolant temperature for stable operation | P | manufacturer | [B] | failsafe thermostat stuck open (coolant infiltration of the dry cavity in the Coolant Control Valve integrated thermostat) | Mazda-specific pattern failure: the engine fails to reach operating temperature. Mazda issued a chain of TSBs (#01-011/21, #01-013/22, #01-005/23, #01-005/24, #01-001/26) and Special Service Program SSP D8 extended the warranty to 15 years/150,000 miles (2018–2025 CX-5, 2019–2023 Mazda3, 2019–2022 CX-3, 2018–2021 Mazda6, 2020–2023 CX-30). Fix is an updated dummy-plug kit plus PCM software update — check dealer VIN coverage before paying. |
| P1000 | OBD II Monitor Testing Not Completed | P | manufacturer | [B] | — | Set when drive cycles are incomplete; not a fault. |
| P1001 | Unable to Achieve Self-Test Function or SCP Error | P | manufacturer | [B] | SCP network fault (Ford era) | Ford-era self-test code; SCP = the J1850 PWM network. |
| P1100 | Mass Airflow Sensor Circuit Intermittent | P | manufacturer | [C] | — | — |
| P1101 | Mass Airflow Sensor Circuit out of Self-Test Range | P | manufacturer | [C] | — | KOEO/KOER self-test-era code. |
| P1116 | ECT Sensor Circuit Out of Self Test Range | P | manufacturer | [C] | — | — |
| P1120 | Throttle Position Sensor out of Range Low | P | manufacturer | [C] | — | — |
| P1131 | HO2S Bank 1 Sensor 1 Signal Below 0.45v (A/F Ratio Too Lean) | P | manufacturer | [C] | — | — |
| P1260 | THEFT Detected, Vehicle Immobilized (Anti-Theft System Signal Detected — Engine Disabled) | P | manufacturer | [B] | unprogrammed/incorrect key; PCM replaced without immobilizer programming | Seen as an archived (inactive) code on the engine ECU via generic scanners. Immobilizer programming after PCM replacement requires M-MDS/IDS — dealer-tool territory. Do not attempt key workarounds. |
| P2006 | Intake Manifold Runner Control Stuck Closed | P | manufacturer | [C] | — | Listed in the Mazda3 OBD code chart; IMRC actuator. |
| U0073 | CAN bus communication error | U | manufacturer | [B] | CAN wiring fault; module pulling the bus down | Listed in the Mazda3 workshop manual DTC table. |
| U0100 | Lost communication with the PCM | U | manufacturer | [B] | PCM power/ground; HS-CAN wiring | Listed in the Mazda3 workshop manual DTC table. |
| U0140 | CAN communication system (lost communication with body modules) | U | manufacturer | [B] | — | HVAC-section U-codes from the Mazda3 workshop manual — body/MS-CAN module communication losses. |
| U0155 | CAN communication system (lost communication with body modules) | U | manufacturer | [B] | — | HVAC-section U-codes from the Mazda3 workshop manual — body/MS-CAN module communication losses. |
| U0184 | CAN communication system (lost communication with body modules) | U | manufacturer | [B] | — | HVAC-section U-codes from the Mazda3 workshop manual — body/MS-CAN module communication losses. |
| U0415 | Invalid data received from MRCC/SBS (Mazda Radar Cruise Control / Smart Brake Support) | U | manufacturer | [C] | — | Seen as U0415:00 / U0420:00 in the MNAO M-Tip. |
| U0420 | Invalid data received from MRCC/SBS (Mazda Radar Cruise Control / Smart Brake Support) | U | manufacturer | [C] | — | Seen as U0415:00 / U0420:00 in the MNAO M-Tip. |
| U0516 | CAN communication system (lost communication with body modules) | U | manufacturer | [B] | — | HVAC-section U-codes from the Mazda3 workshop manual — body/MS-CAN module communication losses. |
| U2023 | Fault received from other modules | U | manufacturer | [B] | — | Listed in the Mazda3 workshop manual DTC table. |
| U300A | Electric Parking Brake (EPB) — control module | U | manufacturer | [C] | — | Seen as U300A:62. |

## mercedes — 126 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1000 | HRA headlamp range adjustment — control unit supply voltage too low (undervoltage) | B | manufacturer | [B] | low vehicle battery voltage; wiring to control unit; defective control unit | — |
| B1004 | LCP lower control panel — control unit does not match vehicle type | B | manufacturer | [B] | incorrect control unit installed (part-number mismatch) | Coding/variant mismatch — verify part number against VIN. |
| B1056 | Automatic air conditioning — problem in CAN communication with control unit DCM-RL | B | manufacturer | [B] | CAN wiring/connections; defective DCM-RL | — |
| B1128 | Heater core temperature sensor (B10/1) | B | manufacturer | [C] | — | AAC (automatic air conditioning) sensor family — see B1226–B1235. NOTE: one community list prints "B1128 Heater core temperature (B10/1)" while another prints "B1229 Heater core temperature (B10/1)" — transcription conflict, flagged [?]. |
| B1201 | Electric seat adjustment front left — hall sensor front height (M27m3) | B | manufacturer | [B] | faulty hall sensor; wiring | — |
| B1213 | Seat memory installed — exterior right rearview mirror voltage faulty | B | manufacturer | [B] | mirror actuator/wiring | One community list prints B1213 as LEFT mirror and B1214 as RIGHT; another prints both as right — transcription conflict, flagged [?]. |
| B1214 | Seat memory installed — exterior right rearview mirror voltage faulty | B | manufacturer | [B] | mirror actuator/wiring | See B1213 left/right conflict note. |
| B1226 | In-car temperature sensor (B10/4) | B | manufacturer | [C] | — | AAC sensor family. |
| B1227 | Outside temperature indicator temperature sensor | B | manufacturer | [C] | — | AAC sensor family. |
| B1229 | Heater core temperature sensor (B10/1) | B | manufacturer | [C] | — | See B1128 transcription conflict. |
| B1230 | Evaporator temperature sensor (B10/6) | B | manufacturer | [C] | — | AAC sensor family. |
| B1231 | ECT sensor (B11/4) | B | manufacturer | [C] | — | AAC sensor family. |
| B1232 | Refrigerant pressure sensor (B12) | B | manufacturer | [C] | — | AAC sensor family. |
| B1233 | Refrigerant temperature sensor (B12/1) | B | manufacturer | [C] | — | AAC sensor family. |
| B1234 | Sun sensor (B32) | B | manufacturer | [C] | — | AAC sensor family. |
| B1235 | Emissions sensor (B31) | B | manufacturer | [C] | — | AAC sensor family. |
| B1241 | Refrigerant fill | B | manufacturer | [C] | — | AAC — refrigerant charge issue. |
| B1246 | PTS Parktronic — A42b1 (left outer sensor, front bumper) | B | manufacturer | [C] | — | Parktronic sensor fault. |
| B1310 | Left/window airbag sensor defective | B | manufacturer | [C] | — | SRS component — follow standard airbag safety practice (battery disconnect, wait before probing). |
| B1315 | Front passenger child seat recognition problem | B | manufacturer | [C] | — | Occupant-classification system. |
| B1416 | Coolant circulation pump (M13) | B | manufacturer | [C] | — | AAC actuator family — see B1417–B1425. |
| B1417 | Duovalve (Y21y1), left | B | manufacturer | [C] | — | AAC actuator family. |
| B1418 | Duovalve (Y21y2), right | B | manufacturer | [C] | — | AAC actuator family. |
| B1419 | Electromagnetic clutch (A9k1) | B | manufacturer | [C] | — | AAC actuator family. |
| B1420 | Idle speed increase | B | manufacturer | [C] | — | AAC actuator family. |
| B1421 | Pulse module (N05) | B | manufacturer | [C] | — | AAC actuator family. |
| B1422 | Series interface (K1) connection to instrument cluster (A1) | B | manufacturer | [C] | — | AAC actuator family. |
| B1423 | Switchover valve block (Y11) | B | manufacturer | [C] | — | AAC actuator family. |
| B1424 | Activated charcoal filter actuator (A32m2) open | B | manufacturer | [C] | — | AAC actuator family. |
| B1425 | Activated charcoal filter actuator (A32m2) closed | B | manufacturer | [C] | — | AAC actuator family. |
| B1432 | Non-USA DTC | B | manufacturer | [C] | — | Market-variant code — not applicable to US vehicles. |
| B1459 | Series interface (K2) connection to instrument cluster (A1) | B | manufacturer | [C] | — | — |
| B1462 | Wide open throttle (WOT) position signal — diesel engines | B | manufacturer | [C] | — | Diesel models. |
| B1476 | Airbag malfunction indicator and warning lamp defective | B | manufacturer | [C] | — | SRS telltale circuit. |
| B1481 | HRA — part E2m1 (right headlamp range adjustment motor) short to ground | B | manufacturer | [C] | — | See B1489/B1492 for open/short-to-positive variants. |
| B1489 | HRA — part E2m1 (right headlamp range adjustment motor) open or short to positive | B | manufacturer | [C] | — | See B1481. |
| B1492 | HRA — part E1m1 (left headlamp range adjustment motor) short to positive | B | manufacturer | [C] | — | See B1481. |
| B1703 | Intermittent no-start in AAM — immobilizer module | B | manufacturer | [B] | all-activity module (AAM) / immobilizer circuit | Immobilizer-adjacent code documented at DTC-description level only. |
| B1729 | PSE pneumatic system door lock control module (A37) | B | manufacturer | [C] | — | Pneumatic central locking. |
| B1736 | Navigation system's CD player — check general CD / CD data block | B | manufacturer | [C] | — | Infotainment. |
| B1768 | Faulty open data flap limit switch (front flap) | B | manufacturer | [C] | — | — |
| B1773 | HRA — zero position programming not yet carried out or not possible | B | manufacturer | [C] | programming incomplete; mechanical fault | Requires headlamp-range zero-position programming (XENTRY). |
| B1850 | Electric seat adjustment front right — CAN communication interrupted with DCM | B | manufacturer | [C] | CAN wiring; door control module | — |
| C1000 | Control unit N47-5 (ESP and BAS control module) is defective | C | manufacturer | [A] | not documented (one DAS print variant phrases C1000 as "Check power supply of component N47-5" — flagged variant) | CONFLICT — a community code list labels C1000 "Traction System Control Module" [C]; the DAS text is preferred. |
| C1001 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1002 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1003 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1004 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1005 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1006 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1007 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1008 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1009 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100A | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100B | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100C | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100D | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100E | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C100F | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1010 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. Community variant: "Battery voltage low" — CONFLICT with DAS (see C1001–C1013 range). Low voltage causes cascading CAN faults — always check supply voltage first. |
| C1011 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. Community variant: "ASR/ETS/ESP circuit open or shorted" — CONFLICT with DAS (see C1001–C1013 range). |
| C1012 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. Community variant: "Battery voltage high" — CONFLICT with DAS (see C1001–C1013 range). An ML320 owner report independently shows "C1012 - ESP and BAS Control Module Is Faulty" from dealer/indie scans [C] — a third variant; meaning is model-dependent, verify per model. |
| C1013 | Control unit N47-5 (ESP and BAS control module) is defective (each code in range) | C | manufacturer | [A] | — | CONFLICT — a community list assigns C1010 "Battery Voltage Low", C1011 "ASR/ETS/ESP Circuit Open or Shorted", C1012 "Battery Voltage High" [C]; the DAS texts are preferred per model. |
| C1014 | Y10 (SPS solenoid valve) — electrical fault | C | manufacturer | [A] | — | Speed-sensitive power steering solenoid. |
| C1018 | Short circuit in the voltage supply of sensors B34 (ESP brake pressure sensor) and A7/7b1 (BAS diaphragm travel sensor) | C | manufacturer | [A] | — | — |
| C1020 | Fault or defect in CAN communication | C | manufacturer | [A] | — | CONFLICT — community list labels C1020 "CAN Communication Fault" (consistent) [C]. |
| C1021 | CAN communication with EA/CC/ISC control module interrupted | C | manufacturer | [C] | — | — |
| C1024 | CAN communication with engine control module interrupted | C | manufacturer | [C] | — | — |
| C1025 | CAN communication — BAS communication with ESP control unit faulty | C | manufacturer | [C] | — | — |
| C1035 | Signal from component N49 (steering angle sensor) is faulty | C | manufacturer | [A] | — | — |
| C1037 | Fault in CAN communication with component B24/15 (rotary speed and lateral acceleration sensor) | C | manufacturer | [A] | — | — |
| C1038 | Engine control module not identified, or incorrect control module | C | manufacturer | [A] | — | Module-identification/coding mismatch. |
| C1040 | Fault in CAN communication with component B24/15 (rotary speed and lateral acceleration sensor) | C | manufacturer | [A] | — | See C1037. |
| C1046 | Fault or defect in CAN communication | C | manufacturer | [A] | — | See C1020. |
| C1047 | Vehicle version — coding is faulty | C | manufacturer | [A] | — | Variant-coding mismatch — recode with XENTRY (SCN path for module replacement). |
| C1100 | Left front axle VSS circuit fault | C | manufacturer | [C] | wheel speed sensor; wiring; tone ring | — |
| C1101 | Right front axle VSS circuit fault | C | manufacturer | [C] | wheel speed sensor; wiring; tone ring | — |
| C1102 | ETS/ASR, ABS left axle VSS circuit fault | C | manufacturer | [C] | wheel speed sensor; wiring; tone ring | — |
| C1103 | Right rear axle VSS circuit fault | C | manufacturer | [C] | wheel speed sensor; wiring; tone ring | — |
| C1121 | AIRmatic — fault in component B24/3 (acceleration sensor) | C | manufacturer | [C] | — | CONFLICT — one community list prints B22/3 (level sensor) for C1121 [C]; component attribution flagged [?]. |
| C1122 | AIRmatic — fault in component B24/4 (acceleration sensor) | C | manufacturer | [C] | — | CONFLICT — one list prints B22/4 (level sensor) for C1122 [C]; flagged [?]. |
| C1123 | AIRmatic — fault in component B24/6 (acceleration sensor) | C | manufacturer | [C] | — | CONFLICT — one list prints B22/6 (level sensor) for C1123 [C]; flagged [?]. |
| C1132 | AIRmatic — fault in component B22/8 (level sensor) | C | manufacturer | [C] | — | — |
| C1133 | AIRmatic — fault in component B22/9 (level sensor) | C | manufacturer | [C] | — | — |
| C1135 | AIRmatic — fault in component B22/3 (level sensor) | C | manufacturer | [C] | — | — |
| C1140 | Steering angle sensor not initialized | C | manufacturer | [B] | sensor replacement / battery disconnect without initialization | Seen as Intermittent on a real 2001 W203 scan. Initialize the steering angle sensor, then clear. |
| C1141 | Brake pressure sensor B34 (brake master cylinder) | C | manufacturer | [C] | — | Seen on a 2000 ML320 with dealer + independent scans (owner report). |
| C1142 | ABS lateral acceleration sensor open/shorted | C | manufacturer | [C] | sensor; wiring | — |
| C1144 | AIRmatic — fault in component B7 (pressure sensor) | C | manufacturer | [C] | — | — |
| C1185 | Faulty BAS diaphragm travel sensor unit | C | manufacturer | [C] | — | — |
| C1200 | Brake light switch (open/shorted/implausible) | C | manufacturer | [B] | faulty brake light switch; wiring | Seen as Intermittent on a real 2001 W203 scan. A classic cause of ESP/BAS warnings. |
| C1202 | BAS release switch — plausibility | C | manufacturer | [B] | — | Seen as Intermittent on a real 2001 W203 scan. |
| C1300 | Left front axle solenoid valve (Hold) (A7/3y6) open/shorted | C | manufacturer | [C] | solenoid; wiring | An ML320 owner report independently shows "C1300 - Solenoid Valve A7/3YC Hold Pressure" [C] — consistent. |
| C1303 | Right front axle solenoid valve (Hold) open/shorted | C | manufacturer | [C] | solenoid; wiring | — |
| C1311 | Switchover solenoid valve (Release) open/shorted | C | manufacturer | [C] | solenoid; wiring | — |
| C1312 | Master cylinder switchover valve | C | manufacturer | [C] | — | — |
| C1314 | Voltage supply solenoid valves | C | manufacturer | [C] | — | Seen on a 2000 ML320 with dealer + independent scans (owner report). |
| C1401 | High pressure return pump circuit open/shorted; will not shut off | C | manufacturer | [C] | pump; relay; wiring | — |
| C1501 | SPS P-valve | C | manufacturer | [C] | — | Speed-sensitive steering valve. |
| C1512 | Brakes overheated | C | manufacturer | [C] | — | — |
| C1529 | Precharging of accumulator is not available | C | manufacturer | [B] | — | SBC (Sensotronic Brake Control) system. Seen as Intermittent on a real 2001 W203 scan. |
| C1600 | Temperature after engine is turned off | C | manufacturer | [C] | — | Heat-soak informational code. |
| P1000 | Electronic gear selector module (N15/5) defective | P | manufacturer | [B] | faulty gear selector module (N15/5); wiring; CAN communication faults | Transmission/EGS family code. See also P1747/P1750/P1832/P1910/P1912. |
| P1228 | Unknown code (reported on 1997 C220 CDI) | P | manufacturer | [C] | — | Listed as "yet unknown" in community lists — do not act on without model-specific documentation. |
| P1386 | Knock control fault | P | manufacturer | [C] | faulty knock sensor(s); incorrect fuel octane; engine mechanical issues | — |
| P1570 | Intermittent no-start — immobilizer module | P | manufacturer | [B] | faulty immobilizer module; wiring; key/transponder issues | Immobilizer-adjacent code documented at DTC-description level only. No bypass material sought or reproduced. |
| P1664 | Electronic heater booster fault | P | manufacturer | [B] | — | Seen on a 2001 W203 CDI Autocom scan alongside P0703 (brake signal). Diesel models. |
| P1747 | Electronic gear selector module — defective interaction of CAN with control unit A1 (instrument cluster) | P | manufacturer | [B] | CAN communication fault between EGS and cluster; wiring; module faults | EGS family — see P1000. |
| P1750 | Electronic gear selector module — very low control unit supply voltage | P | manufacturer | [B] | low system voltage; wiring; charging system | Check battery/charging first — low voltage causes cascading CAN faults on Mercedes (cf. C1010/C361). |
| P1832 | Electronic gear selector module — short in circuit N15/5 output stage | P | manufacturer | [B] | short in selector-module output circuit; module fault | EGS family — see P1000. |
| P1910 | Electronic gear selector module — control unit overvoltage | P | manufacturer | [B] | charging-system overvoltage; wiring | EGS family — see P1000. |
| P1912 | Electronic gear selector module — weak touch push-button voltage | P | manufacturer | [B] | — | EGS family — see P1000. |
| P2000 | NOx trap efficiency below threshold (Bank 1) | P | manufacturer | [B] | degraded NOx storage catalyst; exhaust system faults | Diesel emissions. NOTE: on a 2001 W203 Autocom scan, P2000 appears with a different text ("Braking torque from the traction system over CAN bus; implausible") — meaning is model/era-dependent; confirm per model [B — real scan]. |
| P2001 | NOx trap efficiency below threshold (Bank 2) | P | manufacturer | [B] | degraded NOx storage catalyst; exhaust system faults | Diesel emissions. |
| P2003 | Particulate trap efficiency below threshold (Bank 1) | P | manufacturer | [B] | degraded DPF; exhaust system faults | Diesel emissions. |
| P2004 | Particulate trap efficiency below threshold (Bank 2) | P | manufacturer | [B] | degraded DPF; exhaust system faults | Diesel emissions. |
| P2031 | Exhaust gas temperature sensor circuit (Bank 1 Sensor 2) | P | manufacturer | [B] | EGT sensor; wiring | See P2032/P2033 for low/high variants. |
| P2032 | Exhaust gas temperature sensor circuit low (Bank 1 Sensor 2) | P | manufacturer | [B] | EGT sensor; wiring short to ground | — |
| P2033 | Exhaust gas temperature sensor circuit high (Bank 1 Sensor 2) | P | manufacturer | [B] | EGT sensor; wiring short to positive/open | — |
| P2080 | Exhaust gas temperature sensor circuit range/performance (Bank 1 Sensor 1) | P | manufacturer | [B] | EGT sensor; wiring | — |
| P2081 | Exhaust gas temperature sensor circuit intermittent (Bank 1 Sensor 1) | P | manufacturer | [B] | EGT sensor; wiring/connector | — |
| P2100 | Throttle actuator control motor circuit / open | P | manufacturer | [B] | throttle actuator; wiring | — |
| P2101 | Throttle actuator control motor circuit range/performance | P | manufacturer | [B] | throttle actuator; wiring | — |
| P2208 | Transmission — speed of Y3/6n2 to Y3/6n3 excessive | P | manufacturer | [B] | transmission speed sensors; internal transmission fault | 722.x transmission speed-sensor plausibility. |
| P261F71 | Coolant circulation pump output malfunction — actuator blocked (Sprinter, OM651) | P | manufacturer | [C] | coolant intrusion into vacuum system via water pump internal seal (documented field pattern on OM651) | UDS-format code (P261F + failure-type byte 0x71). Newer-model code format; do not expect on pre-UDS models. |
| U0020 | Low speed CAN communication bus B | U | manufacturer | [C] | CAN-B wiring/module fault | — |

## nissan — 274 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1017 | Occupant Classification System Control Unit [Unit Fail] | B | manufacturer | [A] | — | OCS control unit malfunctioning; FSM repair order: replace RH front seat cushion/OCS control unit assembly (do not disassemble the cushion). |
| B1018 | Occupant Classification Sensor [Unit Fail] | B | manufacturer | [A] | damaged wiring under passenger seat; poor connector contact; failed OCS sensor mat in seat cushion | OCS sensor mat malfunctioning. Check wiring under the seat, unplug/clean/reconnect; the sensor is inside the seat cushion and is not separately serviceable — cushion assembly replacement is the FSM repair. |
| B1019 | Belt Tension Sensor [Unit Fail] | B | manufacturer | [A] | — | CONFLICT — 2007 Xterra FSM lists B1019 as "BELT TENSION SENS [UNIT FAIL]" (belt tension sensor malfunctioning; repair: replace RH front seat belt assembly), while the 2010 Altima SRC section lists B1019 as "OCCUPANT SENS [OTHER FAIL]" (OCS malfunctioning). Meaning appears model/year-dependent; verify against the specific vehicle's FSM. |
| B1020 | Occupant Classification System Control Unit [Unit Fail] | B | manufacturer | [A] | — | Grouped with B1017/B1021 in the FSM chart; same OCS control unit diagnosis. |
| B1021 | Occupant Classification System Control Unit [Unit Fail] | B | manufacturer | [A] | — | Grouped with B1017/B1020 in the FSM chart; same OCS control unit diagnosis. |
| B1022 | Occupant Classification System Control Unit [Communication Fail] | B | manufacturer | [A] | — | Communication between the OCS control unit and the air bag diagnosis sensor unit is interrupted; check harness connections before replacing units. |
| B1023 | Front Passenger Air Bag OFF Indicator Circuit | B | manufacturer | [A] | — | Front passenger air bag OFF indicator malfunctioning; FSM repair order: check harness, replace harness, replace the indicator, replace air bag diagnosis sensor unit. |
| B1033 | Crash Zone Sensor [Unit Fail] | B | manufacturer | [A] | — | Crash zone sensor internal failure; FSM repair order: check harness, replace harness, replace crash zone sensor, replace air bag diagnosis sensor unit. |
| B1034 | Crash Zone Sensor [Unit Fail] | B | manufacturer | [A] | — | See B1033. |
| B1035 | Crash Zone Sensor [Communication Fail] | B | manufacturer | [A] | — | Crash zone sensor communication failure with air bag diagnosis sensor unit. |
| B1049 | Driver Air Bag Module [Open] | B | manufacturer | [A] | open in driver air bag module circuit including spiral cable (clock spring); damaged harness; faulty module | CONFLICT — the 2007 Xterra FSM CONSULT-II chart places B1049/B1054 under DRIVER AIRBAG MODULE [OPEN] (circuit open including the spiral cable), while community sources (JustAnswer) variously describe B1049 as a front-passenger airbag/OCS/pretensioner fault. FSM repair order: visually check harness, replace harness if damaged, replace driver air bag module, replace spiral cable, replace air bag diagnosis sensor unit. Trust the FSM for the specific vehicle. |
| B1050 | Driver Air Bag Module [VB-Short] | B | manufacturer | [A] | — | Driver air bag module circuit shorted to some power supply circuit (including spiral cable). |
| B1051 | Driver Air Bag Module [GND-Short] | B | manufacturer | [A] | — | Driver air bag module circuit shorted to ground (including spiral cable). |
| B1052 | Driver Air Bag Module [Short] | B | manufacturer | [A] | — | Driver air bag module circuits shorted to each other. |
| B1054 | Driver Air Bag Module [Open] | B | manufacturer | [A] | — | Second-stage (dual-stage inflator) counterpart of B1049; see B1049 notes and conflict. |
| B1055 | Driver Air Bag Module [VB-Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1050. |
| B1056 | Driver Air Bag Module [GND-Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1051. |
| B1057 | Driver Air Bag Module [Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1052. Note: B1053 is skipped in this scheme (stage 1 = B1049–B1052, stage 2 = B1054–B1057). |
| B1065 | Front Passenger Air Bag Module [Open] | B | manufacturer | [A] | — | Front passenger air bag module circuit open; FSM repair order: check harness, replace harness, replace module, replace diagnosis sensor unit. |
| B1066 | Front Passenger Air Bag Module [VB-Short] | B | manufacturer | [A] | — | Front passenger air bag module circuit shorted to some power supply circuit. |
| B1067 | Front Passenger Air Bag Module [GND-Short] | B | manufacturer | [A] | — | Front passenger air bag module circuit shorted to ground. |
| B1068 | Front Passenger Air Bag Module [Short] | B | manufacturer | [A] | — | Front passenger air bag module circuits shorted to each other. |
| B1070 | Front Passenger Air Bag Module [Open] | B | manufacturer | [A] | — | Second-stage counterpart of B1065. |
| B1071 | Front Passenger Air Bag Module [VB-Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1066. |
| B1072 | Front Passenger Air Bag Module [GND-Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1067. |
| B1073 | Front Passenger Air Bag Module [Short] | B | manufacturer | [A] | — | Second-stage counterpart of B1068. |
| B2014 | Chain of S/L-BCM — steering lock unit to BCM communication fault; inhibits engine cranking | B | manufacturer | [A] | — | From the Nissan power-distribution service manual BCM DTC chart; engine cranking is inhibited while this code is active. |
| B2108 | Steering Lock Relay ON | B | manufacturer | [A] | faulty IPDM E/R (relay stuck ON) | IPDM E/R detects the steering lock relay stuck at ON for ~1 second even though the BCM commands it OFF. Check 10A fuse No. 40 in IPDM E/R; if the code is current, replace IPDM E/R. |
| B2109 | Steering Lock Relay | B | manufacturer | [A] | — | Steering lock relay ON signal transmitted from BCM to IPDM E/R via CAN; IPDM E/R turns the relay ON and reports steering release to BCM. (Coupe variant in source.) |
| B210B | Starter Control Relay — Stuck ON | B | manufacturer | [A] | faulty IPDM E/R; harness/connector faults in starter control relay circuit | IPDM E/R detects the starter control relay stuck in the ON position for 1 second or more (comparing BCM CAN signals against IPDM E/R inputs). If current, replace IPDM E/R. |
| B210C | Starter Control Relay — Stuck OFF (Circuit) | B | manufacturer | [A] | faulty IPDM E/R; faulty BCM; low IPDM E/R supply voltage (~7–8V); harness faults | IPDM E/R detects the starter control relay stuck in the OFF position for 1 second or more. May set spuriously on low IPDM E/R supply voltage. |
| B210D | Starter Relay — Stuck ON (Circuit) | B | manufacturer | [A] | harness/connectors (starter motor relay control circuit open/shorted); faulty IPDM E/R; faulty BCM | IPDM E/R detects the starter relay stuck in the ON position for 5 seconds or more. |
| B210E | Starter Relay — Stuck OFF | B | manufacturer | [A] | faulty IPDM E/R; faulty BCM; low battery/IPDM E/R supply voltage | IPDM E/R detects the starter relay stuck in the OFF position for 5 seconds or more. Diagnose B2605 first if displayed together. |
| B210F | Shift Position / Clutch Interlock Switch | B | manufacturer | [A] | harness/connectors (CAN line or transmission range switch circuit open/shorted); faulty transmission range switch; faulty IPDM E/R; faulty BCM | IPDM E/R detects a mismatch between the hardwired P/N position signal from the transmission range switch and the P/N signal received from BCM via CAN. |
| B2110 | Shift Position / Clutch Interlock Switch | B | manufacturer | [A] | — | Pairs with B210F in the SEC diagnosis section (shift position/clutch interlock switch circuit). |
| B2190 | Difference of Key (NATS antenna) — different/unregistered key detected via NATS antenna | B | manufacturer | [B] | unregistered key used | BCM-level counterpart to P1615; resolve any U-codes (communication faults) before diagnosing B-codes. |
| B2191 | Difference of Key — ID verification between BCM and Intelligent Key is NG; prohibits steering-lock release / engine start with unregistered Intelligent Key | B | manufacturer | [A] | unregistered Intelligent Key; Intelligent Key malfunction | Nissan service-manual procedure: perform initialization with CONSULT-III and re-register ALL Intelligent Keys. CONFLICT: one YouTube DTC video labels B2191 as "HO2S Heater Circuit Short (Right Bank)" — this contradicts the Nissan service manual and is almost certainly a mislabeled generic decode; the service-manual definition (Difference of Key) is used here. |
| B2192 | ID Discord BCM-ECM — BCM performs ID verification with ECM; inhibits engine cranking | B | manufacturer | [A] | — | BCM-level counterpart to P1611; erase DTC after initialization. |
| B2193 | Chain of BCM-ECM — BCM to ECM communication chain fault; inhibits engine cranking | B | manufacturer | [A] | — | BCM-level counterpart to P1612; erase DTC after repair. |
| B2195 | Anti-Scanning — inhibits engine cranking | B | manufacturer | [A] | — | NATS anti-scanning function tripped; ignition ON/OFF cycle per service manual. |
| B2196 | Dongle NG — inhibits engine cranking | B | manufacturer | [A] | — | Dongle-unit (RHD models) malfunction; erase DTC after repair. |
| B2198 | NATS Antenna Amp — inhibits engine cranking | B | manufacturer | [A] | NATS antenna amplifier malfunction | BCM-level counterpart to P1614; erase DTC 500 ms after signal communication becomes consistent. |
| B2555 | Stop Lamp | B | manufacturer | [A] | — | Stop lamp switch circuit monitored by BCM. |
| B2556 | Push-Button Ignition Switch | B | manufacturer | [A] | — | Push-button ignition switch circuit monitored by BCM. |
| B2557 | Vehicle Speed | B | manufacturer | [A] | — | Vehicle speed signal monitored by BCM. |
| B2562 | Low Voltage | B | manufacturer | [A] | low battery voltage; charging system fault | BCM low-voltage detection; check battery and charging system first (also appears in BCM priority chart position 1). |
| B2590 | not verified — referenced as a NATS DTC in a Mitchell 1 Nissan TSB alongside P1610-P1615/B2191-B2193, but no definition was found in verifiable sources | B | manufacturer | [C] | — | Listed here for completeness so the TSB's code set is not silently truncated; treat the definition as unverified. |
| B2601 | Shift Position | B | manufacturer | [A] | — | Shift position signal monitored by BCM (one of B2601/B2602/B2603 shift-position family). |
| B2602 | Shift Position | B | manufacturer | [A] | — | See B2601. |
| B2603 | Shift Position Status | B | manufacturer | [A] | — | Shift position status signal. |
| B2604 | PNP/Clutch Switch | B | manufacturer | [A] | — | Park/neutral position (CVT) / clutch interlock (M/T) switch signal. |
| B2605 | PNP/Clutch Switch | B | manufacturer | [A] | — | See B2604. Diagnose B2605 before B210E when both are displayed. |
| B2608 | Starter Relay — inhibits engine cranking | B | manufacturer | [A] | — | Starter motor relay control signal / CAN status signal inconsistency. |
| B260F | Engine State Signal Lost — inhibits engine cranking | B | manufacturer | [A] | — | Received engine status signal (CAN) lost after power position changes to ACC. |
| B2614 | BCM (Accessory Relay Circuit) | B | manufacturer | [A] | accessory relay circuit open/shorted; faulty BCM; faulty accessory relay; harness/connectors | BCM requests accessory relay operation but gets no response for 2+ seconds. (PCS section: power distribution system.) |
| B2615 | BCM | B | manufacturer | [A] | — | BCM internal fault (one of the B2614/B2615/B2616/B2618 BCM group; B2617 not used). |
| B2616 | BCM | B | manufacturer | [A] | — | BCM internal fault; see B2615. |
| B2618 | BCM | B | manufacturer | [A] | — | BCM internal fault; see B2615. |
| B2619 | BCM — inhibits engine cranking | B | manufacturer | [A] | — | BCM-internal fault flag in the cranking-inhibit chart. |
| B261A | Push-Button Ignition Switch | B | manufacturer | [A] | — | Push-button ignition switch circuit (PCS/power distribution context). |
| B261F | ASCD Cancel / Clutch Switch | B | manufacturer | [A] | — | ASCD cancel/clutch switch circuit. |
| B2620 | Neutral Switch (Park/Neutral Position Switch) | B | manufacturer | [A] | — | Listed as "NEUTRAL SW" in the Juke index and "PARK/NEUTRAL POSITION SWITCH" in the Note SEC. |
| B2621 | Inside Key Antenna | B | manufacturer | [A] | — | Intelligent Key inside antenna circuit (door lock / key system). |
| B2622 | Inside Key Antenna | B | manufacturer | [A] | — | See B2621 (second inside-antenna channel). |
| B2626 | Outside Key Antenna | B | manufacturer | [A] | — | Intelligent Key outside antenna circuit. |
| B2627 | Outside Key Antenna | B | manufacturer | [A] | — | See B2626 (second outside-antenna channel). |
| B2628 | Outside Key Antenna | B | manufacturer | [A] | — | See B2626 (third outside-antenna channel). |
| B26E8 | Clutch Interlock Switch | B | manufacturer | [A] | — | Clutch interlock switch circuit (M/T models). |
| B26F1 | Ignition Relay OFF — inhibits engine cranking | B | manufacturer | [A] | — | — |
| B26F2 | Ignition Relay ON | B | manufacturer | [A] | — | Fail-safe: inhibit engine cranking. Ignition switch ON signal (CAN, from BCM) stuck OFF/ON mismatch. |
| B26F3 | Starter Control Relay ON | B | manufacturer | [A] | — | Starter control relay stuck ON. |
| B26F4 | Starter Control Relay OFF | B | manufacturer | [A] | — | Starter control relay stuck OFF. |
| B26F6 | BCM | B | manufacturer | [A] | — | BCM internal fault (one of the B26F6/B26F7/B26F8 BCM group). |
| B26F7 | BCM | B | manufacturer | [A] | — | BCM internal fault; see B26F6. |
| B26F8 | BCM | B | manufacturer | [A] | — | BCM internal fault; see B26F6. |
| B26F9 | Crank Request Circuit — Short | B | manufacturer | [A] | — | Crank request circuit shorted. |
| B26FA | Crank Request Circuit — Open | B | manufacturer | [A] | — | Crank request circuit open. |
| B26FB | Clutch Switch | B | manufacturer | [A] | — | Clutch switch circuit. |
| B26FC | Key Registration | B | manufacturer | [A] | — | Key registration fault (Intelligent Key / NATS key registration). |
| C1101 | RR RH Sensor 1 — circuit of rear RH wheel sensor is open | C | manufacturer | [A] | wheel sensor; sensor reluctor/tone ring; wiring harness between ABS module and sensor; faulty ABS actuator and electric unit (control unit) | From the Nissan brake-control service manual self-diagnostic item chart. If the sensor was already replaced with no change, inspect the reluctor ring and the harness before condemning the ABS unit; a capable scanner reading ABS live wheel-speed data is the fastest next step. |
| C1102 | RR LH Sensor 1 — circuit of rear LH wheel sensor is open | C | manufacturer | [A] | wheel sensor; reluctor; harness; ABS control unit | Same diagnostic path as C1101 (rear LH position). |
| C1103 | FR RH Sensor 1 — circuit of front RH wheel sensor is open | C | manufacturer | [A] | wheel sensor; reluctor; harness; ABS control unit | Same diagnostic path as C1101 (front RH position). |
| C1104 | FR LH Sensor 1 — circuit of front LH wheel sensor is open | C | manufacturer | [A] | wheel sensor; reluctor; harness; ABS control unit | Same diagnostic path as C1101 (front LH position). Note: some scan tools convert Nissan 2-digit ABS codes to 4-digit codes inaccurately — confirm with a Nissan-capable tool. |
| C1105 | RR RH Sensor 2 — circuit of rear RH wheel sensor is shorted, or sensor power voltage is unusual | C | manufacturer | [A] | shorted sensor circuit; abnormal sensor supply voltage; excessive gap between wheel sensor and sensor rotor (control unit cannot identify pulses) | — |
| C1106 | RR LH Sensor 2 — circuit of rear LH wheel sensor is shorted, or sensor power voltage is unusual | C | manufacturer | [A] | shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap | — |
| C1107 | FR RH Sensor 2 — circuit of front RH wheel sensor is shorted, or sensor power voltage is unusual | C | manufacturer | [A] | shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap | — |
| C1108 | FR LH Sensor 2 — circuit of front LH wheel sensor is shorted, or sensor power voltage is unusual | C | manufacturer | [A] | shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap | — |
| C1109 | Battery Voltage Abnormal — ABS actuator and electric unit (control unit) power voltage too low | C | manufacturer | [A] | low battery voltage; charging system fault | Check battery/charging before condemning the ABS unit — low voltage alone sets this code. |
| C1110 | Controller Failure — internal malfunction of ABS actuator and electric unit (control unit) | C | manufacturer | [A] | internal ABS control-unit failure | Service-manual reference: ABS/TCS/VDC control unit inspection; this code means the unit itself, not its inputs. |
| C1111 | Pump Motor — ABS pump motor fault during actuator motor operation | C | manufacturer | [B] | ABS pump motor; power/ground to the pump | The pump can be bench-tested by remotely applying power and ground to verify it activates. |
| C1113 | G-Sensor | C | manufacturer | [A] | — | ABS/VDC G-sensor circuit. |
| C1114 | Main Relay | C | manufacturer | [A] | — | ABS actuator main relay circuit. |
| C1115 | ABS Sensor [Abnormal Signal] | C | manufacturer | [A] | incorrect (non-specified) tires fitted; wheel sensor / sensor rotor issues; ABS module ground faults | Set when a wheel-speed difference vs the other wheels is detected while driving (e.g., wrong-size tires). Inspect sensor connectors for corrosion/damage, clean sensor rings, check harness and module grounds. |
| C1116 | Stop Lamp Switch | C | manufacturer | [A] | — | Stop lamp switch signal not input when the brake pedal operates. |
| C1120 | Front LH IN ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in front LH ABS IN (inlet) solenoid valve. |
| C1121 | Front LH OUT ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in front LH ABS OUT (outlet) solenoid valve. |
| C1122 | Front RH IN ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in front RH ABS IN solenoid valve. |
| C1123 | Front RH OUT ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in front RH ABS OUT solenoid valve. |
| C1124 | Rear LH IN ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in rear LH ABS IN solenoid valve. |
| C1125 | Rear LH OUT ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in rear LH ABS OUT solenoid valve. |
| C1126 | Rear RH IN ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in rear RH ABS IN solenoid valve. |
| C1127 | Rear RH OUT ABS Solenoid Valve | C | manufacturer | [A] | — | Malfunction detected in rear RH ABS OUT solenoid valve. |
| C1130 | Engine Signal 1 | C | manufacturer | [A] | failed ABS actuator; ABS module wiring short/open; ABS module with mismatched/unprogrammed VIN | Malfunction detected in ECM system as seen by the ABS actuator and electric unit (control unit). Community reports treat it as an ABS control unit failure code. |
| C1131 | Engine Signal 2 | C | manufacturer | [A] | — | Engine signal 2 as seen by the ABS control unit. |
| C1132 | Engine Signal 3 | C | manufacturer | [A] | — | Engine signal 3 as seen by the ABS control unit. |
| C1133 | Engine Signal 4 | C | manufacturer | [A] | — | Engine signal 4 as seen by the ABS control unit. (Note: the Armada index skips from ENGINE SIGNAL 4 to ENGINE SIGNAL 6.) |
| C1136 | Engine Signal 6 | C | manufacturer | [A] | — | Engine signal 6 as seen by the ABS control unit. (ENGINE SIGNAL 5 not listed in the index.) |
| C1140 | Actuator Relay | C | manufacturer | [A] | — | ABS actuator relay circuit. |
| C1142 | Pressure Sensor Circuit | C | manufacturer | [A] | — | ABS pressure sensor circuit. |
| C1143 | Steering Angle Sensor Circuit | C | manufacturer | [A] | — | Steering angle sensor circuit fault (VDC). |
| C1144 | Steering Angle Sensor Signal | C | manufacturer | [A] | — | Steering angle sensor signal fault (VDC). |
| C1145 | Yaw Rate Sensor | C | manufacturer | [A] | — | Yaw rate sensor fault (VDC). |
| C1146 | Side G-Sensor Circuit | C | manufacturer | [A] | — | Side (lateral) G-sensor circuit fault (VDC). |
| C1155 | Brake Fluid Level Low | C | manufacturer | [A] | low brake fluid; brake fluid level switch/sensor fault | Brake fluid level low detection. |
| C1156 | Steering Angle Sensor Communication Circuit | C | manufacturer | [A] | — | Steering angle sensor communication circuit fault. |
| C1160 | Decel G-Sensor Set (Not Calibrated) | C | manufacturer | [A] | — | Deceleration G-sensor neutral position not set/calibrated. |
| C1163 | Steering Angle Sensor Safe (Neutral Position Not Learned) | C | manufacturer | [A] | — | Steering angle sensor safe/neutral position not established. |
| C1164 | Cut Valve 1 (CV1) | C | manufacturer | [A] | — | ABS actuator cut valve 1 (VDC/TCS hydraulic circuit). |
| C1165 | Cut Valve 2 (CV2) | C | manufacturer | [A] | — | ABS actuator cut valve 2. |
| C1166 | Suction Valve 1 (SV1) | C | manufacturer | [A] | — | ABS actuator suction valve 1. |
| C1167 | Suction Valve 2 (SV2) | C | manufacturer | [A] | — | ABS actuator suction valve 2. |
| C1170 | Variant Coding | C | manufacturer | [A] | — | ABS control unit variant coding mismatch (incorrect coding for the vehicle). |
| C1176 | Stop Lamp Switch 2 | C | manufacturer | [A] | — | Second stop lamp switch signal circuit. |
| C1704 | Low Tire Pressure — Front LH | C | manufacturer | [A] | low tire inflation pressure (at or below ~182–189 kPa / ~26–27 psi depending on model) | TPMS low-pressure warning. Check and adjust all tire pressures to specification, then drive at 40 km/h (25 MPH) or more for ~10 minutes and re-run BCM self-diagnosis. |
| C1705 | Low Tire Pressure — Front RH | C | manufacturer | [A] | low tire inflation pressure | See C1704. |
| C1706 | Low Tire Pressure — Rear RH | C | manufacturer | [A] | low tire inflation pressure | See C1704. |
| C1707 | Low Tire Pressure — Rear LH | C | manufacturer | [A] | low tire inflation pressure | See C1704. |
| C1708 | Tire Pressure Transmitter — No Data, Front LH | C | manufacturer | [A] | — | No data received from the front LH tire pressure transmitter (ID registration or transmitter fault). |
| C1709 | Tire Pressure Transmitter — No Data, Front RH | C | manufacturer | [A] | — | See C1708 (front RH). |
| C1710 | Tire Pressure Transmitter — No Data, Rear RH | C | manufacturer | [A] | — | See C1708 (rear RH). |
| C1711 | Tire Pressure Transmitter — No Data, Rear LH | C | manufacturer | [A] | — | See C1708 (rear LH). |
| C1716 | Tire Pressure Transmitter — Pressure Data Error, Front LH | C | manufacturer | [A] | — | Pressure data error from the front LH transmitter. |
| C1717 | Tire Pressure Transmitter — Pressure Data Error, Front RH | C | manufacturer | [A] | — | See C1716 (front RH). |
| C1718 | Tire Pressure Transmitter — Pressure Data Error, Rear RH | C | manufacturer | [A] | — | See C1716 (rear RH). |
| C1719 | Tire Pressure Transmitter — Pressure Data Error, Rear LH | C | manufacturer | [A] | — | See C1716 (rear LH). |
| C1729 | Vehicle Speed Signal Error (TPMS) | C | manufacturer | [A] | — | Vehicle speed signal error as seen by the tire pressure monitoring function (BCM). |
| P0603 | ECM Back Up Circuit | P | manufacturer | [A] | — | — |
| P0850 | Park/Neutral Position Switch Circuit | P | manufacturer | [A] | — | — |
| P1031 | A/F Sensor Heater (Bank 1) | P | manufacturer | [B] | — | Nissan TSB NTB04-032a (2004 Titan/Armada): MIL ON with P1031/P1051/P1148/P1168 addressed by ECM reprogram after confirming ECM part number against the bulletin chart. |
| P1032 | Air Fuel Ratio (A/F) Sensor 1 Heater Control Circuit High (Bank 1) | P | manufacturer | [A] | faulty A/F sensor 1 (bank 1); A/F sensor 1 heater harness open or shorted; poor electrical connection in A/F sensor 1 circuit | High-circuit counterpart of P1031. Nissan TSB NTB04-032a (2004 Titan/Armada) covers the A/F sensor heater low-circuit codes P1031/P1051 (ECM reprogram after confirming ECM part number); the high-circuit codes P1032/P1052 share the same heater circuit diagnosis. |
| P1051 | A/F Sensor Heater (Bank 2) | P | manufacturer | [B] | — | Same TSB NTB04-032a coverage as P1031 (bank 2 counterpart). |
| P1052 | Air Fuel Ratio (A/F) Sensor 1 Heater Control Circuit High (Bank 2) | P | manufacturer | [A] | — | High-circuit counterpart of P1051 (bank 2). See P1032 notes for the shared heater-circuit context. |
| P1065 | ECM Power Supply (Battery Voltage Supply) | P | manufacturer | [A] | failing battery (voltage below 12V engine-off); failing alternator (outside 13.2–14.4V running); loose/corroded battery cables; wiring fault to ECM backup power | ECM receives battery voltage at all times for memory backup. Per Nissan tech guidance: check alternator output (13.2–14.4V running), then battery voltage after 15 min rest (below 12V suggests a bad cell); code may self-clear after 75–100 miles of driving if power supply is healthy. |
| P1102 | MAF Sensor Performance Problem | P | manufacturer | [C] | — | — |
| P1105 | MAP/BARO Pressure Switch Solenoid Valve | P | manufacturer | [B] | — | — |
| P1110 | Intake Valve Timing Control, Bank 1 | P | manufacturer | [B] | dirty/low engine oil; faulty intake valve timing control solenoid valve (bank 1); solenoid harness open/shorted; faulty crankshaft position sensor (POS); faulty camshaft position sensor | Set when the gap between target and actual cam phase angle exceeds the threshold. Check/change engine oil and filter before replacing the solenoid valve. |
| P1111 | Intake Valve Timing Control Solenoid Valve Circuit, Bank 1 | P | manufacturer | [B] | — | Circuit-level counterpart of P1110 on some models/years. |
| P1116 | Automatic Transmission Turbine Revolution Sensor Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1119 | Engine Coolant Temperature (ECT) Sensor Radiator Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1120 | Throttle Position (TP) Sensor 2 Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1121 | Electric Throttle Control Actuator | P | manufacturer | [A] | — | In fail-safe, ECM regulates throttle opening around idle; engine speed will not rise above ~2,000 rpm. |
| P1122 | Electric Throttle Control Function | P | manufacturer | [A] | — | — |
| P1123 | Throttle Motor Relay Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1124 | Electric Throttle Control Actuator | P | manufacturer | [A] | — | Groups with P1126/P1128 in the Titan priority chart under electric throttle control actuator faults. |
| P1125 | Throttle Position (TP) Sensor 1 and 2 Signal Malfunction | P | manufacturer | [C] | — | — |
| P1126 | Thermostat Function | P | manufacturer | [B] | — | — |
| P1128 | Electric Throttle Control Actuator | P | manufacturer | [A] | — | Groups with P1124/P1126 in the Titan priority chart under electric throttle control actuator faults. |
| P1130 | Swirl Control Valve Control Solenoid Valve | P | manufacturer | [B] | — | — |
| P1131 | Intake Manifold Air Control Solenoid Malfunction | P | manufacturer | [C] | — | — |
| P1132 | Intake Manifold Air Control Solenoid Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1135 | Camshaft Position (CMP) Actuator RH Malfunction | P | manufacturer | [C] | — | Bank 2 (RH) counterpart of P1110; intake valve timing control solenoid valve, bank 2. |
| P1136 | Camshaft Position (CMP) Actuator Intake Bank 2 Circuit Malfunction | P | manufacturer | [C] | — | Circuit-level counterpart of P1135; bank 2 analog of P1111. |
| P1137 | Intake Manifold Air Control Actuator Position Sensor Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1138 | Intake Manifold Air Control Solenoid Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1140 | Camshaft Position (CMP) Actuator LH Circuit Malfunction | P | manufacturer | [C] | — | Bank 1 (LH) circuit-level analog; pairs with P1110/P1111 family. |
| P1143 | Heated Oxygen Sensor 1 Lean Shift Monitoring, Bank 1 | P | manufacturer | [B] | faulty front heated oxygen sensor (bank 1); intake air leaks; HO2S1 harness open/shorted; poor electrical connection; fuel pressure; injectors | Detected when the sensor's max/min voltages do not reach specified values. Reported on 2002–2003 Frontier/Altima; Nissan issued ground-fix guidance (reinforce intake/sensor grounds) for persistent P1143 before replacing sensors. |
| P1144 | Heated Oxygen Sensor 1 Rich Shift Monitoring, Bank 1 | P | manufacturer | [B] | faulty front heated oxygen sensor (bank 1); HO2S1 harness open/shorted; poor electrical connection; inappropriate fuel pressure; faulty injectors; intake or exhaust leaks | Detected when an excessively high sensor voltage is sent to the ECM. Replacing the front O2 sensor (bank 1) usually resolves it. |
| P1145 | Camshaft Position (CMP) Actuator Position Sensor Intake Bank 2 Circuit Malfunction | P | manufacturer | [C] | — | Bank 2 intake valve timing control position sensor circuit; pairs with P1140 (bank 1). |
| P1146 | Heated Oxygen Sensor 2 (Bank 1) — Voltage Low | P | manufacturer | [A] | — | Rear (post-catalyst) oxygen sensor, bank 1. |
| P1147 | Heated Oxygen Sensor 2 (Bank 1) — Voltage High | P | manufacturer | [A] | — | Rear (post-catalyst) oxygen sensor, bank 1. |
| P1148 | Closed Loop Control (Bank 1) — A/F sensor closed-loop fault | P | manufacturer | [B] | failed A/F sensor (bank 1 sensor 1); damaged sensor connectors; poor grounding; wiring shorts; exhaust leaks | Nissan TSB NTB04-032a covers 2004 Titan/Armada MIL ON with P1148/P1168 — fix is an ECM reprogram (verify ECM part number against the bulletin first). On other models, inspect the A/F sensor harness and connectors before condemning the sensor. |
| P1164 | Heated Oxygen Sensor 1 (Bank 2) — Voltage High | P | manufacturer | [C] | — | — |
| P1165 | Swirl Control Valve Control Vacuum Switch | P | manufacturer | [B] | — | — |
| P1166 | Heated Oxygen Sensor 2 (Bank 2) — Voltage High | P | manufacturer | [A] | — | Rear (post-catalyst) oxygen sensor, bank 2. Note: the source list gives P1166 and P1167 the identical description; the FSM groups both under heated oxygen sensor 2 without distinguishing sub-conditions. |
| P1167 | Heated Oxygen Sensor 2 (Bank 2) — Voltage High | P | manufacturer | [A] | — | See P1166 — source list duplicates the description for P1166/P1167; FSM does not distinguish them. |
| P1168 | Closed Loop Control (Bank 2) — A/F sensor closed-loop fault | P | manufacturer | [B] | failed A/F sensor (bank 2 sensor 1); wiring/connector damage; poor grounding | Bank-2 counterpart of P1148; same TSB NTB04-032a ECM-reprogram coverage on 2004 Titan/Armada. |
| P1169 | Heated Oxygen Sensor 3 — Voltage Low | P | manufacturer | [C] | — | Note: the source list gives P1169 and P1170 the identical description ("HO2S 3 voltage low"). |
| P1170 | Heated Oxygen Sensor 3 — Voltage Low | P | manufacturer | [C] | — | See P1169 — source list duplicates the description for P1169/P1170. |
| P1211 | ABS/TCS Control Unit | P | manufacturer | [B] | — | — |
| P1212 | ABS/TCS Communication Line — ECM cannot receive information from ABS actuator and electric unit (control unit) continuously | P | manufacturer | [B] | CAN communication line open or shorted (harness/connectors); ABS actuator and electric unit (control unit); weak battery | Diagnose U1000/U1001 communication codes FIRST before chasing P1212; the TCM/ABS module is not necessarily at fault. |
| P1217 | Engine Over Temperature (Overheat) | P | manufacturer | [B] | — | — |
| P1220 | Fuel Pressure (FP) Control Module Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1223 | Throttle Position (TP) Sensor 2 — Voltage Low | P | manufacturer | [C] | — | — |
| P1224 | Throttle Position (TP) Sensor 2 — Voltage High | P | manufacturer | [C] | — | — |
| P1225 | Closed Throttle Position Learning, Bank 1 (CTP Learning) | P | manufacturer | [A] | — | Closed-throttle-position learning value out of range; usually corrected by performing the throttle valve closed position learning procedure. |
| P1226 | Closed Throttle Position Learning, Bank 1 (CTP Learning) | P | manufacturer | [A] | — | See P1225 — FSM lists P1225/P1226 under the same CTP LEARNING-B1 item without distinguishing sub-conditions. |
| P1227 | Accelerator Pedal Position (APP) Sensor 2 — Voltage Low | P | manufacturer | [C] | — | — |
| P1228 | Accelerator Pedal Position (APP) Sensor 2 — Voltage High | P | manufacturer | [C] | — | — |
| P1229 | Sensor Power Supply | P | manufacturer | [A] | — | ECM sensor power supply circuit fault; diagnose before sensor-level codes that share the supply. |
| P1271 | Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Voltage Low | P | manufacturer | [A] | — | — |
| P1272 | Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Voltage High | P | manufacturer | [A] | — | — |
| P1273 | A/F Sensor Bank 1 Lean Shift Monitoring — A/F signal shifted lean for a specified period | P | manufacturer | [B] | faulty A/F sensor 1 (bank 1); sensor harness open/shorted; poor electrical connection; low fuel pressure; faulty fuel injector; faulty mass air flow sensor; intake air leaks | Nissan TSBs 04-090A/04-126/04-027a/05-095/04-025 cover P1273/P1283 on 2004-2005 VQ35/VQ40 vehicles — review the bulletins before normal troubleshooting. After repair, clear the mixture-ratio self-learning data or the code can return. |
| P1274 | A/F Sensor Bank 1 Rich Shift Monitoring | P | manufacturer | [B] | — | Bank-1 rich counterpart of P1273; referenced in the same Nissan TSB family (04-090A series). |
| P1276 | Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Activity | P | manufacturer | [A] | — | A/F sensor 1 activity monitor, bank 1. |
| P1278 | Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Slow Response | P | manufacturer | [A] | — | See P1279 — FSM groups both under A/F sensor 1 without distinguishing sub-conditions. |
| P1279 | Air Fuel Ratio (A/F) Sensor 1 (Bank 1) — Slow Response | P | manufacturer | [A] | — | See P1278. |
| P1281 | Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Voltage Low | P | manufacturer | [A] | — | Bank 2 counterpart of P1271. |
| P1282 | Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Voltage High | P | manufacturer | [A] | — | Bank 2 counterpart of P1272. |
| P1283 | A/F Sensor Bank 2 Lean Shift Monitoring — A/F signal shifted lean for a specified period | P | manufacturer | [B] | faulty A/F sensor 1 (bank 2); sensor harness open/shorted; poor electrical connection; low fuel pressure; faulty fuel injector; intake air leaks; faulty air flow meter | Same TSB family and self-learning-clear requirement as P1273 (bank 2). |
| P1284 | A/F Sensor Bank 2 Rich Shift Monitoring | P | manufacturer | [B] | — | Bank-2 rich counterpart of P1283. |
| P1286 | Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Activity | P | manufacturer | [A] | — | Bank 2 counterpart of P1276. |
| P1288 | Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Slow Response | P | manufacturer | [A] | — | Bank 2 counterpart of P1278/P1279. |
| P1289 | Air Fuel Ratio (A/F) Sensor 1 (Bank 2) — Slow Response | P | manufacturer | [A] | — | See P1288. |
| P1320 | Ignition Signal | P | manufacturer | [B] | — | — |
| P1335 | Crankshaft Position Sensor (REF) | P | manufacturer | [B] | — | — |
| P1336 | Crankshaft Position Sensor (CKPS) | P | manufacturer | [B] | — | — |
| P1400 | EGRC Solenoid Valve | P | manufacturer | [B] | — | — |
| P1401 | EGR Temperature Sensor | P | manufacturer | [B] | — | — |
| P1402 | EGR System | P | manufacturer | [B] | — | — |
| P1421 | Cold Start Control | P | manufacturer | [A] | — | — |
| P1440 | EVAP Control System Small Leak | P | manufacturer | [B] | — | — |
| P1441 | Vacuum Cut Valve Bypass Valve | P | manufacturer | [B] | — | Nissan-specific EVAP architecture (vacuum cut valve + bypass valve); distinct from generic P044x leak codes. |
| P1442 | Evaporative Emission (EVAP) Canister Purge System — Small Leak Detected | P | manufacturer | [C] | — | — |
| P1443 | Evaporative Emission (EVAP) Canister Purge Control System — Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1444 | Canister Purge Volume Control Solenoid Valve | P | manufacturer | [B] | — | — |
| P1445 | EVAP Canister Purge Volume Control Valve | P | manufacturer | [B] | — | — |
| P1446 | EVAP Canister Vent Control Valve (Closed) | P | manufacturer | [B] | — | — |
| P1447 | EVAP Control System Purge Flow Monitoring | P | manufacturer | [B] | — | — |
| P1448 | EVAP Canister Vent Control Valve (Open) | P | manufacturer | [B] | — | — |
| P1456 | Evaporative Emission (EVAP) Canister Purge System — Very Small Leak Detected | P | manufacturer | [C] | — | Finer leak threshold than P1440/P1442 (small leak). |
| P1464 | Fuel Level Sensor Circuit (Ground Signal) | P | manufacturer | [B] | — | — |
| P1480 | Engine Coolant Blower Motor Control Circuit Malfunction | P | manufacturer | [C] | — | Cooling fan control circuit; pairs with P1900 (blower motor circuit). |
| P1490 | Vacuum Cut Valve Bypass Valve (Circuit) | P | manufacturer | [B] | — | — |
| P1491 | Vacuum Cut Valve Bypass Valve | P | manufacturer | [B] | — | — |
| P1492 | EVAP Canister Purge Control/Solenoid Valve (Circuit) | P | manufacturer | [B] | — | — |
| P1493 | EVAP Canister Purge Control Valve/Solenoid Valve | P | manufacturer | [B] | — | — |
| P1550 | TCC Solenoid Valve | P | manufacturer | [B] | — | YEAR-SPLIT (recorded): older Nissan lists map P1550 to the TCC solenoid (this entry); 1999–2004 models' FSM coverage ('Battery Current Sensor') diverges by model year and engine. P1550 meaning is model/year-dependent — verify against the year-specific FSM. |
| P1551 | Battery Current Sensor | P | manufacturer | [A] | — | One of five codes (P1550–P1554) the FSM groups under "BAT CURRENT SENSOR"; sub-conditions (low/high/performance) are on the diagnosis pages, not the index. |
| P1552 | Battery Current Sensor | P | manufacturer | [A] | — | See P1551. |
| P1553 | Battery Current Sensor | P | manufacturer | [A] | — | See P1551. |
| P1554 | Battery Current Sensor | P | manufacturer | [A] | — | See P1551. |
| P1564 | ASCD Steering Switch | P | manufacturer | [A] | — | Automatic speed control device (cruise control) steering switch circuit. |
| P1568 | Cruise Control Master Switch Signal Out of Specification | P | manufacturer | [C] | — | — |
| P1572 | ASCD Brake Switch | P | manufacturer | [A] | — | Automatic speed control device brake switch circuit. |
| P1574 | ASCD Vehicle Speed Sensor | P | manufacturer | [A] | — | Automatic speed control device vehicle speed sensor signal. |
| P1605 | A/T Diagnostic Communication Line | P | manufacturer | [B] | — | — |
| P1610 | NATS Lock Mode — NATS shifted to a mode preventing engine start after 5+ consecutive start attempts with an unregistered key or malfunctioning IMMU/ECM | P | manufacturer | [A] | unregistered ignition key used repeatedly; IMMU or ECM malfunction; low battery voltage mimicking NATS failure | Nissan TSB (2005-2008 NATS vehicles, via Mitchell 1): a no-start with P1610 is often NOT NATS-related — check battery voltage/state of charge with GR-8 first; do NOT replace NATS components until battery service is ruled out. P1610 with other NATS codes (P1611-P1615, B2191-B2193, B2590) points to the service manual. |
| P1611 | NATS ID Discord IMMU-ECM — ID verification between IMMU/BCM (NATS control unit) and ECM is NG; system initialization required | P | manufacturer | [A] | ECM replaced without NATS initialization; key ID registration lost | Common after ECM replacement — reprogramming/initialization of keys is required (dealer or locksmith with NATS capability). Initialization erases ALL registered key IDs; have all customer keys present. |
| P1612 | NATS Chain of ECM-IMMU — communication impossible between ECM and IMMU (NATS control unit) | P | manufacturer | [A] | wiring between ECM and IMMU; IMMU malfunction | Service manual note: CHAIN OF ECM-IMMU can be stored spuriously during the key registration procedure even when nothing is malfunctioning — do not chase it if it appears mid-registration. |
| P1613 | NATS ECM INT CIRC-IMMU — malfunction of the ECM internal circuit of the IMMU communication line | P | manufacturer | [A] | — | — |
| P1614 | NATS Chain of IMMU-Key — IMMU cannot receive the key ID signal | P | manufacturer | [A] | NATS antenna amplifier (on ignition cylinder) faulty; unregistered or damaged key/FOB; blown fuse; weak FOB battery | If it is the only code, try a different registered key first and check fuses; the antenna amp communicates with the BCM — inspect it before condemning the ECM. |
| P1615 | NATS Difference of Key — IMMU receives the key ID signal but ID verification between key ID and IMMU is NG | P | manufacturer | [A] | unregistered or wrong key used | Key must be registered to the vehicle via CONSULT-II/III NATS software; all keys must be present at registration. |
| P1700 | CVT Shift Control Malfunction | P | manufacturer | [C] | — | — |
| P1705 | Throttle Position Sensor Circuit (A/T) | P | manufacturer | [B] | — | — |
| P1706 | Park/Neutral Position (PNP) Switch | P | manufacturer | [B] | — | — |
| P1715 | Input Pulley Speed Sensor (CVT) | P | manufacturer | [A] | — | CVT input (primary) pulley speed sensor circuit. |
| P1716 | AT Turbine Revolution Sensor Circuit Malfunction | P | manufacturer | [A] | — | Automatic transmission turbine (input) revolution sensor. |
| P1720 | Vehicle Speed Sensor (VSS) Signal Variation | P | manufacturer | [C] | — | — |
| P1730 | AT Fail-Safe Function Circuit Malfunction | P | manufacturer | [A] | — | Automatic transmission fail-safe control circuit. |
| P1740 | Lock-Up Select Solenoid Valve Circuit (CVT) | P | manufacturer | [A] | — | CVT lock-up select solenoid valve circuit. |
| P1752 | AT Input Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | Note: the source list gives P1752 and P1754 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions. |
| P1754 | AT Input Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | See P1752. |
| P1757 | AT Front Brake Solenoid Valve Malfunction | P | manufacturer | [A] | — | Note: the source list gives P1757 and P1759 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions. |
| P1759 | AT Front Brake Solenoid Valve Malfunction | P | manufacturer | [A] | — | See P1757. |
| P1760 | Overrun Clutch Solenoid Valve (Circuit) | P | manufacturer | [B] | — | — |
| P1762 | AT Direct Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | Note: the source list gives P1762 and P1764 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions. |
| P1764 | AT Direct Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | See P1762. |
| P1767 | AT High and Low Reverse Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | Note: the source list gives P1767 and P1769 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions. |
| P1769 | AT High and Low Reverse Clutch Solenoid Valve Malfunction | P | manufacturer | [A] | — | See P1767. |
| P1772 | AT Low Coast Brake Solenoid Valve Malfunction | P | manufacturer | [A] | — | Note: the source list gives P1772 and P1774 the identical description; the FSM groups both under A/T solenoid valves without distinguishing sub-conditions. |
| P1774 | AT Low Coast Brake Solenoid Valve Malfunction | P | manufacturer | [A] | — | See P1772. |
| P1775 | Torque Converter Clutch Solenoid — Voltage Low | P | manufacturer | [C] | — | — |
| P1776 | Torque Converter Clutch Solenoid — Converter Slip During Lock Condition | P | manufacturer | [C] | — | — |
| P1777 | CVT Step Motor Circuit | P | manufacturer | [A] | — | CVT step motor circuit fault. |
| P1778 | CVT Step Motor Function | P | manufacturer | [A] | — | CVT step motor mechanical/functional fault. |
| P1780 | AT Shift Change Signal Malfunction | P | manufacturer | [C] | — | — |
| P1800 | Intake Manifold Air Control Solenoid Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1805 | Brake Switch Circuit | P | manufacturer | [A] | — | Brake (stop lamp) switch circuit input to ECM. |
| P1815 | Manual Mode Switch — impossible switch-signal pattern detected (manual/non-manual/up/down) | P | manufacturer | [A] | harness or connectors (switch circuits open or shorted); mode select switch (in A/T control device); position select switch (in A/T control device); sticky/bad microswitch in the shifter assembly | NOT an OBD-II self-diagnostic item — CONSULT-III only. The up/down switches are in series with the manual throw; the code means one switch shows active while the auto throw also shows active, which is impossible with working switches. Check for spills/debris in the shifter assembly. |
| P1900 | Engine Coolant Blower Motor Circuit | P | manufacturer | [C] | — | Cooling fan/blower motor circuit; pairs with P1480 (blower motor control circuit). |
| U1000 | CAN Communication Line — missing CAN communications on the network (signal malfunction) | U | manufacturer | [A] | CAN communication harness open or shorted; faulty ECM; poor harness ground connection (engine compartment and behind-dash grounds); low battery voltage | Nissan TSB NTB10-066C: always diagnose communication codes FIRST; when a module reports U1000 it is typically operating normally — the fault is external to that module. Set when communication is lost for longer than 2 seconds. A well-known field fix is cleaning/resecuring the harness grounds (paint under dash-brace grounds causes high resistance). |
| U1001 | CAN Communication Line — ECM-specific missing CAN communications on the network | U | manufacturer | [A] | CAN harness open/shorted; faulty ECM; poor grounds; failed combination meter or other control unit pulling the bus down | Same TSB NTB10-066C guidance as U1000. A failed control unit (e.g. combination meter) can cause U1001 — CAN diagnostics with an advanced scanner identifies the silent module. |
| U1002 | CAN Communication Line — missing CAN communications, tighter specification than U1000 | U | manufacturer | [A] | — | Per TSB NTB10-066C, same diagnostic path as U1000 with a tighter detection spec. |
| U1010 | Control Unit — module internal error | U | manufacturer | [A] | — | TSB NTB10-066C: if a module is highlighted as faulty while other modules/segments show communication errors, diagnose the others first, erase DTCs, and re-run CAN diagnosis — replace the module only if it is still flagged alone. |

## stellantis — 106 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1B00 | Driver Airbag Squib 1 Circuit Low | B | manufacturer | [A] | Clockspring failure (known issue — FCA TSB 08-119-15 extended clockspring warranty to 10 yr/150,000 mi on 2007 JK Wrangler for this code family); squib wiring shorted low; driver airbag; ORC | Part of the B1B00-B1B07 driver-squib series. Always disconnect the 12 V battery and wait two minutes before working on squib circuits. Use an SRS load tool (not a plain multimeter) on live squib circuits per service procedure. |
| B1B01 | Driver Airbag Squib 1 Circuit High | B | manufacturer | [A] | Clockspring failure; squib wiring shorted high; driver airbag; ORC | See B1B00 notes (same series/procedure). |
| B1B02 | Driver Airbag Squib 1 Circuit Open | B | manufacturer | [A] | Open circuit in the clockspring (most common); improper clockspring neutral position; disengaged/poor-contact squib connector; open in driver airbag squib circuit; ORC malfunction | The classic JK/JK-era code. If the clockspring was already replaced and the code persists, suspect the airbag module itself or the clockspring-to-airbag harness. Factory test: disconnect driver squib connectors, connect SRS load tool, re-read ORC DTCs — if the code clears with the load tool, replace the driver airbag. |
| B1B03 | Driver Airbag Squib 1 Circuit Shorted Together | B | manufacturer | [A] | Squib circuits shorted together; clockspring; wiring; ORC | See B1B00 notes (same series/procedure). |
| B1B04 | Driver Airbag Squib 2 Circuit Low | B | manufacturer | [A] | Clockspring failure; squib wiring shorted low; driver airbag; ORC | See B1B00 notes (same series/procedure). |
| B1B05 | Driver Airbag Squib 2 Circuit High | B | manufacturer | [A] | Clockspring failure; squib wiring shorted high; driver airbag; ORC | See B1B00 notes (same series/procedure). |
| B1B06 | Driver Airbag Squib 2 Circuit Open | B | manufacturer | [A] | Open circuit in the clockspring; improper clockspring neutral position; disengaged/poor-contact squib connector; driver airbag; ORC malfunction | Same family as B1B02 (squib 2 instead of squib 1). See B1B02 notes. |
| B1B07 | Driver Airbag Squib 2 Circuit Shorted Together | B | manufacturer | [A] | Squib circuits shorted together; clockspring; wiring; ORC | See B1B00 notes (same series/procedure). |
| C1000 | Brake Pedal Switch 1 Circuit - Performance | C | manufacturer | [C] | Brake signal 1 circuit shorted to voltage; brake lamp switch operation; ABS module; TIPM/BCM | The ABS module detects an invalid signal between master-cylinder pressure applied and the brake-lamp switch output for ~2 minutes. CONFLICT: a Mitsubishi service source uses C1000 for "stop lamp switch circuit abnormality" — the description above is the FCA (RAM/Journey) use; verify against the vehicle line before applying. |
| C1008 | Brake Fluid Level Circuit High | C | manufacturer | [C] | Brake fluid level switch circuit shorted high; switch failure | not documented beyond description |
| C100A | Left Front Wheel Speed Sensor Circuit | C | manufacturer | [B] | Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction | ABS module monitors voltage fluctuation in each wheel-speed-sensor circuit; sets on detected open/short. After any ABS work, perform a key-off/key-on cycle and re-establish scan-tool communication before rechecking codes — the ABS only re-tests sensors after a key cycle. Wiring should test under 5 ohms with no shorts to power or ground. |
| C1011 | Left Front Wheel Speed Sensor Signal Erratic Performance | C | manufacturer | [B] | Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module | Signal-quality (erratic) counterpart to C100A's circuit fault. See C100A notes. |
| C1014 | Left Front Wheel Speed Sensor Comparative Performance | C | manufacturer | [B] | One wheel-speed reading disagreeing with the other three; tire size mismatch; sensor fault | Comparative/rationality code — the module compares all four wheel speeds. See C100A notes. |
| C1015 | Right Front Wheel Speed Sensor Circuit | C | manufacturer | [B] | Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction | Right-front counterpart of C100A. See C100A notes. |
| C101C | Right Front Wheel Speed Sensor Signal Erratic Performance | C | manufacturer | [B] | Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module | See C1011 notes (left-front counterpart). |
| C101F | Right Front Wheel Speed Sensor Comparative Performance | C | manufacturer | [B] | Wheel-speed disagreement; tire size mismatch; sensor fault | See C1014 notes (left-front counterpart). |
| C1020 | Left Rear Wheel Speed Sensor Circuit | C | manufacturer | [B] | Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction | Left-rear counterpart of C100A. See C100A notes. |
| C1027 | Left Rear Wheel Speed Sensor Signal Erratic Performance | C | manufacturer | [B] | Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module | See C1011 notes (front counterpart). |
| C102A | Left Rear Wheel Speed Sensor Comparative Performance | C | manufacturer | [B] | Wheel-speed disagreement; tire size mismatch; sensor fault | See C1014 notes (front counterpart). |
| C102B | Right Rear Wheel Speed Sensor Circuit | C | manufacturer | [B] | Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction | Right-rear counterpart of C100A. See C100A notes. |
| C1032 | Right Rear Wheel Speed Sensor Signal Erratic Performance | C | manufacturer | [B] | Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module | See C1011 notes (front counterpart). |
| C1035 | Right Rear Wheel Speed Sensor Comparative Performance | C | manufacturer | [B] | Wheel-speed disagreement; tire size mismatch; sensor fault | See C1014 notes (front counterpart). |
| C1041 | Left Front Tone Wheel Performance | C | manufacturer | [B] | Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault | not documented beyond description |
| C1042 | Right Front Tone Wheel Performance | C | manufacturer | [B] | Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault | not documented beyond description |
| C1043 | Left Rear Tone Wheel Performance | C | manufacturer | [B] | Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault | not documented beyond description |
| C1044 | Right Rear Tone Wheel Performance | C | manufacturer | [B] | Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault | not documented beyond description |
| C1046 | Left Front Wheel Pressure Phase Monitoring | C | manufacturer | [B] | ABS hydraulic control fault; wheel-speed plausibility fault | not documented beyond description |
| C1047 | Right Front Wheel Pressure Phase Monitoring | C | manufacturer | [B] | ABS hydraulic control fault; wheel-speed plausibility fault | not documented beyond description |
| C1048 | Left Rear Wheel Pressure Phase Monitoring | C | manufacturer | [B] | ABS hydraulic control fault; wheel-speed plausibility fault | not documented beyond description |
| C1049 | Right Rear Wheel Pressure Phase Monitoring | C | manufacturer | [B] | ABS hydraulic control fault; wheel-speed plausibility fault | not documented beyond description |
| C1073 | ABS Pump Motor Control Circuit | C | manufacturer | [B] | Pump motor circuit open/shorted; ABS module; TIPM power feed | not documented beyond description |
| C1078 | Tire Revolutions Range Performance | C | manufacturer | [B] | Tire size does not match programmed revolutions; aftermarket tire-size change without PCM/ABS reconfiguration | Plausibility code on tire revolutions per mile. Documented owner trigger: changing tire size with an aftermarket tuner without updating the vehicle configuration (Power Wagon Registry case also set U1412/U1417/U1418/P1C4E alongside). |
| C107C | Brake Pedal Switch 1/2 Stuck | C | manufacturer | [B] | Brake pedal switch stuck; switch misadjustment; wiring | not documented beyond description |
| C107D | Brake Pedal Switch 1/2 Correlation | C | manufacturer | [B] | Brake pedal dual-switch disagreement; switch failure; wiring | not documented beyond description |
| C1210 | G Sensor Input Circuit Performance | C | manufacturer | [B] | Lateral/longitudinal G-sensor fault; wiring; ABS/ESP module | not documented beyond description |
| C1219 | Steering Angle Sensor Erratic Performance | C | manufacturer | [B] | Steering angle sensor fault; clockspring; wiring; sensor not initialized | not documented beyond description |
| C121A | Steering Angle Sensor Not Initialized | C | manufacturer | [B] | Sensor replaced without calibration; alignment work without SAS reset; module replacement | Requires steering-angle-sensor calibration/initialization procedure after repair (scan tool). |
| C121C | Torque Request Signal Denied | C | manufacturer | [B] | ESP/PCM torque-request plausibility fault; CAN communication fault | not documented beyond description |
| C121D | Brake Pressure Sensor Circuit | C | manufacturer | [B] | Brake pressure sensor circuit open/shorted; sensor failure; ABS module | not documented beyond description |
| C121E | Brake Pressure Sensor Comparative Performance | C | manufacturer | [B] | Brake pressure sensor rationality fault; sensor failure | not documented beyond description |
| P1184 | Engine Oil Temperature Circuit Malfunction (Cummins diesel) | P | manufacturer | [C] | — | Appears in the Cummins-diesel DTC list (dodgeforum diesel tech list); do not confuse with P1184's use on other makes. not documented beyond description. |
| P1185 | Fuel Pump Temperature Sensor High / FTS High (Cummins diesel) | P | manufacturer | [C] | — | The diesel-list formatting groups P1184 (engine oil temp) and P1185/P1186 (fuel pump temp sensor high/low). Reported, not resolved: some generic DTC databases map P1185 differently (e.g. to engine oil temp range) — the Cummins context is the verified Stellantis use. |
| P1294 | Target Idle Not Reached | P | manufacturer | [A] | Engine/brake-booster/vacuum hose leaks; throttle plate/linkage misposition; IAC wiring intermittent or observable defect; throttle body defective; failed PCM; carbon deposits; driver circuit open/shorted | Monitored with engine idling in Drive (auto trans), no MAP/TP sensor codes present. Sets when idle is >200 rpm above or <100 rpm below target for ~14-20 s (two consecutive failures / two bad trips, model-dependent). Scan-tool IAC wiggle test is the standard first check (service manual TC-25A/TC-138B test path). |
| P1390 | Cam and Crank Signals Don't Match | P | manufacturer | [B] | Timing chain/belt misalignment; CMP/CKP sensor faults; wiring | not documented beyond description |
| P1391 | Intermittent Loss of Camshaft Position Sensor or Crankshaft Position Sensor | P | manufacturer | [B] | Failing CMP or CKP sensor; connector/wiring intermittent; tone wheel damage | Classic no-start/stall code on 4.0L/4.7L/5.2L/5.9L era engines; often one of the two sensors fails hot. not documented further in sources checked. |
| P1398 | Mis-Fire Adapter Numerator at Limit | P | manufacturer | [B] | CKP sensor / tone wheel issues; PCM misfire-adaptive at correction limit | not documented beyond description |
| P1491 | Radiator Fan Control Relay Circuit | P | manufacturer | [A] | Fused B(+) or fused ignition-switch output circuit open; radiator fan relay defective; relay control circuit open or shorted to ground; radiator fan relay ground circuit open; fan motor wiring intermittent/observable defect; PCM defective; (2003+ models: Intelligent Power Module shorted/open) | Monitored with ignition on, battery >10-10.4 V, while PCM commands fans on. Sets on open/short detected in the relay control circuit. |
| P1492 | Battery Temperature Sensor Voltage Too High | P | manufacturer | [B] | Battery temp sensor circuit shorted to voltage; sensor failure | not documented beyond description |
| P1493 | Battery Temperature Sensor Voltage Too Low | P | manufacturer | [B] | Battery temp sensor circuit shorted to ground or open; sensor failure | not documented beyond description |
| P1494 | Leak Detection Pump (LDP) Switch or Mechanical Fault — EVAP Leak Detection Pump Pressure Switch Condition | P | manufacturer | [A] | Wiring harness intermittent; LDP switch sense circuit shorted to ground or open; LDP vacuum supply; leak detection pump itself; faulty gas cap or vacuum leak elsewhere in EVAP system; PCM | Monitored immediately after cold start (battery/ambient 40-90 F, coolant within 10 F of ambient). Sets when the pressure-switch state does not change when the solenoid is energized. Inspect LDP hoses/wiring under the vehicle for debris damage before replacing the pump; aftermarket gas caps that bleed down faster than the Mopar cap are a known false trigger. Chrysler's LDP-based EVAP monitor is distinctive to the brand — no other OEM uses this exact pump design. |
| P1495 | Leak Detection Pump Solenoid Circuit | P | manufacturer | [B] | LDP solenoid electrical failure; solenoid harness open/shorted; poor electrical connection; PCM driver | Electrical-circuit counterpart to P1494's switch/mechanical fault. Check solenoid connector and wiring for damage/corrosion first. |
| P1496 | 5 Volt Supply Output Too Low | P | manufacturer | [B] | Shorted 5 V reference circuit (any sensor on the 5 V bus); PCM | not documented beyond description |
| P1594 | Charging System Voltage Too High | P | manufacturer | [B] | Alternator overcharging; wiring; battery; PCM field control | not documented beyond description |
| P1595 | Speed Control Solenoid Circuits | P | manufacturer | [B] | Speed control vacuum/vent solenoid control circuits shorted or open; hoses; cruise control master switch | not documented beyond description |
| P1596 | Speed Control Switch Always High | P | manufacturer | [B] | Cruise control master switch stuck/faulty; wiring shorted to voltage | not documented beyond description |
| P1597 | Speed Control Switch Always Low | P | manufacturer | [B] | Speed control switch stuck/faulty; wiring shorted to ground | not documented beyond description |
| P1598 | A/C Pressure Sensor Volts Too High | P | manufacturer | [B] | A/C pressure signal circuit shorted to 5 V supply or battery voltage; A/C pressure sensor internal failure; signal circuit open; sensor ground circuit open; PCM | Factory diagnostic path (NGC-era): verify refrigerant charge first, then read A/C pressure sensor voltage with scan tool — fault threshold is above ~4.6 V; resistance-test the signal circuit against the 5 V supply for a short (<5 ohms = shorted). Note: the same code number means something different on Peugeot and other makes — this entry is the Stellantis definition only. |
| P1599 | A/C Pressure Sensor Volts Too Low | P | manufacturer | [B] | A/C pressure sensor circuit shorted to ground or open; low refrigerant charge; sensor failure | not documented beyond description |
| P1602 | PCM Not Programmed | P | manufacturer | [B] | New/replacement PCM never flashed; incorrect programming | Set by a fresh or incorrectly programmed PCM; resolve with dealer-level flashing (wiTECH). No sensor diagnosis applies. |
| P1682 | Charging System Voltage Too Low | P | manufacturer | [B] | Alternator; drive belt; battery; wiring; PCM field control | not documented beyond description |
| P1684 | Battery Disconnected Within Last 50 Starts (informational — not a fault) | P | manufacturer | [A] | Battery was disconnected or lost power (intentional service, dead battery, cleared PCM memory); weak battery/connections can also set it | STATUS ONLY — indicates PCM memory was cleared within the last ~50 ignition cycles and does NOT indicate a problem. Self-clears after ~50 starts. On the pre-CAN key-dance readout, "P1684 and done" means only this status is stored. Do not chase it as a drivability fault; if it will not clear alongside real symptoms, check battery cables/voltage. |
| P1685 | Wrong or Invalid Key Message Received From SKIM (Sentry Key Immobilizer Module) | P | manufacturer | [B] | Non-programmed or damaged key; SKIM/ignition antenna ring fault; SKIM module failure; bus communication fault | SKIM says the key presented is not recognized — engine typically cranks then stalls (start-stall) or will not start. Distinct from P1686 (no message at all). |
| P1686 | No SKIM Bus Message Received | P | manufacturer | [B] | SKIM not powered (poor connection, broken wire); SKIM module failure; PCI/CCD bus wiring fault; PCM fault | Diagnose with a scan tool that can reach the whole vehicle network — determine which modules answer and which do not to localize the bus break. Cleaning the key/ignition cylinder is the field first step; battery-disconnect capacitor-drain reboot is a documented folk remedy, not factory procedure. |
| P1687 | No Cluster Bus Message (no MIC / instrument cluster bus message) | P | manufacturer | [B] | Instrument cluster failure or power loss; PCI/CCD bus wiring fault; PCM fault | Often paired with P1686; tach/temp gauges may work intermittently with warning lamps on. Address bus-level faults before condemning modules. |
| P1688 | Internal Fuel Injection Pump Controller Failure (Cummins diesel) | P | manufacturer | [B] | Injection pump controller internal failure; wiring | Cummins-diesel specific. not documented beyond description. |
| P1693 | DTC Detected In Companion Module (DTC detected in ECM or PCM) | P | manufacturer | [B] | Fault stored in the companion controller (ECM vs PCM split on diesels); companion module fault | Informational pointer — read the companion module for the real fault; most common on Cummins-diesel trucks with separate ECM/PCM. |
| P1694 | No CCD Messages Received From ECM | P | manufacturer | [B] | CCD/PCI bus wiring fault; ECM power/ground; ECM failure | Pre-CAN (CCD/PCI bus) era code. Determine which modules the scan tool can reach to localize the fault. |
| P1695 | No CCD/J1850 Message From Body Control Module (BCM) | P | manufacturer | [B] | BCM power/ground; CCD/PCI bus wiring fault; BCM failure | not documented beyond description |
| P1698 | No CCD Messages Received From PCM / No Bus Message From TCM | P | manufacturer | [B] | PCM/TCM power/ground; CCD bus wiring fault; module failure | The reported description varies slightly by source (PCM vs TCM as the silent module) — reported, not resolved; treat as "a powertrain module is silent on the CCD bus" and verify which module the scan tool cannot reach. |
| P1719 | Skip Shift Solenoid Circuit | P | manufacturer | [B] | Skip-shift (CAGS) solenoid circuit open/shorted; solenoid failure | Manual-transmission skip-shift (1st-to-4th) solenoid. not documented beyond description. |
| P1740 | TCC Or OD Solenoid Performance (torque reduction signal rationality) | P | manufacturer | [B] | Bad overdrive or torque-converter solenoid; torque converter clutch material unable to hold lockup | Chrysler-only code (not SAE-approved description). On RE transmissions the PCM looks for an RPM drop after OD/TCC apply; lockup occurs in 4th so the PCM cannot distinguish OD shift from TCC lockup by RPM alone. |
| P1756 | Governor Pressure Not Equal To Target At 15-20 PSI (mid-pressure malfunction) | P | manufacturer | [B] | Governor pressure solenoid; valve body; transmission fluid level; governor pressure sensor; transmission mechanical fault | RE-series automatic transmission code. not documented beyond description. |
| P1757 | Governor Pressure Above 3 PSI When Request Is 0 PSI (zero-pressure malfunction) | P | manufacturer | [B] | Governor pressure solenoid; valve body; sensor; mechanical fault | not documented beyond description |
| P1762 | Governor Pressure Sensor Offset Improper Voltage | P | manufacturer | [B] | Governor pressure sensor; signal wire open/short; valve body; transmission fluid level; no 5 V supply from PCM | Sets when the sensor input is out of range for 3 consecutive park/neutral calibrations. |
| P1763 | Governor Pressure Sensor Voltage Too High | P | manufacturer | [B] | Signal wire open or shorted; sensor failure; valve body | not documented beyond description |
| P1764 | Governor Pressure Sensor Voltage Too Low | P | manufacturer | [B] | Signal wire shorted; sensor failure; transmission fluid level; mechanical fault | not documented beyond description |
| P1765 | Transmission 12 Volt Supply Relay Control Circuit | P | manufacturer | [B] | Trans relay control circuit open or shorted; relay failure | not documented beyond description |
| P1899 | Park/Neutral Position Switch Stuck In Park or In Gear | P | manufacturer | [B] | P/N switch failure or misadjustment; wiring | not documented beyond description |
| U1008 | LIN 1 Bus | U | manufacturer | [C] | LIN bus wiring fault; LIN slave module failure | not documented beyond description |
| U110A | Lost Communication With SCM (Steering Control Module) | U | manufacturer | [C] | SCM power/ground; CAN bus wiring fault; SCM failure | not documented beyond description |
| U110C | Lost Fuel Level Message | U | manufacturer | [B] | CAN bus communication fault; Front Control Module (FCM) failure; wiring/connectors corroded or damaged | Frequently appears with U0141/U1403/U110E as a CAN/FCM cluster of faults — inspect FCM connectors and CAN wiring before replacing modules. |
| U110D | Lost Communication With Security Siren | U | manufacturer | [C] | Security siren module power/ground; CAN bus wiring fault | not documented beyond description |
| U110E | Lost Ambient Temperature Message | U | manufacturer | [B] | CAN C bus circuit open or shorted; Body Control Module; PCM; ambient temperature sensor itself | Theory of operation: the ambient temp sensor is a direct BCM input; the BCM transmits it to the PCM over the CAN C bus. A failed ambient temp sensor (located near the radiator/under hood) is a common real fix. |
| U110F | Lost Fuel Volume Message | U | manufacturer | [C] | CAN bus communication fault; sending module failure | not documented beyond description |
| U1110 | Lost Vehicle Speed Message | U | manufacturer | [B] | CAN C bus circuit open or shorted; Electronic Pedestrian Protection Module (EPPM); ESP/ABS module; PCM | Often the PRIMARY fault with U1120/U0121 as collateral — fix the vehicle-speed source first. Symptoms: dead speedometer, traction/ABS warnings. EPPM (floor panel under left front seat on some models) is a known failure point; inspect its connector for burned pins. |
| U1113 | Lost A/C Pressure Message | U | manufacturer | [C] | CAN bus communication fault; sending module failure | not documented beyond description |
| U1120 | Lost Wheel Distance Message | U | manufacturer | [B] | Anti-lock Brake Module; CAN C bus circuit open or shorted; PCM | Wheel-distance comes from the ABS module over CAN C. No-speedometer + ABS/traction warnings are typical. Check TCCM/TIPM connectors for corrosion; a tire-size change via tuner has been observed to trigger this family of codes. |
| U113B | Lost Communication With Switch Bank Module | U | manufacturer | [C] | Switch bank module power/ground; CAN bus wiring fault | not documented beyond description |
| U1141 | Lost ESP Torque Request Message | U | manufacturer | [B] | CAN bus open or shorted condition; ESP/ABS module; PCM | not documented beyond description |
| U1149 | Lost Communication With Multifunction (module) | U | manufacturer | [C] | Module power/ground; CAN bus wiring fault | not documented beyond description |
| U1159 | Lost Communication With ASBS | U | manufacturer | [C] | Module power/ground; CAN bus wiring fault | not documented beyond description |
| U1169 | Lost Communication With Intrusion Sensor 1 | U | manufacturer | [C] | Intrusion sensor power/ground; CAN/LIN wiring fault | not documented beyond description |
| U1170 | Lost Communication With Intrusion Sensor 2 | U | manufacturer | [C] | Intrusion sensor power/ground; CAN/LIN wiring fault | not documented beyond description |
| U1179 | Lost Communication With Intrusion Sensor 3 | U | manufacturer | [C] | Intrusion sensor power/ground; CAN/LIN wiring fault | not documented beyond description |
| U1403 | Implausible Fuel Level Signal Received | U | manufacturer | [B] | CAN B bus open or shorted; CAN B bus hardware DTCs also active; cluster module; Front Control Module; PCM | Monitored with ignition on; continuously monitored; one-trip fault. Diagnostic path: confirm the DTC is active, then check for CAN B hardware DTCs before condemning the cluster/FCM/PCM. |
| U1411 | Implausible Fuel Volume Signal Received | U | manufacturer | [B] | CAN B bus open or shorted; cluster module; Front Control Module; PCM | Same diagnostic family as U1403 (fuel-level/volume messages ride CAN B via cluster/FCM). not documented beyond probable causes. |
| U1412 | Implausible Vehicle Speed Signal Received | U | manufacturer | [B] | Wheel speed sensor / ABS signal fault; CAN C bus fault; ABS module; PCM | Seen together with U1417/U1418 after tire-size changes via aftermarket tuners — the PCM rejects wheel-distance/speed data inconsistent with its configuration. Verify tire size programming matches the fitted tires. |
| U1414 | Implausible/Missing ECU Network Configuration Data | U | manufacturer | [C] | Module replaced without configuration; network configuration data missing/corrupt | not documented beyond description |
| U1415 | Implausible/Missing Vehicle Configuration Data | U | manufacturer | [C] | Module replaced without PROXI/configuration alignment; corrupt config data | not documented beyond description |
| U1416 | Implausible Security Siren Signal Received | U | manufacturer | [C] | Security siren module fault; wiring | not documented beyond description |
| U1417 | Implausible Left Wheel Distance Signal Received | U | manufacturer | [B] | Vehicle speed sensor fault active in anti-lock brake module; CAN C bus circuit shorted or open; ABS module; PCM; wheel speed sensor(s) | Monitored with ignition on; PCM receives implausible wheel-distance over CAN C from the ABS module; one-trip fault. Diagnostic path: verify the DTC is active, confirm the ABS module is active on CAN C, check for ABS-module DTCs, check FCM for active DTCs. Often appears with U1418 (both sides) — on RAM trucks, front wheel speed sensors were the confirmed fix in owner cases. |
| U1418 | Implausible Right Wheel Distance Signal Received | U | manufacturer | [B] | Same family as U1417 — wheel speed sensor(s); ABS module; CAN C bus open/shorted; PCM | Steering-wheel lock-to-lock rotation x3 is a reported owner workaround for clearing it when the sensor is still good (unverified factory procedure — treat as anecdotal). Triggers CEL and/or ABS/traction warnings. |
| U1419 | Implausible Data Received From OCS Sensor 3 - Left Front | U | manufacturer | [C] | Occupant classification sensor fault; wiring | not documented beyond description |
| U141A | Implausible Data Received From OCS Sensor 2 - Right Front | U | manufacturer | [C] | Occupant classification sensor fault; wiring | not documented beyond description |
| U141B | Implausible Data Received From OCS Sensor 4 - Left Rear | U | manufacturer | [C] | Occupant classification sensor fault; wiring | not documented beyond description |
| U141C | Implausible Data Received From OCS Sensor 1 - Right Rear | U | manufacturer | [C] | Occupant classification sensor fault; wiring | not documented beyond description |

## subaru — 72 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1100 | Integ. Unit System Error | B | manufacturer | [A] | internal fault in the body integrated unit | From the FSM LAN-diagnostics DTC table; BIU-internal fault (vs. communication faults U12xx). |
| B1500 | Keyless UART Communication Malfunction | B | manufacturer | [A] | internal problem in the keyless entry control module, or a problem in the communication line | Keyless-entry UART link fault (BIU system). |
| C0041 | Parameter Selection Error | C | manufacturer | [A] | parameter selection failure (VDC control module configuration) | VDC system. Detailed codes 5148/5149. |
| C0042 | Power Supply Voltage Failure | C | manufacturer | [A] | power voltage malfunction to the VDC control module | VDC system. Check power/ground to the VDCCM&H/U before condemning the module. Detailed code 5000/5001. |
| C0044 | TCM Communication Circuit | C | manufacturer | [A] | CAN communication failure of transmission control module | VDC system view of a TCM communication loss. Detailed codes 5137/5140/5142. |
| C0045 | TCM Malfunction / Incorrect VDC Control Module Specifications | C | manufacturer | [A] | malfunction of transmission control module; different VDC control module specification | VDC system. Detailed codes 5144/5146. |
| C0046 | Body Integrated Module Communication Circuit | C | manufacturer | [A] | body integrated module communication circuit fault | VDC system view of a BIU communication loss. Detailed code 5155. |
| C0047 | Improper CAN Communication | C | manufacturer | [A] | CAN communication line circuit is open or shorted | Detecting condition (FSM): CAN communication line circuit open or shorted. Symptoms: ABS and VDC do not operate. Detailed codes 1504H–15C0H family; FSM detailed code 5135. Diagnose the physical CAN pair, not the module, first. |
| C0051 | Valve Relay | C | manufacturer | [A] | VDC valve relay circuit fault | VDC hydraulic control unit valve relay. Detailed codes 021FH/0220H/0221H/0280H. |
| C0052 | Motor and Motor Relay OFF Failure / ON Failure / Motor Malfunction | C | manufacturer | [A] | VDC pump motor / motor relay fault | VDC hydraulic unit pump motor circuit. Detailed codes 0562H/0574H/0580H/05A0H/0560H/04B0H. |
| C0054 | BLS Circuit Open / BLS ON Malfunction | C | manufacturer | [A] | brake lamp switch (BLS) circuit open or stuck ON | VDC system monitors the brake lamp switch input. Detailed codes 04B0H/043CH. |
| P1152 | O2 Sensor Circuit Range/Performance (Low) (Bank 1 Sensor 1) | P | manufacturer | [B] | — | — |
| P1153 | O2 Sensor Circuit Range/Performance (High) (Bank 1 Sensor 1) | P | manufacturer | [B] | — | — |
| P1160 | Return Spring Failure | P | manufacturer | [C] | — | Throttle-body return-spring plausibility (drive-by-wire era). |
| P1400 | Fuel Tank Pressure Control Solenoid Valve Circuit Low | P | manufacturer | [B] | — | EVAP system (fuel tank pressure control solenoid), distinct from the generic P044x EVAP family. |
| P1410 | Secondary Air Injection System Switching Valve Stuck Open | P | manufacturer | [B] | — | Secondary-air injection (cold-start emissions) — a common Subaru-specific code family. |
| P1420 | Fuel Tank Pressure Control Solenoid Valve Circuit High | P | manufacturer | [B] | — | Pair to P1400 (circuit low). |
| P1443 | Vent Control Solenoid Valve Function Problem | P | manufacturer | [B] | — | EVAP vent control solenoid functional fault (vs. circuit faults). |
| P1491 | Positive Crankcase Ventilation (Blowby) Function Problem | P | manufacturer | [B] | — | PCV/blowby functional monitor, not a circuit code. |
| P1500 | Radiator Fan Relay 1 Circuit Malfunction | P | manufacturer | [B] | — | — |
| P1501 | Idle Control System Malfunction (Fail Safe) | P | manufacturer | [C] | — | Fail-safe idle control fault. |
| P1502 | Radiator Fan Function Problem | P | manufacturer | [C] | — | Fan functional fault (vs. P1500 circuit fault). |
| P1507 | Idle Control System Malfunction (Fail Safe) | P | manufacturer | [C] | — | — |
| P1510 | Idle Air Control Solenoid Signal 1 Circuit Low Input | P | manufacturer | [C] | — | — |
| P1511 | Idle Air Control Solenoid Signal 1 Circuit High Input | P | manufacturer | [C] | — | — |
| P1512 | Idle Air Control Solenoid Signal 2 Circuit Low Input | P | manufacturer | [C] | — | — |
| P1513 | Idle Air Control Solenoid Signal 2 Circuit High Input | P | manufacturer | [C] | — | — |
| P1514 | Idle Air Control Solenoid Signal 3 Circuit Low Input | P | manufacturer | [C] | — | — |
| P1515 | Idle Air Control Solenoid Signal 3 Circuit High Input | P | manufacturer | [C] | — | — |
| P1516 | Idle Air Control Solenoid Signal 4 Circuit Low Input | P | manufacturer | [C] | — | — |
| P1517 | Idle Air Control Solenoid Signal 4 Circuit High Input | P | manufacturer | [C] | — | — |
| P1518 | Starter Switch Circuit Low Input | P | manufacturer | [A] | — | Starter-request switch input circuit. |
| P1520 | Cooling Fan Relay 1 Circuit High Input | P | manufacturer | [C] | — | Pair to P1500 (circuit malfunction). |
| P1540 | Vehicle Speed Sensor Malfunction 2 | P | manufacturer | [C] | — | — |
| P1544 | Exhaust Gas Temperature Too High | P | manufacturer | [C] | — | High exhaust-temperature detection (turbo models). |
| P1560 | Back-Up Voltage Circuit Malfunction | P | manufacturer | [A] | — | ECM keep-alive/backup power circuit — check ECM backup power supply. |
| P1570 | Antenna | P | manufacturer | [A] | faulty immobilizer antenna / key communication coil | Immobilizer system. Key registration and antenna diagnosis are SSM3/SSM4 dealer procedures. |
| P1571 | Reference Code Incompatibility | P | manufacturer | [A] | reference code incompatibility between body integrated unit and ECM | Immobilizer system — BIU/ECM pairing mismatch. |
| P1572 | IMM Circuit Failure (Except Antenna Circuit) | P | manufacturer | [A] | communication failure between body integrated unit and ECM; combination meter and BIU registration failure | Immobilizer system (non-antenna circuit). |
| P1574 | Key Communication Failure | P | manufacturer | [A] | communication failure between key and body integrated unit | Immobilizer system. |
| P1576 | EGI Control Module EEPROM | P | manufacturer | [A] | ECM malfunctioning (EEPROM) | Immobilizer system — ECM-side EEPROM fault. |
| P1577 | IMM Control Module EEPROM | P | manufacturer | [A] | body integrated unit malfunctioning (EEPROM) | Immobilizer system — BIU-side EEPROM fault. |
| P1578 | Meter Failure | P | manufacturer | [A] | reference code incompatibility between combination meter and BIU; communication failure between BIU and ECM | Immobilizer system — combination-meter involvement. |
| P1590 | Neutral Position Switch Circuit High Input | P | manufacturer | [C] | — | — |
| P1591 | Neutral Position Switch Circuit Low Input | P | manufacturer | [C] | — | Pair to P1590. |
| P1592 | Neutral Position Switch Circuit (MT Model) | P | manufacturer | [C] | — | Manual-transmission variant. |
| P1594 | Automatic Transaxle Diagnosis Input Signal Circuit Malfunction | P | manufacturer | [C] | — | AT diagnosis input signal family (P1594/P1595/P1596). |
| P1595 | Automatic Transaxle Diagnosis Input Signal Circuit Low Input | P | manufacturer | [C] | — | — |
| P1596 | Automatic Transaxle Diagnosis Input Signal Circuit High Input | P | manufacturer | [C] | — | — |
| P1602 | Control Module Programming Error | P | manufacturer | [C] | — | ECM programming/flash integrity fault. |
| P1698 | Engine Torque Control Cut Signal Circuit Malfunction (Low Input) | P | manufacturer | [C] | — | ECM↔TCM torque-control interface (AT torque-down request line). |
| P1699 | Engine Torque Control Cut Signal Circuit Malfunction (High Input) | P | manufacturer | [C] | — | Pair to P1698. |
| P1700 | Throttle Position Sensor Circuit Malfunction (A/T) | P | manufacturer | [C] | — | AT-related TPS circuit code. |
| P1701 | Cruise Control Set Signal Circuit Malfunction (A/T) | P | manufacturer | [C] | — | — |
| P1702 | Auto Trans Diagnosis Input Signal Circuit | P | manufacturer | [C] | — | Related to the P1594/P1595/P1596/P1722/P1742 family. |
| P1703 | Low Clutch Timing Control Solenoid Valve Circuit Malfunction | P | manufacturer | [C] | — | AT clutch timing solenoid. |
| P1704 | 2-4 Brake Timing Solenoid Valve Circuit Malfunction | P | manufacturer | [C] | — | AT 2-4 brake timing solenoid. |
| P1705 | 2-4 Brake Pressure Solenoid Valve (Solenoid D) Circuit | P | manufacturer | [C] | — | AT 2-4 brake pressure solenoid. |
| P1711 | Engine Torque Control Signal 1 Circuit Malfunction | P | manufacturer | [C] | — | ECM↔TCM torque-control interface, channel 1. |
| P1712 | Engine Torque Control Signal 2 Circuit Malfunction | P | manufacturer | [C] | — | ECM↔TCM torque-control interface, channel 2. |
| P1718 | AT CAN Communication Circuit | P | manufacturer | [C] | CAN communication line fault (ECM↔TCM/BIU); wiring harness, grounds, power, CAN twisted pair | 2006 Legacy GT owner report: "P1718 code meaning an issue with the CAN communication circuit". Appears in the FSM LAN-diagnostics tables alongside U1201/U1221 — always read the LAN system DTCs together with it. On a 2005+ vehicle, check harness grounds (the DLC shares a ground point with the BIU) before condemning modules. |
| P1722 | Auto Trans Diagnosis Input Signal High Input | P | manufacturer | [C] | — | Related to the P1594/P1595/P1596/P1702/P1742 family. |
| P1742 | Auto Trans Diagnosis Input Signal Malfunction | P | manufacturer | [C] | — | Related to the P1594/P1595/P1596/P1702/P1722 family. |
| U1201 | CAN-HS Counter Abnormal | U | manufacturer | [A] | unstable high-speed CAN communication (high-speed CAN communication error); faulty control module on the HS bus | FSM detecting condition: "Communication is unstable due to a high-speed CAN communication error." Symptoms: combination-meter fault display; possible control issues. Diagnostic procedure: if U0073 is current, diagnose U0073 first; clear and recheck (temporary poor communication is common); if persistent, disconnect control modules other than the BIU one at a time (fitting 120 Ω across CAN-Hi/Lo when the ECM or VDC CM is disconnected) until U1201 clears — the last-removed module is faulty. |
| U1202 | not verified — appears in FSM LAN-diagnostics tables in the TCM/BIU columns adjacent to U1201 | U | manufacturer | [C] | — | Seen in 2010–2013 Legacy FSM LAN(diag) DTC tables (e.g. "U1202 or P1725" in the TCM column). Textual definition was not extracted in this pass. |
| U1221 | CAN-HS ECM No-Receive Data | U | manufacturer | [A] | CAN system communication-line failure (ECM to integrated unit); ECM failure | BIU-detected loss of ECM data on HS-CAN. A 2005 Legacy GT owner report documents a U1221 stranding event traced to a computer/communication issue. In the FSM LAN table it pairs with P1718 and C0047/C0140. |
| U1222 | CAN-HS TCM No-Receive Data | U | manufacturer | [A] | TCM faulty (per FSM probable-cause column) | BIU-detected loss of TCM data on HS-CAN. Pairs with U0101/C0047/C0140 in the FSM table. |
| U1223 | CAN-HS VDC/ABS No-Receive Data | U | manufacturer | [A] | VDC/ABS control module faulty (per FSM probable-cause column) | BIU-detected loss of VDC/ABS data on HS-CAN. Pairs with U0122/P1718 in the FSM table. |
| U1229 | not verified — appears in FSM LAN-diagnostics tables in EPB-related rows ("Hi and Loside circuits near electronic parking brake are open/are shorted to ground") | U | manufacturer | [C] | — | Textual definition was not extracted in this pass; context suggests electronic-parking-brake CAN faults. |
| U122A | not verified — appears in FSM LAN-diagnostics tables in FUEL-related rows | U | manufacturer | [C] | — | Textual definition was not extracted in this pass. |
| U122B | not verified — appears in FSM LAN-diagnostics tables in ABS-related rows | U | manufacturer | [C] | — | Textual definition was not extracted in this pass. |
| U1321 | CAN-LS Meter No-Receive Data | U | manufacturer | [A] | combination meter faulty (per FSM probable-cause column) | Low-speed-CAN fault — the combination meter is on CAN-LS, confirming a second, slower CAN network exists. This is the only LS-CAN DTC extracted in this pass. |

## toyota — 283 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| B1100 | Airbag Sensor Assembly Center Malfunction | B | manufacturer | [A] | airbag sensor assembly center (internal malfunction) | Recorded when the airbag sensor assembly center detects its own internal malfunction (sub-code /31 on 2004 Corolla). Manual hint: if any other SRS code is present at the same time, repair the other code FIRST. Inspection starts with IG2 supply voltage (10–14 V) — check battery/charging system if out of range. Disconnect battery and wait 90+ seconds before probing SRS circuits. |
| B1135 | Half Connection Detection Malfunction | B | manufacturer | [A] | — | CONFLICT — make-dependent meaning. On Toyota (2004 Corolla RM1037U SRS chart, B1135/24) this is "HALF CONNECTION DETECTION MALFUNCTION" (connector half-connection detection) [A]. On Nissan (2014 Cube SRS manual) B1135 is "SIDE AIR BAG MODULE LH [VB-SHORT]" [B]. Do not cross-apply. |
| B1140 | Side Airbag Sensor Assembly RH Malfunction | B | manufacturer | [A] | side airbag sensor assembly RH; airbag sensor assembly center; instrument panel wire No.3 | Satellite side-impact sensor (RH) internal malfunction (sub-code /32 on 2004 Corolla). |
| B1141 | Side Airbag Sensor Assembly LH Malfunction | B | manufacturer | [A] | side airbag sensor assembly LH; airbag sensor assembly center; instrument panel wire No.3 | Satellite side-impact sensor (LH) internal malfunction (sub-code /33 on 2004 Corolla). |
| B1150 | Occupant Classification ECU Circuit Malfunction | B | manufacturer | [A] | occupant classification ECU; FSR+/FSR- sensor circuit (open/short to ground or to B+); wire harness | From the 2005 4Runner repair manual (RM1165U) CI B1150/23 diagnostics: check FSR+ to FSR- isolation (1 MΩ or higher), then FSR lines to body ground (below 1 V with ignition ON). Occupant-classification (passenger weight-sensor) circuit. |
| B1153 | Seat Position Airbag Sensor Assembly Malfunction | B | manufacturer | [A] | seat position airbag sensor; airbag sensor assembly center; instrument panel wire No.3; wire harness (seat position airbag sensor – front seat inner belt assembly) | Seat-track position sensor used for dual-stage deployment decisions (sub-code /25 on 2004 Corolla). |
| B1180 | Short in D Squib (2nd Step) Circuit | B | manufacturer | [B] | horn button assembly (D squib 2nd step); spiral cable sub-assembly; airbag sensor assembly center; instrument panel wire | Driver airbag 2nd-stage squib line short (sub-code /17). A Toyota technician (JustAnswer) notes the clockspring (spiral cable) is the most common cause; airbag sensor and wiring are the other candidates. B1181 (dedup) is the open-circuit sibling; B1182 is the short-to-ground sibling. |
| B1181 | Open in D Squib (2nd Step) Circuit | B | manufacturer | [A] | open in D+ or D- wire harness of squib; D squib (2nd step) malfunction; spiral cable sub-assembly malfunction; airbag sensor assembly center malfunction | Driver airbag 2nd-stage squib circuit. Disconnect battery, wait 90+ seconds before probing SRS circuits. Check D2+/D2- resistance (below 1 ohm OK). A broken clockspring (spiral cable) is the most common cause on high-mileage vehicles. |
| B1182 | Short to GND in D Squib (2nd Step) Circuit | B | manufacturer | [B] | horn button assembly (D squib 2nd step); spiral cable sub-assembly; airbag sensor assembly center; instrument panel wire | Third member of the chart sequence B1180/17 (short), B1181/18 (open), B1182/19 (short to ground) — driver 2nd-stage squib. Individual detection-item text not captured beyond the sequence; the short/open/GND/B+ 4-code pattern is the Toyota SRS convention. |
| B1207 | Smart ECU Communication Stop | B | manufacturer | [A] | smart ECU malfunction; wire harness (MPX lines); gateway ECU | Stored when communication between the smart ECU and gateway ECU stops for more than 10 seconds. 2004 Prius multiplex system. |
| B1660 | P Seat Airbag Active Mode Indicator Circuit Malfunction | B | manufacturer | [A] | open/short to ground or short to B+ in passenger airbag ON/OFF indicator circuit; faulty telltale light assembly; faulty airbag ECU assembly; instrument panel wire harness | Passenger airbag ON/OFF indicator circuit fault (not the airbag itself). A common field fix on Highlanders is the indicator LED/board in the overhead console. |
| B1771 | Occupant Detection Malfunction | B | manufacturer | [C] | — | Seen on a Techstream readout alongside B1801/B1811 after steering/column work (listed as "Occupation Detection" in the owner transcription — likely "Occupant Detection"). Occupant-classification system area. |
| B1800 | Short in Driver Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly | Set when the airbag sensor assembly receives a line-short signal 5 times in the driver squib circuit during the primary check (sub-code /51). Disconnect battery, wait 90+ seconds before probing. A failed clockspring is the classic cause. |
| B1801 | Open in Driver Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly | Open signal received for 2 seconds (sub-code /51). A Toyota master technician (JustAnswer, Hilux B1801) identifies the spiral cable under the steering wheel as the recognized failure point; the wheel must come off to replace it. |
| B1802 | Short to GND in Driver Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly | Short-to-ground signal received for 0.5 seconds (sub-code /51). |
| B1803 | Short to B+ in Driver Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly | Short-to-B+ signal received for 0.5 seconds (sub-code /51). |
| B1805 | Short in Front Passenger Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly | Line short detected during the primary check (sub-code /52). Passenger-dash airbag squib. |
| B1806 | Open in Front Passenger Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly | Open detected in the passenger squib circuit (sub-code /52). A Yaris owner thread shows this presenting as "open circuit in passenger front squib" — check for anything disconnected under/around the passenger dash and seat. |
| B1807 | Short to GND in Front Passenger Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly | Short-to-ground detected (sub-code /52). |
| B1808 | Short to B+ in Front Passenger Side Squib Circuit | B | manufacturer | [A] | instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly | Short-to-B+ detected (sub-code /52). |
| B1810 | Short in Driver Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly | Driver dual-stage airbag 2nd-step squib (sub-code /53). NOTE — generic B-body databases (ecutesting.com, retrolib.info) list B1810–B1813 as lamp/wiper circuits; those are non-Toyota body-control definitions. On Toyota these are SRS squib circuits per the Toyota service-manual DTC charts — do not cross-apply. |
| B1811 | Open in Driver Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly | Open in the driver 2nd-step squib circuit (sub-code /53). A Yaris owner thread defines it as "Open in D squib (Dual stage - 2nd step) circuit" and notes the code cannot be cleared until the underlying open is repaired. See B1810 cross-apply warning. |
| B1812 | Short to GND in Driver Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly | Short-to-ground in the driver 2nd-step squib circuit (sub-code /53). See B1810 cross-apply warning. |
| B1813 | Short to B+ in Driver Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly | Short-to-B+ in the driver 2nd-step squib circuit (sub-code /53). See B1810 cross-apply warning. |
| B1815 | Short in Front Passenger Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly | Passenger dual-stage airbag 2nd-step squib (sub-code /54). |
| B1816 | Open in Front Passenger Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly | Open in the passenger 2nd-step squib circuit (sub-code /54). |
| B1817 | Short to GND in Front Passenger Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly | Short-to-ground in the passenger 2nd-step squib circuit (sub-code /54). |
| B1818 | Short to B+ in Front Passenger Side Squib 2nd Step Circuit | B | manufacturer | [A] | instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly | Short-to-B+ in the passenger 2nd-step squib circuit (sub-code /54). |
| B181A | Short in Passenger Side Airbag Variable Vent Hole Squib Circuit | B | manufacturer | [B] | — | Hex-digit DTC (B181A–B181D) for the passenger airbag variable-vent-hole squib, from the Toyota Venza/4Runner/Tacoma airbag DTC charts (check-mode *2). Trouble areas not captured in the excerpts. |
| B181B | Open in Passenger Side Airbag Variable Vent Hole Squib Circuit | B | manufacturer | [B] | — | See B181A. |
| B181C | Short to GND in Passenger Side Airbag Variable Vent Hole Squib Circuit | B | manufacturer | [B] | — | See B181A. |
| B181D | Short to B+ in Passenger Side Airbag Variable Vent Hole Squib Circuit | B | manufacturer | [B] | — | See B181A. |
| B1820 | Short in Side Squib RH Circuit | B | manufacturer | [A] | No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly | RH seat side-airbag squib (sub-code /55). Older manuals phrase it as "Side Squib (D Seat Side)" — D = driver side on LHD vehicles. |
| B1821 | Open in Side Squib RH Circuit | B | manufacturer | [A] | floor wire / No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly; seat-harness chafing under the seat | Toyota TSB EL002-08 (revised 2008) specifically covers DTC B1821/B1826 "OPEN SIDE SQUIB CIRCUIT" — SRS light on; the repair procedure addresses the seat side-airbag harness (harness chafing/pinching under the front seats). Check the seat harness routing before condemning the squib. |
| B1822 | Short to GND in Side Squib RH Circuit | B | manufacturer | [A] | No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly | Short-to-ground in the RH side squib circuit (sub-code /55). |
| B1823 | Short to B+ in Side Squib RH Circuit | B | manufacturer | [A] | No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly | Short-to-B+ in the RH side squib circuit (sub-code /55). |
| B1825 | Short in Side Squib LH Circuit | B | manufacturer | [A] | floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly | LH seat side-airbag squib (sub-code /56). |
| B1826 | Open in Side Squib LH Circuit | B | manufacturer | [A] | floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly; seat-harness chafing under the seat | Covered by Toyota TSB EL002-08 alongside B1821 — see B1821 notes. |
| B1827 | Short to GND in Side Squib LH Circuit | B | manufacturer | [A] | floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly | Short-to-ground in the LH side squib circuit (sub-code /56). |
| B1828 | Short to B+ in Side Squib LH Circuit | B | manufacturer | [A] | floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly | Short-to-B+ in the LH side squib circuit (sub-code /56). |
| B1830 | Short in Curtain Shield Squib RH Circuit | B | manufacturer | [A] | — | RH roof curtain-shield airbag squib (sub-code /57). Trouble areas not captured in the excerpts. |
| B1831 | Open in Curtain Shield Squib RH Circuit | B | manufacturer | [A] | — | See B1830. |
| B1832 | Short to GND in Curtain Shield Squib RH Circuit | B | manufacturer | [A] | — | See B1830. |
| B1833 | Short to B+ in Curtain Shield Squib RH Circuit | B | manufacturer | [A] | — | See B1830. |
| B1835 | Short in Curtain Shield Squib LH Circuit | B | manufacturer | [A] | — | LH roof curtain-shield airbag squib (sub-code /58). |
| B1836 | Open in Curtain Shield Squib LH Circuit | B | manufacturer | [A] | — | See B1835. |
| B1837 | Short to GND in Curtain Shield Squib LH Circuit | B | manufacturer | [A] | — | See B1835. |
| B1838 | Short to B+ in Curtain Shield Squib LH Circuit | B | manufacturer | [A] | — | See B1835. |
| B1840 | Short in Curtain Shield Squib RH 2nd Step Circuit | B | manufacturer | [A] | — | RH curtain-shield 2nd-step squib (sub-code /59). Trouble areas not captured in the excerpts. |
| B1841 | Open in Curtain Shield Squib RH 2nd Step Circuit | B | manufacturer | [A] | — | See B1840. |
| B1842 | Short to GND in Curtain Shield Squib RH 2nd Step Circuit | B | manufacturer | [A] | — | See B1840. |
| B1843 | Short to B+ in Curtain Shield Squib RH 2nd Step Circuit | B | manufacturer | [A] | — | See B1840. |
| B1845 | Short in Curtain Shield Squib LH 2nd Step Circuit | B | manufacturer | [B] | — | LH curtain-shield 2nd-step squib (sub-code /61). B1845 confirmed in the chart; B1846/B1847/B1848 follow the standard short/open/GND/B+ 4-code pattern but their individual detection-item rows were not captured in the excerpt. |
| B1846 | Open in Curtain Shield Squib LH 2nd Step Circuit | B | manufacturer | [C] | — | Pattern-inferred sibling of B1845 — see B1845 note. |
| B1847 | Short to GND in Curtain Shield Squib LH 2nd Step Circuit | B | manufacturer | [C] | — | Pattern-inferred sibling of B1845 — see B1845 note. |
| B1848 | Short to B+ in Curtain Shield Squib LH 2nd Step Circuit | B | manufacturer | [C] | — | Pattern-inferred sibling of B1845 — see B1845 note. |
| B1900 | Short in Front Pretensioner Squib RH Circuit | B | manufacturer | [A] | shorted seatbelt pretensioner wiring (melted/chafed insulation near the connector); front seat outer belt assembly RH (pretensioner squib); airbag sensor assembly | RH seatbelt pretensioner squib (sub-code /73 — shared across B1900–B1903; the SRS warning light blink code alone cannot distinguish them, use a scan tool). A Yaris field thread found melted pretensioner-wire insulation a few inches from the connector with the exposed conductors touching — inspect the yellow / yellow-black pair end to end. |
| B1901 | Open in P/T Squib (RH) Circuit | B | manufacturer | [C] | deployed seatbelt pretensioner (RH); open in pretensioner squib circuit; wiring | "P/T squib" = seatbelt pretensioner squib. If the vehicle was in a crash, check the pretensioner for deployment (orange visible through inspection holes = popped, replace the assembly). 2006-2011 Yaris SRS codes are identical across those years. |
| B1902 | Short to GND in Front Pretensioner Squib RH Circuit | B | manufacturer | [A] | shorted seatbelt pretensioner wiring; front seat outer belt assembly RH; airbag sensor assembly | See B1900 — sub-code /73 family. |
| B1903 | Short to B+ in Front Pretensioner Squib RH Circuit | B | manufacturer | [A] | shorted seatbelt pretensioner wiring; front seat outer belt assembly RH; airbag sensor assembly | See B1900 — sub-code /73 family. (B1901, the open-circuit sibling, is in the v1.2.1 file.) |
| C0278 | Open or Short in ABS Solenoid Relay Circuit | C | manufacturer | [C] | ABS solenoid relay; wiring; skid control ECU | Seen on LX470/land-cruiser-family ABS. Often appears in a cascade with other ABS codes when battery voltage is low — address C1241 first. |
| C1201 | Engine Control System Malfunction | C | manufacturer | [B] | any stored engine (P-code) malfunction — this code is a consequence, not a root cause | INFORMATIONAL. Set by the skid control ECU whenever the engine control system has a malfunction; TRAC/A-TRAC/VSC are disabled as fail-safe. CONFLICT: an AI-generated JustAnswer snippet describes C1201 as a crankshaft-position/MAP-sensor circuit code — that contradicts the Toyota brake-control DTC chart (BC-85), which defines it as Engine Control System Malfunction [A/B]. Diagnose and repair the underlying P-code; C1201 then clears. |
| C1202 | Brake Fluid Level Low / Open Circuit in Brake Fluid Level Warning Switch Circuit | C | manufacturer | [A] | brake fluid level; brake fluid level warning switch; harness and connector; skid control ECU; ABS No.1 relay; ABS No.2 relay | Check the reservoir level first — the code covers both genuinely low fluid and an open in the warning-switch circuit (sub-code /68 on Prius). |
| C1203 | ECM Communication Circuit Malfunction | C | manufacturer | [B] | ECM; CAN communication circuit; skid control ECU | Brake-control-system view of an ECM communication loss. |
| C1210 | Zero Point Calibration of Yaw Rate Sensor Undone | C | manufacturer | [B] | zero point calibration incomplete (e.g. after sensor/ECU replacement or battery disconnect); faulty yaw rate sensor | Perform yaw-rate-sensor zero-point calibration with Techstream (on level ground, steering centered), then clear the code. |
| C1223 | ABS Control System Malfunction | C | manufacturer | [B] | skid control ECU; ABS actuator circuit faults | General ABS-system fault flag — read the accompanying specific C-codes (wheel speed, solenoid) for the real fault. |
| C1231 | Steering Angle Sensor Circuit Malfunction | C | manufacturer | [B] | steering angle sensor; sensor circuit; sensor power supply; CAN communication system | — |
| C1232 | Stuck in Deceleration Sensor | C | manufacturer | [B] | yaw rate / deceleration sensor; sensor circuit | — |
| C1233 | VSC Controller Power Line Fault | C | manufacturer | [C] | — | A single community source describes C1233 as a short or break in the power line of the VSC controller; no Toyota chart excerpt was found for it in this pass. |
| C1234 | Yaw Rate Sensor Malfunction | C | manufacturer | [B] | yaw rate sensor; yaw rate sensor circuit | — |
| C1235 | Foreign Matter on Front Speed Sensor RH Tip / Abnormal Pulse Waveform (FR) | C | manufacturer | [A] | right front speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU | Set when the speed-sensor pulse waveform is abnormal for 5 s+ at 20 km/h (12 mph) or more (sub-code /35 on Prius). The chart also lists foreign matter on the sensor tip as a cause. |
| C1236 | Foreign Matter on Front Speed Sensor LH Tip / Abnormal Pulse Waveform (FL) | C | manufacturer | [A] | left front speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU | Left-front mirror of C1235 (sub-code /36). NOTE: C1237 was not confirmed in the excerpts — do not assume it exists. |
| C1238 | Foreign Matter on Rear Speed Sensor RH Tip / Abnormal Pulse Waveform (RR) | C | manufacturer | [A] | right rear speed sensor; speed sensor circuit; sensor installation; skid control ECU | Right-rear mirror of C1235 (sub-code /38, detailed code 304). |
| C1239 | Foreign Matter on Rear Speed Sensor LH Tip / Abnormal Pulse Waveform (RL) | C | manufacturer | [A] | left rear speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU | Left-rear mirror of C1235 (sub-code /39, detailed code 305). |
| C1241 | Low Battery Positive Voltage or Abnormally High Battery Positive Voltage | C | manufacturer | [B] | low battery charge; faulty battery; faulty charging system (alternator); power source circuit fault to the skid control ECU | Recorded when voltage at the skid-control-ECU terminal falls outside the detection threshold. A weak battery causes CASCADING false ABS/VSC codes (C0278, C1223, C1231, C1253, C1256, C1340 often appear together) — always load-test the battery and charging system before chasing the other codes. Seen on Prius ABS/VSC/TRAC reports and LX470. |
| C1242 | Open Circuit in IG1/IG2 Power Source Circuit | C | manufacturer | [C] | IG1/IG2 power source wiring; fuse; skid control ECU power circuit | Seen on Prius ABS/VSC/TRAC Techstream reports. |
| C1243 | Malfunction in Deceleration Sensor (Constant Output) | C | manufacturer | [A] | yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit) | From the Kluger/Highlander ABS-VSC chart (05-288): constant-output malfunction of the deceleration sensor (sub-code /43). Fail-safe: the ECU cuts current to the ABS solenoid relay and prohibits ABS control — the brake system reverts to normal (non-ABS) braking. |
| C1244 | Malfunction in Deceleration Sensor | C | manufacturer | [A] | yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit) | General deceleration-sensor malfunction (sub-code /44) — see C1243 fail-safe note. |
| C1245 | Malfunction in Deceleration Sensor | C | manufacturer | [A] | yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit) | Set when, at 30 km/h+, the difference between the acceleration/deceleration values computed from the deceleration sensor and from vehicle speed exceeds 0.35 G for 60 s+ (sub-code /45). Fail-safe per C1243. |
| C1246 | Malfunction in Master Cylinder Pressure Sensor | C | manufacturer | [A] | skid control ECU; harness and connector; brake pedal stroke sensor | Prius ECB brake system (sub-code /46). Do not confuse with C1364 (W/C pressure sensor). |
| C1247 | Malfunction in Stroke Sensor | C | manufacturer | [A] | skid control ECU; harness and connector | Brake pedal stroke sensor (sub-code /47, Prius ECB). |
| C1249 | Open in Stop Lamp Switch Power Line | C | manufacturer | [C] | break or damage in the power line supplying the stop lamp switch | — |
| C1251 | Open in Pump Motor Circuit | C | manufacturer | [A] | wire harness; ABS and traction actuator | The brake-control VSC chart lists C1251/51 as "Open in Pump Motor Circuit" (BC-109); the Kluger ABS chart phrases the same code as "ABS pump motor is locked / open circuit in pump motor circuit". Check the pump-motor circuit before condemning the actuator. |
| C1252 | Hydro-Booster Pump Motor Malfunction | C | manufacturer | [A] | brake actuator assembly; ABS MTR relay | Prius ECB hydro-booster pump motor (sub-code /52). |
| C1253 | Hydro-Booster Pump Motor Relay Malfunction | C | manufacturer | [C] | pump motor relay; wiring; accumulator pressure | Land Cruiser / LX470 brake hydro-booster system. Often cascades with C1241 (low voltage). |
| C1256 | Accumulator Low Pressure | C | manufacturer | [C] | accumulator; hydro-booster pump; low system voltage | Seen on Prius and LX470 brake reports; check C1241 first. |
| C1259 | HV System Regenerative Malfunction | C | manufacturer | [A] | hybrid control system | Regenerative-brake coordination fault on the hybrid side (sub-code /58, Prius). A JustAnswer thread pairs it with P3120 on a 2001 Prius under hard acceleration — check hybrid codes alongside. |
| C1267 | Open or Short Circuit of Brake Pedal Load Sensing Switch Circuit | C | manufacturer | [B] | brake pedal load sensing switch; brake pedal load sensing switch circuit; ABS No.2 fuse | Sub-code /67 on the brake-control chart (BC-111). |
| C1271 | Low Output Signal of Front Speed Sensor RH (Test Mode DTC) | C | manufacturer | [B] | front speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor | Test-mode DTC — set during the ABS sensor check function, not during normal driving. |
| C1272 | Low Output Signal of Front Speed Sensor LH (Test Mode DTC) | C | manufacturer | [B] | front speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor | Test-mode DTC — see C1271. |
| C1273 | Low Output Signal of Rear Speed Sensor RH (Test Mode DTC) | C | manufacturer | [B] | rear speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor | Test-mode DTC — see C1271. |
| C1290 | Steering Angle Sensor Zero Point Malfunction | C | manufacturer | [B] | yaw rate/deceleration sensor zero-point calibration incomplete; poor steering-wheel center adjustment; poor front wheel alignment | Perform zero-point calibration (level ground, centered steering, correct alignment) with Techstream. |
| C1300 | Skid Control ECU Malfunction (ABS ECU Malfunction) | C | manufacturer | [C] | software malfunction in the skid control ECU; oxidized contacts; damaged power supply wiring to the module | Seen as current on a Prius Techstream ABS report. Check power/ground to the actuator before condemning the ECU. |
| C1311 | Open Circuit in Main Relay 1 | C | manufacturer | [A] | skid control ECU; harness and connector; ABS No.1 relay | Prius ECB main-relay diagnostics (sub-code /11). C1311–C1314 cover open/short of main relays 1 and 2. |
| C1312 | Short Circuit in Main Relay 1 | C | manufacturer | [A] | skid control ECU; harness and connector; ABS No.2 relay | See C1311 (sub-code /12). |
| C1313 | Open Circuit in Main Relay 2 | C | manufacturer | [A] | skid control ECU; harness and connector; ABS No.1 relay | See C1311 (sub-code /13). |
| C1314 | Short Circuit in Main Relay 2 | C | manufacturer | [A] | skid control ECU; harness and connector; ABS No.2 relay | See C1311 (sub-code /14). |
| C1315 | Changeover Solenoid Malfunction (SMC1) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly (SMC1) | Prius ECB stroke-simulator cut/changeover solenoid SMC1 (sub-code /31). |
| C1316 | Changeover Solenoid Malfunction (SMC2) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly (SMC2) | See C1315 (sub-code /32). |
| C1319 | Changeover Solenoid Malfunction (SCSS) | C | manufacturer | [A] | skid control ECU; harness and connector; stroke simulator; fluid leakage | Stroke-simulator cut solenoid (sub-code /35). The chart lists fluid leakage as a trouble area — inspect for external leaks. |
| C1331 | ABS Controller Wiring Fault (Front Left Wheel) | C | manufacturer | [C] | damaged wiring to the front-left wheel ABS sensor; insulation damage | Check the sensor harness for chafing along its routing. |
| C1336 | Zero Point Calibration of Acceleration Sensor Undone | C | manufacturer | [B] | zero point calibration incomplete; ABS and traction actuator (skid control ECU) | Perform acceleration-sensor zero-point calibration with Techstream. |
| C1337 | Different Diameter Tire Malfunction | C | manufacturer | [B] | tire size (mismatched tire diameters) | Set when wheel-speed logic detects implausible diameter differences (sub-code /37, BC-117). Check for a mismatched spare or mixed tire sizes before chasing sensors. |
| C1340 | Open Circuit in Center Differential Lock Signal | C | manufacturer | [C] | center differential lock signal circuit; transfer indicator | 4WD models (LX470/Land Cruiser). Set with the center diff lock ON. |
| C1341 | Malfunction in Hydraulic System (FR) | C | manufacturer | [A] | brake actuator assembly; disc rotor; fluid leakage | Front-right hydraulic circuit malfunction (sub-code /62, Prius). A PriusChat thread notes an INF sub-code is available for C1343 (RR sibling) — expect similar detail codes here. |
| C1342 | Malfunction in Hydraulic System (FL) | C | manufacturer | [A] | brake actuator assembly; fluid leakage | Front-left mirror of C1341 (sub-code /63). |
| C1343 | Malfunction in Hydraulic System (RR) | C | manufacturer | [C] | fluid leakage; warped disc rotor; brake actuator assembly | A PriusChat thread (Gen 2 Prius, C1241 + C1343) describes C1343 as "difficulty holding the pressure constant in the right rear brake line" — check for leaks and rotor warpage before condemning the actuator, and read the three-digit INF sub-code for the detailed workup. (C1344, the presumed RL sibling, was not verified in this pass.) |
| C1352 | Increasing Pressure Solenoid Malfunction (FR) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | Front-right pressure-increase solenoid (sub-code /21, Prius). C1352–C1355 = increasing-pressure solenoids FR/FL/RR/RL; C1356–C1359 = decreasing-pressure solenoids FR/FL/RR/RL. |
| C1353 | Increasing Pressure Solenoid Malfunction (FL) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1352 (sub-code /23). |
| C1354 | Increasing Pressure Solenoid Malfunction (RR) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1352 (sub-code /25). |
| C1355 | Increasing Pressure Solenoid Malfunction (RL) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1352 (sub-code /27). |
| C1356 | Decreasing Pressure Solenoid Malfunction (FR) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | Front-right pressure-decrease solenoid (sub-code /22). |
| C1357 | Decreasing Pressure Solenoid Malfunction (FL) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1356 (sub-code /24). |
| C1358 | Decreasing Pressure Solenoid Malfunction (RR) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1356 (sub-code /26). |
| C1359 | Decreasing Pressure Solenoid Malfunction (RL) | C | manufacturer | [A] | skid control ECU; harness and connector; brake actuator assembly | See C1356 (sub-code /28). |
| C1361 | Short Circuit in ABS Motor Fail Safe Relay Circuit | C | manufacturer | [B] | ABS1 H-fuse; VSC MTR relay; VSC MTR relay circuit; VSC FAIL relay; VSC FAIL relay circuit; ABS and traction actuator | Sub-code /91 on the brake-control VSC chart (BC-78). |
| C1364 | Malfunction in W/C Pressure Sensor | C | manufacturer | [A] | skid control ECU; harness and connector | Wheel-cylinder pressure sensor (sub-code /61, Prius). Do not confuse with C1246 (master cylinder pressure sensor). |
| C1365 | Malfunction in ACC Pressure Sensor | C | manufacturer | [A] | brake actuator assembly (accumulator pressure sensor); skid control ECU | Accumulator pressure sensor (sub-code /54, Prius). |
| C1368 | Linear Valve Offset Malfunction | C | manufacturer | [A] | initialization of linear solenoid valve and calibration undone; skid control ECU | Set when linear-solenoid-valve initialization/calibration has not been performed (sub-code /67, Prius) — run the calibration with Techstream. |
| C1377 | Capacitor Malfunction | C | manufacturer | [A] | brake control power supply assembly (capacitor); harness and connector; ABS No.1 fuse; ABS No.2 fuse; ABS No.3 fuse | The brake control power supply (capacitor block, "black box near the battery in the rear" on Gen 2 Prius) provides auxiliary brake power when 12 V drops. Detailed codes: 101 capacitor deteriorated (replace), 102 excessive self-discharge, 103 input voltage 16.4 V+ for 10 s+, 105/106/108 internal charge/backup-output/voltage-monitor circuit faults, 109/110 open/short in 12 V input or OUT1/OUT2 lines. Check 12 V battery, grounds and ABS fuses first — the capacitor block itself is very reliable, and the code often appears after brake work disturbs its connectors. |
| C1378 | Capacitor Communication Circuit Malfunction | C | manufacturer | [A] | harness and connector; skid control ECU | Communication fault between the skid control ECU and the brake control power supply (sub-code /44, Prius). |
| C1380 | Stop Light Control Relay Malfunction | C | manufacturer | [B] | stop light assembly; stop light switch circuit; STOP LP CTRL relay; ABS and traction actuator (skid control ECU) | — |
| C1391 | Abnormal Leak of Accumulator Pressure | C | manufacturer | [C] | accumulator; brake actuator internal leak | Seen on Prius ABS/VSC/TRAC Techstream reports. |
| C1431 | Brake Actuator Pump Motor DTC (2012–2013 Camry) | C | manufacturer | [A] | poor ground on the left fender side panel bracket (after collision/body repair); brake actuator pump motor | Toyota TSB T-SB-0172-13 (Nov 2013): some 2012–2013 Camry vehicles exhibit ABS brake-actuator pump-motor noise from the engine compartment with brake, ABS and/or TRAC warning lamps on and DTC C1431 stored — caused by a poor ground on the left fender side panel bracket (loose, incorrect bolts, or improperly painted after body-shop repairs). Inspect and repair the fender grounds. The TSB excerpt does not state the formal detection-item title. |
| P1100 | BARO Sensor Circuit | P | manufacturer | [C] | — | — |
| P1120 | Accelerator Pedal Position Sensor Circuit Malfunction | P | manufacturer | [A] | open or short in accelerator pedal position sensor circuit; faulty accelerator pedal position sensor; faulty engine ECU | If stored, the ECM shuts down power to the throttle motor and magnetic clutch; the throttle valve closes via return spring (limp-home on the cable). Check VPA/VPA2 voltages (0-5V sweep with pedal). |
| P1121 | Accelerator Pedal Position Sensor Range/Performance Problem | P | manufacturer | [B] | — | CONFLICT — model-dependent meaning. The 2004 Prius repair manual (RM1075U) defines P1121 as "COOLANT FLOW CONTROL VALVE POSITION SENSOR CIRCUIT STUCK" (CHS water valve position sensor / tank outlet temp sensor) [A]. Most other Toyota models use the accelerator-pedal range/performance meaning [B]. Confirm against the model-specific manual. |
| P1125 | Throttle Control Motor Circuit Malfunction | P | manufacturer | [B] | open or short in throttle control motor circuit; faulty throttle control motor; faulty ECM | — |
| P1126 | Magnetic Clutch Circuit Malfunction | P | manufacturer | [C] | — | Throttle-body magnetic clutch circuit (ETCS). Check clutch circuit continuity. |
| P1127 | ETCS Actuator Power Source Circuit Malfunction | P | manufacturer | [B] | open in ETCS power source circuit; faulty ECM | — |
| P1128 | Throttle Control Motor Lock Malfunction | P | manufacturer | [B] | throttle control motor; throttle body (carbon/deposit lock) | — |
| P1129 | Electric Throttle Control System Malfunction | P | manufacturer | [B] | electric throttle control system; ECM | — |
| P1130 | Air/Fuel Sensor Circuit Range/Performance (Bank 1 Sensor 1) | P | manufacturer | [B] | faulty A/F sensor (Bank 1 Sensor 1); wiring; ECM | Toyota uses wideband A/F sensors (not conventional O2) upstream; test with a scan tool reading A/F sensor current/voltage, not a simple rich/lean toggle. |
| P1133 | Air/Fuel Sensor Circuit Response (Bank 1 Sensor 1) | P | manufacturer | [B] | aging A/F sensor (slow response); exhaust leaks ahead of sensor | Response/slow-response code — the sensor still functions but is lazy; often intermittent before setting permanently. |
| P1135 | Air/Fuel Sensor Heater Circuit Malfunction (Bank 1 Sensor 1) | P | manufacturer | [B] | open/short in heater circuit; failed sensor heater element | Check heater resistance at the sensor connector before replacing the sensor. |
| P1150 | Air/Fuel Sensor Circuit Range/Performance (Bank 2 Sensor 1) | P | manufacturer | [B] | A/F sensor nearing end of life (may test good intermittently); wiring | CONFLICT — retrolib.info transcribes this as "(Bank 1 Sensor 2)", but Toyota service-manual convention (P1150/P1153/P1155 = Bank 2 Sensor 1) and a Toyota master technician (JustAnswer) confirm Bank 2 Sensor 1. A sensor can read fine at times then fail — the MIL cycling on/off is the classic end-of-life pattern. |
| P1153 | Air/Fuel Sensor Circuit Response (Bank 2 Sensor 1) | P | manufacturer | [B] | aging A/F sensor; exhaust leak ahead of sensor | — |
| P1155 | Air/Fuel Sensor Heater Circuit Malfunction (Bank 2 Sensor 1) | P | manufacturer | [B] | open/short in heater circuit; failed sensor heater element | Check heater resistance at the sensor connector first. |
| P1200 | Fuel Pump Relay Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1300 | Igniter Circuit Malfunction (No. 1) | P | manufacturer | [A] | open or short in IGF1/IGT1 circuit from No. 1 ignition coil with igniter to ECM; faulty No. 1 ignition coil with igniter; faulty ECM | — |
| P1305 | Igniter Circuit Malfunction (No. 2) | P | manufacturer | [A] | open or short in IGF2/IGT2 circuit; faulty No. 2 ignition coil with igniter; faulty ECM | Numbering is model-dependent — on the 2001 Prius the sequence is P1300 (No.1), P1305 (No.2), P1310 (No.3), P1315 (No.4); other models number P1300/P1310 as No.1/No.2. |
| P1310 | Igniter Circuit Malfunction (No. 3) | P | manufacturer | [A] | open or short in IGF/IGT circuit; faulty ignition coil with igniter; faulty ECM | See P1305 numbering note — verify per model. |
| P1315 | Igniter Circuit Malfunction (No. 4) | P | manufacturer | [A] | open or short in IGF1/IGT4 circuit; faulty No. 4 ignition coil with igniter; faulty ECM | See P1305 numbering note — verify per model. |
| P1335 | No Crankshaft Position Sensor Signal - Engine Running | P | manufacturer | [C] | — | — |
| P1345 | Variable Valve Timing Sensor Circuit (Left Bank) | P | manufacturer | [C] | — | Left/right bank split applies to V-engine models; on inline engines use the Bank 1 codes (P1346/P1349). |
| P1346 | VVT Sensor / Camshaft Position Sensor Circuit Range/Performance Problem (Bank 1) | P | manufacturer | [B] | faulty VVT (camshaft position) sensor; VVT sensor harness open/shorted or poor connection; low/dirty engine oil (VVT-i is oil-pressure actuated); stuck/faulty oil control valve (OCV); stretched timing chain/belt or jumped teeth; faulty ECM (rare) | The ECM compares crankshaft (NE) and camshaft (VV) signals; check engine oil level/condition FIRST (cheap, common). 2001 Prius manual lists "mechanical system (jumping teeth of timing belt, belt stretched)" as a trouble area. |
| P1349 | VVT System Malfunction (Bank 1) | P | manufacturer | [B] | valve timing off; faulty OCV; faulty VVT controller assembly; faulty ECM | System-level code (vs P1346 sensor-level): points at the VVT-i actuator/oil-control side rather than the sensor circuit. |
| P1350 | Variable Valve Timing Sensor Circuit Fault (Right Bank) | P | manufacturer | [C] | — | See P1345 bank note. |
| P1351 | Variable Valve Timing Sensor Out of Range (Right Bank) | P | manufacturer | [C] | — | See P1345 bank note. |
| P1354 | Variable Valve Timing Circuit Fault (Right Bank) | P | manufacturer | [C] | — | See P1345 bank note. |
| P1400 | Sub-Throttle Position Sensor Malfunction | P | manufacturer | [C] | — | — |
| P1401 | Sub-Throttle Position Sensor Range/Performance Problem | P | manufacturer | [C] | — | — |
| P1405 | Turbo Pressure Sensor Circuit Malfunction | P | manufacturer | [C] | — | Diesel/turbo models. |
| P1406 | Turbo Pressure Sensor Range/Performance Problem | P | manufacturer | [C] | — | Diesel/turbo models. |
| P1410 | EGR Valve Position Sensor Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1411 | EGR Valve Position Sensor Circuit Range/Performance | P | manufacturer | [C] | — | — |
| P1430 | Vacuum Sensor for Adsorber and Catalyst System Circuit Malfunction | P | manufacturer | [A] | open or short in vacuum sensor circuit; faulty vacuum sensor for HC adsorber and catalyst system; faulty ECM | 2001 Prius HC-adsorber/catalyst system. |
| P1431 | Vacuum Sensor for Adsorber and Catalyst System Circuit Range/Performance Problem | P | manufacturer | [A] | faulty vacuum sensor for HC adsorber and catalyst system; vacuum line fault | 2001 Prius HC-adsorber/catalyst system. |
| P1436 | Variable Valve Malfunction (HC Adsorber and Catalyst System) | P | manufacturer | [A] | vacuum line; actuator for HC adsorber and catalyst system; front exhaust pipe | 2001 Prius HC-adsorber/catalyst system. |
| P1437 | Vacuum Line Malfunction (HC Adsorber and Catalyst System) | P | manufacturer | [A] | vacuum line; VSV for HC adsorber and catalyst system; check valve | 2001 Prius HC-adsorber/catalyst system. |
| P1455 | Vapor Reducing Fuel Tank System Leak Detected (Small Leak) | P | manufacturer | [A] | hose and pipe; heated oxygen sensor; fuel system; VVT system; ignition system; mass air flow meter; ECM | 2001 Prius vapor-reducing fuel tank system (EVAP-adjacent). |
| P1500 | Starter Signal Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1510 | Boost Pressure Control Circuit Malfunction | P | manufacturer | [C] | — | Turbo models. |
| P1511 | Boost Pressure Low | P | manufacturer | [C] | — | Turbo models. |
| P1512 | Boost Pressure High | P | manufacturer | [C] | — | Turbo models. |
| P1520 | Stop Lamp Switch Signal Malfunction | P | manufacturer | [C] | — | Stop-lamp switch input is used by cruise control and shift interlock; check switch adjustment. |
| P1525 | Resolver Circuit Malfunction | P | manufacturer | [A] | HV ECU; engine ECU | Hybrid transaxle resolver (motor position sensor) circuit — hybrid models only. |
| P1565 | Cruise Control Main Switch Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1600 | ECM BATT Malfunction | P | manufacturer | [A] | open in back-up power source circuit (BATT terminal wiring, EFI fuse); faulty ECM | Battery voltage is supplied to the ECM BATT terminal even with ignition OFF (DTC memory, A/F adaptives). HINT from the manual: if P1600 is present, the ECM does not store any other DTC. Check BATT terminal voltage (9-14V) and the EFI fuse first. |
| P1603 | Engine Stall History | P | manufacturer | [B] | ignition system (spark plug, ignition coil); fuel system (injector, fuel pump, fuel quality); intake/exhaust (MAF, air leaks, throttle body, A/F sensor, VVT system); ECM; wiring/connectors; engine coolant temp sensor | Stored when the engine stops without the ignition/engine switch being operated (after P1604 startability monitoring finishes). ALWAYS check whether the vehicle ran out of fuel first — stalling from an empty tank sets this code. MIL does not come on; DTC stored in memory. |
| P1604 | Startability Malfunction | P | manufacturer | [A] | immobiliser system; engine assembly (excess friction, compression loss); starter; crankshaft position sensor; coolant temp sensor; fuel pump/control system; fuel pipes; injector; throttle body; fuel pressure regulator; battery; spark plug; ignition coil circuit; intake system; camshaft timing OCV; MAF meter; A/F sensor; valve timing; purge VSV; EGR; ECM | Stored when the engine does not start despite STA signal input, takes a long time to start, or stalls just after starting (drops to 200 rpm or less within ~2 seconds). Check fuel level FIRST — running out of fuel sets this code. Then review freeze-frame data via Techstream/GTS. |
| P1605 | Rough Idling | P | manufacturer | [B] | — | CONFLICT — older Toyota-specific lists (retrolib.info) define P1605 as "Knock Control CPU" [C]. Newer Toyota repair-manual excerpts pair P1605 with P1603 as "Rough Idling" [B]. Meaning is era/model-dependent; confirm against the model-specific manual. |
| P1630 | Traction Control System Malfunction | P | manufacturer | [C] | — | — |
| P1633 | ECU Malfunction (ETCS Circuit) | P | manufacturer | [A] | ECM (internal ETCS circuit fault) | 2001 Prius lists this as an ECM-internal fault — the listed remedy is ECM replacement after ruling out external circuits. |
| P1636 | HV ECU Malfunction | P | manufacturer | [A] | HV ECU; engine ECU | Hybrid models only. |
| P1637 | EGSTP Signal Malfunction | P | manufacturer | [A] | HV ECU; engine ECU | Hybrid models only (EGSTP = engine-stop signal line between HV ECU and engine ECU). |
| P1645 | Body Control Module Fault | P | manufacturer | [C] | — | — |
| P1647 | Transmission Control Module Fault | P | manufacturer | [C] | — | — |
| P1652 | Idle Air Control Valve Control Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1656 | OCV Circuit Malfunction (for VVT-i) | P | manufacturer | [A] | open or short in OCV circuit; faulty oil control valve (OCV); faulty ECM | The OCV meters oil pressure to the VVT-i controller — a frequent companion to P1346/P1349. |
| P1658 | Wastegate Valve Control Circuit Malfunction | P | manufacturer | [C] | — | Turbo models. |
| P1661 | EGR Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1662 | EGR Bypass Valve Control Circuit Malfunction | P | manufacturer | [C] | — | — |
| P1663 | Right Oil Control Valve / Variable Valve Timing System | P | manufacturer | [C] | — | See P1345 bank note. |
| P1690 | Oil Control Valve / Variable Valve Timing System Fault | P | manufacturer | [C] | — | — |
| P1692 | Oil Control Valve / Variable Valve Timing System Open | P | manufacturer | [C] | — | — |
| P1693 | Oil Control Valve / Variable Valve Timing System Closed | P | manufacturer | [C] | — | — |
| P1700 | Transmission Output Shaft Speed Sensor Fault | P | manufacturer | [C] | — | — |
| P1705 | Automatic Transmission Direct Clutch Speed Sensor Fault | P | manufacturer | [C] | — | — |
| P1715 | ABS Rear Wheel Speed Sensor Fault | P | manufacturer | [C] | — | Transmission code referencing the ABS rear wheel-speed input. |
| P1725 | Automatic Transmission Input Shaft Speed Sensor / Turbine Speed Sensor Circuit Fault | P | manufacturer | [C] | — | — |
| P1730 | Automatic Transmission Intermediate Shaft Speed Sensor Fault | P | manufacturer | [C] | — | — |
| P1755 | Torque Converter Clutch Solenoid Circuit Fault | P | manufacturer | [C] | — | — |
| P1760 | Automatic Transmission Pressure Control Shift Solenoid Fault | P | manufacturer | [C] | — | — |
| P1765 | Automatic Transmission Pressure Control Shift Solenoid Fault | P | manufacturer | [C] | — | — |
| P1780 | Park/Neutral Position Switch Malfunction | P | manufacturer | [C] | — | A/T only. |
| P2111 | Throttle Actuator Control System - Stuck Open | P | generic | [A] | throttle actuator; throttle body assembly; throttle valve; ECM; wire harness or connector | Set when the ECM signals the throttle actuator to close but it stays open (1-trip). Monitor logic: throttle valve remains at a fixed angle despite high drive current (2 A+, 80%+ close duty) with no TP voltage change for 0.5 s. MIL immediate. Confirmation: clear DTCs, start engine, fully depress and release the pedal quickly. |
| P2112 | Throttle Actuator Control System - Stuck Closed | P | generic | [A] | throttle actuator; throttle body assembly; throttle valve; ECM; wire harness or connector | Mirror of P2111 — ECM signals open, actuator stays closed (2 A+, 80%+ open duty, no TP voltage change, 0.5 s, 1-trip, MIL immediate). |
| P2118 | Throttle Actuator Control Motor Current Range / Performance | P | generic | [A] | open in ETCS power source (+BM) circuit; battery; battery terminals; ETCS fuse; ECM | The ETCS has a dedicated +BM power supply; when it drops below 4 V for 0.8 s+ the ECM calls it an open and cuts current to the throttle actuator. After repair, cycle the ignition off for the ECM to re-allow actuator current. |
| P2120 | Throttle / Pedal Position Sensor / Switch "D" Circuit | P | generic | [A] | accelerator pedal sensor assembly; ECM | VPA fluctuates rapidly beyond the upper/lower malfunction thresholds for 0.5 s+ (1-trip). Check Accel Sensor Out No.1/No.2 via Techstream (Data List). |
| P2121 | Throttle / Pedal Position Sensor / Switch "D" Circuit Range/Performance | P | generic | [B] | accelerator pedal position sensor assembly; ECM | Range/performance companion to the P2120 circuit codes. Toyota inspection procedure checks VCPA/VCP2 reference voltage (4.5–5.5 V), then replaces the pedal sensor assembly, then the ECM if the DTC recurs. |
| P2122 | Throttle / Pedal Position Sensor / Switch "D" Circuit Low Input | P | generic | [A] | accelerator pedal sensor assembly; open in VCPA circuit; open or ground short in VPA circuit; ECM | VPA 0.4 V or less for 0.5 s+ (1-trip). MIL on, DTC stored. |
| P2123 | Throttle / Pedal Position Sensor / Switch "D" Circuit High Input | P | generic | [A] | accelerator pedal sensor assembly; open in EPA circuit; ECM | VPA 4.8 V or more for 2.0 s+ (1-trip). MIL on, DTC stored. |
| P2125 | Throttle / Pedal Position Sensor / Switch "E" Circuit | P | generic | [A] | accelerator pedal sensor assembly; ECM | VPA2 fluctuates rapidly beyond thresholds for 0.5 s+ (1-trip) — the "E"/No.2 channel mirror of P2120. |
| P2126 | Throttle / Pedal Position Sensor / Switch "E" Circuit Range/Performance | P | generic | [B] | accelerator pedal sensor assembly; ECM | Range/performance companion to P2125; see P2121 diagnostic note for the Toyota inspection sequence. |
| P2127 | Throttle / Pedal Position Sensor / Switch "E" Circuit Low Input | P | generic | [A] | accelerator pedal sensor assembly; open in VCP2 circuit; open or ground short in VPA2 circuit; ECM | VPA2 1.2 V or less for 0.5 s+ (1-trip). MIL on, DTC stored. |
| P2128 | Throttle / Pedal Position Sensor / Switch "E" Circuit High Input | P | generic | [A] | accelerator pedal sensor assembly; open in EPA2 circuit; ECM | Both conditions for 2.0 s+ (1-trip): (a) VPA2 4.8 V or more, (b) VPA between 0.4 V and 3.45 V. |
| P2135 | Throttle / Pedal Position Sensor / Switch "A" / "B" Voltage Correlation | P | generic | [A] | short between VTA1 and VTA2 circuits; throttle position sensor (built into throttle body with motor assembly); ECM | Correlation code for the two TP sensors in the throttle body. Set when (a) VTA1–VTA2 differ by 0.02 V or less for 0.5 s+, or (b) VTA1 is 0.2 V or less and VTA2 is 1.75 V or less for 0.4 s+ (1-trip). Check Throttle Position No.1/No.2 via Techstream — normal: No.1 0.5–1.1 V released / 3.2–4.8 V depressed; No.2 2.1–3.1 V released / 4.6–4.98 V depressed. |
| P2138 | Throttle / Pedal Position Sensor / Switch "D" / "E" Voltage Correlation | P | generic | [A] | short between VPA and VPA2 circuits; accelerator pedal sensor assembly; ECM | APP-sensor correlation companion to P2135. Set when (a) |VPA − VPA2| is 0.02 V or less, or (b) VPA is 0.4 V or less and VPA2 is 1.2 V or less, for 2.0 s+ (1-trip). Check Accel Sensor Out No.1/No.2 via Techstream. |
| P2195 | Oxygen (A/F) Sensor Signal Stuck Lean (Bank 1 Sensor 1) | P | generic | [A] | open or short in A/F sensor (Bank 1 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM | Two monitors: (1) voltage — A/F voltage above 3.8 V (very lean) while HO2 sensor rises from below 0.21 V to 0.59 V+ for 5 s; (2) current — during fuel-cut, A/F current 3.6 mA or more for 3 s cumulative (high-side stuck). Use the A/F CONTROL active test to graph A/F vs HO2 response; P2A00 may set alongside. |
| P2196 | Oxygen (A/F) Sensor Signal Stuck Rich (Bank 1 Sensor 1) | P | generic | [A] | open or short in A/F sensor (Bank 1 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM | Mirror of P2195: A/F voltage below 2.8 V (very rich) while HO2 falls from 0.59 V+ to below 0.21 V for 5 s, or fuel-cut A/F current below ~1.0 mA for 3 s cumulative (low-side stuck). 2-trip logic. |
| P2197 | Oxygen (A/F) Sensor Signal Stuck Lean (Bank 2 Sensor 1) | P | generic | [A] | open or short in A/F sensor (Bank 2 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM | Bank 2 mirror of P2195. On Toyota V-engines Bank 2 is the bank containing cylinder No. 2. |
| P2198 | Oxygen (A/F) Sensor Signal Stuck Rich (Bank 2 Sensor 1) | P | generic | [A] | open or short in A/F sensor (Bank 2 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM | Bank 2 mirror of P2196. |
| P2440 | Secondary Air Injection System Switching Valve Stuck Open (Bank 1) | P | generic | [B] | air switching valve stuck open (carbon buildup, debris from disintegrated air-pump filter foam or impeller blades, moisture); air injection pump | Toyota/Lexus secondary-air systems are a known failure family. A Toyota TSB (2005–2009 2UZ-FE 4.7L) attributes these codes to debris passing through the air pump contaminating the valves — inspect pump, hoses and bypass valve; replacement typically covers pump + hoses + valve assembly. Field check: pull the hose, start the engine — exhaust at the valve port means the valve is stuck open. |
| P2441 | Secondary Air Injection System Switching Valve Stuck Closed (Bank 1) | P | generic | [B] | air switching valve stuck closed (carbon, debris); air injection pump | See P2440 — same TSB/debris context. Bypass-harness field fixes target this family but defeat an emissions monitor; not recommended as a repair. |
| P2442 | Secondary Air Injection System Switching Valve Stuck Open (Bank 2) | P | generic | [B] | air switching valve stuck open (carbon, debris, moisture); air injection pump | Bank 2 mirror of P2440. |
| P2443 | Secondary Air Injection System Switching Valve Stuck Closed (Bank 2) | P | generic | [B] | air switching valve stuck closed (carbon, debris); air injection pump | Bank 2 mirror of P2441. |
| P2444 | Secondary Air Injection System Pump Stuck ON (Bank 1) | P | generic | [B] | air injection pump relay stuck; pump control circuit fault | Pump-side companion to the valve codes — the pump runs when it should be off. Not individually enumerated in the forum guides; definition follows the SAE J2012 P244x pattern (P2445/P2447 stuck-OFF are documented there). |
| P2445 | Secondary Air Injection System Pump Stuck OFF (Bank 1) | P | generic | [B] | failed air injection pump; pump relay/circuit open; debris-seized pump | See P2440 — pump failures in this family commonly trace to the disintegrating internal foam filter. |
| P2446 | Secondary Air Injection System Pump Stuck ON (Bank 2) | P | generic | [B] | air injection pump relay stuck; pump control circuit fault | Bank 2 mirror of P2444 — see P2444 note. |
| P2447 | Secondary Air Injection System Pump Stuck OFF (Bank 2) | P | generic | [B] | failed air injection pump; pump relay/circuit open | Bank 2 mirror of P2445. |
| P2A00 | A/F Sensor Circuit Slow Response (Bank 1 Sensor 1) | P | generic | [A] | open or short in A/F sensor circuit; A/F sensor; A/F sensor heater; EFI main relay; air induction system; fuel pressure; injector; ECM | After warm-up the ECM runs active A/F control (~10 s), forcing injection volume up/down around stoichiometry and measuring the A/F sensor response rate; if the deterioration level is below threshold the DTC sets. Confirmation: check Mode 06 O2-sensor monitor data via Techstream. Although the title says "oxygen sensor", on Toyota this is the wideband A/F sensor. |
| P2A03 | A/F Sensor Circuit Slow Response (Bank 2 Sensor 1) | P | generic | [A] | not documented (same family as P2A00) | Bank 2 companion to P2A00 — see P2A00 notes. Listed alongside P2A00 in the Toyota SFI charts. |
| P3000 | High Voltage Battery Fault | P | manufacturer | [C] | — | — |
| P3001 | High Voltage Battery ECU Fault | P | manufacturer | [C] | — | NOTE — the source list gives both P3001 and P3100 as "High Voltage Battery ECU Fault" and P3105/P3109 as battery-ECU communication faults; the distinctions are the source's, not independently verified. |
| P3002 | High Voltage Battery ECU Communication Fault | P | manufacturer | [B] | wire harness; battery ECU | A Toyota master technician (JustAnswer) describes the P3105-family symptom as communication failure between the battery ECU (inside the HV battery case) and the HV ECU (under the passenger footrest) — check connectors and harness before condemning either ECU. |
| P3004 | High Voltage Power Cable Fault | P | manufacturer | [C] | — | — |
| P3005 | High Voltage Fuse Blown | P | manufacturer | [C] | — | — |
| P3006 | High Voltage Battery State Of Charge Uneven | P | manufacturer | [C] | — | — |
| P3009 | High Voltage Leak Detected | P | manufacturer | [C] | — | High-voltage insulation/leak fault — hybrid models only. Treat as a safety-relevant code; do not probe HV circuits without training and PPE. |
| P3011 | High Voltage Battery Module 1 Fault | P | manufacturer | [C] | — | P3011 through P3029 map to HV battery modules/blocks 1 through 19 (per the source list); only P3011 is entered here as the range representative — do not invent per-module entries. |
| P3030 | High Voltage Battery Monitor Circuit Fault | P | manufacturer | [C] | — | — |
| P3060 | High Voltage Battery Temperature Sensor or Circuit Fault | P | manufacturer | [C] | — | — |
| P3076 | High Voltage Battery Cooling Fan Abnormal Air Flow | P | manufacturer | [C] | — | — |
| P3077 | High Voltage Battery Cooling Fan Motor or Circuit Fault | P | manufacturer | [C] | — | — |
| P3100 | High Voltage Battery ECU Fault | P | manufacturer | [C] | — | See P3001 note — the source lists both P3001 and P3100 with this description; distinction unverified. |
| P3101 | Engine System Fault | P | manufacturer | [C] | — | Seen on Gen 1 Prius alongside P3191 (engine does not start); owner threads pair it with no-start diagnosis (fuel, spark, MAF). |
| P3105 | High Voltage Battery ECU or Communication Circuit Fault | P | manufacturer | [B] | wire harness; battery ECU | See P3002 — battery ECU ↔ HV ECU communication failure; reseat connectors, check harness continuity. |
| P3106 | Engine ECM or Communication Circuit Fault | P | manufacturer | [C] | — | — |
| P3107 | Air Bag ECU or Communication Circuit Fault | P | manufacturer | [C] | — | Hybrid-vehicle-control view of an SRS ECU communication fault — check SRS codes as well. |
| P3108 | A/C Amplifier ECU or Communication Circuit Fault | P | manufacturer | [C] | — | — |
| P3109 | High Voltage Battery ECU or Communication Circuit Fault | P | manufacturer | [C] | — | See P3105 note — source lists both P3105 and P3109 with this description; distinction unverified. |
| P3110 | HV IGCT Relay or Circuit Fault | P | manufacturer | [C] | — | — |
| P3115 | Hybrid System Main Relay Fault | P | manufacturer | [C] | — | System main relay (SMR) circuit — hybrid models only. |
| P3120 | High Voltage Transaxle Fault | P | manufacturer | [B] | — | An ATSG technical bulletin reproduces a scan tool showing "P3120 HV transaxle assy malfunction" set in the HV ECU with the master warning lamp on and READY on; information sub-codes narrow it to resolver/MG data — read the INF codes before condemning the transaxle. |
| P3125 | Converter & Inverter Assembly Malfunction | P | manufacturer | [B] | +B short in DC/DC converter NODD wiring; DC/DC converter malfunction; open or ground short in DC/DC converter NODD wiring; converter & inverter assembly; wire harness | From the 2002 Prius repair manual (RM883U DI-271): the HV ECU monitors DC/DC converter operation because a failed converter drains the auxiliary battery until the car cannot keep driving. Information codes 263/264/265 narrow it (263: +B short in NODD wiring; 264: converter malfunction; 265: open/GND short in NODD wiring). NOTE: a Toyota TSB advises that if P3125 is present due to P3130, do not diagnose P3125 — fix the inverter cooling fault first. |
| P3130 | Inverter Cooling System Malfunction | P | manufacturer | [B] | inverter coolant pump (electric water pump) failure; coolant flow blockage/kinked hoses; low coolant | Snap-on SureTrack documented case (2001 Prius): inverter temperature exceeded range with clean full coolant — no circulation at the reservoir despite voltage at the pump; replacing the electric water pump fixed it. A Toyota TSB covers P3130+P3125 together: check inverter-reservoir water flow first; if P3125 is present due to P3130, ignore P3125. |
| P3135 | High Voltage Circuit Breaker Sensor Fault | P | manufacturer | [C] | — | — |
| P3140 | Interlock Malfunction | P | manufacturer | [A] | service plug not installed correctly (handle not flipped up, bent/broken microswitch tab); inverter terminal cover or sensor cover removed; open in interlock signal circuit | From the 2002 Prius repair manual (RM883U): the HV ECU shuts down the system main relay if it detects safety-device operation (service plug removal, inverter terminal cover, sensor cover) while the vehicle is stopped (INF 350); an open in the interlock signal circuit while running sets INF 351 without shutting down HV. PriusChat field reports confirm the service-plug microswitch as the common cause — the code returns immediately at key-on until the switch closes. |
| P3145 | Vehicle Speed Sensor or Circuit Fault | P | manufacturer | [C] | — | Hybrid-vehicle-control view of a vehicle speed sensor fault. |
| P3190 | Poor Engine Power | P | manufacturer | [A] | air induction system; throttle body; fuel pressure; engine; mass air flow meter | Hybrid models (2001 Prius): engine cannot produce expected power. |
| P3191 | Engine Does Not Start | P | manufacturer | [A] | mass air flow meter; out of fuel; engine coolant temp sensor; crankshaft position sensor; camshaft position sensor; ECM | Hybrid models (2001 Prius). Check fuel level first. |
| P3193 | Fuel Run Out | P | manufacturer | [A] | out of fuel; ECM | Set when the fuel-low-level signal is input to the ECM AND the P3190/P3191 detection condition is satisfied (1-trip). Hybrid note: running out of fuel forces the car onto battery-only operation, deep-discharging the HV battery — refuel and recharge promptly. |
| U0101 | Lost Communication with TCM | U | generic | [A] | CAN communication system | On Toyota hybrids the lane-departure/pre-crash documentation phrases this as lost communication with the hybrid vehicle control ECU; the clearance-warning (IPA) documentation phrases it as lost communication with the TCM. When 2+ U-codes set simultaneously, inspect the connectors and wire harnesses of each ECU rather than chasing them individually. |
| U0111 | Lost Communication with Battery Energy Control Module "A" | U | generic | [B] | hybrid battery ECU; CAN communication system; corroded battery terminals/connections | A Toyota master technician (JustAnswer, 2007 Prius) describes U0111 as interrupted communication with the hybrid battery's computer (ECU); it commonly appears alongside P0A80 (replace hybrid battery pack). Check battery connections for corrosion first. |
| U0121 | Lost Communication with ABS Control Module | U | generic | [A] | CANL/CANH circuit; skid control ECU | From the 2004 Scion xB repair manual (RM1031U) CAN communication system, skid-control-ECU communication-stop mode (sub-code /94): the condition where the skid control ECU cannot transmit data continues for 5+ seconds, or the no-transmit condition repeatedly occurs 10 times. |
| U0122 | Lost Communication with Vehicle Dynamics Control Module | U | generic | [A] | CAN communication system | From the Toyota 4WD-control DTC documentation: communication lost between the skid control ECU (brake actuator assembly) and the 4-wheel-drive control ECU for 0.72 s+ (1-trip). Note: this DTC also appears transiently while skid-control-ECU data is being overwritten (4LO lamp blinks) — clear DTCs after such work. |
| U0123 | Lost Communication with Yaw Rate Sensor Module | U | generic | [A] | yaw rate sensor; CANL/CANH circuit; skid control ECU; steering angle sensor; junction connector | 2004 Scion xB RM1031U: with ECU IG1 voltage at 9.5 V+, no data received from the yaw rate sensor for 1 s+, or reception impossible one or more times within 5 s repeatedly 10 times (sub-code /62). |
| U0124 | Lost Communication with Lateral Acceleration Sensor Module | U | generic | [A] | yaw rate sensor (deceleration sensor); CANL/CANH circuit; skid control ECU; junction connector | Same detection pattern as U0123 but for the deceleration (lateral-G) sensor channel (sub-code /95). See also C1243–C1245 for the sensor-side faults. |
| U0126 | Lost Communication with Steering Angle Sensor Module | U | generic | [A] | steering angle sensor (spiral cable with sensor sub-assembly); CAN communication system | Same detection pattern as U0123 for the steering angle sensor (sub-code /63). The IPA/parking-assist documentation phrases it as lost communication with the spiral cable with sensor sub-assembly. |
| U0129 | Lost Communication with Brake System Control Module | U | generic | [A] | brake actuator assembly (skid control ECU); CAN communication system | Pre-crash safety city sensor view: unable to receive data from the brake actuator assembly (skid control ECU) for 5 s+ while driving at 5 km/h+. Also reported by the power steering ECU and combination meter. |
| U0130 | Lost Communication with VGRS | U | generic | [A] | VGRS ECU (front steering control ECU); CAN communication system | Variable Gear Ratio Steering models only — lost communication with the VGRS ECU (front steering control ECU). |
| U0131 | Lost Communication with Power Steering Control Module | U | generic | [A] | power steering ECU assembly; CAN communication system | Reported by the combination meter assembly and lane-departure system when power-steering ECU data stops. |
| U0140 | Lost Communication with Main Body ECU | U | generic | [A] | main body ECU (multiplex network body ECU); CAN communication system; seat belt control ECU; driving support ECU | Pre-crash view: communication stop between the main body ECU and the driving support ECU (or seat belt control ECU) for 1 s+ with the engine switch on (IG). The certification-ECU (smart key) documentation uses the same definition with 1-trip logic. |
| U0142 | Lost Communication with Body Control Module "B" | U | generic | [B] | main body ECU (multiplex network body ECU); CAN communication system | CONFLICT — the lane-departure/CAN-chart documentation defines U0142 as "Lost Communication with Body Control Module 'B'" (reported by the combination meter), while the certification-ECU (smart key) documentation defines U0142 identically to U0140: "Lost Communication with Main Body ECU" (CAN error between certification ECU and main body ECU). Both are Toyota repair-manual sources; the reporting ECU determines which definition applies. |
| U0151 | Lost Communication with Restraints Control Module | U | generic | [A] | center airbag sensor assembly; CAN communication system; seat belt control ECU | Pre-crash view: communication stop between the center airbag sensor and the seat belt control ECU for 1 s+ (IG on). The CAN chart phrases it as "Lost Communication with Airbag ECU". |
| U0155 | Lost Communication with Combination Meter | U | generic | [A] | combination meter assembly; CAN communication system | Pre-crash safety city sensor view: unable to receive data from the combination meter for 80 s+ while driving at 5 km/h+. The clearance-warning ECU documentation phrases it as lost communication with the instrument panel cluster (IPC). |
| U0163 | Lost Communication with Navigation Control Module | U | generic | [A] | radio receiver assembly (navigation); CAN communication system | Phrased in the Toyota IPA documentation as lost communication with the radio receiver assembly. A community fault guide notes GPS malfunction as a symptom. |
| U0208 | Lost Communication with "Seat Control Module A" | U | generic | [B] | — | Appears as a row in the Toyota CAN communication system DTC matrix (RHD with entry-and-start system); per-system detection conditions not captured in the excerpts. |
| U0235 | Lost Communication with Cruise Control Front Distance Range Sensor | U | generic | [A] | front millimeter wave radar sensor; CAN communication system; driving support ECU | Pre-crash view: communication stop between the front millimeter wave radar sensor and the driving support ECU for 1 s+ (IG on). |
| U0293 | HV ECU Communication Malfunction | U | generic | [A] | CAN communication system | Listed in the Toyota lane-departure-alert DTC set as "HV ECU Communication" — a communication malfunction involving the hybrid vehicle control ECU. Per-system detection conditions not captured in the excerpts. |
| U1100 | Lost Communication with Seat Belt Control ECU | U | manufacturer | [A] | seat belt control ECU branch line or connector; power source circuit of seat belt control ECU; seat belt control ECU ground circuit; seat belt control ECU | Set when no communication from the seat belt control ECU continues. Pre-crash safety system family (see U1104 in v1.2.1). |
| U1103 | Lost Communication with Stop and Start Control Module | U | manufacturer | [B] | ECM; engine stop-and-start ECU; CAN communication system fault | Stored when there is no communication between the ECM and the engine stop-and-start ECU for 1.16+ seconds with the ignition on (1-trip logic). MIL does not come on. (Techstream may display the extended form U110387.) |
| U1104 | Lost Communication with Driving Support ECU | U | manufacturer | [B] | driving support ECU; millimeter-wave radar / camera sensors; CAN communication system | Pre-crash safety system: set on a communication malfunction between the collision-detection sensors/ECUs or the pre-crash control ECUs. |
| U1110 | Lost Communication with Intuitive Parking Assist Module | U | manufacturer | [B] | clearance warning ECU assembly; CAN communication system | Lexus parking-assist (clearance sonar) module. NOTE: U1110 is make-specific — on Dodge/RAM it has a different definition. Do not cross-apply. |
| U1114 | Lost Communication with Main Switch Module | U | manufacturer | [B] | CAN communication system | The clearance-warning ECU documentation phrases it as lost communication with the integration control and panel assembly. Appears in the Toyota CAN communication DTC matrix. |
| U1115 | Lost Communication with Tilt and Telescopic Module | U | manufacturer | [B] | multiplex tilt and telescopic ECU CAN branch wire or connector; power source circuit of multiplex tilt and telescopic ECU; multiplex tilt and telescopic ECU ground circuit; multiplex tilt and telescopic ECU | No communication from the multiplex tilt and telescopic ECU; reported by the main body ECU (multiplex network body ECU). Power tilt/telescopic steering column models. |
| U1117 | Lost Communication with Accessory Gateway | U | manufacturer | [A] | connector and branch wire of sub bus 2 of option connector (bus buffer ECU); internal malfunction of option connector (bus buffer ECU) | Data from the option connector (bus buffer ECU) cannot be received. Reported by the certification ECU (smart key ECU); 1-trip logic, confirm with engine switch on (IG) for 10 s+. |
| U1118 | Lost Communication with Rear Radar Sensor | U | manufacturer | [B] | rear radar sensor; CAN communication system | Pre-crash safety system family — see U1104. |
| U1121 | Lost Communication with Driver Monitor ECU | U | manufacturer | [B] | driver monitor ECU/camera; CAN communication system | Pre-crash safety system family — see U1104. |
| U1124 | Lost Communication with Right Headrest Control ECU | U | manufacturer | [B] | right headrest control ECU; CAN communication system | Pre-crash safety system family — see U1104. |
| U1125 | Lost Communication with Left Headrest Control ECU | U | manufacturer | [B] | left headrest control ECU; CAN communication system | Pre-crash safety system family — see U1104. |
| U1133 | Lost Communication with PMN Module | U | manufacturer | [C] | — | Appears as a row in the Toyota CAN communication system DTC matrix; the "PMN" expansion and per-system detection conditions were not documented in the excerpts. |

## volvo — 33 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| CEM-1A51 | Communication with the supplemental restraint system module (SRS). Signal missing | U | manufacturer | [B] | open circuit on LS-CAN to SRS; SRS node disconnected; weak/disturbed CAN message | Typical of an open circuit in the CAN bus; often appears with other CEM-1A5x codes. Disconnecting a node without first disconnecting the battery can set these. |
| CEM-1A52 | Communication with the driver door module (DDM). Signal missing | U | manufacturer | [B] | LS-CAN wiring to DDM; DDM disconnected | See CEM-1A51 pattern. |
| CEM-1A53 | Communication with the passenger door module (PDM). Signal missing | U | manufacturer | [B] | LS-CAN wiring to PDM; PDM disconnected | See CEM-1A51 pattern. |
| CEM-1A55 | Communication with the climate control module (CCM). Signal missing | U | manufacturer | [B] | LS-CAN wiring to CCM | See CEM-1A51 pattern. |
| CEM-1A56 | Communication with the driver information module (DIM). Signal missing | U | manufacturer | [B] | LS-CAN wiring to DIM | See CEM-1A51 pattern. |
| CEM-1A5E | Communication with the steering wheel angle sensor module (SAS). Signal missing | U | manufacturer | [B] | LS-CAN wiring to SAS | See CEM-1A51 pattern. |
| CEM-1A5F | Communication with the brake control module (BCM/ABS). Signal missing | U | manufacturer | [B] | HS-CAN wiring to BCM | See CEM-1A51 pattern. |
| CEM-1A61 | Communication with the transmission control module (TCM). Signal missing | U | manufacturer | [B] | HS-CAN wiring to TCM | See CEM-1A51 pattern. |
| CEM-1A62 | Communication with the engine control module (ECM). Signal missing | U | manufacturer | [B] | HS-CAN wiring to ECM | See CEM-1A51 pattern. |
| CEM-DF03 | CAN_H (or CAN_L) short to battery, low speed network | U | manufacturer | [B] | pinched/shorted LS-CAN wiring; short between CAN_H and CAN_L; single-wire operation | Detection is continuous; a permanent fault is detected within a few seconds. Check for shorts between CAN H/L and to battery/ground on the LS bus. |
| CEM-DF04 | CAN_L short to ground, low speed network | U | manufacturer | [B] | LS-CAN_L wiring shorted to ground | See CEM-DF03. |
| CEM-DF05 | CAN_H short to ground, low speed network | U | manufacturer | [B] | LS-CAN_H wiring shorted to ground | See CEM-DF03. |
| CEM-DF06 | CAN_L or CAN_H short to battery, low speed network | U | manufacturer | [B] | LS-CAN wiring shorted to battery | See CEM-DF03. |
| CEM-DF13 | CAN_H or CAN_L short to battery, high speed network | U | manufacturer | [B] | HS-CAN wiring shorted to battery | High-speed-network counterpart of DF03–DF06. |
| CEM-DF14 | CAN_L short to ground, high speed network | U | manufacturer | [B] | HS-CAN_L wiring shorted to ground | See CEM-DF13. |
| CEM-DF15 | CAN_H short to ground, high speed network | U | manufacturer | [B] | HS-CAN_H wiring shorted to ground | See CEM-DF13. |
| CEM-DF16 | CAN_L or CAN_H short to battery, high speed network | U | manufacturer | [B] | HS-CAN wiring shorted to battery | See CEM-DF13. |
| E000 | CAN high speed checksum error — communication fault with control unit on HS-CAN | U | manufacturer | [B] | disturbed/corrupt CAN message; contact bounce; single-wire operation; wrong-baud-rate node; faulty crystal in a node | Posted by any node; designed for contact-bounce/corrupted-message detection but also appears on CAN_H↔CAN_L shorts or one-wire communication. A permanent fault is detected within seconds. |
| E001 | CAN low speed checksum error — communication fault with control unit on LS-CAN | U | manufacturer | [B] | see E000, on the LS bus | LS counterpart of E000. E003 in some modules = configuration fault on the same buses. |
| P0016 | Camshaft position, inlet — High (Volvo module code ECM-670C) | P | manufacturer | [C] | — | — |
| P0532 | A/C pressure sensor — Signal too low (Volvo module code ECM-520D) | P | manufacturer | [C] | — | — |
| P0533 | A/C pressure sensor — Signal too high (Volvo module code ECM-520C) | P | manufacturer | [C] | — | — |
| P0560 | Battery voltage — Faulty signal (Volvo module code ECM-8200) | P | manufacturer | [C] | — | — |
| P0561 | System relay — Signal too low (Volvo module code ECM-800B) | P | manufacturer | [C] | — | — |
| P0602 | Malfunction indicator light CEM — Faulty signal (Volvo module code ECM-5110) | P | manufacturer | [C] | — | — |
| P0604 | Memory error RAM — Faulty signal (Volvo module code ECM-9970) | P | manufacturer | [C] | — | — |
| P0605 | Memory error ROM — Faulty signal (Volvo module code ECM-9980) | P | manufacturer | [C] | — | — |
| P0606 | Engine control module (ECM) — Faulty signal (Volvo module code ECM-9990) | P | manufacturer | [C] | — | — |
| P0607 | Control module, internal fault (timer circuit) (Volvo module code ECM-711A) | P | manufacturer | [B] | corroded ECM connector (one shop report); internal ECM timer fault | VADIS conversion-table example: "DTC ECM-711A is stored if the engine control module registers a fault in the internal circuit for the timer in the control module." P0607 maps to a family of ECM-98xx/72xx internal-fault codes. |
| P0627 | Fuel pump control module — Signal missing (Volvo module code ECM-291B) | P | manufacturer | [C] | — | — |
| P0628 | Fuel pump control module — Signal too low (Volvo module code ECM-291D) | P | manufacturer | [C] | — | — |
| P0642 | Power supply (5 volt) — Signal too low (Volvo module code ECM-810D) | P | manufacturer | [C] | — | — |
| P0650 | Malfunction indicator lamp (MIL) — Signal missing (Volvo module code ECM-660B) | P | manufacturer | [C] | — | — |

## vw — 140 codes

| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |
|---|---|---|---|---|---|---|
| P0705 | Multi-Function Transmission Range Switch — Malfunction (PRNDL Input) | P | manufacturer | [B] | F125 multifunction switch failure; water ingress at the switch; wiring fault | VAG 5-digit: 00293. The infamous F125 switch on 01M/01V automatics — causes limp mode and wrong gear display. The switch sits on the transmission and is moisture-prone. |
| P0712 | Transmission Fluid Temperature Sensor Circuit — Low Input (G93) | P | manufacturer | [C] | — | VAG 5-digit: 00300 (shared 5-digit with P0713) |
| P0713 | Transmission Fluid Temperature Sensor Circuit — High Input (G93) | P | manufacturer | [C] | — | VAG 5-digit: 00300 (shared 5-digit with P0712) |
| P0715 | Input / Turbine Speed Sensor Circuit — Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 00297 (shared 5-digit with P0721/P0722) |
| P0721 | Vehicle Speed Sensor Circuit — Range/Performance, Signal Noisy (G38) | P | manufacturer | [C] | — | VAG 5-digit: 00297 |
| P0722 | Vehicle Speed Sensor Circuit — No Signal | P | manufacturer | [C] | — | VAG 5-digit: 00297 |
| P0725 | Engine Speed Input Circuit (RPM Sensor) — Malfunction | P | manufacturer | [C] | loose ECM power relay; faulty engine speed sensor | VAG 5-digit: 00529. The table notes "also check for loose ECM power relay". |
| P0726 | Engine Speed Input Circuit — RPM Upper Limit Exceeded | P | manufacturer | [C] | — | VAG 5-digit: 00543 |
| P0727 | Engine Speed Input Circuit (RPM Sensor) — No Signal | P | manufacturer | [C] | — | VAG 5-digit: 00529 |
| P0730 | Transmission Shift-Range Controller — Incorrect Gear Ratio | P | manufacturer | [C] | — | VAG 5-digit: 00652 (shared with P0731–P0734) |
| P0731 | Transmission Shift-Range Controller — Gear 1 Incorrect Ratio | P | manufacturer | [C] | slipping clutch pack; low ATF; valve body fault | VAG 5-digit: 00652. Pattern P0731–P0734 = gears 1–4 incorrect ratio. |
| P1101 | O2 Sensor Circuit (Bank 1 Sensor 1) — Voltage Too Low / Air Leak | P | manufacturer | [C] | exhaust leak upstream of sensor; faulty O2 sensor; wiring fault | VAG 5-digit: 17509. CONFLICT: one community DTC list maps P1102 (not P1101) to this text — the 5-digit mapping here follows the VAG DTC table transcription. |
| P1102 | O2 Sensor Heater Circuit (Bank 1 Sensor 1) — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17510. CONFLICT: a second community list gives "O2S Heating Circuit Bank 1 Sensor 1 Voltage Too Low/Air Leak" for P1102 — the two sources disagree; 5-digit mapping follows the VAG DTC table transcription. |
| P1103 | O2 Sensor Heater Circuit (Bank 1 Sensor 1) — Output Too Low | P | manufacturer | [C] | — | VAG 5-digit: 17511 |
| P1104 | O2 Sensor Circuit (Bank 1 Sensor 2) — Voltage Too Low / Air Leak | P | manufacturer | [C] | — | VAG 5-digit: 17512 |
| P1105 | O2 Sensor Heater Circuit (Bank 1 Sensor 2) — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17513 |
| P1106 | O2 Sensor Circuit (Bank 2 Sensor 1) — Voltage Too Low / Air Leak | P | manufacturer | [C] | — | VAG 5-digit: 17514 |
| P1107 | O2 Sensor Heater Circuit (Bank 2 Sensor 1) — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17515 |
| P1108 | O2 Sensor Heater Circuit (Bank 2 Sensor 1) — Output Too Low | P | manufacturer | [C] | — | VAG 5-digit: 17516 |
| P1109 | O2 Sensor Circuit (Bank 2 Sensor 2) — Voltage Too Low / Air Leak | P | manufacturer | [C] | — | VAG 5-digit: 17517 |
| P1110 | O2 Sensor Heater Circuit (Bank 2 Sensor 2) — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17518 |
| P1113 | O2 Sensor Heater Resistance Too High (Bank 1 Sensor 1) | P | manufacturer | [C] | aging heater element; wiring resistance | From the community VW fault-code list; no 5-digit mapping verified. |
| P1115 | O2 Sensor Heater Circuit Short to Ground (Bank 1 Sensor 1) | P | manufacturer | [C] | — | From the community VW fault-code list; no 5-digit mapping verified. |
| P1116 | O2 Sensor Heater Circuit Open (Bank 1 Sensor 1) | P | manufacturer | [C] | — | From the community VW fault-code list; no 5-digit mapping verified. |
| P1117 | O2 Sensor Heater Circuit Short to Ground (Bank 1 Sensor 2) | P | manufacturer | [C] | — | From the community VW fault-code list; no 5-digit mapping verified. |
| P1118 | O2 Sensor Heater Circuit Open (Bank 1 Sensor 2) | P | manufacturer | [C] | — | From the community VW fault-code list; no 5-digit mapping verified. |
| P1127 | Long Term Fuel Trim — System Too Rich (Bank 1) | P | manufacturer | [C] | leaking injector; excessive fuel pressure; faulty MAF over-reporting | VAG 5-digit: 17535. Check MVB 032 fuel trim values. |
| P1128 | Long Term Fuel Trim — System Too Lean (Bank 1) | P | manufacturer | [B] | vacuum/intake leaks (unmetered air); MAF under-reporting (Ross-Tech notes the MAF may die slowly without setting a MAF code — 17536/P1128 is the classic symptom); exhaust leak ahead of O2 sensor; low fuel pressure | VAG 5-digit: 17536. Ross-Tech MAF tech tip: a dying MAF under-reports airflow and the ECU compensates lean — check MAF g/s against spec under load, not just at idle. WD-40/propane around intake joints to find vacuum leaks. |
| P1129 | Long Term Fuel Trim — System Too Rich (Bank 2) | P | manufacturer | [C] | — | Bank-2 counterpart of P1127. From the community VW fault-code list. |
| P1130 | Long Term Fuel Trim — System Too Lean (Bank 2) | P | manufacturer | [C] | — | Bank-2 counterpart of P1128. From the community VW fault-code list. |
| P1136 | Long Term Fuel Trim Additive Fuel — System Too Lean (Bank 1) | P | manufacturer | [C] | — | Additive (idle-range) trim variant. From the community VW fault-code list. |
| P1137 | Long Term Fuel Trim Additive Fuel — System Too Rich (Bank 1) | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1138 | Long Term Fuel Trim Additive Fuel — System Too Lean (Bank 2) | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1139 | Long Term Fuel Trim Additive Fuel — System Too Rich (Bank 2) | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1141 | Load Calculation Cross Check — Range/Performance | P | manufacturer | [C] | faulty MAF sensor (classic 1.8T cause); intake leaks | Well-known 1.8T code — the ECU cross-checks MAF against throttle/rpm model. From the community VW fault-code list. |
| P1144 | Mass Air Flow Sensor — Open / Short to Ground | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1145 | Mass Air Flow Sensor — Short to Positive | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1146 | Mass Air Flow Sensor — Supply Voltage | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1155 | Manifold Absolute Pressure Sensor — Short to Positive | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1156 | Manifold Absolute Pressure Sensor — Open / Short to Ground | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1157 | Manifold Absolute Pressure Sensor — Supply Voltage | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1160 | Intake Air Temperature Sensor — Short to Ground | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1161 | Intake Air Temperature Sensor — Open / Short to Positive | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1162 | Intake Air Temperature Sensor — Short to Ground | P | manufacturer | [C] | — | From the community VW fault-code list (duplicate-text variant of P1160 in the source). |
| P1163 | Fuel Temperature Sensor — Open / Short to Positive | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1164 | Fuel Temperature Sensor — Implausible Signal | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1171 | Throttle Actuation Potentiometer Signal 2 — Range/Performance | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1172 | Throttle Actuation Potentiometer Signal 2 — Signal Too Low | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1173 | Throttle Actuation Potentiometer Signal 2 — Signal Too High | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1176 | Rear O2S Correction | P | manufacturer | [C] | — | From the community VW fault-code list; terse source text. |
| P1177 | O2 Correction Behind Catalyst Bank 1 — Limit Attained | P | manufacturer | [C] | aging catalyst; exhaust leak | From the community VW fault-code list. |
| P1196 | O2 Sensor Heater Circuit Bank 1 Sensor 1 — Electrical Malfunction | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1197 | O2 Sensor Heater Circuit Bank 2 Sensor 1 — Electrical Malfunction | P | manufacturer | [C] | — | From the community VW fault-code list. |
| P1201 | Cylinder 1 Fuel Injector Circuit — Electrical Malfunction | P | manufacturer | [C] | injector coil open/shorted; wiring fault; driver fault in ECU | VAG 5-digit: 17609. Pattern repeats P1201–P1208 for cylinders 1–8. |
| P1208 | Cylinder 8 Fuel Injector Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17616. Pattern P1201–P1208 covers cylinders 1–8 (electrical malfunction). |
| P1213 | Cylinder 1 Fuel Injector Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17621. Pattern P1213–P1220 = cylinders 1–8 short to B+. |
| P1225 | Cylinder 1 Fuel Injector Circuit — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17633. Pattern P1225–P1232 = cylinders 1–8 short to ground. |
| P1237 | Cylinder 1 Fuel Injector Circuit — Open Circuit | P | manufacturer | [C] | — | VAG 5-digit: 17645. Pattern P1237–P1244 = cylinders 1–8 open circuit. |
| P1250 | Fuel Level Too Low | P | manufacturer | [C] | actually low fuel; faulty fuel level sender | VAG 5-digit: 17656. Informational — set when the tank runs dry; can accompany lean codes. |
| P1325 | Cylinder 1 Knock Control — Limit Attained | P | manufacturer | [C] | poor fuel quality; carbon buildup; excessive timing advance | VAG 5-digit: 17733. Pattern P1325–P1332 = cylinders 1–8 knock control at limit. |
| P1332 | Cylinder 8 Knock Control — Limit Attained | P | manufacturer | [C] | — | VAG 5-digit: 17740. End of the P1325–P1332 cylinder 1–8 pattern. |
| P1339 | Crankshaft Position / Engine Speed Sensors — Cross Connected | P | manufacturer | [C] | sensors swapped during repair; wiring mix-up | VAG 5-digit: 17747. Appears after sensor replacement with connectors crossed. |
| P1340 | Camshaft Position Sensor (G40) / Engine Speed Sensor (G28) — Incorrect Correlation | P | manufacturer | [B] | timing belt/chain incorrectly installed (chain probably lengthened); Camshaft Position Sensor (G40) faulty; Engine Speed Sensor (G28) faulty | VAG 5-digit: 17748. Ross-Tech: check timing installation (use MVB to check chain), check/replace G40 and G28. Special notes: on 1.8T check engine oil pressure (pickup may be restricted) and confirm the correct G40 is installed (single-gap vs 4-gap); on VR6 see Technical Bulletin 15-07-03; on 30-valve V6 with companion code 17755 check cam chain tensioners are on the correct heads. Almost always a mechanical timing deficiency, not just a sensor. |
| P1341 | Ignition Coil Power Output Stage 1 — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17749. Pattern: P1341/P1343/P1345 = stages 1/2/3 short to ground. |
| P1343 | Ignition Coil Power Output Stage 2 — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17751 |
| P1345 | Ignition Coil Power Output Stage 3 — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17753 |
| P1391 | Camshaft Position Sensor (Bank 2) — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17799 |
| P1392 | Camshaft Position Sensor (Bank 2) Open — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17800 |
| P1393 | Ignition Coil Power Output Stage 1 — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17801. Pattern P1393–P1395 = stages 1–3 electrical malfunction. |
| P1396 | Engine Speed Sensor — Missing Tooth | P | manufacturer | [C] | damaged reluctor ring; faulty G28 | VAG 5-digit: 17804 |
| P1400 | EGR Valve Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17808 |
| P1401 | EGR Valve Circuit — Power Stage Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17809 |
| P1402 | EGR Valve Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17810 |
| P1407 | EGR Temperature Sensor — Signal Too Low | P | manufacturer | [C] | — | VAG 5-digit: 17815 |
| P1408 | EGR Temperature Sensor — Signal Too High | P | manufacturer | [C] | — | VAG 5-digit: 17816 |
| P1409 | Tank Ventilation Valve — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17817 |
| P1410 | Tank Ventilation Valve — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17818 |
| P1411 | Secondary Air Injection System (Bank 2) — Restricted Flow | P | manufacturer | [C] | — | VAG 5-digit: 17819 |
| P1414 | Secondary Air Injection System (Bank 2) — Leak Detected | P | manufacturer | [C] | — | VAG 5-digit: 17822 |
| P1418 | Fuel Level Sensor — Signal Too High | P | manufacturer | [C] | — | VAG 5-digit: 17826 |
| P1420 | Secondary Air Injection System Control Module — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17828 |
| P1421 | Secondary Air Injection System Control Valve Circuit — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17829 |
| P1422 | Secondary Air Injection System Control Valve Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17830 |
| P1423 | Secondary Air Injection System (Bank 1) — Flow Too Low | P | manufacturer | [C] | combi valve stuck; SAI pump weak; hoses split | VAG 5-digit: 17831 |
| P1424 | Secondary Air Injection System (Bank 1) — Leak Detected | P | manufacturer | [C] | — | VAG 5-digit: 17832 |
| P1425 | Tank Ventilation Valve — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17833 |
| P1426 | Tank Ventilation Valve — Open Circuit | P | manufacturer | [C] | — | VAG 5-digit: 17834 |
| P1434 | Secondary Air Injection System Pump Relay Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17842 |
| P1436 | Secondary Air Injection System Pump Relay Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17844 |
| P1440 | EGR Valve Circuit — Power Stage Open | P | manufacturer | [C] | — | VAG 5-digit: 17848 |
| P1450 | Secondary Air Injection System Pump Relay Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17858. Source text duplicates P1434 wording; kept as transcribed. |
| P1451 | Secondary Air Injection System Pump Relay Circuit — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 17859 |
| P1452 | Secondary Air Injection System Pump Relay Circuit — Open Circuit | P | manufacturer | [C] | — | VAG 5-digit: 17860 |
| P1470 | EVAP Emission Control System Leak Detection Pump Circuit — Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17878 |
| P1471 | EVAP Emission Control System Leak Detection Pump Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17879 |
| P1475 | EVAP Emission Control System Leak Detection Pump — Malfunction, Signal Circuit Open | P | manufacturer | [C] | — | VAG 5-digit: 17883 |
| P1476 | EVAP Emission Control System Leak Detection Pump — Malfunction / Insufficient Vacuum | P | manufacturer | [B] | EVAP system faulty/leaking; leak detection pump faulty; insufficient vacuum supply to the pump | VAG 5-digit: 17884. Check the EVAP system for leaks, check the LDP itself, check vacuum supply at the LDP. Technician guidance: check the gas cap first (worn seal), then inspect all vacuum lines — the braided fabric lines near the air filter housing are known to fail; larger lines can soften, collapse or split. The LDP sits below the air filter housing at the frame rail (2.0). VCDS basic settings can exercise the LDP (listen for clicking). |
| P1477 | EVAP Emission Control System Circuit — Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17885. From the Bentley-derived DTC table; not in the PDF transcription. |
| P1478 | EVAP Emission Control System — Clamped Tube Detected | P | manufacturer | [C] | kinked/clamped EVAP hose | VAG 5-digit: 17886. From the Bentley-derived DTC table; not in the PDF transcription. |
| P1500 | Fuel Pump Relay Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17908 |
| P1502 | Fuel Pump Relay Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17910 |
| P1504 | Intake Air System — Leak Detected (Bypass Air Determined) | P | manufacturer | [C] | — | VAG 5-digit: 17912 |
| P1509 | Idle Air Control Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17917 |
| P1510 | Idle Air Control Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17918 |
| P1511 | Intake Manifold Changeover Valve Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17919 |
| P1512 | Intake Manifold Changeover Valve Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17920. Related: P1521 (changeover valve 2 electrical malfunction). |
| P1516 | Intake Manifold Changeover Valve 2 Circuit — Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 17924 (Bentley-derived table; numbering offset vs PDF). From the scribd DTC table. |
| P1518 | Intake Camshaft Control Bank 1 — Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17926. From the scribd DTC table. |
| P1521 | Intake Manifold Changeover Valve 2 Circuit — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17929. From the scribd DTC table. |
| P1522 | Intake Camshaft Control Bank 2 — Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17930. From the scribd DTC table. |
| P1525 | Intake Camshaft Control Bank 1 — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 17933. From the scribd DTC table. |
| P1543 | Throttle Actuation Potentiometer — Signal Too Low | P | manufacturer | [C] | — | VAG 5-digit: 17951 |
| P1544 | Throttle Actuation Potentiometer — Signal Too High | P | manufacturer | [C] | — | VAG 5-digit: 17952 |
| P1580 | Throttle Actuator (Bank 1) — Malfunction | P | manufacturer | [B] | low battery voltage; throttle body fault | VAG 5-digit: 17988. May be caused by a low battery if found together with 16487/P0103 — check charging system first. |
| P1582 | Idle Adaptation at Limit | P | manufacturer | [C] | vacuum leak; dirty throttle body | VAG 5-digit: 17990 |
| P1600 | Power Supply (B+) Terminal 15 — Low Voltage | P | manufacturer | [C] | weak battery; poor terminal 15 supply | VAG 5-digit: 18008 |
| P1602 | Power Supply (B+) Terminal 30 — Low Voltage | P | manufacturer | [B] | battery disconnected or discharged; blown fuse; wiring fault | VAG 5-digit: 18010. The classic "battery was disconnected" signature — frequently spurious after battery work; clear and recheck. |
| P1606 | Rough Road Specification Engine Torque (ABS Control Unit) — Electrical Malfunction | P | manufacturer | [C] | — | VAG 5-digit: 18014 |
| P1611 | MIL Call-up Circuit / Transmission Control Module — Short to Ground | P | manufacturer | [C] | — | VAG 5-digit: 18019 |
| P1612 | Engine Control Module — Incorrectly Coded | P | manufacturer | [C] | wrong coding after module replacement; coding lost | VAG 5-digit: 18020. Recode the ECU with VCDS/ODIS. |
| P1613 | MIL Call-up Circuit — Open or Short to B+ | P | manufacturer | [C] | — | VAG 5-digit: 18021 |
| P1704 | Kick-down Switch — Short to Ground (F8) | P | manufacturer | [C] | — | VAG 5-digit: 00296 |
| P1711 | ABS Wheel Speed Signal 1 (Left Front) — Range/Performance (G47) | P | manufacturer | [C] | — | VAG 5-digit: 00283. Transmission sees these when the ABS wheel-speed signal is implausible. |
| P1716 | ABS Wheel Speed Signal 2 (Right Front) — Range/Performance (G45) | P | manufacturer | [C] | — | VAG 5-digit: 00285 |
| P1721 | ABS Wheel Speed Signal 3 (Right Rear) — Range/Performance (G44) | P | manufacturer | [C] | — | VAG 5-digit: 00287 |
| P1726 | ABS Wheel Speed Signal 4 (Left Rear) — Range/Performance (G46) | P | manufacturer | [C] | — | VAG 5-digit: 00290 |
| P1728 | Varying ABS Wheel Speed Signals — Range/Performance | P | manufacturer | [C] | mismatched tire sizes; faulty wheel-speed sensor | VAG 5-digit: 00597 |
| P1746 | Transmission Control Module Relay — Supply Voltage (B+) Malfunction, Low | P | manufacturer | [C] | low battery; bad ground | VAG 5-digit: 00532. Table notes "Low Battery or Bad Ground". |
| P1749 | Transmission Control Module — Incorrectly Coded | P | manufacturer | [C] | — | VAG 5-digit: 01044. Recode the TCM. |
| P1750 | Supply Voltage (B+) | P | manufacturer | [C] | — | VAG 5-digit: 00532 (shared with P1746). Terse source text. |
| P1766 | Throttle Angle Signal — Stuck Off | P | manufacturer | [C] | — | VAG 5-digit: 00638 (shared with P1767) |
| P1767 | Throttle Angle Signal — Stuck On | P | manufacturer | [C] | — | VAG 5-digit: 00638 (shared with P1766) |
| P1771 | Load Signal — Stuck Off (RPM Signal Missing) | P | manufacturer | [C] | — | VAG 5-digit: 00549 (shared with P1772) |
| P1772 | Load Signal — Stuck On (RPM Signal Missing) | P | manufacturer | [C] | — | VAG 5-digit: 00549 (shared with P1771) |
| P1780 | Engine Intervention — Unreadable | P | manufacturer | [C] | loose ECM power relay | VAG 5-digit: 00545 (shared with P1781/P1782). Table notes "also check for loose ECM power relay". |
| P1781 | Engine Intervention — Stuck Off | P | manufacturer | [C] | — | VAG 5-digit: 00545 |
| P1782 | Engine Intervention — Stuck On | P | manufacturer | [C] | — | VAG 5-digit: 00545 |
| U1121 | Databus — Missing Message | U | manufacturer | [A] | indicated control module not transmitting; wiring/connector fault; module offline after coding change | VW TSB 01-21-10 lists U112100 as logged across multiple control units (front camera, HV battery charger, etc.), usually passive/sporadic. Extremely common on MQB-platform vehicles — often a consequence of another module's fault rather than a databus wiring problem. Diagnose the indicated missing-message source (symptom byte identifies it) before condemning wiring. |
| U1122 | Databus — Implausible Message | U | manufacturer | [B] | transmitting module sending out-of-range values; software mismatch after retrofit | Seen in VCDS scans as "U1122 00 - Implausible Message". Often accompanies retrofits or module swaps. |
| U1123 | Databus — Received Error Value | U | manufacturer | [A] | transmitting module reporting an error state; e.g. ACC reporting irreversible error cascades U1123 into dependent modules | VW TSB 01-21-10 lists U112300 (received error value for data bus). VCDS scans show it with a bracketed source identifier (e.g. the ACC or instrument cluster message that carried the error value). Usually passive; clear and road-test. |

_Generated by scripts/build.py — do not hand-edit._
