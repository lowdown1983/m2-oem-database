# Honda/Acura + VW Group body/chassis UDS DIDs (service 0x22) — thin-spot fill

Compiled 2026-10-07. Complements the powertrain-heavy v1.3.0 sets (59 Honda / 280 VW DIDs).
New entries only — nothing below duplicates an existing `dids.yaml` DID *in the same module context*.
Where a DID number already exists on a different module, the conflict is flagged in Coverage notes instead of duplicated.

Grading: A = OEM/primary verified, B = strong community/secondary or multi-source agreement,
C = single weak source. Scalings marked INFERRED where the source itself publishes competing decodings.
Session/Security are stated only as observed in the source captures; "not documented" means exactly that.

---

## 0x202F — ECU 0x714/0x77E (instrument cluster 17)
- Name: ClusterEngineOilTemperature
- Description: Engine oil temperature as displayed/held by the cluster, 1 byte: °C = A − 58. Note the source warns this is the *cluster's* value (modeled on engines without a real oil-temp sensor), not necessarily the ECU sensor; do not "correct" the −58 offset to −60.
- Make: vw (VW Group; MQB-era)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.1 — formula mechanically derived from OBDb v3 captures (CC BY-SA), seen on Audi Q3, Seat Leon, VW Jetta ≤2018, Audi A4/A6/RS3, VW Amarok/Polo, Audi TT

## 0x224B — ECU 0x714/0x77E (instrument cluster 17)
- Name: OilThermalWearRemainingKm
- Description: Oil thermal wear / remaining oil life, 2 bytes big-endian: km = (A×256 + B)
- Make: vw (VW Group; MQB-era)
- Size: 2 bytes
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.1 — seen on VW Golf, VW Tiguan, Audi Q3, VW Jetta (multi-model agreement)

## 0x2299 — ECU 0x714/0x77E (instrument cluster 17)
- Name: ClusterAverageFuelConsumption
- Description: Trip-computer average fuel consumption, 2 bytes big-endian: l/100 km = (A×256 + B) / 10
- Make: vw (VW Group; MQB-era)
- Size: 2 bytes
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [C]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.1 — single-model source (VW Golf), derived from OBDb v3 captures

## 0x1014 — ECU 0x714/0x77E (instrument cluster 17)
- Name: ClusterAmbientAirTemperature
- Description: Ambient air temperature as seen by the cluster, 1 byte: °C = A × 0.5 − 50
- Make: vw (VW Group; MQB-era)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [C]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.1 — single-model source (VW Golf), derived from OBDb v3 captures

## 0x2A07 — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryVoltageIbs
- Description: 12 V battery voltage from the intelligent battery sensor / battery energy management, 2 bytes big-endian: V = (A×256 + B) / 1000 + 4. Served on the 0x710/0x77A CAN pair (on MQB this is the gateway pair serving the J367 battery-monitor subsystem; see Coverage notes).
- Make: vw (VW Group; MQB — Golf, Tiguan, Q3, Jetta)
- Size: 2 bytes
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — seen on VW Golf, VW Tiguan, Audi Q3, VW Jetta ≥2017 (multi-model agreement)

## 0x2A09 — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryCurrentIbs
- Description: 12 V battery current. Two mutually incompatible decodings are published (source's own trap note): 3-byte variant A = ((A×65536 + B×256 + C) × 10 / 10000) − 3000; 4-byte variant A = SIGNED(A×16777216 + B×65536 + C×256 + D) / 1000. DID existence is multi-model; the correct scaling per vehicle is INFERRED — probe both and sanity-gate current to ±250 A.
- Make: vw (VW Group; MQB — Golf, Tiguan, Q3, Jetta)
- Size: 3 bytes (16/24-bit variant) or 4 bytes (32-bit variant)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B] for DID existence; scaling [INFERRED — competing decodings published]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — seen on VW Golf, VW Tiguan, Audi Q3, VW Jetta ≥2017; the doc explicitly flags the two incompatible decodings and advises probing both

## 0x2A0A — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatterySensorTemperature
- Description: Battery sensor temperature, 1 byte: °C = A − 40
- Make: vw (VW Group; MQB — Audi Q3, VW Jetta ≥2022)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [C]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — two-model source (Audi Q3, VW Jetta ≥2022), derived from OBDb v3 captures

## 0x2A0C — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryStateOfCharge12V
- Description: 12 V battery state of charge, 1 byte: % = A (0–100)
- Make: vw (VW Group; MQB — Golf, Tiguan, Q3, Jetta)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — seen on VW Golf, VW Tiguan, Audi Q3, VW Jetta (multi-model agreement)

## 0x2A0F — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryUsableCharge
- Description: Usable 12 V battery charge, 1 byte: Ah = A (0–255)
- Make: vw (VW Group; MQB — Golf, Tiguan, Jetta)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — seen on VW Golf, VW Tiguan, VW Jetta (multi-model agreement)

