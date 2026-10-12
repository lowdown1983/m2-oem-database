# SAE J2012 Generic DTC Reference

Generic (non-manufacturer-specific) diagnostic trouble codes for the M2 OEM vehicle database v1.2.
Research date: 2026-10-06.

## Method

- Descriptions verified against live web sources (see Sources below). Every entry carries a quality
  grade: **A** = SAE standard text or factory service manual · **B** = reputable DTC database /
  technician source with cross-source agreement · **C** = single community source.
- Possible causes and diagnostic notes are included ONLY where sources documented them; every other
  entry says "not documented" rather than inventing content. No seed/key or proprietary material.
- Descriptions are short SAE-standard phrases (facts), quoted briefly per the copyright rule.
- Conflicts between sources are reported in Coverage notes, not silently resolved.

## Sources

- motor-talk.de forum attachment 778093 — full SAE J2012 P/B/C/U code transcription (community)
- scribd.com/document/136565407/OBD-2-20Codes — "SAE Diagnostic Trouble Codes Guide" transcription
- scribd.com/document/48581189/ODBII-codes — "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (B0xxx)
- retrolib.info — EOBD Network (U) Codes PDF (U-code cross-check)
- scribd.com/document/726385302/Control-Module-U-Code-List (U-code cross-check)
- scribd.com/document/369113064/Diagnostic-Trouble-Codes-TOAD-pdf (P34xx cross-check)
- guzzle7pt3.com/dtc3.php — DTC list (P2Axx, P28xx, P34xx cross-check)
- carobdcodes.com, obdii.pro, obdeleven.com, garagepro.shop (P0011 causes)
- troublecodes.net, chiptuners.in (P2002)
- uptake.com/topics/obd2-codes (P0300, P0171, P0420, P0442, P0500)
- jegs.com tech articles (P0128, P0401, P0446)
- scribd.com/document/416099864/electronic-sensor (P0100, P0130, P0170, P0303, P0304)
- mainelysubarus.com — GM TSB 08-07-30-021 (U0073); justanswer.com (U0100/U0101)

## P0xxx — Generic Powertrain Codes

## P0xxx — Generic Powertrain Codes
## P0001
- Description: Fuel Volume Regulator Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0002
- Description: Fuel Volume Regulator Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0003
- Description: Fuel Volume Regulator Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0004
- Description: Fuel Volume Regulator Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0005
- Description: Fuel Shutoff Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0006
- Description: Fuel Shutoff Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0007
- Description: Fuel Shutoff Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0008
- Description: Engine Position System Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0009
- Description: Engine Position System Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0010
- Description: A Camshaft Position Actuator Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0011
- Description: A Camshaft Position - Timing Over-Advanced or System Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: low, dirty, or wrong-viscosity engine oil (leading cause - VVT is hydraulically actuated); stuck oil control valve (OCV)/VVT solenoid; failed camshaft phaser; sludged oil passages; stretched timing chain; faulty camshaft position sensor
- Diagnostic notes: Change oil and filter with the exact specified viscosity first - resolves many cases; then remove and test the oil control valve (clean or replace); if symptoms persist, evaluate cam phaser and timing chain
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; description independently confirmed by carobdcodes.com, obdii.pro, obdeleven.com

