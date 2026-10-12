# Per-platform bus/module maps (v1.3 research)

Derived from the 32 opendbc DBCs in the database (node lists, per-message
senders, message names) cross-checked against the make bus-architecture
briefs in this directory and live platform-topology sources. Every entry is
graded: **A** = factory topology documentation · **B** = DBC node names
corroborated by community topology · **C** = inferred from DBC names alone.

Module-name expansions are engineering interpretations of DBC node/sender
names, not factory definitions, unless marked [A]. "Missing" lists name
modules the make briefs place on the platform's buses but which do not
appear anywhere in the platform's DBCs — opendbc is an ADAS-driving subset,
not a full-vehicle capture.

Research date: 2026-10-06.

---

## GM — Global A

### gm_global_a_chassis
- Platform: GM Global A — chassis bus
- Make: gm
- Bus: HS GMLAN (Chassis Expansion), 500 kbps, pins 6/14
- Modules (DBC BU_ nodes): K182_PACM (Park Assist Control Module), K43_PSCM
  (Power Steering Control Module), K17_EBCM (Electronic Brake Control
  Module), K124_ASCM (Active Safety Control Module)
- Grade: [B]
- Evidence: DBC node names match GM chassis-module naming (K-series
  designators); GM service doc lists EBCM on HS GMLAN [A]
- Missing: ECM, TCM, BCM, electronic suspension (ESC) — not in this DBC

### gm_global_a_high_voltage_management
- Platform: GM Global A — high-voltage (hybrid/EV) bus
- Make: gm
- Bus: HS GMLAN, 500 kbps, pins 6/14 (hybrid high-voltage segment)
- Modules (DBC BU_ nodes): K16_BECM (Battery Energy Control Module),
  K114B_HPCM (Hybrid Powertrain Control Module), T18_BatteryCharger
  (onboard charger)
- Grade: [B]
- Evidence: DBC node names + message set (Battery_Module_1-4, Pack_Stats,
  Charger_stats, Battery_temp) corroborate a battery-management segment
- Missing: ECM, APM (in powertrain_expansion DBC), contactor controllers

### gm_global_a_lowspeed
- Platform: GM Global A — low-speed bus
- Make: gm
- Bus: SW GMLAN (single-wire), 33.33 kbps, pin 1
- Modules (inferred from message content — DBC BU_ is generic GMLAN/NEO):
  door status (DriverDoorStatus), chime, blinkers, steering-wheel angle,
  gear shifter, pedals, cruise buttons, wheel speed, side radars
  (LeftRadar/RightRadar)
- Grade: [B]
- Evidence: message content is body/comfort traffic consistent with SWCAN;
  GM brief places body modules on SW GMLAN pin 1 [B]
- Missing: BCM itself, HVAC, radio, instrument cluster, seat modules —
  none appear as named nodes

### gm_global_a_lowspeed_1818125
- Platform: GM Global A — low-speed bus (extended capture)
- Make: gm
- Bus: SW GMLAN (single-wire), 33.33 kbps, pin 1
- Modules: 367 messages of body/comfort traffic (ODI center-stack/BCM
  exchanges, climate requests, seat settings, lighting customization,
  lane-keeping) — BCM and center-stack/infotainment nodes dominate
- Grade: [B]
- Evidence: message-name content (ODI_BCM_2_CenterStack, AMM lighting,
  heated-windshield requests) matches SWCAN body traffic [B]
- Missing: named module nodes (BU_ is placeholder XXX); individual module
  attribution is inference from message names [C]

### gm_global_a_object
- Platform: GM Global A — object/ADAS bus
- Make: gm
- Bus: ADAS object bus (likely Chassis Expansion HS segment), 500 kbps —
  bus assignment inferred [C]
- Modules (DBC BU_ nodes / senders): K109_FCM (Front Camera Module),
  B233B_LRR (Long-Range Radar), VIS_FO / VIS2_FO (vision/camera nodes),
  EOCM variants (External Object Calculation Module), K124_ASCM
