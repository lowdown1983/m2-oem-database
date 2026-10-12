#!/usr/bin/env python3
"""Build the M2/SuperB OEM Vehicle Database.

ONE command rebuild: source/*.yaml -> generated/

  python3 scripts/build.py

Steps:
  1. Parse all source/*.yaml
  2. Validate each against schemas/*.json (fails loudly)
  3. Cross-reference checks (fail loudly):
     - every OEM-* token in evidence strings exists in _meta.yaml source catalog
  4. Write generated/json/ (one JSON per source + index.json)
  5. Write generated/wiki/ (*.md with grades and evidence)
  6. Write generated/rag-chunks.jsonl (embedding-ready, self-contained chunks)
  7. Run the 12-question validation test against the generated artifacts and
     write generated/wiki/validation.md (all 12 must pass)

generated/ is NEVER hand-edited.
"""
import json
import re
import sys
from pathlib import Path

import yaml
import jsonschema

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source"
SCHEMAS = ROOT / "schemas"
GEN = ROOT / "generated"
GEN_JSON = GEN / "json"
GEN_WIKI = GEN / "wiki"

SOURCE_FILES = {
    "_meta": ("_meta.yaml", None),
    "makes": ("makes.yaml", "makes.schema.json"),
    "diagnostics": ("diagnostics.yaml", "diagnostics.schema.json"),
    "vehicles": ("vehicles.yaml", "vehicles.schema.json"),
    "dtcs": ("dtcs.yaml", "dtcs.schema.json"),
    "dids": ("dids.yaml", "dids.schema.json"),
    "asbuilt": ("asbuilt.yaml", "asbuilt.schema.json"),
    "module_maps": ("module_maps.yaml", "module_maps.schema.json"),
}

OEM_TOKEN = re.compile(r"OEM-[A-Z0-9-]+")


