# Stellantis (Chrysler / Dodge / Jeep / RAM / Fiat) — Manufacturer-Specific DTCs

Research for the M2 OEM vehicle database v1.2. **SAE J2012 generic codes are intentionally excluded** — a separate agent covers those.
Grades: **A** = Stellantis/FCA service info or TSB · **B** = reputable DTC database, Mitchell service data, or multi-source agreement · **C** = single community source.
Research date: 2026-10-06.

Ordering: P-codes, then U-codes, then B/C-codes, per priority.

---

# P-codes (manufacturer-specific)

## P1184
- Description: Engine Oil Temperature Circuit Malfunction (Cummins diesel)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: not documented
- Diagnostic notes: Appears in the Cummins-diesel DTC list (dodgeforum diesel tech list); do not confuse with P1184's use on other makes. not documented beyond description.
- Grade: [C]
- Evidence: dodgeforum.com diesel-tech trouble code list (community list)

## P1185
- Description: Fuel Pump Temperature Sensor High / FTS High (Cummins diesel)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: not documented
- Diagnostic notes: The diesel-list formatting groups P1184 (engine oil temp) and P1185/P1186 (fuel pump temp sensor high/low). Reported, not resolved: some generic DTC databases map P1185 differently (e.g. to engine oil temp range) — the Cummins context is the verified Stellantis use.
- Grade: [C]
- Evidence: dodgeforum.com diesel-tech trouble code list (community list)

## P1294
- Description: Target Idle Not Reached
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Engine/brake-booster/vacuum hose leaks; throttle plate/linkage misposition; IAC wiring intermittent or observable defect; throttle body defective; failed PCM; carbon deposits; driver circuit open/shorted
- Diagnostic notes: Monitored with engine idling in Drive (auto trans), no MAP/TP sensor codes present. Sets when idle is >200 rpm above or <100 rpm below target for ~14-20 s (two consecutive failures / two bad trips, model-dependent). Scan-tool IAC wiggle test is the standard first check (service manual TC-25A/TC-138B test path).
- Grade: [A]
- Evidence: FCA service manual excerpts via charm.li (1998-1999 Concorde/Intrepid/Dakota/Town & Country); corroborated by 2carpros diagnostic walkthrough

## P1390
- Description: Cam and Crank Signals Don't Match
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Timing chain/belt misalignment; CMP/CKP sensor faults; wiring
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: archiveteam Chrysler/Dodge/Jeep code table; multi-list agreement

## P1391
- Description: Intermittent Loss of Camshaft Position Sensor or Crankshaft Position Sensor
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Failing CMP or CKP sensor; connector/wiring intermittent; tone wheel damage
- Diagnostic notes: Classic no-start/stall code on 4.0L/4.7L/5.2L/5.9L era engines; often one of the two sensors fails hot. not documented further in sources checked.
- Grade: [B]
- Evidence: archiveteam Chrysler/Dodge/Jeep code table; multi-list agreement

## P1398
- Description: Mis-Fire Adapter Numerator at Limit
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: CKP sensor / tone wheel issues; PCM misfire-adaptive at correction limit
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: archiveteam Chrysler/Dodge/Jeep code table

## P1491
- Description: Radiator Fan Control Relay Circuit
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Fused B(+) or fused ignition-switch output circuit open; radiator fan relay defective; relay control circuit open or shorted to ground; radiator fan relay ground circuit open; fan motor wiring intermittent/observable defect; PCM defective; (2003+ models: Intelligent Power Module shorted/open)
- Diagnostic notes: Monitored with ignition on, battery >10-10.4 V, while PCM commands fans on. Sets on open/short detected in the relay control circuit.
- Grade: [A]
- Evidence: FCA service manual excerpts via charm.li (1999-2003 Caravan/Town & Country/Cherokee/Dakota/Voyager)

## P1492
- Description: Battery Temperature Sensor Voltage Too High
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Battery temp sensor circuit shorted to voltage; sensor failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list; dodgeforum DTC list agreement

## P1493
- Description: Battery Temperature Sensor Voltage Too Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Battery temp sensor circuit shorted to ground or open; sensor failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list; dodgeforum DTC list agreement

