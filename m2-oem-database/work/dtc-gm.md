# GM Manufacturer-Specific DTCs (Chevrolet / Buick / GMC / Cadillac)

Research for the M2 OEM vehicle database v1.2. Research date: 2026-10-06.

Grades: **A** = GM Service Information / TSB text · **B** = reputable DTC database or multi-source agreement · **C** = single community source.
Scope: GM includes Chevrolet, Buick, GMC, Cadillac (plus Pontiac/Saturn/Hummer/Saab where the code set applies).
Generic SAE J2012 P0xxx/B0xxx/C0xxx/U0xxx codes are NOT duplicated here (separate list covers them); U0xxx network codes below appear only where GM service bulletins add GM-specific diagnostic context.

## P-codes (powertrain)

## P1101
- Description: Intake Air Flow System Performance
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Vacuum/air leaks in intake tract; clogged PCV system or valve; dirty or faulty MAF sensor; restricted air filter; faulty/leaking charge-air (intercooler) tubes on turbo engines; faulty boost pressure or MAP sensor
- Diagnostic notes: GM SI (Document ID 3355356, 2018 Malibu 2.0L Turbo): "The ECM compares the actual air flow based on throttle position (TP) to a calculated airflow based on MAP sensor and MAF." Sets when actual airflow exceeds calculated. Review PIP5402D / 20-NA-047 for leak checks; verify boost and MAP sensors agree KOEO; MAF should read approx 3 g/s (2000-2500 Hz) at idle. Common on 1.4L LE2 / 1.5L LFV turbo engines.
- Grade: A
- Evidence: GM Service Information excerpt (SI Doc ID 3355356) via scribd archive

## P1174
- Description: Fuel Trim Cylinder Balance Bank 1
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Clogged fuel injectors (Multec 2 injectors, 2000-2008 models); vacuum leaks; aged O2 sensors; MAF issues
- Diagnostic notes: GM TSB 04-06-04-047G (US) / 05-06-04-022D (Canada): "Various Driveability Symptoms Due to Clogged Fuel Injectors" — MIL with P1174/P1175 (+ P0171/P0172/P0174/P0300) on 2000-2008 GM cars/light trucks. GM recommends testing with Active Fuel Injector Tester AFIT CH-47976. CONFLICT: an EOBD overview document lists P1174 as "Injection pump cam ring position sensor" — that reading belongs to the diesel (Duramax/Isuzu) context, not gasoline GM. Report both; use the TSB meaning on gasoline vehicles.
- Grade: B
- Evidence: GM TSB 04-06-04-047G via gmtnation forum archive; conflict from scribd EOBD overview doc

## P1175
- Description: Fuel Trim Cylinder Balance Bank 2
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Same as P1174 (clogged injectors, vacuum leaks, O2/MAF issues), bank 2
- Diagnostic notes: Covered by the same GM TSB 04-06-04-047G as P1174. Diagnose both banks together; a both-banks fault points to something common (intake leak, MAF, fuel pressure).
- Grade: B
- Evidence: GM TSB 04-06-04-047G via gmtnation forum archive

## P1258
- Description: Engine Coolant Overtemperature - Protection Mode Active
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Cooling system fault (thermostat, water pump, low coolant, cooling fans, restricted radiator); faulty ECT sensor (rule out P0116/P0117/P0118/P0128 first)
- Diagnostic notes: GM SI: Type A DTC. ECM monitors ECT; sets when coolant exceeds ~131-136 C for several seconds (threshold varies by model/calibration, e.g. 131 C for 7 s on Enclave LZ4/LY7, 136 C for 1 s or 10 s cumulative on CTS). Action: ECM alternately disables groups of cylinders (fuel injectors OFF) to cool the engine — "Overheated Engine Protection Operating Mode"; coolant lamp + DIC message. Diagnose the cooling system, not the code.
- Grade: A
- Evidence: GM Service Information excerpts (multiple models) via gm.saturn.team

