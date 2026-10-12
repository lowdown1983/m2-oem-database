# Per-platform bus/module maps

Module-to-bus assignments for the 32 opendbc DBC platforms, derived from DBC node names cross-checked against the bus-architecture briefs. Inferred assignments are marked; on gateway-heavy platforms the DBC captures gateway-forwarded traffic, not raw bus traffic.

## bmw_e9x_e8x — BMW E90 3-series (2005–2011; E91/E92/E93 share the architecture) — PT-CAN [B]

- Make: bmw; bus: PT-CAN, 500 kbps (3 wires: CAN-H/CAN-L + separate wake-up line, not CAN signaling)
- Evidence: OEM-BMW-TRAIN — ST401 Body Electronics II; OEM-BMW-COMM — opendbc bmw_e9x_e8x.dbc CAN-ID attribution (DME 0xAA/0xA8/0xB4…, DSC 0xC8/0xCE…, EGS 0xBA…, SZL 0xC4…) cross-checked with bimmerforums E90 CAN project

| Node | Module |
|---|---|
| DME_DDE | Engine control (DME petrol / DDE diesel) |
| EGS | Transmission control |
| DSC | Dynamic stability control |
| EKPS | Fuel pump control |
| GWS | Gear selector switch |

- Not in DBC (brief-documented): K-CAN body modules (CAS, FRM, KOMBI — not on PT-CAN), F-CAN chassis nodes

## bmw_e9x_e8x — BMW E90 3-series (2005–2011) — K-CAN (body) [B]

- Make: bmw; bus: K-CAN, 100 kbps (not on DLC — tap behind JBE; reported fault-tolerant-style, TJA1051 compatibility UNVERIFIED)
- Evidence: OEM-BMW-TRAIN — ST401; BMW E90 junction-box overview (scribd)

| Node | Module |
|---|---|
| CAS | Car Access System |
| JBE_JBBF | Junction box electronics (gateway PT<->K) |
| FRM | Footwell module |
| KOMBI | Instrument cluster |
| IHKA | Climate control |
| MRS | Airbag (multiple restraint system) |
| FZD | Roof function center |
| CCC_CIC | Infotainment headunit |
| PDC | Park distance control |

- Not in DBC (brief-documented): PT-CAN powertrain modules, F-CAN chassis nodes, MOST ring nodes (fiber, out of scope)

## bmw_e9x_e8x — BMW E90 3-series (2005–2011) — F-CAN (chassis) [B]

- Make: bmw; bus: F-CAN, 500 kbps (direct tap at DSC/SZL)
- Evidence: OEM-BMW-TRAIN — ST401

| Node | Module |
|---|---|
| DSC | Dynamic stability control |
| SZL | Steering column switch cluster |
| AL | Active steering |

- Not in DBC (brief-documented): PT-CAN and K-CAN nodes

## bmw_e9x_e8x — BMW F30 3-series (2012–2018) — all CAN buses (no dedicated DBC; nearest: bmw_e9x_e8x E-series, NOT directly transferable) [B]

- Make: bmw; bus: PT-CAN 500k / PT-CAN2 500k / K-CAN (Body) 100k / K-CAN2 500k (none on DLC except D-CAN diagnostic link)
- Evidence: OEM-BMW-TRAIN — BMW F30 Complete Vehicle training (via bimmerscan.com FEM page). No F30 DBC in database; E-series CAN IDs do not transfer (gateway encapsulation).

| Node | Module |
|---|---|
| DME_DDE | Engine control |
| EGS | Transmission control |
| ACSM | Airbag |
| EKPS | Fuel pump |
| GWS | Gear selector |
| REM | Rear electronics module |
| FZD | Roof function center |
| PMA | Parking maneuvering assistant |
| FLA | High-beam assistant |
| FEM_ZGW | Front electronics module with integrated central gateway ZGM (absorbs CAS/JBE/FRM) |
| HU_H | Headunit high (NBT) |
| IHKA | Climate control |

- Not in DBC (brief-documented): FlexRay chassis nodes (DSC, ICM, VDM, EPS — out of M2 scope), MOST ring, Ethernet nodes (HU-H, KOMBI — out of M2 scope)

## bmw_e9x_e8x — BMW G20 3-series (2019+) — gateway only (no dedicated DBC; CAN FD / DoIP — OUT OF M2 SCOPE) [C]

