# Toyota / Lexus — Manufacturer-Specific DTCs (v1.4.0 expansion)

Research for the M2 OEM vehicle database (v1.4.0). All 175 codes below are NEW —
none of them appear in the v1.2.1 file (`work/dtc-toyota.md`, 108 codes), which is
not duplicated here. Research date: 2026-10-07.

Grading legend (same as v1.2.1): **A** = Toyota/Lexus service manual or TSB
excerpt · **B** = reputable DTC database or multi-source agreement · **C** = single
community source. Unverified items are marked [?].

Scope note: per the research brief, Toyota-context entries are given for selected
codes in the SAE-generic ranges that were explicitly listed as gaps (throttle
P211x/P212x/P2135/P2138, A/F P2195–P2198/P2A00, secondary-air P2440–P2447,
network U0101/U0121–U0142). Those entries carry the Toyota service-manual
detection conditions and sub-codes rather than the bare generic definitions, and
their Scope line says so. Everything else is manufacturer (Toyota).

Toyota quirks (carried over from v1.2.1): DTCs are often printed with a 2-digit
sub-code (e.g. C1377/43, B1900/73, U0121/94) — the 5-character code is the
OBD-II DTC; the sub-code is the Toyota internal detail code [B].

---

## P2111
- Description: Throttle Actuator Control System - Stuck Open
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: throttle actuator; throttle body assembly; throttle valve; ECM; wire harness or connector
- Diagnostic notes: Set when the ECM signals the throttle actuator to close but it stays open (1-trip). Monitor logic: throttle valve remains at a fixed angle despite high drive current (2 A+, 80%+ close duty) with no TP voltage change for 0.5 s. MIL immediate. Confirmation: clear DTCs, start engine, fully depress and release the pedal quickly.
- Grade: [A]
- Evidence: Toyota Tundra/Sequoia SFI service manual excerpts (ttundra.com); 1GR-FE ES-289 excerpt; Toyota Venza service manual — detection condition, monitor strategy, trouble areas agree

## P2112
- Description: Throttle Actuator Control System - Stuck Closed
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: throttle actuator; throttle body assembly; throttle valve; ECM; wire harness or connector
- Diagnostic notes: Mirror of P2111 — ECM signals open, actuator stays closed (2 A+, 80%+ open duty, no TP voltage change, 0.5 s, 1-trip, MIL immediate).
- Grade: [A]
- Evidence: Toyota Tundra SFI / Venza service manual excerpts; zatonevkredit.ru Toyota repair-manual raw pages

## P2118
- Description: Throttle Actuator Control Motor Current Range / Performance
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open in ETCS power source (+BM) circuit; battery; battery terminals; ETCS fuse; ECM
- Diagnostic notes: The ETCS has a dedicated +BM power supply; when it drops below 4 V for 0.8 s+ the ECM calls it an open and cuts current to the throttle actuator. After repair, cycle the ignition off for the ECM to re-allow actuator current.
- Grade: [A]
- Evidence: Toyota Tundra service manual excerpt "Throttle Actuator Control Motor Current Range / Performance (P2118)" (ttundra.com)

## P2120
- Description: Throttle / Pedal Position Sensor / Switch "D" Circuit
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; ECM
- Diagnostic notes: VPA fluctuates rapidly beyond the upper/lower malfunction thresholds for 0.5 s+ (1-trip). Check Accel Sensor Out No.1/No.2 via Techstream (Data List).
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru Toyota repair-manual raw pages; 2UZ-FE RM1113E DI-218

## P2121
- Description: Throttle / Pedal Position Sensor / Switch "D" Circuit Range/Performance
- Category: P
- Scope: generic (SAE); Toyota repair-manual DTC listing documented
- Possible causes: accelerator pedal position sensor assembly; ECM
- Diagnostic notes: Range/performance companion to the P2120 circuit codes. Toyota inspection procedure checks VCPA/VCP2 reference voltage (4.5–5.5 V), then replaces the pedal sensor assembly, then the ECM if the DTC recurs.
- Grade: [B]
- Evidence: Toyota 2TR-FE EFI diagnostics excerpt "DTC P2121 Throttle Position Sensor Guide" (scribd.com); zatonevkredit.ru Toyota hybrid repair-manual DTC list (P2121-106)

## P2122
- Description: Throttle / Pedal Position Sensor / Switch "D" Circuit Low Input
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; open in VCPA circuit; open or ground short in VPA circuit; ECM
- Diagnostic notes: VPA 0.4 V or less for 0.5 s+ (1-trip). MIL on, DTC stored.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages; 2ZR-FAE SFI excerpt (mymitchell.com)

## P2123
- Description: Throttle / Pedal Position Sensor / Switch "D" Circuit High Input
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; open in EPA circuit; ECM
- Diagnostic notes: VPA 4.8 V or more for 2.0 s+ (1-trip). MIL on, DTC stored.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages

## P2125
- Description: Throttle / Pedal Position Sensor / Switch "E" Circuit
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; ECM
- Diagnostic notes: VPA2 fluctuates rapidly beyond thresholds for 0.5 s+ (1-trip) — the "E"/No.2 channel mirror of P2120.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages

## P2126
- Description: Throttle / Pedal Position Sensor / Switch "E" Circuit Range/Performance
- Category: P
- Scope: generic (SAE); Toyota repair-manual DTC listing documented
- Possible causes: accelerator pedal sensor assembly; ECM
- Diagnostic notes: Range/performance companion to P2125; see P2121 diagnostic note for the Toyota inspection sequence.
- Grade: [B]
- Evidence: zatonevkredit.ru Toyota hybrid repair-manual DTC list (P2126-109); SAE J2012 title pattern

## P2127
- Description: Throttle / Pedal Position Sensor / Switch "E" Circuit Low Input
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; open in VCP2 circuit; open or ground short in VPA2 circuit; ECM
- Diagnostic notes: VPA2 1.2 V or less for 0.5 s+ (1-trip). MIL on, DTC stored.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages

## P2128
- Description: Throttle / Pedal Position Sensor / Switch "E" Circuit High Input
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: accelerator pedal sensor assembly; open in EPA2 circuit; ECM
- Diagnostic notes: Both conditions for 2.0 s+ (1-trip): (a) VPA2 4.8 V or more, (b) VPA between 0.4 V and 3.45 V.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages

## P2135
- Description: Throttle / Pedal Position Sensor / Switch "A" / "B" Voltage Correlation
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: short between VTA1 and VTA2 circuits; throttle position sensor (built into throttle body with motor assembly); ECM
- Diagnostic notes: Correlation code for the two TP sensors in the throttle body. Set when (a) VTA1–VTA2 differ by 0.02 V or less for 0.5 s+, or (b) VTA1 is 0.2 V or less and VTA2 is 1.75 V or less for 0.4 s+ (1-trip). Check Throttle Position No.1/No.2 via Techstream — normal: No.1 0.5–1.1 V released / 3.2–4.8 V depressed; No.2 2.1–3.1 V released / 4.6–4.98 V depressed.
- Grade: [A]
- Evidence: Toyota Tundra SFI / 4Runner 1GR-FE / Venza service manual excerpts (ttundra.com, trail4runner.com, tovenza.com); zatonevkredit.ru repair-manual raw pages — detection conditions and reference voltages agree

## P2138
- Description: Throttle / Pedal Position Sensor / Switch "D" / "E" Voltage Correlation
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: short between VPA and VPA2 circuits; accelerator pedal sensor assembly; ECM
- Diagnostic notes: APP-sensor correlation companion to P2135. Set when (a) |VPA − VPA2| is 0.02 V or less, or (b) VPA is 0.4 V or less and VPA2 is 1.2 V or less, for 2.0 s+ (1-trip). Check Accel Sensor Out No.1/No.2 via Techstream.
- Grade: [A]
- Evidence: Toyota Tundra SFI service manual; zatonevkredit.ru repair-manual raw pages; 2UZ-FE RM1113E DI-220

