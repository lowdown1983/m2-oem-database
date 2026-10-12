# Toyota / Lexus — Manufacturer-Specific DTCs

Research for the M2 OEM vehicle database (v1.2.1). Covers Toyota/Lexus-specific
(P1xxx/B1xxx/C1xxx/U1xxx) codes only — SAE J2012 generic codes (P0xxx, B0xxx,
C0xxx, U0xxx) are already in the database and are NOT duplicated here, except
where a Toyota-specific note applies.

Every factual claim carries a quality grade: **A** = Toyota/Lexus service manual
or TSB excerpt · **B** = reputable DTC database or multi-source agreement ·
**C** = single community source. Unverified items are marked [?].
Research date: 2026-10-06.

Toyota quirks relevant to DTC work:
- Toyota DTCs are often printed with a 2-digit sub-code (e.g. C1201/51, B1181/18,
  U0100/65) — the 5-character code is the OBD-II DTC; the sub-code is the
  Toyota internal detail code [B — Toyota repair-manual DTC charts].
- C1201 (Engine Control System Malfunction) is INFORMATIONAL: the skid control
  ECU sets it whenever any engine DTC is present and disables TRAC/VSC. Fix the
  engine (P-) code and C1201 clears — do not chase it as a brake fault [B].
- Hybrid P0Axx codes are SAE generic — not listed here. Toyota hybrid-specific
  codes live in the P1xxx/P3xxx manufacturer ranges (P1636, P3190, P3191) [B].
- P1121 is model-dependent: accelerator-pedal meaning on most models, but the
  2004 Prius repair manual (RM1075U) defines it as the CHS coolant-flow-control
  water valve — see the conflict note under P1121 [A].

---

## P1100
- Description: BARO Sensor Circuit
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1120
- Description: Accelerator Pedal Position Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in accelerator pedal position sensor circuit; faulty accelerator pedal position sensor; faulty engine ECU
- Diagnostic notes: If stored, the ECM shuts down power to the throttle motor and magnetic clutch; the throttle valve closes via return spring (limp-home on the cable). Check VPA/VPA2 voltages (0-5V sweep with pedal).
- Grade: [A] description; [B] causes (service-manual trouble areas)
- Evidence: Toyota/Lexus service manual excerpts (jzgte.com 1UZ-FE diagnostics; clublexus.com LS430 DI-101) — circuit description and fail-safe behavior

## P1121
- Description: Accelerator Pedal Position Sensor Range/Performance Problem
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — model-dependent meaning. The 2004 Prius repair manual (RM1075U) defines P1121 as "COOLANT FLOW CONTROL VALVE POSITION SENSOR CIRCUIT STUCK" (CHS water valve position sensor / tank outlet temp sensor) [A]. Most other Toyota models use the accelerator-pedal range/performance meaning [B]. Confirm against the model-specific manual.
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; conflict from Prius RM1075U via priuschat attachment

## P1125
- Description: Throttle Control Motor Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in throttle control motor circuit; faulty throttle control motor; faulty ECM
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2001 Prius repair manual RM778U detection-item table (via carmanualsonline.info); retrolib.info list agrees

## P1126
- Description: Magnetic Clutch Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Throttle-body magnetic clutch circuit (ETCS). Check clutch circuit continuity.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1127
- Description: ETCS Actuator Power Source Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open in ETCS power source circuit; faulty ECM
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2001 Prius repair manual RM778U (open in ETCS power source circuit); retrolib.info agrees

## P1128
- Description: Throttle Control Motor Lock Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: throttle control motor; throttle body (carbon/deposit lock)
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2001 Prius repair manual RM778U; retrolib.info agrees

## P1129
- Description: Electric Throttle Control System Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: electric throttle control system; ECM
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2001 Prius repair manual RM778U; retrolib.info agrees

