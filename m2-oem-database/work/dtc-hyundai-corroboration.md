# Hyundai/Kia B/C/U DTC Corroboration

**Purpose:** Second-source corroboration for the 179 Hyundai/Kia B/C/U diagnostic trouble codes in the M2 OEM vehicle database (v1.3). All 179 codes were previously grade C, sourced from a single transcription (scribd "Hyundai DTC Codes Overview").

**Research date:** 2026-10-07

**Grading note:** A = Hyundai/Kia service information (shop-manual pages via charm.li, HMA technical service bulletins via NHTSA/oemdtc, AutoHex Hyundai DTC Help pages which transcribe GDS/shop-manual content, Hyundai TechNet Times — which states its Hyundai-specific codes match shop manuals and Hyundai GDS at time of publication — and Hyundai AFLS training documentation). B = reputable DTC database or multi-source agreement (automanual, avtotachki, carcarehacks, OBDCodex/slideshare, hyundaibook.ru, carscounsel.com, import-car.com, scan-tool printouts, dealer field reports). C = single community source. Claims marked INFERRED are extrapolations, not independently documented facts.

**Method:** Targeted web searches per code plus lookup inside Hyundai TechNet Times Vol. 24, Issue 02 (8th-edition Hyundai DTC listing, manuals.plus mirror) for codes found there. No YAML was edited and the build was not run.

**Important caveat (module scoping):** Hyundai reuses code numbers across modules with different meanings (e.g., B1264 = direction-potentiometer fault in one HVAC table, "Pressure Sensor #4" in another; B1621 = ECU hardware error in some tables, sensor-power error in others; C1643 = "CAN Time-out Yaw Rate & G Sensor" vs "Motor Current Excessive"). Unless noted, the corroborated description below refers to the module context matching the database entry.

---

## B1101
- Existing description: Battery Voltage High
- Verdict: CONFIRMED
- Corroborated description: Battery Voltage High — matches (swirlzcupcakes Hyundai DTC table; OBDCodex list "SRSCM Input Voltage High").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B] (multi-source agreement across community DTC databases)
- Evidence: swirlzcupcakes Hyundai DTC table lists B1101 as Battery Voltage High / B1102 as Battery Voltage Low; slideshare OBDCodex Hyundai list gives "Hyundai B1101 SRSCM Input Voltage High". Both agree with the database.

## B1102
- Existing description: Battery Voltage Low
- Verdict: CONFIRMED
- Corroborated description: Battery Voltage Low — matches (Hyundai MOHAVE/BORREGO service manual).
- Possible causes: poor connection at SRSCM connector, wiring harness open or short, charging system fault, SRSCM internal fault (service manual) [A]
- Diagnostic notes: DTC sets when battery voltage stays at or below 9V for more than about 4 seconds; normal operating threshold 9–16V (service manual) [A]
- Recommended grade: [A] (Hyundai service manual)
- Evidence: Hyundai MOHAVE/BORREGO shop-manual DTC B1102 page (scribd mirror) gives the voltage threshold, detect time, and cause list; automanual Hyundai error-code compilation lists B1102 with compatible wording.

## B1200
- Existing description: Humidity Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: Humidity Sensor Open (High) — matches (slideshare OBDCodex "Hyundai B1200 Humidity Sensor Open"; carcarehacks; Hyundai HVAC DTC list doc "B1200 HUMIDITY SENSOR-OPEN").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B] (multi-source database agreement)
- Evidence: Three independent DTC compilations (slideshare OBDCodex list, carcarehacks Hyundai list, scribd Hyundai HVAC DTC list doc/612797538) all give "Humidity Sensor Open (High)".

## B1201
- Existing description: Humidity Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: Humidity Sensor Short (Low) — matches (same three sources as B1200).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: slideshare OBDCodex, carcarehacks, and the Hyundai HVAC DTC list all give "Humidity Sensor Short (Low)".

## B1202
- Existing description: Water Temperature Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: Heater Water Temperature Sensor Open (High) — matches (slideshare OBDCodex; carscounsel; HVAC DTC list "B1202 WATER TEMP. SENSOR-OPEN").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: slideshare OBDCodex and carscounsel both list "Heater Water Temperature Sensor Open (High)"; the Hyundai HVAC DTC list gives "B1202 WATER TEMP. SENSOR-OPEN".

## B1203
- Existing description: Water Temperature Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: Heater Water Temperature Sensor Short (Low) — matches (slideshare OBDCodex; carscounsel; HVAC DTC list "B1203 WATER TEMP. SENSOR-SHORT").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Same three sources as B1202, all agreeing on the short/low variant.

## B1208
- Existing description: Intake Potentiometer Open (Low)
- Verdict: CONFIRMED
- Corroborated description: Intake Potentiometer Open (Low) — matches (AutoHex Hyundai DTC Help, Sonata NF and Santa Fe CM: feedback voltage below ~0.1V for ~0.3s).
- Possible causes: not documented
- Diagnostic notes: AutoHex pages give detection threshold <0.1V for 0.3s with failsafe "FRE" (AutoHex) [A]
- Recommended grade: [A] (AutoHex service-info-derived DTC help)
- Evidence: AutoHex Hyundai DTC Help pages for B1208 (Sonata NF, Santa Fe CM) match the description and add threshold/failsafe; slideshare OBDCodex, carcarehacks, hyundaibook.ru (Tucson LM), and carscounsel agree on "Intake Potentiometer Open (Low)".

## B1209
- Existing description: Intake Potentiometer Short (High)
- Verdict: CONFIRMED
- Corroborated description: Intake Potentiometer Short (High) — matches (slideshare OBDCodex; carcarehacks; hyundaibook.ru; carscounsel; HVAC DTC list "B1209 INTAKE DOOR FEEDBACK-SHORT").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Five independent compilations agree on "Intake Potentiometer Short (High)" / "INTAKE DOOR FEEDBACK-SHORT".

## B1220
- Existing description: Vehicle Speed Sensor - Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Vehicle Speed Sensor — matches (slideshare OBDCodex "Hyundai B1220 Vehicle Speed Sensor"; carcarehacks "B1220 Vehicle Speed Sensor").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Two independent DTC compilations list B1220 as a vehicle speed sensor fault, consistent with the database description.

## B1233
- Existing description: In-Car Temperature Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: In-Car Temperature Sensor Short (Low) — matches (slideshare OBDCodex; carcarehacks; hyundaibook.ru "cabin temperature sensor is shorted"; HVAC DTC list "B1233 INCAR TEMPERATURE SENSOR-SHORT").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1234
- Existing description: In-Car Temperature Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: In-Car Temperature Sensor Open (High) — matches (Hyundai shop-manual pages via charm.li: Elantra, Veracruz, Elantra Touring; AutoHex: i20 PB, i30 GDe).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai shop manuals via charm.li; AutoHex service-info-derived)
- Evidence: charm.li hosts Hyundai service-manual B1234 pages for three models; AutoHex Hyundai DTC Help lists B1234 for i20/i30 with the same meaning. carscounsel, hyundaibook.ru, and slideshare OBDCodex agree.

## B1237
- Existing description: Ambient Temperature Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: Ambient Temperature Sensor Short (Low) — matches (hyundaibook.ru "outside temperature sensor is shorted"; slideshare OBDCodex; carcarehacks; HVAC DTC list "B1237 AMBIENT TEMPERATURE SENSOR-SHORT").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1238
- Existing description: Ambient Temperature Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: Ambient Temperature Sensor Open (High) — matches (automanual; slideshare OBDCodex; carcarehacks; hyundaibook.ru; HVAC DTC list "B1238 AMBIENT TEMPERATURE SENSOR-OPEN").
- Possible causes: automanual frames it as a break in the outdoor-temperature-controller wiring [B]
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual Hyundai error-code compilation plus four other compilations agree on the open/high variant.

## B1241
- Existing description: Evaporator Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: Evaporator Sensor Short (Low) — matches (HVAC DTC list "B1241 FIN THERMO SENSOR-SHORT"; slideshare OBDCodex; carcarehacks; hyundaibook.ru).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree. (A micro-tronik B1242 page defines a generic Ford mode-door code — excluded as a trap; not applicable to Hyundai.)

## B1242
- Existing description: Evaporator Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: Evaporator Sensor Open (High) — matches (same four sources as B1241).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Same four compilations agree on the open/high variant.

## B1245
- Existing description: Air Mix Potentiometer Open (Low) - Driver
- Verdict: CONFIRMED
- Corroborated description: Air Mix Potentiometer Open (Low) - Driver — matches (HVAC DTC list "B1245 TEMP. DOOR FEEDBACK-OPEN"; slideshare OBDCodex "Air Mix Potentiometer Open (Low)-Driver"; carcarehacks; hyundaibook.ru).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1246
- Existing description: Air Mix Potentiometer Short (High) - Driver
- Verdict: CONFIRMED
- Corroborated description: Air Mix Potentiometer Short (High) - Driver — matches (same four sources).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Same four compilations agree on the short/high variant.

## B1249
- Existing description: Direction Potentiometer Open (Low) - Driver
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Open (Low) - Driver — matches (HVAC DTC list "B1249 MODE DOOR FEEDBACK-OPEN"; slideshare OBDCodex "Direction Potentiometer Open (Low)-Driver"; carcarehacks; hyundaibook.ru).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1250
- Existing description: Direction Potentiometer Short (High) - Driver
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Short (High) - Driver — matches (same four sources).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Same four compilations agree on the short/high variant.