## P1494
- Description: Leak Detection Pump (LDP) Switch or Mechanical Fault — EVAP Leak Detection Pump Pressure Switch Condition
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Wiring harness intermittent; LDP switch sense circuit shorted to ground or open; LDP vacuum supply; leak detection pump itself; faulty gas cap or vacuum leak elsewhere in EVAP system; PCM
- Diagnostic notes: Monitored immediately after cold start (battery/ambient 40-90 F, coolant within 10 F of ambient). Sets when the pressure-switch state does not change when the solenoid is energized. Inspect LDP hoses/wiring under the vehicle for debris damage before replacing the pump; aftermarket gas caps that bleed down faster than the Mopar cap are a known false trigger. Chrysler's LDP-based EVAP monitor is distinctive to the brand — no other OEM uses this exact pump design.
- Grade: [A]
- Evidence: FCA powertrain diagnostic manual excerpt (viperclub.org owner citing manual); FCA service manual via charm.li; corroborated by JustAnswer Chrysler techs

## P1495
- Description: Leak Detection Pump Solenoid Circuit
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: LDP solenoid electrical failure; solenoid harness open/shorted; poor electrical connection; PCM driver
- Diagnostic notes: Electrical-circuit counterpart to P1494's switch/mechanical fault. Check solenoid connector and wiring for damage/corrosion first.
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list; JustAnswer Dodge tech Q&A (white/dark-green vs white/dark-blue wire voltage check)

## P1496
- Description: 5 Volt Supply Output Too Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Shorted 5 V reference circuit (any sensor on the 5 V bus); PCM
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list

## P1594
- Description: Charging System Voltage Too High
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Alternator overcharging; wiring; battery; PCM field control
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: dodgeforum Chrysler DTC list; yumpu Autodata 2004 edition ("Alternator - voltage high")

## P1595
- Description: Speed Control Solenoid Circuits
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Speed control vacuum/vent solenoid control circuits shorted or open; hoses; cruise control master switch
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1596
- Description: Speed Control Switch Always High
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Cruise control master switch stuck/faulty; wiring shorted to voltage
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1597
- Description: Speed Control Switch Always Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Speed control switch stuck/faulty; wiring shorted to ground
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; manuals.plus Chrysler OBD2 code list

## P1598
- Description: A/C Pressure Sensor Volts Too High
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: A/C pressure signal circuit shorted to 5 V supply or battery voltage; A/C pressure sensor internal failure; signal circuit open; sensor ground circuit open; PCM
- Diagnostic notes: Factory diagnostic path (NGC-era): verify refrigerant charge first, then read A/C pressure sensor voltage with scan tool — fault threshold is above ~4.6 V; resistance-test the signal circuit against the 5 V supply for a short (<5 ohms = shorted). Note: the same code number means something different on Peugeot and other makes — this entry is the Stellantis definition only.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists; factory NGC driveability test procedure via chryslerforum.com service-manual attachment; yumpu Autodata 2004 edition

## P1599
- Description: A/C Pressure Sensor Volts Too Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: A/C pressure sensor circuit shorted to ground or open; low refrigerant charge; sensor failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1602
- Description: PCM Not Programmed
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: New/replacement PCM never flashed; incorrect programming
- Diagnostic notes: Set by a fresh or incorrectly programmed PCM; resolve with dealer-level flashing (wiTECH). No sensor diagnosis applies.
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1682
- Description: Charging System Voltage Too Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Alternator; drive belt; battery; wiring; PCM field control
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; dodgeforum DTC list

## P1684
- Description: Battery Disconnected Within Last 50 Starts (informational — not a fault)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Battery was disconnected or lost power (intentional service, dead battery, cleared PCM memory); weak battery/connections can also set it
- Diagnostic notes: STATUS ONLY — indicates PCM memory was cleared within the last ~50 ignition cycles and does NOT indicate a problem. Self-clears after ~50 starts. On the pre-CAN key-dance readout, "P1684 and done" means only this status is stored. Do not chase it as a drivability fault; if it will not clear alongside real symptoms, check battery cables/voltage.
- Grade: [A]
- Evidence: 2002-2008 Chrysler/Dodge/Jeep code guide (scribd, Skidsmadawg96); JustAnswer Chrysler tech ("P1684(12) - Battery was Disconnected (Informational code Only)"); partsofacarengine.com