## P1130
- Description: Air/Fuel Sensor Circuit Range/Performance (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: faulty A/F sensor (Bank 1 Sensor 1); wiring; ECM
- Diagnostic notes: Toyota uses wideband A/F sensors (not conventional O2) upstream; test with a scan tool reading A/F sensor current/voltage, not a simple rich/lean toggle.
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; JustAnswer Toyota master-technician thread (P1150 family context)

## P1133
- Description: Air/Fuel Sensor Circuit Response (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: aging A/F sensor (slow response); exhaust leaks ahead of sensor
- Diagnostic notes: Response/slow-response code — the sensor still functions but is lazy; often intermittent before setting permanently.
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; multi-source agreement on A/F response semantics

## P1135
- Description: Air/Fuel Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open/short in heater circuit; failed sensor heater element
- Diagnostic notes: Check heater resistance at the sensor connector before replacing the sensor.
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; standard Toyota A/F heater diagnostics

## P1150
- Description: Air/Fuel Sensor Circuit Range/Performance (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: A/F sensor nearing end of life (may test good intermittently); wiring
- Diagnostic notes: CONFLICT — retrolib.info transcribes this as "(Bank 1 Sensor 2)", but Toyota service-manual convention (P1150/P1153/P1155 = Bank 2 Sensor 1) and a Toyota master technician (JustAnswer) confirm Bank 2 Sensor 1. A sensor can read fine at times then fail — the MIL cycling on/off is the classic end-of-life pattern.
- Grade: [B]
- Evidence: JustAnswer Toyota master-technician thread (Genchi Genbutsu); Toyota A/F code convention

## P1153
- Description: Air/Fuel Sensor Circuit Response (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: aging A/F sensor; exhaust leak ahead of sensor
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; Toyota A/F code convention

## P1155
- Description: Air/Fuel Sensor Heater Circuit Malfunction (Bank 2 Sensor 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open/short in heater circuit; failed sensor heater element
- Diagnostic notes: Check heater resistance at the sensor connector first.
- Grade: [B]
- Evidence: retrolib.info Toyota-specific list; Toyota A/F code convention

## P1200
- Description: Fuel Pump Relay Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1300
- Description: Igniter Circuit Malfunction (No. 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in IGF1/IGT1 circuit from No. 1 ignition coil with igniter to ECM; faulty No. 1 ignition coil with igniter; faulty ECM
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-115)

## P1305
- Description: Igniter Circuit Malfunction (No. 2)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in IGF2/IGT2 circuit; faulty No. 2 ignition coil with igniter; faulty ECM
- Diagnostic notes: Numbering is model-dependent — on the 2001 Prius the sequence is P1300 (No.1), P1305 (No.2), P1310 (No.3), P1315 (No.4); other models number P1300/P1310 as No.1/No.2.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-115)

## P1310
- Description: Igniter Circuit Malfunction (No. 3)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in IGF/IGT circuit; faulty ignition coil with igniter; faulty ECM
- Diagnostic notes: See P1305 numbering note — verify per model.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-115)

## P1315
- Description: Igniter Circuit Malfunction (No. 4)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in IGF1/IGT4 circuit; faulty No. 4 ignition coil with igniter; faulty ECM
- Diagnostic notes: See P1305 numbering note — verify per model.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-115)

## P1335
- Description: No Crankshaft Position Sensor Signal - Engine Running
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1345
- Description: Variable Valve Timing Sensor Circuit (Left Bank)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Left/right bank split applies to V-engine models; on inline engines use the Bank 1 codes (P1346/P1349).
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1346
- Description: VVT Sensor / Camshaft Position Sensor Circuit Range/Performance Problem (Bank 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: faulty VVT (camshaft position) sensor; VVT sensor harness open/shorted or poor connection; low/dirty engine oil (VVT-i is oil-pressure actuated); stuck/faulty oil control valve (OCV); stretched timing chain/belt or jumped teeth; faulty ECM (rare)
- Diagnostic notes: The ECM compares crankshaft (NE) and camshaft (VV) signals; check engine oil level/condition FIRST (cheap, common). 2001 Prius manual lists "mechanical system (jumping teeth of timing belt, belt stretched)" as a trouble area.
- Grade: [B]
- Evidence: charm.li 2002 Lexus GS300 (2JZ-GE) service manual excerpt; 2001 Prius RM778U (DI-120); toyotaspace.com, cardiag.me, eobdcode.com agree

## P1349
- Description: VVT System Malfunction (Bank 1)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: valve timing off; faulty OCV; faulty VVT controller assembly; faulty ECM
- Diagnostic notes: System-level code (vs P1346 sensor-level): points at the VVT-i actuator/oil-control side rather than the sensor circuit.
- Grade: [B]
- Evidence: 2001 Prius repair manual RM778U (DI-121); retrolib.info agrees

## P1350
- Description: Variable Valve Timing Sensor Circuit Fault (Right Bank)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P1345 bank note.
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1351
- Description: Variable Valve Timing Sensor Out of Range (Right Bank)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P1345 bank note.
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1354
- Description: Variable Valve Timing Circuit Fault (Right Bank)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P1345 bank note.
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1400
- Description: Sub-Throttle Position Sensor Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1401
- Description: Sub-Throttle Position Sensor Range/Performance Problem
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1405
- Description: Turbo Pressure Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Diesel/turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1406
- Description: Turbo Pressure Sensor Range/Performance Problem
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Diesel/turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1410
- Description: EGR Valve Position Sensor Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1411
- Description: EGR Valve Position Sensor Circuit Range/Performance
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1430
- Description: Vacuum Sensor for Adsorber and Catalyst System Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in vacuum sensor circuit; faulty vacuum sensor for HC adsorber and catalyst system; faulty ECM
- Diagnostic notes: 2001 Prius HC-adsorber/catalyst system.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-127)

## P1431
- Description: Vacuum Sensor for Adsorber and Catalyst System Circuit Range/Performance Problem
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: faulty vacuum sensor for HC adsorber and catalyst system; vacuum line fault
- Diagnostic notes: 2001 Prius HC-adsorber/catalyst system.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-131)

## P1436
- Description: Variable Valve Malfunction (HC Adsorber and Catalyst System)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: vacuum line; actuator for HC adsorber and catalyst system; front exhaust pipe
- Diagnostic notes: 2001 Prius HC-adsorber/catalyst system.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-133)