- Make: bmw; bus: CAN FD buses + DoIP over Ethernet (OBD 3/11/12/13); K-CAN4 ≈ F30 K-CAN2 role
- Evidence: OEM-BMW-COMM — obdii365 BDC3 case study; community G-series notes. A CAN-2.0-only tool's role on G20 is limited to whatever the BDC exposes on classic-CAN DLC pins, if anything.

| Node | Module |
|---|---|
| BDC | Body Domain Controller — central gateway and immobilizer (BDC3 from 2020) |

- Not in DBC (brief-documented): Full G20 bus/module table not verified in this pass — BMW G-series training material not found in public sources, DME/DDE, EGS and chassis nodes (CAN FD — no M2 hardware)

## ford_cads — Ford CADS (older driver-assist) [C]

- Make: ford; bus: radar private bus (MRR direct) — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC node list contains only MRR; message set is radar-internal (XCP calibration protocol)

| Node | Module |
|---|---|
| MRR | Medium-Range Radar) only — status, header, XCP DAQ messages; 64-bit variant in FORD_CADS_64 |

- Not in DBC (brief-documented): everything else — single-sensor DBC

## ford_cads_64 — Ford CADS (older driver-assist) [C]

- Make: ford; bus: radar private bus (MRR direct) — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC node list contains only MRR; message set is radar-internal (XCP calibration protocol)

| Node | Module |
|---|---|
| MRR | Medium-Range Radar) only — status, header, XCP DAQ messages; 64-bit variant in FORD_CADS_64 |

- Not in DBC (brief-documented): everything else — single-sensor DBC

## ford_cgea1_2_bodycan_2011 — Ford CGEA 1.2 — body CAN [B]

- Make: ford; bus: MS-CAN, 125 kbps, pins 3/11
- Evidence: OEM-MODULE-MAPS — message content matches the Ford brief's MS-CAN module list (GEM/BCM, door modules, EATC) [B]

- Not in DBC (brief-documented): instrument cluster, RCM, KVM, PAM — named in brief, absent here

## ford_cgea1_2_ptcan_2011 — Ford CGEA 1.2 — powertrain CAN [B]

- Make: ford; bus: HS-CAN, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — message content matches the Ford brief's HS-CAN module list (PCM, TCM, ABS, EPAS) [B]

- Not in DBC (brief-documented): BCM/GWM, APIM, instrument cluster, RCM — not in this DBC

## ford_fusion_2018_adas — Ford Fusion 2018 — ADAS bus [C]

- Make: ford; bus: ADAS/private bus (not DLC-exposed) — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC contains only object-track messages; no module nodes named

| Node | Module |
|---|---|
| object-tracking nodes (Object_00 … Object_13+) — radar/camera fusion output only | — |

- Not in DBC (brief-documented): IPMA, radar module, PSCM — the actual ADAS ECUs

## ford_fusion_2018_pt — Ford Fusion 2018 — powertrain CAN [B]

- Make: ford; bus: HS-CAN, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — 14-message subset consistent with HS-CAN powertrain traffic [B]

- Not in DBC (brief-documented): PCM, TCM as named nodes, APIM, IPC

## ford_lincoln_base_pt — Ford/Lincoln base — powertrain CAN (shared base DBC) [B]

- Make: ford; bus: HS-CAN, 500 kbps, pins 6/14 (opendbc maps this DBC to Bus.pt for current Ford platforms incl. CAN-FD ones — but the DBC itself is classic-CAN format)
- Evidence: OEM-MODULE-MAPS — DBC node names corroborated by the Ford brief's module/ID list (GWM 0x726, PCM 0x7E0) and openpilot's Ford platform mapping [B]

- Not in DBC (brief-documented): BCM/BdyCM, APIM, IPC, RCM, SCCM — named in brief, absent here

## gm_global_a_chassis — GM Global A — chassis bus [B]

- Make: gm; bus: HS GMLAN (Chassis Expansion), 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — DBC node names match GM chassis-module naming (K-series designators); GM service doc lists EBCM on HS GMLAN [A]

| Node | Module |
|---|---|
| K182_PACM | Park Assist Control Module |
| K43_PSCM | Power Steering Control Module |
| K17_EBCM | Electronic Brake Control Module |
| K124_ASCM | Active Safety Control Module |

- Not in DBC (brief-documented): ECM, TCM, BCM, electronic suspension (ESC) — not in this DBC

## gm_global_a_high_voltage_management — GM Global A — high-voltage (hybrid/EV) bus [B]