- Grade: [C]
- Evidence: DBC node names alone; no factory topology found for the object
  bus. Sender counts (VIS2_FO 22, LRR 20 msgs) corroborate a camera+radar
  fusion segment
- Missing: everything powertrain/chassis/body — this DBC is ADAS-only

### gm_global_a_powertrain_expansion
- Platform: GM Global A — powertrain expansion bus
- Make: gm
- Bus: HS GMLAN (Powertrain Expansion), 500 kbps — inferred [C]
- Modules: K1_APM (Accessory Power Module) — APM_Stats / APM_Command
- Grade: [C]
- Evidence: DBC contains only the APM node; "powertrain expansion" is the
  DBC filename's claim, corroborated by the GM brief's HS-variant list [B]
- Missing: ECM, TCM — the actual powertrain controllers are not in this DBC

---

## Ford

### ford_cgea1_2_ptcan_2011
- Platform: Ford CGEA 1.2 — powertrain CAN
- Make: ford
- Bus: HS-CAN, 500 kbps, pins 6/14
- Modules (inferred from message names — BU_ is placeholder XXX): PATS
  (Global_PATS_*), brake data, EPAS (EPAS_INFO), steering-wheel data,
  PCM/ECM/TCM/ABS traffic
- Grade: [B]
- Evidence: message content matches the Ford brief's HS-CAN module list
  (PCM, TCM, ABS, EPAS) [B]
- Missing: BCM/GWM, APIM, instrument cluster, RCM — not in this DBC

### ford_cgea1_2_bodycan_2011
- Platform: Ford CGEA 1.2 — body CAN
- Make: ford
- Bus: MS-CAN, 125 kbps, pins 3/11
- Modules (inferred from message names): BCM (BCM_m_FrP01/02), driver-seat
  modules, keyfob/pad, power liftgate, running boards, climate seats —
  body/comfort traffic
- Grade: [B]
- Evidence: message content matches the Ford brief's MS-CAN module list
  (GEM/BCM, door modules, EATC) [B]
- Missing: instrument cluster, RCM, KVM, PAM — named in brief, absent here

### ford_fusion_2018_pt
- Platform: Ford Fusion 2018 — powertrain CAN
- Make: ford
- Bus: HS-CAN, 500 kbps, pins 6/14
- Modules (inferred from message names): EPAS, steering-wheel/buttons,
  yaw/accel sensors, cruise, engine data, wheel speed, doors, BCM-to-HS
  body bridge (BCM_to_HS_Body), lane-keeping
- Grade: [B]
- Evidence: 14-message subset consistent with HS-CAN powertrain traffic [B]
- Missing: PCM, TCM as named nodes; APIM, IPC

### ford_fusion_2018_adas
- Platform: Ford Fusion 2018 — ADAS bus
- Make: ford
- Bus: ADAS/private bus (not DLC-exposed) — inferred [C]
- Modules: object-tracking nodes (Object_00 … Object_13+) — radar/camera
  fusion output only
- Grade: [C]
- Evidence: DBC contains only object-track messages; no module nodes named
- Missing: IPMA, radar module, PSCM — the actual ADAS ECUs

### ford_lincoln_base_pt
- Platform: Ford/Lincoln base — powertrain CAN (shared base DBC)
- Make: ford
- Bus: HS-CAN, 500 kbps, pins 6/14 (opendbc maps this DBC to Bus.pt for
  current Ford platforms incl. CAN-FD ones — but the DBC itself is
  classic-CAN format)
- Modules (DBC BU_ nodes, by sender volume): GWM (Gateway Module, 127
  msgs), IPMA_ADAS (Image Processing Module A, 62), PCM_HEV (36),
  SOBDMC_HPCM_FD1 (26), ABS_ESC (24), TSTR (tester, 15), ECM_Diesel (9),
  PSCM (7), TCM_DSL (7), PCM (6), TCCM (5), VDM (3), CMR_DSMC (3)
