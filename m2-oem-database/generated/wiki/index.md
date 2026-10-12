# M2/SuperB OEM Vehicle Database — v1.4.0 (2026-10-07)

Big Three v1: GM, Ford, Stellantis. Bus architecture, diagnostic access, and opendbc message catalogs.

Separate database from the hardware knowledge pack (v1.4.0): vehicle data is community-sourced and variable-quality, so it carries its own evidence grades rather than diluting the hardware pack's bar. Bus/diagnostic facts were researched per-make by three agents (2026-10-06) using web primary sources; message catalogs were mechanically harvested from a shallow clone of commaai/opendbc. Every factual claim carries a grade: A = factory documentation or verified capture; B = reputable community source (opendbc, FORScan docs, well-documented reverse-engineering, trade press); C = single anecdotal report or vendor marketing. Source conflicts are reported, not silently resolved. No seed/key algorithm or gateway bypass is invented or reproduced anywhere in this database — only publicly documented, legitimate access paths.


## Quality grades

- **A** — Factory documentation or verified capture.
- **B** — Reputable community source: opendbc, FORScan docs, well-documented reverse-engineering, trade press.
- **C** — Single anecdotal report or vendor marketing copy.

## Contents

- [Bus architecture](makes.md) — per-make buses, legacy protocols, M2 hardware mapping
- [Diagnostic access](diagnostics.md) — protocols, services, gateways, tools, seed/key policy
- [Vehicle message catalog](vehicles.md) — opendbc DBC harvest (32 DBCs, signal-level decode)
- [DTC catalog](dtcs.md) — SAE J2012 generic + manufacturer-specific trouble codes
- [UDS DID catalog](dids.md) — ISO-standard + make-specific Data Identifiers
- [Ford as-built](asbuilt.md) — module addresses, block format, UDS mapping
- [Module maps](module_maps.md) — per-platform bus/module assignments for the 32 DBCs
- [Validation](validation.md) — 36-question test against these artifacts

## Primary sources

