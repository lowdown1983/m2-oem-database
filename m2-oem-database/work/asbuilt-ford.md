# Ford As-Built Data Format — v1.3 platform depth

Research for the M2 OEM vehicle database (v1.3 expansion). Covers the FORMAT
and well-known module addresses/blocks only — no specific vehicle's data is
reproduced here (no VIN was available and none is needed for the format).
Every factual claim carries a quality grade: **A** = Ford service info /
official Ford source · **B** = FORScan community consensus (multiple
independent sources agree) · **C** = single forum thread or unverified.
Conflicts are reported, not silently resolved.

Research date: 2026-10-06.

---

## 1. What as-built data is

- As-built data is the per-module configuration record Ford assigns at the
  factory: "the code engineers enter into a module to make it work right.
  Each module has a set of characters that must be entered in a unique order
  to configure it to a particular vehicle" — and the term comes from it being
  "the code used when the module was installed on the factory assembly line"
  [B — fenderbender trade press].
- Ford publishes the factory record per VIN through the official
  Motorcraft portal at motorcraftservice.com/AsBuilt (choose
  country/language first so the cookie is set, then the link works)
  [B — Ford's own portal, via fordownersclub/forscan.org forum guidance].
- Important nuance [B — fenderbender]: the portal's data reflects the
  *latest* calibration Ford has for that VIN, not a frozen factory image —
  "when you enter As-Built data into a module today that happened to have
  been built many years ago, any updates that have occurred since are
  included in today's As-Built data code."
- On the Motorcraft portal the body module is labeled **"BCE Modules"**;
  in FORScan the same module is **BCM/BdyCM** — "BdyCM (As Built) is BCM
  (FORScan)" [C — single fordownersclub thread].
- As-built data is what a dealer (IDS) or FORScan loads into a replacement
  module during PMI (Programmable Module Installation) so it matches the
  vehicle [B — fenderbender].

## 2. Format specification

### 2.1 Address structure

- Every as-built line is addressed as **MODULE-BLOCK-LINE**, e.g.
  `7D0-01-01`. The first three hex digits are the module's diagnostic
  address; the next two groups are the configuration block and the line
  within that block [B — FORScan tutorial: "the first 3 digits of an
  address denotes the module… Every address in BdyCM will begin with 726,
  every address in IPC will begin with 720, and every address in APIM will
  begin with 7D0"].
- Data follows as space-separated groups of 4 hex digits, e.g.
  `726-48-02 0100 0000 0078`. The trailing group of the line carries the
  **checksum** [B — F150 forum code sheet; FORScan tutorial].
- Lines have variable length: "some addresses may contain up to 10 values
  and others only 2 values" [B — FORScan tutorial].

### 2.2 Checksum

- The checksum is "a mathematical sum of all the prior hex digits" in the
  line [B — FORScan tutorial]. FORScan computes it automatically on write;
  the user does not need to calculate it.
- Community spreadsheets mark the checksum position with `zz` and data
  positions with `x` (don't-care / keep existing value), e.g.
  `726-41-02 xxx0 xxxx xxxx` means "change only the 4th hex digit of the
  first group to 0" [B — F150 community code sheets].
- When hand-entering data (e.g. VIN coding), the checksum field can be
  filled with `00` as a placeholder; FORScan regenerates the real checksum
  on write [B — FG-Falcon VIN-coding guide].

### 2.3 As-built vs "as configured" (FORScan easy mode)

- FORScan offers two views of the same module configuration: plain-English
  "Module Configuration" and "Module Configuration (AS BUILT format)".
  "They both do the same thing… You can use whichever" [B — fordownersclub].
  "Easy" mode edits the same underlying as-built bytes with less risk of
  transcription errors, "if Forscan has the correct values. Sometimes it
  could be wrong and you would need to go the manual way to fix it"
  [B — f150gen14].
- Practical consequence: ~90% of common feature toggles are reachable in
  easy mode without touching hex; the spreadsheet/as-built path is for
  features FORScan hasn't mapped to plain English [C — f150gen14].

## 3. Module address catalog

Addresses below are the 3-digit hex prefixes used in as-built lines AND the
module's UDS physical request ID on the diagnostic CAN (Ford +8 convention:
request 7D0 → response 7D8, etc. [B — community UDS research]). Unless
noted, addresses are consistent across 2011–2023 model years per the
FORScan community module listings.

## 701
- Module: Global Positioning Sensor Module (GPSM)
- Blocks: documented lines not verified in this pass
- Notes: Deprecated module; replaced by SYNC 3 and the new GPS antenna. No longer used.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing (scribd)

## 706
- Module: Image Processing Module A (IPMA) — forward driving assist, lane keeping/departure warning (Gentex or Mobileye)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings (multiple)

## 712
- Module: Seat Control Module G (SCMG) — driver lumbar and massage control
- Blocks: 09-02, 10-01, 10-02 documented in Explorer spreadsheet
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 713
- Module: Seat Control Module H (SCMH) — passenger lumbar and massage control
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 714
- Module: Heated Steering Wheel Module (HSWM)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan setup guide module table

## 716
- Module: Gateway Module A (GWM)
- Blocks: no configurable as-built data (per Explorer listing)
- Notes: Gateway itself carries no user-configurable as-built lines.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 720
- Module: Instrument Panel Cluster (IPC)
- Blocks: 01-01 through 07-01 documented in F150 community sheets (e.g. 720-01-01, 720-01-02, 720-01-03, 720-04-01, 720-07-01)
- Notes: Cluster configuration: chimes, displayed temps, trailer-brake gain display, quick-boot. See §4 for well-known blocks.
- Grade: [B]
- Evidence: FORScan community module listings + F150 code spreadsheets

## 721
- Module: Vehicle Dynamics Module (VDM)
- Blocks: documented lines not verified in this pass
- Notes: 2020MY+ only.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 724
- Module: Steering Column Control Module (SCCM) — steering wheel adjustments, switches, turn signals
- Blocks: 01-01 documented (turn-signal flash count)
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings + F150 code sheets

## 725
- Module: Wireless Accessory Charging Module (WACM)
- Blocks: documented lines not verified in this pass
- Notes: 2020MY+ only.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 726
- Module: Body Control Module (BCM / BdyCM; "BCE" on the Motorcraft portal)
- Blocks: extensive — 01-01 through 48-02 documented in community sheets (e.g. 726-01-01, 726-01-02, 726-08-01, 726-17-01, 726-21-01, 726-25-02, 726-28-02, 726-30-01, 726-37-01, 726-41-02, 726-42-01, 726-48-02)
- Notes: The most-modified module in the FORScan community. VIN stored at 726-09-01 through 726-11-01 (16-19MY). See §4 for well-known blocks.
- Grade: [B]
- Evidence: FORScan community module listings + F150/Super Duty code spreadsheets

## 727
- Module: Audio Control Module (ACM) — radio module / CD player, Sirius
- Blocks: 01-01, 01-02 documented (subwoofer, line-level preamp outputs)
- Notes: MS-CAN module on many platforms.
- Grade: [B]
- Evidence: FORScan community module listings + F150 code sheets

## 730
- Module: Power Steering Control Module (PSCM) — Nexteer unit on 2017MY+
- Blocks: documented lines not verified in this pass
- Notes: Contains a wheel-size field. Listed without address in the FORScan setup-guide table; address confirmed in the Explorer 11-23MY listing.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 731
- Module: Remote Function Actuator (RFA)
- Blocks: documented lines not verified in this pass
- Notes: 2011-2015MY only.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 732
- Module: Gear Shift Module (GSM)
- Blocks: documented lines not verified in this pass
- Notes: 2020MY-23MY only.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 733
- Module: HVAC — Heating, Ventilation, Air Conditioning
- Blocks: 02-01 through 02-04 store the VIN (16-19MY)
- Notes: Address 733 was EATC (Electronic Automatic Temperature Control) on 2011-2015MY — same address, renamed module. VIN stored at 733-02-01 through 733-02-04.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 736
- Module: Parking Assist Control Module (PAM)
- Blocks: 04-01 documented (perpendicular park enable)
- Notes: As-built change recommended for SYNC 2 → SYNC 3 upgrades.
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing + F150 code sheets

## 737
- Module: Restraint Control Module (RCM) — airbags, seatbelts
- Blocks: 01-01 through 01-04 store the VIN
- Notes: Contains seat/seatbelt configuration data. RCM as-built also appears on the Motorcraft portal (737-01-01 example lines).
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing; fordownersclub

## 740
- Module: Driver Door Module (DDM)
- Blocks: 03-01, 05-01, 12-01, 13-01 documented (mirror autofold, global windows)
- Notes: —
- Grade: [B]
- Evidence: FORScan tutorial + F150 code sheets

## 741
- Module: Passenger Door Module (PDM)
- Blocks: 03-01, 05-01, 12-01 documented (mirror autofold, global windows)
- Notes: —
- Grade: [B]
- Evidence: FORScan tutorial + F150 code sheets

## 744
- Module: Driver Seat Module (DSM)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [C]
- Evidence: Explorer 11-23MY FORScan module listing (single source)

## 751
- Module: Radio Transceiver Module (RTM) — also listed as tire-pressure monitor receiver in some sources
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 757
- Module: Trailer Brake Control Module (TBM / TBC)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 760
- Module: Anti-Lock Brake System (ABS)
- Blocks: 01-01 through 01-04 store the VIN; 03-01 documented (hill descent control)
- Notes: 2011-2015 Explorer/Police Utility lists show ABS at 76D — address is model-year/platform dependent; 760 is the current address [conflict reported, resolved by recency].
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing + F150 code sheets

## 761
- Module: Transfer Case Control Module (TCCM)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 764
- Module: Cruise Control Module (CCM)
- Blocks: 02-01 through 02-04 store the VIN
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 766
- Module: Running Board Control Module (RBM)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 776
- Module: Seat Control Module E (SCME)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [C]
- Evidence: Explorer 11-23MY FORScan module listing (single source)

## 783
- Module: Audio Digital Signal Processing Module (DSP)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 791
- Module: Trailer Module (TRM)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 7A5
- Module: Front Control/Display Interface Module (FCDIM)
- Blocks: documented lines not verified in this pass
- Notes: Some modules in this family (FDIM) require UDS 0x27 Security Access to modify VIN in as-built data [B — FG-Falcon VIN guide].
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing; FG-Falcon guide

## 7A7
- Module: Front Controls Interface Module (FCIM)
- Blocks: 02-01 through 02-04 store the VIN
- Notes: 2011-2015 Explorer/Police Utility lists show FCIM at 75A — address is model-year/platform dependent; 7A7 is the current address [conflict reported, resolved by recency].
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 7B1
- Module: Image Processing Module B (IPMB) — reverse camera module
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: FORScan community module listings

## 7B2
- Module: Heads-Up Display (HUD)
- Blocks: no configurable as-built data (per Explorer listing)
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 7C4
- Module: Side Obstacle Detection Control Module, Left (SODL)
- Blocks: 07-01 through 07-04 store the VIN
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 7C6
- Module: Side Obstacle Detection Control Module, Right (SODR)
- Blocks: 07-01 through 07-04 store the VIN
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 7D0
- Module: Accessory Protocol Interface Module (APIM) — SYNC module
- Blocks: 01-01 through 09-02 documented in community sheets (e.g. 7D0-01-01, 7D0-01-02, 7D0-02-01, 7D0-03-01, 7D0-04-02, 7D0-09-02)
- Notes: The SYNC configuration hub: audio sources, DSP, camera, themes, nav-in-motion. Block 8-9 not available on SYNC 3.0 [C — scribd Explorer guide]. See §4.
- Grade: [B]
- Evidence: FORScan community module listings + F150/Super Duty/Explorer code spreadsheets

## 7D5
- Module: Digital Audio Control Module C (DACMC)
- Blocks: documented lines not verified in this pass
- Notes: —
- Grade: [B]
- Evidence: Explorer 11-23MY FORScan module listing

## 7D7
- Module: GSM alternate — NOT VERIFIED. The brief listed 7D7 as a candidate address, but no source in this pass confirms a module at 7D7; the Explorer 11-23MY listing places the Gear Shift Module at 732 (2020MY+). Treat 7D7 as unverified [?].
- Blocks: —
- Notes: Do not use without on-vehicle verification.
- Grade: [C]
- Evidence: none found — flagged unverified

## 7E0
- Module: Powertrain Control Module (PCM)
- Blocks: Motorcraft portal lists PCM blocks 1-9 (e.g. PCM 1..9 lines)
- Notes: Primary powertrain module; UDS request ID 7E0 → response 7E8 (+8 convention).
- Grade: [B]
- Evidence: FORScan community module listings; Motorcraft AsBuilt portal sample

## 7E1
- Module: Transmission Control Module (TCM)
- Blocks: documented lines not verified in this pass
- Notes: Address confirmed by two independent FORScan community sources; one setup-guide copy truncates it as "70" (transcription artifact, not a distinct address) [conflict reported, resolved].
- Grade: [B]
- Evidence: Super Duty FORScan codes guide; fordownersclub module list

---

## 4. Well-known blocks (general purposes)

Bit/field meanings inside these blocks are MODEL- AND YEAR-SPECIFIC. The
purposes below are the block's general domain per the FORScan community;
never apply one model year's bit map to another without verifying against
that vehicle's spreadsheet.

- **720-01-01 (IPC)** — cluster feature flags: seatbelt chime, engine/trans
  temp display enable, and similar IPC options [B — F150 2019 code sheet].
- **720-01-02 / 720-01-03 (IPC)** — further cluster options; 720-01-03
  carries keyless-entry enable values on some models [C — Explorer Police
  Utility thread].
- **720-04-01 (IPC)** — trailer brake controller gain-setting display [B —
  F150 code sheet]. **720-07-01 (IPC)** — trailer brake control module
  enable; IPC quick-boot flag [B — F150/Super Duty sheets].
- **7D0-01-01 (APIM)** — head-unit feature flags: audio sources
  (Sirius/SDARS), Sony DSP enable, reverse camera, stereo extended-play
  timer, CAN steering-wheel switch type + clock master, AUX/climate/chime
  strategy, speaker fader [B — Explorer + F150 APIM references].
- **7D0-01-02 (APIM)** — climate menu on SYNC screen, fan speed, max
  defrost, nav byte (00 = no nav, 04 = with nav) [B — F150 sheets; xdaforums
  nav-activation thread].
- **7D0-02-01 / 7D0-03-01 (APIM)** — boot animation / theme selection,
  navigation-in-motion [B — Super Duty sheet].
- **726-01-01 (BCM)** — alarm/horn/crash configuration ENUMs on 2020+
  Super Duty (Alarm_Sound_Cfg, Horn_Sound_Cfg, Crash_Enable_Cfg,
  Crash_Spinout_Enable_Cfg) [B — Super Duty BCM sheet].
- **726-01-02 (BCM)** — panic alarm mode (lights+horn vs lights only),
  OBD-protect enable, trailer-connect config [B — F150 sheets].
- **726-37-01 (BCM)** — panic alarm fob behavior (disabled / 2-press /
  enabled) [B — F150 sheet]. **726-41-02 (BCM)** — double-honk disable,
  running lamps [B — FORScan tutorial example]. **726-42-01 (BCM)** —
  Secure Idle [B — F150 sheet]. **726-48-02 (BCM)** — auto start/stop
  disable [B — F150 2019 code sheet].
- **727-01-01 / 727-01-02 (ACM)** — auxiliary subwoofer enable, variable
  line-level preamp outputs for aftermarket amps [B — F150 sheet].
- **724-01-01 (SCCM)** — turn-signal flash count [B — F150 sheet].
- **760-03-01 (ABS)** — hill descent control enable [B — Super Duty sheet].
- **736-04-01 (PAM)** — perpendicular park enable (only on trucks already
  equipped with Active Park Assist) [B — F150 sheet].
- **VIN storage blocks** (ASCII hex of the 17-char VIN + checksum): BCM
  726-09-01–726-11-01, HVAC 733-02-01–733-02-04, ABS 760-01-01–760-01-04,
  CCM 764-02-01–764-02-04, RCM 737-01-01–737-01-04, FCIM 7A7-02-01–7A7-02-04,
  SODL/R 7C4/7C6-07-01–07-04 [B — Explorer 11-23MY listing].

## 5. How as-built relates to UDS

- Reading as-built data over the wire is UDS **0x22 ReadDataByIdentifier**
  against the module's configuration DIDs; writing is **0x2E
  WriteDataByIdentifier** [B — UDS service semantics; 0x22-F190-as-VIN
  example in community UDS docs].
- The exact DID mapping for each as-built block is Ford-proprietary per
  module — FORScan abstracts it away, and the community spreadsheets work
  at the block-line level, not the DID level [C — inferred from the
  tooling; no public Ford DID-to-block table found].
- Session/security prerequisites: FORScan manages UDS session control
  (0x10) internally; **as-built writes require a FORScan Extended License**
  [B — FORScan docs/community]. Some modules additionally require **0x27
  Security Access** for security-sensitive as-built fields — documented for
  FDIM-family VIN writes ("Some modules such as the FDIM require something
  called Security Access in order to modify the VIN in the as built data")
  [B — FG-Falcon VIN guide].
- Module addressing on the wire follows Ford's **+8 response convention**:
  request 7D0 → response 7D8, 726 → 72E, 7E0 → 7E8, etc. [B — community
  UDS research, cross-checked in this project's diagnostics data].
- Relevance to the M2 firmware: the UDS mode's existing 0x22/0x2E
  implementation is the correct primitive for as-built read/write; what is
  still missing is the per-module DID map (Ford-proprietary) and the
  per-module 0x27 seed/key handling (no public algorithm — never to be
  invented).

## 6. Safety notes and the FORScan backup workflow

- **Back up first, always.** FORScan's Programming screen lists every
  detected module; each entry marked "AS-BUILT format" is entered and saved
  via "save all" to a `.abt` file (default location `\documents\Forscan\`).
  Do this for ALL as-built modules before changing anything — even if you
  only plan to touch one [B — FORScan tutorial].
- **Extended License is required** for configuration writes (free from the
  FORScan forum, generated against the install's hardware ID) [B —
  FORScan docs].
- **Wrong values can brick a module.** "Following this procedure can
  potentially brick the module" [C — FG-Falcon VIN guide]; "Don't get
  greedy and change a bunch of stuff day one… You'll have no time if you
  brick your truck due to poor discipline" [C — f150gen14]. Work key-on /
  engine-off, one module and one small change at a time, verify the change
  took before moving on.
- **Recovery paths if something goes wrong:** (1) restore the `.abt`
  backups through FORScan's programming screen [B — FORScan tutorial];
  (2) pull the factory record for the VIN from motorcraftservice.com/AsBuilt
  and re-apply it [B — Ford portal]; (3) dealer IDS PMI as the last resort
  [B — fenderbender].
- **Dealer-visit hygiene** (community practice): back up the modded
  modules, restore factory `.abt` files before the visit, re-apply mods
  afterward [C — FORScan tutorial thread].
- **Don't trust one spreadsheet blindly.** Bit meanings are model- and
  year-specific; a 2019 F-150 sheet does not apply to a 2022 Explorer.
  When FORScan's plain-English easy mode offers the same setting, prefer
  it — it edits the same bytes with less transcription risk [B —
  f150gen14].

## Coverage notes

- Could NOT verify in this pass: the 7D7 address from the brief (no source
  found; GSM is at 732 on 2020MY+ instead) [?]; full block ranges per
  module (only the community-documented blocks are listed); the
  Ford-proprietary DID mapping behind each as-built block; per-module 0x27
  security-access requirements beyond the FDIM-family note; pre-2011
  module addresses (CGEA-era vehicles use different maps).
- Thin spots: 744 DSM and 776 SCME rest on a single source [C]; HVAC
  733's pre-2016 EATC-era block layout was not researched; BCM block
  purposes skew toward F-150/Super Duty (the best-documented community
  spreadsheets) — other models' BCM blocks differ.
- No full vehicle as-built dump is reproduced anywhere in this file, per
  the project rule — format, addresses, and block purposes only.
- All examples use masked (`x`/`zz`) notation from community spreadsheets;
  the two unmasked single lines cited (726-48-02, 726-41-02) are brief
  quotes of already-public spreadsheet rows, not vehicle data.

## Sources consulted

- FORScan community module-address tables (scribd setup guides; Explorer
  11-23MY module listing with per-module VIN-storage blocks) [B]
- FORScan tutorial (Google doc): address anatomy (module-block-line),
  checksum as hex-digit sum, .abt backup/restore procedure, DDM/PDM
  programming examples [B]
- F150 2019 code sheet (f150forum) + 2020-22 Super Duty FORScan spreadsheet
  (Google Sheets): block purposes, ENUM-style field decodes [B]
- F150/Super Duty/Explorer APIM references (scribd): 7D0-01-01 bit fields
  [B]
- fenderbender (trade press): as-built definition, PMI, Motorcraft portal
  behavior [B]
- motorcraftservice.com/AsBuilt (Ford official portal) [A for existence]
- FG-Falcon VIN-coding guide (GitHub wiki): VIN hex layout, 00 checksum
  placeholder, FDIM 0x27 security-access note, brick warning [B/C]
- f150gen14.com threads: easy-vs-as-built equivalence, beginner discipline
  [B/C]
- fordownersclub / fordraptorforum threads: BCE-vs-BCM naming, TCM 7E1
  confirmation [B/C]
- forscan.org forum: TCM programming / as-built upload procedure [B]
- Community UDS references: 0x22/0x2E/0x27/0x10 service roles, Ford +8
  response convention [B]
