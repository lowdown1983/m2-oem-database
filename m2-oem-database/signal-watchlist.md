# M2 signal watchlist — high-value decode specs from the OEM database v1.1

**What this is:** one ready-to-use row per signal class per make, for live sniffing in M2RET mode
or for building watch/trigger lists in your firmware. Every row was re-verified 2026-10-06 against
the raw opendbc DBC text in `work/opendbc/opendbc/dbc/` — the IDs, bit positions, factors and units
below match the DBC files byte-for-byte.

**Evidence grade:** B/C — community opendbc captures, NOT verified against a real vehicle.
Treat as starting guesses: sniff the frame first, confirm the value moves with the car, then trust it.
Decode formula everywhere: `value = raw × factor + offset`.

**ID note:** GM Global-A lowspeed rows are 29-bit extended IDs (set extended frame bit).
Everything else is a standard 11-bit ID unless marked `ext`.

| Make | Signal | CAN ID | Frame | Msg name | Sig name | Bits | Byte order | Sign | Factor | Offset | Unit | Source DBC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GM | RPM | 0x802CA000 ext | 2150408192 | Engine_Information_1_LS | EngSpd | 23\|16 | motorola | u | 0.25 | 0 | rpm | gm_global_a_lowspeed_1818125 |
| GM | Vehicle speed | 0x10210000 ext | 270598144 | VehicleSpeed | VehicleSpeed1 | 7\|16 | motorola | u | 0.01 | 0 | mph | gm_global_a_lowspeed |
| GM | Steering angle | 0x10240000 ext | 270794752 | SteeringWheelAngle | SteeringWheelAngle | 39\|16 | motorola | s | 0.0625 | 0 | deg | gm_global_a_lowspeed |
| GM | Coolant temp¹ | 0x460 | 1120 | Coolant_Temp | Inlet_Coolant_Temp | 1\|10 | motorola | u | 0.125 | -40 | °C | gm_global_a_high_voltage_management |
| GM | Brake pressure | 0x170 | 368 | EBCMFrictionBrakeStatus | FrictionBrakePressure | 23\|16 | motorola | u | 1 | 0 | kPa (unverified) | gm_global_a_chassis |
| Ford | Wheel speed FL | 0x217 | 535 | WheelSpeed_CG1 | WhlFl_W_Meas | 7\|14 | motorola | u | 0.04 | 0 | rad/s² | ford_fusion_2018_pt |
| Ford | Coolant temp³ | — | — | (use OBD2 PID 0x05) | — | — | — | — | — | — | — | not in opendbc Ford set |
| Stellantis | RPM | 0xFC | 252 | ENGINE_1 | ENGINE_RPM | 7\|14 | motorola | u | 1 | 0 | rev/min | fca_giorgio |
| Stellantis | Accel pedal | 0xFC | 252 | ENGINE_1 | ACCEL_PEDAL | 20\|8 | motorola | u | 0.4 | 0 | % | fca_giorgio |
| Stellantis | Wheel speed FL | 0xEE | 238 | ABS_1 | WHEEL_SPEED_FL | 7\|13 | motorola | u | 0.017 | 0 | m/s | fca_giorgio |
| Stellantis | Steering angle | 0xDE | 222 | EPS_1 | STEERING_ANGLE | 5\|14 | motorola | u | 0.1 | -716.8 | deg | fca_giorgio |
| Stellantis | Brake pressure | 0x1E4 | 484 | BRAKE_1 | DRIVER_BRAKE_PRESSURE | 7\|12 | motorola | u | 1 | 0 | (raw) | chrysler_cusw |
| Toyota | RPM | 0x1C4 | 452 | POWERTRAIN | ENGINE_RPM | 7\|16 | motorola | u | 1 | 0 | rpm | toyota_prius_2010_pt |
| Toyota | Wheel speed FR | 0xAA | 170 | WHEELS_SPEEDS | FRONT_RIGHT_WHEEL_SPEED | 7\|16 | motorola | u | 0.01 | -67.67 | km/h | toyota_iQ_2009_can |
| Toyota | Steering angle | 0x25 | 37 | STEER_ANGLE_SENSOR | STEER_ANGLE | 3\|12 | motorola | s | 1.5 | 0 | deg | toyota_prius_2010_pt |
| Toyota | Gear | 0x127 | 295 | GEAR_PACKET | GEAR | 47\|4 | motorola | u | 1 | 0 | enum | toyota_prius_2010_pt |
| Toyota | Brake pressed | 0x226 | 550 | BRAKE_MODULE | BRAKE_PRESSED | 37\|1 | motorola | u | 1 | 0 | bool | toyota_prius_2010_pt |
| Honda | Vehicle speed | 0x300 | 768 | VEHICLE_STATE | VEHICLE_SPEED | 15\|8 | motorola | u | 1 | 0 | kph | acura_ilx_2016_nidec |
| VW | Throttle | 0x391 | 913 | OBD_01 | OBD_Abs_Throttle_Pos | 16\|8 | intel | u | 0.39216 | 0 | % | vw_mqb |
| VW | Wheel speed HL | 0xB2 | 178 | ESP_19 | ESP_HL_Radgeschw_02 | 0\|16 | intel | u | 0.0075 | 0 | km/h | vw_mqb |
| VW | Brake pressed | 0x139 | 313 | ESP_NEW_3 | BRAKE_PRESSED_1 | 16\|1 | intel | u | 1 | 0 | bool | vw_mqbevo |
| Hyundai | RPM⁴ | 0x280 | 640 | ECU_Data2 | RPM | 32\|8 | intel | u | 32 | 0 | rpm | hyundai_santafe_2007 |
| Hyundai | Wheel speed FR | 0x1F1 | 497 | ESP_WheelSpeed | FrontRightWheelSpeed | 16\|12 | intel | u | 0.125 | 0 | km/h | hyundai_santafe_2007 |
| Hyundai | Coolant temp | 0x329 | 809 | ECU_Data5 | ECT | 8\|8 | intel | s | 0.75 | -48 | °C | hyundai_santafe_2007 |
| Hyundai | Throttle | 0x329 | 809 | ECU_Data5 | TPS | 40\|8 | intel | u | 0.47266 | -15 | % | hyundai_santafe_2007 |
| Hyundai | Gear | 0x43F | 1087 | TCU_Data | CurrentGear | 0\|3 | intel | u | 1 | 0 | enum | hyundai_santafe_2007 |
| Nissan | RPM⁵ | 0x233 | 563 | ENGINE_7 | RPMhi + RPMlow | 56\|8 + 32\|8 | intel | u | 3.15 | 0 | r/min | nissan_xterra_2011 |
| Nissan | Vehicle speed | 0x280 | 640 | SPEED | SPEED | 32\|16 | intel | u | 0.01 | 0 | km/h | nissan_xterra_2011 |
| Nissan | Steering angle | 0x2 | 2 | STEERING | STEERING_ANGLE | 0\|16 | intel | s | 0.1 | 0 | deg | nissan_xterra_2011 |
| Nissan | Throttle | 0x23D | 573 | ENGINE_3 | Throttle_position_capped | 16\|8 | intel | u | 0.392 | 0 | % | nissan_xterra_2011 |

**Footnotes**
1. GM coolant temp only exists in the high-voltage-management DBC — it is a hybrid/BEV bus, may not
   be present on a conventional car. OBD2 PID 0x05 via your OBD2 poller is the safer path on GM too.
2. Ford wheel speed is in rad/s. Convert with the tire radius: km/h ≈ raw × 0.04 × r(m) × 3.6.
   (r ≈ 0.33 m for a typical sedan → km/h ≈ raw × 0.0475.)
3. Ford has no coolant-temp signal in the opendbc Ford set. Your OBD2 poller (PID 0x05) already covers it.
4. Hyundai RPM factor 32 is what the DBC says (raw 0–255 → 0–8160 rpm). Unusual but self-consistent;
   confirm on the vehicle.
5. Nissan RPM is split across two 8-bit signals. Likely combine as `(RPMhi << 8 | RPMlow) × 3.15`
   treated as one 16-bit value — confirm against a tach reading before trusting.

**How to use in M2RET mode:** the frames above are what GVRET shows by ID. Set your CAN filter or
watch list to the IDs for the make you're plugged into, pull the bits per the table, apply the
formula. The full machine copy of this table (same rows, JSON) is `signal-watchlist.json` next to this file.
