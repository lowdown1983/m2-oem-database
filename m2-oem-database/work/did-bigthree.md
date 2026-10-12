# GM / Ford / Stellantis — manufacturer-specific UDS Data Identifiers (0x22)

Research for the M2 OEM vehicle database (v1.3). ISO-standard DIDs 0xF180–0xF19E
are covered by a separate agent and are NOT duplicated here.

Terminology notes (verified from the OEM specs themselves):
- GM GMLAN era: DIDs are read with service **$1A** (ReadDataByIdentifier) and are
  **1-byte** identifiers; service **$22** is ReadDataByParameterIdentifier (PIDs).
  On Global A (UDS), $22 reads 2-byte DIDs. GMW3110 §9.3.2.4.2 documents the $1A
  boot-software DIDs below. [A — GMW3110]
- Ford: service $22 is called **"Mode $22 / Request Parameter By PID"**; Ford's
  "PIDs" are what UDS calls DIDs. Identifiers below are written as Ford writes
  them ($D100 etc.). [A — Ford Global Diagnostic Specification Part One v2003.0]
- Stellantis: standard UDS $22 with 2-byte DIDs.

Every claim graded: A = OEM service info/standard · B = multi-source or verified
capture · C = single community source. Research date: 2026-10-06.

---

## GM (GMLAN-era $1A DIDs, from GMW3110)

## 0xB0
- Name: ECU Diagnostic Address
- Description: Returns the ECU's diagnostic address. Used by the tester (with DID $B0 table) to determine the relationship of each ECU's diagnostic address to its physical request/response CAN identifiers during setup of the base diagnostic configuration matrix. Required in boot software (except SPS_TYPE_C ECUs).
- Make: gm
- Size: not documented
- Session: boot software (SPS programming); operational-software availability not documented
- Security: boot-software pseudo code assumes the ECU is unlocked when operating out of boot software
- Grade: [A]
- Evidence: GMW3110 (GM Worldwide Engineering Standard, Feb 2010) §9.3.2.4.2, via pcmhacking.net mirror

## 0xCC
- Name: ECU Base Model Part Number (minimum set)
- Description: One of the minimum DIDs ($CC and $DC) required for determining the ECU base model part number, so a programming tool can select the correct file(s) for programming.
- Make: gm
- Size: not documented
- Session: boot software; operational-software availability not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## 0xDC
- Name: ECU Base Model Part Number (minimum set)
- Description: One of the minimum DIDs ($CC and $DC) required for determining the ECU base model part number, so a programming tool can select the correct file(s) for programming.
- Make: gm
- Size: not documented
- Session: boot software; operational-software availability not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## 0xCB
- Name: Software End Model Part Number
- Description: The boot software shall be capable of reporting the Software End Model part number via DID $CB.
- Make: gm
- Size: not documented
- Session: boot software; operational-software availability not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## 0x92
- Name: Optional DID (per CTS)
- Description: Support is optional; required only if specified in the ECU's CTS (or SSTS / supplemental diagnostic specification).
- Make: gm
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## 0xB4
- Name: Traceability Data
- Description: Traceability data DID; support may be required based on regional practices, specified in the CTS if needed.
- Make: gm
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## 0xB5
- Name: Broadcast Code
- Description: Broadcast Code DID; support may be required based on regional practices, specified in the CTS if needed.
- Make: gm
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

## SWMI / SWMIAC
- Name: Software Module Identifier / Software Module Identifier Alpha Code
- Description: The boot software shall report the SWMI and SWMIAC DIDs for the operational software module(s) once programmed (and per calibration module, if the utility file allows individual calibration programming). Numeric DID values are per-ECU (CTS), not fixed in the standard.
- Make: gm
- Size: not documented
- Session: boot software; operational-software availability not documented
- Security: not documented
- Grade: [A]
- Evidence: GMW3110 §9.3.2.4.2, via pcmhacking.net mirror

---

## Ford (Mode $22 PIDs, from Ford Global Diagnostic Specification)

All below are "mandatory supported PIDs" per Table 16.3 of the Ford Global
Diagnostic Specification Part One v2003.0 (Ford Motor Company, R&VT/EESE).
[A] throughout this section.

## 0xD100
- Name: ECU Operating State / Mode
- Description: Contains the ECU's current operating state/mode as a 1-byte state-encoded value. Supported by ALL Ford ECUs. Values: $01 = Operational State; $02 = Diagnostic State; $03 = On-Demand Self-Test / Execution Routine State; $07 = Information Transfer State; $09 = No Stored Codes Logging State; $0A = Input Integrity Test State; $0B = Secure Diagnostic State; $0D = Manufacturer State.
- Make: ford
- Size: 1 byte (SED — state encoded)
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.3 / Table 16.4, via Caltech archive