## P1437
- Description: Vacuum Line Malfunction (HC Adsorber and Catalyst System)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: vacuum line; VSV for HC adsorber and catalyst system; check valve
- Diagnostic notes: 2001 Prius HC-adsorber/catalyst system.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-135)

## P1455
- Description: Vapor Reducing Fuel Tank System Leak Detected (Small Leak)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: hose and pipe; heated oxygen sensor; fuel system; VVT system; ignition system; mass air flow meter; ECM
- Diagnostic notes: 2001 Prius vapor-reducing fuel tank system (EVAP-adjacent).
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-140)

## P1500
- Description: Starter Signal Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1510
- Description: Boost Pressure Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1511
- Description: Boost Pressure Low
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1512
- Description: Boost Pressure High
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1520
- Description: Stop Lamp Switch Signal Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Stop-lamp switch input is used by cruise control and shift interlock; check switch adjustment.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1525
- Description: Resolver Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: HV ECU; engine ECU
- Diagnostic notes: Hybrid transaxle resolver (motor position sensor) circuit — hybrid models only.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-141)

## P1565
- Description: Cruise Control Main Switch Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1600
- Description: ECM BATT Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open in back-up power source circuit (BATT terminal wiring, EFI fuse); faulty ECM
- Diagnostic notes: Battery voltage is supplied to the ECM BATT terminal even with ignition OFF (DTC memory, A/F adaptives). HINT from the manual: if P1600 is present, the ECM does not store any other DTC. Check BATT terminal voltage (9-14V) and the EFI fuse first.
- Grade: [A]
- Evidence: Toyota/Lexus service manuals (2000 Celica RM744U, 2000 Lexus SC300/SC400 RM715U via jzgte.com/safe-manuals.com)

## P1603
- Description: Engine Stall History
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: ignition system (spark plug, ignition coil); fuel system (injector, fuel pump, fuel quality); intake/exhaust (MAF, air leaks, throttle body, A/F sensor, VVT system); ECM; wiring/connectors; engine coolant temp sensor
- Diagnostic notes: Stored when the engine stops without the ignition/engine switch being operated (after P1604 startability monitoring finishes). ALWAYS check whether the vehicle ran out of fuel first — stalling from an empty tank sets this code. MIL does not come on; DTC stored in memory.
- Grade: [B]
- Evidence: Toyota repair-manual SFI/ECD excerpts via zatonevkredit.ru (multiple models agree)