## P1516
- Description: Throttle Actuator Control (TAC) Module Throttle Actuator Position Performance
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Carbon buildup on throttle plate/bore; faulty TAC module or throttle body; TAC motor wiring open/shorted; poor connector contact; high resistance in TP sensor circuits; ECM fault
- Diagnostic notes: GM-ONLY code (same number means different things on other makes). GM SI: sets when actual vs desired throttle position differs by more than 7.5% for 30 s (values vary by model). Type A DTC; ECM commands Reduced Engine Power mode and sets P2106/P2110. Clearing the code restores power only if it is the sole fault. Check throttle body for carbon/ice holding the blade open before replacing parts.
- Grade: A
- Evidence: GM Service Information (Pontiac G3 2009 / Impala 2007 DTC docs) via gm.saturn.team

## P1637
- Description: Generator L-Terminal Circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Loose or corroded connections at alternator or PCM; faulty voltage regulator; open/grounded L-terminal wire (generator will not operate if L wire is open or grounded); PCM fault
- Diagnostic notes: GM SI (1999 Corvette): the L (lamp) terminal enables generator operation after engine start and reports internal faults (regulator grounds L on internal fault). Scan tool: L terminal should read Inactive KOEO and Active with engine running. DTCs P1637 and P1638 may set together; the L-terminal circuit can cause P1638 to set. One diagnostic table covers both.
- Grade: A
- Evidence: GM Service Information diagnostic aids via gm.saturn.team; Corvette SI circuit description

## P1638
- Description: Generator F-Terminal Circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Faulty voltage regulator; open/shorted field winding; wiring fault on F-terminal circuit; wrong/clone alternator (field duty cycle out of range); PCM fault
- Diagnostic notes: GM SI: PCM monitors generator field duty cycle (PWM) on the F terminal — expects ~0% KOEO and 5-100% with engine running. Out-of-range PWM sets the code; PCM then sends a Class 2 message to illuminate "Charge System Fault" and may turn the alternator off. Scan tool: F terminal should read 10-40% KOEO, >5% running.
- Grade: A
- Evidence: GM Service Information via gm.saturn.team; CorvetteForum SI excerpts

## P1682
- Description: Ignition 1 Switch Circuit 2
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Bad relay or blown fuse (ECM/IGN circuits); faulty ignition switch; open/short in ignition-1 wiring; faulty underhood fuse block; ECM fault
- Diagnostic notes: GM SI circuit description: two ignition-1 voltage circuits feed the ECM (one via powertrain relay for TAC circuits, one via run/crank relay or ignition switch for remaining circuits). Code sets on a voltage difference between the two circuits (>~3 V reported on some models). Test B+ at both ECM ignition feeds (e.g. C1-19 on some models); swap relays and check fuses before condemning the ECM. Model-year variation exists in which relays feed the two circuits — verify against the model SI.
- Grade: B
- Evidence: GM SI circuit/system description via TahoeYukonForum; technician reports (JustAnswer)

## P1811
- Description: Maximum Adapt and Long Shift
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Pressure control solenoid failure; debris/wear in valve body (torque signal regulator valve or actuator feed limit valve sticking); worn/sticking line boost valve and sleeve; PCM/TCM calibration
- Diagnostic notes: Classic 4T65E code. GM SI: shift taking longer than 0.65 s with adapt at its limit increments a counter; counter = 2 in one trip sets the code (Type C — MIL does NOT light; harsh shifts are the symptom). When set, PCM commands maximum line pressure and disables adapts — the bang-shifting is the protection strategy, not the root fault. GM TSB 08-07-30-013 (2007 Terraza/Uplander/Montana SV6/Relay): FALSE P1811 — reprogram TCM with updated calibration (PN 24247599), do NOT replace TCM/valve body/solenoids for that concern. Watch TAP (Transaxle Adaptive Pressure) cells on a scan tool to find the slipping element.
- Grade: A
- Evidence: GM TSB 08-07-30-013; GM SI circuit description via badsol.net archive; trade-press teardown guides

## P1860
- Description: TCC PWM Solenoid Circuit Electrical
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Open or short in TCC PWM solenoid circuit; faulty TCC PWM solenoid valve; wiring harness fault; PCM fault
- Diagnostic notes: GM SI: PCM provides a ground path (circuit 418) for the TCC PWM solenoid that smooths TCC apply. Sets on continuous open/short detected via voltage feedback vs commanded duty cycle (command ON/voltage stays B+, or command OFF/voltage stays 0 V). Type varies by model/year (A, B, C, or D). Diagnostic cascade: P1860 can cause P1870 to set — always diagnose the electrical code first.
- Grade: A
- Evidence: GM Service Information via gm.saturn.team (multiple models)