- Make: gm; bus: HS GMLAN, 500 kbps, pins 6/14 (hybrid high-voltage segment)
- Evidence: OEM-MODULE-MAPS — DBC node names + message set (Battery_Module_1-4, Pack_Stats, Charger_stats, Battery_temp) corroborate a battery-management segment

| Node | Module |
|---|---|
| K16_BECM | Battery Energy Control Module |
| K114B_HPCM | Hybrid Powertrain Control Module |
| T18_BatteryCharger | onboard charger |

- Not in DBC (brief-documented): ECM, APM (in powertrain_expansion DBC), contactor controllers

## gm_global_a_lowspeed — GM Global A — low-speed bus [B]

- Make: gm; bus: SW GMLAN (single-wire), 33.33 kbps, pin 1
- Evidence: OEM-MODULE-MAPS — message content is body/comfort traffic consistent with SWCAN; GM brief places body modules on SW GMLAN pin 1 [B]

- Not in DBC (brief-documented): BCM itself, HVAC, radio, instrument cluster, seat modules — none appear as named nodes

## gm_global_a_lowspeed_1818125 — GM Global A — low-speed bus (extended capture) [B]

- Make: gm; bus: SW GMLAN (single-wire), 33.33 kbps, pin 1
- Evidence: OEM-MODULE-MAPS — message-name content (ODI_BCM_2_CenterStack, AMM lighting, heated-windshield requests) matches SWCAN body traffic [B]

| Node | Module |
|---|---|
| 367 messages of body/comfort traffic (ODI center-stack/BCM exchanges, climate requests, seat settings, lighting customization, lane-keeping) — BCM and center-stack/infotainment nodes dominate | — |

- Not in DBC (brief-documented): named module nodes (BU_ is placeholder XXX), individual module attribution is inference from message names [C]

## gm_global_a_object — GM Global A — object/ADAS bus [C]

- Make: gm; bus: ADAS object bus (likely Chassis Expansion HS segment), 500 kbps — bus assignment inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC node names alone; no factory topology found for the object bus. Sender counts (VIS2_FO 22, LRR 20 msgs) corroborate a camera+radar fusion segment

- Not in DBC (brief-documented): everything powertrain/chassis/body — this DBC is ADAS-only

## gm_global_a_powertrain_expansion — GM Global A — powertrain expansion bus [C]

- Make: gm; bus: HS GMLAN (Powertrain Expansion), 500 kbps — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC contains only the APM node; "powertrain expansion" is the DBC filename's claim, corroborated by the GM brief's HS-variant list [B]

| Node | Module |
|---|---|
| K1_APM | Accessory Power Module) — APM_Stats / APM_Command |

- Not in DBC (brief-documented): ECM, TCM — the actual powertrain controllers are not in this DBC ---

## acura_ilx_2016_nidec — Acura ILX 2016 — F-CAN (Nidec ADAS) [B]

- Make: honda; bus: F-CAN, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — Honda brief documents F-CAN at 500 kbps on 6/14 [A/B]; openpilot's hondacan.py confirms the F-CAN ADAS layout [B]

| Node | Module |
|---|---|
| ADAS, RADAR (Nidec radar unit); message content: vehicle state, radar diagnostics | — |

- Not in DBC (brief-documented): ECM, VSA modulator, EPS, gauge module — the actual F-CAN powertrain nodes, B-CAN (MICU, climate, immobilizer) entirely absent (never at the DLC per the brief) ---

## hyundai_2015_ccan — Hyundai 2015 — C-CAN (chassis) [B]

- Make: hyundai; bus: C-CAN, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — DBC node names corroborated by the public 2015 Hyundai C-CAN DBC node documentation (EMS/TCU/ESC/IBOX/SMK/SCC) [B]; matches the Hyundai brief's C-CAN description [B]

- Not in DBC (brief-documented): SMK (smart key) as a sender, CGW gateway node present in BU_ list but sends nothing in this capture

## hyundai_2015_mcan — Hyundai 2015 — M-CAN (multimedia/body) [B]

- Make: hyundai; bus: M-CAN — bitrate and DLC exposure UNCONFIRMED [?] (treated as interior-only per the Hyundai brief)
- Evidence: OEM-MODULE-MAPS — DBC node names are body/multimedia modules [B]; M-CAN bitrate/pins unconfirmed per the Hyundai brief [?]