- Grade: [B]
- Evidence: DBC node names corroborated by the Ford brief's module/ID list
  (GWM 0x726, PCM 0x7E0) and openpilot's Ford platform mapping [B]
- Missing: BCM/BdyCM, APIM, IPC, RCM, SCCM — named in brief, absent here

### FORD_CADS / FORD_CADS_64
- Platform: Ford CADS (older driver-assist)
- Make: ford
- Bus: radar private bus (MRR direct) — inferred [C]
- Modules: MRR (Medium-Range Radar) only — status, header, XCP DAQ
  messages; 64-bit variant in FORD_CADS_64
- Grade: [C]
- Evidence: DBC node list contains only MRR; message set is radar-internal
  (XCP calibration protocol)
- Missing: everything else — single-sensor DBC

## Stellantis

### chrysler_cusw
- Platform: Chrysler CUSW (Compact US Wide — Dart, 200, Cherokee KL)
- Make: stellantis
- Bus: CAN-C, 500 kbps, pins 6/14
- Modules (inferred from message names — BU_ is placeholder XXX): EPS
  (EPS_STATUS), doors, gear selector, seatbelts, steering levers/column,
  traction button, wheel speeds, brakes, LKAS/DAS (driver-assist)
- Grade: [B]
- Evidence: message content matches CAN-C powertrain/chassis profile;
  Stellantis brief places EPS/ABS/PCM/TCM/BCM on CAN-C [B]
- Missing: PCM, TCM, BCM, ORC, SGW as named nodes; CAN-IHS side absent

### chrysler_pacifica_2017_hybrid_private_fusion
- Platform: Chrysler Pacifica 2017 Hybrid — private fusion bus
- Make: stellantis
- Bus: private/internal bus behind the gateway (NOT DLC-exposed) —
  inferred [C]
- Modules: unknown — message names are opaque (a_1, b_1, unknown_200);
  31 messages, none decoded to a module
- Grade: [C]
- Evidence: filename's "private_fusion" claim only; consistent with the
  Stellantis brief's private-CAN concept (gateway-internal buses) [B]
- Missing: effectively everything — this DBC is an undecoded private-bus
  capture

### fca_giorgio
- Platform: FCA Giorgio (Alfa Romeo Giulia/Stelvio)
- Make: stellantis
- Bus: CAN-C powertrain, 500 kbps (DBC content); platform also has
  125 kbps CAN-IHS per community RE [C]
- Modules (inferred from message names): EPS (EPS_1/2), ABS (ABS_1–7),
  ENGINE (ENGINE_1) — powertrain/chassis set
- Grade: [B]
- Evidence: message names match CAN-C profile; Giulia sim-racing project
  documents the dual-bus layout (500k powertrain + 125k IHS) [C],
  consistent with the Stellantis brief's CAN-C/CAN-IHS split [B]
- Missing: BCM, SGW, TCM, body/IHS modules — IHS side not captured

---

## Toyota / Lexus

### toyota_2017_ref_pt
- Platform: Toyota 2017 reference — powertrain CAN (V Bus)
- Make: toyota
- Bus: CAN V Bus (HS), 500 kbps, pins 6/14
- Modules (DBC BU_ nodes, by sender volume): CGW (Central Gateway ECU,
  113 msgs — dominant forwarder), DS1 (Driving Support ECU 1, 7),
  FCM (Forward recognition Camera Module, 7), SCS (5), AFS (Adaptive
  Front-lighting System, 3), BSR/CSR (2 each), KSS (2), FRD/MAV (1 each)
- Grade: [B]
- Evidence: DBC node names + Toyota repair-manual CAN V Bus member list
  (ECM, airbag, skid control, EPS, gateway ECU, DLC3) [B]; CGW dominance
  matches the gateway-ECU architecture in the Toyota brief [B]
- Missing: ECM, skid control ECU, main body ECU, combination meter as
  named senders — the DBC is gateway/ADAS-weighted; BEAN/AVC-LAN absent
  entirely (no M2-reachable path in any case)