## P1604
- Description: Startability Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: immobiliser system; engine assembly (excess friction, compression loss); starter; crankshaft position sensor; coolant temp sensor; fuel pump/control system; fuel pipes; injector; throttle body; fuel pressure regulator; battery; spark plug; ignition coil circuit; intake system; camshaft timing OCV; MAF meter; A/F sensor; valve timing; purge VSV; EGR; ECM
- Diagnostic notes: Stored when the engine does not start despite STA signal input, takes a long time to start, or stalls just after starting (drops to 200 rpm or less within ~2 seconds). Check fuel level FIRST — running out of fuel sets this code. Then review freeze-frame data via Techstream/GTS.
- Grade: [A]
- Evidence: Toyota service manual excerpts via lexusgxor.com and toyotaspace.com (DTC P1604 description/detection/trouble-area tables)

## P1605
- Description: Rough Idling
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — older Toyota-specific lists (retrolib.info) define P1605 as "Knock Control CPU" [C]. Newer Toyota repair-manual excerpts pair P1605 with P1603 as "Rough Idling" [B]. Meaning is era/model-dependent; confirm against the model-specific manual.
- Grade: [B]
- Evidence: Toyota repair-manual excerpts via zatonevkredit.ru (P1603/P1605); conflict from retrolib.info

## P1630
- Description: Traction Control System Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1633
- Description: ECU Malfunction (ETCS Circuit)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: ECM (internal ETCS circuit fault)
- Diagnostic notes: 2001 Prius lists this as an ECM-internal fault — the listed remedy is ECM replacement after ruling out external circuits.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-145)

## P1636
- Description: HV ECU Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: HV ECU; engine ECU
- Diagnostic notes: Hybrid models only.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-146)

## P1637
- Description: EGSTP Signal Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: HV ECU; engine ECU
- Diagnostic notes: Hybrid models only (EGSTP = engine-stop signal line between HV ECU and engine ECU).
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-148)

## P1645
- Description: Body Control Module Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1647
- Description: Transmission Control Module Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1652
- Description: Idle Air Control Valve Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1656
- Description: OCV Circuit Malfunction (for VVT-i)
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: open or short in OCV circuit; faulty oil control valve (OCV); faulty ECM
- Diagnostic notes: The OCV meters oil pressure to the VVT-i controller — a frequent companion to P1346/P1349.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-150)

## P1658
- Description: Wastegate Valve Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Turbo models.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1661
- Description: EGR Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1662
- Description: EGR Bypass Valve Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P1663
- Description: Right Oil Control Valve / Variable Valve Timing System
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P1345 bank note.
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1690
- Description: Oil Control Valve / Variable Valve Timing System Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1692
- Description: Oil Control Valve / Variable Valve Timing System Open
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1693
- Description: Oil Control Valve / Variable Valve Timing System Closed
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1700
- Description: Transmission Output Shaft Speed Sensor Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1705
- Description: Automatic Transmission Direct Clutch Speed Sensor Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1715
- Description: ABS Rear Wheel Speed Sensor Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Transmission code referencing the ABS rear wheel-speed input.
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1725
- Description: Automatic Transmission Input Shaft Speed Sensor / Turbine Speed Sensor Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1730
- Description: Automatic Transmission Intermediate Shaft Speed Sensor Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1755
- Description: Torque Converter Clutch Solenoid Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1760
- Description: Automatic Transmission Pressure Control Shift Solenoid Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1765
- Description: Automatic Transmission Pressure Control Shift Solenoid Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Lexus/Toyota OBD-II codes guide (single community source)

## P1780
- Description: Park/Neutral Position Switch Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: A/T only.
- Grade: [C]
- Evidence: retrolib.info Toyota-specific DTC list (single transcription)

## P3190
- Description: Poor Engine Power
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: air induction system; throttle body; fuel pressure; engine; mass air flow meter
- Diagnostic notes: Hybrid models (2001 Prius): engine cannot produce expected power.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-153)

## P3191
- Description: Engine Does Not Start
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: mass air flow meter; out of fuel; engine coolant temp sensor; crankshaft position sensor; camshaft position sensor; ECM
- Diagnostic notes: Hybrid models (2001 Prius). Check fuel level first.
- Grade: [A]
- Evidence: 2001 Prius repair manual RM778U (DI-153)

---

