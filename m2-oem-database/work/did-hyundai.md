# Hyundai / Kia — manufacturer-specific UDS Data Identifiers (service 0x22)

Research for the M2 OEM vehicle database v1.3. Manufacturer-specific DIDs only.
ISO-standard DIDs 0xF180–0xF19E are deliberately excluded (covered separately).
KWP2000 service 0x21 "local IDs" (2101/2102/…) used by older platforms are
out of scope but cross-referenced where the same DID number speaks 0x22 on
newer platforms.

Grade key: **A** = OEM service info; **B** = multi-source community agreement
or verified capture; **C** = single community source. Per-entry flags mark
which field of the grade an inference touches.

Research date: 2026-10-06.

## Conventions

- Request addressing is normal 11-bit physical: request `0x7Ex` → response `0x7Ex+8` on most ECUs (verified on BMS 0x7E4→0x7EC, CLU 0x7C6→0x7CE). canair's `B-index` counts the 3-byte response echo (`62 DID_hi DID_lo`), so **B04 = first data byte** (cross-verified against EVNotiPi's byte offsets for 0x0101 and 0xB002).
- `Session`: none of the sources used a non-default session (0x10) before these reads. `Security`: no source reported a seed/key (0x27) requirement for any read listed. Both are stated as "not documented" where the source does not explicitly confirm.
- Model applicability is per-entry. 2017 Ioniq EV data comes from canair's whole-day capture/reverse-engineering program (WiCAN community, 2026). Kona/Niro EV data comes from JejuSoul OBD-PIDs (Torque community, years of real-world use) and EVNotiPi (Kona EV, open source). Genesis shares the Hyundai/Kia platform and DIDs; Kia-specific evidence is noted per entry.
- Sizes marked "not documented" were never explicitly stated; "≥N bytes inferred" means the highest referenced byte index requires at least N.

---

## BMS (0x7E4 → 0x7EC) — Kona EV / Niro EV / Ioniq 5-era platforms

NOTE: on the 2017 Ioniq EV these same DID numbers (0101/0102/…) are served
over KWP2000 service 0x21 at the same address (canair BMS profile,
`id_protocol: KWP2000`). The 0x22 form below is for the UDS-speaking
Kona/Niro EV platform. Genesis EV models share this platform.

## 0x0101
- Name: BMS main telemetry block
- Description: Battery pack state: SOC (BMS + display), pack current, pack DC voltage, max/min cell temps, 4 module temps, inlet temp, aux battery voltage, charge/discharge power limits, cumulative charge/ discharge Ah and kWh, operating time, charge-port and relay status bits. Byte layout cross-verified byte-for-byte between two independent community sources (SOC at data byte 5 = e/2, signed current at bytes 11–12 = (K*256+L)/10 A, voltage at bytes 13–14 = (m*256+n)/10 V, max/min temps at bytes 15–16).
- Make: hyundai
- Size: not documented (EVNotiPi decodes 62 response bytes / 59 data bytes; JejuSoul references up to data byte 58; ≥61 bytes inferred)
- Session: default session (no 0x10 used by any source)
- Security: not documented (no seed/key reported)
- Grade: [B] multi-source community agreement (EVNotiPi Kona EV open-source decoder + JejuSoul Kona/Niro EV Torque PID set, years of use, byte layouts agree exactly)
- Evidence: EVNotiPi car/kona_ev.py fields + JejuSoul 003_Kona&Niro_EV_BMS.csv (65 PID rows); independent third corroboration claimed in cxalem/scainner RESEARCH.md (EVNotiPi vs OVMS byte offsets)

## 0x0102
- Name: BMS cell voltages 1–32
- Description: Cells 1–32, one byte each, value/50 = volts (JejuSoul) = ×0.02 V (EVNotiPi). Sources agree on layout exactly.
- Make: hyundai
- Size: not documented (~39 bytes inferred: 3 echo + 4 pad + 32 cell bytes)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

