# Nissan / Infiniti — manufacturer-specific diagnostic identifiers (0x21 local IDs)

> **Nissan CAN-era quirk (applies to every entry below):** Nissan's enhanced
> diagnostics are KWP2000-style, NOT pure UDS. The working sequence is
> **DiagnosticSessionControl `0x10 0xC0` followed by service `0x21`
> (readDataByLocalIdentifier)** with a **1-byte local ID**. Positive
> response is `0x61 <localID> <data…>`. On CAN-era ICE modules UDS service
> `0x22` is **rejected with NRC `0x12`** — verified live on a 2018
> Pathfinder R52 (ECM `0x7E0`/`0x7E8`, TCM `0x7E1`/`0x7E9`) [B], and
> independently corroborated by the Leaf TCU community app (session
> `02 10 C0`, reads `02 21 <id>`, writes `3B <id> …`) [B] and by the 370Z
> community (session `02 10 C0` to BCM `0x745` unlocks enhanced commands)
> [C]. ISO-standard DIDs (mode 0x01 PIDs, `0xF190` VIN, etc.) are NOT
> duplicated here — this file covers only Nissan/Infiniti-specific
> identifiers. Every identifier below is a **0x21 local ID unless stated
> otherwise**.

Addressing seen in captures (Nissan follows ISO 15765-4 physical addressing):
- ECM: request `0x7E0` → response `0x7E8`
- TCM/CVT: request `0x7E1` → response `0x7E9`
- Leaf TCU (ZE0/AZE0): request `0x746` → response `0x783` (EV-CAN)

---

## TCU — Nissan Leaf ZE0/AZE0 (Continental 2012 / Ficosa Gen2.5 profiles)

All reads are `02 21 <id>` after `02 10 C0`; writes are `3B <id> …`.
No security access required for reads. These are the local-ID field
definitions of a working open-source TCU configurator app tested against
real Leaf TCUs (TX `0x746` / RX `0x783`).

## 0x04
- Name: TcuActivation
- Description: TCU activation state; 0x21 local ID (not UDS 0x22). Non-zero = activated. Writable via 0x3B (activation write uses value 01 to activate, 00 to deactivate).
- Make: nissan
- Size: 1 byte
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required for reads; writes via service 0x3B (Ficosa profile adds session 0x10 0xFA + routines 0x31 0x1000/0x1001 before writes — routine contents not documented)
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (Continental 2012 and Ficosa Gen2.5 profiles); read command "02 21 04", activation write "3B 04 01/00"

## 0x09
- Name: TcuSignalLevel
- Description: TCU cellular signal data; 0x21 local ID (not UDS 0x22). App decodes first 3 bytes as antenna level, reception power, error rate; remaining bytes not documented. Read-only.
- Make: nissan
- Size: 20 bytes
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required (read-only field)
- Grade: [B] name/encoding; [C] meaning of bytes 3–19 (not documented)
- Evidence: open-source Leaf TCU configurator (both profiles); app renders byte 0/1/2 as ANT level, reception power, error rate

## 0x81
- Name: TcuVin
- Description: VIN stored in the TCU; 0x21 local ID (not UDS 0x22). App reads 19 bytes = 17-char VIN followed by a 2-byte big-endian checksum, and validates the checksum against a CRC of the VIN before display. Writable via "3B 81" with fresh checksum appended.
- Make: nissan
- Size: 17 bytes VIN + 2-byte checksum = 19 bytes on the wire
- Session: 0x10 0xC0 prerequisite; reads work with no security access
- Security: none required for reads
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (both profiles); VIN+CRC split and validation implemented in the app's adapter code

## 0x59
- Name: TcuDtcStatus
- Description: DTC read/clear function on the TCU. **Not** read via 0x21: the app reads it with service `0x19 0x02 0xFF` and clears with `0x14 0xFF 0xFF 0xFF`. Included because it lives in the same TCU local-ID/field namespace.
- Make: nissan
- Size: not documented (multi-frame, up to 4096-byte app buffer)
- Session: 0x10 0xC0 prerequisite
- Security: not documented
- Grade: [B] services used; [C] payload layout (not documented)
- Evidence: open-source Leaf TCU configurator (both profiles); clear command "14FFFFFF", read "031902FF"

## 0x03
- Name: TcuServicesFlags
- Description: Telematics service enable flags (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). 12 bytes; bytes 8–11 are 0/1 flags for SVTB, RLU, horn, remote start (in that order). Writable via "3B 03".
- Make: nissan
- Size: 12 bytes
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads; Ficosa writes add session 0x10 0xFA + routines 0x31 0x1000/0x1001
- Grade: [B]
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile); byte-8..11 flag positions used by the app's service switches

## 0x10
- Name: TcuApnDial (Continental 2012) / TcuApnName (Ficosa Gen2.5)
- Description: Cellular APN dial/name string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Same ID, different label per TCU supplier profile. Writable via "3B 10 01 <data>".
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name/size; [C] size (app buffer length, wire length assumed equal — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles; label differs by profile)

