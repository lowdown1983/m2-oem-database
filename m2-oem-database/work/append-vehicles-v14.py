#!/usr/bin/env python3
"""Append v1.4.0 harvest entries to source/vehicles.yaml, matching v1.1.0 style."""
import json


def q(s):
    """Single-quote a string if it needs it (matches existing file style)."""
    s = str(s)
    if s == "" or any(c in s for c in ":#'\"{}[],&*!|><%@`") or s != s.strip():
        return "'" + s.replace("'", "''") + "'"
    return s


def num(f):
    if f == int(f):
        return f"{f:.1f}"
    return repr(f)


out = []
harvest = json.load(open("/home/hatch/workspace/m2-oem-database/work/opendbc-harvest-v14.json"))
for make in ["subaru", "mazda", "bmw", "mercedes", "volvo"]:
    for e in harvest[make]:
        out.append(f"- make: {e['make']}")
        out.append(f"  dbc: {e['dbc']}")
        out.append(f"  platform: {q(e['platform'])}")
        out.append(f"  vehicles_note: {q(e['vehicles_note'])}")
        out.append(f"  message_count: {e['message_count']}")
        out.append(f"  signal_count: {e['signal_count']}")
        out.append(f"  grade: {e['grade']}")
        out.append(f"  evidence: {q(e['evidence'])}")
        out.append(f"  messages:")
        for m in e["messages"]:
            out.append(f"  - id_dec: {m['id_dec']}")
            out.append(f"    id_hex: '{m['id_hex']}'")
            out.append(f"    name: {q(m['name'])}")
            out.append(f"    dlc: {m['dlc']}")
            out.append(f"    signals:")
            for s in m["signals"]:
                out.append(f"    - name: {q(s['name'])}")
                out.append(f"      start_bit: {s['start_bit']}")
                out.append(f"      length: {s['length']}")
                out.append(f"      byte_order: {s['byte_order']}")
                out.append(f"      signed: {'true' if s['signed'] else 'false'}")
                out.append(f"      factor: {num(s['factor'])}")
                out.append(f"      offset: {num(s['offset'])}")
                out.append(f"      unit: {q(s['unit'])}")

path = "/home/hatch/workspace/m2-oem-database/source/vehicles.yaml"
with open(path) as f:
    content = f.read()
if not content.endswith("\n"):
    content += "\n"
with open(path, "w") as f:
    f.write(content + "\n".join(out) + "\n")
print(f"appended {sum(len(v) for v in harvest.values())} entries")