## 0x2A10 — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryRestVoltage
- Description: Battery voltage at rest, 1 byte: V = A × 54 / 255 + 9 (Audi Q3 uses a different scaling, A / 10 + 9 — verify per model; INFERRED which applies where)
- Make: vw (VW Group; MQB — Golf, Tiguan, Jetta; Q3 variant noted)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B] for DID existence; Q3 scaling variant [INFERRED]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — seen on VW Golf, VW Tiguan, VW Jetta with A×54/255+9; Audi Q3 reports A/10+9

## 0x2A61 — ECU 0x710/0x77A (battery monitor, MQB)
- Name: BatteryTotalCharge
- Description: Lifetime battery charge/discharge energy, 8-byte response holding two 32-bit big-endian fields: total charge Ah = (A×16777216 + B×65536 + C×256 + D) / 10; total discharge Ah = (E×16777216 + F×65536 + G×256 + H) / 10
- Make: vw (VW Group; MQB — Audi Q3, VW Jetta ≥2017)
- Size: 8 bytes (two 32-bit fields)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [C]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — two-model source (Audi Q3, VW Jetta ≥2017), derived from OBDb v3 captures

## 0x2A00 — ECU 0x710/0x77A (battery monitor, MQB)
- Name: StartStopTargetVoltage
- Description: Start/stop system target voltage, 1 byte: V = A / 10 + 10.6
- Make: vw (VW Group; MQB — VW Jetta ≥2017)
- Size: 1 byte
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [C]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.2 — single-model source (VW Jetta ≥2017), derived from OBDb v3 captures

## 0x18A0 — ECU 0x70B/0x775 (direct TPMS 65)
- Name: TirePressureFrontRight
- Description: Direct-TPMS front-right tire pressure; value at payload byte 5 (0-based): bar = F / 40 (0–6.375 bar). Audi TT uses a different layout for the same DIDs (G/10 with a position enum 0=FL,1=FR,2=RL,3=RR at byte 0) — verify layout per model.
- Make: vw (VW Group — Audi A4/A6/RS3, VW Amarok, VW Polo)
- Size: not documented (response ≥6 bytes; pressure field at byte 5)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown; fcm1 noted for the Polo variant)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]; TT layout variant [INFERRED]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.5 — seen on Audi A4/A6/RS3, VW Amarok, VW Polo, derived from OBDb v3 captures

## 0x18A1 — ECU 0x70B/0x775 (direct TPMS 65)
- Name: TirePressureFrontLeft
- Description: Direct-TPMS front-left tire pressure; value at payload byte 5: bar = F / 40
- Make: vw (VW Group — Audi A4/A6/RS3, VW Amarok, VW Polo)
- Size: not documented (response ≥6 bytes; pressure field at byte 5)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown; fcm1 noted for the Polo variant)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.5 — seen on Audi A4/A6/RS3, VW Amarok, VW Polo, derived from OBDb v3 captures

## 0x18A2 — ECU 0x70B/0x775 (direct TPMS 65)
- Name: TirePressureRearLeft
- Description: Direct-TPMS rear-left tire pressure; value at payload byte 5: bar = F / 40
- Make: vw (VW Group — Audi A4/A6/RS3, VW Amarok, VW Polo)
- Size: not documented (response ≥6 bytes; pressure field at byte 5)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown; fcm1 noted for the Polo variant)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.5 — seen on Audi A4/A6/RS3, VW Amarok, VW Polo, derived from OBDb v3 captures

## 0x18A3 — ECU 0x70B/0x775 (direct TPMS 65)
- Name: TirePressureRearRight
- Description: Direct-TPMS rear-right tire pressure; value at payload byte 5: bar = F / 40
- Make: vw (VW Group — Audi A4/A6/RS3, VW Amarok, VW Polo)
- Size: not documented (response ≥6 bytes; pressure field at byte 5)
- Session: not documented; source captures read it in default session (no 0x10 prerequisite shown; fcm1 noted for the Polo variant)
- Security: not documented; source performs read-only 0x22 polling, no 0x27 used
- Grade: [B]
- Evidence: miskibin/obd2-dashboard `docs/research-multibrand-extended-pids.md` §4.5 — seen on Audi A4/A6/RS3, VW Amarok, VW Polo, derived from OBDb v3 captures

