# Nissan / Infiniti — Manufacturer-Specific DTCs (v1.2.1)

Research for the M2 OEM vehicle database v1.2.1 expansion. SAE J2012 generic
codes are NOT duplicated here (they live in work/dtc-generic.md). Every entry
carries a quality grade: **A** = Nissan/Infiniti service manual or TSB text ·
**B** = reputable DTC database / multi-source agreement · **C** = single
community source. "not documented" means no source was found — nothing is
invented. Research date: 2026-10-06.

---

## P-codes (Nissan-specific)

## P1031
- Description: A/F Sensor Heater (Bank 1)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Nissan TSB NTB04-032a (2004 Titan/Armada): MIL ON with P1031/P1051/P1148/P1168 addressed by ECM reprogram after confirming ECM part number against the bulletin chart.
- Grade: [B]
- Evidence: Nissan TSB NTB04-032a excerpt via scribd (A/F sensor heater / closed loop)

## P1051
- Description: A/F Sensor Heater (Bank 2)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Same TSB NTB04-032a coverage as P1031 (bank 2 counterpart).
- Grade: [B]
- Evidence: Nissan TSB NTB04-032a excerpt via scribd

## P1105
- Description: MAP/BARO Pressure Switch Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1126
- Description: Thermostat Function
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1130
- Description: Swirl Control Valve Control Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1148
- Description: Closed Loop Control (Bank 1) — A/F sensor closed-loop fault
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: failed A/F sensor (bank 1 sensor 1); damaged sensor connectors; poor grounding; wiring shorts; exhaust leaks
- Diagnostic notes: Nissan TSB NTB04-032a covers 2004 Titan/Armada MIL ON with P1148/P1168 — fix is an ECM reprogram (verify ECM part number against the bulletin first). On other models, inspect the A/F sensor harness and connectors before condemning the sensor.
- Grade: [B]
- Evidence: Nissan TSB NTB04-032a (reprogram fix); JustAnswer Nissan techs (causes: harness, grounds, sensor)

## P1165
- Description: Swirl Control Valve Control Vacuum Switch
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1168
- Description: Closed Loop Control (Bank 2) — A/F sensor closed-loop fault
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: failed A/F sensor (bank 2 sensor 1); wiring/connector damage; poor grounding
- Diagnostic notes: Bank-2 counterpart of P1148; same TSB NTB04-032a ECM-reprogram coverage on 2004 Titan/Armada.
- Grade: [B]
- Evidence: Nissan TSB NTB04-032a; JustAnswer Nissan techs

## P1211
- Description: ABS/TCS Control Unit
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1212
- Description: ABS/TCS Communication Line — ECM cannot receive information from ABS actuator and electric unit (control unit) continuously
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: CAN communication line open or shorted (harness/connectors); ABS actuator and electric unit (control unit); weak battery
- Diagnostic notes: Diagnose U1000/U1001 communication codes FIRST before chasing P1212; the TCM/ABS module is not necessarily at fault.
- Grade: [B]
- Evidence: fixya.com technician answer (causes); troublecodehub (diagnose-U-first guidance)

## P1217
- Description: Engine Over Temperature (Overheat)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1273
- Description: A/F Sensor Bank 1 Lean Shift Monitoring — A/F signal shifted lean for a specified period
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: faulty A/F sensor 1 (bank 1); sensor harness open/shorted; poor electrical connection; low fuel pressure; faulty fuel injector; faulty mass air flow sensor; intake air leaks
- Diagnostic notes: Nissan TSBs 04-090A/04-126/04-027a/05-095/04-025 cover P1273/P1283 on 2004-2005 VQ35/VQ40 vehicles — review the bulletins before normal troubleshooting. After repair, clear the mixture-ratio self-learning data or the code can return.
- Grade: [B]
- Evidence: Nissan TSB excerpts via justanswer.com; eobdcode.com (causes list); my4dsc.com (self-learning clear)

## P1274
- Description: A/F Sensor Bank 1 Rich Shift Monitoring
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank-1 rich counterpart of P1273; referenced in the same Nissan TSB family (04-090A series).
- Grade: [B]
- Evidence: Nissan TSB excerpt via justanswer.com (P1273/P1283 with P1274/P1284 rich monitors)