## P1685
- Description: Wrong or Invalid Key Message Received From SKIM (Sentry Key Immobilizer Module)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Non-programmed or damaged key; SKIM/ignition antenna ring fault; SKIM module failure; bus communication fault
- Diagnostic notes: SKIM says the key presented is not recognized — engine typically cranks then stalls (start-stall) or will not start. Distinct from P1686 (no message at all).
- Grade: [B]
- Evidence: dodgeforum Chrysler DTC list; scribd Chrysler/Jeep list; yumpu Autodata 2004 edition ("Key not programmed into immobilizer control")

## P1686
- Description: No SKIM Bus Message Received
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: SKIM not powered (poor connection, broken wire); SKIM module failure; PCI/CCD bus wiring fault; PCM fault
- Diagnostic notes: Diagnose with a scan tool that can reach the whole vehicle network — determine which modules answer and which do not to localize the bus break. Cleaning the key/ignition cylinder is the field first step; battery-disconnect capacitor-drain reboot is a documented folk remedy, not factory procedure.
- Grade: [B]
- Evidence: dodgeforum Chrysler DTC list; fixya/JustAnswer Chrysler tech Q&As; naxja.org SKIM thread (no-start/start-stall behavior)

## P1687
- Description: No Cluster Bus Message (no MIC / instrument cluster bus message)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Instrument cluster failure or power loss; PCI/CCD bus wiring fault; PCM fault
- Diagnostic notes: Often paired with P1686; tach/temp gauges may work intermittently with warning lamps on. Address bus-level faults before condemning modules.
- Grade: [B]
- Evidence: dodgeforum Chrysler DTC list; JustAnswer Dodge tech ("NO MIC BUS MESSAGE ... the BUS consists of wires and circuit boards")

## P1688
- Description: Internal Fuel Injection Pump Controller Failure (Cummins diesel)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Injection pump controller internal failure; wiring
- Diagnostic notes: Cummins-diesel specific. not documented beyond description.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists

## P1693
- Description: DTC Detected In Companion Module (DTC detected in ECM or PCM)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Fault stored in the companion controller (ECM vs PCM split on diesels); companion module fault
- Diagnostic notes: Informational pointer — read the companion module for the real fault; most common on Cummins-diesel trucks with separate ECM/PCM.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists; yumpu Autodata 2004 edition

## P1694
- Description: No CCD Messages Received From ECM
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: CCD/PCI bus wiring fault; ECM power/ground; ECM failure
- Diagnostic notes: Pre-CAN (CCD/PCI bus) era code. Determine which modules the scan tool can reach to localize the fault.
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list; scribd Chrysler/Jeep list

## P1695
- Description: No CCD/J1850 Message From Body Control Module (BCM)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: BCM power/ground; CCD/PCI bus wiring fault; BCM failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: manuals.plus Chrysler OBD2 code list; scribd Chrysler/Jeep list

## P1698
- Description: No CCD Messages Received From PCM / No Bus Message From TCM
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: PCM/TCM power/ground; CCD bus wiring fault; module failure
- Diagnostic notes: The reported description varies slightly by source (PCM vs TCM as the silent module) — reported, not resolved; treat as "a powertrain module is silent on the CCD bus" and verify which module the scan tool cannot reach.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists; dodgeforum DTC list

## P1719
- Description: Skip Shift Solenoid Circuit
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Skip-shift (CAGS) solenoid circuit open/shorted; solenoid failure
- Diagnostic notes: Manual-transmission skip-shift (1st-to-4th) solenoid. not documented beyond description.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists

## P1740
- Description: TCC Or OD Solenoid Performance (torque reduction signal rationality)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Bad overdrive or torque-converter solenoid; torque converter clutch material unable to hold lockup
- Diagnostic notes: Chrysler-only code (not SAE-approved description). On RE transmissions the PCM looks for an RPM drop after OD/TCC apply; lockup occurs in 4th so the PCM cannot distinguish OD shift from TCC lockup by RPM alone.
- Grade: [B]
- Evidence: manuals.plus + scribd Chrysler DTC lists; scribd notes quoting Al Steier technical analysis