### toyota_prius_2010_pt
- Platform: Toyota Prius 2010 — powertrain CAN (hybrid)
- Make: toyota
- Bus: CAN V Bus (HS), 500 kbps, pins 6/14
- Modules (DBC BU_ nodes): DSU (Driving Support Unit), HCU (Hybrid
  Control Unit), EPS, IPAS (Intelligent Parking Assist); message content:
  brake module, wheel speeds, gas pedal, steer torque, pre-collision
- Grade: [B]
- Evidence: node names match Prius hybrid topology (HV ECU, HV battery on
  the HS bus per the Toyota brief) [B]
- Missing: ECM, HV battery ECU as named nodes (0x7E2/0x7E3 diagnostic IDs
  from the brief have no DBC counterpart here)

### toyota_adas / toyota_tss2_adas
- Platform: Toyota ADAS (TSS / TSS 2.0) — camera bus
- Make: toyota
- Bus: ADAS camera private bus (not DLC-exposed) — inferred [C]
- Modules: forward-camera object tracking (TRACK_A_0 … A_12, STATUS_MSG)
- Grade: [C]
- Evidence: DBC contains only object-track messages; no module nodes
- Missing: the camera ECU itself, radar, DSU

### toyota_radar_dsu_tssp
- Platform: Toyota TSS-P — radar/DSU bus
- Make: toyota
- Bus: radar private bus (not DLC-exposed) — inferred [C]
- Modules: RADAR node + DSU (Driving Support Unit); OBJECT_0 … OBJECT_11,
  steering buttons, cluster display messages
- Grade: [C]
- Evidence: BU_ lists RADAR; consistent with the Toyota brief's
  radar→DSU→powertrain forwarding topology [C]
- Missing: millimeter-wave radar ECU details, skid control ECU

### toyota_iQ_2009_can
- Platform: Toyota iQ 2009 — CAN
- Make: toyota
- Bus: CAN V Bus (HS), 500 kbps — inferred [C]
- Modules (inferred from message names): engine, steering, braking,
  wheel speeds, vehicle dynamics — basic powertrain/chassis set
- Grade: [C]
- Evidence: message content only; no named module nodes
- Missing: gateway ECU, body modules

---

## Honda / Acura

### acura_ilx_2016_nidec
- Platform: Acura ILX 2016 — F-CAN (Nidec ADAS)
- Make: honda
- Bus: F-CAN, 500 kbps, pins 6/14
- Modules (DBC BU_ nodes): ADAS, RADAR (Nidec radar unit); message
  content: vehicle state, radar diagnostics
- Grade: [B]
- Evidence: Honda brief documents F-CAN at 500 kbps on 6/14 [A/B];
  openpilot's hondacan.py confirms the F-CAN ADAS layout [B]
- Missing: ECM, VSA modulator, EPS, gauge module — the actual F-CAN
  powertrain nodes; B-CAN (MICU, climate, immobilizer) entirely absent
  (never at the DLC per the brief)

---

## Volkswagen Group

### vw_mqb
- Platform: VW MQB — gateway-forwarded CAN
- Make: vw
- Bus: diagnosis/powertrain CAN via J533 gateway, 500 kbps, pins 6/14
- Modules (DBC BU_ nodes, by sender volume): Gateway_MQB (35 msgs —
  dominant forwarder), Motor_Diesel_MQB (19), Getriebe_DQ_MQB/DQ_Hybrid
  (transmission, 9+2), Airbag_MQB (6), BMS_MQB (3), LEH_MQB (3),
  SAK_MQB (2), Motor_Hybrid_MQB (2), Waehlhebel_MQB (gear selector, 1)
- Grade: [B]
- Evidence: node names match the VW brief's MQB topology (all buses
  500k, J533 gateway at 0x19) [B]; gateway dominance matches the
  "diagnosis CAN to J533" DLC model [B]
- Missing: comfort/infotainment modules (gateway-internal per the brief);
  ABS/ESP as named senders is thin