## P1283
- Description: A/F Sensor Bank 2 Lean Shift Monitoring — A/F signal shifted lean for a specified period
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: faulty A/F sensor 1 (bank 2); sensor harness open/shorted; poor electrical connection; low fuel pressure; faulty fuel injector; intake air leaks; faulty air flow meter
- Diagnostic notes: Same TSB family and self-learning-clear requirement as P1273 (bank 2).
- Grade: [B]
- Evidence: Nissan TSB excerpts via justanswer.com; eobdcode.com (causes); nicoclub forums (field reports)

## P1284
- Description: A/F Sensor Bank 2 Rich Shift Monitoring
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Bank-2 rich counterpart of P1283.
- Grade: [B]
- Evidence: Nissan TSB excerpt via justanswer.com

## P1320
- Description: Ignition Signal
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1335
- Description: Crankshaft Position Sensor (REF)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1336
- Description: Crankshaft Position Sensor (CKPS)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1400
- Description: EGRC Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1401
- Description: EGR Temperature Sensor
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1402
- Description: EGR System
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1440
- Description: EVAP Control System Small Leak
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1441
- Description: Vacuum Cut Valve Bypass Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Nissan-specific EVAP architecture (vacuum cut valve + bypass valve); distinct from generic P044x leak codes.
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1444
- Description: Canister Purge Volume Control Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1445
- Description: EVAP Canister Purge Volume Control Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1446
- Description: EVAP Canister Vent Control Valve (Closed)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1447
- Description: EVAP Control System Purge Flow Monitoring
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1448
- Description: EVAP Canister Vent Control Valve (Open)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1464
- Description: Fuel Level Sensor Circuit (Ground Signal)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1490
- Description: Vacuum Cut Valve Bypass Valve (Circuit)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1491
- Description: Vacuum Cut Valve Bypass Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1492
- Description: EVAP Canister Purge Control/Solenoid Valve (Circuit)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1493
- Description: EVAP Canister Purge Control Valve/Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1550
- Description: TCC Solenoid Valve
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1605
- Description: A/T Diagnostic Communication Line
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1610
- Description: NATS Lock Mode — NATS shifted to a mode preventing engine start after 5+ consecutive start attempts with an unregistered key or malfunctioning IMMU/ECM
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: unregistered ignition key used repeatedly; IMMU or ECM malfunction; low battery voltage mimicking NATS failure
- Diagnostic notes: Nissan TSB (2005-2008 NATS vehicles, via Mitchell 1): a no-start with P1610 is often NOT NATS-related — check battery voltage/state of charge with GR-8 first; do NOT replace NATS components until battery service is ruled out. P1610 with other NATS codes (P1611-P1615, B2191-B2193, B2590) points to the service manual.
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart (scribd/manuals.plus excerpts); Nissan TSB via vehicleservicepros.com (Mitchell 1)

## P1611
- Description: NATS ID Discord IMMU-ECM — ID verification between IMMU/BCM (NATS control unit) and ECM is NG; system initialization required
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: ECM replaced without NATS initialization; key ID registration lost
- Diagnostic notes: Common after ECM replacement — reprogramming/initialization of keys is required (dealer or locksmith with NATS capability). Initialization erases ALL registered key IDs; have all customer keys present.
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart; Autel walkthrough (initialization erases all key IDs)

## P1612
- Description: NATS Chain of ECM-IMMU — communication impossible between ECM and IMMU (NATS control unit)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: wiring between ECM and IMMU; IMMU malfunction
- Diagnostic notes: Service manual note: CHAIN OF ECM-IMMU can be stored spuriously during the key registration procedure even when nothing is malfunctioning — do not chase it if it appears mid-registration.
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart

## P1613
- Description: NATS ECM INT CIRC-IMMU — malfunction of the ECM internal circuit of the IMMU communication line
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart

## P1614
- Description: NATS Chain of IMMU-Key — IMMU cannot receive the key ID signal
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: NATS antenna amplifier (on ignition cylinder) faulty; unregistered or damaged key/FOB; blown fuse; weak FOB battery
- Diagnostic notes: If it is the only code, try a different registered key first and check fuses; the antenna amp communicates with the BCM — inspect it before condemning the ECM.
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart; JustAnswer/fixya technician guidance (antenna amp, key try-first)