## B1181
- Description: Open in D Squib (2nd Step) Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: open in D+ or D- wire harness of squib; D squib (2nd step) malfunction; spiral cable sub-assembly malfunction; airbag sensor assembly center malfunction
- Diagnostic notes: Driver airbag 2nd-stage squib circuit. Disconnect battery, wait 90+ seconds before probing SRS circuits. Check D2+/D2- resistance (below 1 ohm OK). A broken clockspring (spiral cable) is the most common cause on high-mileage vehicles.
- Grade: [A] description; [B] causes (service-manual trouble areas + field experience)
- Evidence: 2004 Corolla repair manual RM1037U SRS diagnostics (via scribd.com); fixya.com field thread (clockspring)

## B1207
- Description: Smart ECU Communication Stop
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: smart ECU malfunction; wire harness (MPX lines); gateway ECU
- Diagnostic notes: Stored when communication between the smart ECU and gateway ECU stops for more than 10 seconds. 2004 Prius multiplex system.
- Grade: [A]
- Evidence: 2004 Prius repair manual RM1076E (05-2266, via toyotamanuals.gitlab.io)

## B1660
- Description: P Seat Airbag Active Mode Indicator Circuit Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: open/short to ground or short to B+ in passenger airbag ON/OFF indicator circuit; faulty telltale light assembly; faulty airbag ECU assembly; instrument panel wire harness
- Diagnostic notes: Passenger airbag ON/OFF indicator circuit fault (not the airbag itself). A common field fix on Highlanders is the indicator LED/board in the overhead console.
- Grade: [A] description; [B] causes (Toyota Service Information trouble areas)
- Evidence: Toyota Service Information print 2023 (via scribd.com B1660 document)

## B1901
- Description: Open in P/T Squib (RH) Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: deployed seatbelt pretensioner (RH); open in pretensioner squib circuit; wiring
- Diagnostic notes: "P/T squib" = seatbelt pretensioner squib. If the vehicle was in a crash, check the pretensioner for deployment (orange visible through inspection holes = popped, replace the assembly). 2006-2011 Yaris SRS codes are identical across those years.
- Grade: [C]
- Evidence: yarisworld.com forum (single community thread, experienced member)

---

## C0278
- Description: Open or Short in ABS Solenoid Relay Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: ABS solenoid relay; wiring; skid control ECU
- Diagnostic notes: Seen on LX470/land-cruiser-family ABS. Often appears in a cascade with other ABS codes when battery voltage is low — address C1241 first.
- Grade: [C]
- Evidence: ih8mud.com forum (single owner report with Techstream readout)

## C1201
- Description: Engine Control System Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: any stored engine (P-code) malfunction — this code is a consequence, not a root cause
- Diagnostic notes: INFORMATIONAL. Set by the skid control ECU whenever the engine control system has a malfunction; TRAC/A-TRAC/VSC are disabled as fail-safe. CONFLICT: an AI-generated JustAnswer snippet describes C1201 as a crankshaft-position/MAP-sensor circuit code — that contradicts the Toyota brake-control DTC chart (BC-85), which defines it as Engine Control System Malfunction [A/B]. Diagnose and repair the underlying P-code; C1201 then clears.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com "Toyota DTCs for Brake Control System"); JustAnswer Toyota thread (P0430/C1201 case)

## C1203
- Description: ECM Communication Circuit Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: ECM; CAN communication circuit; skid control ECU
- Diagnostic notes: Brake-control-system view of an ECM communication loss.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1210
- Description: Zero Point Calibration of Yaw Rate Sensor Undone
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: zero point calibration incomplete (e.g. after sensor/ECU replacement or battery disconnect); faulty yaw rate sensor
- Diagnostic notes: Perform yaw-rate-sensor zero-point calibration with Techstream (on level ground, steering centered), then clear the code.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1223
- Description: ABS Control System Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; ABS actuator circuit faults
- Diagnostic notes: General ABS-system fault flag — read the accompanying specific C-codes (wheel speed, solenoid) for the real fault.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1231
- Description: Steering Angle Sensor Circuit Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: steering angle sensor; sensor circuit; sensor power supply; CAN communication system
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1232
- Description: Stuck in Deceleration Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate / deceleration sensor; sensor circuit
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1234
- Description: Yaw Rate Sensor Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate sensor; yaw rate sensor circuit
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1241
- Description: Low Battery Positive Voltage or Abnormally High Battery Positive Voltage
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: low battery charge; faulty battery; faulty charging system (alternator); power source circuit fault to the skid control ECU
- Diagnostic notes: Recorded when voltage at the skid-control-ECU terminal falls outside the detection threshold. A weak battery causes CASCADING false ABS/VSC codes (C0278, C1223, C1231, C1253, C1256, C1340 often appear together) — always load-test the battery and charging system before chasing the other codes. Seen on Prius ABS/VSC/TRAC reports and LX470.
- Grade: [B]
- Evidence: JustAnswer Toyota thread (technician description); priuschat.com Techstream ABS report (C1241 current); ih8mud.com cascade case