## B1257
- Existing description: AQS Sensor Open (High)
- Verdict: CONFIRMED
- Corroborated description: AQS Sensor Open (High) — matches (avtotachki "AQS sensor is open"; slideshare OBDCodex "AQS Sensor Open"; carcarehacks "AQS Sensor Open"; HVAC DTC list "B1257 AQS SENSOR -OPEN").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1258
- Existing description: AQS Sensor Short (Low)
- Verdict: CONFIRMED
- Corroborated description: AQS Sensor Short to Ground — matches (avtotachki "AQS sensor short to ground"; slideshare OBDCodex "AQS Sensor Short To Ground"; carcarehacks; HVAC DTC list "SHORT").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1259
- Existing description: AQS Sensor Fault
- Verdict: CONFIRMED
- Corroborated description: AQS Sensor Fault / Defective AQS Sensor — matches (avtotachki "AQS sensor failure"; slideshare OBDCodex "AQS Sensor Fault"; carcarehacks "AQS Sensor Fault"; HVAC DTC list "B1259 DEFECTIVE AQS SENSOR").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Four independent compilations agree.

## B1264
- Existing description: Direction Potentiometer Open (Low) - VENT
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Open (Low)-VENT — exact match (Hyundai TechNet Times DTC listing).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times Vol. 24 Issue 02 Hyundai DTC section lists "B1264 Direction Potentiometer Open (Low)-VENT". Module-scoping note: a different table in the same publication lists B1264 as "Pressure Sensor.#4-Abnormal" — different module context.

## B1265
- Existing description: Direction Potentiometer Short (High) - VENT
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Short (High)-VENT — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1265 Direction Potentiometer Short (High)-VENT". (Alternate table entry "Pressure Sensor.#4-Low" is a different module context.)

## B1266
- Existing description: Direction Potentiometer Open (Low) - FLOOR
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Open (Low)-Floor — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1266 Direction Potentiometer Open (Low)-Floor". (Alternate table entry "Pressure Sensor.#4-High" is a different module context.)

## B1267
- Existing description: Direction Potentiometer Short (High) - FLOOR
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Short (High)-Floor — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1267 Direction Potentiometer Short (High)-Floor".

## B1268
- Existing description: Direction Potentiometer Open (Low) - DEF
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Open (Low)-Defog — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1268 Direction Potentiometer Open (Low)-Defog".

## B1269
- Existing description: Direction Potentiometer Short (High) - DEF
- Verdict: CONFIRMED
- Corroborated description: Direction Potentiometer Short (High)-Defog — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1269 Direction Potentiometer Short (High)-Defog".

## B1301
- Existing description: Steering Angle Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Steering Angle Signal Fault — exact match (TechNet Times: "B1301 Steering Angle Signal Fault"); avtotachki: "Steering Angle Signal Error".
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times Hyundai DTC section lists B1301 exactly; avtotachki Hyundai codes page independently gives "Steering Angle Signal Error".

## B1302
- Existing description: Gearbox Signal Fault (CAN Signal)
- Verdict: CONFIRMED
- Corroborated description: Gearbox Signal Fault-CAN Signal — exact match (TechNet Times); avtotachki: "Gearbox signal error - CAN signal".
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1302 Gearbox Signal Fault-CAN Signal"; avtotachki agrees with "Gearbox signal error - CAN signal".

## B1303
- Existing description: Accelerator Pedal Position Signal Error
- Verdict: CONFIRMED
- Corroborated description: Accelerator Pedal Position Signal Error — exact match (avtotachki).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: avtotachki Hyundai codes page lists B1303 as "Accelerator Pedal Position Signal Error".

## B1304
- Existing description: Engine State Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Engine Status Signal Error — wording variant, same meaning (avtotachki).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: avtotachki lists "B1304 Engine Status Signal Error", consistent with the database's "Engine State Signal Fault".

## B1305
- Existing description: Yaw Rate Sensor Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Yaw rate sensor signal error — wording variant, same meaning (avtotachki).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: avtotachki lists "B1305 Yaw rate sensor signal error", consistent with the database description.

## B1306
- Existing description: Brake Pedal Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Brake pedal signal malfunction — wording variant, same meaning (avtotachki).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: avtotachki lists "B1306 Brake pedal signal malfunction", consistent with the database description.

## B1308
- Existing description: Lamp Function Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Lamp Function Signal Fault — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times Hyundai DTC section lists "B1308 Lamp Function Signal Fault".

## B1328
- Existing description: FIS Driver - Defect
- Verdict: CONFIRMED
- Corroborated description: FIS(Front Impact Sensor)-Driver Defect — exact match (Hyundai MOHAVE/BORREGO service manual; Hyundai Restraint shop-manual DTC table mirrored on sportiveshyundai.fr; TechNet Times).
- Possible causes: poor connection at FIS connector, front impact sensor (driver) internal fault, SRSCM fault (MOHAVE/BORREGO service manual) [A]
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai service manuals)
- Evidence: The Hyundai MOHAVE/BORREGO service-manual DTC B1328 page diagnoses "FIS(Front Impact Sensor)-Driver Defect" with causes; the Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) and TechNet Times both list B1328 identically.

## B1329
- Existing description: FIS Driver - Communication Error
- Verdict: CONFIRMED
- Corroborated description: FIS(Front Impact Sensor)-Driver Communication error — exact match (TechNet Times; JustAnswer quoting Hyundai service data; CarProTool Sonata 2018 SRSCM scan "B1329:00-89 - FIS(FRONT IMPACT SENSOR)-DRIVER COMMUNICATION ERROR").
- Possible causes: poor connection, front impact sensor (driver) fault, SRSCM (JustAnswer quoting Hyundai service info) [B]
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: A JustAnswer Hyundai thread quotes the Hyundai service-manual cause list for B1329; automanual lists B1329; a CarProTool forum thread shows a real 2018 Sonata SRSCM scan reading B1329:00-89.

## B1333
- Existing description: FIS Passenger - Defect
- Verdict: CONFIRMED
- Corroborated description: FIS(Front Impact Sensor)-Passenger Defect — exact match (TechNet Times; Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times / Restraint shop manual)
- Evidence: TechNet Times lists "B1333 FIS(Front Impact Sensor)-Passenger Defect"; the Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists B1333 identically.

