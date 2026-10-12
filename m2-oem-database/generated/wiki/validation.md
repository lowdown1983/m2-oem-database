# Validation test

36 OEM questions, each answered SOLELY from the generated artifacts (`generated/json/` + `generated/rag-chunks.jsonl`). Grades: A/B/C per the database method.

## Q1 — PASS

**Q:** Which DLC pin and bitrate is GM's single-wire GMLAN?

**A:** Pin [1], 33.33 kbps [B]

## Q2 — PASS

**Q:** Which DLC pins carry GM mid-speed GMLAN, and what is the bitrate caveat?

**A:** Pins [3, 11]; 95.2 kbps per ACDelco [A] but one spec excerpt says 95.2-or-125 [B] — model-dependent

## Q3 — PASS

**Q:** Which DLC pins and bitrate is Ford's MS-CAN?

**A:** Pins [3, 11] (Ford-proprietary), 125 kbps [B]

## Q4 — PASS

**Q:** What was Ford's pre-CAN corporate protocol, on which pins, and what is its quirk?

**A:** SCP = J1850 PWM 41.6 kbps on pins [2, 10]; Ford's variant REQUIRES In-Frame Response bytes [B]

## Q5 — PASS

**Q:** What is the Stellantis Secure Gateway, which years, and what does it block?

**A:** SGW (2018+ (one vendor doc says 2017 — unresolved conflict; consensus is 2018+)): CAN firewall at the DLC. Reads (DTCs, live data) still work; WRITES (DTC clear, actuations, programming) blocked without auth. Legitimate paths: AutoAuth ($50/yr shop), wiTECH 2.0, physical bypass [B]

## Q6 — PASS

**Q:** Which DLC pins and bitrate is Stellantis CAN-C1?

**A:** Pins [6, 14], 500 kbps [A]

## Q7 — PASS

**Q:** What are the GM physical diagnostic request/response IDs for the ECM?

**A:** 11-bit USDT: tester sends $7E0-$7E7, ECU answers $7E8-$7EF; ECM = 0x7E0/0x7E8 (verified by ELM327 VIN-read capture) [B]

## Q8 — PASS

**Q:** What is Ford's diagnostic response-ID convention?

**A:** +8 response offset: request 0x7E0 -> response 0x7E8 [B]

## Q9 — PASS

**Q:** Can the M2 watch Ford HS-CAN and MS-CAN at the same time?

**A:** Yes — two independent CAN controllers (HS-CAN 6/14 + MS-CAN 3/11); a switched ELM327 sees only one at a time [B]

## Q10 — PASS

**Q:** Can the M2 participate on a 2021+ F-150 CAN-FD bus?

**A:** No — TJA1051 transceivers are CAN 2.0 only; 2021+ CAN-FD Fords are out of scope for M2 CAN work [B]

## Q11 — PASS

**Q:** What must M2 firmware do before expecting replies from sleeping GM SWCAN modules?

**A:** Send high-voltage wake-up first: mode(2), then mode(3) for normal communication [A]

## Q12 — PASS

**Q:** What was pre-CAN Chrysler's PCI bus, physically?

**A:** SAE J1850 VPW, single wire on DLC pin [2], ~10.4 kbps [B]

## Q13 — PASS

**Q:** Which CAN buses does Toyota expose at the DLC3?

**A:** ONLY the 500 kbps HS CAN V Bus on pins [6, 14]; the 250 kbps MS-CAN sits behind the gateway ECU — one M2 CAN controller normally suffices at the DLC [B]

## Q14 — PASS

**Q:** A generic scanner on Toyota 0x7E0 sees no hybrid DTCs. Which IDs must it use instead?

**A:** HV ECU 0x7E2/0x7EA, HV battery 0x7E3/0x7EB — a generic OBD-II scanner talking only to 0x7E0 never sees hybrid DTCs [B]

## Q15 — PASS

**Q:** What is Honda's B-CAN (speed, wiring), and is it at the OBD-II port?

**A:** Single-wire 33.33 kbps [A]; NOT at the DLC — requires a behind-dash tap (BCM 36-pin connector on 2016 Civic/2017 CR-V). Speed conflict flagged: one community project claims 150 kbps on 2016+ [C], unverified

## Q16 — PASS

**Q:** What is Honda's documented diagnostic CAN addressing?

**A:** 29-bit: tester 0x18DB33F1 -> ECM 0x18DAF110 [B]; try 29-bit first (the 11-bit 0x7E0/0x7E8 path is single-source [C])

## Q17 — PASS

**Q:** What does VW's SFD block, and what does it explicitly NOT block?

**A:** Blocks WRITING services (adaptations, coding, parametrizations) on protected ECUs; per VW's own workshop manual, reads and bootloader-based flashing are NOT SFD-protected. SFD2 on 2024+ [B]

## Q18 — PASS

**Q:** How many CAN pairs does VW expose on the DLC?

**A:** ONE: pins [6, 14] = the diagnosis CAN to the J533 gateway (comfort/infotainment are gateway-internal) [B]

## Q19 — PASS

**Q:** Is Hyundai's M-CAN exposed at the OBD-II port?

