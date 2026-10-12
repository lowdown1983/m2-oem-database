# Ford / Lincoln / Mercury — Manufacturer-Specific DTCs

Research for the M2 OEM vehicle database (v1.2 DTC expansion). Covers FORD-SPECIFIC
codes only — SAE J2012 generic codes (P0xxx etc.) are covered separately and are
NOT duplicated here.

Every DTC carries a quality grade: **A** = Ford service info / Motorcraft document ·
**B** = reputable DTC database or multi-source agreement · **C** = single
community/technician source. Conflicts are reported, not silently resolved.
"not documented" means no source in this pass gave causes/notes — nothing invented.

Research date: 2026-10-06.

## Sources

- Ford 2008 P/B/C/U DTC master list (autoequipment.com.au PDF, "Ford 2008
  P_B_C_U_codes.pdf") — comprehensive Ford DTC chart; descriptions mirror Ford
  PC/ED wording [B]
- "Ford OBD-II Trouble Codes" list (stdrivers.co.uk forum, Ford ST/RS community)
  — matches the 2008 chart on overlapping codes [B where they agree]
- Ford 2004 OBD System Operation Summary (motorcraftservice.com, obdsm972.pdf),
  quoted via explorerforum.com — ERFS/FPDM diagnostic mechanism [A, via quote]
- JustAnswer Ford specialists (Ron Z., 18+ yr Ford diagnostics; Tom, ASE Master)
  — possible-cause lists for P1151, P1450, P1443, P1288 [C]
- explorerforum.com / screamandfly.com technician threads — P1744 TCC diagnosis,
  P1233 field experience [C]
- fordownersclub.com — U1900 cluster solder-joint quirk (Focus Mk2) [C]
- scribd "Ford-Error-Codes" / "Ford Diagnostic Codes and Procedures" docs —
  older SCP-era B-codes (B1202/B1204/B1317/B1318/B1342/U1262/U2196-U2201) [C]

## Ford DTC quirks (read before diagnosing)

1. **Three DTC classes: KOEO / KOER / Continuous Memory.** Ford's On-Demand
   self-tests are Key On Engine Off (KOEO) and Key On Engine Running (KOER);
   faults detected during normal driving are stored as Continuous Memory codes.
   A scan tool retrieves all three. Service continuous-memory codes LAST —
   after KOEO and KOER pass (EEC-IV/V heritage, still true on OBD-II Fords) [B —
   explorerforum KOEO procedure thread; yumpu Ford-testing doc].
2. **"Out of Self-Test Range" codes are test artifacts, not hard faults.**
   P1116 (ECT), P1124 (TP), P1288 (CHT), P1703 (brake switch), P1705/P1709
   (TR/PNP), P1780 (O/D cancel) and similar set when the sensor read out of the
   expected window DURING the self-test. A P1288 after disconnecting the MAF,
   for example, is a test artifact of the disturbed test conditions [B — code
   list wording; C — justanswer field case].
3. **P1000 cannot be cleared with a scan tool.** It sets after KAM clear /
   battery disconnect and self-clears only when all OBD-II monitors complete
   their drive cycles [B — 2carpros Ford tech].
4. **SCP era vs CAN era.** Pre-~2004 Fords speak SCP (J1850 PWM); their network
   faults are U12xx "SCP (J1850) Communications Bus Fault" codes. CAN-era
   vehicles use U01xx/U02xx "Lost Communication" codes instead. U1900 (SCP bus
   fault) on a Focus Mk2-era cluster is a known solder-joint failure inside the
   instrument cluster — both CAN buses route through it [C — fordownersclub].
5. **PATS codes are status, not circuit faults.** P1260 (theft detected — engine
   disabled), P1269 (immobilizer code not programmed), U1451 (anti-theft status
   signal missing) describe the passive anti-theft system STATE. Diagnose via
   PATS PIDs/key count, not by chasing a circuit [B/C — inferred from code
   semantics; flagged as inference].
6. **"System Pass" exists as a code.** P1111 = System Pass (all-clear from the
   self-test) [B — 2008 chart].

---

## P-codes (Ford-specific)

## P1000
- Description: OBD-II Monitor Testing Incomplete
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: battery disconnected, KAM cleared, DTCs cleared with scan tool
- Diagnostic notes: Cannot be cleared with a scan tool — self-clears after a full
  OBD-II drive cycle completes all monitors. If it will not clear, a monitor is
  not running (check enable criteria, e.g. fuel level, ambient temp).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; 2carpros Ford tech thread

## P1001
- Description: KOER Test Cannot Be Completed
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: test aborted (see also P127A/P127B aborted-KOER codes)
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: stdrivers Ford OBD-II code list; 2008 Ford DTC chart

## P1100
- Description: Mass Air Flow Sensor Circuit Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1101
- Description: Mass Air Flow Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: dirty/faulty MAF sensor, air intake leak
- Diagnostic notes: KOEO self-test artifact class — the MAF reading was outside
  the expected window when the test ran. Cleaning the MAF sensing wire is the
  common first step (Ford-tech community practice).
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; justanswer field case

## P1116
- Description: Engine Coolant Temperature Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: engine not at expected temperature during test, ECT sensor fault
- Diagnostic notes: Self-test-range class — run the test on a fully warmed engine.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1117
- Description: Engine Coolant Temperature Sensor Circuit Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1120
- Description: Throttle Position Sensor Out of Range (RATCH too low)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Throttle Position Sensor out of range")

## P1121
- Description: Throttle Position Sensor Inconsistent with MAF / MAP Sensor
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Rationality check between TP and airflow — check both sensors,
  not just the TP.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1124
- Description: Throttle Position Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1125
- Description: Throttle Position Sensor Circuit Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1127
- Description: Exhaust Not Warm Enough, Downstream HO2S Not Tested
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: short KOER run, exhaust not at operating temperature
- Diagnostic notes: KOER quirk — the downstream O2 monitor is skipped when the
  exhaust is cold; not a sensor fault.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1130
- Description: Lack of HO2S11 Switches — Fuel Trim at Limit (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: same family as P1131 (lean-side causes) driven to the fuel-trim limit
- Diagnostic notes: The O2 sensor has hit its compensation limit — it is reporting
  the mixture condition, not necessarily failed itself.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1131
- Description: Lack of HO2S11 Switch — Sensor Indicates Lean (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: air intake leak after the MAF, vacuum/PCV hose leaks, base engine
  mechanical fault (compression, valve timing), HO2S circuit (wet/oily/corroded
  terminals), low fuel pressure or ran out of fuel
- Diagnostic notes: Classic Ford lean code — usually NOT the sensor itself; the
  sensor is correctly reporting a lean condition caused upstream. Check fuel trims.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart (description); JustAnswer Ford tech possible-cause list

## P1132
- Description: Lack of HO2S11 Switch — Sensor Indicates Rich (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Mirror of P1131 for the rich side.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1137
- Description: Lack of HO2S12 Switch — Sensor Indicates Lean (Bank 1, downstream)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1138
- Description: Lack of HO2S12 Switch — Sensor Indicates Rich (Bank 1, downstream)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1150
- Description: Lack of HO2S21 Switches — Adaptive Fuel at Limit (Bank 2)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: bank-2 equivalents of the P1130 family
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1151
- Description: Lack of HO2S21 Switch — Sensor Indicates Lean (Bank 2)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: air intake system leaking, vacuum hoses leaking/damaged, air
  leaks after the MAF or in the PCV system, base engine mechanical fault, HO2S
  circuits wet/oily/corroded or poor terminal contact, HO2S signal circuit
  open/shorted, low fuel pressure or vehicle driven out of fuel
- Diagnostic notes: Same as P1131, opposite bank. Ford-tech guidance: these codes
  typically do NOT point to the O2 sensor itself — the sensor is compensating for
  an excessively lean mixture; check base idle, EGR, fuel and air-induction systems.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; JustAnswer (Tom, ASE Master; Ron Z., Ford
  diagnostics specialist)

## P1152
- Description: Lack of HO2S21 Switch — Sensor Indicates Rich (Bank 2)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Mirror of P1131 for bank 2 rich side.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1157
- Description: Lack of HO2S22 Switch — Sensor Indicates Lean (Bank 2, downstream)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1158
- Description: Lack of HO2S22 Switch — Sensor Indicates Rich (Bank 2, downstream)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P115A
- Description: Low Fuel Level — Forced Limited Power
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: fuel level genuinely low
- Diagnostic notes: Strategy code, not a circuit fault — the PCM limits power to
  protect the fuel pump. Refuel and clear.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc

## P115B
- Description: Low Fuel Level — Forced Engine Shutdown
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: fuel level critically low
- Diagnostic notes: Strategy code — PCM shuts the engine down to protect the pump.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc

## P1220
- Description: Series Throttle Control System Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1224
- Description: Throttle Position Sensor B Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class (TP sensor B).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1230
- Description: Fuel Pump Low Speed Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Open Power to Fuel Pump circuit" — wording differs, same circuit)

## P1231
- Description: Fuel Pump Secondary Circuit Low / High Speed
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1232
- Description: Fuel Pump Speed Primary Circuit Fault (two-speed fuel pump)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1233
- Description: Fuel Pump Driver Module Off-Line
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: FPDM lost power, tripped inertia fuel shutoff switch, failed
  Fuel Pump Driver Module, fuel rail pressure sensor fault
- Diagnostic notes: Per the Ford 2004 OBD System Operation Summary: Electronic
  Returnless Fuel Systems use the FPDM to control fuel pressure; the PCM outputs
  a 5–51% duty cycle and the FPDM runs the pump at twice that; the FPDM returns a
  duty-cycled diagnostic signal on the Fuel Pump Monitor circuit. If the FPDM
  outputs no diagnostic signal (0 or 100% duty cycle), the PCM sets P1233. Check
  FPDM power/ground and the inertia switch first — the pump will still build some
  pressure with a tripped switch on some models, so do not rule it out by cranking.
- Grade: [A] mechanism; [B] description; [C] field causes
- Evidence: Ford 2004 OBD System Operation Summary (motorcraftservice.com,
  quoted via explorerforum.com); 2008 Ford DTC chart; stdrivers list agrees

## P1234
- Description: Fuel Pump Driver Module Off-Line
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Same description as P1233 in Ford's chart (duplicate code —
  both listed).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1235
- Description: Fuel Pump Control Out of Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1236
- Description: Fuel Pump Control Out of Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1237
- Description: Fuel Pump Secondary Circuit Fault (Fuel Pump Driver Module)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1238
- Description: Fuel Pump Primary Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1244
- Description: Generator Load Input High
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1245
- Description: Generator Load Input Low
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1246
- Description: Generator Load Input Circuit Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Alternator Load Input Failed")

## P1247
- Description: Turbo Boost Pressure Low
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1248
- Description: Turbo Boost Pressure Not Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1249
- Description: Wastegate Control Valve Performance
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1250
- Description: Lack of Power to FPRC Solenoid (Fuel Pressure Regulator Control)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — the 2008 Ford chart phrases it "SOLENOID (PRC) —
  Open Or Short"; the stdrivers Ford OBD-II list phrases it "Lack of Power to
  FPRC Solenoid". Same PRC solenoid circuit, different wording; reported, not
  reconciled.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list (wording differs)

## P1260
- Description: Theft Detected — Engine Disabled
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented (PATS state, not a circuit fault)
- Diagnostic notes: PATS status code — the passive anti-theft system disabled the
  engine. Check PATS PIDs: number of programmed keys (B1213 sets when below
  minimum), key/PATS transceiver status. Do not chase as a circuit fault.
- Grade: [B] description; [C] diagnostic guidance (inference from code semantics)
- Evidence: 2008 Ford DTC chart ("Engine disabled by PATS"); stdrivers list agrees

## P1261
- Description: Cylinder #1 High to Low Side Short (injector)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1261–P1268 cover cylinders 1–8 high-to-low side injector
  shorts; P1271–P1278 repeat the same set (duplicate range in Ford's chart).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; scribd Code-Description doc (P1261–P1268 injector shorts)

## P1269
- Description: Immobilizer Code Not Programmed
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: PATS key/PATS module not programmed to the PCM
- Diagnostic notes: Program keys with a PATS-capable tool; check B1213 (key count
  below minimum).
- Grade: [B] description; [C] notes
- Evidence: scribd Code-Description doc; 2008 Ford DTC chart

## P1270
- Description: Engine RPM or Vehicle Speed Limiter Reached
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented (strategy/event code)
- Diagnostic notes: Informational — set when the limiter intervened, not a fault.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1285
- Description: Cylinder Head Overtemperature Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Precursor to P1299 fail-safe cooling.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1288
- Description: Cylinder Head Temperature Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: faulty CHT sensor (most common per field reports), actual
  overheating / low coolant, CHT wiring damage
- Diagnostic notes: Self-test-range class — but ALSO sets for genuine overheat
  signal issues. One field case: P1288 appeared after disconnecting the MAF during
  diagnosis (test artifact); with P1299 present, treat as real overheat strategy.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer (EricFromCT, Ford
  Senior Master tech)

## P1289
- Description: Cylinder Head Temperature Sensor Signal Greater Than Self-Test Range (high input)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1290
- Description: Cylinder Head Temperature Sensor Signal Less Than Self-Test Range (low input)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1299
- Description: Cylinder Head Temperature Sensor Detected Engine Overheating Condition (fail-safe cooling active)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: genuine overheating (low coolant, thermostat, water pump),
  faulty CHT sensor
- Diagnostic notes: Fail-safe cooling strategy — the PCM alternately disables fuel
  injectors to air-cool the engine; vehicle enters limp-home mode. Verify actual
  coolant level/temperature before condemning the sensor.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer Ford tech thread

## P1309
- Description: Misfire Detection Monitor Not Enabled
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1351
- Description: Ignition Diagnostic Monitor (IDM) Circuit Input Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1351–P1364 cover IDM and ignition coil primary/secondary
  circuit faults (coils A–D individually: P1352–P1355 primary).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1356
- Description: Loss of Ignition Diagnostic Module Input to PCM (PIP signal present while IDM indicates engine not turning)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1359
- Description: Spark Output (SAW) Circuit Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1380
- Description: Variable Cam Timing Solenoid Circuit Fault (short or open)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1380–P1388 cover VCT solenoid circuits and over-advanced /
  over-retarded cam timing (banks A/B).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1381
- Description: Variable Cam Timing Over-Advanced (Bank A)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Cam Timing Advance is excessive")

## P1383
- Description: Variable Cam Timing Over-Retarded (Bank A)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Cam Timing Advance is excessive" — wording approximate)

## P1390
- Description: Octane Adjust Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Relates to Ford's octane-adjust feature (2008 chart notes the
  vehicle may be adjusted to run on 91-octane fuel).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1400
- Description: DPFE Sensor Circuit Low Voltage Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: DPFE sensor fault, DPFE hose faults, wiring
- Diagnostic notes: The DPFE (Differential Pressure Feedback EGR) sensor and its
  hoses are Ford's classic EGR failure point. P1400–P1409 cover the DPFE/EVR
  circuit family.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1401
- Description: DPFE Sensor Circuit High Voltage Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: DPFE sensor fault, wiring
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1403
- Description: DPFE Sensor Hoses Reversed
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: hoses swapped during service
- Diagnostic notes: Check the upstream/downstream hose routing at the DPFE sensor
  and orifice tube.
- Grade: [B] description; [C] notes
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1405
- Description: DPFE Sensor Upstream Hose — Plugged or Open
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1406
- Description: DPFE Sensor Downstream Hose Off or Plugged
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1407
- Description: EGR No Flow Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: EGR valve stuck closed, restricted flow path, DPFE fault
- Diagnostic notes: not documented
- Grade: [B] description; [C] causes (inference from code semantics — flagged)
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1408
- Description: EGR Flow Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class for EGR flow.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1409
- Description: EGR Vacuum Regulator (EVR) Circuit Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — the stdrivers Ford OBD-II list shows P1409 twice
  with two wordings ("EGR Vacuum Regulator circuit malfunction" / "Electronic
  Vacuum Regulator Control circuit fault", both marked uncertain with "?"). The
  2008 chart settles on "EVR circuit fault". Reported, not reconciled.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list (dual uncertain wording)

## P1411
- Description: Secondary Air Injection — Incorrect Downstream Flow Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Secondary Air is not being diverted")

## P1413
- Description: Secondary Air Injection System Monitor Circuit Low Voltage
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1414
- Description: Secondary Air Injection System Monitor Circuit High Voltage
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1442
- Description: Secondary Air Injection System Monitor Circuit High Voltage
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — generic OBD-II references assign P1442 to EVAP
  small-leak on some makes; Ford's 2008 chart places P1442 in the secondary-air
  monitor family (same description as P1414). Use the Ford-specific meaning on
  Ford vehicles.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1443
- Description: EVAP Purge Control Solenoid / Purge Control Valve Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: faulty canister purge flow sensor / purge solenoid, carbon-clogged
  solenoid, vacuum leaks in EVAP plumbing
- Diagnostic notes: Classic Ford EVAP code (1990s–2000s). On older models the
  purge flow sensor at the top-center front of the engine is the common fix; often
  appears with P0401/P1444. Smoke-test the EVAP plumbing if the solenoid tests OK.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer (Ron, Ford drivability
  specialist); explorerforum Ranger thread

## P1444
- Description: EVAP Purge Flow Sensor Circuit Low Input
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Purge Flow Sensor circuit Input Low")

## P1445
- Description: EVAP Purge Flow Sensor Circuit High Input
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1450
- Description: Unable to Bleed Up Fuel Tank Vacuum (EVAP)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: stuck-open canister purge valve/solenoid (most common),
  restricted canister, plugged vent-valve filter, EVAP tube blockage, faulty fuel
  tank pressure sensor, capless filler-pipe fault
- Diagnostic notes: The stuck-open purge valve classically causes hard starting
  right AFTER refueling (fuel vapor floods the intake). Updated purge solenoid
  part released for affected models (e.g. Escape CV6Z-9D289-R per Ford tech).
  Smoke-test if no visible fault.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer (Ron Z., Ford
  diagnostics; DTC chart posted for 2015 Focus)

## P1451
- Description: EVAP Control System Canister Vent Solenoid Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1452
- Description: Unable to Bleed Up Fuel Tank Vacuum (EVAP)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Same description as P1450 in Ford's chart.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1455
- Description: EVAP System — Substantial Leak or Blockage Detected (gross leak / no flow)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1460
- Description: Wide Open Throttle A/C Cutoff (WAC) Circuit Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1461
- Description: A/C Pressure Sensor Circuit Low Input
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1462
- Description: A/C Pressure Sensor Circuit High Input
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1463
- Description: A/C Pressure Sensor — Insufficient Pressure Change
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1464
- Description: A/C Switch On During Self-Test
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: operator left A/C on during KOEO/KOER
- Diagnostic notes: Test-procedure artifact — switch the A/C off and rerun the
  self-test.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("ACCS to PCM High During Self-Test")

## P1469
- Description: Low Air Conditioning Cycling Period
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1473
- Description: Fan Secondary Monitor Circuit High with Fans Off
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1473–P1484 cover the cooling-fan primary/secondary monitor
  and relay circuits.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1474
- Description: Low Fan Control Primary Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1479
- Description: High Fan Control Primary Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1480
- Description: Fan Secondary Monitor Circuit Low with Low Fan On
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1481
- Description: Fan Secondary Monitor Circuit Low with High Fan On
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1500
- Description: Vehicle Speed Sensor Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1500–P1503 cover VSS intermittent/malfunction variants.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1504
- Description: Idle Air Control Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1504–P1509 cover IAC circuit/adaptive-clip/over/under-speed faults.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1506
- Description: Idle Air Control Over-Speed Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1507
- Description: Idle Air Control Under-Speed Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1512
- Description: Intake Manifold Runner Control Stuck Closed (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1512–P1520/P1537/P1538 cover the IMRC stuck-open/closed and
  circuit faults (also P2004–P2008 in the P2xxx range).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1518
- Description: Intake Manifold Runner Control Stuck Open (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1520
- Description: Intake Manifold Runner Control Circuit Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1530
- Description: A/C System Fault (A/C clutch circuit open or short)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Open or Short to A/C Compressor Clutch circuit")

## P1537
- Description: Intake Manifold Runner Control Stuck Open (Bank 1)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1538
- Description: Intake Manifold Runner Control Stuck Open (Bank 2)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1550
- Description: Power Steering Pressure Sensor/Switch Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class — cycle the steering during KOER (part
  of the standard KOER steering-input sequence).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1600
- Description: Loss of KAM (Keep Alive Memory) Power
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: battery disconnected, KAM fuse open, PCM power interruption
- Diagnostic notes: Expected after any battery disconnect — clear and retest.
  Persistent P1600 points to the KAM power circuit (see also P1633).
- Grade: [B] description; [C] notes
- Evidence: 2008 Ford DTC chart

## P1602
- Description: Immobilizer Module – PCM Communication Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: PATS network fault class — see also U-codes (U1262 SCP).
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1605
- Description: PCM Keep Alive Memory Test Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1610
- Description: PCM Reprogramming Error / Immobilizer Code Words Do Not Match
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: interrupted module programming, PATS code-word mismatch
- Diagnostic notes: P1610–P1624 cover PCM/PATS reprogramming errors and
  immobilizer code-word/ID mismatches. Reprogram with a PATS-capable tool.
- Grade: [B] description; [C] notes
- Evidence: 2008 Ford DTC chart

## P1625
- Description: Voltage to Vehicle Load Control Module Fan Circuit Not Detected
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1632
- Description: Smart Alternator Fault (sensor/circuit)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: smart-charge alternator circuit fault, wiring
- Diagnostic notes: not documented
- Grade: [B] description; [C] causes (fordownersclub field thread)
- Evidence: 2008 Ford DTC chart; fordownersclub Focus thread

## P1633
- Description: Power Supply to the KAM Fuse (KAPWR circuit)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: KAM fuse open, KAPWR circuit fault
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1635
- Description: Tire / Axle Out of Acceptable Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: incorrect tire size or axle ratio vs PCM calibration
- Diagnostic notes: Sets when the measured tire/axle combination disagrees with
  the PCM's programmed ratio — common after gear swaps or oversized tires without
  recalibration.
- Grade: [B] description; [C] notes (inference from code semantics — flagged)
- Evidence: 2008 Ford DTC chart

## P1639
- Description: PCM Vehicle Identification Block Corrupted or Not Programmed
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: module replacement without programming, corrupted flash
- Diagnostic notes: Program/reprogram the PCM with As-Built data.
- Grade: [B] description; [C] notes (inference — flagged)
- Evidence: 2008 Ford DTC chart

## P1640
- Description: Powertrain DTCs Available in Another Control Module
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Pointer code — query the other powertrain module (e.g. TCM)
  for the actual fault.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1650
- Description: Power Steering Pressure Switch Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class (see P1550).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1651
- Description: Power Steering Pressure Switch Input Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1700
- Description: Transmission Failed to Engage Neutral / Transmission Control System Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: internal transmission fault, TCM fault/communication
- Diagnostic notes: Generic transmission pointer on older Fords — often accompanied
  by a flashing O/D light. Retrieve transmission-specific codes; on 2008-chart
  wording it is the neutral-engagement failure.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer (john/eauto, ASE trans tech)

## P1701
- Description: Reverse Engagement Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1702
- Description: Transmission Range Sensor Circuit Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1703
- Description: Brake Switch Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: faulty brake switch signal, water/corrosion damage to switch or wiring
- Diagnostic notes: Self-test-range class — the BOO (brake on/off) input must
  change state during KOEO/KOER. One field case (2013 F-150) traced it to flood
  corrosion at the brake switch connector.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list ("Brake On/Off Switch out of Self-Test Range"); JustAnswer field case

## P1704
- Description: Digital Transmission Range Sensor Failed to Transition State
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1705
- Description: Manual Lever Position / Transmission Range Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1709
- Description: Park/Neutral Position Switch Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1711
- Description: Transmission Fluid Temperature Sensor Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1728
- Description: Transmission Slip Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1729
- Description: 4x4 Low Switch Error / Circuit Malfunction
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1740
- Description: Torque Converter Clutch System — Performance or Mechanically Stuck Off
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: TCC solenoid electrical fault or contamination, low/dirty
  transmission fluid, wiring/connector corrosion
- Diagnostic notes: TCC slip is evaluated functionally under steady-state lockup.
  Check fluid level/condition first; clean/replace the TCC solenoid; verify harness.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; JustAnswer (2008 F-150 P1740/P1744 case)

## P1741
- Description: Torque Converter Clutch Control Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1742
- Description: Torque Converter Clutch Solenoid Failed On
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Companion to P1743 (both listed as "failed on" in Ford's chart).
  If no slip is detected with the TCC commanded OFF, the TCC DTC for stuck-on
  engagement sets (per Ford OBD System Operation Summary description).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1743
- Description: Torque Converter Clutch Solenoid Failed On
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1744
- Description: Torque Converter Clutch System Stuck in Off Position (performance)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: low transmission fluid, contaminated fluid, damaged/malfunctioning
  TCC solenoid valve, failed torque converter (excessive TCC slippage)
- Diagnostic notes: The TCC solenoid is checked functionally: if converter slip
  exceeds the malfunction threshold while the TCC is commanded ON, P1744 stores
  (Ford OBD System Operation Summary, via motorcraftservice.com). If the solenoid
  tests good per pinpoint tests, converter replacement is the most likely repair
  (Ford-tech field guidance). Symptoms: MIL, transmission overheating, poor fuel
  economy, hard/late shifts; cycling the key may temporarily clear symptoms.
- Grade: [B] description; [B] mechanism (Ford OBD summary quote); [C] field repair guidance
- Evidence: 2008 Ford DTC chart; stdrivers list; explorerforum (Drew quoting
  motorcraftservice obdsm972.pdf); screamandfly Ford-tech thread; youtube DTC summary

## P1746
- Description: Electronic Pressure Control Solenoid — Open Circuit
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1746–P1749/P1760 cover EPC solenoid open/short/failed-low faults.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1747
- Description: Electronic Pressure Control Solenoid — Short Circuit
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1749
- Description: Electronic Pressure Control Solenoid Failed Low
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1751
- Description: Shift Solenoid #1 Performance / Functional Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1754
- Description: Coast Clutch Solenoid Circuit Malfunction / Electrical Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1756
- Description: Shift Solenoid #2 Performance / Functional Fault
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1760
- Description: Electronic Pressure Control Solenoid Short Circuit
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1762
- Description: Overdrive Band Failed Off
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1780
- Description: Transmission Control Switch / Overdrive Cancel Circuit Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: misaligned/faulty transmission range sensor (TRS), O/D cancel
  switch or wiring fault, connector corrosion
- Diagnostic notes: Self-test-range class. Inspect the TRS on the transmission
  housing; cleaning the sensor/connector can help; proper alignment on
  installation is critical. Often paired with P1703 (brake switch) after
  water damage.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; stdrivers list; JustAnswer (2013 F-150 and 2011
  Transit Connect cases)

## P1781
- Description: 4x4 Low Switch Out of Self-Test Range
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Self-test-range class.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1783
- Description: Transmission Over-Temperature Condition
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1784
- Description: Transmission Mechanical Failure — First and Reverse
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Internal mechanical fault class (P1784–P1787).
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1785
- Description: Transmission Mechanical Failure — First and Second
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1786
- Description: 3-2 Downshift Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1787
- Description: 2-1 Downshift Error
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1788
- Description: Coast Clutch Solenoid Open Circuit
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1789
- Description: Coast Clutch Solenoid Short Circuit
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list agrees

## P1800
- Description: Transmission Clutch Interlock Safety Switch Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1800–P1803 cover the clutch-interlock safety switch circuits
  (manual-transmission starter interlock).
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1804
- Description: Four Wheel Drive High Indicator Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1804–P1899 cover the 4WD transfer-case family: high/low
  indicators, mode-select circuits, contact plates A–D, shift motor, differential
  lockup, axle-disconnect solenoids/sensors.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1812
- Description: Four Wheel Drive Mode Select Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1828
- Description: Transmission Transfer Case High-to-Low Shift Relay Coil Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1838
- Description: Transmission Transfer Case Shift Motor Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1867
- Description: Transmission Transfer Case Contact Plate General Circuit Failure
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Representative of the P1846–P1865 contact-plate A–D circuit family.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1900
- Description: Output Shaft Speed Sensor Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; stdrivers list ("Transmission system problems" — generic wording)

## P1901
- Description: Turbine Shaft Speed Sensor Intermittent
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1A00
- Description: Transmission Generator Brake Failure (hybrid)
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: P1A00–P1A15 are Ford hybrid (Escape Hybrid eCVT) codes:
  generator/motor/inverter shutdown circuits, hybrid battery power limits,
  immediate-shutdown signals.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## P1A0C
- Description: Hybrid Powertrain Control Module — Engine Disabled
- Category: P
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

---

## U-codes (Ford network)

## U0100
- Description: Lost Communication with ECM / PCM
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: CAN wiring fault, PCM power/ground fault, failed PCM, gateway fault
- Diagnostic notes: The foundational CAN-era network code. When multiple U-codes
  set simultaneously, inspect shared CAN wiring, connectors, and power/grounds
  before condemning any single module.
- Grade: [B] description; [C] notes (Toyota service-manual tech-tip pattern, applied to Ford — flagged as cross-make guidance)
- Evidence: 2008 Ford DTC chart

## U0101
- Description: Lost Communication with TCM
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U0121
- Description: Lost Communication with ABS Control Module
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U0140
- Description: Lost Communication with BCM
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U0155
- Description: Lost Communication with Instrument Panel Cluster (IPC) Control Module
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U1262
- Description: SCP (J1850) Data Link Fault / Communication Bus Fault
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: SCP-era (pre-CAN) Ford network fault — the J1850 PWM bus
  itself is faulted, as distinct from U12xx "missing message" codes. On CAN-era
  vehicles, look at U01xx/U02xx instead.
- Grade: [B] description; [C] notes (era distinction — inference, flagged)
- Evidence: 2008 Ford DTC chart ("SCP Data Link Fault"); scribd Ford-Error-Codes
  doc ("Communication bus fault (missing CAN messages)" for D262/U1262)

## U1451
- Description: Anti-Theft Status Signal Missing — Engine Disabled
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: PATS network status code — companion to P1260.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U1900
- Description: SCP (J1850) Communication Bus Fault
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: instrument-cluster solder-joint failure (Focus Mk2-era),
  CAN/SCP wiring fault
- Diagnostic notes: Field quirk (Focus Mk2): both communication buses route
  through the instrument cluster; cold solder joints inside the cluster set U1900
  plus a spray of spurious U-codes in other modules. Tapping the dash above the
  cluster with the engine running can make the fault come and go — cluster
  re-soldering is the documented fix.
- Grade: [B] description; [C] quirk
- Evidence: 2008 Ford DTC chart; fordownersclub.com Focus Mk2 thread

## U2012
- Description: CAN Communication Bus Fault (missing messages)
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; fordownersclub FORScan capture (Focus Mk2 ABS module)

## U2023
- Description: Fault Received from External Node
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## U3000
- Description: Control Module (general module fault)
- Category: U
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Generic module-fault pointer; U3001–U3011 refine it (improper
  shutdown, VIN, battery voltage, ignition inputs, grounds).
- Grade: [B]
- Evidence: 2008 Ford DTC chart

---

## B-codes (Ford body)

## B1202
- Description: Fuel Pump and Sender Unit / Fuel Level Sensor Open Circuit
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: SCP-era body code (reported as 9202 in the older hex listing).
- Grade: [C]
- Evidence: scribd Ford-Error-Codes doc

## B1204
- Description: Fuel Pump and Sender Unit / Fuel Level Sensor Short to Ground
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd Ford-Error-Codes doc

## B1213
- Description: Anti-Theft Number of Programmed Keys Is Below Minimum
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: keys erased, PATS module replaced without key programming
- Diagnostic notes: Companion to P1260/P1269 — program the minimum key count with
  a PATS-capable tool.
- Grade: [B] description; [C] notes
- Evidence: 2008 Ford DTC chart

## B1231
- Description: Crash Detected
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: actual collision event, RCM fault, battery disconnect with
  damaged sensors/airbags
- Diagnostic notes: Set by the restraints control module on crash input; can also
  appear spuriously after battery disconnects on damaged SRS hardware.
- Grade: [C]
- Evidence: scribd FORD Fault-Codes DTC manual

## B1317
- Description: Battery Voltage High (greater than ~16V)
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: overcharging alternator, voltage regulator fault
- Diagnostic notes: not documented
- Grade: [B] description; [C] causes (explorerforum field thread)
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc; explorerforum B1318 thread

## B1318
- Description: Battery Voltage Low (less than ~10V)
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: discharged/failed battery (lost cell, low electrolyte), faulty
  alternator, fusible-link/wiring fault in the charge circuit
- Diagnostic notes: Extremely common "ghost" code — low system voltage during
  cranking sets B1318 plus a spray of unrelated codes. Always verify battery
  health under LOAD (not just open-circuit voltage) and alternator output before
  chasing the other codes.
- Grade: [B] description; [C] causes
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc; explorerforum B1318
  thread (multiple field cases)

## B1342
- Description: ECU Is Defective / ECU Internal Fault
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — the older scribd Ford-Error-Codes listing attaches
  B1342 to several unrelated items ("PCM is defective", "Odometer RESET button
  sticking", "Trip computer SET button sticking", "NVM memory failure"), suggesting
  B1342 is a catch-all module-internal fault on SCP-era Fords. The 2008 chart
  settles on "ECU internal fault". Reported, not reconciled.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc (multiple wordings)

## B1359
- Description: Ignition Run/Accessory Circuit Failure
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: B1351–B1366 cover the ignition key-in/run/start circuit family.
- Grade: [B]
- Evidence: 2008 Ford DTC chart; scribd Ford-Error-Codes doc

## B2477
- Description: Module Configuration Failure
- Category: B
- Scope: manufacturer (Ford)
- Possible causes: module replaced without As-Built configuration, corrupted config
- Diagnostic notes: Configure the module with Ford As-Built data (see also P1639
  for the PCM-side equivalent).
- Grade: [C] description; [C] notes (inference — flagged)
- Evidence: scribd Ford-Error-Codes doc ("A477 (B2477) Module configuration failure")

---

## C-codes (Ford chassis)

## C1100
- Description: ABS Pump Switch Circuit Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: C1100–C1115 cover the ABS pump/motor relay and power-relay circuits.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1145
- Description: Right Front Wheel Speed Sensor Input Circuit Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: C1145–C1237 is the wheel-speed-sensor family: input circuit
  failure, open/short to battery/ground, coherency faults, missing signal, tone-
  ring missing-tooth faults (C1139–C1144).
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1155
- Description: Left Front Wheel Speed Sensor Input Circuit Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1165
- Description: Right Rear Wheel Speed Sensor Input Circuit Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1175
- Description: Left Rear Wheel Speed Sensor Input Circuit Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1233
- Description: Left Front Wheel Speed Sensor Input Signal Missing
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: "Signal missing" subgroup (C1233–C1237, one per corner plus
  rear-center C1230).
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1284
- Description: Oil Pressure Switch Failure
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: 2008 Ford DTC chart; JustAnswer Ford DTC list thread

## C1414
- Description: Incorrect Module Design Level (fault PIDs may be available)
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: wrong module hardware/software level for the vehicle
- Diagnostic notes: Ford's note: additional fault PIDs may be available — check
  the datalogger/restraints PIDs for detail.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

## C1415
- Description: Incorrect Module Configuration
- Category: C
- Scope: manufacturer (Ford)
- Possible causes: not documented
- Diagnostic notes: Companion to B2477 — configure with As-Built data.
- Grade: [B]
- Evidence: 2008 Ford DTC chart

---

## Coverage notes

**Ranges NOT verified in this pass (systematic gaps):**
- P2xxx Ford-specific diesel/SCR codes (P2004–P2008 IMRC noted in P1512 entry but
  not individually listed; P20xx reductant/DPF family excluded — largely
  generic-SAE or Power Stroke diesel-specific, thin verification).
- P12xx/P13xx Power Stroke diesel codes beyond the ICP family mention
  (P1211/P1280–P1284 listed in the 2008 chart but not individually verified here).
- B-codes above B1444 (B15xx–B29xx: airbag, seating, lighting subfamilies) —
  not surveyed; only the commonly-seen B12xx/B13xx/B2477 are covered.
- C-codes above C1419 (C15xx–C19xx: steering/suspension subfamilies) — not surveyed.
- U-codes U03xx–U11xx (software incompatibility U0300–U0334 listed in the 2008
  chart but not individually covered) and U30xx beyond U3000–U3011.
- Model-year applicability: the 2008 chart is a master list across the Ford
  lineup — individual codes may not apply to every model/year. No per-model
  applicability matrix was verified.

**Conflicts reported (not resolved):**
- P1250: "Lack of Power to FPRC Solenoid" (stdrivers) vs "SOLENOID (PRC) — Open
  Or Short" (2008 chart).
- P1409: stdrivers lists it twice with two wordings, both marked uncertain;
  2008 chart says "EVR circuit fault".
- P1442: Ford-specific meaning (secondary-air monitor circuit high) vs generic
  references assigning it to EVAP small leak on other makes.
- B1342: "ECU internal fault" (2008 chart) vs multiple unrelated wordings
  (odometer reset button, NVM failure) in the older SCP-era listing.
- P1383: stdrivers wording ("Cam Timing Advance is excessive") vs 2008 chart
  ("Variable Cam Timing overretarded, bank B") — the 2008 chart is taken as
  authoritative.
- stdrivers listed "P1409?" with question marks and "P1519?/P1520?" IMRC
  variants — uncertain entries in that list were NOT carried into this file.

**Grading summary:** Descriptions are predominantly [B] (Ford 2008 master DTC
chart, cross-checked against the stdrivers Ford OBD-II list where they overlap).
The P1233 ERFS/FPDM mechanism is [A] (quoted from Ford's own 2004 OBD System
Operation Summary via motorcraftservice.com). Possible causes and diagnostic
notes are [C] unless noted — drawn from Ford-specialist technician Q&A and field
threads, and marked "not documented" wherever no source supported them. Nothing
was invented.