## P1756
- Description: Governor Pressure Not Equal To Target At 15-20 PSI (mid-pressure malfunction)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Governor pressure solenoid; valve body; transmission fluid level; governor pressure sensor; transmission mechanical fault
- Diagnostic notes: RE-series automatic transmission code. not documented beyond description.
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1757
- Description: Governor Pressure Above 3 PSI When Request Is 0 PSI (zero-pressure malfunction)
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Governor pressure solenoid; valve body; sensor; mechanical fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1762
- Description: Governor Pressure Sensor Offset Improper Voltage
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Governor pressure sensor; signal wire open/short; valve body; transmission fluid level; no 5 V supply from PCM
- Diagnostic notes: Sets when the sensor input is out of range for 3 consecutive park/neutral calibrations.
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1763
- Description: Governor Pressure Sensor Voltage Too High
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Signal wire open or shorted; sensor failure; valve body
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1764
- Description: Governor Pressure Sensor Voltage Too Low
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Signal wire shorted; sensor failure; transmission fluid level; mechanical fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list; yumpu Autodata 2004 edition

## P1765
- Description: Transmission 12 Volt Supply Relay Control Circuit
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: Trans relay control circuit open or shorted; relay failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list

## P1899
- Description: Park/Neutral Position Switch Stuck In Park or In Gear
- Category: P
- Scope: manufacturer (Stellantis)
- Possible causes: P/N switch failure or misadjustment; wiring
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: scribd Chrysler/Jeep DTC list

---

# U-codes (network — high importance on Stellantis)

## U1008
- Description: LIN 1 Bus
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: LIN bus wiring fault; LIN slave module failure
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U110A
- Description: Lost Communication With SCM (Steering Control Module)
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: SCM power/ground; CAN bus wiring fault; SCM failure
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U110C
- Description: Lost Fuel Level Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN bus communication fault; Front Control Module (FCM) failure; wiring/connectors corroded or damaged
- Diagnostic notes: Frequently appears with U0141/U1403/U110E as a CAN/FCM cluster of faults — inspect FCM connectors and CAN wiring before replacing modules.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; JustAnswer Dodge tech (Nitro CAN/FCM cluster)

## U110D
- Description: Lost Communication With Security Siren
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Security siren module power/ground; CAN bus wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U110E
- Description: Lost Ambient Temperature Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN C bus circuit open or shorted; Body Control Module; PCM; ambient temperature sensor itself
- Diagnostic notes: Theory of operation: the ambient temp sensor is a direct BCM input; the BCM transmits it to the PCM over the CAN C bus. A failed ambient temp sensor (located near the radiator/under hood) is a common real fix.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; JustAnswer Q&A with Dodge service manager (possible causes + theory of operation)

## U110F
- Description: Lost Fuel Volume Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN bus communication fault; sending module failure
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1110
- Description: Lost Vehicle Speed Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN C bus circuit open or shorted; Electronic Pedestrian Protection Module (EPPM); ESP/ABS module; PCM
- Diagnostic notes: Often the PRIMARY fault with U1120/U0121 as collateral — fix the vehicle-speed source first. Symptoms: dead speedometer, traction/ABS warnings. EPPM (floor panel under left front seat on some models) is a known failure point; inspect its connector for burned pins.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; JustAnswer Dodge Journey factory-manual probable causes (U1110-00)

## U1113
- Description: Lost A/C Pressure Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN bus communication fault; sending module failure
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1120
- Description: Lost Wheel Distance Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Anti-lock Brake Module; CAN C bus circuit open or shorted; PCM
- Diagnostic notes: Wheel-distance comes from the ABS module over CAN C. No-speedometer + ABS/traction warnings are typical. Check TCCM/TIPM connectors for corrosion; a tire-size change via tuner has been observed to trigger this family of codes.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; JustAnswer Dodge Journey factory-manual probable causes (U1120); ramforum/JustAnswer Wrangler cases

## U113B
- Description: Lost Communication With Switch Bank Module
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Switch bank module power/ground; CAN bus wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1141
- Description: Lost ESP Torque Request Message
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN bus open or shorted condition; ESP/ABS module; PCM
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: JustAnswer Dodge Journey factory-manual probable causes

## U1149
- Description: Lost Communication With Multifunction (module)
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Module power/ground; CAN bus wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1159
- Description: Lost Communication With ASBS
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Module power/ground; CAN bus wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1169
- Description: Lost Communication With Intrusion Sensor 1
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Intrusion sensor power/ground; CAN/LIN wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1170
- Description: Lost Communication With Intrusion Sensor 2
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Intrusion sensor power/ground; CAN/LIN wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1179
- Description: Lost Communication With Intrusion Sensor 3
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Intrusion sensor power/ground; CAN/LIN wiring fault
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1403
- Description: Implausible Fuel Level Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN B bus open or shorted; CAN B bus hardware DTCs also active; cluster module; Front Control Module; PCM
- Diagnostic notes: Monitored with ignition on; continuously monitored; one-trip fault. Diagnostic path: confirm the DTC is active, then check for CAN B hardware DTCs before condemning the cluster/FCM/PCM.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; factory-style diagnostic procedure (YouTube walkthrough citing FCA service info, WK Grand Cherokee / Durango)