### vw_mlb
- Platform: VW MLB (Audi longitudinal) — gateway-forwarded CAN
- Make: vw
- Bus: diagnosis/powertrain CAN via gateway, 500 kbps, pins 6/14
- Modules (DBC BU_ nodes, by sender volume): Gateway_D4C7 (61),
  Motor_EDC17_D4 (diesel engine, 20), SCU_D4 (11),
  Getriebe_AL551_951_D4_C7 (transmission, 9), SCR_C7 (9),
  Airbag_D4 (6), Motor_Slave_D4 (5), EPB_D4 (4), SAK_C7 (3),
  ESP_D4 (3), LWS_D4 (steering-angle sensor, 1)
- Grade: [B]
- Evidence: DBC node names corroborate the MLB gateway topology [B]
- Missing: comfort/infotainment (gateway-internal); instrument cluster

### vw_mqbevo
- Platform: VW MQB Evo — gateway-forwarded CAN
- Make: vw
- Bus: diagnosis CAN via gateway, 500 kbps, pins 6/14 (CAN FD on MQB Evo
  unconfirmed — this DBC is classic-CAN format)
- Modules (inferred from message names — no BU_ list): Airbag, LWI
  (steering angle), Motor_Hybrid, Getriebe_Hybrid, LH_EPS, ESP
  (ESP_19/21/NEW_1), Waehlhebel (gear selector)
- Grade: [B]
- Evidence: message names match MQB Evo module set; SFD-era platform per
  the VW brief [B]
- Missing: gateway node itself as named sender; comfort/infotainment;
  SFD-protected modules' write paths (out of scope for a DBC)