## 0x7128 — ECU 18DA60F1/18DAF160 (body/ABS 0x60)
- Name: BodyAbsUnknown7128
- Description: Positive 0x22 response observed on ECU 0x60 ("Body/ABS (?)"); payload not decoded
- Make: honda (observed on Honda WN7 electric motorcycle, 2026 EU — not confirmed on Honda cars)
- Size: not documented
- Session: default session — source reads with `10 01` + `3E` TesterPresent keepalive; data readable without session elevation
- Security: none required (verified by source: no 0x27 SecurityAccess used for any data in the doc)
- Grade: [C]
- Evidence: cnc-lasercraft/honda-wn7-wican `docs/obd-protocol.md` — "Known ECUs" table lists 0x60 Body/ABS (?) with DIDs "7122, 7128, 712A (not decoded)"; values cross-checked against a passive capture of Honda's official MCS diagnostic tool. Single vehicle, single source.

## 0x712A — ECU 18DA60F1/18DAF160 (body/ABS 0x60)
- Name: BodyAbsUnknown712A
- Description: Positive 0x22 response observed on ECU 0x60 ("Body/ABS (?)"); payload not decoded
- Make: honda (observed on Honda WN7 electric motorcycle, 2026 EU — not confirmed on Honda cars)
- Size: not documented
- Session: default session — source reads with `10 01` + `3E` TesterPresent keepalive; data readable without session elevation
- Security: none required (verified by source: no 0x27 SecurityAccess used for any data in the doc)
- Grade: [C]
- Evidence: cnc-lasercraft/honda-wn7-wican `docs/obd-protocol.md` — "Known ECUs" table lists 0x60 Body/ABS (?) with DIDs "7122, 7128, 712A (not decoded)"; values cross-checked against a passive capture of Honda's official MCS diagnostic tool. Single vehicle, single source.

---

## Coverage notes (documented gaps — not entries)

**Honda SRS / airbag: no public UDS DIDs.** Honda SRS historically uses proprietary blink-code
diagnosis: bridge the SCS service connector and count SRS-lamp blinks (the ABS lamp works the same way;
honda-tech.com, civic5.com document the pin-bridging procedure for 1990s–2000s models). Honda-specific SRS
DTC formats (e.g., 11-1x driver airbag, 81-6x OPDS; NHTSA bulletin INSL-PE05043 documents SRS DTCs 15-1/15-2/15-3
for OPDS faults) are read via the SRS module, not as UDS 0x22 DIDs, and no B1xxx UDS DID data is published.
Grade of the blink-code claim: B (multiple independent community sources agree); the absence of public UDS
SRS DIDs is a negative result, not a proof of nonexistence.

**Honda MICU / door multiplex units: no public UDS DIDs found.** Honda's body multiplex control is
documented only through HDS data lists and B-/U-code DTCs, which are not published as 0x22 DID reads.

**Honda HVAC / climate: no public UDS DIDs found.** (Existing Honda 0x2613 ACRefrigerantPressure and
0x260A/0x260C/0x260D/0x2612/0x2613/0x261E–0x2622/0x263D HVAC-adjacent entries in the db are VW, not Honda.)

**Honda ABS/VSA: no additional DIDs beyond 0x4004/0x4005/0x4201 found.** Wheel speeds, steering angle,
and yaw data on Honda VSA (DA28) are not published as 0x22 DIDs in any source consulted.

**Honda unmapped targets 0E and 15.** The OBDb-derived Honda research (miskibin §12.1) lists Honda targets
`0E` and `15` as seen in captures but unmapped to any module — candidates for future probing, not entries.

**Honda Accord signalset not re-examined.** The existing Honda DIDs were imported from the Honda-Civic
and Honda-CR-V signalsets; the 1.3 KB Honda-Accord signalset may hold additional body DIDs.

