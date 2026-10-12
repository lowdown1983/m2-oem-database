#!/usr/bin/env python3
"""Harvest v1.4.0 DBCs (5 new makes) into the vehicles.yaml entry format.

Mechanical harvest from commaai/opendbc @ a7da786. Handles indented BO_
lines (the v1.1.0 parser bug that skipped F_Vision_Obj_Track_12 and
F_Vision_Environment_3). Output: work/opendbc-harvest-v14.json (provenance)
and stdout YAML fragment for appending to source/vehicles.yaml.
"""
import json
import re
import sys

BO_RE = re.compile(r"^\s*BO_\s+(\d+)\s+(\w+)\s*:\s*(\d+)")
SG_RE = re.compile(
    r"^\s*SG_\s+(\w+)\s*(?:M|m\d*[Mm])?\s*:\s*(\d+)\|(\d+)@([01])([+-])"
    r"\s*\(\s*([^,]+?)\s*,\s*([^\)]+?)\s*\)[^\"]*\"([^\"]*)\""
)

# (make, dbc stem, platform, vehicles_note) — vehicle-specific DBCs only,
# generator templates (_subaru_global etc.) excluded, matching v1.1.0.
TARGETS = [
    ("subaru", "opendbc/dbc/generator/subaru/subaru_forester_2017.dbc",
     "Subaru Global Platform", "Forester 2017; Subaru Global Platform underpins 2017+ models"),
    ("subaru", "opendbc/dbc/generator/subaru/subaru_global_2017.dbc",
     "Subaru Global Platform", "Global-platform reference capture, 2017"),
    ("subaru", "opendbc/dbc/generator/subaru/subaru_global_2020_hybrid.dbc",
     "Subaru Global Platform", "Global-platform hybrid reference capture, 2020"),
    ("subaru", "opendbc/dbc/generator/subaru/subaru_outback_2015.dbc",
     "Subaru SJ platform", "Outback 2015 (pre-global SJ platform)"),
    ("subaru", "opendbc/dbc/generator/subaru/subaru_outback_2019.dbc",
     "Subaru Global Platform", "Outback 2019 (global platform)"),
    ("mazda", "opendbc/dbc/mazda_2017.dbc",
     "Mazda SkyActiv", "Mazda reference capture, 2017 (SkyActiv era)"),
    ("mazda", "opendbc/dbc/mazda_3_2019.dbc",
     "Mazda SkyActiv-Vehicle Architecture", "Mazda3 2019 (SkyActiv-Vehicle Architecture)"),
    ("mazda", "opendbc/dbc/mazda_radar.dbc",
     "Mazda SkyActiv", "Mazda radar/ADAS bus capture"),
    ("mazda", "opendbc/dbc/mazda_rx8.dbc",
     "Mazda RX-8", "RX-8 (pre-SkyActiv, rotary)"),
    ("bmw", "opendbc/dbc/bmw_e9x_e8x.dbc",
     "BMW E9x/E8x", "3-series E9x / 1-series E8x (pre-Fxx, PT-CAN/K-CAN era)"),
    ("mercedes", "opendbc/dbc/mercedes_benz_e350_2010.dbc",
     "Mercedes W212", "E350 2010 (W212)"),
    ("volvo", "opendbc/dbc/volvo_v40_2017_pt.dbc",
     "Volvo V40", "V40 2017 powertrain bus"),
    ("volvo", "opendbc/dbc/volvo_v60_2015_pt.dbc",
     "Volvo V60", "V60 2015 powertrain bus"),
]

BASE = "/home/hatch/workspace/m2-oem-database/work/opendbc"
EVIDENCE_TMPL = "opendbc/%s (commaai/opendbc @ a7da786, shallow clone 2026-10-06)"


def parse_dbc(path):
    messages = []
    cur = None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = BO_RE.match(line)
            if m:
                id_dec = int(m.group(1))
                cur = {
                    "id_dec": id_dec,
                    "id_hex": hex(id_dec),
                    "name": m.group(2),
                    "dlc": int(m.group(3)),
                    "signals": [],
                }
                messages.append(cur)
                continue
            s = SG_RE.match(line)
            if s and cur is not None:
                cur["signals"].append({
                    "name": s.group(1),
                    "start_bit": int(s.group(2)),
                    "length": int(s.group(3)),
                    "byte_order": "motorola" if s.group(4) == "0" else "intel",
                    "signed": s.group(5) == "-",
                    "factor": float(s.group(6)),
                    "offset": float(s.group(7)),
                    "unit": s.group(8),
                })
    return messages


def main():
    harvest = {}
    total_msg = 0
    total_sig = 0
    for make, rel, platform, note in TARGETS:
        stem = rel.split("/")[-1].replace(".dbc", "")
        msgs = parse_dbc(f"{BASE}/{rel}")
        sig_count = sum(len(m["signals"]) for m in msgs)
        total_msg += len(msgs)
        total_sig += sig_count
        entry = {
            "make": make,
            "dbc": stem,
            "platform": platform,
            "vehicles_note": note,
            "message_count": len(msgs),
            "signal_count": sig_count,
            "grade": "B",
            "evidence": EVIDENCE_TMPL % rel,
            "messages": msgs,
        }
        harvest.setdefault(make, []).append(entry)
        print(f"{make}/{stem}: {len(msgs)} msgs, {sig_count} sigs", file=sys.stderr)
    with open("/home/hatch/workspace/m2-oem-database/work/opendbc-harvest-v14.json", "w") as f:
        json.dump(harvest, f, indent=1)
    print(f"TOTAL: {total_msg} messages, {total_sig} signals", file=sys.stderr)


if __name__ == "__main__":
    main()
