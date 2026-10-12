# Ford as-built reference

Format: `MODULE-BLOCK-LINE` (e.g. `7D0-01-01`), space-separated 4-hex-digit groups, trailing group = checksum (FORScan auto-computes). As-built = Ford's per-VIN factory record (motorcraftservice.com/AsBuilt) reflecting the latest calibration. Reads = UDS 0x22, writes = 0x2E; module addresses double as UDS request IDs (+8 convention). **Back up every module (.abt) before any write.**

| Address | Module | Blocks | Grade | Notes |
|---|---|---|---|---|
| 701 | Global Positioning Sensor Module (GPSM) | — | [B] | Deprecated module; replaced by SYNC 3 and the new GPS antenna. No longer used. |
| 706 | Image Processing Module A (IPMA) — forward driving assist, lane keeping/departure warning (Gentex or Mobileye) | — | [B] | — |
| 712 | Seat Control Module G (SCMG) — driver lumbar and massage control | — | [B] | — |
| 713 | Seat Control Module H (SCMH) — passenger lumbar and massage control | — | [B] | — |
| 714 | Heated Steering Wheel Module (HSWM) | — | [B] | — |
| 716 | Gateway Module A (GWM) | — | [B] | Gateway itself carries no user-configurable as-built lines. |
| 720 | Instrument Panel Cluster (IPC) | 720-01-01, 720-01-02, 720-01-03, 720-04-01, 720-07-01 | [B] | Cluster configuration: chimes, displayed temps, trailer-brake gain display, quick-boot. See §4 for well-known blocks. |
| 721 | Vehicle Dynamics Module (VDM) | — | [B] | 2020MY+ only. |
| 724 | Steering Column Control Module (SCCM) — steering wheel adjustments, switches, turn signals | — | [B] | — |
| 725 | Wireless Accessory Charging Module (WACM) | — | [B] | 2020MY+ only. |
| 726 | Body Control Module (BCM / BdyCM; "BCE" on the Motorcraft portal) | 726-01-01, 726-01-02, 726-08-01, 726-17-01, 726-21-01, 726-25-02, 726-28-02, 726-30-01, 726-37-01, 726-41-02, 726-42-01, 726-48-02 | [B] | The most-modified module in the FORScan community. VIN stored at 726-09-01 through 726-11-01 (16-19MY). See §4 for well-known blocks. |
| 727 | Audio Control Module (ACM) — radio module / CD player, Sirius | — | [B] | MS-CAN module on many platforms. |
| 730 | Power Steering Control Module (PSCM) — Nexteer unit on 2017MY+ | — | [B] | Contains a wheel-size field. Listed without address in the FORScan setup-guide table; address confirmed in the Explorer 11-23MY listing. |
| 731 | Remote Function Actuator (RFA) | — | [B] | 2011-2015MY only. |
| 732 | Gear Shift Module (GSM) | — | [B] | 2020MY-23MY only. |
| 733 | HVAC — Heating, Ventilation, Air Conditioning | — | [B] | Address 733 was EATC (Electronic Automatic Temperature Control) on 2011-2015MY — same address, renamed module. VIN stored at 733-02-01 through 733-02-04. |
| 736 | Parking Assist Control Module (PAM) | — | [B] | As-built change recommended for SYNC 2 → SYNC 3 upgrades. |
| 737 | Restraint Control Module (RCM) — airbags, seatbelts | — | [B] | Contains seat/seatbelt configuration data. RCM as-built also appears on the Motorcraft portal (737-01-01 example lines). |
| 740 | Driver Door Module (DDM) | — | [B] | — |
| 741 | Passenger Door Module (PDM) | — | [B] | — |
| 744 | Driver Seat Module (DSM) | — | [C] | — |
| 751 | Radio Transceiver Module (RTM) — also listed as tire-pressure monitor receiver in some sources | — | [B] | — |
| 757 | Trailer Brake Control Module (TBM / TBC) | — | [B] | — |
| 760 | Anti-Lock Brake System (ABS) | — | [B] | 2011-2015 Explorer/Police Utility lists show ABS at 76D — address is model-year/platform dependent; 760 is the current address [conflict reported, resolved by recency]. |
| 761 | Transfer Case Control Module (TCCM) | — | [B] | — |
| 764 | Cruise Control Module (CCM) | — | [B] | — |
| 766 | Running Board Control Module (RBM) | — | [B] | — |
| 776 | Seat Control Module E (SCME) | — | [C] | — |
| 783 | Audio Digital Signal Processing Module (DSP) | — | [B] | — |
| 791 | Trailer Module (TRM) | — | [B] | — |
| 7A5 | Front Control/Display Interface Module (FCDIM) | — | [B] | Some modules in this family (FDIM) require UDS 0x27 Security Access to modify VIN in as-built data [B — FG-Falcon VIN guide]. |
| 7A7 | Front Controls Interface Module (FCIM) | — | [B] | 2011-2015 Explorer/Police Utility lists show FCIM at 75A — address is model-year/platform dependent; 7A7 is the current address [conflict reported, resolved by recency]. |
| 7B1 | Image Processing Module B (IPMB) — reverse camera module | — | [B] | — |
| 7B2 | Heads-Up Display (HUD) | — | [B] | — |
| 7C4 | Side Obstacle Detection Control Module, Left (SODL) | — | [B] | — |
| 7C6 | Side Obstacle Detection Control Module, Right (SODR) | — | [B] | — |
| 7D0 | Accessory Protocol Interface Module (APIM) — SYNC module | 7D0-01-01, 7D0-01-02, 7D0-02-01, 7D0-03-01, 7D0-04-02, 7D0-09-02 | [B] | The SYNC configuration hub: audio sources, DSP, camera, themes, nav-in-motion. Block 8-9 not available on SYNC 3.0 [C — scribd Explorer guide]. See §4. |
| 7D5 | Digital Audio Control Module C (DACMC) | — | [B] | — |
| 7D7 | GSM alternate — NOT VERIFIED. The brief listed 7D7 as a candidate address, but no source in this pass confirms a module at 7D7; the Explorer 11-23MY listing places the Gear Shift Module at 732 (2020MY+). Treat 7D7 as unverified [?]. | — | [C] | Do not use without on-vehicle verification. |
| 7E0 | Powertrain Control Module (PCM) | — | [B] | Primary powertrain module; UDS request ID 7E0 → response 7E8 (+8 convention). |
| 7E1 | Transmission Control Module (TCM) | — | [B] | Address confirmed by two independent FORScan community sources; one setup-guide copy truncates it as "70" (transcription artifact, not a distinct address) [conflict reported, resolved]. |

_Generated by scripts/build.py — do not hand-edit._