**VAG BCM (09 / J519 central electrics): no public UDS DID list found.** Adaptation-vs-DID distinction:
on UDS-based VAG body modules, adaptation channels are accessed via 0x22/0x2E with DIDs (the IDE/ENG
channel names map to DIDs inside the module's ODX data), but no public DID↔IDE mapping for body modules
was found; on pre-2009 KWP2000 modules, adaptation uses KWP service 0x08 channels, which are not UDS DIDs
at all. Do not conflate the two. VCDS adaptation-channel documentation (IDE/ENG codes, e.g. MQB BCM
adaptations) is therefore not a DID source.

**VAG airbag (15 / J234): no public 0x22 DID list found.** VAG airbag modules report 5-digit fault codes
(e.g., 00952, 01314) that frequently have no verified P/B/C equivalents — flagged, not mapped. CAN pair
0x715/0x77F is documented (ODIS extraction, A6 C7) for the address, but no DID contents are public.

**VAG steering (44): no new public DIDs found** beyond existing 0x0346 (ID.4). **VAG HVAC (08): no new MQB
Climatronic UDS DIDs found** beyond the existing ID.4 0x26xx set.

**DID-number reuse across modules (do not treat as duplicates):**
- 0x2A0B exists in the db as HvBatteryPackTemperature (VW ID.4 BMS context, 16-bit signed /64 °C). The same
  number 0x2A0B is also served by the MQB 12 V battery monitor (IBS) with a different layout (A − 40 °C).
  The ECU address (0x710/0x77A vs the HV BMS pair) disambiguates — not entered as a new DID.
- 0x2A0E exists in the db as StartStopBatteryResistance from the ID.4 (raw × 0.2 mΩ). MQB captures show
  the same scaling on Golf/Tiguan (A × 20/100) but an incompatible SIGNED(A)/5 variant on Audi Q3 and some
  Jettas — a caution on the existing entry's scaling, not a new DID.

**0x710/0x77A platform meaning.** On MQB cars the 0x710/0x77A pair serves the battery monitor (J367/BDM,
a LIN slave surfaced through the gateway) — that is where the 0x2Axx entries above come from. On other
platforms (e.g., A6 C7 per the ODIS extraction) 0x710/0x77A is the gateway J533 itself. Same CAN pair,
different platform meaning — verify per platform.

**Evaluated and excluded:** iglooom/bcm_firmware_mod documents a 492-entry 0x22 DID table (DIDs 0x0202,
0x0329, 0x0631, 0x203E–0x2042, 0x40xx/0x41xx, 0xE203, …) reverse-engineered from firmware with bench
validation — but the target is a **Ford** BCM (tester 0x726/ECU 0x72E, "APP_body_cmd_bus", RKE context,
JV6T part numbers), out of scope for this Honda/VW task. alagrandeur/mk7-cluster-bench-controller cites
only powertrain DIDs (0x39C0 MAP, 0x202C coolant on the engine ECU) — no body additions.

---

## Sources consulted

1. miskibin/obd2-dashboard — `docs/research-multibrand-extended-pids.md` (2026-08-12; author's research
   notes; PID formulas mechanically derived from OBDb v3 `default.json` captures, CC BY-SA 4.0).
   Primary source for all 16 VW entries. https://github.com/miskibin/obd2-dashboard/blob/HEAD/docs/research-multibrand-extended-pids.md
2. cnc-lasercraft/honda-wn7-wican — `docs/obd-protocol.md` (2026-08; reverse-engineered on a 2026 Honda WN7,
   cross-checked against a passive capture of Honda's official MCS diagnostic tool). Source for 0x7128/0x712A
   and the Honda session/security behavior. https://github.com/cnc-lasercraft/honda-wn7-wican/blob/HEAD/docs/obd-protocol.md
3. OBDb org — obdb/acura-integra commit `8a60038` (2026-09): confirms the Honda family DID set
   (DA26 6001 TPMS, DA28 4004/4005 ABS, DA60 7022/7028/7029/7060 cluster) and module mapping; no new body
   DIDs beyond the db's existing ones. https://github.com/obdb/acura-integra/commit/8a6003853ffe38f6310a38ed98f28ff4caf2c3a0
4. dspl1236/vag-cp-docs — `technical/obd-tools-uds-protocol-esp32.md`: VAG UDS CAN-ID table extracted from
   ODIS via ConnorHowell/vag-uds-ids (community extraction, single source). Corroborates the module/CAN pairs
   used here (714/77E cluster, 710/77A gateway, 715/77F airbag, 70B/775 TPMS).
   https://github.com/dspl1236/vag-cp-docs/blob/HEAD/technical/obd-tools-uds-protocol-esp32.md
5. Ross-Tech — VCDS VW issues page: BCM = J519 = address 09 naming; 2000–2001 airbag controller
   (6Q0-909-605-A) scan hazard. https://www.ross-tech.com/vag-com/vw_issues.php
6. OBDeleven forum — VAG 5-digit fault-code examples (B10CD00, C10A700, B126113, B10051B etc.); basis for
   the "no verified P/B/C equivalents" flag. https://forum.obdeleven.com/thread/3176/fault-codes-mean
7. honda-tech.com, civic5.com — Honda ABS/SRS blink-code procedures via the SCS service connector.
   https://honda-tech.com/forums/honda-accord-1990-2002-2/obd-3382748/ · https://civic5.com/forum/topic/10324-abs-fault-codes-and-how-to-get-them/
8. NHTSA — Honda SRS service bulletin (SRS DTCs 15-1/15-2/15-3, OPDS). https://static.nhtsa.gov/odi/inv/2005/INSL-PE05043-23903.pdf
9. iglooom/bcm_firmware_mod — `docs/live_debug_uds.md`: 492-entry DID table on a Ford (not VAG) BCM;
   evaluated, excluded as out of scope. https://github.com/iglooom/bcm_firmware_mod/blob/HEAD/docs/live_debug_uds.md
10. alagrandeur/mk7-cluster-bench-controller — MQB cluster bench project; only powertrain DIDs cited,
    no body additions. https://github.com/alagrandeur/mk7-cluster-bench-controller