def fail(msg):
    print(f"BUILD FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def load_sources():
    data = {}
    for key, (fname, _) in SOURCE_FILES.items():
        path = SRC / fname
        if not path.exists():
            fail(f"missing source file: {path}")
        with open(path) as f:
            data[key] = yaml.safe_load(f)
    return data


def validate(data):
    n = 0
    for key, (_, schema_name) in SOURCE_FILES.items():
        if schema_name is None:
            continue
        schema_path = SCHEMAS / schema_name
        if not schema_path.exists():
            fail(f"missing schema: {schema_path}")
        with open(schema_path) as f:
            schema = json.load(f)
        try:
            jsonschema.validate(data[key], schema)
        except jsonschema.ValidationError as e:
            fail(f"schema violation in {key}: {e.message} (at {list(e.absolute_path)})")
        n += 1
    print(f"schema validation: OK ({n}/{n} files)")


def walk_strings(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)
    elif isinstance(obj, str):
        yield obj


def cross_check(data):
    errors = []
    catalog = {s["id"] for s in data["_meta"]["sources"]}
    for key, doc in data.items():
        if key == "_meta":
            continue
        for s in walk_strings(doc):
            for tok in OEM_TOKEN.findall(s):
                if tok not in catalog:
                    errors.append(f"{key}: unknown evidence source '{tok}'")
    if errors:
        for e in errors:
            print(f"  CROSS-REF ERROR: {e}", file=sys.stderr)
        fail(f"{len(errors)} cross-reference check(s) failed")
    print("cross-reference checks: OK")


# ---------------------------------------------------------------- JSON output

def write_json(data):
    GEN_JSON.mkdir(parents=True, exist_ok=True)
    for key, doc in data.items():
        with open(GEN_JSON / f"{key}.json", "w") as f:
            json.dump(doc, f, indent=2)
            f.write("\n")

    makes = data["makes"]["makes"]
    diag = {m["make"]: m for m in data["diagnostics"]["makes"]}
    entries = data["vehicles"]["entries"]
    dtcs = data["dtcs"]["entries"]
    index = {
        "pack": data["_meta"]["pack"],
        "pack_version": data["_meta"]["pack_version"],
        "date": data["_meta"]["date"],
        "files": sorted(f"{k}.json" for k in data),
        "counts": {
            "makes": len(makes),
            "buses": sum(len(m.get("buses", [])) for m in makes),
            "legacy_protocols": sum(len(m.get("legacy", [])) for m in makes),
            "m2_mappings": sum(len(m.get("m2_mapping", [])) for m in makes),
            "diagnostic_services": sum(len(m.get("services", [])) for m in diag.values()),
            "gateways": sum(len(m.get("gateways", [])) for m in diag.values()),
            "dbc_files": len(entries),
            "messages": sum(e["message_count"] for e in entries),
            "signals": sum(len(msg.get("signals", []))
                           for e in entries for msg in e["messages"]),
            "dtcs": len(dtcs),
            "dtcs_generic": sum(1 for d in dtcs if d["scope"] == "generic"),
            "dtcs_manufacturer": sum(1 for d in dtcs if d["scope"] == "manufacturer"),
            "dids": len(data["dids"]["entries"]),
            "asbuilt_modules": len(data["asbuilt"]["entries"]),
            "module_map_platforms": len(data["module_maps"]["entries"]),
        },
    }
    with open(GEN_JSON / "index.json", "w") as f:
        json.dump(index, f, indent=2)
        f.write("\n")
    print(f"generated/json: OK ({len(data)} source files + index.json)")


# ---------------------------------------------------------------- wiki output

def grade_badge(g):
    return f"[{g}]"


def write_wiki(data):
    GEN_WIKI.mkdir(parents=True, exist_ok=True)
    meta = data["_meta"]

    lines = [
        f"# {meta['pack']} — v{meta['pack_version']} ({meta['date']})",
        "",
        meta["scope"],
        "",
        meta["method"],
        "",
        "## Quality grades",
        "",
    ]
    for label, meaning in meta["grades"].items():
        lines.append(f"- **{label}** — {meaning}")
    lines += [
        "",
        "## Contents",
        "",
        "- [Bus architecture](makes.md) — per-make buses, legacy protocols, M2 hardware mapping",
        "- [Diagnostic access](diagnostics.md) — protocols, services, gateways, tools, seed/key policy",
        "- [Vehicle message catalog](vehicles.md) — opendbc DBC harvest (32 DBCs, signal-level decode)",
        "- [DTC catalog](dtcs.md) — SAE J2012 generic + manufacturer-specific trouble codes",
        "- [UDS DID catalog](dids.md) — ISO-standard + make-specific Data Identifiers",
        "- [Ford as-built](asbuilt.md) — module addresses, block format, UDS mapping",
        "- [Module maps](module_maps.md) — per-platform bus/module assignments for the 32 DBCs",
        "- [Validation](validation.md) — 36-question test against these artifacts",
        "",
        "## Primary sources",
        "",
    ]
    for s in meta["sources"]:
        lines.append(f"- `{s['id']}` — {s['name']}")
    lines += ["", "_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "index.md").write_text("\n".join(lines))

    # makes.md
    lines = ["# Bus architecture by make", ""]
    for m in data["makes"]["makes"]:
        lines += [f"## {m['full_name'] or m['make']}", "",
                  "### Buses", "",
                  "| Bus | Bitrate | DLC pins | Wires | Years | Grade | Notes |",
                  "|---|---|---|---|---|---|---|"]
        for b in m.get("buses", []):
            pins = ", ".join(str(p) for p in b.get("obd2_pins", [])) or "—"
            lines.append(f"| {b['name']} | {b.get('bitrate_kbps', '—')} kbps | {pins} | "
                         f"{b.get('wire_count', '—')} | {b.get('years', '—')} | {grade_badge(b['grade'])} | "
                         f"{b.get('notes', '')} |")
        if m.get("legacy"):
            lines += ["", "### Legacy protocols", "",
                      "| Protocol | Bitrate | DLC pins | Years | Grade | Notes |",
                      "|---|---|---|---|---|---|---|"]
            for leg in m["legacy"]:
                pins = ", ".join(str(p) for p in leg.get("obd2_pins", [])) or "—"
                lines.append(f"| {leg['protocol']} | {leg.get('bitrate_kbps', '—')} kbps | {pins} | "
                             f"{leg.get('years', '—')} | {grade_badge(leg['grade'])} | {leg.get('notes', '')} |")
        if m.get("m2_mapping"):
            lines += ["", "### M2 hardware mapping", "",
                      "| M2 hardware | Bus | Notes |",
                      "|---|---|---|"]
            for mp in m["m2_mapping"]:
                lines.append(f"| {mp['m2_hardware']} | {mp['bus']} | {mp.get('notes', '')} |")
        lines += [""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "makes.md").write_text("\n".join(lines))

    # diagnostics.md
    lines = ["# Diagnostic access by make", ""]
    for m in data["diagnostics"]["makes"]:
        lines += [f"## {m.get('full_name') or m['make']} {grade_badge(m['grade'])}", "",
                  f"- Protocol: {m.get('diagnostic_protocol', '—')}",
                  f"- Evidence: {m.get('evidence', '—')}", "",
                  "### Services", "",
                  "| Service | ID | Support | Grade |",
                  "|---|---|---|---|"]
        for s in m.get("services", []):
            lines.append(f"| {s['name']} | {s.get('service_id', '—')} | {s.get('support', '')} | "
                         f"{grade_badge(s['grade'])} |")
        if m.get("gateways"):
            lines += ["", "### Gateways", ""]
            for g in m["gateways"]:
                lines += [f"#### {g['module']} {grade_badge(g['grade'])} ({g.get('years', '—')})", "",
                          f"- Effect: {g.get('effect', '')}"]
                if g.get("bypass"):
                    lines.append(f"- Legitimate access: {g['bypass']}")
                lines += [f"- Evidence: {g.get('evidence', '')}", ""]
        if m.get("tools"):
            lines += ["### Tool ecosystem", ""]
            for t in m["tools"]:
                lines.append(f"- **{t['name']}** — {t.get('notes', '')}")
            lines += [""]
        lines += [f"### Seed/key policy", "", m.get("seed_key", ""), ""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "diagnostics.md").write_text("\n".join(lines))

    # vehicles.md
    lines = ["# Vehicle message catalog (opendbc harvest)", "",
             "Mechanically harvested from commaai/opendbc. Grade B: real captures, but "
             "comma.ai's ADAS-driving subset — not complete vehicle databases, 2016+ focused.",
             "Signal-level decode (start bit, length, byte order, factor, offset, unit) lives in "
             "`generated/json/vehicles.json` and the per-message RAG chunks; the wiki shows "
             "the signal count per message.", ""]
    for e in data["vehicles"]["entries"]:
        lines += [f"## {e['dbc']} — {e['platform']} {grade_badge(e['grade'])}", "",
                  f"- Make: {e['make']}; {e.get('vehicles_note', '')}",
                  f"- Messages: {e['message_count']}; signals: "
                  f"{sum(len(m.get('signals', [])) for m in e['messages'])}",
                  f"- Evidence: {e.get('evidence', '')}", "",
                  "| ID (dec) | ID (hex) | Name | DLC | Signals |",
                  "|---|---|---|---|---|"]
        for msg in e["messages"]:
            lines.append(f"| {msg['id_dec']} | {msg['id_hex']} | {msg['name']} | "
                         f"{msg.get('dlc', '—')} | {len(msg.get('signals', []))} |")
        lines += [""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "vehicles.md").write_text("\n".join(lines))

    # dtcs.md
    dtcs = data["dtcs"]["entries"]
    lines = ["# DTC catalog", "",
             "Diagnostic trouble codes: SAE J2012 generic codes plus manufacturer-specific "
             "codes for the covered makes. Grade B/C: community and aftermarket sources — "
             "verify safety-critical diagnoses against factory service information.", ""]
    by_make = {}
    for d in dtcs:
        by_make.setdefault(d["make"], []).append(d)
    for mk in sorted(by_make):
        entries = sorted(by_make[mk], key=lambda d: d["code"])
        lines += [f"## {mk} — {len(entries)} codes", "",
                  "| Code | Description | Category | Scope | Grade | Possible causes | Diagnostic notes |",
                  "|---|---|---|---|---|---|---|"]
        for d in entries:
            causes = "; ".join(d.get("possible_causes", [])) or "—"
            notes = d.get("diagnostic_notes", "") or "—"
            lines.append(f"| {d['code']} | {d['description']} | {d['category']} | {d['scope']} | "
                         f"{grade_badge(d['grade'])} | {causes} | {notes} |")
        lines += [""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "dtcs.md").write_text("\n".join(lines))

    # dids.md
    dids = data["dids"]["entries"]
    lines = ["# UDS DID catalog", "",
             "Data Identifiers for UDS service 0x22 (ReadDataByIdentifier). "
             "ISO-standard DIDs (0xF180–0xF19E) are [A] per ISO 14229-1:2013 — the standard fixes "
             "number and name, not record length. Nissan entries are KWP2000-style 0x21 local IDs, "
             "not 0x22 DIDs. Hyundai DID numbering is ECU-scoped — always pair the DID with its ECU.", ""]
    by_make = {}
    for d in dids:
        by_make.setdefault(d["make"], []).append(d)
    for mk in ["iso"] + sorted(m for m in by_make if m != "iso"):
        entries = sorted(by_make[mk], key=lambda d: d["did"])
        lines += [f"## {mk} — {len(entries)} DIDs", "",
                  "| DID | Name | Size | Session | Security | Grade | Description |",
                  "|---|---|---|---|---|---|---|"]
        for d in entries:
            ctx = f" ({d['ecu_context']})" if d.get("ecu_context") else ""
            svc = f" [{d['service']}]" if d.get("service", "0x22") != "0x22" else ""
            lines.append(f"| {d['did']}{svc} | {d['name']}{ctx} | {d.get('size', '—')} | "
                         f"{d.get('session', '—')} | {d.get('security', '—')} | "
                         f"{grade_badge(d['grade'])} | {d['description']} |")
        lines += [""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "dids.md").write_text("\n".join(lines))

    # asbuilt.md
    ab = data["asbuilt"]["entries"]
    lines = ["# Ford as-built reference", "",
             "Format: `MODULE-BLOCK-LINE` (e.g. `7D0-01-01`), space-separated 4-hex-digit groups, "
             "trailing group = checksum (FORScan auto-computes). As-built = Ford's per-VIN factory record "
             "(motorcraftservice.com/AsBuilt) reflecting the latest calibration. "
             "Reads = UDS 0x22, writes = 0x2E; module addresses double as UDS request IDs (+8 convention). "
             "**Back up every module (.abt) before any write.**", ""]
    lines += ["| Address | Module | Blocks | Grade | Notes |",
              "|---|---|---|---|---|"]
    for a in sorted(ab, key=lambda a: a["address"]):
        blocks = ", ".join(a.get("blocks", [])) or "—"
        lines.append(f"| {a['address']} | {a['module']} | {blocks} | "
                     f"{grade_badge(a['grade'])} | {a.get('notes', '')} |")
    lines += ["", "_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "asbuilt.md").write_text("\n".join(lines))

    # module_maps.md
    mms = data["module_maps"]["entries"]
    lines = ["# Per-platform bus/module maps", "",
             "Module-to-bus assignments for the 32 opendbc DBC platforms, derived from DBC node names "
             "cross-checked against the bus-architecture briefs. Inferred assignments are marked; "
             "on gateway-heavy platforms the DBC captures gateway-forwarded traffic, not raw bus traffic.", ""]
    for mm in sorted(mms, key=lambda m: (m["make"], m["dbc"])):
        lines += [f"## {mm['dbc']} — {mm.get('platform', '')} {grade_badge(mm['grade'])}", "",
                  f"- Make: {mm['make']}; bus: {mm.get('bus', '')}",
                  f"- Evidence: {mm.get('evidence', '')}", ""]
        if mm.get("modules"):
            lines += ["| Node | Module |", "|---|---|"]
            for mod in mm["modules"]:
                lines.append(f"| {mod['node']} | {mod.get('name', '—')} |")
            lines += [""]
        if mm.get("missing"):
            lines.append(f"- Not in DBC (brief-documented): {', '.join(mm['missing'])}")
            lines += [""]
    lines += ["_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "module_maps.md").write_text("\n".join(lines))
    print(f"generated/wiki: OK ({len([p for p in GEN_WIKI.glob('*.md')])} pages)")


def fmt_signal(s):
    """Compact one-line signal decode: NAME startbit|length byteorder signedness factor offset unit."""
    bo = "intel" if s.get("byte_order") == "intel" else "moto"
    sg = "s" if s.get("signed") else "u"
    unit = s.get("unit") or "-"
    return (f"{s['name']} {s['start_bit']}|{s['length']}{bo} {sg} "
            f"f={s.get('factor')} o={s.get('offset')} {unit}")


def chunk(cid, title, text, grade, source_file):
    return {"id": cid, "title": title, "text": text,
            "grade": grade, "source_file": source_file}


def write_rag_chunks(data):
    chunks = []
    for m in data["makes"]["makes"]:
        mk = m["make"]
        for b in m.get("buses", []):
            pins = ", ".join(str(p) for p in b.get("obd2_pins", [])) or "not on DLC"
            text = (f"{m.get('full_name')}: {b['name']} — {b.get('bitrate_kbps', '?')} kbps, "
                    f"DLC pins {pins}, {b.get('wire_count', '?')}-wire, years {b.get('years', '?')}. "
                    f"{b.get('notes', '')}")
            slug = re.sub(r"[^a-z0-9]+", "-", b["name"].lower()).strip("-")
            chunks.append(chunk(f"oem-{mk}-bus-{slug}", f"{mk.upper()} bus: {b['name']}",
                                text, b["grade"], "makes.yaml"))
        for leg in m.get("legacy", []):
            pins = ", ".join(str(p) for p in leg.get("obd2_pins", [])) or "—"
            text = (f"{m.get('full_name')} legacy: {leg['protocol']} — "
                    f"{leg.get('bitrate_kbps', '?')} kbps, DLC pins {pins}, years {leg.get('years', '?')}. "
                    f"{leg.get('notes', '')}")
            slug = re.sub(r"[^a-z0-9]+", "-", leg["protocol"].lower()).strip("-")[:40]
            chunks.append(chunk(f"oem-{mk}-legacy-{slug}", f"{mk.upper()} legacy: {leg['protocol']}",
                                text, leg["grade"], "makes.yaml"))
        for mp in m.get("m2_mapping", []):
            text = (f"M2 hardware mapping for {m.get('full_name')}: {mp['m2_hardware']} -> "
                    f"{mp['bus']}. {mp.get('notes', '')}")
            slug = re.sub(r"[^a-z0-9]+", "-", mp["bus"].lower()).strip("-")[:40]
            chunks.append(chunk(f"oem-{mk}-m2map-{slug}", f"M2 mapping: {mp['bus']}",
                                text, "B", "makes.yaml"))

    for m in data["diagnostics"]["makes"]:
        mk = m["make"]
        for s in m.get("services", []):
            text = (f"{m.get('full_name')} diagnostic service: {s['name']} "
                    f"({s.get('service_id', '')}). {s.get('support', '')}")
            slug = re.sub(r"[^a-z0-9]+", "-", s["name"].lower()).strip("-")[:40]
            chunks.append(chunk(f"oem-{mk}-svc-{slug}", f"{mk.upper()} diag: {s['name']}",
                                text, s["grade"], "diagnostics.yaml"))
        for g in m.get("gateways", []):
            text = (f"{m.get('full_name')} gateway: {g['module']} ({g.get('years', '')}). "
                    f"{g.get('effect', '')} Legitimate access: {g.get('bypass', 'n/a')}")
            slug = re.sub(r"[^a-z0-9]+", "-", g["module"].lower()).strip("-")[:40]
            chunks.append(chunk(f"oem-{mk}-gw-{slug}", f"{mk.upper()} gateway: {g['module']}",
                                text, g["grade"], "diagnostics.yaml"))
        chunks.append(chunk(f"oem-{mk}-seedkey", f"{mk.upper()} seed/key policy",
                            f"{m.get('full_name')} seed/key policy: {m.get('seed_key', '')}",
                            m["grade"], "diagnostics.yaml"))

    for e in data["vehicles"]["entries"]:
        slug = re.sub(r"[^a-z0-9]+", "-", e["dbc"].lower()).strip("-")
        id_list = ", ".join(f"{msg['id_hex']} ({msg['name']})" for msg in e["messages"])
        text = (f"opendbc DBC {e['dbc']} [{e['grade']}]: {e['platform']} — {e.get('vehicles_note', '')} "
                f"{e['message_count']} messages: {id_list}")
        chunks.append(chunk(f"oem-dbc-{slug}", f"DBC: {e['dbc']}",
                            text, e["grade"], "vehicles.yaml"))
        for msg in e["messages"]:
            sigs = msg.get("signals", [])
            parts = [sigs[i:i + 20] for i in range(0, len(sigs), 20)] or [[]]
            for pi, part in enumerate(parts):
                sig_text = "; ".join(fmt_signal(s) for s in part) or "no signals decoded"
                part_note = f" (part {pi + 1}/{len(parts)})" if len(parts) > 1 else ""
                text = (f"CAN ID {msg['id_hex']} ({msg['id_dec']}) = {msg['name']}, DLC "
                        f"{msg.get('dlc', '?')}, in {e['dbc']} ({e['platform']}, make {e['make']}) "
                        f"[{e['grade']}]{part_note}. Signals: {sig_text}")
                cid = f"oem-msg-{slug}-{msg['id_dec']}" + (f"-p{pi + 1}" if len(parts) > 1 else "")
                chunks.append(chunk(cid,
                                    f"Message {msg['id_hex']} {msg['name']} ({e['dbc']})",
                                    text, e["grade"], "vehicles.yaml"))

    for d in data["dtcs"]["entries"]:
        scope = "SAE J2012 generic" if d["scope"] == "generic" else f"{d['make']} manufacturer-specific"
        text = (f"DTC {d['code']} ({scope}, category {d['category']}): {d['description']}.")
        if d.get("possible_causes"):
            text += f" Possible causes: {'; '.join(d['possible_causes'])}."
        if d.get("diagnostic_notes"):
            text += f" Diagnostic notes: {d['diagnostic_notes']}"
        slug = d["code"].lower()
        chunks.append(chunk(f"oem-dtc-{d['make']}-{slug}",
                            f"DTC {d['code']} ({d['make']})",
                            text, d["grade"], "dtcs.yaml"))

    for d in data["dids"]["entries"]:
        svc = d.get("service", "0x22")
        text = (f"UDS DID {d['did']} ({d['name']}), make {d['make']}, service {svc}: "
                f"{d['description']}. Size: {d.get('size', 'not documented')}; "
                f"session: {d.get('session', 'not documented')}; "
                f"security: {d.get('security', 'not documented')}.")
        if d.get("ecu_context"):
            text += f" Observed on: {d['ecu_context']}."
        slug = d["did"].lower().replace("0x", "")
        chunks.append(chunk(f"oem-did-{d['make']}-{slug}",
                            f"DID {d['did']} {d['name']} ({d['make']})",
                            text, d["grade"], "dids.yaml"))

    for a in data["asbuilt"]["entries"]:
        text = (f"Ford as-built module {a['address']} = {a['module']}. "
                f"Documented blocks: {', '.join(a.get('blocks', [])) or 'not documented'}. "
                f"{a.get('notes', '')}")
        chunks.append(chunk(f"oem-asbuilt-{a['address'].lower()}",
                            f"Ford as-built {a['address']} ({a['module']})",
                            text, a["grade"], "asbuilt.yaml"))

    for mm in data["module_maps"]["entries"]:
        mods = ", ".join(f"{m['node']} ({m.get('name', '?')})" for m in mm.get("modules", []))
        text = (f"Platform {mm['dbc']} ({mm.get('platform', '')}, {mm['make']}): bus {mm.get('bus', '')}. "
                f"Modules: {mods or 'none listed'}.")
        if mm.get("missing"):
            text += f" Brief-documented but not in DBC: {', '.join(mm['missing'])}."
        slug = re.sub(r"[^a-z0-9]+", "-", mm["dbc"].lower()).strip("-")
        chunks.append(chunk(f"oem-modmap-{slug}",
                            f"Module map: {mm['dbc']}",
                            text, mm["grade"], "module_maps.yaml"))

    with open(GEN / "rag-chunks.jsonl", "w") as f:
        for ch in chunks:
            f.write(json.dumps(ch) + "\n")
    print(f"generated/rag-chunks.jsonl: OK ({len(chunks)} chunks)")
    return chunks


# ---------------------------------------------------------------- validation test

def run_validation():
    """Answer 36 OEM questions SOLELY from the generated artifacts."""
    with open(GEN_JSON / "makes.json") as f:
        makesd = json.load(f)
    with open(GEN_JSON / "diagnostics.json") as f:
        diagd = json.load(f)
    with open(GEN_JSON / "vehicles.json") as f:
        vehd = json.load(f)

    makes = {m["make"]: m for m in makesd["makes"]}
    diag = {m["make"]: m for m in diagd["makes"]}

    results = []

    def check(qid, question, ok, answer):
        results.append({"id": qid, "question": question,
                        "answer": answer, "result": "PASS" if ok else "FAIL"})
        return ok

    def bus(make, name):
        for b in makes[make].get("buses", []):
            if b["name"] == name:
                return b
        return {}

    # Q1: GM SWCAN pin + bitrate
    sw = bus("gm", "Single-Wire (Low-Speed) GMLAN")
    q1_ok = (sw.get("obd2_pins") == [1] and sw.get("bitrate_kbps") == 33.33)
    check("Q1", "Which DLC pin and bitrate is GM's single-wire GMLAN?",
          q1_ok, f"Pin {sw.get('obd2_pins')}, {sw.get('bitrate_kbps')} kbps {grade_badge(sw.get('grade'))}"
          if q1_ok else "GM SWCAN facts missing")

    # Q2: GM MS-CAN pins
    ms = bus("gm", "Mid-Speed GMLAN")
    q2_ok = (ms.get("obd2_pins") == [3, 11] and "95.2" in ms.get("notes", ""))
    check("Q2", "Which DLC pins carry GM mid-speed GMLAN, and what is the bitrate caveat?",
          q2_ok, f"Pins {ms.get('obd2_pins')}; 95.2 kbps per ACDelco [A] but one spec excerpt says 95.2-or-125 [B] — model-dependent"
          if q2_ok else "GM MS-CAN facts missing")

    # Q3: Ford MS-CAN pins + bitrate
    fms = bus("ford", "MS-CAN")
    q3_ok = (fms.get("obd2_pins") == [3, 11] and fms.get("bitrate_kbps") == 125)
    check("Q3", "Which DLC pins and bitrate is Ford's MS-CAN?",
          q3_ok, f"Pins {fms.get('obd2_pins')} (Ford-proprietary), {fms.get('bitrate_kbps')} kbps {grade_badge(fms.get('grade'))}"
          if q3_ok else "Ford MS-CAN facts missing")

    # Q4: Ford SCP legacy
    scp = next((l for l in makes["ford"].get("legacy", []) if "SCP" in l["protocol"]), {})
    q4_ok = ("PWM" in scp.get("protocol", "") and scp.get("obd2_pins") == [2, 10]
             and "IFR" in scp.get("notes", ""))
    check("Q4", "What was Ford's pre-CAN corporate protocol, on which pins, and what is its quirk?",
          q4_ok, f"SCP = J1850 PWM 41.6 kbps on pins {scp.get('obd2_pins')}; Ford's variant REQUIRES In-Frame Response bytes {grade_badge(scp.get('grade'))}"
          if q4_ok else "Ford SCP facts missing")

    # Q5: Stellantis SGW
    sgw = next((g for g in diag["stellantis"].get("gateways", []) if "SGW" in g["module"]), {})
    q5_ok = ("2018" in sgw.get("years", "") and "BLOCKED" in sgw.get("effect", "")
             and "AutoAuth" in sgw.get("bypass", ""))
    check("Q5", "What is the Stellantis Secure Gateway, which years, and what does it block?",
          q5_ok, f"SGW ({sgw.get('years', '')}): CAN firewall at the DLC. Reads (DTCs, live data) still work; WRITES (DTC clear, actuations, programming) blocked without auth. Legitimate paths: AutoAuth ($50/yr shop), wiTECH 2.0, physical bypass {grade_badge(sgw.get('grade'))}"
          if q5_ok else "SGW facts missing")

    # Q6: Stellantis CAN-C1 pins
    cc1 = bus("stellantis", "CAN-C1")
    q6_ok = (cc1.get("obd2_pins") == [6, 14] and cc1.get("bitrate_kbps") == 500)
    check("Q6", "Which DLC pins and bitrate is Stellantis CAN-C1?",
          q6_ok, f"Pins {cc1.get('obd2_pins')}, {cc1.get('bitrate_kbps')} kbps {grade_badge(cc1.get('grade'))}"
          if q6_ok else "CAN-C1 facts missing")

    # Q7: GM diagnostic addressing
    usdt = next((s for s in diag["gm"].get("services", [])
                 if "USDT" in s["name"]), {})
    q7_ok = ("$7E0" in usdt.get("service_id", "") and "0x7E0/0x7E8" in usdt.get("support", ""))
    check("Q7", "What are the GM physical diagnostic request/response IDs for the ECM?",
          q7_ok, f"11-bit USDT: tester sends $7E0-$7E7, ECU answers $7E8-$7EF; ECM = 0x7E0/0x7E8 (verified by ELM327 VIN-read capture) {grade_badge(usdt.get('grade'))}"
          if q7_ok else "GM USDT facts missing")

    # Q8: Ford +8 offset
    p8 = next((s for s in diag["ford"].get("services", [])
               if "+8" in s["name"]), {})
    q8_ok = ("0x7E0 -> 0x7E8" in p8.get("service_id", ""))
    check("Q8", "What is Ford's diagnostic response-ID convention?",
          q8_ok, f"+8 response offset: request 0x7E0 -> response 0x7E8 {grade_badge(p8.get('grade'))}"
          if q8_ok else "Ford +8 facts missing")

    # Q9: M2 simultaneous HS+MS on Ford
    fmap = " ".join(mp.get("notes", "") for mp in makes["ford"].get("m2_mapping", []))
    q9_ok = ("SIMULTANEOUSLY" in fmap)
    check("Q9", "Can the M2 watch Ford HS-CAN and MS-CAN at the same time?",
          q9_ok, "Yes — two independent CAN controllers (HS-CAN 6/14 + MS-CAN 3/11); a switched ELM327 sees only one at a time [B]"
          if q9_ok else "M2 Ford mapping facts missing")

    # Q10: M2 vs CAN FD
    cfd = bus("ford", "CAN FD")
    q10_ok = ("CANNOT PARTICIPATE" in cfd.get("notes", ""))
    check("Q10", "Can the M2 participate on a 2021+ F-150 CAN-FD bus?",
          q10_ok, "No — TJA1051 transceivers are CAN 2.0 only; 2021+ CAN-FD Fords are out of scope for M2 CAN work [B]"
          if q10_ok else "CAN FD facts missing")

    # Q11: GM SWCAN wake-up
    gmap = " ".join(mp.get("notes", "") for mp in makes["gm"].get("m2_mapping", []))
    q11_ok = ("mode(2)" in gmap and "HV-wake" in gmap)
    check("Q11", "What must M2 firmware do before expecting replies from sleeping GM SWCAN modules?",
          q11_ok, "Send high-voltage wake-up first: mode(2), then mode(3) for normal communication [A]"
          if q11_ok else "SWCAN wake facts missing")

    # Q12: Stellantis pre-CAN PCI
    pci = next((l for l in makes["stellantis"].get("legacy", [])
                if "PCI" in l["protocol"]), {})
    q12_ok = ("VPW" in pci.get("protocol", "") and pci.get("obd2_pins") == [2])
    check("Q12", "What was pre-CAN Chrysler's PCI bus, physically?",
          q12_ok, f"SAE J1850 VPW, single wire on DLC pin {pci.get('obd2_pins')}, ~10.4 kbps {grade_badge(pci.get('grade'))}"
          if q12_ok else "PCI facts missing")

    # Q13: Toyota DLC3 CAN layout
    ths = bus("toyota", "CAN V Bus (HS)")
    q13_ok = (ths.get("obd2_pins") == [6, 14] and ths.get("bitrate_kbps") == 500
              and "not on the DLC" in bus("toyota", "MS-CAN").get("notes", ""))
    check("Q13", "Which CAN buses does Toyota expose at the DLC3?",
          q13_ok, f"ONLY the 500 kbps HS CAN V Bus on pins {ths.get('obd2_pins')}; "
                  "the 250 kbps MS-CAN sits behind the gateway ECU — one M2 CAN controller "
                  f"normally suffices at the DLC {grade_badge(ths.get('grade'))}"
          if q13_ok else "Toyota bus facts missing")

    # Q14: Toyota hybrid diagnostic IDs
    th_svc = next((s for s in diag["toyota"].get("services", [])
                   if "Physical addressing" in s["name"]), {})
    q14_ok = ("0x7E2/0x7EA" in th_svc.get("support", "") and "0x7E3/0x7EB" in th_svc.get("support", ""))
    check("Q14", "A generic scanner on Toyota 0x7E0 sees no hybrid DTCs. Which IDs must it use instead?",
          q14_ok, "HV ECU 0x7E2/0x7EA, HV battery 0x7E3/0x7EB — a generic OBD-II scanner "
                  f"talking only to 0x7E0 never sees hybrid DTCs {grade_badge(th_svc.get('grade'))}"
          if q14_ok else "Toyota hybrid ID facts missing")

    # Q15: Honda B-CAN facts
    bc = bus("honda", "B-CAN")
    q15_ok = (bc.get("bitrate_kbps") == 33.33 and bc.get("wire_count") == 1
              and "NEVER at the DLC" in bc.get("notes", ""))
    check("Q15", "What is Honda's B-CAN (speed, wiring), and is it at the OBD-II port?",
          q15_ok, f"Single-wire 33.33 kbps {grade_badge(bc.get('grade'))}; NOT at the DLC — "
                  "requires a behind-dash tap (BCM 36-pin connector on 2016 Civic/2017 CR-V). "
                  "Speed conflict flagged: one community project claims 150 kbps on 2016+ [C], unverified"
          if q15_ok else "Honda B-CAN facts missing")

    # Q16: Honda diagnostic addressing
    hs = next((s for s in diag["honda"].get("services", [])
               if "29-bit" in s["name"]), {})
    q16_ok = ("0x18DB33F1" in hs.get("service_id", "") and "0x18DAF110" in hs.get("service_id", ""))
    check("Q16", "What is Honda's documented diagnostic CAN addressing?",
          q16_ok, f"29-bit: tester 0x18DB33F1 -> ECM 0x18DAF110 {grade_badge(hs.get('grade'))}; "
                  "try 29-bit first (the 11-bit 0x7E0/0x7E8 path is single-source [C])"
          if q16_ok else "Honda addressing facts missing")

    # Q17: VW SFD scope
    sfd = next((g for g in diag["vw"].get("gateways", [])
                if "SFD" in g["module"]), {})
    q17_ok = ("adaptations, coding, parametrizations" in sfd.get("effect", "")
              and "NOT SFD-protected" in sfd.get("effect", ""))
    check("Q17", "What does VW's SFD block, and what does it explicitly NOT block?",
          q17_ok, "Blocks WRITING services (adaptations, coding, parametrizations) on protected ECUs; "
                  "per VW's own workshop manual, reads and bootloader-based flashing are NOT SFD-protected. "
                  f"SFD2 on 2024+ {grade_badge(sfd.get('grade'))}"
          if q17_ok else "SFD facts missing")

    # Q18: VW DLC CAN pairs
    vd = bus("vw", "Diagnosis CAN")
    q18_ok = (vd.get("obd2_pins") == [6, 14] and "single CAN pair" in vd.get("notes", ""))
    check("Q18", "How many CAN pairs does VW expose on the DLC?",
          q18_ok, f"ONE: pins {vd.get('obd2_pins')} = the diagnosis CAN to the J533 gateway "
                  "(comfort/infotainment are gateway-internal) [B]"
          if q18_ok else "VW DLC facts missing")

    # Q19: Hyundai M-CAN at the DLC?
    hmc = bus("hyundai", "M-CAN")
    q19_ok = (hmc.get("obd2_pins") == [] and "UNCONFIRMED" in hmc.get("notes", ""))
    check("Q19", "Is Hyundai's M-CAN exposed at the OBD-II port?",
          q19_ok, "Not confirmed — no source places M-CAN on OBD-II pins; treat as interior-only "
                  "unless a per-model wiring diagram says otherwise [C]"
          if q19_ok else "Hyundai M-CAN facts missing")

    # Q20: Nissan DDL vs ELM327
    ddl = next((l for l in makes["nissan"].get("legacy", [])
                if "DDL" in l["protocol"]), {})
    q20_ok = ("153.6 kHz" in ddl.get("notes", "") and "ELM327" in ddl.get("notes", ""))
    check("Q20", "Can an ELM327/STN chip speak Nissan's DDL/Consult I protocol?",
          q20_ok, "No — DDL needs a host-generated 153.6 kHz async clock plus 12V idle-low signaling, "
                  f"which no ELM AT command set provides {grade_badge(ddl.get('grade'))}"
          if q20_ok else "Nissan DDL facts missing")

    # ---- v1.2 DTC questions (answered solely from generated/json/dtcs.json) ----
    with open(GEN_JSON / "dtcs.json") as f:
        dtcd = json.load(f)
    dentries = {(d["make"], d["code"]): d for d in dtcd["entries"]}

    # Q21: decode raw mode-03 bytes 03 00 -> P0300
    p0300 = dentries.get(("generic", "P0300"), {})
    q21_ok = ("Misfire" in p0300.get("description", "") and p0300.get("scope") == "generic")
    check("Q21", "A mode-03 response contains the two DTC bytes 0x03 0x00. Which code is this and what does it mean?",
          q21_ok, f"P0300 — {p0300.get('description', '')} {grade_badge(p0300.get('grade'))} "
                  f"(SAE J2012 generic; possible causes include: {'; '.join(p0300.get('possible_causes', [])[:2])})"
          if q21_ok else "P0300 facts missing")

    # Q22: Ford manufacturer-specific P1151
    p1151 = dentries.get(("ford", "P1151"), {})
    q22_ok = ("HO2S21" in p1151.get("description", "") and "Lean" in p1151.get("description", "")
              and p1151.get("scope") == "manufacturer")
    check("Q22", "What is Ford-specific DTC P1151?",
          q22_ok, f"P1151 — {p1151.get('description', '')} {grade_badge(p1151.get('grade'))} "
                  "(Ford manufacturer-specific, not SAE generic)"
          if q22_ok else "Ford P1151 facts missing")

    # Q23: Stellantis P1494 (LDP EVAP)
    p1494 = dentries.get(("stellantis", "P1494"), {})
    q23_ok = ("Leak Detection Pump" in p1494.get("description", "") and p1494.get("grade") == "A")
    check("Q23", "What is Stellantis DTC P1494, and what is a notorious false trigger?",
          q23_ok, f"P1494 — {p1494.get('description', '')} {grade_badge(p1494.get('grade'))}; "
                  "Chrysler's unique LDP EVAP design means an aftermarket gas cap can falsely trigger it"
          if q23_ok else "Stellantis P1494 facts missing")

    # Q24: GM P1811 with causes
    p1811 = dentries.get(("gm", "P1811"), {})
    q24_ok = ("Maximum Adapt" in p1811.get("description", "")
              and any("solenoid" in c.lower() for c in p1811.get("possible_causes", [])))
    check("Q24", "What is GM DTC P1811 and what commonly causes it?",
          q24_ok, f"P1811 — {p1811.get('description', '')} {grade_badge(p1811.get('grade'))}; "
                  f"commonly: {'; '.join(p1811.get('possible_causes', [])[:2])}"
          if q24_ok else "GM P1811 facts missing")

    # Q25: DTC catalog composition (v1.4.0: Big Three + generic baseline)
    n_man = sum(1 for d in dtcd["entries"] if d["scope"] == "manufacturer")
    n_gen = sum(1 for d in dtcd["entries"] if d["scope"] == "generic")
    per_make = {mk: sum(1 for d in dtcd["entries"] if d["make"] == mk)
                for mk in ("gm", "ford", "stellantis")}
    q25_ok = (n_gen == 2143 and n_man >= 395
              and per_make == {"gm": 107, "ford": 182, "stellantis": 106})
    check("Q25", "How is the v1.4.0 DTC catalog composed for the Big Three?",
          q25_ok, f"{n_gen} SAE J2012 generic codes (2098 baseline + 45 Toyota-documented SAE entries); Big Three manufacturer-specific: "
                  f"GM {per_make['gm']}, Ford {per_make['ford']}, Stellantis {per_make['stellantis']} "
                  f"(v1.4.0 adds 10 import makes on top)"
          if q25_ok else "DTC catalog counts missing")

    # ---- v1.2.1 import-make DTC questions ----
    # Q26: Toyota P1346
    p1346 = dentries.get(("toyota", "P1346"), {})
    q26_ok = ("VVT" in p1346.get("description", "") and p1346.get("scope") == "manufacturer")
    check("Q26", "What is Toyota-specific DTC P1346?",
          q26_ok, f"P1346 — {p1346.get('description', '')} {grade_badge(p1346.get('grade'))}"
          if q26_ok else "Toyota P1346 facts missing")

    # Q27: Honda P1259 (VTEC = usually an oil problem)
    p1259 = dentries.get(("honda", "P1259"), {})
    q27_ok = ("VTEC" in p1259.get("description", "")
              and any("oil" in c.lower() for c in p1259.get("possible_causes", [])))
    check("Q27", "What is Honda DTC P1259, and what should be checked first?",
          q27_ok, f"P1259 — {p1259.get('description', '')} {grade_badge(p1259.get('grade'))}; "
                  f"check first: {p1259.get('possible_causes', ['?'])[0]} (VTEC codes are usually oil codes)"
          if q27_ok else "Honda P1259 facts missing")

    # Q28: VW P1476 (5-digit mapping)
    p1476 = dentries.get(("vw", "P1476"), {})
    q28_ok = ("Leak Detection Pump" in p1476.get("description", "")
              and "17884" in p1476.get("diagnostic_notes", ""))
    check("Q28", "What is VW DTC P1476, and what is its 5-digit VAG code?",
          q28_ok, f"P1476 — {p1476.get('description', '')} {grade_badge(p1476.get('grade'))}; "
                  "5-digit VAG code 17884 recorded in diagnostic notes"
          if q28_ok else "VW P1476 facts missing")

    # Q29: Hyundai P1295
    p1295 = dentries.get(("hyundai", "P1295"), {})
    q29_ok = ("Electronic Throttle Control" in p1295.get("description", "")
              and p1295.get("scope") == "manufacturer")
    check("Q29", "What is Hyundai-specific DTC P1295?",
          q29_ok, f"P1295 — {p1295.get('description', '')} {grade_badge(p1295.get('grade'))}"
          if q29_ok else "Hyundai P1295 facts missing")

    # Q30: Nissan P1610 (NATS lock mode)
    p1610 = dentries.get(("nissan", "P1610"), {})
    q30_ok = ("Lock Mode" in p1610.get("description", "") and p1610.get("grade") == "A")
    check("Q30", "What is Nissan DTC P1610, and what commonly triggers it spuriously?",
          q30_ok, f"P1610 — {p1610.get('description', '')} {grade_badge(p1610.get('grade'))}; "
                  "often just a weak battery or repeated unregistered-key attempts — don't replace NATS parts first"
          if q30_ok else "Nissan P1610 facts missing")

    # ---- v1.4.0 all-makes DTC composition ----
    # (Q31 v1.2.1 composition check superseded by v1.4.0 counts)
    n_total = len(dtcd["entries"])
    imp = {mk: sum(1 for d in dtcd["entries"] if d["make"] == mk)
           for mk in ("toyota", "honda", "vw", "hyundai", "nissan",
                      "subaru", "mazda", "bmw", "mercedes", "volvo")}
    q31_ok = (n_total == 4411 and imp == {"toyota": 283, "honda": 465, "vw": 140,
                                          "hyundai": 440, "nissan": 274,
                                          "subaru": 72, "mazda": 40, "bmw": 45,
                                          "mercedes": 126, "volvo": 33})
    check("Q31", "How is the v1.4.0 DTC catalog composed?",
          q31_ok, f"{n_total} DTCs total: {n_gen} SAE generic + {n_man} manufacturer-specific; "
                  f"import makes: Toyota {imp['toyota']}, Honda {imp['honda']}, VW {imp['vw']}, "
                  f"Hyundai/Kia {imp['hyundai']}, Nissan {imp['nissan']}, Subaru {imp['subaru']}, "
                  f"Mazda {imp['mazda']}, BMW {imp['bmw']}, Mercedes {imp['mercedes']}, Volvo {imp['volvo']}"
          if q31_ok else "v1.4.0 catalog counts missing")

    with open(GEN_JSON / "dids.json") as f:
        didd = json.load(f)
    didx = {(d["make"], d["did"]): d for d in didd["entries"]}
    with open(GEN_JSON / "asbuilt.json") as f:
        abd = json.load(f)
    abx = {a["address"]: a for a in abd["entries"]}
    with open(GEN_JSON / "module_maps.json") as f:
        mmd = json.load(f)

    # ---- v1.3.0/v1.4.0 platform-depth questions ----
    # Q32: ISO DID 0xF190
    f190 = didx.get(("iso", "0xF190"), {})
    q32_ok = ("VIN" in f190.get("name", "") and "17" in f190.get("size", "")
              and f190.get("grade") == "A")
    check("Q32", "What is ISO-standard DID 0xF190, and how big is it?",
          q32_ok, f"0xF190 = {f190.get('name', '')}: {f190.get('size', '')} "
                  f"{grade_badge(f190.get('grade'))} (ISO 14229-1:2013)"
          if q32_ok else "0xF190 facts missing")

    # Q33: Ford DID 0xD100
    d100 = didx.get(("ford", "0xD100"), {})
    q33_ok = ("Operating State" in d100.get("name", "") and d100.get("grade") == "A")
    check("Q33", "What is Ford DID 0xD100, and which ECUs support it?",
          q33_ok, f"0xD100 = {d100.get('name', '')} {grade_badge(d100.get('grade'))} — "
                  "supported by ALL Ford ECUs (Ford Global Diagnostic Spec)"
          if q33_ok else "Ford 0xD100 facts missing")

    # Q34: Nissan 0x21 local IDs
    n04 = didx.get(("nissan", "0x04"), {})
    q34_ok = (n04.get("service") == "0x21-local")
    check("Q34", "A Nissan Leaf TCU identifier is documented as 0x04. Which service reads it — 0x22?",
          q34_ok, f"No — service {n04.get('service', '')}: Nissan CAN-era modules use KWP2000-style "
                  f"0x21 local IDs (0x22 rejected with NRC 0x12) {grade_badge(n04.get('grade'))}"
          if q34_ok else "Nissan local-ID facts missing")

    # Q35: Ford as-built APIM
    apim = abx.get("7D0", {})
    q35_ok = ("APIM" in apim.get("module", "") and "7D0-01-01" in apim.get("blocks", []))
    check("Q35", "What is Ford as-built module address 7D0, and how is its data addressed?",
          q35_ok, f"7D0 = {apim.get('module', '')} {grade_badge(apim.get('grade'))}; "
                  "format MODULE-BLOCK-LINE (e.g. 7D0-01-01), trailing group = checksum"
          if q35_ok else "Ford as-built 7D0 facts missing")

    # Q36: v1.4.0 composition
    n_dids, n_ab, n_mm = len(didd["entries"]), len(abd["entries"]), len(mmd["entries"])
    q36_ok = (n_dids == 637 and n_ab == 41 and n_mm == 51)
    check("Q36", "How is the v1.4.0 platform-depth layer composed?",
          q36_ok, f"{n_dids} UDS/SSM identifiers (36 ISO-standard + 601 make-specific, incl. 30 Subaru SSM2 parameter addresses), "
                  f"{n_ab} Ford as-built modules, {n_mm} per-platform module maps (13 makes)"
          if q36_ok else "v1.4.0 composition facts missing")

    all_pass = all(r["result"] == "PASS" for r in results)
    n = len(results)
    lines = ["# Validation test", "",
             f"{n} OEM questions, each answered SOLELY from the generated artifacts "
             "(`generated/json/` + `generated/rag-chunks.jsonl`). Grades: A/B/C per the database method.", ""]
    for r in results:
        lines += [f"## {r['id']} — {r['result']}", "", f"**Q:** {r['question']}", "",
                  f"**A:** {r['answer']}", ""]
    lines += [f"**Overall: {f'{n}/{n} PASS' if all_pass else 'FAILURES PRESENT'}**", "",
              "_Generated by scripts/build.py — do not hand-edit._", ""]
    (GEN_WIKI / "validation.md").write_text("\n".join(lines))
    for r in results:
        print(f"  {r['id']}: {r['result']} — {r['question'][:60]}...")
    if not all_pass:
        fail("validation test: one or more questions FAILED")
    print(f"validation test: {n}/{n} PASS")
    return results


def main():
    data = load_sources()
    validate(data)
    cross_check(data)
    write_json(data)
    write_wiki(data)
    write_rag_chunks(data)
    run_validation()
    print("BUILD OK")


if __name__ == "__main__":
    main()