## P2195
- Description: Oxygen (A/F) Sensor Signal Stuck Lean (Bank 1 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open or short in A/F sensor (Bank 1 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM
- Diagnostic notes: Two monitors: (1) voltage — A/F voltage above 3.8 V (very lean) while HO2 sensor rises from below 0.21 V to 0.59 V+ for 5 s; (2) current — during fuel-cut, A/F current 3.6 mA or more for 3 s cumulative (high-side stuck). Use the A/F CONTROL active test to graph A/F vs HO2 response; P2A00 may set alongside.
- Grade: [A]
- Evidence: Toyota SFI repair-manual excerpts via zatonevkredit.ru; 1GR-FE EFI manual (toyotamanuals.gitlab.io); 2AZ-FE SFI manual (aurion.serve.rip) — monitor descriptions and thresholds agree

## P2196
- Description: Oxygen (A/F) Sensor Signal Stuck Rich (Bank 1 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open or short in A/F sensor (Bank 1 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM
- Diagnostic notes: Mirror of P2195: A/F voltage below 2.8 V (very rich) while HO2 falls from 0.59 V+ to below 0.21 V for 5 s, or fuel-cut A/F current below ~1.0 mA for 3 s cumulative (low-side stuck). 2-trip logic.
- Grade: [A]
- Evidence: Toyota SFI repair-manual excerpts via zatonevkredit.ru (P2195/P2196 DTC table with trouble areas)

## P2197
- Description: Oxygen (A/F) Sensor Signal Stuck Lean (Bank 2 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open or short in A/F sensor (Bank 2 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM
- Diagnostic notes: Bank 2 mirror of P2195. On Toyota V-engines Bank 2 is the bank containing cylinder No. 2.
- Grade: [A]
- Evidence: 1GR-FE EFI service manual (toyotamanuals.gitlab.io) — P2195/P2197 and P2196/P2198 paired tables

## P2198
- Description: Oxygen (A/F) Sensor Signal Stuck Rich (Bank 2 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open or short in A/F sensor (Bank 2 Sensor 1) circuit; A/F sensor; intake system; fuel pressure; fuel injector assembly; ECM
- Diagnostic notes: Bank 2 mirror of P2196.
- Grade: [A]
- Evidence: 1GR-FE EFI service manual (toyotamanuals.gitlab.io)

## P2A00
- Description: A/F Sensor Circuit Slow Response (Bank 1 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: open or short in A/F sensor circuit; A/F sensor; A/F sensor heater; EFI main relay; air induction system; fuel pressure; injector; ECM
- Diagnostic notes: After warm-up the ECM runs active A/F control (~10 s), forcing injection volume up/down around stoichiometry and measuring the A/F sensor response rate; if the deterioration level is below threshold the DTC sets. Confirmation: check Mode 06 O2-sensor monitor data via Techstream. Although the title says "oxygen sensor", on Toyota this is the wideband A/F sensor.
- Grade: [A]
- Evidence: Toyota Camry/Sequoia/Venza/Tacoma service manuals (charm.li, 4 separate models agree); 2003 Tacoma RM1002U DI-198 excerpt (ww.jackmd.com)

## P2A03
- Description: A/F Sensor Circuit Slow Response (Bank 2 Sensor 1)
- Category: P
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: not documented (same family as P2A00)
- Diagnostic notes: Bank 2 companion to P2A00 — see P2A00 notes. Listed alongside P2A00 in the Toyota SFI charts.
- Grade: [A]
- Evidence: Toyota Camry 2GR-FE / Sequoia 3UR-FBE service manuals (charm.li) — P2A00/P2A03 paired

## P2440
- Description: Secondary Air Injection System Switching Valve Stuck Open (Bank 1)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air switching valve stuck open (carbon buildup, debris from disintegrated air-pump filter foam or impeller blades, moisture); air injection pump
- Diagnostic notes: Toyota/Lexus secondary-air systems are a known failure family. A Toyota TSB (2005–2009 2UZ-FE 4.7L) attributes these codes to debris passing through the air pump contaminating the valves — inspect pump, hoses and bypass valve; replacement typically covers pump + hoses + valve assembly. Field check: pull the hose, start the engine — exhaust at the valve port means the valve is stuck open.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com secondary-air code guides (agree); JustAnswer Toyota TSB excerpt (P1441/P1442/P1444/P1445/P2440/P2441 debris cause)

## P2441
- Description: Secondary Air Injection System Switching Valve Stuck Closed (Bank 1)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air switching valve stuck closed (carbon, debris); air injection pump
- Diagnostic notes: See P2440 — same TSB/debris context. Bypass-harness field fixes target this family but defeat an emissions monitor; not recommended as a repair.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com guides; JustAnswer Toyota TSB excerpt

## P2442
- Description: Secondary Air Injection System Switching Valve Stuck Open (Bank 2)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air switching valve stuck open (carbon, debris, moisture); air injection pump
- Diagnostic notes: Bank 2 mirror of P2440.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com guides

## P2443
- Description: Secondary Air Injection System Switching Valve Stuck Closed (Bank 2)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air switching valve stuck closed (carbon, debris); air injection pump
- Diagnostic notes: Bank 2 mirror of P2441.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com guides

## P2444
- Description: Secondary Air Injection System Pump Stuck ON (Bank 1)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air injection pump relay stuck; pump control circuit fault
- Diagnostic notes: Pump-side companion to the valve codes — the pump runs when it should be off. Not individually enumerated in the forum guides; definition follows the SAE J2012 P244x pattern (P2445/P2447 stuck-OFF are documented there).
- Grade: [B]
- Evidence: SAE J2012 P244x pattern; 4runners.com / tacomaworld.com guides (stuck-OFF siblings)

## P2445
- Description: Secondary Air Injection System Pump Stuck OFF (Bank 1)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: failed air injection pump; pump relay/circuit open; debris-seized pump
- Diagnostic notes: See P2440 — pump failures in this family commonly trace to the disintegrating internal foam filter.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com guides

## P2446
- Description: Secondary Air Injection System Pump Stuck ON (Bank 2)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: air injection pump relay stuck; pump control circuit fault
- Diagnostic notes: Bank 2 mirror of P2444 — see P2444 note.
- Grade: [B]
- Evidence: SAE J2012 P244x pattern; 4runners.com / tacomaworld.com guides (stuck-OFF siblings)

## P2447
- Description: Secondary Air Injection System Pump Stuck OFF (Bank 2)
- Category: P
- Scope: generic (SAE range); Toyota-context documented
- Possible causes: failed air injection pump; pump relay/circuit open
- Diagnostic notes: Bank 2 mirror of P2445.
- Grade: [B]
- Evidence: 4runners.com / tacomaworld.com / tundras.com guides

## P3000
- Description: High Voltage Battery Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3001
- Description: High Voltage Battery ECU Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: NOTE — the source list gives both P3001 and P3100 as "High Voltage Battery ECU Fault" and P3105/P3109 as battery-ECU communication faults; the distinctions are the source's, not independently verified.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3002
- Description: High Voltage Battery ECU Communication Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: wire harness; battery ECU
- Diagnostic notes: A Toyota master technician (JustAnswer) describes the P3105-family symptom as communication failure between the battery ECU (inside the HV battery case) and the HV ECU (under the passenger footrest) — check connectors and harness before condemning either ECU.
- Grade: [B]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com); JustAnswer Toyota master-technician thread (2002 Prius P3105)

## P3004
- Description: High Voltage Power Cable Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3005
- Description: High Voltage Fuse Blown
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3006
- Description: High Voltage Battery State Of Charge Uneven
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3009
- Description: High Voltage Leak Detected
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: High-voltage insulation/leak fault — hybrid models only. Treat as a safety-relevant code; do not probe HV circuits without training and PPE.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3011
- Description: High Voltage Battery Module 1 Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: P3011 through P3029 map to HV battery modules/blocks 1 through 19 (per the source list); only P3011 is entered here as the range representative — do not invent per-module entries.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3030
- Description: High Voltage Battery Monitor Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3060
- Description: High Voltage Battery Temperature Sensor or Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3076
- Description: High Voltage Battery Cooling Fan Abnormal Air Flow
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3077
- Description: High Voltage Battery Cooling Fan Motor or Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3100
- Description: High Voltage Battery ECU Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P3001 note — the source lists both P3001 and P3100 with this description; distinction unverified.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3101
- Description: Engine System Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Seen on Gen 1 Prius alongside P3191 (engine does not start); owner threads pair it with no-start diagnosis (fuel, spark, MAF).
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com); priuschat.com 2003 Prius P3191/P3101 thread

## P3105
- Description: High Voltage Battery ECU or Communication Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: wire harness; battery ECU
- Diagnostic notes: See P3002 — battery ECU ↔ HV ECU communication failure; reseat connectors, check harness continuity.
- Grade: [B]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com); JustAnswer Toyota master-technician thread

## P3106
- Description: Engine ECM or Communication Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3107
- Description: Air Bag ECU or Communication Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Hybrid-vehicle-control view of an SRS ECU communication fault — check SRS codes as well.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3108
- Description: A/C Amplifier ECU or Communication Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3109
- Description: High Voltage Battery ECU or Communication Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See P3105 note — source lists both P3105 and P3109 with this description; distinction unverified.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3110
- Description: HV IGCT Relay or Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3115
- Description: Hybrid System Main Relay Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: System main relay (SMR) circuit — hybrid models only.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3120
- Description: High Voltage Transaxle Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: An ATSG technical bulletin reproduces a scan tool showing "P3120 HV transaxle assy malfunction" set in the HV ECU with the master warning lamp on and READY on; information sub-codes narrow it to resolver/MG data — read the INF codes before condemning the transaxle.
- Grade: [B]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com); ATSG bulletin 17-07 (Gen-1 Prius misleading-DTCs article)

## P3125
- Description: Converter & Inverter Assembly Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: +B short in DC/DC converter NODD wiring; DC/DC converter malfunction; open or ground short in DC/DC converter NODD wiring; converter & inverter assembly; wire harness
- Diagnostic notes: From the 2002 Prius repair manual (RM883U DI-271): the HV ECU monitors DC/DC converter operation because a failed converter drains the auxiliary battery until the car cannot keep driving. Information codes 263/264/265 narrow it (263: +B short in NODD wiring; 264: converter malfunction; 265: open/GND short in NODD wiring). NOTE: a Toyota TSB advises that if P3125 is present due to P3130, do not diagnose P3125 — fix the inverter cooling fault first.
- Grade: [B]
- Evidence: Toyota Prius RM883U DTC P3125 excerpt (via yumpu.com); JustAnswer Toyota TSB excerpt (P3130→P3125 relationship)

## P3130
- Description: Inverter Cooling System Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: inverter coolant pump (electric water pump) failure; coolant flow blockage/kinked hoses; low coolant
- Diagnostic notes: Snap-on SureTrack documented case (2001 Prius): inverter temperature exceeded range with clean full coolant — no circulation at the reservoir despite voltage at the pump; replacing the electric water pump fixed it. A Toyota TSB covers P3130+P3125 together: check inverter-reservoir water flow first; if P3125 is present due to P3130, ignore P3125.
- Grade: [B]
- Evidence: garagewire.co.uk SureTrack real-fix article; JustAnswer Toyota TSB excerpt; "Toyota Prius OBDII Fault Code Guide" (scribd.com)

## P3135
- Description: High Voltage Circuit Breaker Sensor Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3140
- Description: Interlock Malfunction
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: service plug not installed correctly (handle not flipped up, bent/broken microswitch tab); inverter terminal cover or sensor cover removed; open in interlock signal circuit
- Diagnostic notes: From the 2002 Prius repair manual (RM883U): the HV ECU shuts down the system main relay if it detects safety-device operation (service plug removal, inverter terminal cover, sensor cover) while the vehicle is stopped (INF 350); an open in the interlock signal circuit while running sets INF 351 without shutting down HV. PriusChat field reports confirm the service-plug microswitch as the common cause — the code returns immediately at key-on until the switch closes.
- Grade: [A]
- Evidence: Toyota Prius RM883U DTC P3140 excerpt (via scribd.com); priuschat.com P3140 thread (INF 350, service-plug microswitch)

## P3145
- Description: Vehicle Speed Sensor or Circuit Fault
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Hybrid-vehicle-control view of a vehicle speed sensor fault.
- Grade: [C]
- Evidence: "Toyota Prius OBDII Fault Code Guide" (scribd.com, single community transcription)

## P3193
- Description: Fuel Run Out
- Category: P
- Scope: manufacturer (Toyota)
- Possible causes: out of fuel; ECM
- Diagnostic notes: Set when the fuel-low-level signal is input to the ECM AND the P3190/P3191 detection condition is satisfied (1-trip). Hybrid note: running out of fuel forces the car onto battery-only operation, deep-discharging the HV battery — refuel and recharge promptly.
- Grade: [A]
- Evidence: Toyota repair-manual DTC P3190/P3191/P3193 excerpt via zatonevkredit.ru (detection condition + trouble areas); ALLDATA 2007 Prius P3191 article (via scribd.com) confirms the P3190/P3191/P3193 family

---

## B1100
- Description: Airbag Sensor Assembly Center Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: airbag sensor assembly center (internal malfunction)
- Diagnostic notes: Recorded when the airbag sensor assembly center detects its own internal malfunction (sub-code /31 on 2004 Corolla). Manual hint: if any other SRS code is present at the same time, repair the other code FIRST. Inspection starts with IG2 supply voltage (10–14 V) — check battery/charging system if out of range. Disconnect battery and wait 90+ seconds before probing SRS circuits.
- Grade: [A]
- Evidence: 2004 Corolla repair manual RM1037U SRS diagnostics (via scribd.com and library.tokaintanda.com); JustAnswer Toyota thread confirms B1100 = airbag sensor assembly center

## B1135
- Description: Half Connection Detection Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: CONFLICT — make-dependent meaning. On Toyota (2004 Corolla RM1037U SRS chart, B1135/24) this is "HALF CONNECTION DETECTION MALFUNCTION" (connector half-connection detection) [A]. On Nissan (2014 Cube SRS manual) B1135 is "SIDE AIR BAG MODULE LH [VB-SHORT]" [B]. Do not cross-apply.
- Grade: [A]
- Evidence: 2004 Corolla RM1037U SRS DTC chart (via scribd.com); conflict from Nissan Cube SRS manual (via scribd.com)

## B1140
- Description: Side Airbag Sensor Assembly RH Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: side airbag sensor assembly RH; airbag sensor assembly center; instrument panel wire No.3
- Diagnostic notes: Satellite side-impact sensor (RH) internal malfunction (sub-code /32 on 2004 Corolla).
- Grade: [A]
- Evidence: 2004 Corolla RM1037U SRS DTC chart (via scribd.com)

## B1141
- Description: Side Airbag Sensor Assembly LH Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: side airbag sensor assembly LH; airbag sensor assembly center; instrument panel wire No.3
- Diagnostic notes: Satellite side-impact sensor (LH) internal malfunction (sub-code /33 on 2004 Corolla).
- Grade: [A]
- Evidence: 2004 Corolla RM1037U SRS DTC chart (via scribd.com)

## B1150
- Description: Occupant Classification ECU Circuit Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: occupant classification ECU; FSR+/FSR- sensor circuit (open/short to ground or to B+); wire harness
- Diagnostic notes: From the 2005 4Runner repair manual (RM1165U) CI B1150/23 diagnostics: check FSR+ to FSR- isolation (1 MΩ or higher), then FSR lines to body ground (below 1 V with ignition ON). Occupant-classification (passenger weight-sensor) circuit.
- Grade: [A]
- Evidence: 2005 4Runner repair manual RM1165U SRS diagnostics (via toyota-4runner.org)

## B1153
- Description: Seat Position Airbag Sensor Assembly Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: seat position airbag sensor; airbag sensor assembly center; instrument panel wire No.3; wire harness (seat position airbag sensor – front seat inner belt assembly)
- Diagnostic notes: Seat-track position sensor used for dual-stage deployment decisions (sub-code /25 on 2004 Corolla).
- Grade: [A]
- Evidence: 2004 Corolla RM1037U SRS DTC chart (via scribd.com)

## B1180
- Description: Short in D Squib (2nd Step) Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: horn button assembly (D squib 2nd step); spiral cable sub-assembly; airbag sensor assembly center; instrument panel wire
- Diagnostic notes: Driver airbag 2nd-stage squib line short (sub-code /17). A Toyota technician (JustAnswer) notes the clockspring (spiral cable) is the most common cause; airbag sensor and wiring are the other candidates. B1181 (dedup) is the open-circuit sibling; B1182 is the short-to-ground sibling.
- Grade: [B]
- Evidence: Toyota SRS DTC chart sequence B1180/17–B1182/19 (via scribd.com); JustAnswer Toyota technician thread (2004 4Runner B1180)

## B1182
- Description: Short to GND in D Squib (2nd Step) Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: horn button assembly (D squib 2nd step); spiral cable sub-assembly; airbag sensor assembly center; instrument panel wire
- Diagnostic notes: Third member of the chart sequence B1180/17 (short), B1181/18 (open), B1182/19 (short to ground) — driver 2nd-stage squib. Individual detection-item text not captured beyond the sequence; the short/open/GND/B+ 4-code pattern is the Toyota SRS convention.
- Grade: [B]
- Evidence: Toyota SRS DTC chart sequence B1180/17–B1182/19 (via scribd.com)

## B1771
- Description: Occupant Detection Malfunction
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Seen on a Techstream readout alongside B1801/B1811 after steering/column work (listed as "Occupation Detection" in the owner transcription — likely "Occupant Detection"). Occupant-classification system area.
- Grade: [C]
- Evidence: yarisworld.com forum Techstream readout (single community thread)

## B1800
- Description: Short in Driver Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly
- Diagnostic notes: Set when the airbag sensor assembly receives a line-short signal 5 times in the driver squib circuit during the primary check (sub-code /51). Disconnect battery, wait 90+ seconds before probing. A failed clockspring is the classic cause.
- Grade: [A]
- Evidence: Toyota service-manual DTC B1800/51–B1803/51 excerpts via zatonevkredit.ru and toyotaspace.com (detection conditions + trouble areas); jdmfsm.info 05-1038 excerpt

## B1801
- Description: Open in Driver Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly
- Diagnostic notes: Open signal received for 2 seconds (sub-code /51). A Toyota master technician (JustAnswer, Hilux B1801) identifies the spiral cable under the steering wheel as the recognized failure point; the wheel must come off to replace it.
- Grade: [A]
- Evidence: Toyota service-manual excerpts via zatonevkredit.ru, toyotaspace.com; 2004 Prius RM1075U B1801/51 procedure (via scribd.com); JustAnswer Toyota master-tech thread

## B1802
- Description: Short to GND in Driver Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly
- Diagnostic notes: Short-to-ground signal received for 0.5 seconds (sub-code /51).
- Grade: [A]
- Evidence: Toyota service-manual DTC B1800/51–B1803/51 excerpts via zatonevkredit.ru and toyotaspace.com

## B1803
- Description: Short to B+ in Driver Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib); airbag sensor assembly
- Diagnostic notes: Short-to-B+ signal received for 0.5 seconds (sub-code /51).
- Grade: [A]
- Evidence: Toyota service-manual DTC B1800/51–B1803/51 excerpts via zatonevkredit.ru and toyotaspace.com

## B1805
- Description: Short in Front Passenger Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly
- Diagnostic notes: Line short detected during the primary check (sub-code /52). Passenger-dash airbag squib.
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1805/52–B1808/52 excerpts via zatonevkredit.ru (detection conditions + trouble areas); arendaavto-sochi.ru Toyota SRS table agrees

## B1806
- Description: Open in Front Passenger Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly
- Diagnostic notes: Open detected in the passenger squib circuit (sub-code /52). A Yaris owner thread shows this presenting as "open circuit in passenger front squib" — check for anything disconnected under/around the passenger dash and seat.
- Grade: [A]
- Evidence: Toyota repair-manual excerpts via zatonevkredit.ru; yarisworld.com B1806 thread

## B1807
- Description: Short to GND in Front Passenger Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly
- Diagnostic notes: Short-to-ground detected (sub-code /52).
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1805/52–B1808/52 excerpts via zatonevkredit.ru

## B1808
- Description: Short to B+ in Front Passenger Side Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 2 instrument panel wire; front passenger side squib (instrument panel passenger airbag assembly); airbag ECU assembly
- Diagnostic notes: Short-to-B+ detected (sub-code /52).
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1805/52–B1808/52 excerpts via zatonevkredit.ru

## B1810
- Description: Short in Driver Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Driver dual-stage airbag 2nd-step squib (sub-code /53). NOTE — generic B-body databases (ecutesting.com, retrolib.info) list B1810–B1813 as lamp/wiper circuits; those are non-Toyota body-control definitions. On Toyota these are SRS squib circuits per the Toyota service-manual DTC charts — do not cross-apply.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts (tovenza.com, to4runner.net, ttguide.net); Toyota repair-manual excerpts via zatonevkredit.ru (trouble areas)

## B1811
- Description: Open in Driver Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Open in the driver 2nd-step squib circuit (sub-code /53). A Yaris owner thread defines it as "Open in D squib (Dual stage - 2nd step) circuit" and notes the code cannot be cleared until the underlying open is repaired. See B1810 cross-apply warning.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table; yarisworld.com owner thread

## B1812
- Description: Short to GND in Driver Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Short-to-ground in the driver 2nd-step squib circuit (sub-code /53). See B1810 cross-apply warning.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1813
- Description: Short to B+ in Driver Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; spiral cable (with sensor) sub-assembly; horn button assembly / steering pad (driver side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Short-to-B+ in the driver 2nd-step squib circuit (sub-code /53). See B1810 cross-apply warning.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1815
- Description: Short in Front Passenger Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Passenger dual-stage airbag 2nd-step squib (sub-code /54).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1816
- Description: Open in Front Passenger Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Open in the passenger 2nd-step squib circuit (sub-code /54).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1817
- Description: Short to GND in Front Passenger Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Short-to-ground in the passenger 2nd-step squib circuit (sub-code /54).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1818
- Description: Short to B+ in Front Passenger Side Squib 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: instrument panel wire; No. 3 instrument panel wire; instrument panel passenger airbag assembly (front passenger side squib 2nd step); airbag sensor assembly
- Diagnostic notes: Short-to-B+ in the passenger 2nd-step squib circuit (sub-code /54).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B181A
- Description: Short in Passenger Side Airbag Variable Vent Hole Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Hex-digit DTC (B181A–B181D) for the passenger airbag variable-vent-hole squib, from the Toyota Venza/4Runner/Tacoma airbag DTC charts (check-mode *2). Trouble areas not captured in the excerpts.
- Grade: [B]
- Evidence: Toyota Venza airbag-system DTC chart (tovenza.com); Toyota 4Runner DTC chart (to4runner.net); Toyota Tacoma DTC chart (ttguide.net)

## B181B
- Description: Open in Passenger Side Airbag Variable Vent Hole Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B181A.
- Grade: [B]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B181C
- Description: Short to GND in Passenger Side Airbag Variable Vent Hole Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B181A.
- Grade: [B]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B181D
- Description: Short to B+ in Passenger Side Airbag Variable Vent Hole Squib Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B181A.
- Grade: [B]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B1820
- Description: Short in Side Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly
- Diagnostic notes: RH seat side-airbag squib (sub-code /55). Older manuals phrase it as "Side Squib (D Seat Side)" — D = driver side on LHD vehicles.
- Grade: [A]
- Evidence: Toyota airbag-system DTC charts (tovenza.com, to4runner.net, ttguide.net); zatonevkredit.ru trouble-area table; toyotamanuals.gitlab.io 05-144 excerpt

## B1821
- Description: Open in Side Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: floor wire / No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly; seat-harness chafing under the seat
- Diagnostic notes: Toyota TSB EL002-08 (revised 2008) specifically covers DTC B1821/B1826 "OPEN SIDE SQUIB CIRCUIT" — SRS light on; the repair procedure addresses the seat side-airbag harness (harness chafing/pinching under the front seats). Check the seat harness routing before condemning the squib.
- Grade: [A]
- Evidence: Toyota airbag-system DTC charts; Toyota TSB EL002-08 via media.fixed-ops.com; JustAnswer Toyota thread (2006 Camry B1821/55)

## B1822
- Description: Short to GND in Side Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly
- Diagnostic notes: Short-to-ground in the RH side squib circuit (sub-code /55).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1823
- Description: Short to B+ in Side Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: No. 2 floor wire; front seat airbag assembly RH (side squib RH); airbag sensor assembly
- Diagnostic notes: Short-to-B+ in the RH side squib circuit (sub-code /55).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1825
- Description: Short in Side Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly
- Diagnostic notes: LH seat side-airbag squib (sub-code /56).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1826
- Description: Open in Side Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly; seat-harness chafing under the seat
- Diagnostic notes: Covered by Toyota TSB EL002-08 alongside B1821 — see B1821 notes.
- Grade: [A]
- Evidence: Toyota airbag-system DTC charts; Toyota TSB EL002-08 via media.fixed-ops.com

## B1827
- Description: Short to GND in Side Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly
- Diagnostic notes: Short-to-ground in the LH side squib circuit (sub-code /56).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1828
- Description: Short to B+ in Side Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: floor wire; front seat airbag assembly LH (side squib LH); airbag sensor assembly
- Diagnostic notes: Short-to-B+ in the LH side squib circuit (sub-code /56).
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts; zatonevkredit.ru trouble-area table

## B1830
- Description: Short in Curtain Shield Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: RH roof curtain-shield airbag squib (sub-code /57). Trouble areas not captured in the excerpts.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts (detection items)

## B1831
- Description: Open in Curtain Shield Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1830.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B1832
- Description: Short to GND in Curtain Shield Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1830.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B1833
- Description: Short to B+ in Curtain Shield Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1830.
- Grade: [A]
- Evidence: Toyota Venza/4Runner/Tacoma airbag-system DTC charts

## B1835
- Description: Short in Curtain Shield Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: LH roof curtain-shield airbag squib (sub-code /58).
- Grade: [A]
- Evidence: Toyota 4Runner airbag-system DTC chart (to4runner.net); zatonevkredit.ru chart excerpt

## B1836
- Description: Open in Curtain Shield Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1835.
- Grade: [A]
- Evidence: Toyota 4Runner airbag-system DTC chart (to4runner.net); zatonevkredit.ru chart excerpt

## B1837
- Description: Short to GND in Curtain Shield Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1835.
- Grade: [A]
- Evidence: Toyota 4Runner airbag-system DTC chart (to4runner.net); zatonevkredit.ru chart excerpt

## B1838
- Description: Short to B+ in Curtain Shield Squib LH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1835.
- Grade: [A]
- Evidence: Toyota 4Runner airbag-system DTC chart (to4runner.net); zatonevkredit.ru chart excerpt

## B1840
- Description: Short in Curtain Shield Squib RH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: RH curtain-shield 2nd-step squib (sub-code /59). Trouble areas not captured in the excerpts.
- Grade: [A]
- Evidence: zatonevkredit.ru Toyota airbag-system DTC chart (detection items B1840/59–B1843/59)

## B1841
- Description: Open in Curtain Shield Squib RH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1840.
- Grade: [A]
- Evidence: zatonevkredit.ru Toyota airbag-system DTC chart

## B1842
- Description: Short to GND in Curtain Shield Squib RH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1840.
- Grade: [A]
- Evidence: zatonevkredit.ru Toyota airbag-system DTC chart

## B1843
- Description: Short to B+ in Curtain Shield Squib RH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: See B1840.
- Grade: [A]
- Evidence: zatonevkredit.ru Toyota airbag-system DTC chart

## B1845
- Description: Short in Curtain Shield Squib LH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: LH curtain-shield 2nd-step squib (sub-code /61). B1845 confirmed in the chart; B1846/B1847/B1848 follow the standard short/open/GND/B+ 4-code pattern but their individual detection-item rows were not captured in the excerpt.
- Grade: [B]
- Evidence: zatonevkredit.ru Toyota airbag-system DTC chart (B1845/61 confirmed)

## B1846
- Description: Open in Curtain Shield Squib LH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Pattern-inferred sibling of B1845 — see B1845 note.
- Grade: [C]
- Evidence: Toyota SRS 4-code squib pattern (B1845/61 anchor from zatonevkredit.ru chart)

## B1847
- Description: Short to GND in Curtain Shield Squib LH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Pattern-inferred sibling of B1845 — see B1845 note.
- Grade: [C]
- Evidence: Toyota SRS 4-code squib pattern (B1845/61 anchor from zatonevkredit.ru chart)

## B1848
- Description: Short to B+ in Curtain Shield Squib LH 2nd Step Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Pattern-inferred sibling of B1845 — see B1845 note.
- Grade: [C]
- Evidence: Toyota SRS 4-code squib pattern (B1845/61 anchor from zatonevkredit.ru chart)

## B1900
- Description: Short in Front Pretensioner Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: shorted seatbelt pretensioner wiring (melted/chafed insulation near the connector); front seat outer belt assembly RH (pretensioner squib); airbag sensor assembly
- Diagnostic notes: RH seatbelt pretensioner squib (sub-code /73 — shared across B1900–B1903; the SRS warning light blink code alone cannot distinguish them, use a scan tool). A Yaris field thread found melted pretensioner-wire insulation a few inches from the connector with the exposed conductors touching — inspect the yellow / yellow-black pair end to end.
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1900/73–B1903/73 excerpt via zatonevkredit.ru; yarisworld.com B1900 field thread

## B1902
- Description: Short to GND in Front Pretensioner Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: shorted seatbelt pretensioner wiring; front seat outer belt assembly RH; airbag sensor assembly
- Diagnostic notes: See B1900 — sub-code /73 family.
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1900/73–B1903/73 excerpt via zatonevkredit.ru

## B1903
- Description: Short to B+ in Front Pretensioner Squib RH Circuit
- Category: B
- Scope: manufacturer (Toyota)
- Possible causes: shorted seatbelt pretensioner wiring; front seat outer belt assembly RH; airbag sensor assembly
- Diagnostic notes: See B1900 — sub-code /73 family. (B1901, the open-circuit sibling, is in the v1.2.1 file.)
- Grade: [A]
- Evidence: Toyota repair-manual DTC B1900/73–B1903/73 excerpt via zatonevkredit.ru

---

## C1202
- Description: Brake Fluid Level Low / Open Circuit in Brake Fluid Level Warning Switch Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake fluid level; brake fluid level warning switch; harness and connector; skid control ECU; ABS No.1 relay; ABS No.2 relay
- Diagnostic notes: Check the reservoir level first — the code covers both genuinely low fluid and an open in the warning-switch circuit (sub-code /68 on Prius).
- Grade: [A]
- Evidence: Prius repair manual RM1076E electronically controlled brake system chart (via toyotamanuals.gitlab.io)

## C1233
- Description: VSC Controller Power Line Fault
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: A single community source describes C1233 as a short or break in the power line of the VSC controller; no Toyota chart excerpt was found for it in this pass.
- Grade: [C]
- Evidence: scribd.com Toyota DTC fault-codes guide (single community source)

## C1235
- Description: Foreign Matter on Front Speed Sensor RH Tip / Abnormal Pulse Waveform (FR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: right front speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU
- Diagnostic notes: Set when the speed-sensor pulse waveform is abnormal for 5 s+ at 20 km/h (12 mph) or more (sub-code /35 on Prius). The chart also lists foreign matter on the sensor tip as a cause.
- Grade: [A]
- Evidence: Prius repair manual RM1076E electronically controlled brake system chart (via toyotamanuals.gitlab.io)

## C1236
- Description: Foreign Matter on Front Speed Sensor LH Tip / Abnormal Pulse Waveform (FL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: left front speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU
- Diagnostic notes: Left-front mirror of C1235 (sub-code /36). NOTE: C1237 was not confirmed in the excerpts — do not assume it exists.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1238
- Description: Foreign Matter on Rear Speed Sensor RH Tip / Abnormal Pulse Waveform (RR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: right rear speed sensor; speed sensor circuit; sensor installation; skid control ECU
- Diagnostic notes: Right-rear mirror of C1235 (sub-code /38, detailed code 304).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1239
- Description: Foreign Matter on Rear Speed Sensor LH Tip / Abnormal Pulse Waveform (RL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: left rear speed sensor; speed sensor circuit; sensor installation; sensor rotor; skid control ECU
- Diagnostic notes: Left-rear mirror of C1235 (sub-code /39, detailed code 305).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1243
- Description: Malfunction in Deceleration Sensor (Constant Output)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit)
- Diagnostic notes: From the Kluger/Highlander ABS-VSC chart (05-288): constant-output malfunction of the deceleration sensor (sub-code /43). Fail-safe: the ECU cuts current to the ABS solenoid relay and prohibits ABS control — the brake system reverts to normal (non-ABS) braking.
- Grade: [A]
- Evidence: Toyota Kluger diagnostic trouble code chart 0542Q-07 (via toyotamanuals.gitlab.io); 2UZ-FE-era DI-347 excerpt (via toyotamanuals.gitlab.io)

## C1244
- Description: Malfunction in Deceleration Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit)
- Diagnostic notes: General deceleration-sensor malfunction (sub-code /44) — see C1243 fail-safe note.
- Grade: [A]
- Evidence: Toyota Kluger diagnostic trouble code chart 0542Q-07 (via toyotamanuals.gitlab.io)

## C1245
- Description: Malfunction in Deceleration Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: yaw rate sensor (deceleration sensor); yaw rate sensor circuit (deceleration sensor circuit)
- Diagnostic notes: Set when, at 30 km/h+, the difference between the acceleration/deceleration values computed from the deceleration sensor and from vehicle speed exceeds 0.35 G for 60 s+ (sub-code /45). Fail-safe per C1243.
- Grade: [A]
- Evidence: Toyota DI-347 deceleration-sensor excerpt (via toyotamanuals.gitlab.io); Kluger DTC chart

## C1246
- Description: Malfunction in Master Cylinder Pressure Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake pedal stroke sensor
- Diagnostic notes: Prius ECB brake system (sub-code /46). Do not confuse with C1364 (W/C pressure sensor).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1247
- Description: Malfunction in Stroke Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector
- Diagnostic notes: Brake pedal stroke sensor (sub-code /47, Prius ECB).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1251
- Description: Open in Pump Motor Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: wire harness; ABS and traction actuator
- Diagnostic notes: The brake-control VSC chart lists C1251/51 as "Open in Pump Motor Circuit" (BC-109); the Kluger ABS chart phrases the same code as "ABS pump motor is locked / open circuit in pump motor circuit". Check the pump-motor circuit before condemning the actuator.
- Grade: [A]
- Evidence: Toyota brake-control DTC chart (via scribd.com "Toyota DTCs for Brake Control System"); Kluger DTC chart 0542Q-07

## C1252
- Description: Hydro-Booster Pump Motor Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake actuator assembly; ABS MTR relay
- Diagnostic notes: Prius ECB hydro-booster pump motor (sub-code /52).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1259
- Description: HV System Regenerative Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: hybrid control system
- Diagnostic notes: Regenerative-brake coordination fault on the hybrid side (sub-code /58, Prius). A JustAnswer thread pairs it with P3120 on a 2001 Prius under hard acceleration — check hybrid codes alongside.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io); JustAnswer Toyota thread (P3120/C1259 case)

## C1267
- Description: Open or Short Circuit of Brake Pedal Load Sensing Switch Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake pedal load sensing switch; brake pedal load sensing switch circuit; ABS No.2 fuse
- Diagnostic notes: Sub-code /67 on the brake-control chart (BC-111).
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com "Toyota DTCs for Brake Control System")

## C1311
- Description: Open Circuit in Main Relay 1
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; ABS No.1 relay
- Diagnostic notes: Prius ECB main-relay diagnostics (sub-code /11). C1311–C1314 cover open/short of main relays 1 and 2.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1312
- Description: Short Circuit in Main Relay 1
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; ABS No.2 relay
- Diagnostic notes: See C1311 (sub-code /12).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1313
- Description: Open Circuit in Main Relay 2
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; ABS No.1 relay
- Diagnostic notes: See C1311 (sub-code /13).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1314
- Description: Short Circuit in Main Relay 2
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; ABS No.2 relay
- Diagnostic notes: See C1311 (sub-code /14).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1315
- Description: Changeover Solenoid Malfunction (SMC1)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly (SMC1)
- Diagnostic notes: Prius ECB stroke-simulator cut/changeover solenoid SMC1 (sub-code /31).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io); priusclub.hu RM1075U excerpt confirms C1315/31 (SMC1), C1316/32 (SMC2)

## C1316
- Description: Changeover Solenoid Malfunction (SMC2)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly (SMC2)
- Diagnostic notes: See C1315 (sub-code /32).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io); priusclub.hu RM1075U excerpt

## C1319
- Description: Changeover Solenoid Malfunction (SCSS)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; stroke simulator; fluid leakage
- Diagnostic notes: Stroke-simulator cut solenoid (sub-code /35). The chart lists fluid leakage as a trouble area — inspect for external leaks.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1337
- Description: Different Diameter Tire Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: tire size (mismatched tire diameters)
- Diagnostic notes: Set when wheel-speed logic detects implausible diameter differences (sub-code /37, BC-117). Check for a mismatched spare or mixed tire sizes before chasing sensors.
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com "Toyota DTCs for Brake Control System")

## C1341
- Description: Malfunction in Hydraulic System (FR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake actuator assembly; disc rotor; fluid leakage
- Diagnostic notes: Front-right hydraulic circuit malfunction (sub-code /62, Prius). A PriusChat thread notes an INF sub-code is available for C1343 (RR sibling) — expect similar detail codes here.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1342
- Description: Malfunction in Hydraulic System (FL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake actuator assembly; fluid leakage
- Diagnostic notes: Front-left mirror of C1341 (sub-code /63).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1343
- Description: Malfunction in Hydraulic System (RR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: fluid leakage; warped disc rotor; brake actuator assembly
- Diagnostic notes: A PriusChat thread (Gen 2 Prius, C1241 + C1343) describes C1343 as "difficulty holding the pressure constant in the right rear brake line" — check for leaks and rotor warpage before condemning the actuator, and read the three-digit INF sub-code for the detailed workup. (C1344, the presumed RL sibling, was not verified in this pass.)
- Grade: [C]
- Evidence: priuschat.com owner thread (single community report with code definitions)

## C1352
- Description: Increasing Pressure Solenoid Malfunction (FR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: Front-right pressure-increase solenoid (sub-code /21, Prius). C1352–C1355 = increasing-pressure solenoids FR/FL/RR/RL; C1356–C1359 = decreasing-pressure solenoids FR/FL/RR/RL.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io); priusclub.hu RM1075U excerpt

## C1353
- Description: Increasing Pressure Solenoid Malfunction (FL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1352 (sub-code /23).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1354
- Description: Increasing Pressure Solenoid Malfunction (RR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1352 (sub-code /25).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1355
- Description: Increasing Pressure Solenoid Malfunction (RL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1352 (sub-code /27).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1356
- Description: Decreasing Pressure Solenoid Malfunction (FR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: Front-right pressure-decrease solenoid (sub-code /22).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io); priusclub.hu RM1075U excerpt

## C1357
- Description: Decreasing Pressure Solenoid Malfunction (FL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1356 (sub-code /24).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1358
- Description: Decreasing Pressure Solenoid Malfunction (RR)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1356 (sub-code /26).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1359
- Description: Decreasing Pressure Solenoid Malfunction (RL)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector; brake actuator assembly
- Diagnostic notes: See C1356 (sub-code /28).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1361
- Description: Short Circuit in ABS Motor Fail Safe Relay Circuit
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: ABS1 H-fuse; VSC MTR relay; VSC MTR relay circuit; VSC FAIL relay; VSC FAIL relay circuit; ABS and traction actuator
- Diagnostic notes: Sub-code /91 on the brake-control VSC chart (BC-78).
- Grade: [B]
- Evidence: Toyota brake-control DTC chart (via scribd.com "Toyota DTCs for Brake Control System")

## C1364
- Description: Malfunction in W/C Pressure Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: skid control ECU; harness and connector
- Diagnostic notes: Wheel-cylinder pressure sensor (sub-code /61, Prius). Do not confuse with C1246 (master cylinder pressure sensor).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1365
- Description: Malfunction in ACC Pressure Sensor
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake actuator assembly (accumulator pressure sensor); skid control ECU
- Diagnostic notes: Accumulator pressure sensor (sub-code /54, Prius).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1368
- Description: Linear Valve Offset Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: initialization of linear solenoid valve and calibration undone; skid control ECU
- Diagnostic notes: Set when linear-solenoid-valve initialization/calibration has not been performed (sub-code /67, Prius) — run the calibration with Techstream.
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1377
- Description: Capacitor Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: brake control power supply assembly (capacitor); harness and connector; ABS No.1 fuse; ABS No.2 fuse; ABS No.3 fuse
- Diagnostic notes: The brake control power supply (capacitor block, "black box near the battery in the rear" on Gen 2 Prius) provides auxiliary brake power when 12 V drops. Detailed codes: 101 capacitor deteriorated (replace), 102 excessive self-discharge, 103 input voltage 16.4 V+ for 10 s+, 105/106/108 internal charge/backup-output/voltage-monitor circuit faults, 109/110 open/short in 12 V input or OUT1/OUT2 lines. Check 12 V battery, grounds and ABS fuses first — the capacitor block itself is very reliable, and the code often appears after brake work disturbs its connectors.
- Grade: [A]
- Evidence: Prius repair manual RM1076E DTC C1377/43 excerpt (via toyotamanuals.gitlab.io); priuschat.com C1377 thread; JustAnswer Toyota thread

## C1378
- Description: Capacitor Communication Circuit Malfunction
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: harness and connector; skid control ECU
- Diagnostic notes: Communication fault between the skid control ECU and the brake control power supply (sub-code /44, Prius).
- Grade: [A]
- Evidence: Prius repair manual RM1076E chart (via toyotamanuals.gitlab.io)

## C1431
- Description: Brake Actuator Pump Motor DTC (2012–2013 Camry)
- Category: C
- Scope: manufacturer (Toyota)
- Possible causes: poor ground on the left fender side panel bracket (after collision/body repair); brake actuator pump motor
- Diagnostic notes: Toyota TSB T-SB-0172-13 (Nov 2013): some 2012–2013 Camry vehicles exhibit ABS brake-actuator pump-motor noise from the engine compartment with brake, ABS and/or TRAC warning lamps on and DTC C1431 stored — caused by a poor ground on the left fender side panel bracket (loose, incorrect bolts, or improperly painted after body-shop repairs). Inspect and repair the fender grounds. The TSB excerpt does not state the formal detection-item title.
- Grade: [A]
- Evidence: Toyota TSB T-SB-0172-13 "ABS C1431 — Brake Noise with DTC" (via static.nhtsa.gov)

---

## U0101
- Description: Lost Communication with TCM
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: CAN communication system
- Diagnostic notes: On Toyota hybrids the lane-departure/pre-crash documentation phrases this as lost communication with the hybrid vehicle control ECU; the clearance-warning (IPA) documentation phrases it as lost communication with the TCM. When 2+ U-codes set simultaneously, inspect the connectors and wire harnesses of each ECU rather than chasing them individually.
- Grade: [A]
- Evidence: Toyota lane-departure-alert repair-manual DTC excerpts via zatonevkredit.ru; Toyota clearance-warning ECU DTC excerpt (U0101/U0155/U1114) via zatonevkredit.ru

## U0111
- Description: Lost Communication with Battery Energy Control Module "A"
- Category: U
- Scope: generic (SAE); Toyota-context documented
- Possible causes: hybrid battery ECU; CAN communication system; corroded battery terminals/connections
- Diagnostic notes: A Toyota master technician (JustAnswer, 2007 Prius) describes U0111 as interrupted communication with the hybrid battery's computer (ECU); it commonly appears alongside P0A80 (replace hybrid battery pack). Check battery connections for corrosion first.
- Grade: [B]
- Evidence: JustAnswer Toyota master-technician thread (2007 Prius P0171/P0420/U0111/P0A80)

## U0121
- Description: Lost Communication with ABS Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: CANL/CANH circuit; skid control ECU
- Diagnostic notes: From the 2004 Scion xB repair manual (RM1031U) CAN communication system, skid-control-ECU communication-stop mode (sub-code /94): the condition where the skid control ECU cannot transmit data continues for 5+ seconds, or the no-transmit condition repeatedly occurs 10 times.
- Grade: [A]
- Evidence: 2004 Scion xB repair manual RM1031U CAN diagnostics (via scribd.com)

## U0122
- Description: Lost Communication with Vehicle Dynamics Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: CAN communication system
- Diagnostic notes: From the Toyota 4WD-control DTC documentation: communication lost between the skid control ECU (brake actuator assembly) and the 4-wheel-drive control ECU for 0.72 s+ (1-trip). Note: this DTC also appears transiently while skid-control-ECU data is being overwritten (4LO lamp blinks) — clear DTCs after such work.
- Grade: [A]
- Evidence: Toyota repair-manual DTC U0122 excerpt via zatonevkredit.ru (detection condition, trouble area, note)

## U0123
- Description: Lost Communication with Yaw Rate Sensor Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: yaw rate sensor; CANL/CANH circuit; skid control ECU; steering angle sensor; junction connector
- Diagnostic notes: 2004 Scion xB RM1031U: with ECU IG1 voltage at 9.5 V+, no data received from the yaw rate sensor for 1 s+, or reception impossible one or more times within 5 s repeatedly 10 times (sub-code /62).
- Grade: [A]
- Evidence: 2004 Scion xB repair manual RM1031U CAN diagnostics (via scribd.com); Toyota lane-departure/pre-crash DTC excerpts via zatonevkredit.ru agree

## U0124
- Description: Lost Communication with Lateral Acceleration Sensor Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: yaw rate sensor (deceleration sensor); CANL/CANH circuit; skid control ECU; junction connector
- Diagnostic notes: Same detection pattern as U0123 but for the deceleration (lateral-G) sensor channel (sub-code /95). See also C1243–C1245 for the sensor-side faults.
- Grade: [A]
- Evidence: 2004 Scion xB repair manual RM1031U CAN diagnostics (via scribd.com); Toyota CAN DTC chart via zatonevkredit.ru

## U0126
- Description: Lost Communication with Steering Angle Sensor Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: steering angle sensor (spiral cable with sensor sub-assembly); CAN communication system
- Diagnostic notes: Same detection pattern as U0123 for the steering angle sensor (sub-code /63). The IPA/parking-assist documentation phrases it as lost communication with the spiral cable with sensor sub-assembly.
- Grade: [A]
- Evidence: 2004 Scion xB repair manual RM1031U CAN diagnostics (via scribd.com); Toyota IPA DTC excerpts via zatonevkredit.ru

## U0129
- Description: Lost Communication with Brake System Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: brake actuator assembly (skid control ECU); CAN communication system
- Diagnostic notes: Pre-crash safety city sensor view: unable to receive data from the brake actuator assembly (skid control ECU) for 5 s+ while driving at 5 km/h+. Also reported by the power steering ECU and combination meter.
- Grade: [A]
- Evidence: Toyota lane-departure/pre-crash DTC excerpts via zatonevkredit.ru; Toyota CAN communication chart via zatonevkredit.ru

## U0130
- Description: Lost Communication with VGRS
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: VGRS ECU (front steering control ECU); CAN communication system
- Diagnostic notes: Variable Gear Ratio Steering models only — lost communication with the VGRS ECU (front steering control ECU).
- Grade: [A]
- Evidence: Toyota IPA/parking-assist DTC excerpt via zatonevkredit.ru

## U0131
- Description: Lost Communication with Power Steering Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: power steering ECU assembly; CAN communication system
- Diagnostic notes: Reported by the combination meter assembly and lane-departure system when power-steering ECU data stops.
- Grade: [A]
- Evidence: Toyota lane-departure / CAN-chart DTC excerpts via zatonevkredit.ru

## U0140
- Description: Lost Communication with Main Body ECU
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: main body ECU (multiplex network body ECU); CAN communication system; seat belt control ECU; driving support ECU
- Diagnostic notes: Pre-crash view: communication stop between the main body ECU and the driving support ECU (or seat belt control ECU) for 1 s+ with the engine switch on (IG). The certification-ECU (smart key) documentation uses the same definition with 1-trip logic.
- Grade: [A]
- Evidence: Toyota pre-crash / certification-ECU DTC excerpts via zatonevkredit.ru

## U0142
- Description: Lost Communication with Body Control Module "B"
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: main body ECU (multiplex network body ECU); CAN communication system
- Diagnostic notes: CONFLICT — the lane-departure/CAN-chart documentation defines U0142 as "Lost Communication with Body Control Module 'B'" (reported by the combination meter), while the certification-ECU (smart key) documentation defines U0142 identically to U0140: "Lost Communication with Main Body ECU" (CAN error between certification ECU and main body ECU). Both are Toyota repair-manual sources; the reporting ECU determines which definition applies.
- Grade: [B]
- Evidence: Toyota lane-departure DTC excerpts vs Toyota certification-ECU DTC excerpts (both via zatonevkredit.ru)

## U0151
- Description: Lost Communication with Restraints Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: center airbag sensor assembly; CAN communication system; seat belt control ECU
- Diagnostic notes: Pre-crash view: communication stop between the center airbag sensor and the seat belt control ECU for 1 s+ (IG on). The CAN chart phrases it as "Lost Communication with Airbag ECU".
- Grade: [A]
- Evidence: Toyota pre-crash DTC excerpts via zatonevkredit.ru; Toyota CAN communication chart via zatonevkredit.ru

## U0155
- Description: Lost Communication with Combination Meter
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: combination meter assembly; CAN communication system
- Diagnostic notes: Pre-crash safety city sensor view: unable to receive data from the combination meter for 80 s+ while driving at 5 km/h+. The clearance-warning ECU documentation phrases it as lost communication with the instrument panel cluster (IPC).
- Grade: [A]
- Evidence: Toyota lane-departure / clearance-warning DTC excerpts via zatonevkredit.ru

## U0163
- Description: Lost Communication with Navigation Control Module
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: radio receiver assembly (navigation); CAN communication system
- Diagnostic notes: Phrased in the Toyota IPA documentation as lost communication with the radio receiver assembly. A community fault guide notes GPS malfunction as a symptom.
- Grade: [A]
- Evidence: Toyota IPA/parking-assist DTC excerpt via zatonevkredit.ru; scribd.com Toyota DTC fault-codes guide (symptom note)

## U0208
- Description: Lost Communication with "Seat Control Module A"
- Category: U
- Scope: generic (SAE); Toyota CAN-chart documented
- Possible causes: not documented
- Diagnostic notes: Appears as a row in the Toyota CAN communication system DTC matrix (RHD with entry-and-start system); per-system detection conditions not captured in the excerpts.
- Grade: [B]
- Evidence: Toyota CAN communication system DTC chart via zatonevkredit.ru (single chart row)

## U0235
- Description: Lost Communication with Cruise Control Front Distance Range Sensor
- Category: U
- Scope: generic (SAE); Toyota service-manual detection conditions documented
- Possible causes: front millimeter wave radar sensor; CAN communication system; driving support ECU
- Diagnostic notes: Pre-crash view: communication stop between the front millimeter wave radar sensor and the driving support ECU for 1 s+ (IG on).
- Grade: [A]
- Evidence: Toyota pre-crash DTC excerpts via zatonevkredit.ru

## U0293
- Description: HV ECU Communication Malfunction
- Category: U
- Scope: generic (SAE); Toyota service-manual documented
- Possible causes: CAN communication system
- Diagnostic notes: Listed in the Toyota lane-departure-alert DTC set as "HV ECU Communication" — a communication malfunction involving the hybrid vehicle control ECU. Per-system detection conditions not captured in the excerpts.
- Grade: [A]
- Evidence: Toyota lane-departure-alert DTC excerpts via zatonevkredit.ru

## U1100
- Description: Lost Communication with Seat Belt Control ECU
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: seat belt control ECU branch line or connector; power source circuit of seat belt control ECU; seat belt control ECU ground circuit; seat belt control ECU
- Diagnostic notes: Set when no communication from the seat belt control ECU continues. Pre-crash safety system family (see U1104 in v1.2.1).
- Grade: [A]
- Evidence: Toyota repair-manual DTC U1100 excerpt via zatonevkredit.ru (detection condition + trouble areas)

## U1114
- Description: Lost Communication with Main Switch Module
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: CAN communication system
- Diagnostic notes: The clearance-warning ECU documentation phrases it as lost communication with the integration control and panel assembly. Appears in the Toyota CAN communication DTC matrix.
- Grade: [B]
- Evidence: Toyota CAN communication system DTC chart via zatonevkredit.ru; Toyota clearance-warning ECU DTC excerpt (U0101/U0155/U1114)

## U1115
- Description: Lost Communication with Tilt and Telescopic Module
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: multiplex tilt and telescopic ECU CAN branch wire or connector; power source circuit of multiplex tilt and telescopic ECU; multiplex tilt and telescopic ECU ground circuit; multiplex tilt and telescopic ECU
- Diagnostic notes: No communication from the multiplex tilt and telescopic ECU; reported by the main body ECU (multiplex network body ECU). Power tilt/telescopic steering column models.
- Grade: [B]
- Evidence: Toyota repair-manual DTC U1115 excerpt via zatonevkredit.ru (detection condition + trouble areas); Toyota CAN communication chart

## U1117
- Description: Lost Communication with Accessory Gateway
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: connector and branch wire of sub bus 2 of option connector (bus buffer ECU); internal malfunction of option connector (bus buffer ECU)
- Diagnostic notes: Data from the option connector (bus buffer ECU) cannot be received. Reported by the certification ECU (smart key ECU); 1-trip logic, confirm with engine switch on (IG) for 10 s+.
- Grade: [A]
- Evidence: Toyota certification-ECU DTC excerpts via zatonevkredit.ru

## U1133
- Description: Lost Communication with PMN Module
- Category: U
- Scope: manufacturer (Toyota)
- Possible causes: not documented
- Diagnostic notes: Appears as a row in the Toyota CAN communication system DTC matrix; the "PMN" expansion and per-system detection conditions were not documented in the excerpts.
- Grade: [C]
- Evidence: Toyota CAN communication system DTC chart via zatonevkredit.ru (single chart row)

---

## Coverage notes

- NEW in this file: 175 codes (P: 55, B: 56, C: 41, U: 23). Together with the v1.2.1 file's 108, Toyota/Lexus coverage is now 283 codes. No v1.2.1 code was duplicated; the dedup list was checked entry by entry.
- Grade distribution: A = 117, B = 30, C = 28. The A grades come overwhelmingly from Toyota repair-manual excerpts (zatonevkredit.ru raw manual pages, toyotamanuals.gitlab.io Prius RM1076E / Kluger / Scion xB / 4Runner / Camry PDFs, ttundra.com / tovenza.com / to4runner.net / ttguide.net service-manual mirrors, charm.li, and one NHTSA-hosted TSB).
- Conflicts reported inline (not silently resolved): B1135 Toyota-vs-Nissan meaning; U0142 "Body Control Module B" vs "Main Body ECU"; B1180/B1182 chart-sequence inference; P3001/P3100 and P3105/P3109 near-duplicate descriptions in the community hybrid list; P3011–P3029 collapsed to a range representative; the ecutesting/retrolib generic B-body definitions (lamp/wiper) vs Toyota SRS squib meanings for B1800–B1848.
- Per the brief, Toyota-context entries were written for explicitly requested SAE-generic-range codes (P211x/P212x/P2135/P2138, P2195–P2198, P2A00/P2A03, P2440–P2447, U0101/U0111/U0121–U0142/U0163/U0208/U0235/U0293). Their Scope lines say so; the bare generic definitions remain the province of the SAE J2012 section of the database.
- Thin / not verified in this pass [?]: B1156–B1159 detection items; B1846–B1848 individual rows (pattern-inferred, graded C); B1905–B1908 (pretensioner LH) and B1920+ ranges; B1650 occupant-classification ECU code; C1237; C1344; C1280/C1288/C1360 (vague single-source descriptions, skipped); C14xx–C17xx beyond C1431; P2121/P2126 (B grade, range/performance titles per SAE pattern); P2237–P2241, P2270/P2271, P2401/P2402, P2420, P2600-series; hybrid P3200/P321E and P3012–P3029 individual modules; U1116/U1126–U1132/U1134/U1135/U1149; diesel D-4D codes (still out of scope).
- No immobilizer/seed-key material was sought or reproduced; immobilizer-adjacent codes are documented at the DTC-description level only.
- Quoting discipline: descriptions and trouble areas above are paraphrased from the sources; brief quoted phrases (e.g. chart titles) stay within fair-use limits. Evidence lines name the source rather than linking, matching the v1.2.1 file's convention.