## P1615
- Description: NATS Difference of Key — IMMU receives the key ID signal but ID verification between key ID and IMMU is NG
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: unregistered or wrong key used
- Diagnostic notes: Key must be registered to the vehicle via CONSULT-II/III NATS software; all keys must be present at registration.
- Grade: [A]
- Evidence: Nissan/Infiniti NATS service-manual self-diagnostic chart

## P1705
- Description: Throttle Position Sensor Circuit (A/T)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1706
- Description: Park/Neutral Position (PNP) Switch
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1760
- Description: Overrun Clutch Solenoid Valve (Circuit)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: Two corroborating transcribed Nissan-specific DTC lists (retrolib.info PDF; sr20-forum.com)

## P1815
- Description: Manual Mode Switch — impossible switch-signal pattern detected (manual/non-manual/up/down)
- Category: P
- Scope: manufacturer (Nissan)
- Possible causes: harness or connectors (switch circuits open or shorted); mode select switch (in A/T control device); position select switch (in A/T control device); sticky/bad microswitch in the shifter assembly
- Diagnostic notes: NOT an OBD-II self-diagnostic item — CONSULT-III only. The up/down switches are in series with the manual throw; the code means one switch shows active while the auto throw also shows active, which is impossible with working switches. Check for spills/debris in the shifter assembly.
- Grade: [A]
- Evidence: Nissan/Infiniti service manual (charm.li excerpts: 2011 Titan, 2007/2003 G35); nicoclub technician (microswitch mechanism)

---

## U-codes (Nissan network)

## U1000
- Description: CAN Communication Line — missing CAN communications on the network (signal malfunction)
- Category: U
- Scope: manufacturer (Nissan)
- Possible causes: CAN communication harness open or shorted; faulty ECM; poor harness ground connection (engine compartment and behind-dash grounds); low battery voltage
- Diagnostic notes: Nissan TSB NTB10-066C: always diagnose communication codes FIRST; when a module reports U1000 it is typically operating normally — the fault is external to that module. Set when communication is lost for longer than 2 seconds. A well-known field fix is cleaning/resecuring the harness grounds (paint under dash-brace grounds causes high resistance).
- Grade: [A]
- Evidence: Nissan TSB NTB10-066C (2024); troublecodehub/fixya field reports (ground fix)

## U1001
- Description: CAN Communication Line — ECM-specific missing CAN communications on the network
- Category: U
- Scope: manufacturer (Nissan)
- Possible causes: CAN harness open/shorted; faulty ECM; poor grounds; failed combination meter or other control unit pulling the bus down
- Diagnostic notes: Same TSB NTB10-066C guidance as U1000. A failed control unit (e.g. combination meter) can cause U1001 — CAN diagnostics with an advanced scanner identifies the silent module.
- Grade: [A]
- Evidence: Nissan TSB NTB10-066C (2024); JustAnswer Nissan dealer tech (combination-meter case)

## U1002
- Description: CAN Communication Line — missing CAN communications, tighter specification than U1000
- Category: U
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Per TSB NTB10-066C, same diagnostic path as U1000 with a tighter detection spec.
- Grade: [A]
- Evidence: Nissan TSB NTB10-066C (2024)

## U1010
- Description: Control Unit — module internal error
- Category: U
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: TSB NTB10-066C: if a module is highlighted as faulty while other modules/segments show communication errors, diagnose the others first, erase DTCs, and re-run CAN diagnosis — replace the module only if it is still flagged alone.
- Grade: [A]
- Evidence: Nissan TSB NTB10-066C (2024)

---

## B-codes (Nissan body / NATS)

## B2014
- Description: Chain of S/L-BCM — steering lock unit to BCM communication fault; inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: From the Nissan power-distribution service manual BCM DTC chart; engine cranking is inhibited while this code is active.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2190
- Description: Difference of Key (NATS antenna) — different/unregistered key detected via NATS antenna
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: unregistered key used
- Diagnostic notes: BCM-level counterpart to P1615; resolve any U-codes (communication faults) before diagnosing B-codes.
- Grade: [B]
- Evidence: JustAnswer Nissan technician (B2190/B2191 NATS antenna, different key detected)