## P1870
- Description: Transmission Component Slipping
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Worn TCC clutch; faulty TCC PWM solenoid (see P1860); sticking shift valves or contamination; TFP manual valve position switch malfunction (P1810); internal transmission failure; low/dirty fluid
- Diagnostic notes: GM SI: PCM computes TCC slip from engine speed vs transmission output speed; sets when slip is excessive (e.g. 200-1500 RPM for 8 s, 3 occurrences, on 1997 4T60-E; 90-500 RPM for 10 s on later trucks). Type B (MIL after 2 trips). Actions: inhibits TCC, commands max line pressure, inhibits 4th in hot mode, freezes adapts. Diagnostic aids: a TFP switch fault or shift-solenoid mechanical fault can set P1870; diagnose engine DTCs and electrical trans codes first.
- Grade: A
- Evidence: GM Service Information via gm.saturn.team (multiple models)

## P2176
- Description: Throttle Actuator Control System - Minimum Throttle Position Not Learned
- Category: P
- Scope: manufacturer (GM)
- Possible causes: Faulty TAC module/throttle body; TAC harness open/shorted or poor connection; throttle plate sticking from carbon buildup; ECM fault
- Diagnostic notes: GM SI: sets when both TP sensors read above 0.95 V during the minimum-learn procedure (learn runs once per ignition cycle). Type A; commands Reduced Engine Power and sets P2106/P2110. Diagnostic aid: high resistance in TP circuits, or the blade held open (ice in bore). After throttle body service, perform the idle/minimum-position learn procedure.
- Grade: B
- Evidence: GM SI conditions (Pontiac G3 2009 / Aveo 2009) via gm.saturn.team; carobdcodes.com

## P1E00
- Description: Hybrid/EV Powertrain Control Module Requested MIL Illumination (informational)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented (code is informational — the root fault is whatever is stored in the hybrid control module)
- Diagnostic notes: Seen on Chevrolet Volt / Malibu Eco alongside hybrid codes (e.g. P0AFA, P1AF0/P1AF2). Volt community reports these secured high-voltage DTCs cannot be cleared with a generic OBD-II reader; they require a dealer-level tool (GDS2) and in some cases HPCM2 reprogramming (SPS2). Always scan the hybrid/EV powertrain control module for the underlying codes rather than diagnosing P1E00 itself.
- Grade: C
- Evidence: Volt owner/technician community (vxdiagshop.com GDS2 guides; JustAnswer)

## Descriptor-only P1xxx entries (transcribed GM lists, 2 sources agree unless noted)

The codes below come from transcribed GM DTC descriptor lists. Descriptions are included; possible causes and diagnostic notes were not documented in the sources and are not invented.

## P1629
- Description: Anti-theft cranking signal error / Passkey cranking error
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1630
- Description: System voltage too high/too low, or ECM immobilizer learning mode (Cavalier and Monte Carlo only)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Immobilizer-learning usage is model-specific (Cavalier/Monte Carlo).
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1631
- Description: Anti-theft password incorrect (also listed as: Oxygen sensor #1 slow response on some models)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: CONFLICT between the two transcribed lists on this code (theft-deterrent vs O2 sensor) — reported, not resolved; verify per model.
- Grade: C
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc disagree)

