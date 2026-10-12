# Stellantis UDS 0x22 DIDs — v1.4 harvest (new entries only)

New manufacturer-specific Stellantis (Jeep/Dodge/Chrysler/Ram/Fiat) service 0x22
DIDs harvested 2026-10-07. Deliberately excludes the three DIDs already in the
database (0x0122 BCM config block, 0xF010 BCM Tazer set, 0x0202 wiTECH datapoint)
and the ISO 0xF180–0xF19F range already covered as standard DIDs.

## 0xA010 — ECU 0x620/0x504 (BCM, Body Control Module)
- Name: CabinTemperature
- Description: Cabin temperature, 1 byte. Convert hex to decimal, subtract 54
  = degrees Fahrenheit (range −54°F to 201°F). Verified against the same formula
  on steering-wheel and ambient temp reads in the same thread.
- Make: stellantis
- Size: 1 byte
- Session: not required for reads — the working script sends `22 A0 10`
  directly with no 0x10 session entry
- Security: none required for read (observed)
- Grade: B
- Evidence: jlwranglerforums.com "JEEP HACKING CAN-C / CAN-IHS / UDS ! (Reverse
  Engineering)" thread — jmccorm Post #180 (Jan 2022) cabin-temp bash script
  (`cansend can1 620#0322A01000000000`, response grep `#100A62A010`); restated in
  the JL Wrangler CAN Bus Reference v2 PDF §7.4. CAN-C, TX 0x620 / RX 0x504.
  Applicability: JL Wrangler / JT Gladiator confirmed (2021 JLUR tested); may
  apply to other PowerNet (DT Ram, WK2) vehicles — INFERRED, not confirmed.