## 0x0103
- Name: BMS cell voltages 33–64
- Description: Cells 33–64, same 1-byte ×0.02 V encoding as 0x0102.
- Make: hyundai
- Size: not documented (~39 bytes inferred, same layout as 0x0102)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

## 0x0104
- Name: BMS cell voltages 65–96
- Description: Cells 65–96, same 1-byte ×0.02 V encoding. Cells 97–98 are in 0x0105, not here.
- Make: hyundai
- Size: not documented (~39 bytes inferred, same layout as 0x0102)
- Session: default session
- Security: not documented
- Grade: [B] multi-source community agreement (EVNotiPi + JejuSoul)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 004_Kona&Niro_EV_BMS_cell_data.csv

## 0x0105
- Name: BMS secondary block (SOH, deterioration, cells 97–98)
- Description: State of health ((z*256+aa)/10 %), minimum deterioration, max/min deterioration cell numbers, display SOC (af/2), battery heater 1/2 temps, airbag duty, cell voltage deviation, cells 97–98 (ai/aj, ×0.02).
- Make: hyundai
- Size: not documented (EVNotiPi decodes 46 bytes; JejuSoul references up to data byte 36; ≥38 bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] existence/size agreement; [C] some individual field decodings (EVNotiPi decodes SOH + display SOC only; heater-temp/deterioration decodings are JejuSoul-only)
- Evidence: EVNotiPi car/kona_ev.py + JejuSoul 003_Kona&Niro_EV_BMS.csv (17 PID rows)

---

## HVAC (0x7B3 → 0x7BB) — Kona/Niro EV + 2017 Ioniq EV