## B2191
- Description: Difference of Key — ID verification between BCM and Intelligent Key is NG; prohibits steering-lock release / engine start with unregistered Intelligent Key
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: unregistered Intelligent Key; Intelligent Key malfunction
- Diagnostic notes: Nissan service-manual procedure: perform initialization with CONSULT-III and re-register ALL Intelligent Keys. CONFLICT: one YouTube DTC video labels B2191 as "HO2S Heater Circuit Short (Right Bank)" — this contradicts the Nissan service manual and is almost certainly a mislabeled generic decode; the service-manual definition (Difference of Key) is used here.
- Grade: [A]
- Evidence: Nissan service manual (SEC section, scribd excerpt: B2191 Difference of Key, initialization + re-register all keys)

## B2192
- Description: ID Discord BCM-ECM — BCM performs ID verification with ECM; inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM-level counterpart to P1611; erase DTC after initialization.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt); niveguide.com (BCM-ECM ID verification)

## B2193
- Description: Chain of BCM-ECM — BCM to ECM communication chain fault; inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM-level counterpart to P1612; erase DTC after repair.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2195
- Description: Anti-Scanning — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: NATS anti-scanning function tripped; ignition ON/OFF cycle per service manual.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2196
- Description: Dongle NG — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Dongle-unit (RHD models) malfunction; erase DTC after repair.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2198
- Description: NATS Antenna Amp — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: NATS antenna amplifier malfunction
- Diagnostic notes: BCM-level counterpart to P1614; erase DTC 500 ms after signal communication becomes consistent.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2590
- Description: not verified — referenced as a NATS DTC in a Mitchell 1 Nissan TSB alongside P1610-P1615/B2191-B2193, but no definition was found in verifiable sources
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Listed here for completeness so the TSB's code set is not silently truncated; treat the definition as unverified.
- Grade: [C]
- Evidence: vehicleservicepros.com (Mitchell 1 TSB excerpt listing B2590 among NATS DTCs)

## B2608
- Description: Starter Relay — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Starter motor relay control signal / CAN status signal inconsistency.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B260F
- Description: Engine State Signal Lost — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: Received engine status signal (CAN) lost after power position changes to ACC.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B2619
- Description: BCM — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: BCM-internal fault flag in the cranking-inhibit chart.
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

## B26F1
- Description: Ignition Relay OFF — inhibits engine cranking
- Category: B
- Scope: manufacturer (Nissan)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan service manual (power distribution system, manuals.plus excerpt)

---

## C-codes (Nissan chassis / ABS-VDC)

## C1101
- Description: RR RH Sensor 1 — circuit of rear RH wheel sensor is open
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: wheel sensor; sensor reluctor/tone ring; wiring harness between ABS module and sensor; faulty ABS actuator and electric unit (control unit)
- Diagnostic notes: From the Nissan brake-control service manual self-diagnostic item chart. If the sensor was already replaced with no change, inspect the reluctor ring and the harness before condemning the ABS unit; a capable scanner reading ABS live wheel-speed data is the fastest next step.
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt); JustAnswer (Titan XD C1101 field case)

## C1102
- Description: RR LH Sensor 1 — circuit of rear LH wheel sensor is open
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: wheel sensor; reluctor; harness; ABS control unit
- Diagnostic notes: Same diagnostic path as C1101 (rear LH position).
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1103
- Description: FR RH Sensor 1 — circuit of front RH wheel sensor is open
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: wheel sensor; reluctor; harness; ABS control unit
- Diagnostic notes: Same diagnostic path as C1101 (front RH position).
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1104
- Description: FR LH Sensor 1 — circuit of front LH wheel sensor is open
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: wheel sensor; reluctor; harness; ABS control unit
- Diagnostic notes: Same diagnostic path as C1101 (front LH position). Note: some scan tools convert Nissan 2-digit ABS codes to 4-digit codes inaccurately — confirm with a Nissan-capable tool.
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt); JustAnswer (scan-tool conversion caveat)