### vw_pq
- Platform: VW PQ (PQ25/35/46) — CAN
- Make: vw
- Bus: powertrain/diagnosis CAN, 500 kbps, pins 6/14 (convenience CAN was
  100k on PQ per SSP287 — this DBC's content reads as powertrain-side)
- Modules (inferred from message names — BU_ is placeholder XXX):
  ZAS (ignition switch), Wischer (wiper), WFS (immobilizer),
  Waehlhebel (gear selector), PSG (pump control units), NOX, Niveau
  (level control), Navigation, Slave nodes, Sitz (seat info)
- Grade: [C]
- Evidence: German message names only; bus assignment inferred from
  content mix [C]
- Missing: J533 gateway, Motor/Getriebe as named nodes; convenience-CAN
  (100k) side not separated in this DBC

---

## Hyundai / Kia

### hyundai_2015_ccan
- Platform: Hyundai 2015 — C-CAN (chassis)
- Make: hyundai
- Bus: C-CAN, 500 kbps, pins 6/14
- Modules (DBC BU_ nodes, by sender volume): CLU (cluster, 17),
  EMS (engine management, 17), BCM (14), ESC (8), TCU (6), DATC (5),
  ACU (airbag, 4), ODS (3), MDPS (steering, 3), ABS (3), _4WD (3),
  SCC (smart cruise, 3), plus ECS, SPAS, DI_BOX, LDWS_LKAS, AHLS, PSB,
  AFLS, EPB, LCA, IBOX, EVP, AAF, CUBIS, OPI, LPI, PGS, HUD, AVM,
  FPCM, LVR, SNV, IAP
- Grade: [B]
- Evidence: DBC node names corroborated by the public 2015 Hyundai C-CAN
  DBC node documentation (EMS/TCU/ESC/IBOX/SMK/SCC) [B]; matches the
  Hyundai brief's C-CAN description [B]
- Missing: SMK (smart key) as a sender; CGW gateway node present in BU_
  list but sends nothing in this capture

### hyundai_2015_mcan
- Platform: Hyundai 2015 — M-CAN (multimedia/body)
- Make: hyundai
- Bus: M-CAN — bitrate and DLC exposure UNCONFIRMED [?] (treated as
  interior-only per the Hyundai brief)
- Modules (DBC BU_ nodes): HU_TMU (head unit / telematics), AMP
  (amplifier), MON (monitor/display), SWRC (steering-wheel remote),
  CLOCK, HUD, DATC, CCP, IBOX, CLU, CGW, AVM, plus RSE (rear-seat
  entertainment), IPM, KBD
- Grade: [B] for module list, [C] for bus assignment
- Evidence: DBC node names are body/multimedia modules [B]; M-CAN
  bitrate/pins unconfirmed per the Hyundai brief [?]
- Missing: exact gateway routing between C-CAN and M-CAN; M-CAN bitrate

### hyundai_i30_2014
- Platform: Hyundai i30 2014 — C-CAN
- Make: hyundai
- Bus: C-CAN, 500 kbps, pins 6/14 — inferred [C]
- Modules (inferred from message names): EMS (EMS_DCT1/2, EMS_H2, EMS6),
  TCS (TCS1/5), ESP (ESP2), VSM (VSM1/2), YRS (yaw-rate sensor)
- Grade: [C]
- Evidence: message names only; consistent with C-CAN powertrain/chassis
  content [C]
- Missing: BCM, TCU as named nodes

### hyundai_santafe_2007
- Platform: Hyundai Santa Fe 2007 — CAN (early)
- Make: hyundai
- Bus: C-CAN, 500 kbps, pins 6/14 — inferred [C] (2007 is early in
  Hyundai's CAN rollout; 2008 was a transition year per the brief)
- Modules (DBC BU_ nodes): ECU, TCU, ESP, SAS (steering-angle sensor),
  ABS, AWD
- Grade: [B]
- Evidence: DBC node names are the classic early-CAN module set [B]
- Missing: BCM, airbag, cluster

---

## Nissan / Infiniti

### nissan_xterra_2011
- Platform: Nissan Xterra 2011 — main CAN
- Make: nissan
- Bus: main CAN, 500 kbps, pins 6/14
- Modules (inferred from message names — BU_ is placeholder XXX):
  ENGINE (ENGINE_1–7), TCU (TCU_1), ABS (ABS_1/2), BCM, SPEED,
  STEERING
- Grade: [B]
- Evidence: message names match the Nissan brief's main-CAN module set
  (ECM, TCM, ABS, BCM, IPDM) [B]
- Missing: IPDM E/R, combination meter, 4WD/transfer modules; AV-CAN
  (pins 3/11) not captured; only 15 messages total — thinnest DBC in the
  database

---

## Coverage notes

- Thinnest platforms (module derivation mostly [C]): gm_global_a_object,
  gm_global_a_powertrain_expansion, FORD_CADS/_64, ford_fusion_2018_adas,
  chrysler_pacifica_2017_hybrid_private_fusion (opaque message names),
  toyota_adas, toyota_tss2_adas, toyota_radar_dsu_tssp, toyota_iQ_2009_can,
  vw_pq, hyundai_i30_2014, nissan_xterra_2011 (15 messages).
- DBCs whose BU_ node list is the placeholder XXX (module names inferred
  from message names only): all Ford CGEA/Fusion DBCs, chrysler_cusw,
  chrysler_pacifica private fusion, toyota_adas/tss2_adas/iQ, vw_pq,
  hyundai_i30_2014, nissan_xterra_2011.
- Systematic gap: no DBC in the set captures a body/comfort bus as seen
  at the DLC (GM SWCAN DBCs are body-ish but BCM itself never appears as
  a named node; Honda B-CAN, VW convenience CAN, and Nissan AV-CAN have
  no DBC coverage at all).
- Gateway dominance pattern: on Toyota (CGW 113/143 msgs), VW
  (Gateway_MQB 35/113, Gateway_D4C7 61/145), and Ford
  (GWM 127/331), the gateway ECU is the top sender — these DBCs capture
  gateway-forwarded/bridged traffic, not raw single-bus traffic. Treat
  module-to-bus assignments on those platforms as "as seen through the
  gateway" [B], not as physical bus membership [?].
- Private/ADAS buses (Ford ADAS, Toyota TSS camera/radar, GM object bus,
  Pacifica private fusion) are not DLC-reachable on any make in this
  set; M2 access requires a direct harness tap behind the relevant
  module or gateway.