## U1411
- Description: Implausible Fuel Volume Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: CAN B bus open or shorted; cluster module; Front Control Module; PCM
- Diagnostic notes: Same diagnostic family as U1403 (fuel-level/volume messages ride CAN B via cluster/FCM). not documented beyond probable causes.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; factory-style diagnostic procedure pattern (U1403/U1411 family)

## U1412
- Description: Implausible Vehicle Speed Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Wheel speed sensor / ABS signal fault; CAN C bus fault; ABS module; PCM
- Diagnostic notes: Seen together with U1417/U1418 after tire-size changes via aftermarket tuners — the PCM rejects wheel-distance/speed data inconsistent with its configuration. Verify tire size programming matches the fitted tires.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; Power Wagon Registry owner case (tire-size change triggered U1412/U1417/U1418 + P1C4E)

## U1414
- Description: Implausible/Missing ECU Network Configuration Data
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Module replaced without configuration; network configuration data missing/corrupt
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1415
- Description: Implausible/Missing Vehicle Configuration Data
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Module replaced without PROXI/configuration alignment; corrupt config data
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1416
- Description: Implausible Security Siren Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Security siren module fault; wiring
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U1417
- Description: Implausible Left Wheel Distance Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Vehicle speed sensor fault active in anti-lock brake module; CAN C bus circuit shorted or open; ABS module; PCM; wheel speed sensor(s)
- Diagnostic notes: Monitored with ignition on; PCM receives implausible wheel-distance over CAN C from the ABS module; one-trip fault. Diagnostic path: verify the DTC is active, confirm the ABS module is active on CAN C, check for ABS-module DTCs, check FCM for active DTCs. Often appears with U1418 (both sides) — on RAM trucks, front wheel speed sensors were the confirmed fix in owner cases.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; factory-style diagnostic procedure (Durango); ramforum.com owner cases

## U1418
- Description: Implausible Right Wheel Distance Signal Received
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Same family as U1417 — wheel speed sensor(s); ABS module; CAN C bus open/shorted; PCM
- Diagnostic notes: Steering-wheel lock-to-lock rotation x3 is a reported owner workaround for clearing it when the sensor is still good (unverified factory procedure — treat as anecdotal). Triggers CEL and/or ABS/traction warnings.
- Grade: [B]
- Evidence: 4x4community.co.za Jeep Wrangler code list; ramforum.com owner cases

## U1419
- Description: Implausible Data Received From OCS Sensor 3 - Left Front
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Occupant classification sensor fault; wiring
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U141A
- Description: Implausible Data Received From OCS Sensor 2 - Right Front
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Occupant classification sensor fault; wiring
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U141B
- Description: Implausible Data Received From OCS Sensor 4 - Left Rear
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Occupant classification sensor fault; wiring
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

## U141C
- Description: Implausible Data Received From OCS Sensor 1 - Right Rear
- Category: U
- Scope: manufacturer (Stellantis)
- Possible causes: Occupant classification sensor fault; wiring
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: 4x4community.co.za Jeep Wrangler code list (single community list)

---

# B-codes (body — ORC/airbag)

## B1B00
- Description: Driver Airbag Squib 1 Circuit Low
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Clockspring failure (known issue — FCA TSB 08-119-15 extended clockspring warranty to 10 yr/150,000 mi on 2007 JK Wrangler for this code family); squib wiring shorted low; driver airbag; ORC
- Diagnostic notes: Part of the B1B00-B1B07 driver-squib series. Always disconnect the 12 V battery and wait two minutes before working on squib circuits. Use an SRS load tool (not a plain multimeter) on live squib circuits per service procedure.
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com (static.oemdtc.com NHTSA PDF)

## B1B01
- Description: Driver Airbag Squib 1 Circuit High
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Clockspring failure; squib wiring shorted high; driver airbag; ORC
- Diagnostic notes: See B1B00 notes (same series/procedure).
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com

