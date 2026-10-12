# M2 Firmware x Big-Three Compatibility Matrix (DRAFT)

**Status:** DRAFT cross-reference — derived 2026-10-06, NOT part of the validated
OEM database build. Promoting anything from here into the firmware docs or the
database source YAMLs needs Marcus's approval per his artifact-edit preference.

**Sources:** `~/workspace/m2-oem-database/source/makes.yaml`,
`~/workspace/m2-oem-database/source/diagnostics.yaml`,
`~/workspace/m2-oem-database/work/ford.md` (esp. point 7, IFR requirement),
`~/workspace/m2-superb-firmware/src/m2/j1850.cpp|h`,
`~/workspace/m2-superb-firmware/src/m2/mode_elm.cpp`.
Hardware claims below inherit the knowledge pack's evidence bar; every
hardware-touching behavior is INFERRED until vehicle-tested (no bench).

## Headline finding (new, from today's cross-check)

**Ford SCP (J1850 PWM, pre-~2004): the J1850 driver cannot receive module
replies.** Ford's SCP variant REQUIRES In-Frame Response bytes — the target
answers inside the same frame, right after EOD, with no SOF
(`work/ford.md` point 7 [B]; `makes.yaml` ford m2_mapping). But:

- `j1850.cpp:130` (vpwEdge): `if (diff >= VPW_RX_EOD_MIN) { endFrameIsr(); return; }`
  with the comment `// EOD (+IFR ignored)` — IFR bytes are deliberately dropped.
- `pwmEdge` is SOF-gated (needs a 40-56us active pulse); IFR bytes have no SOF,
  so after `pwmTransmit` re-attaches the ISR, the module's IFR reply is
  invisible.
- `transact()` then waits for a separate CRC-valid response frame that never
  arrives and returns false; ELM mode's `obdJ1850` (`mode_elm.cpp:184-202`)
  replies `NO DATA`.

Net: on a pre-2004 Ford SCP vehicle, `0100` auto-detect over J1850 PWM and any
ELM OBD-II query via `transact()` fail, while ATMA-style monitoring
(`pollFrame`) still shows whole frames *including* their IFR bytes. GM VPW and
Chrysler PCI are unaffected — neither uses IFR. Fix shape (for Marcus's call):
extend `pwmEdge` to keep capturing symbols after EOD while the bus stays active
within the frame, and let `transact()` accept the extended frame.

## GM (Chevrolet / Buick / GMC / Cadillac)

| Firmware mode | What works | Watch-out |
|---|---|---|
| M2RET / ELM / STN | HS GMLAN (6/14, 500k) full; CAN1 on mid-speed GMLAN (3/11) | Mid-speed bitrate is model-dependent: 95.2 or 125 kbps (grade A/B conflict in `makes.yaml`) |
| UDS | 11-bit USDT $7E0-$7E7 / $7E8-$7EF (ECM = ECU #1); functional $7DF | Modern GM: NO public seed/key algorithm — 0x27 stub holds; reads + user-supplied key only |
| OBD-II poller | Legislated modes on HS bus | — |
| J1850 VPW (1996-~2007) | VPW mode (pin 50 LOW); no IFR in GM — driver OK | Phase-in 2004-2008: a 2005 can be VPW or CAN — auto-detect, don't trust the year |
| SWCAN | Pin 1, 33.33k; `setupSW(33)` normal, `setupSW(83)` flash | Sleeping nodes need HV wake-up `mode(2)` BEFORE expecting replies |
| MITM | CAN0<->CAN1 bridges HS<->mid-speed GMLAN | CAN-only by design (TC7 collision rules out J1850/SWCAN bridging); "stealth" = never originate frames (CAN ACK is physical-layer) |
| Programming | — | Needs SPS2/dealer tool for modern GM; no key = no writes (firmware policy: no invented algorithms, ever) |

## Ford / Lincoln / Mercury

| Firmware mode | What works | Watch-out |
|---|---|---|
| M2RET / ELM / STN | HS-CAN (6/14, 500k) AND MS-CAN (3/11, 125k) **simultaneously** on CAN0/CAN1 | Signature M2 advantage: a switched ELM327 sees one bus at a time — the M2 doesn't. MS-CAN is not on all Fords: probe, don't assume |
| UDS | 0x7E0->0x7E8 "+8" addressing (PCM 0x7E0, GWM 0x726, etc.) | PATS: 0x27 without key returns NRC 0x35; timed access (10-12 min) can't be emulated by homebrew — FORScan owns this |
| OBD-II poller | Legislated modes on HS-CAN | — |
| J1850 PWM / SCP (1996-~2004) | — | **IFR gap (see headline):** `transact()` gets NO DATA on SCP until IFR RX is implemented. Monitor mode still works. IFR bytes are also required if the M2 ever *answers* as an SCP node |
| LIN1/LIN2 | Body/climate sub-buses if tapped at the module | — |
| CAN FD (2021+ F-150, Mach-E, etc.) | NOTHING | TJA1051 is CAN 2.0 only — out of scope for M2 CAN participation |
| Programming | — | No public Ford seed/key; as-built edits are FORScan's domain |

## Stellantis (Chrysler / Dodge / Jeep / RAM / Fiat / Alfa)

| Firmware mode | What works | Watch-out |
|---|---|---|
| M2RET / ELM / STN / OBD-II poller | CAN-C1 (6/14, 500k): reads work through the SGW on 2018+ (DTCs, live data, version info) | 2018+ SGW BLOCKS writes through the DLC: 0x14/0x2E/0x2F/0x31, DTC clear, actuations, programming. Legitimate paths: AutoAuth ($50/yr shop), wiTECH 2.0, or physical 12+8 bypass on your own vehicle. NO DIY AutoAuth path for a homebrew tool |
| UDS | Reads (0x19, 0x22) through SGW | Writes blocked (see above). Pre-2018 (FCM/CGW era): no SGW — full path |
| J1850 VPW / PCI (1999-~2005) | VPW mode; no IFR — driver OK | — |
| K-line (1996-~2004, pin 7) | M2 K-line transceiver (TJA1027) | — |
| MITM | CAN0<->CAN1 | Needs two physical buses; CAN-C2 (12/13) is model-dependent, CAN-BH (3/11) is NOT reachable with stock M2 (both native controllers spoken for; MCP2515 is tied to SWCAN) — would need an external CAN transceiver on SPI |
| CCD (1988-~1998) | NOTHING | No M2 hardware — proprietary 2-wire bus; trap: pins 3/11 were later recycled for CAN-BH |
| SCI / J2610 (90s-early 2000s PCM/TCM flash) | NOTHING | No M2 hardware — UART-based proprietary serial |
| Programming | — | No public FCA seed/key or SGW bypass — 0x27 stub policy holds. Strategy: read-only logging through SGW, or physical bypass on your own vehicle |

## Cross-cutting (already true of the firmware)

- MITM is CAN-only this phase — the TC7 collision rules out J1850/SWCAN
  bridging (Phase 4 design call).
- Programming mode keeps the 3 interlocks, voltage attestation, and the
  permanent no-seed/key-algorithm policy (`docs/SAFETY_REVIEW.md`).
- Every J1850 timing in the driver is INFERRED (GPIO+micros RX, TC6/TC7
  deliberately unclaimed) — the Ford IFR fix included — until vehicle-tested.