- `OEM-OPDBC` — commaai/opendbc (shallow clone @ a7da786, 2026-10-06) — 16 Big Three DBCs, 1366 messages harvested mechanically
- `OEM-KPACK` — M2/SuperB hardware knowledge pack v1.4.0 — M2 OBD-II connector mapping, SWCAN/J1850/due_can software facts (VERIFIED)
- `OEM-GM-TECH` — ACDelco TechConnect 'GM Can Communication' — GM technician publication: three GMLAN buses, bitrates, BCM gateway role
- `OEM-GM-PIN` — Intrepid Control Systems neoVI OBD-II/J1962 pinout (2002) — DLC pin assignments incl. SW/MS/HS GMLAN and J1850
- `OEM-GM-SPEC` — GM Enhanced Diagnostic Test Mode spec excerpt + 11-bit USDT ID table (pcmhacking.net) — $7DF/$7E0-$7E7/$7E8-$7EF
- `OEM-GM-NXP` — NXP MC33897 product page — GMW3089v2.4 single-wire CAN: 33.33/83.33 kbps, high-voltage wake-up, 60 uA sleep
- `OEM-GM-COMM` — GM community sources: pcmhacking.net, HP Tuners forum, techroute66, owner forums (E38/E67 discussion, tool matrix, year anecdotes)
- `OEM-FORD-FORSCAN` — FORScan forum + docs — adapter capability matrix, MS-CAN switch behavior, extended license, service protocols
- `OEM-FORD-OPEN` — comma.ai openpilot Ford wiki — supported vehicles, CAN-FD platform list, Gateway Module definition
- `OEM-FORD-COMM` — Ford community/RE sources: blueovallabs ford-pscm-re glossary, merlinmb ESP32 Focus project, AutoEnginuity docs, Fordmods training material
- `OEM-STLA-STAR` — FCA US LLC STAR Online Publication v4.2 (02/06/2017), Jeep case S1508000235 — DLC pin assignments for CAN-C1/C2/CAN-BH
- `OEM-STLA-SGW` — AutoAuth/FCA guidance via LAUNCH/TOPDON/Autel/Bosch publications — SGW behavior, pricing, approved tools
- `OEM-STLA-COMM` — Stellantis community sources: jlwranglerforums CAN RE thread, TUCRRC Dodge CAN research, Fender Bender trade articles, ramforum
- `OEM-TOYOTA-TRAIN` — Toyota multiplex training doc (Aug 2014) + 2004 Prius manual RM1075U — CAN/BEAN/AVC-LAN speeds, gateway ECU
- `OEM-TOYOTA-SVC` — Toyota service info CHECK DLC3 (2012) — pins 6/14, SIL pulse pin 7, 54-69 ohm termination [A]
- `OEM-TOYOTA-COMM` — Toyota community sources (PriusChat/eevblog/TacomaWorld) — hybrid IDs, TSB T-SB-0043-14 seed flow, BEAN frames
- `OEM-HONDA-SVC` — Honda service manual (2006-2011 Civic) — B-CAN 33.33k single-wire [A], F-CAN, gateway, MPCS fallback
- `OEM-HONDA-COMM` — Honda community RE (opendbc hondacan.py, 29-bit diagnostic IDs, B-CAN tap projects)
- `OEM-VW-SSP` — VW SSP docs (872802 Passat, 553 Tiguan, Audi SSP287) — five CAN networks, bitrates, J533 gateway
- `OEM-VW-SFD` — VW SFD workshop manual — SFD scope/stages, reads+flashing NOT protected
- `OEM-VW-VCDS` — Ross-Tech VCDS — module addresses, Gateway Installation List
- `OEM-VW-COMM` — VW community sources (Autel/OBDeleven SFD paths, KWP-1281 doc, MQB bitrate measurements)
- `OEM-HYUNDAI-COMM` — Hyundai/Kia community sources (HiCOM manual, 2018 Soul field test, C-CAN DBC nodes)
- `OEM-NISSAN-TSB` — Nissan TSB NTB10-066C (2024) — CAN diagnosis, terminators, U-codes [A]
- `OEM-NISSAN-DDL` — Consult Protocol & Commands Issue 7 (Nissan Technical egroup) — DDL physical layer, command set
- `OEM-NISSAN-COMM` — Nissan community captures (Leaf OBD manual, Qashqai/Pathfinder projects) — 500 kbps, query-only DLC, 0x21 vs 0x22
- `OEM-SAE-J2012` — SAE J2012 generic DTC transcriptions (community) — P0xxx/P2xxx/P34xx/B0xxx/C0xxx/U0xxx; SAE text itself paywalled, no A grades claimed
- `OEM-GM-SI` — GM Service Information excerpts (gm.saturn.team archive), GM TSBs (2186567, 04-06-04-047G, 08-07-30-013), Corvette/Terraza SI master DTC lists
- `OEM-FORD-SI` — Ford 2008 master P/B/C/U DTC chart, Ford 2004 OBD System Operation Summary (motorcraftservice.com), stdrivers Ford OBD-II list
- `OEM-FCA-SI` — FCA service-manual excerpts (charm.li), FCA TSB 08-119-15, Mitchell/DTC databases
- `OEM-TOYOTA-DTC` — Toyota/Lexus service-manual excerpts (2001 Prius RM778U, 2004 Corolla RM1037U, 2004 Prius RM1076E, 2002 GS300 via charm.li), Toyota Service Information prints
- `OEM-HONDA-DTC` — Honda advanced-diagnostics PDFs, Honda service-manual U-code troubleshooting, technician sources
- `OEM-VW-DTC` — Ross-Tech wiki fault-code pages, VW TSB 01-21-10 (via NHTSA), VAG DTC transcriptions with 5-digit mappings
- `OEM-HYUNDAI-DTC` — Hyundai TechNet Times (National Service Training & Support Dept. — codes match shop manuals/GDS), transcribed Hyundai DTC documents
- `OEM-NISSAN-DTC` — Nissan/Infiniti service-manual excerpts (NATS chart, BRC section), TSB NTB10-066C (U1000 family), transcribed Nissan DTC lists
- `OEM-UDS-ISO` — ISO 14229-1:2013 Table C.1 (via testerpresent.com.au) — standardized DID numbers/names [A]; sizes/session server-defined
- `OEM-DID-BIG3` — GM GMW3110 §9.3.2.4.2 (GMLAN $1A DIDs); Ford Global Diagnostic Specification Part One v2003.0; jlwranglerforums UDS RE (Stellantis)
- `OEM-DID-IMPORTS` — OBDb signalsets (Toyota Prius, VW ID.4), OVMS vehicle_vweup, papataku/honda_ehev_analyzer, canair captures, Leaf TCU community app, Pathfinder capture
- `OEM-FORD-ASBUILT` — FORScan community (forums, docs, as-built spreadsheets) — module addresses, block purposes, checksum/format
- `OEM-MODULE-MAPS` — DBC BU_ node lists cross-checked against make bus-architecture briefs + platform topology sources
- `OEM-TOYOTA-MANUAL` — Toyota/Lexus repair-manual excerpts via third-party mirrors (zatonevkredit.ru, toyotamanuals.gitlab.io, ttundra.com, tovenza.com, to4runner.net, ttguide.net, charm.li; TSB T-SB-0172-13 via NHTSA)
- `OEM-TOYOTA-HYBRID` — "Toyota Prius OBDII Fault Code Guide" (scribd community transcription) — Gen-1/2 Prius hybrid DTCs
- `OEM-TOYOTA-COMM` — Toyota owner forums and technician threads (priuschat, tacomaworld, 4runners.com, tundras.com, yarisworld, JustAnswer Toyota)
- `OEM-HONDA-SB03020` — Honda Service Bulletin 03-020 "OBD II DTCs and Their Associated Monitors" (2003-03-29), detection-item list
- `OEM-HONDA-LISTS` — Honda DTC compilations (ninjafix.in, 5 Star Auto Repair, freeautomechanic.com, cars-care.net)
- `OEM-HONDA-BLINK` — Honda SRS/ABS/VSA blink-code charts (honda-tech.com technician transcription, civic5.com, JustAnswer Honda technician threads)
- `OEM-HONDA-TRS` — American Honda Interactive Network TRS message (2018-2020 Accord/Insight BCM DTCs) via oemdtc.com NHTSA filing
- `OEM-NISSAN-FSM` — Nissan/Infiniti FSM excerpts (2008 Altima EC, 2007 Xterra, 2010 Altima SRC, 2014 Cube SRS)
- `OEM-NISSAN-COMM` — Nissan owner forums and technician threads (sr20-forum, JustAnswer Nissan, CarProTool scan reports)
- `OEM-HYUNDAI-TECHNET` — Hyundai TechNet Times Vol. 24 Issue 02 (8th-edition Hyundai DTC listing, manuals.plus mirror)
- `OEM-HYUNDAI-SVC` — Hyundai/Kia shop-manual pages via charm.li; MOHAVE/BORREGO service manual; AFLS training doc; Restraint shop-manual DTC table
- `OEM-HYUNDAI-TSB` — HMA TSBs via NHTSA/oemdtc (MDPS MC-10180981-0001/MC-10170896-0001; TPMS 23-BE-001H); AutoHex Hyundai DTC Help (service-info-derived)
- `OEM-HYUNDAI-DB` — Hyundai/Kia DTC compilations (automanual, avtotachki, carcarehacks, OBDCodex, hyundaibook.ru, carscounsel.com, import-car.com, HVAC DTC list)
- `OEM-VW-OBDB` — miskibin/obd2-dashboard research-multibrand-extended-pids.md (formulas derived from OBDb v3 captures, CC BY-SA)
- `OEM-HONDA-WN7` — cnc-lasercraft/honda-wn7-wican obd-protocol.md (2026 Honda WN7 reverse-engineering, MCS-capture cross-checked)
- `OEM-SUBARU-FSM` — Subaru FSM excerpts via jdmcarmanuals.com (Legacy/Impreza/Tribeca engine, VDC, LAN and immobilizer diagnostics)
- `OEM-SUBARU-SSM` — RomRaider SsmProtocol documentation (SSM2 frame format, commands, parameter addresses)
- `OEM-SUBARU-COMM` — Subaru community sources (OBDCodex/scribd DTC transcriptions, forums, opendbc Subaru DBCs, FreeSSM/BtSsm docs)
- `OEM-MAZDA-SVC` — Mazda workshop-manual DTC tables; Mazda M-Tip MT-004/18 (MNAO, via manuals.plus); Mazda service-manual DTC pages
- `OEM-MAZDA-COMM` — Mazda community sources (Vehicle Networks training doc via rx8club, berumiya 6th-gen CAN DBC project, FORScan community, owner forums)
- `OEM-BMW-TRAIN` — BMW technical training (ST401 Body Electronics II bus systems, E90 vehicle electrical, F30 complete vehicle)
- `OEM-BMW-SIB` — BMW SIB 11 02 08 (VANOS faults 2A82/2A87, via oemdtc/NHTSA)
- `OEM-BMW-COMM` — BMW community sources (bimmerforums E90 CAN project, N54 DME code lists, Tool32 MSD80 archives, scribd DTC transcriptions, owner threads)
- `OEM-MERCEDES-DOC` — Daimler AG component descriptions (GF54.21-P-4170GZ central gateway), W211 networking training, Daimler DAS (1999) fault-code printouts
- `OEM-MERCEDES-COMM` — Mercedes community sources (mercedes-hacking-docs, scainner RESEARCH.md, forums, scribd DTC transcriptions, Autocom scan reports)
- `OEM-VOLVO-VADIS` — Volvo CAN-bus diagnostics overview (VADIS-era transcription): E000/E001, CEM-1A51–1A64, DF03–DF16, resistor locations
- `OEM-VOLVO-TJ` — Volvo Technical Journal 34165.1.1 (VOE/Ethernet VIDA connection on SPA/CMA)
- `OEM-VOLVO-COMM` — Volvo community sources (harness pinout repos, forums, opendbc Volvo DBCs, carcarehacks fault-code list, V-Tool/VDASH docs)

_Generated by scripts/build.py — do not hand-edit._