## B1B02
- Description: Driver Airbag Squib 1 Circuit Open
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Open circuit in the clockspring (most common); improper clockspring neutral position; disengaged/poor-contact squib connector; open in driver airbag squib circuit; ORC malfunction
- Diagnostic notes: The classic JK/JK-era code. If the clockspring was already replaced and the code persists, suspect the airbag module itself or the clockspring-to-airbag harness. Factory test: disconnect driver squib connectors, connect SRS load tool, re-read ORC DTCs — if the code clears with the load tool, replace the driver airbag.
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com; FCA ORC diagnostic procedure via manuals.plus (ProDemand excerpt); South Main Auto / JustAnswer tech cases

## B1B03
- Description: Driver Airbag Squib 1 Circuit Shorted Together
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Squib circuits shorted together; clockspring; wiring; ORC
- Diagnostic notes: See B1B00 notes (same series/procedure).
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com

## B1B04
- Description: Driver Airbag Squib 2 Circuit Low
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Clockspring failure; squib wiring shorted low; driver airbag; ORC
- Diagnostic notes: See B1B00 notes (same series/procedure).
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com

## B1B05
- Description: Driver Airbag Squib 2 Circuit High
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Clockspring failure; squib wiring shorted high; driver airbag; ORC
- Diagnostic notes: See B1B00 notes (same series/procedure).
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com

## B1B06
- Description: Driver Airbag Squib 2 Circuit Open
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Open circuit in the clockspring; improper clockspring neutral position; disengaged/poor-contact squib connector; driver airbag; ORC malfunction
- Diagnostic notes: Same family as B1B02 (squib 2 instead of squib 1). See B1B02 notes.
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com; FCA ORC diagnostic procedure via manuals.plus; South Main Auto / JustAnswer tech cases

## B1B07
- Description: Driver Airbag Squib 2 Circuit Shorted Together
- Category: B
- Scope: manufacturer (Stellantis)
- Possible causes: Squib circuits shorted together; clockspring; wiring; ORC
- Diagnostic notes: See B1B00 notes (same series/procedure).
- Grade: [A]
- Evidence: FCA TSB 08-119-15 via oemdtc.com

---

# C-codes (chassis — ABS)

## C1000
- Description: Brake Pedal Switch 1 Circuit - Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake signal 1 circuit shorted to voltage; brake lamp switch operation; ABS module; TIPM/BCM
- Diagnostic notes: The ABS module detects an invalid signal between master-cylinder pressure applied and the brake-lamp switch output for ~2 minutes. CONFLICT: a Mitsubishi service source uses C1000 for "stop lamp switch circuit abnormality" — the description above is the FCA (RAM/Journey) use; verify against the vehicle line before applying.
- Grade: [C]
- Evidence: ramforum.com owner thread quoting FCA diagnostic text (single thread); conflict noted vs Mitsubishi clubcj.net definition

## C1008
- Description: Brake Fluid Level Circuit High
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake fluid level switch circuit shorted high; switch failure
- Diagnostic notes: not documented beyond description
- Grade: [C]
- Evidence: iFixit-hosted FCA ABS diagnostic index PDF (documents.cdn.ifixit.com)

## C100A
- Description: Left Front Wheel Speed Sensor Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction
- Diagnostic notes: ABS module monitors voltage fluctuation in each wheel-speed-sensor circuit; sets on detected open/short. After any ABS work, perform a key-off/key-on cycle and re-establish scan-tool communication before rechecking codes — the ABS only re-tests sensors after a key cycle. Wiring should test under 5 ohms with no shorts to power or ground.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd); JustAnswer Jeep tech (wiring test specs)