## 0xD01E — ECU 0x783/0x503 (HVAC module)
- Name: CabinTemperature
- Description: Cabin temperature reported by the HVAC module on CAN-IHS.
  Same scaling as 0xA010 (raw byte decimal − 54 = °F). Distinct from the BCM
  0xA010 read (different module, different bus). Thread notes it is unknown
  whether units can switch to Celsius or whether the reading depends on radio
  equipment level (8.4" uConnect vs base).
- Make: stellantis
- Size: not documented (script extracts a single byte)
- Session: not required for reads — script sends `22 D0 1E` directly with no
  0x10 session entry
- Security: none required for read (observed)
- Grade: B
- Evidence: same thread, page 13 — `cabintemp` script
  (`cansend can0 783#0322D01E00000000`, response grep `#100962D01E` on 0x503).
  CAN-IHS, TX 0x783 / RX 0x503. Applicability: JL Wrangler / JT Gladiator
  confirmed; wider PowerNet applicability INFERRED.

## 0x01AE — ECU 0x7E0/0x7E8 (PCM, Powertrain Control Module)
- Name: KnockRetard
- Description: Knock retard. Formula: value × 0.5 = degrees. Community notes
  knock retard is often 0 in normal highway driving.
- Make: stellantis
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: C
- Evidence: JL Wrangler CAN Bus Reference v2 PDF §7.6 ("PCM UDS Service 22
  PIDs — discovered by community members using specialized scan tools on the
  PCM (address 7E0)", thread page 50). Applicability: JL/JT PCM INFERRED beyond
  that report.

## 0x0227 — ECU 0x7E0/0x7E8 (PCM, Powertrain Control Module)
- Name: FuelRelatedPid
- Description: Fuel-related parameter, identity and scaling NOT decoded
  ("formula TBD from context"). Included as an existence datapoint only — do
  not treat as a decoded DID.
- Make: stellantis
- Size: not documented
- Session: not documented
- Security: not documented
- Grade: C
- Evidence: same as 0x01AE (v2 PDF §7.6, thread page 50).

## Session / security-access notes (applies to Stellantis reads generally)
- 0x22 READS on JL/JT PowerNet modules work in the default session with no
  0x10 entry and no 0x27 (evidence: the 0xA010 and 0xD01E scripts, Grade B).
- Extended session 0x10 0x03 (the JL thread also shows subfunction 0x92 used
  against the PCM) plus Tester Present 0x3E every ~250 ms is required for
  OUTPUT-control operations — e.g. the horn script enters 0x10 0x03 on BCM
  0x620 before 0x2F I/O control. UDS sessions auto-cancel when the keepalive
  stops (safety feature, not a bug). Grade B, thread + v2 PDF §7.1.
- 0x27 SECURITY ACCESS: no public community documentation of a working
  seed/key exchange for JL/JT BCM or PCM exists. Treat as "required for
  protected writes, algorithm proprietary/undocumented." 2018+ vehicles add the
  Secure Gateway (SGW): writes are blocked and reads of many enhanced DIDs are
  gated — legitimate paths are AutoAuth credential, wiTECH 2.0, or a physical
  bypass; the third-party-tool workaround is removing/replacing the SGW (per
  the jlwranglerforums "FCA Security Bypass" thread). NEVER invent seed/key
  algorithms or bypass procedures.
- DTC clear (0x14) sequences observed on module addresses 0x740/0x743/0x747/
  0x749/0x74B/0x762 in the thread (dstevens) — non-0x22, listed for context only.

## Out-of-scope / adjacent datapoints (not 0x22 DIDs, documented for context)
- 0xD0AD on BCM (0x620): I/O-control identifier (service 0x2F), horn relay —
  ON = `05 2F D0 AD 03 01 00 00`, OFF = `05 2F D0 AD 03 00 00 00`, requires
  extended session. From the JL thread horn script. Not a 0x22 DID.
- 0xF18x family on JL/JT modules: standard ISO ECU-identification DIDs
  (part numbers) confirmed working on "most modules" via 0x22 (dstevens,
  thread #688). Already in the database as standard DIDs.

## Coverage notes (documented gaps — not fabricated)
- RADIO/INFOTAINMENT: no manufacturer-specific 0x22 DIDs found publicly. The
  uConnect radio responds on 0x53F to requests sent to 0x7BF (per the thread),
  and 0x2F/0x11 against it are discussed (radio reboot attempts), but no
  specific radio DIDs are published. Community evidence for what DIDs the
  radio answers to: none found.
- ABS: no ABS-specific 0x22 DIDs found publicly for any Stellantis model.
- WK2 GRAND CHEROKEE: no model-specific DID list found. WK2 is PowerNet-era,
  so some JL/JT DIDs may carry over — INFERRED, unverified, not claimed.
- DT RAM 1500: no DT-specific DID list found. AlfaOBD community threads discuss
  BCM config backups/writes extensively, but AlfaOBD reads config via its own
  functions and does not publish a DID-number table; no quotable DID numbers
  surfaced.
- AMBIENT / STEERING-WHEEL TEMPERATURE DIDs: the thread's temperature work
  verified the same raw−54=°F formula for ambient (×2) and steering-wheel
  temperatures and logged AUX-battery voltage, but the specific DIDs for those
  sensors are not identified in the published posts — only cabin 0xA010 (BCM)
  and 0xD01E (HVAC) are pinned down.
- PCM beyond 0x01AE/0x0227: no wider PCM DID table is published by the
  community; thread notes a member's scan tool found 0x01AE/0x0227, no more.
- BCM 0x0122–0x0149 / 0xF010–0xF013: sizes, encodings, and per-DID names remain
  undocumented (already in the database as grouped grade-C entries).
- KWP2000 (service 0x21 local IDs): older FCA modules (pre-PowerNet,
  e.g. early-2000s LH/JR, WK-gen) used KWP2000; no local-ID table found in
  public sources. No Stellantis 0x21 IDs are claimed here.
- CAN FD: all harvested DIDs are on JL/JT CAN-C (500 kbps) and CAN-IHS
  (125 kbps) — both CAN 2.0, in scope for M2 hardware. No harvested DID
  requires CAN FD.

## Sources consulted
- jlwranglerforums.com — "JEEP HACKING CAN-C / CAN-IHS / UDS ! (Reverse
  Engineering)" thread: pages 13 (cabintemp/0xD01E script), 29 (UDS primer,
  radio 0x7BF/0x53F), 30 (Tazer backup list — used only to confirm exclusion),
  page 42–43 posts (#688: 0xF18x part numbers; module addresses), and the
  v2 reference PDF (jl_wrangler_can_bus_reference_v2) §7.1–7.6
  (0xA010, 0x01AE, 0x0227, session/keepalive, horn 0x2F D0AD).
- jlwranglerforums.com — "Full OBD Scan tool and FCA Security Bypass Question"
  (SGW behavior; third-party bypass approach). Describes, does not instruct.
- github.com/rstellhorn/jeep-jl-powernet-scripts (consulted; Pi scripts cover
  CAN broadcasts and 0x11 radio reset — no additional 0x22 DID tables).
- ramforum.com / 5thgenrams.com AlfaOBD and BCM threads (consulted; confirm
  SGW-era VIN/BCM behavior, e.g. VIN not a writable value on 5th-gen Ram BCMs
  — no DID numbers published).
- kb.fcawitech.com FED WORLD REPORT (consulted; calibration part-number
  tables only — no usable DID traffic rows).
- jlwranglerforums.com Tazer JL Mini user guide (v11.0.6/v11.0.8 PDFs) and
  zautomotive Tazer threads (consulted; feature lists, marry/unmarry backup
  behavior — no DID numbers published by Z Automotive).