## P1632
- Description: Anti-theft fuel disable signal received
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1633
- Description: Ignition power circuit low voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1634
- Description: Ignition power circuit low voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1635
- Description: 5 volt reference voltage to sensors low
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1639
- Description: PCM 5 volt reference voltage low
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1641
- Description: EVAP fuel tank pressure sensor circuit voltage high, or fan 1 relay control circuit, or MIL light circuit, or A/C compressor clutch relay circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Multi-use output-driver code; the meaning depends on model/year — verify per model SI.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1642
- Description: Fan control relay, or vehicle speed sensor output, or secondary air injection relay fault
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Multi-use output-driver code; verify per model SI.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1644
- Description: Throttle position sensor circuit, or traction control fault
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1645
- Description: Boost control solenoid circuit, or EVAP solenoid output circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1650
- Description: Quad driver module (QDM) 1 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1651
- Description: Quad driver module (QDM) 2 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1652
- Description: Quad driver module (QDM) 3 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1653
- Description: Quad driver module (QDM) 4 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1654
- Description: Quad driver module (QDM) 5 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1655
- Description: Quad driver module (QDM) 6 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1656
- Description: Driver 4 line 1
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1657
- Description: Driver 4 line 2
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1658
- Description: Driver 4 line 3
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1660
- Description: Driver 4 line 4
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1661
- Description: Driver 4 line 5
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1662
- Description: Driver 4 line 6
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1663
- Description: Driver 4 line 7
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1664
- Description: Skip shift 1-4 upshift lamp control circuit (also: oil lamp control circuit on Caprice/Fleetwood/Roadmaster)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1665
- Description: Driver 3 line 6 (also listed as: EVAP vent valve solenoid control circuit, 1998)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Year-dependent meaning — verify per model.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1666
- Description: Driver 3 line 6
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1667
- Description: Reverse inhibitor solenoid control circuit (1996-97) / fuel pump speed control circuit (1998)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Year-dependent meaning — verify per model.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1669
- Description: ABS unit expected
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1670
- Description: Quad driver module (QDM) 4 circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1671
- Description: MIL control circuit / oil change lamp control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1672
- Description: Low engine oil level lamp circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1673
- Description: Engine hot lamp control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1674
- Description: Tachometer control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1675
- Description: EVAP vent solenoid control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1676
- Description: EVAP canister purge solenoid control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1677
- Description: Powertrain control module fault (quad driver 4)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1680
- Description: Driver 5 (powertrain control module fault)
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1681
- Description: Driver 5 line 1
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1683
- Description: Driver 5 line 3
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1684
- Description: Driver 5 line 4
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1685
- Description: Driver 5 line 5
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1686
- Description: Driver 5 line 6
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1687
- Description: Driver 5 line 7
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1689
- Description: Traction control system delivered torque control circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Related to C0244 (PWM delivered torque) on the EBCM side.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc; Terraza SI master list)

## P1690
- Description: ECM loop overrun
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1691
- Description: Coolant gauge circuit low voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1692
- Description: Coolant gauge circuit high voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1693
- Description: Tachometer circuit low voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1694
- Description: Tachometer circuit high voltage
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1695
- Description: Remote keyless entry circuit low
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1696
- Description: Remote keyless entry circuit high
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1700
- Description: Malfunction indicator lamp requested by transmission control module
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented (informational — check TCM for underlying codes)
- Diagnostic notes: Informational; scan the TCM for the underlying fault.
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1701
- Description: Malfunction indicator lamp request circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1740
- Description: Torque control/management request circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1743
- Description: TP signal from ECM
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (GM.doc)

## P1760
- Description: Transmission control module supply voltage interrupted
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1779
- Description: Engine torque delivered to TCM signal
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1780
- Description: Park/neutral position switch circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1781
- Description: Engine torque signal circuit
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1790
- Description: Transmission control module checksum
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Internal TCM fault indicator — typically requires TCM replacement/reprogramming.
- Grade: B
- Evidence: Transcribed GM DTC lists (GM.doc)

## P1791
- Description: Transmission control module loop
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1792
- Description: ECM to transmission control module engine coolant signal
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1793
- Description: Transmission control module stack overrun
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Internal TCM fault indicator.
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1795
- Description: CAN bus - throttle body position
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1800
- Description: ECM to transmission control module engine coolant signal
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: Transcribed GM DTC lists (scribd GM-specific list; GM.doc)

## P1801
- Description: Performance selector switch failure
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1804
- Description: Ground control relay
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: GM.doc transcription (single source)

## P1810
- Description: ATF pressure manual valve position switch malfunction
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Per GM SI diagnostic aids for P1870, a TFP manual valve position switch malfunction can set P1870 — diagnose P1810 first when both appear.
- Grade: B
- Evidence: Transcribed GM DTC lists; GM SI P1870 diagnostic aids (gm.saturn.team)

## P1812
- Description: TOT (transmission oil temperature) condition
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: scribd GM-specific list (single source)