## 0x0200
- Name: Number of Continuous DTCs
- Description: Number of continuous DTCs currently stored by the ECU. NUM encoding, 1 byte.
- Make: ford
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.1 / Table 16.3, via Caltech archive

## 0x0202
- Name: Number of DTCs from most recent test
- Description: Number of on-demand DTCs generated during the most recent diagnostic test executed by the ECU. NUM encoding, 1 byte.
- Make: ford
- Size: 1 byte
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.2 / Table 16.3, via Caltech archive

## 0xE200
- Name: Software Version Number
- Description: ECU software revision level and release date. PKT encoding, 3 bytes: Byte 1 = revision level (bits 7-4) + month high bits; Bytes carry month ($1=January … $C=December), day of month ($01-$1F), year ($00 = 1900, $64 = 2000, $FF = 2155).
- Make: ford
- Size: 3 bytes
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.4 / Table 16.5, via Caltech archive

## 0xE217
- Name: Part Number Identification Base
- Description: Control module base part number "group" and "detail" info. PKT encoding, 4 bytes; supports the worldwide FAO part-number identification system. Example: airbag module base 14B056 and ABS module 2M110 encodings are worked in the spec.
- Make: ford
- Size: 4 bytes
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.5 / Table 16.6, via Caltech archive

## 0xE219
- Name: Part Number Identification Suffix
- Description: ECU basic design code, alternate part code, and change (revision) level. 2 bytes, bit-field encoded per Table 16.8 (refer to MRDB for the full value list).
- Make: ford
- Size: 2 bytes
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.7 / Table 16.8, via Caltech archive

## 0xE21A
- Name: Part Number Identification Prefix
- Description: Year/decade, product line, and design responsibility as 4 ASCII bytes (Byte 1 = year/decade, Bytes 2-3 = product line, Byte 4 = design responsibility). Replaces PID $E218 for MY1999+ programs. Example: fuel pump control module for Jaguar X200 (Electrical & Fuel Handling Division) = "1R8U" ($31 $52 $38 $55).
- Make: ford
- Size: 4 bytes (ASCII)
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.7.6 / Table 16.7, via Caltech archive

## 0xE221-0xE226
- Name: Module Serial Number (ASCII)
- Description: ECU serial number in ASCII, 4 bytes per PID; implement only as many as needed. $E221 byte 1 always holds the most significant digit; pad with $00 if the serial is not a multiple of 4 chars. Example: serial 12345678901 → $E221 = 31 32 33 34 ("1234"), $E222 = 35 36 37 38, $E223 = 39 30 31 00.
- Make: ford
- Size: 4 bytes each (ASC)
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.8.1 / Table 16.9, via Caltech archive

## 0xE231-0xE236
- Name: Module Serial Number (BCD)
- Description: ECU serial number in BCD, 4 bytes per PID; $E231 byte 1 high nibble holds the most significant digit; pad with $F if not a multiple of 8 digits.
- Make: ford
- Size: 4 bytes each (BCD)
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.8.1 / Table 16.9, via Caltech archive

## 0xE300-0xE307
- Name: Vehicle Identification Number
- Description: VIN in ASCII, 4 bytes per PID (17-char VIN spans the range).
- Make: ford
- Size: 4 bytes each (ASC)
- Session: not documented
- Security: not documented
- Grade: [A]
- Evidence: Ford Global Diagnostic Specification Part One v2003.0 §16.8.1 / Table 16.9, via Caltech archive

## 0xDE00-0xDEFF
- Name: As-built configuration block N
- Description: As-built block N of a module corresponds to DID 0xDE00 + (N-1). Measured, not assumed: on a 2019 F-250 every checked block matched the live 0x22 read byte-for-byte, including BCM block 726-09 against DID 0xDE08, which decoded to the ASCII VIN prefix "1FT7W2" of that vehicle. This bridges community as-built documentation ("set 726-15-01") to UDS reads. Size is block-dependent (as-built lines carry 5 data bytes + checksum).
- Make: ford
- Size: block-dependent (not fixed)
- Session: reads verified in normal diagnostic operation; writes require security access / extended license per FORScan community
- Security: reads open (verified); writes gated
- Grade: [B]
- Evidence: christianorona/wtfault-scanner (GitHub) — measured on 2019 F-250; corroborated by FORScan as-built block convention (7D0/720/726/7E0 module prefixes)

---

## Ford BCM bench-verified DIDs (iglooom BCM_Firmware_Mod)