## C1242
- Description: Open Circuit in IG1/IG2 Power Source Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: IG1/IG2 power source wiring; fuse; skid control ECU power circuit
- Diagnostic notes: Seen on Prius ABS/VSC/TRAC Techstream reports.
- Grade: [C]
- Evidence: priuschat.com Techstream diagnostic report (single owner report)

## C1249
- Description: Open in Stop Lamp Switch Power Line
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: break or damage in the power line supplying the stop lamp switch
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd.com Toyota DTC fault-codes guide (single community source)

## C1253
- Description: Hydro-Booster Pump Motor Relay Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: pump motor relay; wiring; accumulator pressure
- Diagnostic notes: Land Cruiser / LX470 brake hydro-booster system. Often cascades with C1241 (low voltage).
- Grade: [C]
- Evidence: ih8mud.com forum (single owner Techstream readout)

## C1256
- Description: Accumulator Low Pressure
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: accumulator; hydro-booster pump; low system voltage
- Diagnostic notes: Seen on Prius and LX470 brake reports; check C1241 first.
- Grade: [C]
- Evidence: ih8mud.com forum; priuschat.com Techstream ABS report

## C1271
- Description: Low Output Signal of Front Speed Sensor RH (Test Mode DTC)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: front speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor
- Diagnostic notes: Test-mode DTC — set during the ABS sensor check function, not during normal driving.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1272
- Description: Low Output Signal of Front Speed Sensor LH (Test Mode DTC)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: front speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor
- Diagnostic notes: Test-mode DTC — see C1271.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1273
- Description: Low Output Signal of Rear Speed Sensor RH (Test Mode DTC)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: rear speed sensor; sensor circuit; sensor installation; foreign matter on sensor rotor
- Diagnostic notes: Test-mode DTC — see C1271.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1290
- Description: Steering Angle Sensor Zero Point Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate/deceleration sensor zero-point calibration incomplete; poor steering-wheel center adjustment; poor front wheel alignment
- Diagnostic notes: Perform zero-point calibration (level ground, centered steering, correct alignment) with Techstream.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1300
- Description: Skid Control ECU Malfunction (ABS ECU Malfunction)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: software malfunction in the skid control ECU; oxidized contacts; damaged power supply wiring to the module
- Diagnostic notes: Seen as current on a Prius Techstream ABS report. Check power/ground to the actuator before condemning the ECU.
- Grade: [C]
- Evidence: priuschat.com Techstream diagnostic report; scribd.com Toyota DTC guide

## C1331
- Description: ABS Controller Wiring Fault (Front Left Wheel)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: damaged wiring to the front-left wheel ABS sensor; insulation damage
- Diagnostic notes: Check the sensor harness for chafing along its routing.
- Grade: [C]
- Evidence: scribd.com Toyota DTC fault-codes guide (single community source)

## C1336
- Description: Zero Point Calibration of Acceleration Sensor Undone
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: zero point calibration incomplete; ABS and traction actuator (skid control ECU)
- Diagnostic notes: Perform acceleration-sensor zero-point calibration with Techstream.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1340
- Description: Open Circuit in Center Differential Lock Signal
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: center differential lock signal circuit; transfer indicator
- Diagnostic notes: 4WD models (LX470/Land Cruiser). Set with the center diff lock ON.
- Grade: [C]
- Evidence: ih8mud.com forum (single owner Techstream readout)

## C1380
- Description: Stop Light Control Relay Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: stop light assembly; stop light switch circuit; STOP LP CTRL relay; ABS and traction actuator (skid control ECU)
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com)