## P1814
- Description: Torque converter clutch (TCC) overstress
- Category: P
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: C
- Evidence: scribd GM-specific list (single source)

## U-codes (network)

Note: U0xxx codes are SAE-generic definitions; they are included here only where GM service bulletins add GM-specific diagnostic context. Pure generic definitions belong to the separate J2012 list.

## U0073
- Description: Control Module Communication Bus A Off
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: Backed-out terminals in the transmission 16-way electrical connector (GM-documented pattern failure); short between HS GMLAN (+) and (-); any HS GMLAN circuit shorted to ground or voltage; module internal fault shorting the bus; open in HS GMLAN circuits
- Diagnostic notes: GM bulletin (Cadillac XLR 2007 / Silverado 2008-2009, doc 2186567): intermittent no-crank, IPC gauge fluctuation, door-lock cycling, transmission no-shift with U0073/U0100/U0101/U0102/U0121/U0140 — cause was a terminal for the High Speed GMLAN serial data bus backed out of the transmission connector. "Do NOT replace BCM, ECM, EBCM, TCM, TCCM or wiring harness before checking terminals in transmission connector." HS GMLAN uses two 120-ohm terminators in parallel (BCM + ECM); 60 ohms across the bus is normal, ~120 ohms indicates an open.
- Grade: A
- Evidence: GM service bulletin 2186567; GM SI "Scan Tool Does Not Communicate With High Speed GMLAN Device"

## U0100
- Description: Lost Communication With ECM/PCM
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: Same GMLAN bus faults as U0073; blown fuse / dead OBD-II port power; bad ground; faulty ECM
- Diagnostic notes: Appears in the GM TSB set above (transmission-connector terminal pattern failure). Generic scanners often surface U0100 when the real fault is bus-wide — check the full U-code set before condemning the ECM.
- Grade: A
- Evidence: GM service bulletin 2186567

## U0101
- Description: Lost Communication With TCM
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: TCM not powering up (blown fuse, bad relay, wiring); GMLAN bus fault; faulty TCM
- Diagnostic notes: In the GM TSB set above. Diesel/truck community note: U2106-family symptoms (no PRNDL underline, harsh 3rd-gear limp) point to the TCM not powering up rather than a dead TCM.
- Grade: A
- Evidence: GM service bulletin 2186567

## U0102
- Description: Lost Communication With Transfer Case Control Module
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: GMLAN bus fault; transfer case control module power/ground fault
- Diagnostic notes: In the GM TSB set above.
- Grade: A
- Evidence: GM service bulletin 2186567

## U0121
- Description: Lost Communication With Anti-Lock Brake System (ABS) Control Module
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: GMLAN bus fault; EBCM power/ground fault
- Diagnostic notes: In the GM TSB set above.
- Grade: A
- Evidence: GM service bulletin 2186567

## U0140
- Description: Lost Communication With Body Control Module
- Category: U
- Scope: manufacturer context (GM)
- Possible causes: GMLAN bus fault; BCM power/ground fault
- Diagnostic notes: In the GM TSB set above.
- Grade: A
- Evidence: GM service bulletin 2186567

## U2100
- Description: CAN-BUS Communication (bus-off condition)
- Category: U
- Scope: manufacturer (GM)
- Possible causes: Total or partial loss of high-speed GMLAN serial data (shorts, opens, module internal fault)
- Diagnostic notes: GM SI: "When a module detects a bus-off condition a DTC U0001 or U2100 will be set. These DTCs can be retrieved as history only." Engine will not start with a total HS GMLAN failure while not running. HS GMLAN modules: BCM, OnStar (communication interface module), EBCM, ESC, ECM, TCM.
- Grade: B
- Evidence: GM SI excerpt via scribd ("Scan Tool Does Not Communicate With High Speed GMLAN Device")

## U2105
- Description: Lost Communication With Transmission Control Module (Silverado 2003 context)
- Category: U
- Scope: manufacturer (GM)
- Possible causes: TCM wiring/connector damage or corrosion; low system voltage
- Diagnostic notes: Single technician source (2003 Silverado 2500HD). Check TCM-PCM harness and battery/charging system; clear and retest.
- Grade: C
- Evidence: JustAnswer technician Q&A (single source)