## C1011
- Description: Left Front Wheel Speed Sensor Signal Erratic Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module
- Diagnostic notes: Signal-quality (erratic) counterpart to C100A's circuit fault. See C100A notes.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1014
- Description: Left Front Wheel Speed Sensor Comparative Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: One wheel-speed reading disagreeing with the other three; tire size mismatch; sensor fault
- Diagnostic notes: Comparative/rationality code — the module compares all four wheel speeds. See C100A notes.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1015
- Description: Right Front Wheel Speed Sensor Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction
- Diagnostic notes: Right-front counterpart of C100A. See C100A notes.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C101C
- Description: Right Front Wheel Speed Sensor Signal Erratic Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module
- Diagnostic notes: See C1011 notes (left-front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C101F
- Description: Right Front Wheel Speed Sensor Comparative Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Wheel-speed disagreement; tire size mismatch; sensor fault
- Diagnostic notes: See C1014 notes (left-front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1020
- Description: Left Rear Wheel Speed Sensor Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction
- Diagnostic notes: Left-rear counterpart of C100A. See C100A notes.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1027
- Description: Left Rear Wheel Speed Sensor Signal Erratic Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module
- Diagnostic notes: See C1011 notes (front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C102A
- Description: Left Rear Wheel Speed Sensor Comparative Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Wheel-speed disagreement; tire size mismatch; sensor fault
- Diagnostic notes: See C1014 notes (front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C102B
- Description: Right Rear Wheel Speed Sensor Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged wiring harness/connectors; noise interference; wheel speed sensor malfunction; ABS module malfunction
- Diagnostic notes: Right-rear counterpart of C100A. See C100A notes.
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1032
- Description: Right Rear Wheel Speed Sensor Signal Erratic Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Tone wheel damage/debris; sensor air gap; wiring intermittent; ABS module
- Diagnostic notes: See C1011 notes (front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1035
- Description: Right Rear Wheel Speed Sensor Comparative Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Wheel-speed disagreement; tire size mismatch; sensor fault
- Diagnostic notes: See C1014 notes (front counterpart).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1041
- Description: Left Front Tone Wheel Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1042
- Description: Right Front Tone Wheel Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1043
- Description: Left Rear Tone Wheel Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1044
- Description: Right Rear Tone Wheel Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Damaged/missing tone-wheel teeth; debris on tone wheel; sensor fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1046
- Description: Left Front Wheel Pressure Phase Monitoring
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: ABS hydraulic control fault; wheel-speed plausibility fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1047
- Description: Right Front Wheel Pressure Phase Monitoring
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: ABS hydraulic control fault; wheel-speed plausibility fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1048
- Description: Left Rear Wheel Pressure Phase Monitoring
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: ABS hydraulic control fault; wheel-speed plausibility fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1049
- Description: Right Rear Wheel Pressure Phase Monitoring
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: ABS hydraulic control fault; wheel-speed plausibility fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1073
- Description: ABS Pump Motor Control Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Pump motor circuit open/shorted; ABS module; TIPM power feed
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1078
- Description: Tire Revolutions Range Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Tire size does not match programmed revolutions; aftermarket tire-size change without PCM/ABS reconfiguration
- Diagnostic notes: Plausibility code on tire revolutions per mile. Documented owner trigger: changing tire size with an aftermarket tuner without updating the vehicle configuration (Power Wagon Registry case also set U1412/U1417/U1418/P1C4E alongside).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd); Power Wagon Registry owner case

## C107C
- Description: Brake Pedal Switch 1/2 Stuck
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake pedal switch stuck; switch misadjustment; wiring
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C107D
- Description: Brake Pedal Switch 1/2 Correlation
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake pedal dual-switch disagreement; switch failure; wiring
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1210
- Description: G Sensor Input Circuit Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Lateral/longitudinal G-sensor fault; wiring; ABS/ESP module
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C1219
- Description: Steering Angle Sensor Erratic Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Steering angle sensor fault; clockspring; wiring; sensor not initialized
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C121A
- Description: Steering Angle Sensor Not Initialized
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Sensor replaced without calibration; alignment work without SAS reset; module replacement
- Diagnostic notes: Requires steering-angle-sensor calibration/initialization procedure after repair (scan tool).
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C121C
- Description: Torque Request Signal Denied
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: ESP/PCM torque-request plausibility fault; CAN communication fault
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C121D
- Description: Brake Pressure Sensor Circuit
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake pressure sensor circuit open/shorted; sensor failure; ABS module
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

## C121E
- Description: Brake Pressure Sensor Comparative Performance
- Category: C
- Scope: manufacturer (Stellantis)
- Possible causes: Brake pressure sensor rationality fault; sensor failure
- Diagnostic notes: not documented beyond description
- Grade: [B]
- Evidence: 2009 Dodge Journey ABS electrical diagnostics index (Mitchell, via scribd)

---

# Stellantis DTC quirks

1. **Key-dance code readout (pre-CAN / PCI-bus era).** Cycle the ignition key On-Off-On-Off-On within 5 seconds; the odometer displays stored P-codes. "P1684 and done" (or just "done") means no real DTCs are present — P1684 alone is just the battery-disconnect status. [B — 2002-2008 Chrysler/Dodge/Jeep code guide]
2. **P1684 is informational.** Battery-disconnected-within-50-starts sets no MIL-worthy fault; it self-clears. Do not diagnose it as a failure. [A]
3. **SKIM start-stall.** P1685 (invalid key) and P1686 (no SKIM message) typically produce crank-then-immediate-stall, not a no-crank. The SKIM and PCM must complete their bus handshake for the engine to keep running. [B]
4. **CCD/PCI vs CAN eras.** P1681/P1694/P1695/P1698 "no CCD/J1850 message" codes are pre-CAN (PCI bus) era; the U11xx/U14xx "lost message / implausible signal" family is the CAN-C/CAN-B/CAN-IHS era equivalent. A scan tool that can address the whole network is required to localize silent modules in both eras. [B]
5. **Chrysler's LDP EVAP system.** The leak-detection-pump EVAP monitor (P1491-P1496 cluster) is distinctive to Chrysler — no other OEM uses this pump design. Aftermarket gas caps that bleed down faster than the Mopar cap are a known false P1494 trigger. [B]
6. **SGW era (2018+).** DTC *reads* still work through the Secure Gateway; only writes (clear, actuations) need authorization. So all codes in this file remain readable on SGW vehicles with any scan tool; clearing them requires AutoAuth/wiTECH. [B — v1.0 database research]
7. **Tire-size changes trigger plausibility codes.** Aftermarket tuner tire-size changes have been observed setting C1078 plus U1412/U1417/U1418 and P1C4E — the modules reject wheel-speed data inconsistent with programmed tire revolutions. [C — owner cases]
8. **ABS key-cycle retest.** After ABS work, always key-off/key-on and re-establish scan-tool communication before rechecking codes — the ABS module only re-tests wheel-speed sensors after a key cycle; stale ATT (at-this-time) codes persist otherwise. [C — Ducati-sourced ABS doc describing the same controller behavior; FCA procedure consistent]

---

# Coverage notes

**Verified and included:** 38 P-codes, 28 U-codes, 8 B-codes (full B1B00-B1B07 driver-squib series), 32 C-codes — 106 DTCs total.

**Ranges NOT verified / systematic gaps:**
- **P1100-P1179, P1200-P1289, P1300-P1389, P1400-P1475, P1500-P1593, P1700-P1718, P1720-P1739, P1741-P1755, P1770-P1898**: no Stellantis-specific definitions confirmed from live sources in this pass; skipped rather than invented.
- **P2xxx manufacturer extensions**: Stellantis P2xxx (mostly diesel/SCR, e.g. P20EE family) not researched — out of scope for this pass.
- **B-codes beyond B1B00-B1B07**: passenger-squib and other ORC codes (B1B08+, B2100-series, B2227) not verified.
- **C-codes beyond the 2009 Journey ABS index**: ABS code definitions vary by ABS supplier (ATE vs Bosch) and model year; the C1xxx list here is Journey-2009 based and should be spot-checked per target vehicle.
- **Newer (2018+, SFD/SGW-era) CAN-FD platform codes**: factory service info is paywalled; U-code behavior on JL/JT/DT platforms not covered.
- **Fiat-specific deviations**: no Fiat-only codes verified; the list is Chrysler/Dodge/Jeep/RAM-weighted.
- **U-codes U110A/U110D/U110F/U1113/U113B/U1149/U1159/U1169/U1170/U1179/U1414/U1415/U1416/U1419-U141C**: descriptions from a single community Wrangler code list; probable causes not documented — graded C, verify on-vehicle.
- **C1000**: description conflict between FCA and Mitsubishi sources — flagged inline, needs per-vehicle confirmation.
- **P1184/P1185**: Cummins-diesel list only; some generic databases map these numbers differently — flagged inline.

**Conflicts reported (not silently resolved):**
1. P1185: Cummins-diesel list = fuel pump temp sensor high; some generic databases map P1185 to engine-oil-temp range — Stellantis diesel context recorded as verified use.
2. P1598: means A/C pressure sensor volts high on Stellantis but turbocharger boost control on Peugeot — same number, different make; this file records the Stellantis definition only.
3. P1698: sources disagree whether the silent module is the PCM or the TCM — recorded as "a powertrain module silent on the CCD bus".
4. C1000: FCA (brake pedal switch 1 circuit performance) vs Mitsubishi (stop lamp switch circuit abnormality) — FCA use recorded with conflict flag.