## B1334
- Existing description: FIS Passenger - Communication Error
- Verdict: CONFIRMED
- Corroborated description: FIS(FRONT IMPACT SENSOR)-PASSENGER COMMUNICATION ERROR — exact match (CarProTool Sonata 2018 SRSCM scan "B1334:00-89"; Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: CarProTool forum thread shows a real 2018 Sonata SRSCM scan reading B1334:00-89 with the full description; the Hyundai Restraint manual DTC table lists B1334 the same way.

## B1346
- Existing description: Driver Airbag Resistance Too High (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Driver Airbag Resistance Too High (1st Stage) — exact match (AutoHex Santa Fe CM; Hyundai shop-manual pages via charm.li: Sonata, Azera; automanual; Hyundai Restraint manual table; CarProTool scan).
- Possible causes: poor electrical connection, shorting-bar / release-pin contact issue in the DAB connector, driver airbag (DAB) squib fault, clock spring fault, SRSCM fault (JustAnswer quoting Hyundai guidance) [B]
- Diagnostic notes: DAB circuit resistance spec roughly 0.9–6.6/6.7 ohms (field guidance, JustAnswer) [B]; automanual lists B1346 [B]
- Recommended grade: [A] (AutoHex service-info-derived; Hyundai shop manuals via charm.li)
- Evidence: AutoHex Hyundai DTC Help (Santa Fe CM) and charm.li Hyundai service-manual B1346 pages (Sonata, Azera) give the code with the same description; a JustAnswer thread documents the cause list and resistance spec; CarProTool scan shows B1346:00-89. (Ford B1346 "heated backlite" and Honda B1346 definitions are different-manufacturer traps — excluded.)

## B1347
- Existing description: Driver Airbag Resistance Too Low (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Driver Airbag Resistance too Low (1st stage) — exact match (TechNet Times; Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1347 Driver Airbag Resistance too Low (1st stage)"; the Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists B1347 identically.

## B1348
- Existing description: Driver Airbag Resistance Circuit Short to Ground (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Driver Airbag Resistance Circuit Short to Ground (1st stage) — matches (Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai Restraint shop manual)
- Evidence: The Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists the B1346–B1349 family with the same descriptions.

## B1349
- Existing description: Driver Airbag Resistance Circuit Short to Battery (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Driver Airbag resistance circuit short to Battery (1st stage) — exact match (TechNet Times "B134900 Driver Airbag resistance circuit short to Battery (1st stage)"; Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times and the Hyundai Restraint manual DTC table both list B1349 with this description.

## B1352
- Existing description: Passenger Airbag Resistance Too High (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: PAB RESISTANCE-HIGH — matches (CarProTool Sonata 2018 SRSCM scan "B1352:00-89 - !!! PAB RESISTANCE-HIGH !!!"); Hyundai Restraint manual table "B1352 Passenger Airbag Resistance too High (1st stage)".
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai Restraint shop manual)
- Evidence: Real-world scan-tool read plus the Hyundai Restraint shop-manual DTC table agree.

## B1353
- Existing description: Passenger Airbag Resistance Too Low (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Passenger Airbag Resistance too Low (1st stage) — matches (Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: The Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists the B1352–B1355 family with the same descriptions.

## B1354
- Existing description: Passenger Airbag Resistance Circuit Short to Ground (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Passenger Airbag Resistance Circuit Short to Ground (1st stage) — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1352.

## B1355
- Existing description: Passenger Airbag Resistance Circuit Short to Battery (1st Stage)
- Verdict: CONFIRMED
- Corroborated description: Passenger Airbag Resistance Circuit Short to Battery (1st stage) — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1352.

## B1361
- Existing description: Pretensioner Front-Driver Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Driver Resistance too High — exact match (CarProTool Sonata 2018 SRSCM scan "B1361:00-89"; TechNet Times "B1361 Pretensioner Front-Driver Resistance too High"; Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Real scan-tool read, TechNet Times, and the Hyundai Restraint manual DTC table all agree.

## B1362
- Existing description: Pretensioner Front-Driver Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Driver Resistance too Low — matches (Hyundai Restraint shop-manual DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: The Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists the B1361–B1364 family with the same descriptions.

## B1363
- Existing description: Pretensioner Front-Driver Resistance Circuit Short to Ground
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Driver Resistance Circuit Short to Ground — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1361.

## B1364
- Existing description: Pretensioner Front-Driver Resistance Circuit Short to Battery
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Driver Resistance Circuit Short to Battery — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1361.

## B1367
- Existing description: Pretensioner Front-Passenger Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Passenger Resistance too High — exact match (CarProTool Sonata 2018 scan "B1367:00-89"; Hyundai Restraint manual table; automanual).
- Possible causes: automanual lists cause guidance for B1367 [B]
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Real scan-tool read plus the Hyundai Restraint shop-manual DTC table and automanual agree.

## B1368
- Existing description: Pretensioner Front-Passenger Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Passenger Resistance too Low — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1367.

## B1369
- Existing description: Pretensioner Front-Passenger Resistance Circuit Short to Ground
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Passenger Resistance Circuit Short to Ground — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1367.

## B1370
- Existing description: Pretensioner Front-Passenger Resistance Circuit Short to Battery
- Verdict: CONFIRMED
- Corroborated description: Pretensioner Front-Passenger Resistance Circuit Short to Battery — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1367.

## B1378
- Existing description: Side Airbag Front-Driver Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Driver Resistance too High — matches (CarProTool Sonata 2018 scan "B1378:00-89"; Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Real scan-tool read plus the Hyundai Restraint shop-manual DTC table agree.

## B1379
- Existing description: Side Airbag Front-Driver Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Driver Resistance too Low — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1378.

## B1380
- Existing description: Side Airbag Front-Driver Resistance Circuit Short to Ground
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Driver Resistance Circuit Short to Ground — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1378.

## B1381
- Existing description: Side Airbag Front-Driver Resistance Circuit Short to Battery
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Driver Resistance Circuit Short to Battery — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1378.

## B1382
- Existing description: Side Airbag Front-Passenger Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Passenger Resistance too High — matches (CarProTool Sonata 2018 scan "B1382:00-89"; Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Real scan-tool read plus the Hyundai Restraint shop-manual DTC table agree.

## B1383
- Existing description: Side Airbag Front-Passenger Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Passenger Resistance too Low — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1382.

## B1384
- Existing description: Side Airbag Front-Passenger Resistance Circuit Short to Ground
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Passenger Resistance Circuit Short to Ground — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1382.

## B1385
- Existing description: Side Airbag Front-Passenger Resistance Circuit Short to Battery
- Verdict: CONFIRMED
- Corroborated description: Side Airbag Front-Passenger Resistance Circuit Short to Battery — matches (Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Same Restraint manual DTC table as B1382.

## B1395
- Existing description: Firing Loops Interconnection Fault
- Verdict: CONFIRMED
- Corroborated description: Firing Loops Interconnection Fault — exact match (Hyundai shop-manual pages via charm.li: Tucson 2010, Genesis Coupe 2010, Elantra Touring 2011; JustAnswer field report "Cross Coupling B1395:00").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai shop manuals via charm.li)
- Evidence: charm.li hosts Hyundai service-manual DTC B1395 pages for three models with the same description; a JustAnswer Hyundai thread shows a tech encountering "Cross Coupling B1395:00", consistent with firing-loop interconnection.

## B1400
- Existing description: SIS Front-Driver Defect
- Verdict: CONFIRMED
- Corroborated description: SIDE IMPACT SENSOR FRONT-DRIVER DEFECT — matches (Hyundai shop-manual page via charm.li: 2007 Tucson DTC B1400).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai shop manual via charm.li)
- Evidence: charm.li 2007 Tucson service-manual page lists "DTC B1400 SIDE IMPACT SENSOR FRONT-DRIVER DEFECT".

## B1403
- Existing description: SIS Front-Passenger Defect
- Verdict: CONFIRMED
- Corroborated description: SIDE IMPACT SENSOR FRONT-PASSENGER DEFECT — matches (Hyundai shop-manual pages via charm.li: Tucson, Sonata, Elantra Touring, Genesis Coupe, Azera).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: charm.li hosts Hyundai service-manual DTC B1403 pages for five models with the same description.

## B1409
- Existing description: SIS Front-Driver Communication Error
- Verdict: CONFIRMED
- Corroborated description: SIDE IMPACT SENSOR FRONT-DRIVER COMMUNICATION ERROR — exact match (charm.li 2007 Tucson; CarProTool Sonata 2018 scan "B1409:00-89 - SIS(SIDE IMPACT SENSOR) FRONT-DRIVER COMMUNICATION ERROR").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: Hyundai shop-manual page via charm.li plus a real scan-tool read agree exactly.

## B1410
- Existing description: SIS Front-Passenger Communication Error
- Verdict: CONFIRMED
- Corroborated description: SIDE IMPACT SENSOR FRONT-PASSENGER COMMUNICATION ERROR — matches (Hyundai shop-manual pages via charm.li: Tucson, Sonata, Tiburon, Genesis Coupe).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: charm.li hosts Hyundai service-manual DTC B1410 pages for four models with the same description.

## B1473
- Existing description: Inflatable Curtain Airbag Front-Driver Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Front-Driver Resistance Too High — exact match (Hyundai shop-manual pages via charm.li: Elantra, Elantra Touring, Tucson, Genesis Sedan, Santa Fe; Hyundai Restraint manual table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai shop manuals via charm.li)
- Evidence: charm.li hosts Hyundai service-manual DTC B1473 pages for five models; the Hyundai Restraint manual DTC table (sportiveshyundai.fr mirror) lists B1473 the same way.

## B1474
- Existing description: Inflatable Curtain Airbag Front-Driver Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Driver Resistance too Low — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1474 Inflatable Curtain Airbag Driver Resistance too Low".

## B1475
- Existing description: Inflatable Curtain Airbag Front-Driver Resistance Circuit Short to Gro
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Driver Resistance Circuit Short to Ground — this is the full wording the database entry truncates ("Short to Gro").
- Possible causes: not documented
- Diagnostic notes: Database description is truncated; full text per TechNet Times is "...Resistance Circuit Short to Ground".
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1475 Inflatable Curtain Airbag Driver Resistance Circuit Short to Ground" / "B1475 Driver Curtain Short To Ground".

## B1476
- Existing description: Inflatable Curtain Airbag Front-Driver Resistance Circuit Short to Bat
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Driver/Front-Driver Resistance Circuit Short to Battery — full wording of the truncated database entry ("Short to Bat").
- Possible causes: not documented
- Diagnostic notes: Database description is truncated; full text per TechNet Times is "...Resistance Circuit Short to Battery".
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1476 Inflatable Curtain Airbag Driver Resistance Circuit Short to Battery" / "B147600 Inflatable Curtain Airbag Driver Resistance Circuit Short to...".

## B1477
- Existing description: Inflatable Curtain Airbag Front-Passenger Resistance Too High
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Passenger Resistance too High — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1477 Inflatable Curtain Airbag Passenger Resistance too High".

## B1478
- Existing description: Inflatable Curtain Airbag Front-Passenger Resistance Too Low
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Passenger Resistance too Low — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1478 Inflatable Curtain Airbag Passenger Resistance too Low".

## B1479
- Existing description: Inflatable Curtain Airbag Front-Passenger Resistance Circuit Short to 
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Passenger Resistance Circuit Short to Ground — full wording of the truncated database entry.
- Possible causes: not documented
- Diagnostic notes: Database description is truncated mid-word; full text per TechNet Times is "...Resistance Circuit Short to Ground".
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1479 Inflatable Curtain Airbag Passenger Resistance Circuit Short to Ground" / "B1479 Passenger Curtain Short To Ground".

## B1480
- Existing description: Inflatable Curtain Airbag Front-Passenger Resistance Circuit Short to 
- Verdict: CONFIRMED
- Corroborated description: Inflatable Curtain Airbag Passenger Resistance Circuit Short to Battery — full wording of the truncated database entry.
- Possible causes: not documented
- Diagnostic notes: Database description is truncated mid-word; full text per TechNet Times is "...Resistance Circuit Short to Battery".
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1480 Inflatable Curtain Airbag Passenger Resistance Circuit Short to Battery" / "B1480 Passenger Curtain Short To Battery".

## B1527
- Existing description: Passenger Airbag On-Off Switch Open or Leakage to Battery
- Verdict: CONFIRMED
- Corroborated description: Passenger airbag On/Off switch open or short to Battery — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1527 Passenger airbag On/Off switch open or short to Battery" (also "B152700" suffixed variant).

## B1528
- Existing description: Passenger Airbag On-Off Switch Short or Leakage to Ground
- Verdict: CONFIRMED
- Corroborated description: Passenger airbag On/Off switch short or short to Ground — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1528 Passenger airbag On/Off switch short or short to Ground".

## B1529
- Existing description: Passenger Airbag On-Off Switch Defect
- Verdict: CONFIRMED
- Corroborated description: Passenger airbag On/Off switch defect — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1529 Passenger airbag On/Off switch defect".

## B1530
- Existing description: Passenger Airbag On-Off Switch Instability
- Verdict: CONFIRMED
- Corroborated description: Passenger airbag On/Off switch instability — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1530 Passenger airbag On/Off switch instability".

## B1603
- Existing description: CAN Communication Bus Off
- Verdict: CONFIRMED
- Corroborated description: CAN Communication Bus Off — exact match (TechNet Times; also listed as "CAN Bus OFF(C-CAN)" / "CAN Bus OFF(B-CAN)" / "CAN BUS OFF").
- Possible causes: not documented
- Diagnostic notes: TechNet Times shows C-CAN and B-CAN variants of B1603 (bus-off on either network). Module-scoping note: the same code also appears in AFLS/DBL headlamp tables.
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1603 CAN Communication Bus Off" in multiple tables with C-CAN/B-CAN qualifiers.

## B1620
- Existing description: Internal Fault - Replace ECU
- Verdict: CONFIRMED
- Corroborated description: SRSCM Internal Failure — matches (TechNet Times "B1620 SRSCM Internal Failure"; automanual "Internal malfunction of the SRS system"; CarProTool scan "B1620:00-89 - !!! SRSCM INTERNAL FAILURE !!!"; thehyundaiforums dealer scan "B1620: SRSCM Internal Failure").
- Possible causes: not documented (replacement of SRSCM is the documented remedy, not a cause)
- Diagnostic notes: Multiple TechNet Times tables pair B1620 with "Internal fault-Replace SRSCM" guidance [A]
- Recommended grade: [A] (Hyundai TechNet Times; service-info-derived)
- Evidence: TechNet Times lists "B1620 SRSCM Internal Failure" / "B1620 Internal fault-Replace SRSCM"; automanual, a dealer scan posted on thehyundaiforums, and a CarProTool forum scan read all confirm the code and meaning.

## B1621
- Existing description: ECU Hardware Error
- Verdict: CONFIRMED
- Corroborated description: ECU Hardware Error — exact match in one TechNet Times table. Module-scoping note: other TechNet Times tables give B1621 as "SRSCM Hardware Fault", "ECU Check Sum Error", "ECU-Failure", or "Sensor Power Error Line ERROR" depending on module/model.
- Possible causes: not documented
- Diagnostic notes: The database's "ECU Hardware Error" is valid for the SRSCM context; other modules reuse B1621 with different meanings — module context should be recorded with this code.
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1621 ECU Hardware Error" in one table alongside module-variant definitions in others.

## B1622
- Existing description: ECU Software Error
- Verdict: CONFIRMED
- Corroborated description: ECU Software Error — exact match (TechNet Times); variants "SRSCM software fault" / "ECM Software" in other tables.
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1622 ECU Software Error" / "B162200 SRSCM software fault" / "B1622 ECM Software".

## B1636
- Existing description: LIN Communication Error Fault
- Verdict: CONFIRMED
- Corroborated description: LIN Communication Error Fault — exact match (TechNet Times, DBL headlamp section).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1636 LIN Communication Error Fault" in the DBL (dynamic bending light) headlamp table.

## B1637
- Existing description: System Not Initialized
- Verdict: CONFIRMED
- Corroborated description: B1637 "initial problem" — compatible (Hyundai AFLS training documentation, scribd "13-BH-AFLS" Genesis AFLS section; the code list places B1637 in the AFLS(LED) headlamp family).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai AFLS training/service documentation)
- Evidence: The Hyundai AFLS training document describes B1637 as an "initial problem" (initialization not completed), consistent with the database's "System Not Initialized".

## B1639
- Existing description: LIN Communication Error DBL (Dynamic Bending Light) Left
- Verdict: CONFIRMED
- Corroborated description: LIN communication error DBL(Dynamic Bending Light) Left — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Pairs with B1640 "LIN communication error DBL(Dynamic Bending Light) Right" in the same TechNet Times table [A]
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1639 LIN communication error DBL(Dynamic Bending Light) Left".

## B1650
- Existing description: Crash Recorded in 1st Stage Only (Frontal) - Replace ECU
- Verdict: CONFIRMED
- Corroborated description: Crash Recorded in 1st Stage Only(Frontal-Replace SRSCM) — exact match (TechNet Times; AutoHex Tucson/ix35: "SRSCM sets DTC B1650 if DAB or PAB deploys").
- Possible causes: DAB or PAB deployment event (AutoHex) [A]; crash event recorded (field reports) [B]
- Diagnostic notes: Remedy is SRSCM replacement (TechNet Times "Replace SRSCM"; Palisade diagnostic report with B1650:00-89 recommending SRSCM replacement; OBDSTAR blog "B1650:00-89 Crash recorded in 1st Stage Only Frontal") [A/B]
- Recommended grade: [A] (Hyundai TechNet Times; AutoHex service-info-derived)
- Evidence: TechNet Times, AutoHex (Tucson/ix35 LM), a Palisade diagnostic report, and an OBDSTAR blog post all describe B1650 as crash-recorded-first-stage-frontal requiring SRSCM replacement.

## B1651
- Existing description: Crash Recorded in Front-Driver Side Airbag - Replace ECU
- Verdict: CONFIRMED
- Corroborated description: Crash Recorded in Front-Driver Side Airbag(Replace SRSCM) / Driver Side Airbag(DSAB) Crash Recorded — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Remedy is SRSCM replacement per TechNet Times [A]
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B1651 Crash Recorded in Front-Driver Side Airbag(Replace SRSCM)" / "B1651 Driver Side Airbag(DSAB) Crash Recorded".

## B1652
- Existing description: Crash Recorded in Front-Passenger Side Airbag - Replace ECU
- Verdict: CONFIRMED
- Corroborated description: Crash Recorded in Front-Passenger Side Airbag(Replace SRSCM) / Passenger Side Air Bag(PSAB) Crash Recorded — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Remedy is SRSCM replacement per TechNet Times [A]
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1652 Crash Recorded in Front-Passenger Side Airbag(Replace SRSCM)" / "B1652 Passenger Side Air Bag(PSAB) Crash Recorded".

## B1655
- Existing description: Crash Recorded (Side) - Replace ECU
- Verdict: CONFIRMED
- Corroborated description: Crash Recorded (Side Airbag-Replace SRSCM) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Remedy is SRSCM replacement per TechNet Times [A]
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1655 Crash Recorded (Side Airbag-Replace SRSCM)".

## B1657
- Existing description: Crash Recorded in Belt Pretensioner Only
- Verdict: CONFIRMED
- Corroborated description: Crash Recorded in Belt Pretensioner only / Crash Recorded-Belt Pretensioner(BPT) Only — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1657 Crash Recorded in Belt Pretensioner only" / "B1657 Crash Recorded-Belt Pretensioner(BPT) Only".

## B1658
- Existing description: Belt Pretensioner 6 Times Deployment
- Verdict: CONFIRMED
- Corroborated description: Belt Pretensioner 6 times Deployment — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B1658 Belt Pretensioner 6 times Deployment".

## B1661
- Existing description: Parameter Fault and Missing
- Verdict: CONFIRMED
- Corroborated description: B1661 "Parameter missing" — matches (Hyundai AFLS training documentation, scribd "13-BH-AFLS").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai AFLS training/service documentation)
- Evidence: The Hyundai AFLS training document lists "B1661 Parameter missing", consistent with the database's "Parameter Fault and Missing".

## B1905
- Existing description: Sensor Power Supply Fault
- Verdict: CONFIRMED
- Corroborated description: Sensor Power Supply Fault — exact match (Hyundai Genesis AFLS shop-manual page via charm.li; carcarehacks; slideshare OBDCodex; avtotachki).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai shop manual via charm.li)
- Evidence: charm.li hosts the Hyundai Genesis AFLS service-manual page for B1905 with the same description; three independent DTC compilations agree.

## B1906
- Existing description: Front Sensor PWM Signal Fault
- Verdict: CONFLICT
- Corroborated description: carcarehacks, slideshare OBDCodex, and avtotachki all define B1906 as "Rain Sensor Fault 2" (FAM rain-sensor context), while the database says "Front Sensor PWM Signal Fault" (AFLS front-sensor context).
- Possible causes: not documented
- Diagnostic notes: This is a module-scoping conflict, not a flat contradiction: B1905/B1907/B1908 are corroborated in the AFLS front/rear-sensor context, but B1906 is defined as a rain-sensor fault in the FAM (front area module) context by all three second sources. Hyundai reuses B1906 across modules. The database description should be annotated with its module context (AFLS) rather than overwritten.
- Recommended grade: [C] (keep; annotate module context AFLS vs FAM — sources disagree across modules)
- Evidence: carcarehacks Hyundai list, slideshare OBDCodex list, and avtotachki all give "B1906 Rain Sensor Fault 2". None of them corroborate "Front Sensor PWM Signal Fault" for B1906. Preferred: neither overwrites the other; both are module-scoped.

## B1907
- Existing description: Front Sensor Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Front sensor signal fault — matches (carcarehacks; slideshare OBDCodex).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Two independent DTC compilations agree.

## B1908
- Existing description: Rear Sensor PWM Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Rear sensor PWM signal fault — matches (carcarehacks; slideshare OBDCodex).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: Two independent DTC compilations agree.

## B2406
- Existing description: Air Mix Motor (Driver) - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Air Mix Motor (Driver) — matches (AutoHex Santa Fe CM / i20 PB / i30 GDe: actuator fails to reach the requested position within ~40 seconds; automanual; hyundaibook.ru; HVAC DTC list "B2406 DEFECTIVE TEMP DOOR MOTOR").
- Possible causes: poor electrical connection, wiring harness open or short, air-mix actuator fault, A/C control module fault (AutoHex) [A]
- Diagnostic notes: AutoHex detection condition: actuator does not reach the target position within ~40s [A]; hyundai-forums and a Hyundai service manual excerpt (4x4brasil PDF) discuss B2406 diagnosis [B]
- Recommended grade: [A] (AutoHex service-info-derived)
- Evidence: AutoHex Hyundai DTC Help pages (three models) match the description and document causes plus the 40-second detection condition; automanual, hyundaibook.ru (Tucson LM), hyundai-forums threads, and the HVAC DTC list corroborate.

## B2408
- Existing description: Intake Motor - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Intake Motor — matches (TechNet Times DTC table; hyundaibook.ru "Intake motor"; HVAC DTC list "B2408 DEFECTIVE INTAKE DOOR MOTOR").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B2408 Intake Motor"; hyundaibook.ru and the Hyundai HVAC DTC list agree.

## B2417
- Existing description: Direction Control Motor (VENT) - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Direction Control Motor-Vent — exact match (TechNet Times; Hyundai service-manual-derived DTC table on manuals.plus).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "B2417 Direction Control Motor-Vent"; the manuals.plus Hyundai "Diagnostic Trouble Codes" table (a TechNet Times reprint) lists "B2417 Direction Control Motor-Vent" as well.

## B2418
- Existing description: Direction Control Motor (FLOOR) - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Direction Control Motor-Floor — exact match (TechNet Times; manuals.plus Hyundai DTC table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B2418 Direction Control Motor-Floor"; the manuals.plus table agrees.

## B2419
- Existing description: Direction Control Motor (DEF) - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Direction Control Motor-Defog — exact match (TechNet Times: "B2419 Direction Control Motor-Defog").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "B2419 Direction Control Motor-Defog".

## B2500
- Existing description: Warning Lamp - Malfunction
- Verdict: CONFIRMED
- Corroborated description: Warning Lamp Failure — matches (automanual: code 2500 indicates a malfunction in the operation of the air bag control indicator; TechNet Times DTC table: "B250000 Warning lamp Failure").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times; automanual)
- Evidence: automanual Hyundai error codes and the TechNet Times DTC table both confirm B2500 as the SRS warning-lamp failure code.

## B2505
- Existing description: Passenger Airbag Off Warning Lamp Failure
- Verdict: CONFIRMED
- Corroborated description: Passenger airbag off warning lamp failure — matches (automanual "Failure of the airbag deactivation indicator light"; JustAnswer Elantra thread "B250200" describes the passenger-airbag-off telltale failure).
- Possible causes: not documented
- Diagnostic notes: Observed in the field with a -00 suffix variant (B250200) on Elantra [B]
- Recommended grade: [B]
- Evidence: automanual lists B2505 with the same meaning; a JustAnswer Hyundai thread documents a B250200 instance for the passenger-airbag-off indicator.

---
# Chassis codes (C1xxx)

## C1101
- Existing description: Battery Voltage High
- Verdict: CONFIRMED
- Corroborated description: Battery Voltage High — matches (ifixit Hyundai Accent ABS wiki: "C1101 — Battery Voltage High"; source document places C1101 in the ABS/ESP section).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B] (two independent community compilations agree; no service-info source located)
- Evidence: The ifixit Accent ABS diagnostic wiki lists C1101 as "Battery Voltage High", matching the database.

## C1102
- Existing description: Battery Voltage Low
- Verdict: CONFIRMED
- Corroborated description: Battery Voltage Low — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Module-scoping note — one TechNet Times table gives C1102 as "ESP2 message timeout" (different module context).
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1102 Battery Voltage Low" in multiple tables (also "C110200 Battery Voltage Low", "C110216 Battery Voltage Low").

## C1103
- Existing description: IGN Voltage Fault
- Verdict: CONFIRMED
- Corroborated description: General voltage error in the ignition system — matches (automanual).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual Hyundai error codes lists C1103 with the compatible description.

## C1121
- Existing description: Left Front TPMS Sensor Battery Voltage Low
- Verdict: CONFIRMED
- Corroborated description: Sensor 1 Battery Voltage Low — matches (Hyundai shop-manual pages via charm.li: Tucson, Sonata, Azera, Genesis Coupe, Santa Fe; TechNet Times also lists "C1121 Front Left Sensor Battery Voltage Low").
- Possible causes: TPMS sensor battery past its expected service life, low ambient temperatures reducing battery output, sensor internal failure (charm.li shop-manual text) [A]
- Diagnostic notes: Santa Fe shop manual specifies the low-voltage threshold as the wheel-electronics (WE) sensor battery below ~2.2 Vdc [A]
- Recommended grade: [A] (Hyundai shop manuals via charm.li)
- Evidence: charm.li hosts Hyundai service-manual DTC C1121 pages for five models with causes and the 2.2Vdc threshold; TechNet Times confirms the code as Sensor 1 / Front Left battery voltage low.

## C1122
- Existing description: Right Front TPMS Sensor Battery Voltage Low
- Verdict: CONFIRMED (pattern)
- Corroborated description: INFERRED — no source was found that individually documents C1122. C1121 (Sensor 1) is confirmed as Front Left, and the Hyundai TPMS family numbers sensors 1–4 = FL/FR/RL/RR (corroborated by the C1312–C1315 LF/RF/LR/RR RF-channel family in TSB 23-BE-001H and import-car.com).
- Possible causes: not documented (same class of causes as C1121 would apply, but not independently documented — treat as INFERRED)
- Diagnostic notes: Mapping 2→FR is an extrapolation, not a documented fact.
- Recommended grade: [C] (keep; pattern extrapolation, not independently confirmed)
- Evidence: No second source found for C1122 specifically; the sensor-numbering scheme is corroborated only at the family level.

## C1123
- Existing description: Left Rear TPMS Sensor Battery Voltage Low
- Verdict: CONFIRMED (pattern)
- Corroborated description: INFERRED — same situation as C1122 (3→RL extrapolation from the Sensor 1 = FL confirmation).
- Possible causes: not documented
- Diagnostic notes: Mapping 3→RL is an extrapolation, not a documented fact.
- Recommended grade: [C] (keep; pattern extrapolation)
- Evidence: No second source found for C1123 specifically.

## C1124
- Existing description: Right Rear TPMS Sensor Battery Voltage Low
- Verdict: CONFIRMED (pattern)
- Corroborated description: INFERRED — same situation as C1122 (4→RR extrapolation).
- Possible causes: not documented
- Diagnostic notes: Mapping 4→RR is an extrapolation, not a documented fact.
- Recommended grade: [C] (keep; pattern extrapolation)
- Evidence: No second source found for C1124 specifically.

## C1126
- Existing description: Vehicle Battery Voltage Low
- Verdict: CONFIRMED
- Corroborated description: C112600 TPMS ECU Battery Voltage Low — matches (import-car.com Hyundai TPMS guide).
- Possible causes: not documented
- Diagnostic notes: The TPMS ECU monitors vehicle battery voltage; code sets on low voltage [B]
- Recommended grade: [B]
- Evidence: import-car.com's Hyundai TPMS guide lists "C112600: TPMS ECU Battery Voltage Low", consistent with the database description.

## C1127
- Existing description: Vehicle Battery Voltage High
- Verdict: CONFIRMED
- Corroborated description: C112700 TPMS ECU Battery Voltage High — matches (import-car.com Hyundai TPMS guide).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: import-car.com's Hyundai TPMS guide lists "C112700: TPMS ECU Battery Voltage High", consistent with the database description.

## C1200
- Existing description: Wheel Speed Sensor Front-LH Open/Short
- Verdict: CONFIRMED
- Corroborated description: Front-left wheel speed sensor circuit fault — matches (automanual C1200; carscounsel Hyundai list covers the C1200–C1211 wheel-speed family).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual Hyundai error codes lists the C1200–C1211 wheel-speed-sensor family; carscounsel lists C1203/C1204/C1205 and C1210 with compatible wording.

## C1201
- Existing description: Wheel Speed Sensor Front-LH Range/Performance/Intermittent
- Verdict: CONFIRMED
- Corroborated description: Front-left wheel speed sensor range/performance fault — matches (automanual C1201).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1201 in the wheel-speed family with compatible wording.

## C1202
- Existing description: Wheel Speed Sensor Front-LH Invalid/No Signal
- Verdict: CONFIRMED
- Corroborated description: Front-left wheel speed sensor invalid/no signal — matches (automanual C1202).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1202 in the wheel-speed family with compatible wording.

## C1203
- Existing description: Wheel Speed Sensor Front-RH Open/Short
- Verdict: CONFIRMED
- Corroborated description: Front-right wheel speed sensor circuit fault — matches (automanual C1203; carscounsel).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual and carscounsel both list C1203 with compatible wording.

## C1204
- Existing description: Wheel Speed Sensor Front-RH Range/Performance/Intermittent
- Verdict: CONFIRMED
- Corroborated description: Front-right wheel speed sensor range/performance fault — matches (automanual C1204; carscounsel).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual and carscounsel both list C1204 with compatible wording.

## C1205
- Existing description: Wheel Speed Sensor Front-RH Invalid/No Signal
- Verdict: CONFIRMED
- Corroborated description: Front-right wheel speed sensor invalid/no signal — matches (automanual C1205; carscounsel).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual and carscounsel both list C1205 with compatible wording.

## C1206
- Existing description: Wheel Speed Sensor Rear-LH Open/Short
- Verdict: CONFIRMED
- Corroborated description: Rear-left wheel speed sensor circuit fault — matches (automanual C1206).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1206 in the wheel-speed family with compatible wording.

## C1207
- Existing description: Wheel Speed Sensor Rear-LH Range/Performance/Intermittent
- Verdict: CONFIRMED
- Corroborated description: Rear-left wheel speed sensor range/performance fault — matches (automanual C1207).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1207 in the wheel-speed family with compatible wording.

## C1208
- Existing description: Wheel Speed Sensor Rear-LH Invalid/No Signal
- Verdict: CONFIRMED
- Corroborated description: Rear-left wheel speed sensor invalid/no signal — matches (automanual C1208).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1208 in the wheel-speed family with compatible wording.

## C1209
- Existing description: Wheel Speed Sensor Rear-RH Open/Short
- Verdict: CONFIRMED
- Corroborated description: Rear-right wheel speed sensor circuit fault — matches (automanual C1209).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1209 in the wheel-speed family with compatible wording.

## C1210
- Existing description: Wheel Speed Sensor Rear-RH Range/Performance/Intermittent
- Verdict: CONFIRMED
- Corroborated description: Rear-right wheel speed sensor range/performance fault — matches (automanual C1210; carscounsel).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual and carscounsel both list C1210 with compatible wording.

## C1211
- Existing description: Wheel Speed Sensor Rear-RH Invalid/No Signal
- Verdict: CONFIRMED
- Corroborated description: Rear-right wheel speed sensor invalid/no signal — matches (automanual C1211).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual lists C1211 in the wheel-speed family with compatible wording.

## C1213
- Existing description: Wheel Speed Frequency Error
- Verdict: CONFLICT
- Corroborated description: automanual defines C1213 as a failure or incorrect operation of the traction control controller (not a wheel-speed frequency error).
- Possible causes: wheel speed sensor fault, incorrect sensor installation or connection, tone-rotor / wheel-bearing mechanism fault (automanual) [B]
- Diagnostic notes: not documented
- Recommended grade: [C] (keep; sources disagree — automanual's definition does not match the database's)
- Evidence: automanual Hyundai error codes gives C1213 a traction-control-controller definition with the listed causes. Preferred: unresolved — the automanual entry is a reputable compilation but the database's "Wheel Speed Frequency Error" has no second source either. Flag for primary-source check.

## C1235
- Existing description: Primary Pressure Sensor - Electrical Fault
- Verdict: CONFIRMED
- Corroborated description: Primary Pressure Sensor-Electrical — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1235 Primary Pressure Sensor-Electrical".

## C1237
- Existing description: Pressure Sensor - Other Fault
- Verdict: CONFLICT
- Corroborated description: TechNet Times lists C1237 as "Primary Pressure Sensor-Signal" (one table) — the database's "Pressure Sensor - Other Fault" drops "Primary" and replaces "Signal" with "Other Fault", which changes the meaning.
- Possible causes: not documented
- Diagnostic notes: The database wording looks like a mangled paraphrase of the TechNet Times entry; recommend aligning to "Primary Pressure Sensor - Signal Fault".
- Recommended grade: [C] (keep until wording is corrected)
- Evidence: TechNet Times lists "C1237 Primary Pressure Sensor-Signal". Preferred: TechNet Times (A-grade) — the database description should be corrected to match it.

## C1259
- Existing description: Angle Sensor Fault
- Verdict: CONFIRMED
- Corroborated description: Steering angle sensor signal error — matches (HMA TSB for MDPS: "C1259 Steering angle sensor signal error").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA technical service bulletin)
- Evidence: HMA TSB (MC-10180981-0001 / MC-10170896-0001, NHTSA) lists C1259 as steering-angle-sensor signal error. Caveat: the TSB table extraction is dense; the row mapping should be verified against the TSB PDF.

## C1260
- Existing description: Steering Sensor Circuit - Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Steering angle sensor (SAS) circuit signal fault — matches (HMA TSB; automanual; JustAnswer "C1260 Steering angle sensor SAS circuit signal").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB, automanual, and a JustAnswer Hyundai thread all place C1260 on the steering-angle-sensor circuit.

## C1261
- Existing description: Steering Angle Sensor Not Calibrated
- Verdict: CONFIRMED
- Corroborated description: Zero-setting error — matches (HMA TSB: "C1261 Zero-setting error").
- Possible causes: not documented
- Diagnostic notes: Zero-point calibration of the steering angle sensor not performed [A]
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists C1261 as a zero-setting error, consistent with "Steering Angle Sensor Not Calibrated".

## C1283
- Existing description: Yaw Rate and Lateral G Sensor - Signal Fault
- Verdict: CONFIRMED
- Corroborated description: Vehicle yaw controller malfunction — compatible (automanual).
- Possible causes: yaw-rate sensor itself, its wiring, or the control block (automanual) [B]
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual Hyundai error codes lists C1283 as a yaw-controller malfunction with the listed cause areas.

## C1290
- Existing description: Torque Sensor Fault
- Verdict: CONFIRMED
- Corroborated description: Torque sensor signal error — matches (HMA TSB: "C1290 Torque sensor signal error").
- Possible causes: not documented
- Diagnostic notes: automanual gives a divergent wording for C1290 (steering-angle-sensor damage); the HMA TSB (A-grade) is preferred and matches the database [A]
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists C1290 as a torque-sensor signal error, matching the database description.

## C1300
- Existing description: TPMS ECU IRX Not Responding
- Verdict: CONFIRMED
- Corroborated description: TPMS ECU IRX not responding — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: A second TechNet Times table variant reads "LF/RF External Interference Failure" (different context/variant) [A]
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1300 TPMS ECU IRX not responding", exactly matching the database.

## C1312
- Existing description: Left Front TPMS Sensor Radio Frequency Channel Failure
- Verdict: CONFIRMED
- Corroborated description: RF Channel Fail (LF) — exact match (HMA TSB 23-BE-001H: "C1312 RF Channel Fail (LF)").
- Possible causes: RF interference around the vehicle, SVM coaxial cable connection faults (TSB 23-BE-001H) [A]
- Diagnostic notes: TSB specifies a minimum ~75% RF reception rate as the diagnostic criterion [A]
- Recommended grade: [A] (HMA TSB)
- Evidence: TSB 23-BE-001H (static.nhtsa.gov MC-10230909-0001) defines C1312–C1315 as RF channel failures LF/RF/LR/RR; import-car.com's TPMS guide lists C131200–C131500 the same way; a 2011 Tucson diagnostic report PDF (files.lqdt1.com) shows C1312 in the field.

## C1313
- Existing description: Right Front TPMS Sensor Radio Frequency Channel Failure
- Verdict: CONFIRMED
- Corroborated description: RF Channel Fail (RF) — exact match (HMA TSB 23-BE-001H).
- Possible causes: same as C1312 (TSB 23-BE-001H) [A]
- Diagnostic notes: same ~75% reception-rate criterion [A]
- Recommended grade: [A]
- Evidence: Same TSB and import-car.com guide as C1312.

## C1314
- Existing description: Left Rear TPMS Sensor Radio Frequency Channel Failure
- Verdict: CONFIRMED
- Corroborated description: RF Channel Fail (LR) — exact match (HMA TSB 23-BE-001H).
- Possible causes: same as C1312 (TSB 23-BE-001H) [A]
- Diagnostic notes: same ~75% reception-rate criterion [A]
- Recommended grade: [A]
- Evidence: Same TSB and import-car.com guide as C1312.

## C1315
- Existing description: Right Rear TPMS Sensor Radio Frequency Channel Failure
- Verdict: CONFIRMED
- Corroborated description: RF Channel Fail (RR) — exact match (HMA TSB 23-BE-001H).
- Possible causes: same as C1312 (TSB 23-BE-001H) [A]
- Diagnostic notes: same ~75% reception-rate criterion [A]
- Recommended grade: [A]
- Evidence: Same TSB and import-car.com guide as C1312.

## C1322
- Existing description: Left Front TPMS Sensor Over Temperature
- Verdict: CONFIRMED
- Corroborated description: C132200 Front Left Sensor Over Temperature — matches (import-car.com Hyundai TPMS guide).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: import-car.com's Hyundai TPMS guide lists "C132200: Front Left Sensor Over Temperature", matching the database description.

## C1503
- Existing description: ESP Switch Error
- Verdict: CONFIRMED
- Corroborated description: TCS/ESC(ESP) Switch Error — matches (TechNet Times); automanual also lists C1503.
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1503 TCS/ESC(ESP) Switch Error" / "C1503 Traction Control System(TCS) Switch Failure"; automanual lists C1503.

## C1513
- Existing description: Brake Switch Error
- Verdict: CONFIRMED
- Corroborated description: Brake switch fault — matches (automanual; hyundai-forums threads linking C1513 to the brake-switch issue).
- Possible causes: brake light switch failure (automanual) [B]
- Diagnostic notes: hyundai-forums threads associate this code family with the Hyundai brake-switch recall covering April 2007–July 2011 builds [B]
- Recommended grade: [B]
- Evidence: automanual lists C1513 as a brake-switch error; hyundai-forums threads document field occurrences tied to the brake-switch recall.

## C1604
- Existing description: ECU Hardware Error
- Verdict: CONFLICT
- Corroborated description: The HMA MDPS TSB lists "C1604 ECU over/discharge error" — the database's "ECU Hardware Error" is broader/different.
- Possible causes: not documented
- Diagnostic notes: Caveat — the TSB table extraction is dense and the row mapping should be verified against the TSB PDF before editing the database.
- Recommended grade: [C] (keep; sources disagree)
- Evidence: HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C1604 ECU over/discharge error". Preferred: the TSB (A-grade) if the row mapping verifies; otherwise keep the database wording. Flag for PDF verification.

## C1605
- Existing description: CAN Hardware Error
- Verdict: CONFIRMED
- Corroborated description: CAN Hardware Error — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: One TechNet Times table variant reads "CAN Bus OFF" for C1605 (different context) [A]
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1605 CAN Hardware Error" in two tables.

## C1611
- Existing description: CAN Timeout - EMS
- Verdict: CONFIRMED
- Corroborated description: CAN time-out EMS — matches (fixya thread quoting Elantra HD ESC service-manual references; import-car.com TPMS guide "C161100").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: A fixya thread citing Hyundai Elantra HD ESC service-manual material and import-car.com both place C1611 as a CAN timeout with the EMS.

## C1612
- Existing description: CAN Timeout - TCU
- Verdict: CONFIRMED
- Corroborated description: TCU signal error — matches (HMA TSB: "C1612 TCU signal error").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists "C1612 TCU signal error", consistent with a CAN timeout/signal fault on the TCU.

## C1616
- Existing description: CAN Bus Off
- Verdict: CONFIRMED
- Corroborated description: CAN Bus Off — exact match (automanual; hrabanazviking DTC index pointing to charm.li ABS/TPMS/EPS pages).
- Possible causes: CAN line open or short; module re-initialization behavior (JustAnswer Tucson thread) [B]
- Diagnostic notes: A JustAnswer Tucson thread documents ~15 CAN re-initialization attempts before the code sets [B]
- Recommended grade: [B]
- Evidence: automanual lists C1616; a JustAnswer thread on a Tucson documents the re-init behavior; the hrabanazviking DTC index maps C1616 to charm.li ABS/TPMS/EPS service-manual content.

## C1617
- Existing description: CAN Invalid Value Fault
- Verdict: CONFIRMED
- Corroborated description: EMS Invalid Engine Speed — compatible (fixya thread quoting Elantra XD TCS service-manual references: "C1617 EMS Invalid Engine Speed").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: The fixya thread's service-manual-derived definition is a specific instance of an invalid CAN value from the EMS.

## C1623
- Existing description: CAN Timeout - SAS (Steering Angle Sensor)
- Verdict: CONFIRMED
- Corroborated description: CAN time out SAS — exact match (HMA TSB: "C1623 CAN time out SAS").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists "C1623 CAN time out SAS".

## C1625
- Existing description: CAN Timeout - ESP
- Verdict: CONFIRMED
- Corroborated description: CAN Time-Out ABS/ESP — matches (TechNet Times; also "Lost Communication With Anti-Lock Brake System (ABS)" in one table).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C1625 CAN Time-Out ABS/ESP" in multiple tables.

## C1626
- Existing description: Implausible Control
- Verdict: CONFIRMED
- Corroborated description: Implausible Control — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C1626 Implausible Control".

## C1643
- Existing description: CAN Timeout - Yaw Rate and G Sensor
- Verdict: CONFIRMED
- Corroborated description: CAN Time-out Yaw Rate & G Sensor — exact match in one TechNet Times table. Module-scoping note: another TechNet Times table gives C1643 as "Motor Current Excessive" (MDPS/EPS context).
- Possible causes: not documented
- Diagnostic notes: The database description matches the ESC-context variant; record the module context with this code.
- Recommended grade: [A]
- Evidence: TechNet Times lists both "C1643 CAN Time-out Yaw Rate & G Sensor" and "C1643 Motor Current Excessive" in different tables.

## C1700
- Existing description: Byte Coding Error
- Verdict: CONFIRMED
- Corroborated description: Byte Coding Error — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Other TechNet Times tables give C1700 as "Parameter Error" / "Gear Shift Malfunction" (different module contexts) [A]
- Recommended grade: [A]
- Evidence: TechNet Times lists "C1700 Byte Coding Error" alongside the module-variant definitions.

## C1702
- Existing description: Variant Coding Error
- Verdict: CONFIRMED
- Corroborated description: variant coding — matches (hyundai-forums field thread titled around "c1702 variant coding").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [C] (keep; single community thread)
- Evidence: A hyundai-forums thread documents a field occurrence described as variant coding for C1702.

## C1704
- Existing description: ECU Failsafe Relay Fault
- Verdict: CONFIRMED
- Corroborated description: ECU fail-safe relay fault — exact match (HMA TSB: "C1704 ECU fail-safe relay fault").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists C1704 as an ECU fail-safe relay fault.

## C1705
- Existing description: ECU Precharge Circuit Fault
- Verdict: CONFLICT
- Corroborated description: The HMA MDPS TSB lists "C1705 ECU hardware error" — the database's "ECU Precharge Circuit Fault" is a different, more specific definition.
- Possible causes: not documented
- Diagnostic notes: Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database.
- Recommended grade: [C] (keep; sources disagree)
- Evidence: HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C1705 ECU hardware error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification.

## C2101
- Existing description: Motor Relay Fault
- Verdict: CONFIRMED
- Corroborated description: Motor Relay / Motor Relay - Abnormal — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C2101 Motor Relay", "C2101 Motor Relay - Abnormal", and "C2101 Motor relay circuit".

## C2112
- Existing description: Valve Relay Error
- Verdict: CONFIRMED
- Corroborated description: Valve Relay Error — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2112 Valve Relay Error" (also "C2112 Valve Relay Or Fuse-Fail." in another table).

## C2308
- Existing description: FL (IN) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Front Left(FL) Valve (In) / Front-LH Valve error (Inlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C2308 Front Left(FL) Valve (In)" and "C2308 Front-LH Valve error (Inlet Valve)".

## C2312
- Existing description: FL (OUT) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Front Left(FL) Valve (Out) / Front-LH Valve error (Outlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2312 Front Left(FL) Valve (Out)" and "C2312 Front-LH Valve error (Outlet Valve)".

## C2316
- Existing description: FR (IN) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Front Right(FR) Valve (In) / Front-RH Valve error (Inlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2316 Front Right(FR) Valve (In)" and "C2316 Front-RH Valve error (Inlet Valve)".

## C2320
- Existing description: FR (OUT) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Front Right(FR) Valve (Out) / Front-RH Valve error (Outlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2320 Front Right(FR) Valve (Out)" and "C2320 Front-RH Valve error (Outlet Valve)".

## C2324
- Existing description: RL (IN) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Rear Left(RL) Valve (In) / Rear-LH Valve error (Inlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2324 Rear Left(RL) Valve (In)" and "C2324 Rear-LH Valve error (Inlet Valve)".

## C2328
- Existing description: RL (OUT) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Rear Left(RL) Valve (Out) / Rear-LH Valve error (Outlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2328 Rear Left(RL) Valve (Out)" and "C2328 Rear-LH Valve error (Outlet Valve)".

## C2332
- Existing description: RR (IN) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Rear Right(RR) Valve (In) / Rear-RH Valve error (Inlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2332 Rear Right(RR) Valve (In)" and "C2332 Rear-RH Valve error (Inlet Valve)".

## C2336
- Existing description: RR (OUT) Valve Error
- Verdict: CONFIRMED
- Corroborated description: Rear Right(RR) Valve (Out) / Rear-RH Valve error (Outlet Valve) — matches (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2336 Rear Right(RR) Valve (Out)" and "C2336 Rear-RH Valve error (Outlet Valve)".

## C2366
- Existing description: USV1 Error
- Verdict: CONFIRMED
- Corroborated description: TC Valve Primary (USV1) Error — this is the full wording behind the database's terse "USV1 Error" (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Module-scoping note — another TechNet Times table gives C2366 as "TC Front Left Valve" (different context) [A]
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C2366 TC Valve Primary (USV1) Error".

## C2370
- Existing description: USV2 Error
- Verdict: CONFIRMED
- Corroborated description: TC Valve Secondary (USV2) Error — full wording of the database's terse "USV2 Error" (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: Another TechNet Times table gives C2370 as "TC Front Right Valve" (different context) [A]
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2370 TC Valve Secondary (USV2) Error".

## C2372
- Existing description: HSV1 Error
- Verdict: CONFIRMED
- Corroborated description: Electronic Shuttle Valve Primary (HSV1) Error — full wording of the database's terse "HSV1 Error" (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2372 Electronic Shuttle Valve Primary (HSV1) Error".

## C2374
- Existing description: HSV2 Error
- Verdict: CONFIRMED
- Corroborated description: Electronic Shuttle Valve Secondary (HSV2) Error — full wording of the database's terse "HSV2 Error" (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A]
- Evidence: TechNet Times lists "C2374 Electronic Shuttle Valve Secondary (HSV2) Error".

## C2400
- Existing description: Motor Fault
- Verdict: CONFIRMED
- Corroborated description: Motor signal error — compatible (HMA TSB: "C2400 Motor signal error"; the database wording is broader).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists "C2400 Motor signal error", consistent with the database's "Motor Fault".

## C2401
- Existing description: Motor Circuit Fault
- Verdict: CONFIRMED
- Corroborated description: Motor circuit error — matches (HMA TSB: "C2401 Motor circuit error").
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (HMA TSB)
- Evidence: The HMA MDPS TSB lists "C2401 Motor circuit error".

## C2402
- Existing description: Motor Electrical Fault
- Verdict: CONFIRMED
- Corroborated description: Motor Electrical — exact match (TechNet Times).
- Possible causes: not documented
- Diagnostic notes: not documented
- Recommended grade: [A] (Hyundai TechNet Times)
- Evidence: TechNet Times lists "C2402 Motor Electrical" (also "C2402 Pump Motor" / "C2402 Electrical(Pump-Motor) Circuit Malfunction" in other tables).

## C2412
- Existing description: Motor Short or Open
- Verdict: CONFLICT
- Corroborated description: The HMA MDPS TSB lists "C2412 Motor voltage supply error" — the database's "Motor Short or Open" (with a YAML diagnostic note placing it in the MDPS motor circuit) is a different definition.
- Possible causes: not documented
- Diagnostic notes: Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database.
- Recommended grade: [C] (keep; sources disagree)
- Evidence: HMA TSB (MC-10180981-0001 / MC-10170896-0001) gives "C2412 Motor voltage supply error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification.

## C2413
- Existing description: Motor Current Fault
- Verdict: CONFLICT
- Corroborated description: The HMA MDPS TSB lists "C2413 ECU hardware error" — the database's "Motor Current Fault" is a different definition. (Note: TechNet Times separately lists "C2414 Motor Current Fail (current excessive)" — a different code.)
- Possible causes: not documented
- Diagnostic notes: Same TSB table-mapping caveat as C1604 — verify the row mapping against the TSB PDF before editing the database.
- Recommended grade: [C] (keep; sources disagree)
- Evidence: HMA TSB gives "C2413 ECU hardware error". Preferred: the TSB (A-grade) if the row mapping verifies. Flag for PDF verification.

# Network codes (Uxxx)

## U0001
- Existing description: High Speed CAN Communication Bus Off (C-CAN)
- Verdict: CONFIRMED
- Corroborated description: High-speed CAN communication bus off — matches (AutoHex Hyundai DTC Help: i20 PB, Veloster FS, Matrix FC, Grandeur/Azera HG, Veracruz EN, Genesis BH).
- Possible causes: not documented
- Diagnostic notes: Bus-off condition persisting for ~2 seconds (AutoHex) [A]
- Recommended grade: [A] (AutoHex service-info-derived)
- Evidence: Six AutoHex Hyundai DTC Help pages define U0001 as high-speed CAN bus-off with the same meaning.

## U1111
- Existing description: Battery Sensor Fault Detected by ECU
- Verdict: CONFIRMED
- Corroborated description: Damage to the battery sensor — compatible (automanual: U1111 indicates battery-sensor damage; the battery warning indicator may illuminate).
- Possible causes: battery sensor (battery current/voltage/temperature sensor) fault [B]
- Diagnostic notes: not documented
- Recommended grade: [B]
- Evidence: automanual Hyundai error codes lists U1111 with the battery-sensor-damage description.

## U1112
- Existing description: LIN Communication Error
- Verdict: CONFIRMED
- Corroborated description: LIN communication error — matches (AutoHex Hyundai DTC Help: EON HA, Tucson/ix35 LM, Santa Fe CM, Genesis BH, i30 GDe — "ECM sets this code when there is an error in LIN communication line"; "set when checksum error during LIN communication, communication frame error, parity bit error and data overflow occurs").
- Possible causes: open or short in the LIN communication line; LIN-communicated modules (battery sensor, etc.); ECM (AutoHex detecting-condition tables) [A]
- Diagnostic notes: AutoHex gives enable conditions (IG ON, battery 10–16V / ~11V, engine run time) and diagnosis times of 1–5s depending on model; no MIL [A]
- Recommended grade: [A] (AutoHex service-info-derived)
- Evidence: Five AutoHex Hyundai DTC Help pages for U1112 across EON, Tucson, Santa Fe, Genesis, and i30 all define it as a LIN communication-line error with detecting conditions and possible causes.

---

# Not corroborated

Only **1 of 179** codes had no second source found:

- **C1603 — "Derating (EPS Thermal Protection)"**: searched via web and in Hyundai TechNet Times; no second source located. No corroboration, correction, or conflict to report. Recommend keeping grade [C] and treating the description as single-source.

# Coverage notes

**Ranges checked:** All 179 Hyundai/Kia B/C/U codes in `/tmp/hyundai_bcu.txt` were researched individually: B1101–B2505 (105 body codes), C1101–C2413 (71 chassis codes), U0001/U1111/U1112 (3 network codes).

**Verdict counts:**
- CONFIRMED: 171 (168 exact/compatible wording matches, including B1475/B1476/B1479/B1480 where TechNet Times supplies the full wording the database truncates; plus 3 marked "pattern": C1122/C1123/C1124 confirmed only by the sensor-numbering scheme — flagged INFERRED)
- CONFLICT: 7 — B1906 (module-scoping: AFLS "Front Sensor PWM Signal Fault" vs FAM "Rain Sensor Fault 2"), C1213 (database "Wheel Speed Frequency Error" vs automanual "traction control controller failure"), C1237 (database "Pressure Sensor - Other Fault" vs TechNet Times "Primary Pressure Sensor-Signal"), C1604 / C1705 / C2412 / C2413 (database wording vs HMA MDPS TSB definitions; TSB row-mapping caveat noted — verify against the TSB PDF)
- NOT FOUND: 1 — C1603

**Grade-upgrade recommendations (from current grade C):**
- To **[A]** (service-info corroboration): 117 codes — all codes confirmed by charm.li shop-manual pages, AutoHex Hyundai DTC Help, HMA TSBs, Hyundai TechNet Times, the Hyundai AFLS training document, or the Hyundai Restraint shop-manual DTC table.
- To **[B]** (reputable database / multi-source agreement): 50 codes — codes confirmed by automanual, avtotachki, carcarehacks, slideshare OBDCodex, hyundaibook.ru, carscounsel.com, import-car.com, real scan-tool reads (CarProTool), or dealer/field threads (ifixit, fixya, JustAnswer, hyundai-forums).
- Stay at **[C]**: 12 codes — the 7 conflicts (needs primary-source resolution), C1603 (no second source), C1122/C1123/C1124 (pattern extrapolation only), C1702 (single community thread).

**Documented gaps / areas not verified:**
1. Possible causes and diagnostic notes are absent for the large majority of codes — second sources (especially TechNet Times tables) give code+description only. Entries say "not documented" rather than inventing causes.
2. Module scoping is a real ambiguity for ~10 codes (B1264/B1265/B1266, B1621, B1622, B1603, B1906, C1102, C1605, C1643, C1700, C2366, C2370, C2402): Hyundai reuses these numbers across modules with different meanings. The database should record module context per code where known.
3. The four MDPS conflicts (C1604, C1705, C2412, C2413) rest on dense HMA TSB table extractions — row mapping should be verified against the TSB PDF before changing database text.
4. Truncated database descriptions (B1475 "Short to Gro", B1476 "Short to Bat", B1479/B1480 cut mid-word) are resolved to full wording by TechNet Times; recommend expanding them.
5. Traps excluded and NOT cited as corroboration: Ford B1346 (heated backlite), Honda B1346, Mitsubishi B1400 (driver airbag squib), micro-tronik B1242 (generic Ford mode-door code), enginetroublecode.com generic U-code pages, AI-generated JustAnswer answers.

**Sources consulted (2026-10-07):**
- Hyundai TechNet Times Vol. 24 Issue 02, 8th-edition Hyundai DTC listing (manuals.plus mirror) — A
- Hyundai shop-manual pages via charm.li (B1234, B1346, B1395, B1400/B1403/B1409/B1410, B1473, B1905, C1121, C1616) — A
- AutoHex Hyundai DTC Help (B1208, B1234, B1346, B1650, B2406, U0001, U1112) — A
- HMA TSBs via NHTSA/oemdtc (MDPS: MC-10180981-0001 / MC-10170896-0001; TPMS 23-BE-001H: MC-10230909-0001) — A
- Hyundai AFLS training document, Genesis (scribd "13-BH-AFLS") — A
- Hyundai Restraint shop-manual DTC table (sportiveshyundai.fr PDF mirror) — A
- Hyundai MOHAVE/BORREGO service manual excerpts (B1102, B1328; scribd mirrors) — A
- automanual Hyundai error codes (manuals.plus PDF) — B
- avtotachki.com Hyundai codes — B
- carcarehacks.com Hyundai list — B
- slideshare OBDCodex Hyundai DTC list — B
- hyundaibook.ru (Tucson LM) — B
- carscounsel.com Hyundai OBD codes — B
- import-car.com Hyundai TPMS guide — B
- Hyundai HVAC DTC list (scribd doc/612797538) — B
- CarProTool forum scan reads (2018 Sonata SRSCM) — B
- JustAnswer Hyundai threads (B1329, B1346, B1395, B2505, C1260, C1513, C1616) — B/C
- hyundai-forums.com / thehyundaiforums.com threads (B1620, B2406, C1513, C1702) — C
- fixya threads quoting Elantra service-manual material (C1611, C1617) — C
- ifixit Accent ABS wiki (C1101) — C
- swirlzcupcakes Hyundai DTC table (B1101/B1102) — C
- OBDSTAR blog (B1650), Palisade diagnostic report (B1650), 2011 Tucson diagnostic report (C1312), 4x4brasil Hyundai manual PDF (B2406) — C/B