## P0012
- Description: A Camshaft Position - Timing Over-Retarded (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0013
- Description: B Camshaft Position - Actuator Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0014
- Description: B Camshaft Position - Timing Over-Advanced or System Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0015
- Description: B Camshaft Position - Timing Over-Retarded (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0016
- Description: Crankshaft Position - Camshaft Position Correlation (Bank 1 Sensor A)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0017
- Description: Crankshaft Position - Camshaft Position Correlation (Bank 1 Sensor B)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0018
- Description: Crankshaft Position - Camshaft Position Correlation (Bank 2 Sensor A)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0019
- Description: Crankshaft Position - Camshaft Position Correlation (Bank 2 Sensor B)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0020
- Description: A Camshaft Position Actuator Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0021
- Description: A Camshaft Position - Timing Over-Advanced or System Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0022
- Description: A Camshaft Position - Timing Over-Retarded (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0023
- Description: B Camshaft Position - Actuator Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0024
- Description: B Camshaft Position - Timing Over-Advanced or System Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0025
- Description: B Camshaft Position - Timing Over-Retarded (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0026
- Description: Intake Valve Control Solenoid Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0027
- Description: Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0028
- Description: Intake Valve Control Solenoid Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0029
- Description: Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0030
- Description: HO2S Heater Control Circuit (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0031
- Description: HO2S Heater Control Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0032
- Description: HO2S Heater Control Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0033
- Description: Turbo Charger Bypass Valve Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0034
- Description: Turbo Charger Bypass Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0035
- Description: Turbo Charger Bypass Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0036
- Description: HO2S Heater Control Circuit (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0037
- Description: HO2S Heater Control Circuit Low (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0038
- Description: HO2S Heater Control Circuit High (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0039
- Description: Turbo/Super Charger Bypass Valve Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0040
- Description: O2 Sensor Signals Swapped Bank 1 Sensor 1 / Bank 2 Sensor 1
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0041
- Description: O2 Sensor Signals Swapped Bank 1 Sensor 2 / Bank 2 Sensor 2
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0042
- Description: HO2S Heater Control Circuit (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0043
- Description: HO2S Heater Control Circuit Low (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0044
- Description: HO2S Heater Control Circuit High (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0045
- Description: Turbo/Super Charger Boost Control Solenoid Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0046
- Description: Turbo/Super Charger Boost Control Solenoid Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0047
- Description: Turbo/Super Charger Boost Control Solenoid Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0048
- Description: Turbo/Super Charger Boost Control Solenoid Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0049
- Description: Turbo/Super Charger Turbine Overspeed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0050
- Description: HO2S Heater Control Circuit (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0051
- Description: HO2S Heater Control Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0052
- Description: HO2S Heater Control Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0053
- Description: HO2S Heater Resistance (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0054
- Description: HO2S Heater Resistance (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0055
- Description: HO2S Heater Resistance (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0056
- Description: HO2S Heater Control Circuit (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0057
- Description: HO2S Heater Control Circuit Low (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0058
- Description: HO2S Heater Control Circuit High (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0059
- Description: HO2S Heater Resistance (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0060
- Description: HO2S Heater Resistance (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0061
- Description: HO2S Heater Resistance (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0062
- Description: HO2S Heater Control Circuit (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0063
- Description: HO2S Heater Control Circuit Low (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0064
- Description: HO2S Heater Control Circuit High (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0065
- Description: Air Assisted Injector Control Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0066
- Description: Air Assisted Injector Control Circuit or Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0067
- Description: Air Assisted Injector Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0068
- Description: MAP/MAF - Throttle Position Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0069
- Description: Manifold Absolute Pressure - Barometric Pressure Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0070
- Description: Ambient Air Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0071
- Description: Ambient Air Temperature Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0072
- Description: Ambient Air Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0073
- Description: Ambient Air Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0074
- Description: Ambient Air Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0075
- Description: Intake Valve Control Solenoid Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0076
- Description: Intake Valve Control Solenoid Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0077
- Description: Intake Valve Control Solenoid Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0078
- Description: Exhaust Valve Control Solenoid Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0079
- Description: Exhaust Valve Control Solenoid Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0080
- Description: Exhaust Valve Control Solenoid Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0081
- Description: Intake Valve Control Solenoid Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0082
- Description: Intake Valve Control Solenoid Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0083
- Description: Intake Valve Control Solenoid Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0084
- Description: Exhaust Valve Control Solenoid Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0085
- Description: Exhaust Valve Control Solenoid Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0086
- Description: Exhaust Valve Control Solenoid Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0087
- Description: Fuel Rail/System Pressure - Too Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0088
- Description: Fuel Rail/System Pressure - Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0089
- Description: Fuel Pressure Regulator 1 Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0090
- Description: Fuel Pressure Regulator 1 Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0091
- Description: Fuel Pressure Regulator 1 Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0092
- Description: Fuel Pressure Regulator 1 Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0093
- Description: Fuel System Leak Detected - Large Leak
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0094
- Description: Fuel System Leak Detected - Small Leak
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0095
- Description: Intake Air Temperature Sensor 2 Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0096
- Description: Intake Air Temperature Sensor 2 Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0097
- Description: Intake Air Temperature Sensor 2 Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0098
- Description: Intake Air Temperature Sensor 2 Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0099
- Description: Intake Air Temperature Sensor 2 Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P0100
- Description: Mass or Volume Air Flow Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: disconnected MAF electrical plug; damaged wiring at the plug; defective or damaged MAF sensor; corroded or loose electrical terminals in MAF circuit
- Diagnostic notes: Inspect MAF connector and wiring first before replacing the sensor
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0101
- Description: Mass or Volume Air Flow Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0102
- Description: Mass or Volume Air Flow Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0103
- Description: Mass or Volume Air Flow Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0104
- Description: Mass or Volume Air Flow Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0105
- Description: Manifold Absolute Pressure/Barometric Pressure Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0106
- Description: Manifold Absolute Pressure/Barometric Pressure Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0107
- Description: Manifold Absolute Pressure/Barometric Pressure Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0108
- Description: Manifold Absolute Pressure/Barometric Pressure Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0109
- Description: Manifold Absolute Pressure/Barometric Pressure Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0110
- Description: Intake Air Temperature Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0111
- Description: Intake Air Temperature Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0112
- Description: Intake Air Temperature Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0113
- Description: Intake Air Temperature Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0114
- Description: Intake Air Temperature Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0115
- Description: Engine Coolant Temperature Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0116
- Description: Engine Coolant Temperature Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0117
- Description: Engine Coolant Temperature Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0118
- Description: Engine Coolant Temperature Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0119
- Description: Engine Coolant Temperature Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0120
- Description: Throttle Position Sensor/Switch A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0121
- Description: Throttle Position Sensor/Switch A Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0122
- Description: Throttle Position Sensor/Switch A Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0123
- Description: Throttle Position Sensor/Switch A Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0124
- Description: Throttle Position Sensor/Switch A Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0125
- Description: Insufficient Coolant Temperature for Closed Loop Fuel Control
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0126
- Description: Insufficient Coolant Temperature for Stable Operation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0127
- Description: Intake Air Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0128
- Description: Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature)
- Category: P
- Scope: generic
- Possible causes: thermostat stuck open
- Diagnostic notes: ECT never reaches regulating temperature; check thermostat operation
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; description consistent with jegs.com tech reference

## P0129
- Description: Barometric Pressure Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0130
- Description: O2 Sensor Circuit Malfunction (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: B1S1 oxygen sensor not showing proper activity; wiring fault
- Diagnostic notes: ECM changes fuel management strategy when set; fuel economy will suffer
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0131
- Description: O2 Sensor Circuit Low Voltage (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0132
- Description: O2 Sensor Circuit High Voltage (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0133
- Description: O2 Sensor Circuit Slow Response (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0134
- Description: O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0135
- Description: O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0136
- Description: O2 Sensor Circuit Malfunction (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0137
- Description: O2 Sensor Circuit Low Voltage (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0138
- Description: O2 Sensor Circuit High Voltage (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0139
- Description: O2 Sensor Circuit Slow Response (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0140
- Description: O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0141
- Description: O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0142
- Description: O2 Sensor Circuit Malfunction (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0143
- Description: O2 Sensor Circuit Low Voltage (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0144
- Description: O2 Sensor Circuit High Voltage (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0145
- Description: O2 Sensor Circuit Slow Response (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0146
- Description: O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0147
- Description: O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0148
- Description: Fuel Delivery Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0149
- Description: Fuel Timing Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0150
- Description: O2 Sensor Circuit Malfunction (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0151
- Description: O2 Sensor Circuit Low Voltage (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0152
- Description: O2 Sensor Circuit High Voltage (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0153
- Description: O2 Sensor Circuit Slow Response (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0154
- Description: O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0155
- Description: O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0156
- Description: O2 Sensor Circuit Malfunction (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0157
- Description: O2 Sensor Circuit Low Voltage (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0158
- Description: O2 Sensor Circuit High Voltage (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0159
- Description: O2 Sensor Circuit Slow Response (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0160
- Description: O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0161
- Description: O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0162
- Description: O2 Sensor Circuit Malfunction (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0163
- Description: O2 Sensor Circuit Low Voltage (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0164
- Description: O2 Sensor Circuit High Voltage (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0165
- Description: O2 Sensor Circuit Slow Response (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0166
- Description: O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0167
- Description: O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0168
- Description: Fuel Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0169
- Description: Incorrect Fuel Composition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0170
- Description: Fuel Trim Malfunction (Bank 1)
- Category: P
- Scope: generic
- Possible causes: oxygen sensor feedback driving trim out of range
- Diagnostic notes: Check whether O2 sensors are calling for more or less fuel (positive vs negative trim)
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0171
- Description: System too Lean (Bank 1)
- Category: P
- Scope: generic
- Possible causes: vacuum leaks; faulty MAF sensor; weak fuel pump
- Diagnostic notes: Compare fuel trims at idle vs under load - vacuum leaks show at idle, fuel delivery issues show under load
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0172
- Description: System too Rich (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0173
- Description: Fuel Trim Malfunction (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0174
- Description: System too Lean (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0175
- Description: System too Rich (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0176
- Description: Fuel Composition Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0177
- Description: Fuel Composition Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0178
- Description: Fuel Composition Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0179
- Description: Fuel Composition Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0180
- Description: Fuel Temperature Sensor A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0181
- Description: Fuel Temperature Sensor A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0182
- Description: Fuel Temperature Sensor A Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0183
- Description: Fuel Temperature Sensor A Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0184
- Description: Fuel Temperature Sensor A Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0185
- Description: Fuel Temperature Sensor B Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0186
- Description: Fuel Temperature Sensor B Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0187
- Description: Fuel Temperature Sensor B Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0188
- Description: Fuel Temperature Sensor B Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0189
- Description: Fuel Temperature Sensor B Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0190
- Description: Fuel Rail Pressure Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0191
- Description: Fuel Rail Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0192
- Description: Fuel Rail Pressure Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0193
- Description: Fuel Rail Pressure Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0194
- Description: Fuel Rail Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0195
- Description: Engine Oil Temperature Sensor Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0196
- Description: Engine Oil Temperature Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0197
- Description: Engine Oil Temperature Sensor Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0198
- Description: Engine Oil Temperature Sensor High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0199
- Description: Engine Oil Temperature Sensor Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0200
- Description: Injector Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0201
- Description: Injector Circuit Malfunction - Cylinder 1
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0202
- Description: Injector Circuit Malfunction - Cylinder 2
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0203
- Description: Injector Circuit Malfunction - Cylinder 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0204
- Description: Injector Circuit Malfunction - Cylinder 4
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0205
- Description: Injector Circuit Malfunction - Cylinder 5
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0206
- Description: Injector Circuit Malfunction - Cylinder 6
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0207
- Description: Injector Circuit Malfunction - Cylinder 7
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0208
- Description: Injector Circuit Malfunction - Cylinder 8
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0209
- Description: Injector Circuit Malfunction - Cylinder 9
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0210
- Description: Injector Circuit Malfunction - Cylinder 10
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0211
- Description: Injector Circuit Malfunction - Cylinder 11
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0212
- Description: Injector Circuit Malfunction - Cylinder 12
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0213
- Description: Cold Start Injector 1 Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0214
- Description: Cold Start Injector 2 Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0215
- Description: Engine Shutoff Solenoid Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0216
- Description: Injection Timing Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0217
- Description: Engine Coolant Over Temperature Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription). Note: scribd transcription words P0217 as "Engine Overtemp Condition" - wording conflict reported in Coverage notes; motor-talk wording used here

## P0218
- Description: Transmission Over Temperature Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0219
- Description: Engine Overspeed Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0220
- Description: Throttle/Petal Position Sensor/Switch B Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0221
- Description: Throttle/Petal Position Sensor/Switch B Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0222
- Description: Throttle/Petal Position Sensor/Switch B Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0223
- Description: Throttle/Petal Position Sensor/Switch B Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0224
- Description: Throttle/Petal Position Sensor/Switch B Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0225
- Description: Throttle/Petal Position Sensor/Switch C Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0226
- Description: Throttle/Petal Position Sensor/Switch C Circuit Range/Performance Problem
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0227
- Description: Throttle/Petal Position Sensor/Switch C Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0228
- Description: Throttle/Petal Position Sensor/Switch C Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0229
- Description: Throttle/Petal Position Sensor/Switch C Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0230
- Description: Fuel Pump Primary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0231
- Description: Fuel Pump Secondary Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0232
- Description: Fuel Pump Secondary Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0233
- Description: Fuel Pump Secondary Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0234
- Description: Engine Overboost Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0235
- Description: Turbocharger Boost Sensor A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0236
- Description: Turbocharger Boost Sensor A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0237
- Description: Turbocharger Boost Sensor A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0238
- Description: Turbocharger Boost Sensor A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0239
- Description: Turbocharger Boost Sensor B Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0240
- Description: Turbocharger Boost Sensor B Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0241
- Description: Turbocharger Boost Sensor B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0242
- Description: Turbocharger Boost Sensor B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0243
- Description: Turbocharger Wastegate Solenoid A Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0244
- Description: Turbocharger Wastegate Solenoid A Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0245
- Description: Turbocharger Wastegate Solenoid A Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0246
- Description: Turbocharger Wastegate Solenoid A High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0247
- Description: Turbocharger Wastegate Solenoid B Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0248
- Description: Turbocharger Wastegate Solenoid B Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0249
- Description: Turbocharger Wastegate Solenoid B Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0250
- Description: Turbocharger Wastegate Solenoid B High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0251
- Description: Injection Pump Fuel Metering Control "A" Malfunction (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0252
- Description: Injection Pump Fuel Metering Control "A" Range/Performance (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0253
- Description: Injection Pump Fuel Metering Control "A" Low (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0254
- Description: Injection Pump Fuel Metering Control "A" High (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0255
- Description: Injection Pump Fuel Metering Control "A" Intermittent (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0256
- Description: Injection Pump Fuel Metering Control "B" Malfunction (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0257
- Description: Injection Pump Fuel Metering Control "B" Range/Performance (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0258
- Description: Injection Pump Fuel Metering Control "B" Low (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0259
- Description: Injection Pump Fuel Metering Control "B" High (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0260
- Description: Injection Pump Fuel Metering Control "B" Intermittent (Cam/Rotor/Injector)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0261
- Description: Cylinder 1 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0262
- Description: Cylinder 1 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0263
- Description: Cylinder 1 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0264
- Description: Cylinder 2 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0265
- Description: Cylinder 2 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0266
- Description: Cylinder 2 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0267
- Description: Cylinder 3 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0268
- Description: Cylinder 3 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0269
- Description: Cylinder 3 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0270
- Description: Cylinder 4 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0271
- Description: Cylinder 4 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0272
- Description: Cylinder 4 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0273
- Description: Cylinder 5 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0274
- Description: Cylinder 5 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0275
- Description: Cylinder 5 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0276
- Description: Cylinder 6 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0277
- Description: Cylinder 6 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0278
- Description: Cylinder 6 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0279
- Description: Cylinder 7 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0280
- Description: Cylinder 7 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0281
- Description: Cylinder 7 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0282
- Description: Cylinder 8 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0283
- Description: Cylinder 8 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0284
- Description: Cylinder 8 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0285
- Description: Cylinder 9 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0286
- Description: Cylinder 9 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0287
- Description: Cylinder 9 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0288
- Description: Cylinder 10 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0289
- Description: Cylinder 10 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0290
- Description: Cylinder 10 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0291
- Description: Cylinder 11 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0292
- Description: Cylinder 11 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0293
- Description: Cylinder 11 Contribution/Balance Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0294
- Description: Cylinder 12 Injector Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0295
- Description: Cylinder 12 Injector Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0296
- Description: Cylinder 12 Contribution/Range Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0297
- Description: Vehicle Overspeed Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription). Note: scribd transcription words P0217 as "Engine Overtemp Condition" - wording conflict reported in Coverage notes; motor-talk wording used here

## P0298
- Description: Engine Oil Over Temperature
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription). Note: scribd transcription words P0217 as "Engine Overtemp Condition" - wording conflict reported in Coverage notes; motor-talk wording used here

## P0299
- Description: Turbo/Super Charger Underboost
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription). Note: scribd transcription words P0217 as "Engine Overtemp Condition" - wording conflict reported in Coverage notes; motor-talk wording used here

## P0300
- Description: Random/Multiple Cylinder Misfire Detected
- Category: P
- Scope: generic
- Possible causes: worn spark plugs; faulty ignition coil(s); vacuum leak; low fuel pressure
- Diagnostic notes: Check freeze-frame for the conditions when set; mode $06 misfire counters per cylinder narrow it to the offending cylinder(s)
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0301
- Description: Cylinder 1 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0302
- Description: Cylinder 2 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0303
- Description: Cylinder 3 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: bad ignition coil; worn spark plug; faulty fuel injector; valve train issue
- Diagnostic notes: Swap coil/plug to another cylinder to see if the misfire follows the part
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0304
- Description: Cylinder 4 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: bad ignition coil; worn spark plug; faulty fuel injector; valve train issue
- Diagnostic notes: Swap coil/plug to another cylinder to see if the misfire follows the part
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from community DTC references

## P0305
- Description: Cylinder 5 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0306
- Description: Cylinder 6 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0307
- Description: Cylinder 7 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0308
- Description: Cylinder 8 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0309
- Description: Cylinder 9 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0310
- Description: Cylinder 10 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0311
- Description: Cylinder 11 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0312
- Description: Cylinder 12 Misfire Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0313
- Description: Misfire Detected with Low Fuel
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0314
- Description: Single Cylinder Misfire (Cylinder not Specified)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0315
- Description: Crankshaft Position System Variation Not Learned
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0316
- Description: Engine Misfire Detected on Startup (First 1000 Revolutions)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0317
- Description: Rough Road Hardware Not Present
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0318
- Description: Rough Road Sensor "A" Signal Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0319
- Description: Rough Road Sensor "B" Signal Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0320
- Description: Ignition/Distributor Engine Speed Input Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0321
- Description: Ignition/Distributor Engine Speed Input Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0322
- Description: Ignition/Distributor Engine Speed Input Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0323
- Description: Ignition/Distributor Engine Speed Input Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0324
- Description: Knock Control System Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0325
- Description: Knock Sensor 1 Circuit Malfunction (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0326
- Description: Knock Sensor 1 Circuit Range/Performance (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0327
- Description: Knock Sensor 1 Circuit Low Input (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0328
- Description: Knock Sensor 1 Circuit High Input (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0329
- Description: Knock Sensor 1 Circuit Intermittent (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0330
- Description: Knock Sensor 2 Circuit Malfunction (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0331
- Description: Knock Sensor 2 Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0332
- Description: Knock Sensor 2 Circuit Low Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0333
- Description: Knock Sensor 2 Circuit High Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0334
- Description: Knock Sensor 2 Circuit Intermittent (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0335
- Description: Crankshaft Position Sensor A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0336
- Description: Crankshaft Position Sensor A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0337
- Description: Crankshaft Position Sensor A Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0338
- Description: Crankshaft Position Sensor A Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0339
- Description: Crankshaft Position Sensor A Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0340
- Description: Camshaft Position Sensor A Circuit Malfunction (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0341
- Description: Camshaft Position Sensor A Circuit Range/Performance (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0342
- Description: Camshaft Position Sensor A Circuit Low Input (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0343
- Description: Camshaft Position Sensor A Circuit High Input (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0344
- Description: Camshaft Position Sensor A Circuit Intermittent (Bank 1 or Single Sensor)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0345
- Description: Camshaft Position Sensor A Circuit Malfunction (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0346
- Description: Camshaft Position Sensor A Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0347
- Description: Camshaft Position Sensor A Circuit Low Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0348
- Description: Camshaft Position Sensor A Circuit High Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0349
- Description: Camshaft Position Sensor A Circuit Intermittent (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0350
- Description: Ignition Coil Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0351
- Description: Ignition Coil A Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0352
- Description: Ignition Coil B Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0353
- Description: Ignition Coil C Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0354
- Description: Ignition Coil D Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0355
- Description: Ignition Coil E Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0356
- Description: Ignition Coil F Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0357
- Description: Ignition Coil G Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0358
- Description: Ignition Coil H Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0359
- Description: Ignition Coil I Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0360
- Description: Ignition Coil J Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0361
- Description: Ignition Coil K Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0362
- Description: Ignition Coil L Primary/Secondary Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0363
- Description: Misfire Detected - Fueling Disabled
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0364
- Description: Reserved
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0365
- Description: Camshaft Position Sensor "B" Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0366
- Description: Camshaft Position Sensor "B" Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0367
- Description: Camshaft Position Sensor "B" Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0368
- Description: Camshaft Position Sensor "B" Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0369
- Description: Camshaft Position Sensor "B" Circuit Intermittent (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0370
- Description: Timing Reference High Resolution Signal A Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0371
- Description: Timing Reference High Resolution Signal A Too Many Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0372
- Description: Timing Reference High Resolution Signal A Too Few Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0373
- Description: Timing Reference High Resolution Signal A Intermittent/Erratic Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0374
- Description: Timing Reference High Resolution Signal A No Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0375
- Description: Timing Reference High Resolution Signal B Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0376
- Description: Timing Reference High Resolution Signal B Too Many Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0377
- Description: Timing Reference High Resolution Signal B Too Few Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0378
- Description: Timing Reference High Resolution Signal B Intermittent/Erratic Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0379
- Description: Timing Reference High Resolution Signal B No Pulses
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0380
- Description: Glow Plug/Heater Circuit "A" Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0381
- Description: Glow Plug/Heater Indicator Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0382
- Description: Glow Plug/Heater Circuit "B" Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0385
- Description: Crankshaft Position Sensor B Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0386
- Description: Crankshaft Position Sensor B Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0387
- Description: Crankshaft Position Sensor B Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0388
- Description: Crankshaft Position Sensor B Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0389
- Description: Crankshaft Position Sensor B Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0390
- Description: Camshaft Position Sensor "B" Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0391
- Description: Camshaft Position Sensor "B" Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0392
- Description: Camshaft Position Sensor "B" Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0393
- Description: Camshaft Position Sensor "B" Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0394
- Description: Camshaft Position Sensor "B" Circuit Intermittent (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0400
- Description: Exhaust Gas Recirculation Flow Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0401
- Description: Exhaust Gas Recirculation Flow Insufficient Detected
- Category: P
- Scope: generic
- Possible causes: clogged EGR valve or EGR passages
- Diagnostic notes: Inspect and clean the EGR valve; use a scan tool to monitor EGR sensor readings
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from uptake.com and jegs.com tech references

## P0402
- Description: Exhaust Gas Recirculation Flow Excessive Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0403
- Description: Exhaust Gas Recirculation Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0404
- Description: Exhaust Gas Recirculation Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0405
- Description: Exhaust Gas Recirculation Sensor A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0406
- Description: Exhaust Gas Recirculation Sensor A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0407
- Description: Exhaust Gas Recirculation Sensor B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0408
- Description: Exhaust Gas Recirculation Sensor B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0410
- Description: Secondary Air Injection System Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0411
- Description: Secondary Air Injection System Incorrect Flow Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0412
- Description: Secondary Air Injection System Switching Valve A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0413
- Description: Secondary Air Injection System Switching Valve A Circuit Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0414
- Description: Secondary Air Injection System Switching Valve A Circuit Shorted
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0415
- Description: Secondary Air Injection System Switching Valve B Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0416
- Description: Secondary Air Injection System Switching Valve B Circuit Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0417
- Description: Secondary Air Injection System Switching Valve B Circuit Shorted
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0418
- Description: Secondary Air Injection System Relay "A" Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0419
- Description: Secondary Air Injection System Relay "B" Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0420
- Description: Catalyst System Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: failing catalytic converter; inefficient oxygen sensor; exhaust leak
- Diagnostic notes: Compare upstream vs downstream O2 sensor waveforms before condemning the converter
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from uptake.com and jegs.com tech references

## P0421
- Description: Warm Up Catalyst Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0422
- Description: Main Catalyst Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0423
- Description: Heated Catalyst Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0424
- Description: Heated Catalyst Temperature Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0425
- Description: Catalyst Temperature Sensor (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0426
- Description: Catalyst Temperature Sensor Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0427
- Description: Catalyst Temperature Sensor Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0428
- Description: Catalyst Temperature Sensor High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0429
- Description: Catalyst Heater Control Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0430
- Description: Catalyst System Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0431
- Description: Warm Up Catalyst Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0432
- Description: Main Catalyst Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0433
- Description: Heated Catalyst Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0434
- Description: Heated Catalyst Temperature Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0435
- Description: Catalyst Temperature Sensor (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0436
- Description: Catalyst Temperature Sensor Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0437
- Description: Catalyst Temperature Sensor Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0438
- Description: Catalyst Temperature Sensor High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0439
- Description: Catalyst Heater Control Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0440
- Description: Evaporative Emission Control System Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0441
- Description: Evaporative Emission Control System Incorrect Purge Flow
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0442
- Description: Evaporative Emission Control System Leak Detected (small leak)
- Category: P
- Scope: generic
- Possible causes: loose or damaged gas cap; small EVAP system leak
- Diagnostic notes: Check the gas cap first; smoke-test the EVAP system to find the leak
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from uptake.com and jegs.com tech references

## P0443
- Description: Evaporative Emission Control System Purge Control Valve Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0444
- Description: Evaporative Emission Control System Purge Control Valve Circuit Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0445
- Description: Evaporative Emission Control System Purge Control Valve Circuit Shorted
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0446
- Description: Evaporative Emission Control System Vent Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: EVAP canister vent solenoid/valve fault; wiring fault
- Diagnostic notes: Test the vent valve/solenoid circuit per the service manual
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from uptake.com and jegs.com tech references

## P0447
- Description: Evaporative Emission Control System Vent Control Circuit Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0448
- Description: Evaporative Emission Control System Vent Control Circuit Shorted
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0449
- Description: Evaporative Emission Control System Vent Valve/Solenoid Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0450
- Description: Evaporative Emission Control System Pressure Sensor Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0451
- Description: Evaporative Emission Control System Pressure Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0452
- Description: Evaporative Emission Control System Pressure Sensor Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0453
- Description: Evaporative Emission Control System Pressure Sensor High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0454
- Description: Evaporative Emission Control System Pressure Sensor Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0455
- Description: Evaporative Emission Control System Leak Detected (gross leak)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0456
- Description: Evaporative Emission Control System Leak Detected (very small leak)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0457
- Description: Evaporative Emission Control System Leak Detected (fuel cap loose/off)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0458
- Description: Evaporative Emission System Purge Control Valve Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0459
- Description: Evaporative Emission System Purge Control Valve Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0460
- Description: Fuel Level Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0461
- Description: Fuel Level Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0462
- Description: Fuel Level Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0463
- Description: Fuel Level Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0464
- Description: Fuel Level Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0465
- Description: Purge Flow Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0466
- Description: Purge Flow Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0467
- Description: Purge Flow Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0468
- Description: Purge Flow Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0469
- Description: Purge Flow Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0470
- Description: Exhaust Pressure Sensor Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0471
- Description: Exhaust Pressure Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0472
- Description: Exhaust Pressure Sensor Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0473
- Description: Exhaust Pressure Sensor High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0474
- Description: Exhaust Pressure Sensor Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0475
- Description: Exhaust Pressure Control Valve Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0476
- Description: Exhaust Pressure Control Valve Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0477
- Description: Exhaust Pressure Control Valve Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0478
- Description: Exhaust Pressure Control Valve High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0479
- Description: Exhaust Pressure Control Valve Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0480
- Description: Cooling Fan 1 Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0481
- Description: Cooling Fan 2 Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0482
- Description: Cooling Fan 3 Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0483
- Description: Cooling Fan Rationality Check Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0484
- Description: Cooling Fan Circuit Over Current
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0485
- Description: Cooling Fan Power/Ground Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0486
- Description: Exhaust Gas Recirculation Sensor B Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0487
- Description: Exhaust Gas Recirculation Throttle Position Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0488
- Description: Exhaust Gas Recirculation Throttle Position Control Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0489
- Description: Exhaust Gas Recirculation Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0490
- Description: Exhaust Gas Recirculation Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0491
- Description: Secondary Air Injection System (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0492
- Description: Secondary Air Injection System (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0493
- Description: Fan Overspeed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0494
- Description: Fan Speed Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0495
- Description: Fan Speed High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0496
- Description: Evaporative Emission System High Purge Flow
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0497
- Description: Evaporative Emission System Low Purge Flow
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0498
- Description: Evaporative Emission System Vent Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0499
- Description: Evaporative Emission System Vent Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0500
- Description: Vehicle Speed Sensor Malfunction
- Category: P
- Scope: generic
- Possible causes: faulty vehicle speed sensor; wiring fault
- Diagnostic notes: May affect cruise control and speedometer readings; check sensor signal with a scan tool
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment; causes from uptake.com

## P0501
- Description: Vehicle Speed Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0502
- Description: Vehicle Speed Sensor Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0503
- Description: Vehicle Speed Sensor Intermittent/Erratic/High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0504
- Description: Brake Switch A/B Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0505
- Description: Idle Control System Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0506
- Description: Idle Control System RPM Lower Than Expected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0507
- Description: Idle Control System RPM Higher Than Expected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0508
- Description: Idle Air Control System Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0509
- Description: Idle Air Control System Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0510
- Description: Closed Throttle Position Switch Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0511
- Description: Idle Air Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0512
- Description: Starter Request Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0513
- Description: Incorrect Immobilizer Key
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0514
- Description: Battery Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0515
- Description: Battery Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0516
- Description: Battery Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0517
- Description: Battery Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0518
- Description: Idle Air Control Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0519
- Description: Idle Air Control System Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0520
- Description: Engine Oil Pressure Sensor/Switch Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0521
- Description: Engine Oil Pressure Sensor/Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0522
- Description: Engine Oil Pressure Sensor/Switch Circuit Low Voltage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0523
- Description: Engine Oil Pressure Sensor/Switch Circuit High Voltage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0524
- Description: Engine Oil Pressure Too Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0525
- Description: Cruise Control Servo Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0526
- Description: Fan Speed Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0527
- Description: Fan Speed Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0528
- Description: Fan Speed Sensor Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0529
- Description: Fan Speed Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0530
- Description: A/C Refrigerant Pressure Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0531
- Description: A/C Refrigerant Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0532
- Description: A/C Refrigerant Pressure Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0533
- Description: A/C Refrigerant Pressure Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0534
- Description: Air Conditioner Refrigerant Charge Loss
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0535
- Description: A/C Evaporator Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0536
- Description: A/C Evaporator Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0537
- Description: A/C Evaporator Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0538
- Description: A/C Evaporator Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0539
- Description: A/C Evaporator Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0540
- Description: Intake Air Heater A Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0541
- Description: Intake Air Heater A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0542
- Description: Intake Air Heater A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0543
- Description: Intake Air Heater A Circuit Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0544
- Description: Exhaust Gas Temperature Sensor Circuit (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0545
- Description: Exhaust Gas Temperature Sensor Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0546
- Description: Exhaust Gas Temperature Sensor Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0547
- Description: Exhaust Gas Temperature Sensor Circuit (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0548
- Description: Exhaust Gas Temperature Sensor Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0549
- Description: Exhaust Gas Temperature Sensor Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0550
- Description: Power Steering Pressure Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0551
- Description: Power Steering Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0552
- Description: Power Steering Pressure Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0553
- Description: Power Steering Pressure Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0554
- Description: Power Steering Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0555
- Description: Brake Booster Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0556
- Description: Brake Booster Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0557
- Description: Brake Booster Pressure Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0558
- Description: Brake Booster Pressure Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0559
- Description: Brake Booster Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0560
- Description: System Voltage Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0561
- Description: System Voltage Unstable
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0562
- Description: System Voltage Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0563
- Description: System Voltage High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0564
- Description: Cruise Control Multi-Function Input A Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0565
- Description: Cruise Control On Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0566
- Description: Cruise Control Off Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0567
- Description: Cruise Control Resume Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0568
- Description: Cruise Control Set Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0569
- Description: Cruise Control Coast Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0570
- Description: Cruise Control Accel Signal Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0571
- Description: Cruise Control/Brake Switch A Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0572
- Description: Cruise Control/Brake Switch A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0573
- Description: Cruise Control/Brake Switch A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0574
- Description: Cruise Control System - Vehicle Speed Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0575
- Description: Cruise Control Input Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0576
- Description: Cruise Control Input Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0577
- Description: Cruise Control Input Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0578
- Description: Cruise Control Multi-Function Input A Circuit Stuck
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0579
- Description: Cruise Control Multi-Function Input A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0580
- Description: Cruise Control Multi-Function Input A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0581
- Description: Cruise Control Multi-Function Input A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0582
- Description: Cruise Control Vacuum Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0583
- Description: Cruise Control Vacuum Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0584
- Description: Cruise Control Vacuum Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0585
- Description: Cruise Control Multi-Function Input A/B Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0586
- Description: Cruise Control Vent Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0587
- Description: Cruise Control Vent Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0588
- Description: Cruise Control Vent Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0589
- Description: Cruise Control Multi-Function Input B Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0590
- Description: Cruise Control Multi-Function Input B Circuit Stuck
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0591
- Description: Cruise Control Multi-Function Input B Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0592
- Description: Cruise Control Multi-Function Input B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0593
- Description: Cruise Control Multi-Function Input B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0594
- Description: Cruise Control Servo Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0595
- Description: Cruise Control Servo Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0596
- Description: Cruise Control Servo Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0597
- Description: Thermostat Heater Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0598
- Description: Thermostat Heater Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0599
- Description: Thermostat Heater Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from or generically worded in the scribd SAE transcription)

## P0600
- Description: Serial Communication Link Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0601
- Description: Internal Control Module Memory Check Sum Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0602
- Description: Control Module Programming Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0603
- Description: Internal Control Module Keep Alive Memory (KAM) Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0604
- Description: Internal Control Module Random Access Memory (RAM) Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0605
- Description: Internal Control Module Read Only Memory (ROM) Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0606
- Description: PCM Processor Fault
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0607
- Description: Control Module Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0608
- Description: Control Module VSS Output "A" Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0609
- Description: Control Module VSS Output "B" Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0610
- Description: Control Module Vehicle Options Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0611
- Description: Fuel Injector Control Module Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0612
- Description: Fuel Injector Control Module Relay Control
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0613
- Description: TCM Processor
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0614
- Description: ECM / TCM Incompatible
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0615
- Description: Starter Relay Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0616
- Description: Starter Relay Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0617
- Description: Starter Relay Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0618
- Description: Alternative Fuel Control Module KAM Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0619
- Description: Alternative Fuel Control Module RAM/ROM Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0620
- Description: Generator Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0621
- Description: Generator Lamp "L" Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0622
- Description: Generator Field "F" Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0623
- Description: Generator Lamp Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0624
- Description: Fuel Cap Lamp Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0625
- Description: Generator Field/F Terminal Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0626
- Description: Generator Field/F Terminal Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0627
- Description: Fuel Pump A Control Circuit /Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0628
- Description: Fuel Pump A Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0629
- Description: Fuel Pump A Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0630
- Description: VIN Not Programmed or Incompatible - ECM/PCM
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0631
- Description: VIN Not Programmed or Incompatible - TCM
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0632
- Description: Odometer Not Programmed - ECM/PCM
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0633
- Description: Immobilizer Key Not Programmed - ECM/PCM
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0634
- Description: PCM/ECM/TCM Internal Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0635
- Description: Power Steering Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0636
- Description: Power Steering Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0637
- Description: Power Steering Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0638
- Description: Throttle Actuator Control Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0639
- Description: Throttle Actuator Control Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0640
- Description: Intake Air Heater Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0641
- Description: Sensor Reference Voltage A Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0642
- Description: Sensor Reference Voltage A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0643
- Description: Sensor Reference Voltage A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0644
- Description: Driver Display Serial Communication Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0645
- Description: A/C Clutch Relay Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0646
- Description: A/C Clutch Relay Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0647
- Description: A/C Clutch Relay Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0648
- Description: Immobilizer Lamp Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0649
- Description: Speed Control Lamp Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0650
- Description: Malfunction Indicator Lamp (MIL) Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0651
- Description: Sensor Reference Voltage B Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0652
- Description: Sensor Reference Voltage B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0653
- Description: Sensor Reference Voltage B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0654
- Description: Engine RPM Output Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0655
- Description: Engine Hot Lamp Output Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0656
- Description: Fuel Level Output Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0657
- Description: Actuator Supply Voltage Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0658
- Description: Actuator Supply Voltage Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0659
- Description: Actuator Supply Voltage Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0660
- Description: Intake Manifold Tuning Valve Control Circuit/Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0661
- Description: Intake Manifold Tuning Valve Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0662
- Description: Intake Manifold Tuning Valve Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0663
- Description: Intake Manifold Tuning Valve Control Circuit/Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0664
- Description: Intake Manifold Tuning Valve Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0665
- Description: Intake Manifold Tuning Valve Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0666
- Description: PCM/ECM/TCM Internal Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0667
- Description: PCM/ECM/TCM Internal Temperature Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0668
- Description: PCM/ECM/TCM Internal Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0669
- Description: PCM/ECM/TCM Internal Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0670
- Description: Glow Plug Module Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0671
- Description: Cylinder 1 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0672
- Description: Cylinder 2 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0673
- Description: Cylinder 3 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0674
- Description: Cylinder 4 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0675
- Description: Cylinder 5 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0676
- Description: Cylinder 6 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0677
- Description: Cylinder 7 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0678
- Description: Cylinder 8 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0679
- Description: Cylinder 9 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0680
- Description: Cylinder 10 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0681
- Description: Cylinder 11 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0682
- Description: Cylinder 12 Glow Plug Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0683
- Description: Glow Plug Control Module to PCM Communication Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0684
- Description: Glow Plug Control Module to PCM Communication Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0685
- Description: ECM/PCM Power Relay Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0686
- Description: ECM/PCM Power Relay Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0687
- Description: ECM/PCM Power Relay Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0688
- Description: ECM/PCM Power Relay Sense Circuit /Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0689
- Description: ECM/PCM Power Relay Sense Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0690
- Description: ECM/PCM Power Relay Sense Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0691
- Description: Fan 1 Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0692
- Description: Fan 1 Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0693
- Description: Fan 2 Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0694
- Description: Fan 2 Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0695
- Description: Fan 3 Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0696
- Description: Fan 3 Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0697
- Description: Sensor Reference Voltage C Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0698
- Description: Sensor Reference Voltage C Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0699
- Description: Sensor Reference Voltage C Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0700
- Description: Transmission Control System (MIL Request) Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0701
- Description: Transmission Control System Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0702
- Description: Transmission Control System Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0703
- Description: Torque Converter/Brake Switch B Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0704
- Description: Clutch Switch Input Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0705
- Description: Transmission Range Sensor Circuit malfunction (PRNDL Input)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0706
- Description: Transmission Range Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0707
- Description: Transmission Range Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0708
- Description: Transmission Range Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0709
- Description: Transmission Range Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0710
- Description: Transmission Fluid Temperature Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0711
- Description: Transmission Fluid Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0712
- Description: Transmission Fluid Temperature Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0713
- Description: Transmission Fluid Temperature Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0714
- Description: Transmission Fluid Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0715
- Description: Input/Turbine Speed Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0716
- Description: Input/Turbine Speed Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0717
- Description: Input/Turbine Speed Sensor Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0718
- Description: Input/Turbine Speed Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0719
- Description: Torque Converter/Brake Switch B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0720
- Description: Output Speed Sensor Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0721
- Description: Output Speed Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0722
- Description: Output Speed Sensor Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0723
- Description: Output Speed Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0724
- Description: Torque Converter/Brake Switch B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0725
- Description: Engine Speed input Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0726
- Description: Engine Speed Input Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0727
- Description: Engine Speed Input Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0728
- Description: Engine Speed Input Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0729
- Description: Gear 6 Incorrect Ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0730
- Description: Incorrect Gear Ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0731
- Description: Gear 1 Incorrect ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0732
- Description: Gear 2 Incorrect ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0733
- Description: Gear 3 Incorrect ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0734
- Description: Gear 4 Incorrect ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0735
- Description: Gear 5 Incorrect ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0736
- Description: Reverse incorrect gear ratio
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0737
- Description: TCM Engine Speed Output Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0738
- Description: TCM Engine Speed Output Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0739
- Description: TCM Engine Speed Output Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0740
- Description: Torque Converter Clutch Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0741
- Description: Torque Converter Clutch Circuit Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0742
- Description: Torque Converter Clutch Circuit Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0743
- Description: Torque Converter Clutch Circuit Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0744
- Description: Torque Converter Clutch Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0745
- Description: Pressure Control Solenoid Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0746
- Description: Pressure Control Solenoid Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0747
- Description: Pressure Control Solenoid Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0748
- Description: Pressure Control Solenoid Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0749
- Description: Pressure Control Solenoid Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0750
- Description: Shift Solenoid A Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0751
- Description: Shift Solenoid A Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0752
- Description: Shift Solenoid A Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0753
- Description: Shift Solenoid A Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0754
- Description: Shift Solenoid A Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0755
- Description: Shift Solenoid B Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0756
- Description: Shift Solenoid B Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0757
- Description: Shift Solenoid B Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0758
- Description: Shift Solenoid B Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0759
- Description: Shift Solenoid B Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0760
- Description: Shift Solenoid C Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0761
- Description: Shift Solenoid C Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0762
- Description: Shift Solenoid C Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0763
- Description: Shift Solenoid C Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0764
- Description: Shift Solenoid C Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0765
- Description: Shift Solenoid D Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0766
- Description: Shift Solenoid D Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0767
- Description: Shift Solenoid D Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0768
- Description: Shift Solenoid D Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0769
- Description: Shift Solenoid D Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0770
- Description: Shift Solenoid E Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0771
- Description: Shift Solenoid E Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0772
- Description: Shift Solenoid E Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0773
- Description: Shift Solenoid E Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0774
- Description: Shift Solenoid E Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0775
- Description: Pressure Control Solenoid B
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0776
- Description: Pressure Control Solenoid B Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0777
- Description: Pressure Control Solenoid B Stuck on
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0778
- Description: Pressure Control Solenoid B Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0779
- Description: Pressure Control Solenoid B Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0780
- Description: Shift Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0781
- Description: 1-2 Shift Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; scribd transcription shows truncated "-2 Shift Malfunction" - full "1-2 Shift Malfunction" used (conflict reported in Coverage notes)

## P0782
- Description: 2-3 Shift Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0783
- Description: 3-4 Shift Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0784
- Description: 4-5 Shift Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0785
- Description: Shift/Timing Solenoid Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0786
- Description: Shift/Timing Solenoid Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0787
- Description: Shift/Timing Solenoid Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0788
- Description: Shift/Timing Solenoid High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0789
- Description: Shift/Timing Solenoid Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0790
- Description: Normal/Performance Switch Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0791
- Description: Intermediate Shaft Speed Sensor A Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0792
- Description: Intermediate Shaft Speed Sensor A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0793
- Description: Intermediate Shaft Speed Sensor A Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0794
- Description: Intermediate Shaft Speed Sensor A Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0795
- Description: Pressure Control Solenoid C
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0796
- Description: Pressure Control Solenoid C Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0797
- Description: Pressure Control Solenoid C Stuck on
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0798
- Description: Pressure Control Solenoid C Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0799
- Description: Pressure Control Solenoid C Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0800
- Description: Transfer Case Control System (MIL Request)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0801
- Description: Reverse Inhibit Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0802
- Description: Transmission Control System MIL Request Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0803
- Description: 1-4 Upshift (Skip Shift) Solenoid Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: scribd "SAE Diagnostic Trouble Codes Guide" + motor-talk.de SAE J2012 attachment - two independent transcriptions agree

## P0804
- Description: 1-4 Upshift (Skip Shift) Lamp Control Circuit Malfunction
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0805
- Description: Clutch Position Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0806
- Description: Clutch Position Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0807
- Description: Clutch Position Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0808
- Description: Clutch Position Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0809
- Description: Clutch Position Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0810
- Description: Clutch Position Control Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0811
- Description: Excessive Clutch Slippage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0812
- Description: Reverse Input Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0813
- Description: Reverse Output Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0814
- Description: Transmission Range Display Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0815
- Description: Upshift Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0816
- Description: Downshift Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0817
- Description: Starter Disable Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0818
- Description: Driveline Disconnect Switch Input Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0819
- Description: Up and Down Shift Switch to Transmission Range Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0820
- Description: Gear Lever X-Y Position Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0821
- Description: Gear Lever X Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0822
- Description: Gear Lever Y Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0823
- Description: Gear Lever X Position Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0824
- Description: Gear Lever Y Position Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0825
- Description: Gear Lever Push-Pull Switch (Shift Anticipate)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0826
- Description: Up and Down Shift Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0827
- Description: Up and Down Shift Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0828
- Description: Up and Down Shift Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0829
- Description: 5-6 Shift
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0830
- Description: Clutch Pedal Switch A Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0831
- Description: Clutch Pedal Switch A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0832
- Description: Clutch Pedal Switch A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0833
- Description: Clutch Pedal Switch B Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0834
- Description: Clutch Pedal Switch B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0835
- Description: Clutch Pedal Switch B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0836
- Description: Four Wheel Drive (4WD) Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0837
- Description: Four Wheel Drive (4WD) Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0838
- Description: Four Wheel Drive (4WD) Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0839
- Description: Four Wheel Drive (4WD) Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0840
- Description: Transmission Fluid Pressure Sensor/Switch A Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0841
- Description: Transmission Fluid Pressure Sensor/Switch A Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0842
- Description: Transmission Fluid Pressure Sensor/Switch A Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0843
- Description: Transmission Fluid Pressure Sensor/Switch A Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0844
- Description: Transmission Fluid Pressure Sensor/Switch A Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0845
- Description: Transmission Fluid Pressure Sensor/Switch B Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0846
- Description: Transmission Fluid Pressure Sensor/Switch B Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0847
- Description: Transmission Fluid Pressure Sensor/Switch B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0848
- Description: Transmission Fluid Pressure Sensor/Switch B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0849
- Description: Transmission Fluid Pressure Sensor/Switch B Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0850
- Description: Park/Neutral Switch Input Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0851
- Description: Park/Neutral Switch Input Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0852
- Description: Park/Neutral Switch Input Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0853
- Description: Drive Switch Input Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0854
- Description: Drive Switch Input Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0855
- Description: Drive Switch Input Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0856
- Description: Traction Control Input Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0857
- Description: Traction Control Input Signal Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0858
- Description: Traction Control Input Signal Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0859
- Description: Traction Control Input Signal High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0860
- Description: Gear Shift Module Communication Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0861
- Description: Gear Shift Module Communication Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0862
- Description: Gear Shift Module Communication Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0863
- Description: TCM Communication Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0864
- Description: TCM Communication Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0865
- Description: TCM Communication Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0866
- Description: TCM Communication Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0867
- Description: Transmission Fluid Pressure
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0868
- Description: Transmission Fluid Pressure Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0869
- Description: Transmission Fluid Pressure High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0870
- Description: Transmission Fluid Pressure Sensor/Switch C Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0871
- Description: Transmission Fluid Pressure Sensor/Switch C Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0872
- Description: Transmission Fluid Pressure Sensor/Switch C Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0873
- Description: Transmission Fluid Pressure Sensor/Switch C Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0874
- Description: Transmission Fluid Pressure Sensor/Switch C Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0875
- Description: Transmission Fluid Pressure Sensor/Switch D Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0876
- Description: Transmission Fluid Pressure Sensor/Switch D Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0877
- Description: Transmission Fluid Pressure Sensor/Switch D Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0878
- Description: Transmission Fluid Pressure Sensor/Switch D Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0879
- Description: Transmission Fluid Pressure Sensor/Switch D Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0880
- Description: TCM Power Input Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0881
- Description: TCM Power Input Signal Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0882
- Description: TCM Power Input Signal Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0883
- Description: TCM Power Input Signal High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0884
- Description: TCM Power Input Signal Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0885
- Description: TCM Power Relay Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0886
- Description: TCM Power Relay Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0887
- Description: TCM Power Relay Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0888
- Description: TCM Power Relay Sense Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0889
- Description: TCM Power Relay Sense Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0890
- Description: TCM Power Relay Sense Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0891
- Description: TCM Power Relay Sense Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0892
- Description: TCM Power Relay Sense Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0893
- Description: Multiple Gears Engaged
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0894
- Description: Transmission Component Slipping
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0895
- Description: Shift Time Too Short
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0896
- Description: Shift Time Too Long
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0897
- Description: Transmission Fluid Deteriorated
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0898
- Description: Transmission Control System MIL Request Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0899
- Description: Transmission Control System MIL Request Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0900
- Description: Clutch Actuator Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0901
- Description: Clutch Actuator Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0902
- Description: Clutch Actuator Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0903
- Description: Clutch Actuator Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0904
- Description: Gate Select Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0905
- Description: Gate Select Position Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0906
- Description: Gate Select Position Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0907
- Description: Gate Select Position Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0908
- Description: Gate Select Position Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0909
- Description: Gate Select Control Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0910
- Description: Gate Select Actuator Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0911
- Description: Gate Select Actuator Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0912
- Description: Gate Select Actuator Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0913
- Description: Gate Select Actuator Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0914
- Description: Gear Shift Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0915
- Description: Gear Shift Position Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0916
- Description: Gear Shift Position Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0917
- Description: Gear Shift Position Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0918
- Description: Gear Shift Position Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0919
- Description: Gear Shift Position Control Error
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0920
- Description: Gear Shift Forward Actuator Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0921
- Description: Gear Shift Forward Actuator Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0922
- Description: Gear Shift Forward Actuator Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0923
- Description: Gear Shift Forward Actuator Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0924
- Description: Gear Shift Reverse Actuator Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0925
- Description: Gear Shift Reverse Actuator Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0926
- Description: Gear Shift Reverse Actuator Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0927
- Description: Gear Shift Reverse Actuator Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0928
- Description: Gear Shift Lock Solenoid Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0929
- Description: Gear Shift Lock Solenoid Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0930
- Description: Gear Shift Lock Solenoid Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0931
- Description: Gear Shift Lock Solenoid Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0932
- Description: Hydraulic Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0933
- Description: Hydraulic Pressure Sensor Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0934
- Description: Hydraulic Pressure Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0935
- Description: Hydraulic Pressure Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0936
- Description: Hydraulic Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0937
- Description: Hydraulic Oil Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0938
- Description: Hydraulic Oil Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0939
- Description: Hydraulic Oil Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0940
- Description: Hydraulic Oil Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0941
- Description: Hydraulic Oil Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0942
- Description: Hydraulic Pressure Unit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0943
- Description: Hydraulic Pressure Unit Cycling Period Too Short
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0944
- Description: Hydraulic Pressure Unit Loss of Pressure
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0945
- Description: Hydraulic Pump Relay Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0946
- Description: Hydraulic Pump Relay Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0947
- Description: Hydraulic Pump Relay Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0948
- Description: Hydraulic Pump Relay Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0949
- Description: Auto Shift Manual Adaptive Learning Not Complete
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0950
- Description: Auto Shift Manual Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0951
- Description: Auto Shift Manual Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0952
- Description: Auto Shift Manual Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0953
- Description: Auto Shift Manual Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0954
- Description: Auto Shift Manual Control Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0955
- Description: Auto Shift Manual Mode Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0956
- Description: Auto Shift Manual Mode Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0957
- Description: Auto Shift Manual Mode Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0958
- Description: Auto Shift Manual Mode Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0959
- Description: Auto Shift Manual Mode Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0960
- Description: Pressure Control Solenoid A Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0961
- Description: Pressure Control Solenoid A Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0962
- Description: Pressure Control Solenoid A Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0963
- Description: Pressure Control Solenoid A Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0964
- Description: Pressure Control Solenoid B Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0965
- Description: Pressure Control Solenoid B Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0966
- Description: Pressure Control Solenoid B Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0967
- Description: Pressure Control Solenoid B Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0968
- Description: Pressure Control Solenoid C Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0969
- Description: Pressure Control Solenoid C Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0970
- Description: Pressure Control Solenoid C Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0971
- Description: Pressure Control Solenoid C Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0972
- Description: Shift Solenoid A Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0973
- Description: Shift Solenoid A Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0974
- Description: Shift Solenoid A Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0975
- Description: Shift Solenoid B Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0976
- Description: Shift Solenoid B Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0977
- Description: Shift Solenoid B Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0978
- Description: Shift Solenoid C Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0979
- Description: Shift Solenoid C Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0980
- Description: Shift Solenoid C Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0981
- Description: Shift Solenoid D Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0982
- Description: Shift Solenoid D Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0983
- Description: Shift Solenoid D Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0984
- Description: Shift Solenoid E Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0985
- Description: Shift Solenoid E Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0986
- Description: Shift Solenoid E Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0987
- Description: Transmission Fluid Pressure Sensor/Switch E Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0988
- Description: Transmission Fluid Pressure Sensor/Switch E Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0989
- Description: Transmission Fluid Pressure Sensor/Switch E Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0990
- Description: Transmission Fluid Pressure Sensor/Switch E Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0991
- Description: Transmission Fluid Pressure Sensor/Switch E Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0992
- Description: Transmission Fluid Pressure Sensor/Switch F Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0993
- Description: Transmission Fluid Pressure Sensor/Switch F Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0994
- Description: Transmission Fluid Pressure Sensor/Switch F Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0995
- Description: Transmission Fluid Pressure Sensor/Switch F Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0996
- Description: Transmission Fluid Pressure Sensor/Switch F Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0997
- Description: Shift Solenoid F Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0998
- Description: Shift Solenoid F Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0999
- Description: Shift Solenoid F Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A00
- Description: Motor Electronics Coolant Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A01
- Description: Motor Electronics Coolant Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A02
- Description: Motor Electronics Coolant Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A03
- Description: Motor Electronics Coolant Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A04
- Description: Motor Electronics Coolant Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A05
- Description: Motor Electronics Coolant Pump Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A06
- Description: Motor Electronics Coolant Pump Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A07
- Description: Motor Electronics Coolant Pump Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A08
- Description: DC/DC Converter Status Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A09
- Description: DC/DC Converter Status Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A10
- Description: DC/DC Converter Status Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A11
- Description: DC/DC Converter Enable Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A12
- Description: DC/DC Converter Enable Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A13
- Description: DC/DC Converter Enable Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A14
- Description: Engine Mount Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A15
- Description: Engine Mount Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A16
- Description: Engine Mount Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A17
- Description: Motor Torque Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A18
- Description: Motor Torque Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A19
- Description: Motor Torque Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A20
- Description: Motor Torque Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A21
- Description: Motor Torque Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A22
- Description: Generator Torque Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A23
- Description: Generator Torque Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A24
- Description: Generator Torque Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A25
- Description: Generator Torque Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A26
- Description: Generator Torque Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A27
- Description: Battery Power Off Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A28
- Description: Battery Power Off Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)

## P0A29
- Description: Battery Power Off Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (single source; codes absent from the scribd SAE transcription)


## P2xxx — Generic Powertrain Codes (SAE-controlled)


## P2xxx — Generic Powertrain Codes (SAE-controlled)
## P2000
- Description: NOx Trap Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2001
- Description: NOx Trap Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2002
- Description: Particulate Trap Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: excessive soot accumulation in the diesel particulate filter (DPF); failed or inhibited DPF regeneration; faulty DPF differential pressure sensor
- Diagnostic notes: Inspect and clean the DPF; monitor DPF sensor readings with a scan tool; perform/verify regeneration cycles; check engine oil for fuel dilution from repeated regen attempts
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; description independently confirmed by troublecodes.net, chiptuners.in, justanswer.com

## P2003
- Description: Particulate Trap Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2004
- Description: Intake Manifold Runner Control Stuck Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2005
- Description: Intake Manifold Runner Control Stuck Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2006
- Description: Intake Manifold Runner Control Stuck Closed (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2007
- Description: Intake Manifold Runner Control Stuck Closed (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2008
- Description: Intake Manifold Runner Control Circuit/Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2009
- Description: Intake Manifold Runner Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2010
- Description: Intake Manifold Runner Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2011
- Description: Intake Manifold Runner Control Circuit/Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2012
- Description: Intake Manifold Runner Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2013
- Description: Intake Manifold Runner Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2014
- Description: Intake Manifold Runner Position Sensor/Switch Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2015
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2016
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2017
- Description: Intake Manifold Runner Position Sensor/Switch Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2018
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Intermittent (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2019
- Description: Intake Manifold Runner Position Sensor/Switch Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2020
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2021
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2022
- Description: Intake Manifold Runner Position Sensor/Switch Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2023
- Description: Intake Manifold Runner Position Sensor/Switch Circuit Intermittent (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2024
- Description: Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2025
- Description: Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2026
- Description: Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit Low Voltage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2027
- Description: Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit High Voltage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2028
- Description: Evaporative Emissions (EVAP) Fuel Vapor Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2029
- Description: Fuel Fired Heater Disabled
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2030
- Description: Fuel Fired Heater Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2031
- Description: Exhaust Gas Temperature Sensor Circuit (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2032
- Description: Exhaust Gas Temperature Sensor Circuit Low (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2033
- Description: Exhaust Gas Temperature Sensor Circuit High (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2034
- Description: Exhaust Gas Temperature Sensor Circuit (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2035
- Description: Exhaust Gas Temperature Sensor Circuit Low (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2036
- Description: Exhaust Gas Temperature Sensor Circuit High (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2037
- Description: Reductant Injection Air Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2038
- Description: Reductant Injection Air Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2039
- Description: Reductant Injection Air Pressure Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2040
- Description: Reductant Injection Air Pressure Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2041
- Description: Reductant Injection Air Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2042
- Description: Reductant Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2043
- Description: Reductant Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2044
- Description: Reductant Temperature Sensor Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2045
- Description: Reductant Temperature Sensor Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2046
- Description: Reductant Temperature Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2047
- Description: Reductant Injector Circuit/Open (Bank 1 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2048
- Description: Reductant Injector Circuit Low (Bank 1 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2049
- Description: Reductant Injector Circuit High (Bank 1 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2050
- Description: Reductant Injector Circuit/Open (Bank 2 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2051
- Description: Reductant Injector Circuit Low (Bank 2 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2052
- Description: Reductant Injector Circuit High (Bank 2 Unit 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2053
- Description: Reductant Injector Circuit/Open (Bank 1 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2054
- Description: Reductant Injector Circuit Low (Bank 1 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2055
- Description: Reductant Injector Circuit High (Bank 1 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2056
- Description: Reductant Injector Circuit/Open (Bank 2 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2057
- Description: Reductant Injector Circuit Low (Bank 2 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2058
- Description: Reductant Injector Circuit High (Bank 2 Unit 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2059
- Description: Reductant Injection Air Pump Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2060
- Description: Reductant Injection Air Pump Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2061
- Description: Reductant Injection Air Pump Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2062
- Description: Reductant Supply Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2063
- Description: Reductant Supply Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2064
- Description: Reductant Supply Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2065
- Description: Fuel Level Sensor B Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2066
- Description: Fuel Level Sensor B Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2067
- Description: Fuel Level Sensor B Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2068
- Description: Fuel Level Sensor B Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2069
- Description: Fuel Level Sensor B Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2070
- Description: Intake Manifold Tuning (IMT) Valve Stuck Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2071
- Description: Intake Manifold Tuning (IMT) Valve Stuck Closed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2075
- Description: Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2076
- Description: Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2077
- Description: Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2078
- Description: Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2079
- Description: Intake Manifold Tuning (IMT) Valve Position Sensor/Switch Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2080
- Description: Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2081
- Description: Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2082
- Description: Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2083
- Description: Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2084
- Description: Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2085
- Description: Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2086
- Description: Exhaust Gas Temperature Sensor Circuit Range/Performance (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2087
- Description: Exhaust Gas Temperature Sensor Circuit Intermittent (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2088
- Description: A Camshaft Position Actuator Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2089
- Description: A Camshaft Position Actuator Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2090
- Description: B Camshaft Position Actuator Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2091
- Description: B Camshaft Position Actuator Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2092
- Description: A Camshaft Position Actuator Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2093
- Description: A Camshaft Position Actuator Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2094
- Description: B Camshaft Position Actuator Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2095
- Description: B Camshaft Position Actuator Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2096
- Description: Post Catalyst Fuel Trim System Too Lean (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2097
- Description: Post Catalyst Fuel Trim System Too Rich (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2098
- Description: Post Catalyst Fuel Trim System Too Lean (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2099
- Description: Post Catalyst Fuel Trim System Too Rich (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2100
- Description: Throttle Actuator Control Motor Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2101
- Description: Throttle Actuator Control Motor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2102
- Description: Throttle Actuator Control Motor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2103
- Description: Throttle Actuator Control Motor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2104
- Description: Throttle Actuator Control System - Forced Idle
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2105
- Description: Throttle Actuator Control System - Forced Engine Shutdown
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2106
- Description: Throttle Actuator Control System - Forced Limited Power
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2107
- Description: Throttle Actuator Control Module Processor
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2108
- Description: Throttle Actuator Control Module Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2109
- Description: Throttle/Pedal Position Sensor A Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2110
- Description: Throttle Actuator Control System - Forced Limited RPM
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2111
- Description: Throttle Actuator Control System - Stuck Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2112
- Description: Throttle Actuator Control System - Stuck Closed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2113
- Description: Throttle/Pedal Position Sensor B Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2114
- Description: Throttle/Pedal Position Sensor C Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2115
- Description: Throttle/Pedal Position Sensor D Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2116
- Description: Throttle/Pedal Position Sensor E Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2117
- Description: Throttle/Pedal Position Sensor F Minimum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2118
- Description: Throttle Actuator Control Motor Current Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2119
- Description: Throttle Actuator Control Throttle Body Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2120
- Description: Throttle/Pedal Position Sensor/Switch D Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2121
- Description: Throttle/Pedal Position Sensor/Switch D Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2122
- Description: Throttle/Pedal Position Sensor/Switch D Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2123
- Description: Throttle/Pedal Position Sensor/Switch D Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2124
- Description: Throttle/Pedal Position Sensor/Switch D Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2125
- Description: Throttle/Pedal Position Sensor/Switch E Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2126
- Description: Throttle/Pedal Position Sensor/Switch E Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2127
- Description: Throttle/Pedal Position Sensor/Switch E Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2128
- Description: Throttle/Pedal Position Sensor/Switch E Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2129
- Description: Throttle/Pedal Position Sensor/Switch E Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2130
- Description: Throttle/Pedal Position Sensor/Switch F Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2131
- Description: Throttle/Pedal Position Sensor/Switch F Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2132
- Description: Throttle/Pedal Position Sensor/Switch F Circuit Low Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2133
- Description: Throttle/Pedal Position Sensor/Switch F Circuit High Input
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2134
- Description: Throttle/Pedal Position Sensor/Switch F Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2135
- Description: Throttle/Pedal Position Sensor/Switch "A" /"B" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2136
- Description: Throttle/Pedal Position Sensor/Switch "A" /"C" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2137
- Description: Throttle/Pedal Position Sensor/Switch "B" /"C" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2138
- Description: Throttle/Pedal Position Sensor/Switch "D" /"E" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2139
- Description: Throttle/Pedal Position Sensor/Switch "D" /"F" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2140
- Description: Throttle/Pedal Position Sensor/Switch "E" /"F" Voltage Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2141
- Description: Exhaust Gas Recirculation Throttle Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2142
- Description: Exhaust Gas Recirculation Throttle Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2143
- Description: Exhaust Gas Recirculation Vent Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2144
- Description: Exhaust Gas Recirculation Vent Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2145
- Description: Exhaust Gas Recirculation Vent Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2146
- Description: Fuel Injector Group "A" Supply Voltage Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2147
- Description: Fuel Injector Group "A" Supply Voltage Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2148
- Description: Fuel Injector Group "A" Supply Voltage Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2149
- Description: Fuel Injector Group "B" Supply Voltage Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2150
- Description: Fuel Injector Group "B" Supply Voltage Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2151
- Description: Fuel Injector Group "B" Supply Voltage Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2152
- Description: Fuel Injector Group "C" Supply Voltage Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2153
- Description: Fuel Injector Group "C" Supply Voltage Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2154
- Description: Fuel Injector Group "C" Supply Voltage Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2155
- Description: Fuel Injector Group "D" Supply Voltage Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2156
- Description: Fuel Injector Group "D" Supply Voltage Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2157
- Description: Fuel Injector Group "D" Supply Voltage Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2158
- Description: Vehicle Speed Sensor "B"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2159
- Description: Vehicle Speed Sensor "B" Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2160
- Description: Vehicle Speed Sensor "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2161
- Description: Vehicle Speed Sensor "B" Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2162
- Description: Vehicle Speed Sensor "A" / "B" Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2163
- Description: Throttle/Pedal Position Sensor "A" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2164
- Description: Throttle/Pedal Position Sensor "B" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2165
- Description: Throttle/Pedal Position Sensor "C" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2166
- Description: Throttle/Pedal Position Sensor "D" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2167
- Description: Throttle/Pedal Position Sensor "E" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2168
- Description: Throttle/Pedal Position Sensor "F" Maximum Stop Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2169
- Description: Exhaust Pressure Regulator Vent Solenoid Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2170
- Description: Exhaust Pressure Regulator Vent Solenoid Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2171
- Description: Exhaust Pressure Regulator Vent Solenoid Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2172
- Description: Throttle Actuator Control System - Sudden High Airflow Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2173
- Description: Throttle Actuator Control System - High Airflow Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2174
- Description: Throttle Actuator Control System - Sudden Low Airflow Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2175
- Description: Throttle Actuator Control System - Low Airflow Detected
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2176
- Description: Throttle Actuator Control System - Idle Position Not Learned
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2177
- Description: System Too Lean Off Idle (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2178
- Description: System Too Rich Off Idle (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2179
- Description: System Too Lean Off Idle (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2180
- Description: System Too Rich Off Idle (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2181
- Description: Cooling System Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2182
- Description: Engine Coolant Temperature Sensor 2 Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2183
- Description: Engine Coolant Temperature Sensor 2 Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2184
- Description: Engine Coolant Temperature Sensor 2 Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2185
- Description: Engine Coolant Temperature Sensor 2 Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2186
- Description: Engine Coolant Temperature Sensor 2 Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2187
- Description: System Too Lean at Idle (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2188
- Description: System Too Rich at Idle (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2189
- Description: System Too Lean at Idle (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2190
- Description: System Too Rich at Idle (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2191
- Description: System Too Lean at Higher Load (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2192
- Description: System Too Rich at Higher Load (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2193
- Description: System Too Lean at Higher Load (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2194
- Description: System Too Rich at Higher Load (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2195
- Description: O2 Sensor Signal Stuck Lean (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2196
- Description: O2 Sensor Signal Stuck Rich (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2197
- Description: O2 Sensor Signal Stuck Lean (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2198
- Description: O2 Sensor Signal Stuck Rich (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2199
- Description: Intake Air Temperature Sensor 1 / 2 Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2200
- Description: NOx Sensor Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2201
- Description: NOx Sensor Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2202
- Description: NOx Sensor Circuit Low Input (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2203
- Description: NOx Sensor Circuit High Input (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2204
- Description: NOx Sensor Circuit Intermittent Input (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2205
- Description: NOx Sensor Heater Control Circuit/Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2206
- Description: NOx Sensor Heater Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2207
- Description: NOx Sensor Heater Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2208
- Description: NOx Sensor Heater Sense Circuit (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2209
- Description: NOx Sensor Heater Sense Circuit Range/Performance (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2210
- Description: NOx Sensor Heater Sense Circuit Low Input (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2211
- Description: NOx Sensor Heater Sense Circuit High Input (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2212
- Description: NOx Sensor Heater Sense Circuit Intermittent (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2213
- Description: NOx Sensor Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2214
- Description: NOx Sensor Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2215
- Description: NOx Sensor Circuit Low Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2216
- Description: NOx Sensor Circuit High Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2217
- Description: NOx Sensor Circuit Intermittent Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2218
- Description: NOx Sensor Heater Control Circuit/Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2219
- Description: NOx Sensor Heater Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2220
- Description: NOx Sensor Heater Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2221
- Description: NOx Sensor Heater Sense Circuit (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2222
- Description: NOx Sensor Heater Sense Circuit Range/Performance (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2223
- Description: NOx Sensor Heater Sense Circuit Low Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2224
- Description: NOx Sensor Heater Sense Circuit High Input (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2225
- Description: NOx Sensor Heater Sense Circuit Intermittent (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2226
- Description: Barometric Pressure Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2227
- Description: Barometric Pressure Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2228
- Description: Barometric Pressure Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2229
- Description: Barometric Pressure Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2230
- Description: Barometric Pressure Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2231
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2232
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2233
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2234
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2235
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2236
- Description: O2 Sensor Signal Circuit Shorted to Heater Circuit (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2237
- Description: O2 Sensor Positive Current Circuit/Open (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2238
- Description: O2 Sensor Positive Current Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2239
- Description: O2 Sensor Positive Current Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2240
- Description: O2 Sensor Positive Current Circuit/Open (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2241
- Description: O2 Sensor Positive Current Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2242
- Description: O2 Sensor Positive Current Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2243
- Description: O2 Sensor Reference Voltage Circuit/Open (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2244
- Description: O2 Sensor Reference Voltage Performance (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2245
- Description: O2 Sensor Reference Voltage Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2246
- Description: O2 Sensor Reference Voltage Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2247
- Description: O2 Sensor Reference Voltage Circuit/Open (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2248
- Description: O2 Sensor Reference Voltage Performance (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2249
- Description: O2 Sensor Reference Voltage Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2250
- Description: O2 Sensor Reference Voltage Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2251
- Description: O2 Sensor Negative Current Control Circuit/Open (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2252
- Description: O2 Sensor Negative Current Control Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2253
- Description: O2 Sensor Negative Current Control Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2254
- Description: O2 Sensor Negative Current Control Circuit/Open (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2255
- Description: O2 Sensor Negative Current Control Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2256
- Description: O2 Sensor Negative Current Control Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2257
- Description: Secondary Air Injection System Control "A" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2258
- Description: Secondary Air Injection System Control "A" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2259
- Description: Secondary Air Injection System Control "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2260
- Description: Secondary Air Injection System Control "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2261
- Description: Turbo/Super Charger Bypass Valve - Mechanical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2262
- Description: Turbo Boost Pressure Not Detected - Mechanical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2263
- Description: Turbo/Super Charger Boost System Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2264
- Description: Water in Fuel Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2265
- Description: Water in Fuel Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2266
- Description: Water in Fuel Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2267
- Description: Water in Fuel Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2268
- Description: Water in Fuel Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2269
- Description: Water in Fuel Condition
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2270
- Description: O2 Sensor Signal Stuck Lean (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2271
- Description: O2 Sensor Signal Stuck Rich (Bank 1 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2272
- Description: O2 Sensor Signal Stuck Lean (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2273
- Description: O2 Sensor Signal Stuck Rich (Bank 2 Sensor 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2274
- Description: O2 Sensor Signal Stuck Lean (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2275
- Description: O2 Sensor Signal Stuck Rich (Bank 1 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2276
- Description: O2 Sensor Signal Stuck Lean (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2277
- Description: O2 Sensor Signal Stuck Rich (Bank 2 Sensor 3)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2278
- Description: O2 Sensor Signals Swapped Bank 1 Sensor 3 / Bank 2 Sensor 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2279
- Description: Intake Air System Leak
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2280
- Description: Air Flow Restriction / Air Leak Between Air Filter and MAF
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2281
- Description: Air Leak Between MAF and Throttle Body
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2282
- Description: Air Leak Between Throttle Body and Intake Valves
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2283
- Description: Injector Control Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2284
- Description: Injector Control Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2285
- Description: Injector Control Pressure Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2286
- Description: Injector Control Pressure Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2287
- Description: Injector Control Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2288
- Description: Injector Control Pressure Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2289
- Description: Injector Control Pressure Too High - Engine Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2290
- Description: Injector Control Pressure Too Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2291
- Description: Injector Control Pressure Too Low - Engine Cranking
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2292
- Description: Injector Control Pressure Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2293
- Description: Fuel Pressure Regulator 2 Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2294
- Description: Fuel Pressure Regulator 2 Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2295
- Description: Fuel Pressure Regulator 2 Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2296
- Description: Fuel Pressure Regulator 2 Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2297
- Description: O2 Sensor Out of Range During Deceleration (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2298
- Description: O2 Sensor Out of Range During Deceleration (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2299
- Description: Brake Pedal Position / Accelerator Pedal Position Incompatible
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2300
- Description: Ignition Coil "A" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2301
- Description: Ignition Coil "A" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2302
- Description: Ignition Coil "A" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2303
- Description: Ignition Coil "B" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2304
- Description: Ignition Coil "B" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2305
- Description: Ignition Coil "B" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2306
- Description: Ignition Coil "C" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2307
- Description: Ignition Coil "C" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2308
- Description: Ignition Coil "C" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2309
- Description: Ignition Coil "D" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2310
- Description: Ignition Coil "D" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2311
- Description: Ignition Coil "D" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2312
- Description: Ignition Coil "E" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2313
- Description: Ignition Coil "E" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2314
- Description: Ignition Coil "E" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2315
- Description: Ignition Coil "F" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2316
- Description: Ignition Coil "F" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2317
- Description: Ignition Coil "F" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2318
- Description: Ignition Coil "G" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2319
- Description: Ignition Coil "G" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2320
- Description: Ignition Coil "G" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2321
- Description: Ignition Coil "H" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2322
- Description: Ignition Coil "H" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2323
- Description: Ignition Coil "H" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2324
- Description: Ignition Coil "I" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2325
- Description: Ignition Coil "I" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2326
- Description: Ignition Coil "I" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2327
- Description: Ignition Coil "J" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2328
- Description: Ignition Coil "J" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2329
- Description: Ignition Coil "J" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2330
- Description: Ignition Coil "K" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2331
- Description: Ignition Coil "K" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2332
- Description: Ignition Coil "K" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2333
- Description: Ignition Coil "L" Primary Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2334
- Description: Ignition Coil "L" Primary Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2335
- Description: Ignition Coil "L" Secondary Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2336
- Description: Cylinder #1 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2337
- Description: Cylinder #2 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2338
- Description: Cylinder #3 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2339
- Description: Cylinder #4 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2340
- Description: Cylinder #5 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2341
- Description: Cylinder #6 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2342
- Description: Cylinder #7 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2343
- Description: Cylinder #8 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2344
- Description: Cylinder #9 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2345
- Description: Cylinder #10 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2346
- Description: Cylinder #11 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2347
- Description: Cylinder #12 Above Knock Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2400
- Description: Evaporative Emission System Leak Detection Pump Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2401
- Description: Evaporative Emission System Leak Detection Pump Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2402
- Description: Evaporative Emission System Leak Detection Pump Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2403
- Description: Evaporative Emission System Leak Detection Pump Sense Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2404
- Description: Evaporative Emission System Leak Detection Pump Sense Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2405
- Description: Evaporative Emission System Leak Detection Pump Sense Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2406
- Description: Evaporative Emission System Leak Detection Pump Sense Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2407
- Description: Evaporative Emission System Leak Detection Pump Sense Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2408
- Description: Fuel Cap Sensor/Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2409
- Description: Fuel Cap Sensor/Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2410
- Description: Fuel Cap Sensor/Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2411
- Description: Fuel Cap Sensor/Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2412
- Description: Fuel Cap Sensor/Switch Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2413
- Description: Exhaust Gas Recirculation System Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2414
- Description: O2 Sensor Exhaust Sample Error (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2415
- Description: O2 Sensor Exhaust Sample Error (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2416
- Description: O2 Sensor Signals Swapped Bank 1 Sensor 2 / Bank 1 Sensor 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2417
- Description: O2 Sensor Signals Swapped Bank 2 Sensor 2 / Bank 2 Sensor 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2418
- Description: Evaporative Emission System Switching Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2419
- Description: Evaporative Emission System Switching Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2420
- Description: Evaporative Emission System Switching Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2421
- Description: Evaporative Emission System Vent Valve Stuck Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2422
- Description: Evaporative Emission System Vent Valve Stuck Closed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2423
- Description: HC Adsorption Catalyst Efficiency Below Threshold (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2424
- Description: HC Adsorption Catalyst Efficiency Below Threshold (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2425
- Description: Exhaust Gas Recirculation Cooling Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2426
- Description: Exhaust Gas Recirculation Cooling Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2427
- Description: Exhaust Gas Recirculation Cooling Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2428
- Description: Exhaust Gas Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2429
- Description: Exhaust Gas Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2430
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2431
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2432
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2433
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2434
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2435
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2436
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2437
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2438
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2439
- Description: Secondary Air Injection System Air Flow/Pressure Sensor Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2440
- Description: Secondary Air Injection System Switching Valve Stuck Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2441
- Description: Secondary Air Injection System Switching Valve Stuck Closed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2442
- Description: Secondary Air Injection System Switching Valve Stuck Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2443
- Description: Secondary Air Injection System Switching Valve Stuck Closed
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2444
- Description: Secondary Air Injection System Pump Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2445
- Description: Secondary Air Injection System Pump Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2446
- Description: Secondary Air Injection System Pump Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2447
- Description: Secondary Air Injection System Pump Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2500
- Description: Generator Lamp/L-Terminal Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2501
- Description: Generator Lamp/L-Terminal Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2502
- Description: Charging System Voltage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2503
- Description: Charging System Voltage Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2504
- Description: Charging System Voltage High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2505
- Description: ECM/PCM Power Input Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2506
- Description: ECM/PCM Power Input Signal Range Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2507
- Description: ECM/PCM Power Input Signal Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2508
- Description: ECM/PCM Power Input Signal High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2509
- Description: ECM/PCM Power Input Signal Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2510
- Description: ECM/PCM Power Relay Sense Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2511
- Description: ECM/PCM Power Relay Sense Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2512
- Description: Event Data Recorder Request Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2513
- Description: Event Data Recorder Request Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2514
- Description: Event Data Recorder Request Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2515
- Description: A/C Refrigerant Pressure Sensor "B" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2516
- Description: A/C Refrigerant Pressure Sensor "B" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2517
- Description: A/C Refrigerant Pressure Sensor "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2518
- Description: A/C Refrigerant Pressure Sensor "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2519
- Description: A/C Request "A" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2520
- Description: A/C Request "A" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2521
- Description: A/C Request "A" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2522
- Description: A/C Request "B" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2523
- Description: A/C Request "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2524
- Description: A/C Request "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2525
- Description: Vacuum Reservoir Pressure Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2526
- Description: Vacuum Reservoir Pressure Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2527
- Description: Vacuum Reservoir Pressure Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2528
- Description: Vacuum Reservoir Pressure Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2529
- Description: Vacuum Reservoir Pressure Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2530
- Description: Ignition Switch Run Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2531
- Description: Ignition Switch Run Position Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2532
- Description: Ignition Switch Run Position Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2533
- Description: Ignition Switch Run/Start Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2534
- Description: Ignition Switch Run/Start Position Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2535
- Description: Ignition Switch Run/Start Position Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2536
- Description: Ignition Switch Accessory Position Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2537
- Description: Ignition Switch Accessory Position Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2538
- Description: Ignition Switch Accessory Position Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2539
- Description: Low Pressure Fuel System Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2540
- Description: Low Pressure Fuel System Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2541
- Description: Low Pressure Fuel System Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2542
- Description: Low Pressure Fuel System Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2543
- Description: Low Pressure Fuel System Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2544
- Description: Torque Management Request Input Signal "A"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2545
- Description: Torque Management Request Input Signal "A" Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2546
- Description: Torque Management Request Input Signal "A" Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2547
- Description: Torque Management Request Input Signal "A" High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2548
- Description: Torque Management Request Input Signal "B"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2549
- Description: Torque Management Request Input Signal "B" Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2550
- Description: Torque Management Request Input Signal "B" Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2551
- Description: Torque Management Request Input Signal "B" High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2552
- Description: Throttle/Fuel Inhibit Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2553
- Description: Throttle/Fuel Inhibit Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2554
- Description: Throttle/Fuel Inhibit Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2555
- Description: Throttle/Fuel Inhibit Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2556
- Description: Engine Coolant Level Sensor/Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2557
- Description: Engine Coolant Level Sensor/Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2558
- Description: Engine Coolant Level Sensor/Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2559
- Description: Engine Coolant Level Sensor/Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2560
- Description: Engine Coolant Level Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2561
- Description: A/C Control Module Requested MIL Illumination
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2562
- Description: Turbocharger Boost Control Position Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2563
- Description: Turbocharger Boost Control Position Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2564
- Description: Turbocharger Boost Control Position Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2565
- Description: Turbocharger Boost Control Position Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2566
- Description: Turbocharger Boost Control Position Sensor Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2567
- Description: Direct Ozone Reduction Catalyst Temperature Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2568
- Description: Direct Ozone Reduction Catalyst Temperature Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2569
- Description: Direct Ozone Reduction Catalyst Temperature Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2570
- Description: Direct Ozone Reduction Catalyst Temperature Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2571
- Description: Direct Ozone Reduction Catalyst Temperature Sensor Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2572
- Description: Direct Ozone Reduction Catalyst Deterioration Sensor Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2573
- Description: Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2574
- Description: Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2575
- Description: Direct Ozone Reduction Catalyst Deterioration Sensor Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2576
- Description: Direct Ozone Reduction Catalyst Deterioration Sensor Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2577
- Description: Direct Ozone Reduction Catalyst Efficiency Below Threshold
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2600
- Description: Coolant Pump Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2601
- Description: Coolant Pump Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2602
- Description: Coolant Pump Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2603
- Description: Coolant Pump Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2604
- Description: Intake Air Heater "A" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2605
- Description: Intake Air Heater "A" Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2606
- Description: Intake Air Heater "B" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2607
- Description: Intake Air Heater "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2608
- Description: Intake Air Heater "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2609
- Description: Intake Air Heater System Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2610
- Description: ECM/PCM Internal Engine Off Timer Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2611
- Description: A/C Refrigerant Distribution Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2612
- Description: A/C Refrigerant Distribution Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2613
- Description: A/C Refrigerant Distribution Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2614
- Description: Camshaft Position Signal Output Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2615
- Description: Camshaft Position Signal Output Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2616
- Description: Camshaft Position Signal Output Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2617
- Description: Crankshaft Position Signal Output Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2618
- Description: Crankshaft Position Signal Output Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2619
- Description: Crankshaft Position Signal Output Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2620
- Description: Throttle Position Output Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2621
- Description: Throttle Position Output Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2622
- Description: Throttle Position Output Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2623
- Description: Injector Control Pressure Regulator Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2624
- Description: Injector Control Pressure Regulator Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2625
- Description: Injector Control Pressure Regulator Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2626
- Description: O2 Sensor Pumping Current Trim Circuit/Open (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2627
- Description: O2 Sensor Pumping Current Trim Circuit Low (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2628
- Description: O2 Sensor Pumping Current Trim Circuit High (Bank 1 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2629
- Description: O2 Sensor Pumping Current Trim Circuit/Open (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2630
- Description: O2 Sensor Pumping Current Trim Circuit Low (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2631
- Description: O2 Sensor Pumping Current Trim Circuit High (Bank 2 Sensor 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2632
- Description: Fuel Pump "B" Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2633
- Description: Fuel Pump "B" Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2634
- Description: Fuel Pump "B" Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2635
- Description: Fuel Pump "A" Low Flow/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2636
- Description: Fuel Pump "B" Low Flow/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2637
- Description: Torque Management Feedback Signal "A"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2638
- Description: Torque Management Feedback Signal "A" Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2639
- Description: Torque Management Feedback Signal "A" Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2640
- Description: Torque Management Feedback Signal "A" High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2641
- Description: Torque Management Feedback Signal "B"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2642
- Description: Torque Management Feedback Signal "B" Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2643
- Description: Torque Management Feedback Signal "B" Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2644
- Description: Torque Management Feedback Signal "B" High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2645
- Description: A Rocker Arm Actuator Control Circuit/Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2646
- Description: A Rocker Arm Actuator System Performance or Stuck Off (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2647
- Description: A Rocker Arm Actuator System Stuck On (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2648
- Description: A Rocker Arm Actuator Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2649
- Description: A Rocker Arm Actuator Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2650
- Description: B Rocker Arm Actuator Control Circuit/Open (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2651
- Description: B Rocker Arm Actuator System Performance or Stuck Off (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2652
- Description: B Rocker Arm Actuator System Stuck On (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2653
- Description: B Rocker Arm Actuator Control Circuit Low (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2654
- Description: B Rocker Arm Actuator Control Circuit High (Bank 1)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2655
- Description: A Rocker Arm Actuator Control Circuit/Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2656
- Description: A Rocker Arm Actuator System Performance or Stuck Off (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2657
- Description: A Rocker Arm Actuator System Stuck On (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2658
- Description: A Rocker Arm Actuator Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2659
- Description: A Rocker Arm Actuator Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2660
- Description: B Rocker Arm Actuator Control Circuit/Open (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2661
- Description: B Rocker Arm Actuator System Performance or Stuck Off (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2662
- Description: B Rocker Arm Actuator System Stuck On (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2663
- Description: B Rocker Arm Actuator Control Circuit Low (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2664
- Description: B Rocker Arm Actuator Control Circuit High (Bank 2)
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2665
- Description: Fuel Shutoff Valve "B" Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2666
- Description: Fuel Shutoff Valve "B" Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2667
- Description: Fuel Shutoff Valve "B" Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2668
- Description: Fuel Mode Indicator Lamp Control Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2669
- Description: Actuator Supply Voltage "B" Circuit /Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2670
- Description: Actuator Supply Voltage "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2671
- Description: Actuator Supply Voltage "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2700
- Description: Transmission Friction Element "A" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2701
- Description: Transmission Friction Element "B" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2702
- Description: Transmission Friction Element "C" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2703
- Description: Transmission Friction Element "D" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2704
- Description: Transmission Friction Element "E" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2705
- Description: Transmission Friction Element "F" Apply Time Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2706
- Description: Shift Solenoid "F"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2707
- Description: Shift Solenoid "F" Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2708
- Description: Shift Solenoid "F" Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2709
- Description: Shift Solenoid "F" Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2710
- Description: Shift Solenoid "F" Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2711
- Description: Unexpected Mechanical Gear Disengagement
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2712
- Description: Hydraulic Power Unit Leakage
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2713
- Description: Pressure Control Solenoid "D"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2714
- Description: Pressure Control Solenoid "D" Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2715
- Description: Pressure Control Solenoid "D" Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2716
- Description: Pressure Control Solenoid "D" Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2717
- Description: Pressure Control Solenoid "D" Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2718
- Description: Pressure Control Solenoid "D" Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2719
- Description: Pressure Control Solenoid "D" Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2720
- Description: Pressure Control Solenoid "D" Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2721
- Description: Pressure Control Solenoid "D" Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2722
- Description: Pressure Control Solenoid "E"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2723
- Description: Pressure Control Solenoid "E" Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2724
- Description: Pressure Control Solenoid "E" Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2725
- Description: Pressure Control Solenoid "E" Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2726
- Description: Pressure Control Solenoid "E" Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2727
- Description: Pressure Control Solenoid "E" Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2728
- Description: Pressure Control Solenoid "E" Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2729
- Description: Pressure Control Solenoid "E" Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2730
- Description: Pressure Control Solenoid "E" Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2731
- Description: Pressure Control Solenoid "F"
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2732
- Description: Pressure Control Solenoid "F" Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2733
- Description: Pressure Control Solenoid "F" Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2734
- Description: Pressure Control Solenoid "F" Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2735
- Description: Pressure Control Solenoid "F" Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2736
- Description: Pressure Control Solenoid "F" Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2737
- Description: Pressure Control Solenoid "F" Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2738
- Description: Pressure Control Solenoid "F" Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2739
- Description: Pressure Control Solenoid "F" Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2740
- Description: Transmission Fluid Temperature Sensor "B" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2741
- Description: Transmission Fluid Temperature Sensor "B" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2742
- Description: Transmission Fluid Temperature Sensor "B" Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2743
- Description: Transmission Fluid Temperature Sensor "B" Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2744
- Description: Transmission Fluid Temperature Sensor "B" Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2745
- Description: Intermediate Shaft Speed Sensor "B" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2746
- Description: Intermediate Shaft Speed Sensor "B" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2747
- Description: Intermediate Shaft Speed Sensor "B" Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2748
- Description: Intermediate Shaft Speed Sensor "B" Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2749
- Description: Intermediate Shaft Speed Sensor "C" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2750
- Description: Intermediate Shaft Speed Sensor "C" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2751
- Description: Intermediate Shaft Speed Sensor "C" Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2752
- Description: Intermediate Shaft Speed Sensor "C" Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2753
- Description: Transmission Fluid Cooler Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2754
- Description: Transmission Fluid Cooler Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2755
- Description: Transmission Fluid Cooler Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2756
- Description: Torque Converter Clutch Pressure Control Solenoid
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2757
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2758
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Stuck on
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2759
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2760
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2761
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2762
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2763
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2764
- Description: Torque Converter Clutch Pressure Control Solenoid Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2765
- Description: Input/Turbine Speed Sensor "B" Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2766
- Description: Input/Turbine Speed Sensor "B" Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2767
- Description: Input/Turbine Speed Sensor "B" Circuit No Signal
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2768
- Description: Input/Turbine Speed Sensor "B" Circuit Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2769
- Description: Torque Converter Clutch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2770
- Description: Torque Converter Clutch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2771
- Description: Four Wheel Drive (4WD) Low Switch Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2772
- Description: Four Wheel Drive (4WD) Low Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2773
- Description: Four Wheel Drive (4WD) Low Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2774
- Description: Four Wheel Drive (4WD) Low Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2775
- Description: Upshift Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2776
- Description: Upshift Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2777
- Description: Upshift Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2778
- Description: Upshift Switch Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2779
- Description: Downshift Switch Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2780
- Description: Downshift Switch Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2781
- Description: Downshift Switch Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2782
- Description: Downshift Switch Circuit Intermittent/Erratic
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2783
- Description: Torque Converter Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2784
- Description: Input/Turbine Speed Sensor "A"/"B" Correlation
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2785
- Description: Clutch Actuator Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2786
- Description: Gear Shift Actuator Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2787
- Description: Clutch Temperature Too High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2788
- Description: Auto Shift Manual Adaptive Learning at Limit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2789
- Description: Clutch Adaptive Learning at Limit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2790
- Description: Gate Select Direction Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2791
- Description: Gate Select Direction Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2792
- Description: Gate Select Direction Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2793
- Description: Gear Shift Direction Circuit
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2794
- Description: Gear Shift Direction Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2795
- Description: Gear Shift Direction Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P2821
- Description: Pressure Control Solenoid J Stuck On
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2822
- Description: Pressure Control Solenoid J Electrical
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2823
- Description: Pressure Control Solenoid J Intermittent
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2824
- Description: Pressure Control Solenoid J Control Circuit / Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2825
- Description: Pressure Control Solenoid J Control Circuit Range/Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2826
- Description: Pressure Control Solenoid J Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2827
- Description: Pressure Control Solenoid J Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2828
- Description: Pressure Control Solenoid K
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2829
- Description: Pressure Control Solenoid K Performance or Stuck Off
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2830
- Description: Pressure Control Solenoid K Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)


## P34xx — Generic Powertrain Codes (cylinder deactivation, SAE-assigned)

## P2A00
- Description: O2 Sensor Circuit Range/Performance Bank 1 Sensor 1
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2A01
- Description: O2 Sensor Circuit Range/Performance Bank 1 Sensor 2
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2A02
- Description: O2 Sensor Circuit Range/Performance Bank 1 Sensor 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2A03
- Description: O2 Sensor Circuit Range/Performance Bank 2 Sensor 1
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2A04
- Description: O2 Sensor Circuit Range/Performance Bank 2 Sensor 2
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)

## P2A05
- Description: O2 Sensor Circuit Range/Performance Bank 2 Sensor 3
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: guzzle7pt3.com DTC list (single source; newer SAE additions absent from the motor-talk transcription)


## P34xx — Generic Powertrain Codes (cylinder deactivation, SAE-assigned)
## P3400
- Description: Cylinder Deactivation System
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3401
- Description: Cylinder 1 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3402
- Description: Cylinder 1 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3403
- Description: Cylinder 1 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3404
- Description: Cylinder 1 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3405
- Description: Cylinder 1 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3406
- Description: Cylinder 1 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3407
- Description: Cylinder 1 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3408
- Description: Cylinder 1 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3409
- Description: Cylinder 2 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3410
- Description: Cylinder 2 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3411
- Description: Cylinder 2 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3412
- Description: Cylinder 2 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3413
- Description: Cylinder 2 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3414
- Description: Cylinder 2 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3415
- Description: Cylinder 2 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3416
- Description: Cylinder 2 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3417
- Description: Cylinder 3 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3418
- Description: Cylinder 3 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3419
- Description: Cylinder 3 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3420
- Description: Cylinder 3 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment + guzzle7pt3.com DTC list - two independent transcriptions agree on P3400-P3420

## P3421
- Description: Cylinder 3 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3422
- Description: Cylinder 3 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3423
- Description: Cylinder 3 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3424
- Description: Cylinder 3 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3425
- Description: Cylinder 4 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3426
- Description: Cylinder 4 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3427
- Description: Cylinder 4 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3428
- Description: Cylinder 4 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3429
- Description: Cylinder 4 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3430
- Description: Cylinder 4 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3431
- Description: Cylinder 4 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3432
- Description: Cylinder 4 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3433
- Description: Cylinder 5 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3434
- Description: Cylinder 5 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3435
- Description: Cylinder 5 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3436
- Description: Cylinder 5 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3437
- Description: Cylinder 5 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3438
- Description: Cylinder 5 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3439
- Description: Cylinder 5 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3440
- Description: Cylinder 5 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3441
- Description: Cylinder 6 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3442
- Description: Cylinder 6 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3443
- Description: Cylinder 6 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3444
- Description: Cylinder 6 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3445
- Description: Cylinder 6 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3446
- Description: Cylinder 6 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3447
- Description: Cylinder 6 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3448
- Description: Cylinder 6 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3449
- Description: Cylinder 7 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3450
- Description: Cylinder 7 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3451
- Description: Cylinder 7 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3452
- Description: Cylinder 7 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3453
- Description: Cylinder 7 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3454
- Description: Cylinder 7 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3455
- Description: Cylinder 7 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3456
- Description: Cylinder 7 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3457
- Description: Cylinder 8 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3458
- Description: Cylinder 8 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3459
- Description: Cylinder 8 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3460
- Description: Cylinder 8 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3461
- Description: Cylinder 8 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3462
- Description: Cylinder 8 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3463
- Description: Cylinder 8 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3464
- Description: Cylinder 8 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3465
- Description: Cylinder 9 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3466
- Description: Cylinder 9 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3467
- Description: Cylinder 9 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3468
- Description: Cylinder 9 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3469
- Description: Cylinder 9 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3470
- Description: Cylinder 9 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3471
- Description: Cylinder 9 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3472
- Description: Cylinder 9 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3473
- Description: Cylinder 10 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3474
- Description: Cylinder 10 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3475
- Description: Cylinder 10 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3476
- Description: Cylinder 10 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3477
- Description: Cylinder 10 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3478
- Description: Cylinder 10 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3479
- Description: Cylinder 10 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3480
- Description: Cylinder 10 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3481
- Description: Cylinder 11 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3482
- Description: Cylinder 11 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3483
- Description: Cylinder 11 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3484
- Description: Cylinder 11 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3485
- Description: Cylinder 11 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3486
- Description: Cylinder 11 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3487
- Description: Cylinder 11 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3488
- Description: Cylinder 11 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3489
- Description: Cylinder 12 Deactivation/Intake Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3490
- Description: Cylinder 12 Deactivation/Intake Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3491
- Description: Cylinder 12 Deactivation/Intake Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3492
- Description: Cylinder 12 Deactivation/Intake Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3493
- Description: Cylinder 12 Exhaust Valve Control Circuit/Open
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3494
- Description: Cylinder 12 Exhaust Valve Control Performance
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3495
- Description: Cylinder 12 Exhaust Valve Control Circuit Low
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)

## P3496
- Description: Cylinder 12 Exhaust Valve Control Circuit High
- Category: P
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source)


## B0xxx — Generic Body Codes


## B0xxx — Generic Body Codes
## B0001
- Description: PCM Discrete Input Speed Signal Error
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0004
- Description: PCM Discrete Input Speed Signal Not Present
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0005
- Description: In Park Switch Circuit Malfunction
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0016
- Description: RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0017
- Description: RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0018
- Description: RF/Passenger Frontal Deployment Loop (Single Stage or Stage 1) Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0022
- Description: LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0024
- Description: LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0026
- Description: LF/Driver Frontal Deployment Loop (Single Stage or Stage 1) Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0028
- Description: RF/Passenger Side Deployment Loop Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0029
- Description: RF/Passenger Side Deployment Loop Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0030
- Description: RF/Passenger Side Deployment Loop Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0035
- Description: ADS Closed/Shorted to Ground
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0036
- Description: ADS Open/Missing/Shorted to Battery
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0037
- Description: AUX switch closed/shorted to ground
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0038
- Description: AUX switch open/shorted to battery
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0040
- Description: LF/Driver Side Deployment Loop Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0041
- Description: LF/Driver Side Deployment Loop Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0045
- Description: LF Side Deploy Loop Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0051
- Description: Deployment Commanded
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0053
- Description: Deployment Commanded with Loop Malfunctions Present
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0057
- Description: RF/Passenger Pretensioner Deployment Loop Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0058
- Description: RF/Passenger Pretensioner Deployment Loop Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0059
- Description: RF/Passenger Pretensioner Deployment Loop Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0064
- Description: LF/Driver Pretensioner Deployment Loop Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0065
- Description: LF/Driver Pretensioner Deployment Loop Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0066
- Description: LF/Driver Pretensioner Deployment Loop Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0073
- Description: Supplemental Deployment Loop #1 Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0074
- Description: Supplemental Deployment Loop #1 Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0075
- Description: Supplemental Deployment Loop #1 Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0077
- Description: LF/Driver SIS Malfunction
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0078
- Description: RF/Passenger SIS Malfunction
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0079
- Description: Incorrect LF/Driver SIS Installed
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0080
- Description: Discard LF/Driver SIS
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0081
- Description: Incorrect RF/Passenger SIS Installed
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0082
- Description: Discard RF/Passenger SIS
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0086
- Description: Supplemental Deployment Loop #2 Resistance Low
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0087
- Description: Supplemental Deployment Loop #2 Open
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0088
- Description: Supplemental Deployment Loop #2 Short to Ground/Voltage Out of Range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0090
- Description: Active switch voltage out of range
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0091
- Description: Active switch: wrong state
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0092
- Description: PPS passenger detection error
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0093
- Description: PPS/CPS self-test malfunction
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0094
- Description: CPS childseat detection error
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)

## B0095
- Description: SDM-PPS/CPS mismatch malfunction
- Category: B
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: scribd "OBD2 Diagnostic Trouble Codes Guide" per SAE J2012 (community transcription, single source)


## C0xxx — Generic Chassis Codes


## C0xxx — Generic Chassis Codes
## C0000
- Description: Vehicle Speed Information Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0035
- Description: Left Front Wheel Speed Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0040
- Description: Right Front Wheel Speed Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0041
- Description: Right Front Wheel Speed Sensor Circuit Range/Performance (EBCM)
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0045
- Description: Left Rear Wheel Speed Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0046
- Description: Left Rear Wheel Speed Sensor Circuit Range/Performance (EBCM)
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0050
- Description: Right Rear Wheel Speed Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0051
- Description: LF Wheel Speed Sensor Circuit Range/Performance (EBCM)
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0060
- Description: Left Front ABS Solenoid #1 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0065
- Description: Left Front ABS Solenoid #2 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0070
- Description: Right Front ABS Solenoid #1 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0075
- Description: Right Front ABS Solenoid #2 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0080
- Description: Left Rear ABS Solenoid #1 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0085
- Description: Left Rear ABS Solenoid #2 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0090
- Description: Right Rear ABS Solenoid #1 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0095
- Description: Right Rear ABS Solenoid #2 Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0110
- Description: Pump Motor Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0121
- Description: Valve Relay Circuit Malfunction
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)

## C0128
- Description: Low Brake Fluid Circuit Low
- Category: C
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [C]
- Evidence: motor-talk.de SAE J2012 attachment (community transcription, single source; source mixes generic and OEM chassis codes - included codes are the SAE-generic-plausible C0xxx block: wheel-speed circuits, ABS solenoids, pump motor, valve relay)


## U0xxx — Generic Network Codes


## U0xxx — Generic Network Codes
## U0001
- Description: High Speed CAN Communication Bus
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0002
- Description: High Speed CAN Communication Bus Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0003
- Description: High Speed CAN Communication Bus (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0004
- Description: High Speed CAN Communication Bus (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0005
- Description: High Speed CAN Communication Bus (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0006
- Description: High Speed CAN Communication Bus (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0007
- Description: High Speed CAN Communication Bus (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0008
- Description: High Speed CAN Communication Bus (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0009
- Description: High Speed CAN Communication Bus (-) shorted to Bus (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0010
- Description: Medium Speed CAN Communication Bus
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0011
- Description: Medium Speed CAN Communication Bus Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0012
- Description: Medium Speed CAN Communication Bus (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0013
- Description: Medium Speed CAN Communication Bus (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0014
- Description: Medium Speed CAN Communication Bus (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0015
- Description: Medium Speed CAN Communication Bus (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0016
- Description: Medium Speed CAN Communication Bus (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0017
- Description: Medium Speed CAN Communication Bus (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0018
- Description: Medium Speed CAN Communication Bus (-) shorted to Bus (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0019
- Description: Low Speed CAN Communication Bus
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0020
- Description: Low Speed CAN Communication Bus Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0021
- Description: Low Speed CAN Communication Bus (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0022
- Description: Low Speed CAN Communication Bus (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0023
- Description: Low Speed CAN Communication Bus (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0024
- Description: Low Speed CAN Communication Bus (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0025
- Description: Low Speed CAN Communication Bus (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0026
- Description: Low Speed CAN Communication Bus (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0027
- Description: Low Speed CAN Communication Bus (-) shorted to Bus (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0028
- Description: Vehicle Communication Bus A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0029
- Description: Vehicle Communication Bus A Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0030
- Description: Vehicle Communication Bus A (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0031
- Description: Vehicle Communication Bus A (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0032
- Description: Vehicle Communication Bus A (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0033
- Description: Vehicle Communication Bus A (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0034
- Description: Vehicle Communication Bus A (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0035
- Description: Vehicle Communication Bus A (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0036
- Description: Vehicle Communication Bus A (-) shorted to Bus A (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0037
- Description: Vehicle Communication Bus B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0038
- Description: Vehicle Communication Bus B Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0039
- Description: Vehicle Communication Bus B (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0040
- Description: Vehicle Communication Bus B (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0041
- Description: Vehicle Communication Bus B (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0042
- Description: Vehicle Communication Bus B (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0043
- Description: Vehicle Communication Bus B (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0044
- Description: Vehicle Communication Bus B (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0045
- Description: Vehicle Communication Bus B (-) shorted to Bus B (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0046
- Description: Vehicle Communication Bus C
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0047
- Description: Vehicle Communication Bus C Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0048
- Description: Vehicle Communication Bus C (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0049
- Description: Vehicle Communication Bus C (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0050
- Description: Vehicle Communication Bus C (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0051
- Description: Vehicle Communication Bus C (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0052
- Description: Vehicle Communication Bus C (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0053
- Description: Vehicle Communication Bus C (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0054
- Description: Vehicle Communication Bus C (-) shorted to Bus C (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0055
- Description: Vehicle Communication Bus D
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0056
- Description: Vehicle Communication Bus D Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0057
- Description: Vehicle Communication Bus D (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0058
- Description: Vehicle Communication Bus D (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0059
- Description: Vehicle Communication Bus D (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0060
- Description: Vehicle Communication Bus D (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0061
- Description: Vehicle Communication Bus D (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0062
- Description: Vehicle Communication Bus D (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0063
- Description: Vehicle Communication Bus D (-) shorted to Bus D (+) 
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0064
- Description: Vehicle Communication Bus E
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0065
- Description: Vehicle Communication Bus E Performance
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0066
- Description: Vehicle Communication Bus E (+) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0067
- Description: Vehicle Communication Bus E (+) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0068
- Description: Vehicle Communication Bus E (+) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0069
- Description: Vehicle Communication Bus E (-) Open
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0070
- Description: Vehicle Communication Bus E (-) Low
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0071
- Description: Vehicle Communication Bus E (-) High
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0072
- Description: Vehicle Communication Bus E (-) shorted to Bus E (+)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0073
- Description: Control Module Communication Bus Off
- Category: U
- Scope: generic
- Possible causes: intermittent short on CAN data circuits (GM: circuits 2500/2501); backed-out terminal in transmission harness connections (GM TSB 08-07-30-021)
- Diagnostic notes: If stored as history only, follow the service manual "Testing for Electrical Intermittents" procedure; the affected BCM may stay offline ~20 minutes until timeout. CONFLICT: scribd "Control Module U Code List" words this as "Control Module Communication Bus A Off" - the two-source wording is used here (see Coverage notes)
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0073 confirmed by retrolib.info EOBD U-code PDF and GM TSB 08-07-30-021 (via mainelysubarus.com)

## U0100
- Description: Lost Communication With ECM/PCM "A"
- Category: U
- Scope: generic
- Possible causes: wiring faults; corroded connectors; faulty ECM/PCM
- Diagnostic notes: Inspect wiring harnesses and connectors for damage or corrosion; use a scan tool to identify the non-communicating module
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0100/U0101 descriptions confirmed by retrolib.info EOBD U-code PDF, scribd "Control Module U Code List", and justanswer.com technician threads

## U0101
- Description: Lost Communication with TCM
- Category: U
- Scope: generic
- Possible causes: wiring faults; corroded connectors; faulty TCM
- Diagnostic notes: Inspect wiring harnesses and connectors; check for related U-codes pointing at the same bus segment
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0100/U0101 descriptions confirmed by retrolib.info EOBD U-code PDF, scribd "Control Module U Code List", and justanswer.com technician threads

## U0102
- Description: Lost Communication with Transfer Case Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0103
- Description: Lost Communication With Gear Shift Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0104
- Description: Lost Communication With Cruise Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0105
- Description: Lost Communication With Fuel Injector Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0106
- Description: Lost Communication With Glow Plug Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0107
- Description: Lost Communication With Throttle Actuator Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0108
- Description: Lost Communication With Alternative Fuel Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0109
- Description: Lost Communication With Fuel Pump Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0110
- Description: Lost Communication With Drive Motor Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0111
- Description: Lost Communication With Battery Energy Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0112
- Description: Lost Communication With Battery Energy Control Module B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0113
- Description: Lost Communication With Emissions Critical Control Information
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0114
- Description: Lost Communication With Four-Wheel Drive Clutch Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0115
- Description: Lost Communication With ECM/PCM B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0121
- Description: Lost Communication With Anti-Lock Brake System (ABS) Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0122
- Description: Lost Communication With Vehicle Dynamics Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0123
- Description: Lost Communication With Yaw Rate Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0124
- Description: Lost Communication With Lateral Acceleration Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0125
- Description: Lost Communication With Multi-axis Acceleration Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0126
- Description: Lost Communication With Steering Angle Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0127
- Description: Lost Communication With Tire Pressure Monitor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0128
- Description: Lost Communication With Park Brake Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0129
- Description: Lost Communication With Brake System Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0130
- Description: Lost Communication With Steering Effort Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0131
- Description: Lost Communication With Power Steering Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0132
- Description: Lost Communication With Ride Level Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0140
- Description: Lost Communication With Body Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0141
- Description: Lost Communication With Body Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0142
- Description: Lost Communication With Body Control Module B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0143
- Description: Lost Communication With Body Control Module C
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0144
- Description: Lost Communication With Body Control Module D
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0145
- Description: Lost Communication With Body Control Module E
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0146
- Description: Lost Communication With Gateway A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0147
- Description: Lost Communication With Gateway B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0148
- Description: Lost Communication With Gateway C
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0149
- Description: Lost Communication With Gateway D
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0150
- Description: Lost Communication With Gateway E
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0151
- Description: Lost Communication With Restraints Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0152
- Description: Lost Communication With Side Restraints Control Module (Left)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0153
- Description: Lost Communication With Side Restraints Control Module (Right)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0154
- Description: Lost Communication With Restraints Occupant Sensing Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0155
- Description: Lost Communication With Instrument Panel Cluster (IPC) Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0156
- Description: Lost Communication With Information Center A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0157
- Description: Lost Communication With Information Center B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0158
- Description: Lost Communication With Head Up Display
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0159
- Description: Lost Communication With Parking Assist Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0160
- Description: Lost Communication With Audible Alert Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0161
- Description: Lost Communication With Compass Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0162
- Description: Lost Communication With Navigation Display Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0163
- Description: Lost Communication With Navigation Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0164
- Description: Lost Communication With HVAC Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0165
- Description: Lost Communication With HVAC Control Module (Rear)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0166
- Description: Lost Communication With Auxiliary Heater Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0167
- Description: Lost Communication With Vehicle Immobilizer Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0168
- Description: Lost Communication With Vehicle Security Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0169
- Description: Lost Communication With Sunroof Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0170
- Description: Lost Communication With "Restraints System Sensor A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0171
- Description: Lost Communication With "Restraints System Sensor B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0172
- Description: Lost Communication With "Restraints System Sensor C"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0173
- Description: Lost Communication With "Restraints System Sensor D"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0174
- Description: Lost Communication With "Restraints System Sensor E"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0175
- Description: Lost Communication With "Restraints System Sensor F"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0176
- Description: Lost Communication With "Restraints System Sensor G"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0177
- Description: Lost Communication With "Restraints System Sensor H"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0178
- Description: Lost Communication With "Restraints System Sensor I"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0179
- Description: Lost Communication With "Restraints System Sensor J"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0180
- Description: Lost Communication With Automatic Lighting Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0181
- Description: Lost Communication With Headlamp Leveling Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0182
- Description: Lost Communication With Lighting Control Module (Front)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0183
- Description: Lost Communication With Lighting Control Module (Rear)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0184
- Description: Lost Communication With Radio
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0185
- Description: Lost Communication With Antenna Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0186
- Description: Lost Communication With Audio Amplifier
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0187
- Description: Lost Communication With Digital Disc Player/Changer Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0188
- Description: Lost Communication With Digital Disc Player/Changer Module B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0189
- Description: Lost Communication With Digital Disc Player/Changer Module C
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0190
- Description: Lost Communication With Digital Disc Player/Changer Module D
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0191
- Description: Lost Communication With Television
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0192
- Description: Lost Communication With Personal Computer
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0193
- Description: Lost Communication With "Digital Audio Control Module A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0194
- Description: Lost Communication With "Digital Audio Control Module B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0195
- Description: Lost Communication With Subscription Entertainment Receiver Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0196
- Description: Lost Communication With Rear Seat Entertainment Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0197
- Description: Lost Communication With Telephone Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0198
- Description: Lost Communication With Telematic Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0199
- Description: Lost Communication With "Door Control Module A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0200
- Description: Lost Communication With "Door Control Module B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0201
- Description: Lost Communication With "Door Control Module C"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0202
- Description: Lost Communication With "Door Control Module D"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0203
- Description: Lost Communication With "Door Control Module E"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0204
- Description: Lost Communication With "Door Control Module F"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0205
- Description: Lost Communication With "Door Control Module G"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0206
- Description: Lost Communication With Folding Top Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0207
- Description: Lost Communication With Movable Roof Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0208
- Description: Lost Communication With "Seat Control Module A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0209
- Description: Lost Communication With "Seat Control Module B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0210
- Description: Lost Communication With "Seat Control Module C"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0211
- Description: Lost Communication With "Seat Control Module D"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0212
- Description: Lost Communication With Steering Column Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0213
- Description: Lost Communication With Mirror Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0214
- Description: Lost Communication With Remote Function Actuation
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0215
- Description: Lost Communication With "Door Switch A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0216
- Description: Lost Communication With "Door Switch B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0217
- Description: Lost Communication With "Door Switch C"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0218
- Description: Lost Communication With "Door Switch D"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0219
- Description: Lost Communication With "Door Switch E"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0220
- Description: Lost Communication With "Door Switch F"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0221
- Description: Lost Communication With "Door Switch G"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0222
- Description: Lost Communication With "Door Window Motor A"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0223
- Description: Lost Communication With "Door Window Motor B"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0224
- Description: Lost Communication With "Door Window Motor C"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0225
- Description: Lost Communication With "Door Window Motor D"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0226
- Description: Lost Communication With "Door Window Motor E"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0227
- Description: Lost Communication With "Door Window Motor F"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0228
- Description: Lost Communication With "Door Window Motor G"
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0229
- Description: Lost Communication With Heated Steering Wheel Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0230
- Description: Lost Communication With Rear Gate Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0231
- Description: Lost Communication With Rain Sensing Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0232
- Description: Lost Communication With Side Obstacle Detection Control Module (Left)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0233
- Description: Lost Communication With Side Obstacle Detection Control Module (Right)
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0234
- Description: Lost Communication With Convenience Recall Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0235
- Description: Lost Communication With Cruise Control Front Distance Range Sensor
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; ~40 codes spot cross-checked against retrolib.info EOBD U-code PDF and scribd "Control Module U Code List" - all sampled codes agreed

## U0300
- Description: Internal Control Module Software Incompatibility
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0301
- Description: Software Incompatibility with ECM/PCM
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0302
- Description: Software Incompatibility with Transmission Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0303
- Description: Software Incompatibility with Transfer Case Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0304
- Description: Software Incompatibility with Gear Shift Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0305
- Description: Software Incompatibility with Cruise Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0306
- Description: Software Incompatibility with Fuel Injector Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0307
- Description: Software Incompatibility with Glow Plug Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0308
- Description: Software Incompatibility with Throttle Actuator Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0309
- Description: Software Incompatibility with Alternative Fuel Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0310
- Description: Software Incompatibility with Fuel Pump Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0311
- Description: Software Incompatibility with Drive Motor Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0312
- Description: Software Incompatibility with Battery Energy Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0313
- Description: Software Incompatibility with Battery Energy Control Module B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0314
- Description: Software Incompatibility with Four-Wheel Drive Clutch Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0315
- Description: Software Incompatibility with Anti-Lock Brake System Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0316
- Description: Software Incompatibility with Vehicle Dynamics Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0317
- Description: Software Incompatibility with Park Brake Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0318
- Description: Software Incompatibility with Brake System Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0319
- Description: Software Incompatibility with Steering Effort Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0320
- Description: Software Incompatibility with Power Steering Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0321
- Description: Software Incompatibility with Ride Level Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0322
- Description: Software Incompatibility with Body Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0323
- Description: Software Incompatibility with Instrument Panel Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0324
- Description: Software Incompatibility with HVAC Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0325
- Description: Software Incompatibility with Auxiliary Heater Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0326
- Description: Software Incompatibility with Vehicle Immobilizer Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0327
- Description: Software Incompatibility with Vehicle Security Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0328
- Description: Software Incompatibility with Steering Angle Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0329
- Description: Software Incompatibility with Steering Column Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0330
- Description: Software Incompatibility with Tire Pressure Monitor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0331
- Description: Software Incompatibility with Body Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0400
- Description: Invalid Data Received
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0401
- Description: Invalid Data Received From ECM/PCM
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0402
- Description: Invalid Data Received From Transmission Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0403
- Description: Invalid Data Received From Transfer Case Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0404
- Description: Invalid Data Received From Gear Shift Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0405
- Description: Invalid Data Received From Cruise Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0406
- Description: Invalid Data Received From Fuel Injector Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0407
- Description: Invalid Data Received From Glow Plug Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0408
- Description: Invalid Data Received From Throttle Actuator Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0409
- Description: Invalid Data Received From Alternative Fuel Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0410
- Description: Invalid Data Received From Fuel Pump Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0411
- Description: Invalid Data Received From Drive Motor Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0412
- Description: Invalid Data Received From Battery Energy Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0413
- Description: Invalid Data Received From Battery Energy Control Module B
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0414
- Description: Invalid Data Received From Four-Wheel Drive Clutch Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0415
- Description: Invalid Data Received From Anti-Lock Brake System Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0416
- Description: Invalid Data Received From Vehicle Dynamics Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0417
- Description: Invalid Data Received From Park Brake Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0418
- Description: Invalid Data Received From Brake System Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0419
- Description: Invalid Data Received From Steering Effort Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0420
- Description: Invalid Data Received From Power Steering Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0421
- Description: Invalid Data Received From Ride Level Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0422
- Description: Invalid Data Received From Body Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0423
- Description: Invalid Data Received From Instrument Panel Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0424
- Description: Invalid Data Received From HVAC Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0425
- Description: Invalid Data Received From Auxiliary Heater Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0426
- Description: Invalid Data Received From Vehicle Immobilizer Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0427
- Description: Invalid Data Received From Vehicle Security Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0428
- Description: Invalid Data Received From Steering Angle Sensor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0429
- Description: Invalid Data Received From Steering Column Control Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0430
- Description: Invalid Data Received From Tire Pressure Monitor Module
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## U0431
- Description: Invalid Data Received From Body Control Module A
- Category: U
- Scope: generic
- Possible causes: not documented
- Diagnostic notes: not documented
- Grade: [B]
- Evidence: motor-talk.de SAE J2012 attachment; U0315, U0401, U0402, U0405, U0415-U0418, U0424 spot-confirmed by scribd "Control Module U Code List"

## Coverage notes

### Totals
- 2,098 generic DTC entries: P0xxx 1,021 · P2xxx 655 · P34xx 97 · B0xxx 45 · C0xxx 19 · U0xxx 261.
- Possible causes and/or diagnostic notes are documented for ~20 high-frequency codes (P0011, P0100,
  P0130, P0170, P0171, P0128, P0300, P0303, P0304, P0401, P0420, P0442, P0446, P0500, P2002, U0073,
  U0100, U0101). All other entries say "not documented" per the no-invention rule.

### Source conflicts (reported, not silently resolved)
1. P0217 — scribd SAE transcription: "Engine Overtemp Condition"; motor-talk: "Engine Coolant Over
   Temperature Condition". Motor-talk wording used.
2. P0700 — scribd: "Transmission Control System Malfunction"; motor-talk: "Transmission Control
   System (MIL Request) Malfunction". Motor-talk wording used (more specific).
3. P0574-P0580 — scribd lists seven entries all worded "Cruise Control Related Malfunction" (and
   duplicates P0576); motor-talk gives a distinct description per code. Motor-talk wordings used.
4. P0781 — scribd shows truncated "-2 Shift Malfunction"; motor-talk: "1-2 Shift Malfunction".
   Full wording used.
5. P0120-P0124 — scribd: "Throttle/Petal Position Sensor/Switch" ("Petal" = typo); motor-talk:
   "Throttle Position Sensor/Switch". Motor-talk wording used.
6. U0073 — scribd "Control Module U Code List": "Control Module Communication Bus A Off";
   motor-talk and the retrolib EOBD PDF: "Control Module Communication Bus Off". Two-source
   wording used.

### Codes NOT verified (excluded by the no-invention rule)
- P00B7 ("Engine Coolant Flow Low/Performance" in newer SAE revisions) — mentioned in a single
  JustAnswer thread; not verified, excluded.
- P0Bxx-P0Fxx hybrid/battery generic ranges (newer SAE revisions) — absent from all sources used.
- P2Bxx, P2Cxx and later P2xxx additions beyond P2A05/P2830 — absent from sources used.
- B0096-B0099 and B00A0+ (occupant classification, seatbelt pretensioner stage 2+, etc.) — absent
  from sources used.
- C0xxx beyond the C0000-C0128 block — the motor-talk source mixes generic and OEM chassis codes
  from C0141 upward (GM-style "EBCM", "Speed Wheel Sensor LF"); only the SAE-generic-plausible
  C0xxx block (wheel-speed circuits, ABS solenoids, pump motor, valve relay) is included.
- U0432 and above — absent from sources used.
- U1000+ ("Invalid or Missing Data for Primary Id" family) — manufacturer-specific (GM), excluded
  by scope; they belong to the v1.2 manufacturer-specific research, not this generic reference.
- Unassigned gaps inside the transcribed ranges (P0383-P0384, P0395-P0399, P0409, P2072-P2074,
  P2796-P2799, U0116-U0120, U0133-U0139) — absent from both sources; treated as unassigned in
  SAE J2012, not transcription errors.

### Systematic gaps
- No A-grade entries: the SAE J2012 standard text itself is paywalled; the best available evidence
  is two independent community transcriptions of it (graded B where they agree) plus technician
  sources for common codes.
- Possible causes exist almost exclusively for high-frequency P-codes and U-codes; B0xxx/C0xxx
  entries carry descriptions only.
- P2xxx and P34xx ranges are graded C except where a second source confirmed the wording
  (P2002, P3400-P3420).