## C1105
- Description: RR RH Sensor 2 — circuit of rear RH wheel sensor is shorted, or sensor power voltage is unusual
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: shorted sensor circuit; abnormal sensor supply voltage; excessive gap between wheel sensor and sensor rotor (control unit cannot identify pulses)
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1106
- Description: RR LH Sensor 2 — circuit of rear LH wheel sensor is shorted, or sensor power voltage is unusual
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1107
- Description: FR RH Sensor 2 — circuit of front RH wheel sensor is shorted, or sensor power voltage is unusual
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1108
- Description: FR LH Sensor 2 — circuit of front LH wheel sensor is shorted, or sensor power voltage is unusual
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: shorted sensor circuit; abnormal sensor supply voltage; excessive sensor-to-rotor gap
- Diagnostic notes: not documented
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1109
- Description: Battery Voltage Abnormal — ABS actuator and electric unit (control unit) power voltage too low
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: low battery voltage; charging system fault
- Diagnostic notes: Check battery/charging before condemning the ABS unit — low voltage alone sets this code.
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1110
- Description: Controller Failure — internal malfunction of ABS actuator and electric unit (control unit)
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: internal ABS control-unit failure
- Diagnostic notes: Service-manual reference: ABS/TCS/VDC control unit inspection; this code means the unit itself, not its inputs.
- Grade: [A]
- Evidence: Nissan service manual (brake control system BRC section, carmanuals2.com excerpt)

## C1111
- Description: Pump Motor — ABS pump motor fault during actuator motor operation
- Category: C
- Scope: manufacturer (Nissan)
- Possible causes: ABS pump motor; power/ground to the pump
- Diagnostic notes: The pump can be bench-tested by remotely applying power and ground to verify it activates.
- Grade: [B]
- Evidence: Nissan service manual (brake control system BRC section); JustAnswer (pump bench-test procedure)

---

## Nissan quirks

1. **NATS registration erases all keys.** Any NATS initialization (P1611/P1610/B2191 procedures) erases every registered key ID first — all customer keys must be present before starting, or a half-finished procedure leaves zero working keys [A — service manual; B — Autel walkthrough].
2. **P1610 lock mode is often not NATS.** Nissan's 2005-2008 TSB: check battery voltage/state of charge first; do not replace NATS components for a P1610 no-start until the battery is ruled out [B — Mitchell 1 via vehicleservicepros].
3. **P1612 can set spuriously during key registration.** The service manual notes CHAIN OF ECM-IMMU may store mid-registration with no malfunction — do not chase it in that context [A].
4. **U1000: the reporting module is usually innocent.** Per TSB NTB10-066C, a module reporting U1000 is typically operating normally; the fault is external on the CAN network. Diagnose communication codes before all others [A].
5. **The dash-brace ground fix.** A notorious Nissan field fix for U1000/U1001: harness grounds bolted to the painted dash brace develop high resistance — clean to bare metal, apply dielectric grease, resecure [B — multiple field reports].
6. **P1815 is CONSULT-only.** It is explicitly not an OBD-II self-diagnostic item; a generic scan tool will never report it — only CONSULT-II/III [A — service manual].
7. **B2191 conflict.** One YouTube DTC video decodes B2191 as "HO2S Heater Circuit Short (Right Bank)"; the Nissan service manual defines it as "Difference of Key." The service-manual definition is used here [A vs C].
8. **DDL-era vs CAN-era codes.** Pre-OBD-II Nissan diagnostics used DDL/Consult with its own code scheme (see work/nissan.md §2); the P1xxx/B2xxx/C11xx codes in this file are the OBD-II/CAN-era scheme. Do not mix the two eras [B — inferred from the protocol split].
9. **B2590 is unverified.** It appears in a Mitchell 1 TSB's NATS code list but no definition was found in verifiable sources; it is listed above with an explicit unverified flag rather than omitted [C].

---

## Coverage notes

- Verified and included: 45 P-codes, 4 U-codes, 13 B-codes, 11 C-codes (73 entries; B2590 flagged unverified).
- **Not verified / out of scope this pass:** P12xx beyond P1211/P1212/P1217; P13xx beyond P1320/P1335/P1336; P15xx beyond P1550; P16xx beyond the NATS P1610-P1615 set; P17xx/P18xx transmission/CVT codes beyond P1705/P1706/P1760/P1815 (notably CVT-specific P17xx and 4WD P18xx families); B1xxx airbag (SRS) codes; C11xx beyond C1111 (VDC/ABS solenoid and steering-angle families); U1xxx lost-communication codes beyond the U1000 family; Infiniti-specific deviations from Nissan codes; DDL/Consult-era code definitions.
- B0xxx/C0xxx generic thin spots noted in the v1.2 generic pass also apply here — Nissan-specific B/C ranges would benefit from a second source pass.
- A Nissan FAST/parts-catalog or full ESM extract would be the ideal A-grade source for the unverified ranges above.