Context: reverse-engineering project against a Ford BCM (part JV6T-14C094-AD).
The application's 0x22 DID table holds 492 identifiers in families 0xEExx (129),
0xFDxx (101), 0x40-42xx (117), 0xF1xx (29), 0xC0/C1xx (27), 0x28xx (22, incl.
as-built configuration). The DIDs below were verified SERVED on the bench with
plain `22 <hi> <lo>` (tester 0x726 → ECU 0x72E), each returning exactly 1 byte,
in the DEFAULT session with NO 0x27 security. OEM functional names for these
DIDs are not documented — descriptions below are the project's observed roles.

## 0x0631
- Name: (bench probe — positive control)
- Description: Bench-verified readable; 1-byte response; OEM idle value 00. Used by the project as the positive control (tracks APP_lock_command, visible on the bus). OEM functional name not documented.
- Make: ford
- Size: 1 byte (verified on the wire)
- Session: default session (verified)
- Security: none required (verified — no 0x27)
- Grade: [B]
- Evidence: iglooom/bcm_firmware_mod docs/live_debug_uds.md — bench-verified 0x22 reads on Ford BCM JV6T-14C094-AD

## 0x412E
- Name: (bench probe)
- Description: Bench-verified SERVED, 1-byte response, OEM idle value 86. (Replaced 0x406B in the probe bank after 0x406B returned NRC 0x31 requestOutOfRange — present in the DID table but not served by the application.) OEM functional name not documented.
- Make: ford
- Size: 1 byte (verified on the wire)
- Session: default session (verified)
- Security: none required (verified — no 0x27)
- Grade: [B]
- Evidence: iglooom/bcm_firmware_mod docs/live_debug_uds.md — bench-verified 0x22 reads on Ford BCM JV6T-14C094-AD

---

## Stellantis (UDS $22, community captures)

## 0x0122-0x0149
- Name: BCM configuration DIDs (JL Wrangler)
- Description: Block of BCM configuration DIDs (0x0122–0x0127, 0x0130–0x0149) that the Tazer JL programmer utility reads via UDS 0x22 and backs up to a text file — i.e. these are the configuration bits the Tazer cares about in the BCM. Sizes/encodings not documented. (Note: there are more DIDs in the BCM than these; this is the Tazer backup set, not a full table.)
- Make: stellantis
- Size: not documented
- Session: not documented
- Security: reads observed working (Tazer backup); SGW-era vehicles may gate reads behind bypass/AutoAuth per the database's SGW findings
- Grade: [C]
- Evidence: jlwranglerforums.com "JEEP HACKING CAN-C / CAN-IHS / UDS" reverse-engineering thread — forum member documented the Tazer utility's 0x22 backup DID list

## 0xF010-0xF013
- Name: BCM DIDs (JL Wrangler, Tazer backup set)
- Description: Additional BCM DIDs (0xF010–0xF013) in the same Tazer utility 0x22 backup set as 0x0122–0x0149. Sizes/encodings not documented.
- Make: stellantis
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: jlwranglerforums.com "JEEP HACKING CAN-C / CAN-IHS / UDS" reverse-engineering thread — same Tazer backup DID list

## 0x0202
- Name: (observed in FCA wiTECH traffic)
- Description: A `22 02 02` request with `62 02 02` response appears in FCA wiTECH "FED WORLD REPORT" BCM traffic (2016 Fiat 500X BCM rows). Function not documented — included as an existence datapoint only, not a decoded DID.
- Make: stellantis
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: [C]
- Evidence: FCA wiTECH FED WORLD REPORT (kb.fcawitech.com) — 22 02 02 / 62 02 02 request/response visible in BCM traffic table

---

## Coverage notes

- GM Global A UDS-era (2-byte, $22) manufacturer DIDs: no verified community DID list found in this pass. The GMW3110 $1A DIDs above are GMLAN-era; Global A modules use UDS $22, and their make-specific DIDs (beyond ISO 0xF180–0xF19E, covered separately) were not published in any source found. [gap]
- GM SWMI/SWMIAC numeric DID values are per-ECU (CTS), not in the standard. [gap]
- Ford UDS-era (post-2008) 2-byte DID tables beyond the as-built 0xDE00 mapping were not found published; FORScan's knowledge lives in the app. The pre-CAN-era Ford spec PIDs above remain the documented baseline. [gap]
- Stellantis: AlfaOBD/JScan DID tables are in-app, not published; only the Tazer-observed BCM backup set and the wiTECH traffic datapoint were verifiable. No verified Stellantis DID sizes/encodings found. [gap]
- The iglooom Ford BCM DID table (492 entries) is firmware-derived; OEM names for individual DIDs are unknown, so only the bench-verified-readable examples are listed. [stated limit]
- No seed/key or security-bypass material was sought or reproduced; security fields above report only what sources state about read gating. [policy]