## U2106
- Description: Lost Communication With Engine Control Module
- Category: U
- Scope: manufacturer (GM)
- Possible causes: ECM connectors/wiring corrosion or damage; blown fuses/relays; faulty ECM
- Diagnostic notes: Diesel-forum and technician reports (2004 6.6L): inspect ECM connectors and fuses; battery-disconnect reset may clear. Often accompanies TCM power issues — verify TCM is powering up (PRNDL display, shift behavior) before condemning the ECM.
- Grade: C
- Evidence: thedieselpageforums.com; JustAnswer (single-source each)

## B-codes (body)

## B1001
- Description: Option Configuration Error
- Category: B
- Scope: manufacturer (GM)
- Possible causes: SDM or BCM replaced without VIN programming; VIN mismatch between SDM (inflatable restraint sensing and diagnostic module) and BCM
- Diagnostic notes: The SDM stores the restraint ID from the VIN plus the last 4 digits of the SDM part number; at key-on it compares against the BCM over GMLAN. Mismatch sets B1001 and lights the airbag lamp; the code returns every power cycle until fixed. Fix: with a capable scan tool, run "Setup New BCM" / program the VIN into the SDM so both modules agree. Some vehicles require dealer programming.
- Grade: B
- Evidence: gmtnation.com (GM SI-style description); EFILive forum (SDM/BCM VIN mismatch reports)

## B1325
- Description: Device Power / module communication fault (seen as radio-module communication fault on 2015 Silverado/Sierra)
- Category: B
- Scope: manufacturer (GM)
- Possible causes: Radio module wiring harness damage or loose pins; faulty radio module; BCM communication fault; low system voltage
- Diagnostic notes: Technician reports on 2015 Silverado/Sierra pair B1325 with U0164 (lost communication with HVAC/radio network). Inspect radio harness connectors for corrosion; check BCM for related faults; battery-disconnect reset; reprogram or replace the module if wiring is sound. Descriptor varies by module — verify per model SI.
- Grade: C
- Evidence: JustAnswer technician Q&A (single-source reports)

## C-codes (chassis / EBCM)

Descriptors below are from GM SI master DTC lists (2006 Corvette / Buick Terraza Ext. 2006). Possible causes were not documented in the listing sources and are not invented.

## C0161
- Description: Antilock Brake System (ABS)/Traction Control System (TCS) Brake Switch Circuit
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: EBCM code. Verify brake switch input to the EBCM before replacing the module.
- Grade: B
- Evidence: GM SI master DTC lists (Corvette 2006; Terraza 2006) via corvetteactioncenter/corvetteforum

## C0240
- Description: Powertrain Control Module (PCM) Traction Control Not Allowed
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Informational — the PCM is refusing torque reduction; diagnose the PCM-side DTCs first.
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0242
- Description: Powertrain Control Module (PCM) Indicated TCS Malfunction
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented (fault is in the ECM/PCM, not the EBCM)
- Diagnostic notes: GM SI circuit description: "When certain PCM DTCs are set, the PCM will not be able to perform the torque reduction for traction control. A serial data message is sent to the EBCM indicating that traction control is not allowed." The EBCM then deactivates traction control. This is an INFORMATION code — the fault is in the ECM; diagnose ECM DTCs, not the EBCM.
- Grade: B
- Evidence: GM SI (Mitchell excerpt) via CorvetteForum; GM SI master DTC lists

## C0252
- Description: Vehicle Stability Enhancement System (VSES) Sensors Uncorrelated
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0267
- Description: Low Brake Fluid Indicated
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Check brake fluid level and the fluid-level sensor circuit first — this is a level indication, not necessarily an EBCM fault.
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0281
- Description: Dynamic Rear Proportioning (DRP) Performance
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0550
- Description: Electronic Control Unit (ECU) Performance
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Internal EBCM performance fault — typically requires EBCM replacement/programming after ruling out power/ground.
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0551
- Description: Option Configuration Error
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: EBCM-side analog of B1001 — module configuration/VIN mismatch; programming required.
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter

## C0561
- Description: System Disabled Information Stored
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: Informational — another module has disabled the system; read the disabling module's codes.
- Grade: B
- Evidence: GM SI master DTC lists via corvetteactioncenter/corvetteforum