NOTE: byte layouts agree across platforms for 0x0100 (canair 2017 Ioniq EV
uses B-index; B11 = 6th data byte = Torque letter F; B12 = 7th data byte =
Torque letter G — identical to JejuSoul's Kona EV F/G formulas). Treat as
one DID with platform-shared encoding.

## 0x0100
- Name: HVAC temperature block
- Description: Outdoor temp (G/2−40 °C, 7th data byte), indoor/interior temp (F/2−40 °C, 6th data byte), heat-pump temp (13th data byte, /2−40), compressor duty and assorted status bytes. Verified fields: interior temp, ambient temp (canair); outdoor/indoor temps (JejuSoul).
- Make: hyundai
- Size: not documented (canair references up to B37 → ≥34 data bytes, ≥37 bytes inferred on 2017 Ioniq EV)
- Session: default session
- Security: not documented
- Grade: [B] description/size; [C] unverified trailing fields (canair marks compressor-duty and most bytes unverified)
- Evidence: canair ioniq-2017 hvac.yaml (active, whole-day capture program) + JejuSoul 002_Kona&Niro_EV_HVAC.csv

## 0x0102
- Name: HVAC heat-exchanger block
- Description: Heat exchanger temps ((B10/2)−40, (B11/2)−40), compressor on flag (B17, verified), compressor-on mirror (B18), hotside temp.
- Make: hyundai
- Size: not documented (references up to B19 → ≥16 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description (canair active; 2017 Ioniq EV); [C] most field encodings (only compressor-on verified)
- Evidence: canair ioniq-2017 hvac.yaml

## 0x01A0
- Name: HVAC control/status block
- Description: Driver/passenger set temps, HVAC on/off flags, cooling/ heating mode flags. canair notes "62 bytes. Primary HVAC control/status DID."
- Make: hyundai
- Size: 62 bytes (canair note)
- Session: default session
- Security: not documented
- Grade: [B] description/size; [C] field encodings (canair active, 2017 Ioniq EV; parameter-level detail not fully extracted in this pass)
- Evidence: canair ioniq-2017 hvac.yaml

---

## BCM (0x7A0 → 0x7A8) — 2017 Ioniq EV

NOTE: canair BCM responses are 13 bytes for the 0xB0xx family (10 data
bytes). The 0xC00B response is longer (≥25 bytes, multi-frame).

## 0xC00B
- Name: TPMS tyre pressures and temperatures
- Description: Four tyre pressures (B10, B14, B19, B23 / 72.52 = bar — kPa/psi convention), four tyre temperatures (B11, B15, B20, B25 − 50 °C). Kia Niro EV WiCAN PR#716 corroborated the temperature bytes.
- Make: hyundai
- Size: not documented (≥25 bytes inferred from B25; multi-frame, response_frames=4)
- Session: default session
- Security: not documented
- Grade: [B] multi-source (canair active+verified, 2017 Ioniq EV; OVMS Ioniq 5 poll table independently uses 22 C0 0B for pressures/temperatures per cxalem/scainner RESEARCH.md)
- Evidence: canair ioniq-2017 bcm.yaml + scainner RESEARCH.md citing OVMS

## 0xC002
- Name: TPMS sensor IDs
- Description: TPMS wheel-sensor IDs per OVMS Ioniq 5 poll table.
- Make: hyundai
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single second-hand citation (scainner RESEARCH.md citing OVMS `vehicle_hyundai_ioniq5`; OVMS source not directly read in this pass)
- Evidence: cxalem/scainner RESEARCH.md (Hyundai/Kia section)

## 0xB00E
- Name: BCM charge-port status
- Description: Charge-port-open bit (B10:5), confirmed via Kia Niro EV WiCAN PR#716. Multi-frame (response_frames=2).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [B] single-source but verified true + independent PR corroboration
- Evidence: canair ioniq-2017 bcm.yaml (active)

## 0xB004
- Name: BCM door-lock state
- Description: 13-byte response; B11:6 = door lock state (1=locked), confirmed via fob lock/unlock test.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB005
- Name: BCM unlock bits A
- Description: 13-byte response; B10 changes A0↔AC during fob lock/unlock (bits 2,3). Correlated with B004 lock state.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB006
- Name: BCM unlock bits B
- Description: 13-byte response; B12 changes 00↔04 during fob lock/unlock (bit 2). Correlated with B004/B005.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB003
- Name: BCM 12V battery sensing
- Description: 12V battery voltage (B10×0.08), second 12V sense (B28×0.08), plus B12.
- Make: hyundai
- Size: not documented (references up to B28 → ≥26 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB007
- Name: BCM preheat departure time
- Description: Preheat departure-time setting (draft, decode pending).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB00C
- Name: BCM preheat schedule days
- Description: Preheat schedule day bitmask (draft, decode pending).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB001
- Name: BCM unknown A
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB002
- Name: BCM unknown B
- Description: Answers; content not decoded (draft). NOTE: same DID number as the CLU odometer DID 0xB002 (different ECU, 0x7A0 vs 0x7C6) — DID numbers are ECU-scoped on this platform.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB008
- Name: BCM unknown C
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB009
- Name: BCM unknown D
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xB00A
- Name: BCM unknown E
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 bcm.yaml (draft)

## 0xC011
- Name: BCM 12V bus monitor
- Description: 13-byte response; B11/12.8 = 12V bus voltage, [B13:B14] = event counter; bytes 8–9 (ELM index) change rapidly — not static.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 bcm.yaml (draft)

---

## CLU — cluster (0x7C6 → 0x7CE)

## 0xB002
- Name: Odometer
- Description: 3-byte odometer in km at response offset 9–11 (canair [B12:B14]; EVNotiPi padding 9 + 3-byte field — identical). Total response 15 bytes. Verified across three independent community sources. Also carries an unverified byte at B11 (candidate CLU internal temp, (B11/2)−40).
- Make: hyundai
- Size: 15 bytes
- Session: default session
- Security: not documented
- Grade: [B] multi-source agreement (EVNotiPi Kona EV + JejuSoul Kona/Niro/Soul EV + canair 2017 Ioniq EV); [C] the B11 temp byte (canair inference — flagged)
- Evidence: EVNotiPi car/kona_ev.py (odo 3 bytes at offset 9, `optional`) + JejuSoul Kia_Soul_EV_Cluster_data.csv & Hyundai_Ioniq_EV_BMS_data.csv (Int24(g:h:i)) + canair ioniq-2017 clu.yaml (active)

## 0xB001
- Name: CLU unknown A
- Description: 13-byte response, all zeros when stationary; purpose unknown. Captured payload example: 62 B0 01 followed by 10 zero bytes.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 clu.yaml (draft)

## 0xB003
- Name: CLU unknown B
- Description: 13-byte response; B3=0x88, B7=0x01, rest zeros; purpose unknown. Captured payload example: 62 B0 03 88 00 00 00 01 00 00 00 00 00.
- Make: hyundai
- Size: 13 bytes (captured)
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 clu.yaml (draft)

---

## ESC/ABS (0x7D1) — 2017 Ioniq EV

## 0xC101
- Name: ESC vehicle and wheel speeds
- Description: Real vehicle speed (B12, km/h), 4 wheel speeds (B18–B21, km/h, r=+1.000 vs real speed in driving capture), gear selector (B14), steering angle ([B35:B36]−32768)/10 deg (verified via held-wheel + driving steer sweep vs EPS). Unverified: longitudinal accel candidate (S23−128), brake pressure (B44).
- Make: hyundai
- Size: not documented (references up to B44 → ≥42 data bytes, ≥45 bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified fields; [C] accel/brake-pressure fields (canair inference — flagged)
- Evidence: canair ioniq-2017 esc.yaml (active, 2026-07-22/26/30 driving captures)

## 0xC102
- Name: ESC unknown
- Description: Answers; content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 esc.yaml (draft)

---

## EPS/MDPS (0x7D4) — 2017 Ioniq EV

## 0x0101
- Name: EPS steering/speed block
- Description: 18-byte payload. Absolute steering angle (signed big-endian S9:B10, −(S9×256+B10)/10 deg — verified 2026-07-30, r=+1.000 vs ESC steering angle), EPS-side vehicle speed (B14, km/h, verified), speed band (B15), tail constant 0x1010 at B18/B19. Unverified: B05/B06/B07, B11, candidate torque at B12:S13 (LE signed 16-bit).
- Make: hyundai
- Size: 18 bytes data (21 bytes response inferred; canair states "18-byte payload")
- Session: default session (vehicle state READY required by canair profile)
- Security: not documented
- Grade: [B] description/verified fields; [C] torque and unresolved bytes (canair inference — flagged)
- Evidence: canair ioniq-2017 eps.yaml (active, 2026-07-22 driving capture + 2026-07-30 angle resolution)

## 0x0102
- Name: EPS unknown (static)
- Description: Static/constant response; content not decoded.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] single source, content unknown
- Evidence: canair ioniq-2017 eps.yaml (static)

---

## IGPM — integrated gateway/power module (0x770) — 2017 Ioniq EV

## 0xBC03
- Name: IGPM door/hood/lamp status
- Description: Door-open bits (B10: driver, passenger, RL, RR; trunk B10:7; hood B11:0), door-lock bits (B10:1, B10:3), DRL/tail/high/low beam (B12:2–5), seatbelt FL (B11:1), ACC2/IGN status bits, config byte B09. Most bits verified via timed event captures 2026-07-24.
- Make: hyundai
- Size: not documented (references up to B13 → ≥11 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified bits (canair active; Kia Niro EV WiCAN PR#716 corroboration on door bits); [C] unverified bits (flagged)
- Evidence: canair ioniq-2017 igpm.yaml (active)

## 0xBC04
- Name: IGPM door-lock status
- Description: Door-lock FL/FR bits plus B10 bit 0 field.
- Make: hyundai
- Size: not documented (references up to B10 → ≥8 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] single-source active, verified per canair
- Evidence: canair ioniq-2017 igpm.yaml (active)

## 0xBC06
- Name: IGPM brake/turn-signal status
- Description: Brake light (B10), left/right turn signals (B11:0, B11:1 — corrected 2026-08-09, user-confirmed), brake-pedal bits (B10:2, unverified).
- Make: hyundai
- Size: not documented (references up to B11 → ≥9 data bytes inferred)
- Session: default session
- Security: not documented
- Grade: [B] description/verified fields; [C] brake-pedal bits (flagged)
- Evidence: canair ioniq-2017 igpm.yaml (active)

## 0xBC01
- Name: IGPM unknown A
- Description: Static byte field B5; purpose unknown (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 igpm.yaml (draft)

## 0xBC05
- Name: IGPM unknown B
- Description: Static byte B5; unlock-flash bits (B10), trunk indicator (B11:3) partially decoded.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, partially decoded single source
- Evidence: canair ioniq-2017 igpm.yaml (draft)

## 0xBC07
- Name: IGPM charge-port lock status
- Description: Charge-port lock (B11:7), inverted copy (B12:0), ACC2-related (B12:3), IGPM wake latch (B12:2) — decoded, unverified.
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, decoded-but-unverified single source
- Evidence: canair ioniq-2017 igpm.yaml (draft)

---

## SCC / ADAS radar (0x7D0) — openpilot-era platforms

## 0xF100
- Name: ECU long description (firmware identification string)
- Description: Hyundai-proprietary firmware ID string used by openpilot/ opendbc for ECU fingerprinting. Captured format example (camera ECU): `AEE MFC  AT EUR LHD 1.00 1.00 95740-G2600 190730` — platform code, module name, region, HW/SW versions, part number, date code. Response to `22 F1 00` is `62 F1 00 <ascii>`. Same DID also read from EPS and ADAS ECUs (opendbc PLATFORM_CODE_ECUS = fwdRadar, fwdCamera, eps).
- Make: hyundai
- Size: variable ASCII, not documented (captured examples ~40–50 bytes of payload)
- Session: default session
- Security: not documented
- Grade: [B] verified captures in opendbc + defined read path in opendbc values.py/interface.py
- Evidence: opendbc clone car/hyundai/values.py (HYUNDAI_VERSION_REQUEST_LONG) + car/hyundai/fingerprints.py (real `62 F1 00` responses, e.g. MDPS C `56310G7300` variants)

## 0xF110
- Name: ECU alternate long description
- Description: Alternate firmware-description DID queried by opendbc when 0xF100 does not yield a platform code (HYUNDAI_VERSION_REQUEST_ALT).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] defined in opendbc code; no captured response found in the local clone's fingerprints
- Evidence: opendbc clone car/hyundai/values.py only

## 0x0142
- Name: SCC radar configuration (radar-points debug output)
- Description: Radar config register; openpilot community tooling reads and writes it via 0x22/0x2E to enable radar-track debug output on bus 1 for certain Hyundai radars. Persistent across reboots. Safety-relevant: community notes warn AEB/FCW behavior may be affected.
- Make: hyundai
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C] single community source family (openpilot HOW-TOS text, copied across sunnypilot/animalpilot forks — one origin)
- Evidence: openpilot HOW-TOS.md "Radar Tracks" (via kirito3481/sunnypilot, alexandresato/animalpilot, taik/twilsonco-openpilot mirrors)

## 0x0100
- Name: SCC unknown
- Description: Answers on SCC (0x7D0); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 scc.yaml (draft)

---

## ADAS camera / MFC (0x730) and parking ADAS (0x7B1)

The 0xF100/0xF110 firmware-identification DIDs are read here by opendbc
(see SCC section for full entries — same DIDs, same encoding):

## 0xF100
- Name: ECU long description (firmware identification string)
- Description: See full entry under SCC. opendbc reads it from the ADAS camera ECU (0x730) and parking ADAS ECU (0x7B1) for fingerprinting; 0x7B1 is also the address opendbc silences via 0x28 communication control on CAN-FD blinker platforms (interface.py).
- Make: hyundai
- Size: variable ASCII, not documented
- Session: default session
- Security: not documented
- Grade: [B] verified captures in opendbc
- Evidence: opendbc clone car/hyundai/values.py + fingerprints.py + interface.py (0x730/0x7B1 usage)

## 0xF110
- Name: ECU alternate long description
- Description: Alternate firmware-description DID (see SCC section).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] defined in opendbc code; no captured response in local clone
- Evidence: opendbc clone car/hyundai/values.py only

## 0x0100
- Name: MFC unknown
- Description: Answers on MFC/camera ECU (0x7C4 in canair ioniq-2017; 0x730 on openpilot-era ADAS platforms); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 mfc.yaml (draft)

---

## GSA (0x7B6) — 2017 Ioniq EV

## 0x0100
- Name: GSA unknown
- Description: Answers on GSA (0x7B6); content not decoded (draft).
- Make: hyundai
- Size: not documented
- Session: default session
- Security: not documented
- Grade: [C] draft, single source, content unknown
- Evidence: canair ioniq-2017 gsa.yaml (draft)

---

## Coverage notes

Verified ranges and systematic gaps:

1. **EV powertrain (0x7E2/0x7E3/0x7E5/0x7E6)** — the JejuSoul and canair
   sources show these ECUs (VCU, MCU, OBC/LDC, AAF) speaking KWP2000
   service **0x21** (LIDs 2100/2101/2102/2106) on Soul EV 27 kWh and 2017
   Ioniq EV. No 0x22 equivalents for VCU/MCU/OBC were found — on the
   UDS-speaking Kona/Niro platform only the BMS 0x01xx block is documented
   via 0x22. Motor/inverter, on-board charger, and DC-DC 0x22 DIDs are a
   gap.
2. **EMS/ECM, TCU, EPB, SRS, TPMS-module, BCM on ICE platforms** — no
   community 0x22 captures found for gasoline/diesel EMS or TCU. canair's
   ICE-relevant DIDs stop at the EV ECUs listed above. GDS/KDS technician
   documentation is not publicly available; no OEM service-info source
   was found for any entry (nothing here is Grade A).
3. **DID numbering is ECU-scoped, not global**: 0x0100 exists on HVAC,
   MFC, SCC, and GSA with unrelated content; 0x0101 exists on BMS, EPS,
   and HVAC-draft; 0xB002 exists on both BCM (unknown) and CLU (odometer).
   A DID number alone does not identify the data — always pair with the
   request address.
4. **0xF1xx identity block**: 0xF100/0xF110 are documented; no other
   manufacturer-specific F1xx DIDs (F101–F10F, F111–F17F) were verified.
   The 0xF18B manufacturing-date read used by opendbc is an ISO-standard
   DID and excluded per scope.
5. **Write access (0x2E)**: only 0x0142 (SCC radar) has a documented write
   path; no other 0x2E-writable DIDs verified.
6. **CAN-FD / E-GMP platforms (Ioniq 5/6, EV6, 2021+)**: canair's
   ioniq-5-2022 profile exists but only the CLU ECU file was populated;
   raw captures contain many 0x22 requests (e.g. 22 10 10, 22 51 00,
   22 1A xx families) that are not yet attributed to ECUs — a rich but
   unmined source. OVMS's Ioniq 5 poll table (cited second-hand) is the
   only E-GMP-specific confirmation (0xC002/0xC00B at 0x7A0).
7. **N-performance / ICE telemetry DIDs** (boost, knock, fuel-rail, DCT
   temps, eLSD) appear in an aftermarket app's roadmap as GDS-derived
   targets but no DID numbers were published — unverifiable, excluded.
8. **Kia vs Hyundai**: Kia evidence appears via Kia Niro EV WiCAN PRs and
   shared Kona/Niro EV PID files (same DIDs, same addresses). No
   Kia-only DID divergence was found; all entries apply to both makes
   unless noted. Genesis data is absent but platform-shared by design.
9. **Session/security**: every source performed these reads in the default
   session with no 0x27 unlock. Extended-session-only or secured DIDs
   (if any) are not represented here.