## 0x11
- Name: TcuApnUser (Continental 2012) / TcuDns1 (Ficosa Gen2.5)
- Description: APN username (Continental) / DNS1 (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile. Writable via "3B 11 01 <data>".
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x12
- Name: TcuApnPass (Continental 2012) / TcuDns2 (Ficosa Gen2.5)
- Description: APN password (Continental) / DNS2 (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile. Writable via "3B 12 01 <data>".
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x13
- Name: TcuApnName (Continental 2012) / TcuObsServerPort (Ficosa Gen2.5)
- Description: APN name (Continental) / OBS server port (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x14
- Name: TcuDns1 (Continental 2012) / TcuObsServerUrl (Ficosa Gen2.5)
- Description: DNS1 (Continental) / OBS server URL (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x15
- Name: TcuDns2 (Continental 2012) / TcuApnUser (Ficosa Gen2.5)
- Description: DNS2 (Continental) / APN username (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x16
- Name: TcuProxy (Continental 2012) / TcuApnPass (Ficosa Gen2.5)
- Description: Proxy (Continental) / APN password (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x17
- Name: TcuProxyPort (Continental 2012) / TcuTspApnUser (Ficosa Gen2.5)
- Description: Proxy port (Continental) / TSP APN username (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x18
- Name: TcuApnConnectionType (Continental 2012) / TcuTspApnPass (Ficosa Gen2.5)
- Description: APN connection type (Continental) / TSP APN password (Ficosa) string; 0x21 local ID (not UDS 0x22). ASCII, space-padded. Label differs by supplier profile.
- Make: nissan
- Size: 128 bytes (Continental); 32 bytes (Ficosa)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] sizes (app buffer lengths — flagged)
- Evidence: open-source Leaf TCU configurator (both profiles)

## 0x19
- Name: TcuServerHostname
- Description: Server hostname string (Continental 2012 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Continental 2012 profile only)

## 0x21
- Name: TcuSmsNumber
- Description: SMS number string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 20 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x22
- Name: TcuSmsNumberTsp
- Description: TSP SMS number string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 20 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x2C
- Name: TcuTspApnName
- Description: TSP APN name string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x2E
- Name: TcuTspDns1
- Description: TSP DNS1 string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 32 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x2F
- Name: TcuTspDns2
- Description: TSP DNS2 string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 32 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x30
- Name: TcuTspServerPort
- Description: TSP server port string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x31
- Name: TcuTspServerUrl
- Description: TSP server URL string (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). ASCII, space-padded.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] name; [C] size (app buffer length — flagged)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile)

## 0x32
- Name: TcuTspPki
- Description: TSP PKI data (Ficosa Gen2.5 profile); 0x21 local ID (not UDS 0x22). **Conflict in source: the same profile maps 0x32 to both "TSP PKI" and "TSP root CA"** — one of the two labels is wrong in the app source. Treat the ID as existing but the semantic as disputed.
- Make: nissan
- Size: 128 bytes (app field length)
- Session: 0x10 0xC0 prerequisite
- Security: none required for reads
- Grade: [B] ID exists/responds; [C] semantic (conflict — flagged, unresolved)
- Evidence: open-source Leaf TCU configurator (Ficosa Gen2.5 profile lists 0x32 twice with different labels)

---

## TCM — 2018 Nissan Pathfinder R52 (JATCO CVT), request 0x7E1 → response 0x7E9

Verified by a live 0x21 local-ID sweep (0x01–0x20) after `02 10 C0` on a
real 2018 Pathfinder. Positive response format `61 <lid> <data>`.

## 0x02
- Name: TcmUnknownStoredBlock02
- Description: TCM 0x21 local ID (not UDS 0x22) that returns a positive response. **Content is stored/static data, NOT a live CVT monitor** — it stayed byte-identical across a full 0–104 km/h driving capture (2026-07-04). Meaning, size, and encoding not documented.
- Make: nissan
- Size: not documented
- Session: 0x10 0xC0 prerequisite (verified: session opens on TCM, `61 02 …` returned)
- Security: none required for reads
- Grade: [B] existence/response verified; [C] everything else (not documented — flagged)
- Evidence: 2018 Pathfinder live-diagnostics project; 0x21 LID sweep 0x01–0x20 on TCM 0x7E1→0x7E9; driving capture proved data is static

## 0x04
- Name: TcmUnknownStoredBlock04
- Description: TCM 0x21 local ID (not UDS 0x22) that returns a positive response. **Content is stored/static data, NOT a live CVT monitor** — it stayed byte-identical across a full 0–104 km/h driving capture (2026-07-04). Meaning, size, and encoding not documented.
- Make: nissan
- Size: not documented
- Session: 0x10 0xC0 prerequisite (verified: session opens on TCM, `61 04 …` returned)
- Security: none required for reads
- Grade: [B] existence/response verified; [C] everything else (not documented — flagged)
- Evidence: 2018 Pathfinder live-diagnostics project; 0x21 LID sweep 0x01–0x20 on TCM 0x7E1→0x7E9; driving capture proved data is static

---

## ECM — 2018 Nissan Pathfinder R52 (VQ35DD), request 0x7E0 → response 0x7E8

The same project ran a 0x21 sweep of local IDs 0x01–0x20 on the ECM after
opening session `10 C0`. **No positive responses were documented for any
LID 0x01–0x20 on the ECM** (contrast: the TCM answered 0x02/0x04). The
project therefore relies on generic mode-0x01 PIDs for ECM data. UDS
`0x22` (attempted: VIN DID `0xF190`) was **rejected with NRC `0x12`**
even after session `10 C0` — verified live. No ECM-specific 0x21 local
ID could be verified; none is listed above. This is a verified
negative result, not an absence of data.

---

## Qashqai — single-source UDS DIDs (unconfirmed, model-dependent)

The Pathfinder project notes (from CONSULT-III research, not its own
capture) that fuel-rail-pressure DIDs were "confirmed on Nissan Qashqai"
via UDS `0x22` — but they did **not** verify on their car, and their car
rejects `0x22` outright. Treat as model-dependent.

## 0x2801
- Name: FuelRailPressureMeasured
- Description: Fuel rail pressure, measured value; **UDS 0x22 DID (not a 0x21 local ID)**. Units reported as 0.1 bar per LSB (big-endian u16). Only claimed for Qashqai; the 2018 Pathfinder rejected 0x22 with NRC 0x12, so do not assume it works elsewhere.
- Make: nissan
- Size: 2 bytes (u16, 0.1 bar/LSB)
- Session: 0x10 0xC0 was attempted on Pathfinder; Qashqai session requirement not documented
- Security: not documented (claimed: no security needed for 0x22 live-data reads)
- Grade: [C] (single community source, unconfirmed on the capture vehicle — flagged)
- Evidence: 2018 Pathfinder project's notes citing CONSULT-III research ("confirmed on Nissan Qashqai; UNCONFIRMED for VQ35DD")

## 0x2802
- Name: FuelRailPressureSetpoint
- Description: Fuel rail pressure, setpoint/commanded value; **UDS 0x22 DID (not a 0x21 local ID)**. Units reported as 0.1 bar per LSB (big-endian u16). Same Qashqai-only caveat as 0x2801.
- Make: nissan
- Size: 2 bytes (u16, 0.1 bar/LSB)
- Session: 0x10 0xC0 was attempted on Pathfinder; Qashqai session requirement not documented
- Security: not documented (claimed: no security needed for 0x22 live-data reads)
- Grade: [C] (single community source, unconfirmed on the capture vehicle — flagged)
- Evidence: 2018 Pathfinder project's notes citing CONSULT-III research ("confirmed on Nissan Qashqai; UNCONFIRMED for VQ35DD")

---

## Coverage notes

**Identifier ranges NOT verified:**
- ECM `0x21` local IDs above `0x20` on any Nissan — no public sweep found.
- TCM local IDs above `0x20` (only `0x01`–`0x20` swept on the Pathfinder).
- BCM / ABS / IPDM / airbag / other modules: no `0x21` sweep published. (The 370Z community documented session `10 C0` on BCM `0x745` plus KWP service `0x30` for commanding — e.g. `04 30 05 00 01 00 00 00` door lock/unlock — but no `0x21` local-ID reads.)
- Infiniti-specific modules: nothing found.
- Leaf battery/LBC (`0x7BB`) and VCM local IDs: no verified `0x21` ID list found (LeafSpy reads these but its request set is not publicly documented).
- Consult-I/DDL-era (pre-CAN) is out of scope per task.

**Systematic gaps:**
- No OEM (Nissan/Infiniti service-manual) source for local IDs is publicly available; everything here is community reverse-engineering. Nothing in this file reaches Grade A.
- Encodings: only the TCU string fields (ASCII) and the `0x81` VIN checksum layout are decoded. TCM `0x02`/`0x04` payloads are opaque.
- Newer modules are migrating OFF the `0x21` scheme: per the Leaf TCU community's migration report, the ZE1 AIVC v2.5 TCU (TX `0x7CA`/RX `0x7DA`) uses standard UDS — session `0x10 0x03`, `0x22` with 2-byte DIDs (`0xF190`, `0x4006`, …) and `0x2E` writes. So post-~2018 modules may answer `0x22` after all; the `0x21`/NRC-`0x12` behavior is model- and module-dependent, not a universal Nissan rule. Non-ISO DIDs on those newer modules (e.g. `0x4006`) are not documented anywhere found — open research.

**Conflicts reported (not silently resolved):**
1. Ficosa Gen2.5 profile maps local ID `0x32` to BOTH "TSP PKI" and "TSP root CA" — one label is wrong in the app source.
2. `0x22` acceptance is model-dependent: rejected with NRC `0x12` on the 2018 Pathfinder (verified capture) vs. claimed working on Qashqai for DIDs `0x2801`/`0x2802` (single source, unconfirmed).
3. TCU string-field sizes are the app's buffer lengths (`fieldLength`); wire payload length is assumed equal but not independently verified — flagged `[C]` on each.
4. TCM `0x02`/`0x04` look like plausible live-data IDs but a driving capture proved they are static stored data; do not log them as live CVT signals.