## C0569
- Description: System Configuration Error
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: GM SI master DTC lists via corvetteforum

## C1100
- Description: Base Brake System Pressure Sensor 2
- Category: C
- Scope: manufacturer (GM)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: B
- Evidence: GM SI master DTC list (Buick Terraza Ext. 2006) via gm.saturn.team

## GM platform quirks (diagnostic procedure notes)

- **SWCAN wake-up before code reads:** On low-speed (single-wire) GMLAN vehicles, sleeping modules will not answer diagnostic requests. Send the high-voltage wake-up (mode 2, then mode 3 for normal communication) before expecting code responses — a "no communication" result on SWCAN often means the bus is asleep, not broken.
- **DTC Type A/B/C:** GM classifies powertrain DTCs as Type A (MIL on first trip, e.g. P1258, P1516, P1860 on some models), Type B (MIL after 2 consecutive trips, e.g. P1870), Type C (no MIL; service lamp or nothing, e.g. P1811). The type varies by model and year — always verify per model SI.
- **Global A vs older platforms:** Older (pre-2010, Class 2 / early GMLAN) vehicles use the P16xx/P17xx/P18xx-heavy code set above (quad-driver, driver-5-line, 4T65E codes). Global A (2010+) vehicles shifted toward U-code-heavy network diagnostics and module-specific P1xxx codes (e.g. P1101 on 1.4L/1.5L turbos, hybrid P1Exx on Volt). A code number can mean different things across eras (see P1174 conflict).
- **Informational DTCs:** P1700, P1E00, C0240, C0242, C0561 are informational — they point at another module. Always read the referenced module's codes before diagnosing.
- **Module programming:** B1001/C0551-class configuration errors and most module replacements require VIN programming with a dealer-level tool (Tech2/GDS2/SPS); clearing the code without programming will not fix it.
- **High-voltage safety:** Hybrid/EV DTCs (P1Exx) involve the high-voltage system. Secured HV DTCs may not clear with a generic tool and can require HPCM2 reprogramming. Do not attempt HV diagnosis without proper training and equipment.

## Coverage notes (gaps and unverified ranges)

- **P11xx range:** Only P1101, P1174, P1175 verified. P1100, P1105-P1173, P1176-P11FF not verified — skipped.
- **P12xx range:** Not verified (P1258 done; P1200-P1257, P1259-P12FF skipped). Known-unverified examples: P1248, P1271-P1278 (APP sensor correlation codes exist on some models but were not verified in this pass).
- **P13xx range:** Not covered — GM misfire P13xx codes not verified.
- **P14xx range:** Not covered — GM EVAP/secondary-air P14xx codes not verified.
- **P15xx range:** Only P1516 verified; P1500-P1515, P1517-P15FF skipped.
- **P16xx descriptor-only entries:** from transcribed lists only; causes/notes unverified. P1600-P1628 skipped.
- **P18xx:** P1860/P1870/P1810/P1811 verified; P1802-P1809, P1813, P1815-P18FF skipped.
- **P19xx range:** Not covered — not verified in this pass.
- **P1Axx-P1Dx hybrid/EV codes:** Only P1E00 included (Grade C). P1Axx-P1DFx (Volt/Bolt HPCM codes) not systematically verified — flagged for a dedicated hybrid pass.
- **U1xxx/U2xxx GM-specific:** Not verified (U1500, U1800, U19xx, U2xxx ranges skipped). U2105/U2106 are single-source (Grade C).
- **B-codes:** Only B1001 (B) and B1325 (C) included. B0xxx airbag/SDM codes, B1xxx-B3xxx ranges not systematically verified.
- **C-codes:** EBCM descriptors from Corvette/Terraza SI listings only; causes unquoted from listings. C0xxx wheel-speed/pump-motor codes (C0035-C0110) are largely SAE-generic and belong to the J2012 list. C1xxx+ ranges beyond C1100 not verified.
- **Conflicts reported:** P1174 (TSB fuel-trim vs EOBD diesel injection-pump reading); P1631 (theft-deterrent vs O2-sensor readings between transcribed lists); P1682 feed-circuit variation across model years.
- **Diesel (Duramax) codes:** not covered — the P1174 conflict shows diesel meanings diverge; Duramax-specific P-codes need a separate pass.