| Node | Module |
|---|---|
| HU_TMU | head unit / telematics |
| AMP | amplifier |
| MON | monitor/display |
| SWRC | steering-wheel remote |
| CLOCK, HUD, DATC, CCP, IBOX, CLU, CGW, AVM, plus RSE (rear-seat entertainment | — |
| IPM, KBD | — |

- Not in DBC (brief-documented): exact gateway routing between C-CAN and M-CAN, M-CAN bitrate

## hyundai_i30_2014 — Hyundai i30 2014 — C-CAN [C]

- Make: hyundai; bus: C-CAN, 500 kbps, pins 6/14 — inferred [C]
- Evidence: OEM-MODULE-MAPS — message names only; consistent with C-CAN powertrain/chassis content [C]

- Not in DBC (brief-documented): BCM, TCU as named nodes

## hyundai_santafe_2007 — Hyundai Santa Fe 2007 — CAN (early) [B]

- Make: hyundai; bus: C-CAN, 500 kbps, pins 6/14 — inferred [C] (2007 is early in Hyundai's CAN rollout; 2008 was a transition year per the brief)
- Evidence: OEM-MODULE-MAPS — DBC node names are the classic early-CAN module set [B]

| Node | Module |
|---|---|
| ECU, TCU, ESP, SAS (steering-angle sensor | — |
| ABS, AWD | — |

- Not in DBC (brief-documented): BCM, airbag, cluster ---

## mazda_2017 — Mazda3 BM/BN SkyActiv (2014–2018) — HS-CAN + MS-CAN [B]

- Make: mazda; bus: HS-CAN 500k (6/14) + MS-CAN 125k (3/11, exposed at DLC)
- Evidence: OEM-MAZDA-COMM — Mazda Vehicle Networks training doc; berumiya FBCM/RBCM style classification; opendbc mazda_2017.dbc (102 messages)

| Node | Module |
|---|---|
| PCM | Powertrain control module |
| TCM | Transmission control module |
| DSC_HU_CM | DSC hydraulic unit / control module |
| EPS | Electric power steering |
| SAS | Airbag (SAS) |
| IC | Instrument cluster |
| FBCM_RBCM | Front/rear body control modules (MS-CAN) |
| HVAC | Climate control (MS-CAN) |
| AUDIO | Audio unit (MS-CAN) |
| TPMS | Tire pressure monitoring (MS-CAN) |
| RKE | Keyless entry (MS-CAN) |

- Not in DBC (brief-documented): BCMM-style models (different body architecture)

## mazda_2017 — Mazda CX-5 KE/KF SkyActiv (2012+) — HS-CAN + MS-CAN (nearest DBC: mazda_2017; CX-5 2017–21 dashcam mode) [B]

- Make: mazda; bus: HS-CAN 500k (6/14) + MS-CAN 125k (3/11)
- Evidence: OEM-MAZDA-COMM — berumiya FBCM/RBCM style classification; opendbc CX-5 2017–21 dashcam mode; WardsAuto (first SkyActiv model 2012)

| Node | Module |
|---|---|
| PCM | Powertrain control module |
| TCM | Transmission control module |
| DSC | Dynamic stability control |
| EPS | Electric power steering |
| SRS | Airbag |
| IC | Instrument cluster |
| FBCM_RBCM | Front/rear body control modules (MS-CAN) |
| HVAC | Climate control (MS-CAN) |
| AUDIO | Audio unit (MS-CAN) |

- Not in DBC (brief-documented): 7th-gen BP/CX-30 / 2024+ ND3 architecture (possibly CAN FD — out of M2 scope if so, unverified)

## mazda_rx8 — Mazda6 GG Ford-shared (2003–2008), transitional — SCP + early CAN (nearest DBC: mazda_rx8, Ford-era) [B]

- Make: mazda; bus: SCP J1850 PWM 41.6k (pins 2/10, primary diag bus early GG) + HS-CAN 500k / MS-CAN 125k (added progressively) + K-line (pin 7)
- Evidence: OEM-MAZDA-COMM — Mazda training doc (Mazda3/BK example, GG shares architecture); diagnostics are Ford-style (P1000/P1001 self-test, as-built config)

| Node | Module |
|---|---|
| PCM | Powertrain control module |
| TCM | Transmission control module |
| ABS | ABS module |
| IC | Instrument cluster |
| PJB | Passenger junction box |
| EHPAS | Electro-hydraulic power steering |

- Not in DBC (brief-documented): Full GG CAN module census (progressive rollout — verify per year)

## mercedes_benz_e350_2010 — Mercedes W204 C-class (2007–2014) — CAN-C (powertrain) [B]

- Make: mercedes; bus: CAN-C, 500 kbps, DLC pins 6/14
- Evidence: OEM-MERCEDES-COMM — community pinout/scan sources; Daimler GF54.21-P-4170GZ (CAN-C 500k)

| Node | Module |
|---|---|
| ME | Engine control (e.g. ME9.7) |
| ETC | 722.9 transmission control |
| ESP | Electronic stability program |

- Not in DBC (brief-documented): CAN-B interior modules (behind gateway), MOST audio nodes

## mercedes_benz_e350_2010 — Mercedes W204 C-class (2007–2014) — CAN-B (interior) [C]

- Make: mercedes; bus: CAN-B, 83.3 kbps (behind gateway; tap at X30 hubs)
- Evidence: OEM-MERCEDES-COMM — community pinout sources [B/C]; Daimler GF54.21-P-4170GZ (CAN-B 83.3k) [A]

| Node | Module |
|---|---|
| EZS | Electronic ignition switch (immobilizer master) |
| SAM_F | Front SAM |
| SAM_R | Rear SAM |
| IC | Instrument cluster (on CAN-E link, connector pins 12/13) |

- Not in DBC (brief-documented): CAN-C powertrain modules

## mercedes_benz_e350_2010 — Mercedes W205 C-class (2014–2021) — UDS + DoIP (no dedicated DBC; topology not verified) [C]

- Make: mercedes; bus: UDS-era CAN + DoIP over Ethernet (COMAND/audio section)
- Evidence: OEM-MERCEDES-COMM — aftermarket tool vendors; community notes. Detailed W205 topology is a documented gap.

| Node | Module |
|---|---|
| N3_10 | Engine control MED40/M274 (online SCN coding via XENTRY documented) |

- Not in DBC (brief-documented): Detailed bus/module topology not verified in this pass, Per-module UDS arbitration IDs (undocumented publicly)

## mercedes_benz_e350_2010 — Mercedes W213 E-class (2016–2023) — control-unit overview (no dedicated DBC) [B]

- Make: mercedes; bus: CAN_D / CAN_EXT / CAN_INT / CAN_PTI + Ethernet/DoIP (W213-facelift+); pre-facelift CAN-2.0 at DLC for legislated diagnostics
- Evidence: OEM-MERCEDES-DOC — Daimler overall-network (GVN) component overview ©2023 via mbworld.org; OEM-MERCEDES-COMM — tool-vendor sources [C]

| Node | Module |
|---|---|
| N3_10 | ME-SFI engine control |
| N3_9 | CDI engine control |
| N10_6 | Front SAM |
| N10_8 | Rear SAM |
| N22_1 | Climate control |
| N88 | Tire pressure monitor |
| N112_9 | HERMES telematics |
| N118 | Fuel pump control |
| N83_5 | DC/DC converter (48V models) |
| N97 | Suspension control |
| N5_110 | Weight sensing |

- Not in DBC (brief-documented): Gateway topology detail (beyond control-unit list)

## nissan_xterra_2011 — Nissan Xterra 2011 — main CAN [B]

- Make: nissan; bus: main CAN, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — message names match the Nissan brief's main-CAN module set (ECM, TCM, ABS, BCM, IPDM) [B]

- Not in DBC (brief-documented): IPDM E/R, combination meter, 4WD/transfer modules, AV-CAN (pins 3/11) not captured, only 15 messages total — thinnest DBC in the database ---

## chrysler_cusw — Chrysler CUSW (Compact US Wide — Dart, 200, Cherokee KL) [B]

- Make: stellantis; bus: CAN-C, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — message content matches CAN-C powertrain/chassis profile; Stellantis brief places EPS/ABS/PCM/TCM/BCM on CAN-C [B]

- Not in DBC (brief-documented): PCM, TCM, BCM, ORC, SGW as named nodes, CAN-IHS side absent

## chrysler_pacifica_2017_hybrid_private_fusion — Chrysler Pacifica 2017 Hybrid — private fusion bus [C]

- Make: stellantis; bus: private/internal bus behind the gateway (NOT DLC-exposed) — inferred [C]
- Evidence: OEM-MODULE-MAPS — filename's "private_fusion" claim only; consistent with the Stellantis brief's private-CAN concept (gateway-internal buses) [B]

| Node | Module |
|---|---|
| unknown — message names are opaque (a_1, b_1, unknown_200); 31 messages, none decoded to a module | — |

- Not in DBC (brief-documented): effectively everything — this DBC is an undecoded private-bus capture

## fca_giorgio — FCA Giorgio (Alfa Romeo Giulia/Stelvio) [B]

- Make: stellantis; bus: CAN-C powertrain, 500 kbps (DBC content); platform also has 125 kbps CAN-IHS per community RE [C]
- Evidence: OEM-MODULE-MAPS — message names match CAN-C profile; Giulia sim-racing project documents the dual-bus layout (500k powertrain + 125k IHS) [C], consistent with the Stellantis brief's CAN-C/CAN-IHS split [B]

- Not in DBC (brief-documented): BCM, SGW, TCM, body/IHS modules — IHS side not captured ---

## subaru_forester_2017 — Subaru Global Platform (2017+ Impreza/Crosstrek/Forester/Ascent/Outback-Legacy 2020+) — HS-CAN [B]

- Make: subaru; bus: HS-CAN, 500 kbps, DLC pins 6/14
- Evidence: OEM-SUBARU-COMM — opendbc subaru_global DBCs (0x002 steering, 0x040 throttle, 0x118/0x121/0x122 LKAS, 0x139/0x13A brake/wheels, 0x220-0x222 EyeSight…); comma.ai openpilot wiki [B]

| Node | Module |
|---|---|
| ECM | Engine control module |
| TCM | Transmission control module |
| VDC_ABS | Vehicle dynamics / ABS control |
| EPS | Electric power steering |
| EyeSight | Stereo camera (LKAS, cruise, brake, distance, dash status) |
| BIU | Body integrated unit |
| CLUSTER | Combination meter |
| HVAC | Climate control |
| BSD_RCTA | Blind-spot detection / rear cross-traffic alert radar |

- Not in DBC (brief-documented): CAN-LS body nodes (interior, rate undocumented), LIN sub-bus devices

## subaru_outback_2015 — Subaru pre-global CAN era (2008–2016; BM/BR Legacy/Outback, SH Forester, GH/GE Impreza) — HS-CAN [B]

- Make: subaru; bus: HS-CAN, 500 kbps, DLC pins 6/14 (SSM2 K-line on pin 7 remains live for SSM diagnostics)
- Evidence: OEM-SUBARU-FSM — 2011 Legacy FSM LAN-diagnostics DTC tables [A] (module list); OEM-SUBARU-COMM — opendbc subaru_preglobal_2015.dbc [B]

| Node | Module |
|---|---|
| ECM | Engine control module |
| TCM | Transmission control module |
| VDC_ABS | VDC/ABS control module |
| BIU | Body integrated unit |
| CLUSTER | Combination meter |
| EPB | Electric parking brake |
| AC | Air conditioning |
| SAS | Steering angle sensor |
| EyeSight | EyeSight camera (where fitted) |

- Not in DBC (brief-documented): CAN-LS nodes, 2005 Legacy transition-year dual-bus split (BIU in the middle)

## toyota_2017_ref_pt — Toyota 2017 reference — powertrain CAN (V Bus) [B]

- Make: toyota; bus: CAN V Bus (HS), 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — DBC node names + Toyota repair-manual CAN V Bus member list (ECM, airbag, skid control, EPS, gateway ECU, DLC3) [B]; CGW dominance matches the gateway-ECU architecture in the Toyota brief [B]

- Not in DBC (brief-documented): ECM, skid control ECU, main body ECU, combination meter as named senders — the DBC is gateway/ADAS-weighted, BEAN/AVC-LAN absent entirely (no M2-reachable path in any case)

## toyota_adas — Toyota ADAS (TSS / TSS 2.0) — camera bus [C]

- Make: toyota; bus: ADAS camera private bus (not DLC-exposed) — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC contains only object-track messages; no module nodes

| Node | Module |
|---|---|
| forward-camera object tracking (TRACK_A_0 … A_12, STATUS_MSG | — |

- Not in DBC (brief-documented): the camera ECU itself, radar, DSU

## toyota_iq_2009_can — Toyota iQ 2009 — CAN [C]

- Make: toyota; bus: CAN V Bus (HS), 500 kbps — inferred [C]
- Evidence: OEM-MODULE-MAPS — message content only; no named module nodes

- Not in DBC (brief-documented): gateway ECU, body modules ---

## toyota_prius_2010_pt — Toyota Prius 2010 — powertrain CAN (hybrid) [B]

- Make: toyota; bus: CAN V Bus (HS), 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — node names match Prius hybrid topology (HV ECU, HV battery on the HS bus per the Toyota brief) [B]

| Node | Module |
|---|---|
| DSU | Driving Support Unit |
| HCU | Hybrid Control Unit |
| EPS, IPAS (Intelligent Parking Assist); message content: brake module, wheel speeds, gas pedal, steer torque, pre-collision | — |

- Not in DBC (brief-documented): ECM, HV battery ECU as named nodes (0x7E2/0x7E3 diagnostic IDs from the brief have no DBC counterpart here)

## toyota_radar_dsu_tssp — Toyota TSS-P — radar/DSU bus [C]

- Make: toyota; bus: radar private bus (not DLC-exposed) — inferred [C]
- Evidence: OEM-MODULE-MAPS — BU_ lists RADAR; consistent with the Toyota brief's radar→DSU→powertrain forwarding topology [C]

| Node | Module |
|---|---|
| RADAR node + DSU (Driving Support Unit); OBJECT_0 … OBJECT_11, steering buttons, cluster display messages | — |

- Not in DBC (brief-documented): millimeter-wave radar ECU details, skid control ECU

## toyota_tss2_adas — Toyota ADAS (TSS / TSS 2.0) — camera bus [C]

- Make: toyota; bus: ADAS camera private bus (not DLC-exposed) — inferred [C]
- Evidence: OEM-MODULE-MAPS — DBC contains only object-track messages; no module nodes

| Node | Module |
|---|---|
| forward-camera object tracking (TRACK_A_0 … A_12, STATUS_MSG | — |

- Not in DBC (brief-documented): the camera ECU itself, radar, DSU

## volvo_v40_2017_pt — Volvo P1 — V40 (2013–2019), representative — PT bus [B]

- Make: volvo; bus: HS-CAN 500k (6/14) + LS-CAN 250k (3/11); CEM gateway
- Evidence: OEM-VOLVO-COMM — opendbc volvo_v40_2017_pt.dbc (51 messages); P1 bus architecture carried through to end of production

| Node | Module |
|---|---|
| ECM | Engine control module |
| TCM | Transmission control module |
| BCM | Brake control module |
| CEM | Central electronic module |
| DIM | Driver information module |
| SRS | Supplemental restraint system |
| SAS | Steering angle sensor |
| ACC | Adaptive cruise control |

- Not in DBC (brief-documented): LS-only body modules (DDM/PDM/PSM/CCM per P2/P3 architecture)

## volvo_v60_2015_pt — Volvo P2 — XC90 I (2003–2014), representative — HS-CAN (no P2 DBC in database; nearest: P3-era volvo_v60_2015_pt) [B]

- Make: volvo; bus: HS-CAN, 500 kbps ('05+; 250k in '04), DLC pins 6/14; terminators in BCM + ECM (Bosch EMS MY02+)
- Evidence: OEM-VOLVO-VADIS — Volvo CAN-bus diagnostics overview (VADIS-era transcription)

| Node | Module |
|---|---|
| ECM | Engine control module |
| TCM | Transmission control module |
| BCM | Brake control module (ABS) |
| ETM | Electronic throttle module |
| SAS | Steering angle sensor |

- Not in DBC (brief-documented): LS-CAN body modules (separate bus), CEM itself (gateway, on LS side)

## volvo_v60_2015_pt — Volvo P2 — XC90 I (2003–2014), representative — LS-CAN [B]

- Make: volvo; bus: LS-CAN, 250 kbps ('05+; 125k in '04), DLC pins 3/11; terminators in UEM + REM
- Evidence: OEM-VOLVO-VADIS — Volvo CAN-bus diagnostics overview; OEM-VOLVO-COMM — jasongainor/volvo-p2-pinout (2005 S60R harness) [C]

| Node | Module |
|---|---|
| CEM | Central electronic module (inter-bus gateway) |
| SRS | Supplemental restraint system |
| DDM | Driver door module |
| PDM | Passenger door module |
| PSM | Power seat module |
| CCM | Climate control module |
| DIM | Driver information module |
| RTI | Road traffic information |
| PHM | Phone module |
| AUD | Audio module |
| REM | Rear electronic module |
| SWM | Steering wheel module |
| UEM | Upper electronic module |
| DEM | Differential electronic module |

- Not in DBC (brief-documented): HS-CAN powertrain/chassis modules

## volvo_v60_2015_pt — Volvo P3 — XC60 I (2009–2017), representative — PT bus [B]

- Make: volvo; bus: HS-CAN 500k (6/14) + LS-CAN 250k (3/11); CEM gateway
- Evidence: OEM-VOLVO-COMM — opendbc volvo_v60_2015_pt.dbc (41 messages, real community captures); diagnostic addresses 0x726/0x72E (CEM), 0x730/0x738 (PSCM), 0x764/0x76C (FSM), 0x793/0x79B (CVM)

| Node | Module |
|---|---|
| ECM | Engine control (ECM1/ECM1_2/ECM2/ECM3) |
| TCM | Transmission control |
| BCM | Brake control module |
| CEM | Central electronic module (CEM0/CEM1/CEMBCM0) |
| DIM | Driver information module (DIM0/DIM1) |
| SRS | Supplemental restraint (SRS0/SRS1) |
| SAS | Steering angle sensor (SAS0) |
| PSCM | Power steering control module |
| FSM | Forward sensing module |
| CVM | Camera vision module |

- Not in DBC (brief-documented): Diagnostic addresses beyond 0x72x–0x79x captures (engine-ECM addressing unverified)

## volvo_v60_2015_pt — Volvo SPA — XC90 II (2016+), representative — OUT OF M2 SCOPE (no SPA DBC; DoIP/CAN FD) [C]

- Make: volvo; bus: Unified network, four domain masters; diagnostics = DoIP over Ethernet via VOE adapter; in-vehicle buses CAN FD (tool-vendor reports, INFERRED)
- Evidence: OEM-VOLVO-TJ — Volvo Technical Journal 34165.1.1 (VOE/Ethernet VIDA connection); Volvo Cars SPA press material. SPA/CMA need DoIP/CAN FD — no M2 hardware path.

| Node | Module |
|---|---|
| VDDM | Vehicle dynamics domain master |
| SDM | Safety domain master |
| CBDM | Car body domain master |
| IDM | Infotainment domain master |

- Not in DBC (brief-documented): Per-module CAN FD topology (not published), CMA (XC40 2018+) — same diagnostic posture (VOE/DoIP), no DBC

## vw_mlb — VW MLB (Audi longitudinal) — gateway-forwarded CAN [B]

- Make: vw; bus: diagnosis/powertrain CAN via gateway, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — DBC node names corroborate the MLB gateway topology [B]

- Not in DBC (brief-documented): comfort/infotainment (gateway-internal), instrument cluster

## vw_mqb — VW MQB — gateway-forwarded CAN [B]

- Make: vw; bus: diagnosis/powertrain CAN via J533 gateway, 500 kbps, pins 6/14
- Evidence: OEM-MODULE-MAPS — node names match the VW brief's MQB topology (all buses 500k, J533 gateway at 0x19) [B]; gateway dominance matches the "diagnosis CAN to J533" DLC model [B]

- Not in DBC (brief-documented): comfort/infotainment modules (gateway-internal per the brief), ABS/ESP as named senders is thin

## vw_mqbevo — VW MQB Evo — gateway-forwarded CAN [B]

- Make: vw; bus: diagnosis CAN via gateway, 500 kbps, pins 6/14 (CAN FD on MQB Evo unconfirmed — this DBC is classic-CAN format)
- Evidence: OEM-MODULE-MAPS — message names match MQB Evo module set; SFD-era platform per the VW brief [B]

- Not in DBC (brief-documented): gateway node itself as named sender, comfort/infotainment, SFD-protected modules' write paths (out of scope for a DBC)

## vw_pq — VW PQ (PQ25/35/46) — CAN [C]

- Make: vw; bus: powertrain/diagnosis CAN, 500 kbps, pins 6/14 (convenience CAN was 100k on PQ per SSP287 — this DBC's content reads as powertrain-side)
- Evidence: OEM-MODULE-MAPS — German message names only; bus assignment inferred from content mix [C]

- Not in DBC (brief-documented): J533 gateway, Motor/Getriebe as named nodes, convenience-CAN (100k) side not separated in this DBC ---

_Generated by scripts/build.py — do not hand-edit._