## C1391
- Description: Abnormal Leak of Accumulator Pressure
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: accumulator; brake actuator internal leak
- Diagnostic notes: Seen on Prius ABS/VSC/TRAC Techstream reports.
- Grade: [C]
- Evidence: priuschat.com Techstream diagnostic report (single owner report)

---

## U1103
- Description: Lost Communication with Stop and Start Control Module
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: ECM; engine stop-and-start ECU; CAN communication system fault
- Diagnostic notes: Stored when there is no communication between the ECM and the engine stop-and-start ECU for 1.16+ seconds with the ignition on (1-trip logic). MIL does not come on. (Techstream may display the extended form U110387.)
- Grade: [B]
- Evidence: Toyota repair-manual excerpt via zatonevkredit.ru (U110387: detection condition, trouble areas, confirmation driving pattern)

## U1104
- Description: Lost Communication with Driving Support ECU
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: driving support ECU; millimeter-wave radar / camera sensors; CAN communication system
- Diagnostic notes: Pre-crash safety system: set on a communication malfunction between the collision-detection sensors/ECUs or the pre-crash control ECUs.
- Grade: [B]
- Evidence: Toyota pre-crash safety system DTC chart via zatonevkredit.ru

## U1110
- Description: Lost Communication with Intuitive Parking Assist Module
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: clearance warning ECU assembly; CAN communication system
- Diagnostic notes: Lexus parking-assist (clearance sonar) module. NOTE: U1110 is make-specific — on Dodge/RAM it has a different definition. Do not cross-apply.
- Grade: [B]
- Evidence: Toyota/Lexus repair-manual excerpts via zatonevkredit.ru (IPA/parking-assist DTC chart)

## U1118
- Description: Lost Communication with Rear Radar Sensor
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: rear radar sensor; CAN communication system
- Diagnostic notes: Pre-crash safety system family — see U1104.
- Grade: [B]
- Evidence: Toyota pre-crash safety system DTC chart via zatonevkredit.ru

## U1121
- Description: Lost Communication with Driver Monitor ECU
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: driver monitor ECU/camera; CAN communication system
- Diagnostic notes: Pre-crash safety system family — see U1104.
- Grade: [B]
- Evidence: Toyota pre-crash safety system DTC chart via zatonevkredit.ru

## U1124
- Description: Lost Communication with Right Headrest Control ECU
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: right headrest control ECU; CAN communication system
- Diagnostic notes: Pre-crash safety system family — see U1104.
- Grade: [B]
- Evidence: Toyota pre-crash safety system DTC chart via zatonevkredit.ru

## U1125
- Description: Lost Communication with Left Headrest Control ECU
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: left headrest control ECU; CAN communication system
- Diagnostic notes: Pre-crash safety system family — see U1104.
- Grade: [B]
- Evidence: Toyota pre-crash safety system DTC chart via zatonevkredit.ru

---

## Coverage notes

- P-code coverage is strongest for 1998-2008 gasoline models (the retrolib.info transcription plus 2001 Prius / 2004 Corolla / 2002 Lexus GS300 manual excerpts). Later-model P1xxx (e.g. P2xxx-adjacent Toyota extensions, direct-injection P11xx variants) were not verified in this pass [?].
- P1605 era conflict (Knock Control CPU vs Rough Idling) and P1121 model conflict (APP sensor vs Prius CHS water valve) are reported inline, not resolved.
- P1150 bank conflict (Bank 2 Sensor 1 vs Bank 1 Sensor 2) is reported inline; the service-manual convention (Bank 2 Sensor 1) is used.
- B-code coverage is thin: only 4 codes verified (B1181, B1207, B1660, B1901). The full Toyota SRS B1xxx range (occupant classification, side/curtain squibs) was not verified in this pass [?].
- C-code coverage centers on the brake-control/VSC chart plus Prius/LX470 field reports; C02xx hydro-booster and C14xx-C17xx ranges are partial [?].
- U-code coverage is limited to verified U11xx manufacturer codes; Toyota-specific U01xx/U02xx sub-definitions exist per system but overlap the generic U0xxx already in the database and were deliberately not duplicated.
- Diesel-specific Toyota DTCs (D-4D) were largely out of scope for the sources consulted [?].
- No seed/key or immobilizer-bypass material was sought or reproduced; immobilizer-adjacent codes (P1604) are documented at the DTC-description level only.