**A:** Not confirmed — no source places M-CAN on OBD-II pins; treat as interior-only unless a per-model wiring diagram says otherwise [C]

## Q20 — PASS

**Q:** Can an ELM327/STN chip speak Nissan's DDL/Consult I protocol?

**A:** No — DDL needs a host-generated 153.6 kHz async clock plus 12V idle-low signaling, which no ELM AT command set provides [B]

## Q21 — PASS

**Q:** A mode-03 response contains the two DTC bytes 0x03 0x00. Which code is this and what does it mean?

**A:** P0300 — Random/Multiple Cylinder Misfire Detected [B] (SAE J2012 generic; possible causes include: worn spark plugs; faulty ignition coil(s))

## Q22 — PASS

**Q:** What is Ford-specific DTC P1151?

**A:** P1151 — Lack of HO2S21 Switch — Sensor Indicates Lean (Bank 2) [B] (Ford manufacturer-specific, not SAE generic)

## Q23 — PASS

**Q:** What is Stellantis DTC P1494, and what is a notorious false trigger?

**A:** P1494 — Leak Detection Pump (LDP) Switch or Mechanical Fault — EVAP Leak Detection Pump Pressure Switch Condition [A]; Chrysler's unique LDP EVAP design means an aftermarket gas cap can falsely trigger it

## Q24 — PASS

**Q:** What is GM DTC P1811 and what commonly causes it?

**A:** P1811 — Maximum Adapt and Long Shift [A]; commonly: Pressure control solenoid failure; debris/wear in valve body (torque signal regulator valve or actuator feed limit valve sticking)

## Q25 — PASS

**Q:** How is the v1.4.0 DTC catalog composed for the Big Three?

**A:** 2143 SAE J2012 generic codes (2098 baseline + 45 Toyota-documented SAE entries); Big Three manufacturer-specific: GM 107, Ford 182, Stellantis 106 (v1.4.0 adds 10 import makes on top)

## Q26 — PASS

**Q:** What is Toyota-specific DTC P1346?

**A:** P1346 — VVT Sensor / Camshaft Position Sensor Circuit Range/Performance Problem (Bank 1) [B]

## Q27 — PASS

**Q:** What is Honda DTC P1259, and what should be checked first?

**A:** P1259 — VTEC System Malfunction (Rear Bank / Bank 1) [B]; check first: low engine oil level (VTEC codes are usually oil codes)

## Q28 — PASS

**Q:** What is VW DTC P1476, and what is its 5-digit VAG code?

**A:** P1476 — EVAP Emission Control System Leak Detection Pump — Malfunction / Insufficient Vacuum [B]; 5-digit VAG code 17884 recorded in diagnostic notes

## Q29 — PASS

**Q:** What is Hyundai-specific DTC P1295?

**A:** P1295 — Electronic Throttle Control System Malfunction - Power Management [B]

## Q30 — PASS

**Q:** What is Nissan DTC P1610, and what commonly triggers it spuriously?

**A:** P1610 — NATS Lock Mode — NATS shifted to a mode preventing engine start after 5+ consecutive start attempts with an unregistered key or malfunctioning IMMU/ECM [A]; often just a weak battery or repeated unregistered-key attempts — don't replace NATS parts first

## Q31 — PASS

**Q:** How is the v1.4.0 DTC catalog composed?

**A:** 4411 DTCs total: 2143 SAE generic + 2268 manufacturer-specific; import makes: Toyota 283, Honda 465, VW 140, Hyundai/Kia 440, Nissan 274, Subaru 72, Mazda 40, BMW 45, Mercedes 126, Volvo 33

## Q32 — PASS

**Q:** What is ISO-standard DID 0xF190, and how big is it?

**A:** 0xF190 = VINDataIdentifier: 17 bytes, ASCII [A for 17 — ISO's own scaling example; B for ASCII — white papers and ECU examples agree] [A] (ISO 14229-1:2013)

## Q33 — PASS

**Q:** What is Ford DID 0xD100, and which ECUs support it?

**A:** 0xD100 = ECU Operating State / Mode [A] — supported by ALL Ford ECUs (Ford Global Diagnostic Spec)

## Q34 — PASS

**Q:** A Nissan Leaf TCU identifier is documented as 0x04. Which service reads it — 0x22?

**A:** No — service 0x21-local: Nissan CAN-era modules use KWP2000-style 0x21 local IDs (0x22 rejected with NRC 0x12) [B]

## Q35 — PASS

**Q:** What is Ford as-built module address 7D0, and how is its data addressed?

**A:** 7D0 = Accessory Protocol Interface Module (APIM) — SYNC module [B]; format MODULE-BLOCK-LINE (e.g. 7D0-01-01), trailing group = checksum

## Q36 — PASS

**Q:** How is the v1.4.0 platform-depth layer composed?

**A:** 637 UDS/SSM identifiers (36 ISO-standard + 601 make-specific, incl. 30 Subaru SSM2 parameter addresses), 41 Ford as-built modules, 51 per-platform module maps (13 makes)

**Overall: 36/36 PASS**

_Generated by scripts/build.py — do not hand-edit._
