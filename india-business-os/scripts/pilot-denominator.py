#!/usr/bin/env python3
"""
pilot-denominator.py — W35 tool: compute the Bengaluru pilot denominator
from the OpenCity BBMP Trade Licenses Data 2025 dataset (CKAN).

Purpose (docs/work-items.md W35, research/bengaluru-pilot-map.md):
  ward-level licensed-premise counts mapped to the 4 pilot verticals:
  kirana/grocery, appliance & electronics, electrical, auto-mechanic.

Design notes
  - Python 3 stdlib only (urllib, csv, json, argparse) — no deps.
  - Data is BBMP-era (198-ward map). Wards will need re-mapping to the
    369-ward / 5-corporation structure at build time (bengaluru-pilot-map.md §1).
  - Classification is a keyword heuristic over the licence description/category
    text. It is a *floor* estimate to shortlist wards — ALWAYS inspect real
    columns first (--inspect) and refine keywords after glancing at data.

Usage
  python3 scripts/pilot-denominator.py --list                     # show resources
  python3 scripts/pilot-denominator.py --inspect DIR              # preview schema of one file
  python3 scripts/pilot-denominator.py --fetch DIR                # download CSVs
  python3 scripts/pilot-denominator.py --map DIR [--out out.md]   # compute ward×vertical counts

Author: session agent · Date: 2026-09-08
"""

import argparse
import csv
import io
import json
import re
import sys
import urllib.parse
import urllib.request

PACKAGE_ID = "bbmp-trade-licenses-data-2025"
BASE = "https://newdata.opencity.in/api/3/action"

# Keyword rules, in precedence order (first match wins).
# Order matters: 'auto electrician' contains 'electrician' -> AUTO must win.
RULES = [
    ("auto-mechanic", re.compile(
        r"auto\b|automobile|vehicle|garage|motor\b|motorcycle|car\b|cars\b|bike|scooter|"
        r"two[- ]?wheeler|four[- ]?wheeler|tyre|tire|service station|auto electrician|"
        r"auto spare|spare parts|workshop", re.I)),
    ("appliance & electronics", re.compile(
        r"appliance|refrigerator|washing machine|fridge|air cond|microwave|tv\b|television|"
        r"electronic|mobile|cell phone|computer|cctv|telecom|phone|laptop", re.I)),
    ("electrical", re.compile(
        r"electrical|electrician|wiring|switchgear|lighting|hardware & electrical", re.I)),
    ("kirana/grocery", re.compile(
        r"kirana|grocery|provision|general merchant|general store|supermarket|"
        r"departmental|vegetable|fruit|milk|dairy|confectionery", re.I)),
]

VERTICALS = [name for name, _ in RULES]


def ckan(action, params=None):
    url = f"{BASE}/{action}" + (f"?{urllib.parse.urlencode(params)}" if params else "")
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def package_resources():
    data = ckan("package_show", {"id": PACKAGE_ID})["result"]
    out = []
    for res in data.get("resources", []):
        out.append({
            "id": res["id"], "name": res.get("name", ""),
            "format": res.get("format", ""), "url": res.get("url", ""),
        })
    return data.get("title", ""), out


def find_cols(headers):
    """Heuristic column roles: ward, text-to-classify, (optional) address.
    Two-tier: prefer descriptive content columns over generic 'trade/business'."""
    ward = text = addr = None
    strong = ("description", "category", "activity", "occupation", "nature",
              "licence", "license", "type of trade", "trade category")
    weak = ("trade", "business", "work")
    for h in headers:
        hl = (h or "").lower()
        if ward is None and ("ward" in hl or "constitu" in hl):
            ward = h
        if addr is None and ("address" in hl or "premises" in hl or "location" in hl):
            addr = h
    for tier in (strong, weak):
        if text is not None:
            break
        for key in tier:
            for h in headers:
                if key in (h or "").lower():
                    text = h
                    break
            if text is not None:
                break
    return ward, text, addr


def classify(blob):
    for name, rx in RULES:
        if rx.search(blob):
            return name
    return "UNCLASSIFIED"


def load_rows(path):
    """Robust row loader tolerant of encoding/dialect quirks."""
    raw = open(path, "rb").read()
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    sample = text[:4096]
    dialect = csv.Sniffer().sniff(sample, delimiters=",;\t") if csv.Sniffer().has_header(sample) else csv.excel
    return list(csv.DictReader(io.StringIO(text), dialect=dialect))


def cmd_list(_args):
    title, res = package_resources()
    print(f"# {title}")
    for i, r in enumerate(res):
        print(f"{i:02d}  {r['name']}  [{r['format']}]  {r['url']}")


def cmd_inspect(args):
    import glob
    files = sorted(glob.glob(args.directory + "/*.csv")) or sorted(glob.glob(args.directory + "/*.CSV"))
    if not files:
        sys.exit("no CSV found in " + args.directory)
    rows = load_rows(files[0])
    print(f"file: {files[0]}  rows: {len(rows)}")
    print("columns:", ", ".join(rows[0].keys()))
    for row in rows[:3]:
        print({k: (v[:40] if v else "") for k, v in row.items()})


def cmd_fetch(args):
    import os
    os.makedirs(args.directory, exist_ok=True)
    title, res = package_resources()
    print(f"fetching {len(res)} resources for {title}")
    for r in res:
        if r["format"].lower() not in ("csv", ""):
            continue
        name = re.sub(r"[^\w.-]+", "_", r["name"]).strip("_") + ".csv"
        path = os.path.join(args.directory, name)
        try:
            urllib.request.urlretrieve(r["url"], path)
            print("  ok ", name)
        except Exception as e:  # noqa: BLE001
            print("  ERR", name, e)


def cmd_map(args):
    import glob
    import collections
    files = sorted(glob.glob(args.directory + "/*.csv")) or sorted(glob.glob(args.directory + "/*.CSV"))
    if not files:
        sys.exit("no CSV found in " + args.directory)
    counts = collections.defaultdict(lambda: collections.Counter())
    unclassified = collections.Counter()
    column_warnings = set()
    grand = collections.Counter()
    for f in files:
        rows = load_rows(f)
        if not rows:
            continue
        ward, text, _ = find_cols(list(rows[0].keys()))
        if text is None:
            column_warnings.add(f.split("/")[-1] + ": no text column found")
            continue
        for row in rows:
            blob = (str(row.get(text) or "") + " " + str(row.get(ward) or "")).strip()
            if not blob:
                continue
            v = classify(blob)
            w = (str(row.get(ward) or "UNKNOWN")).strip()
            counts[w][v] += 1
            grand[v] += 1
            if v == "UNCLASSIFIED":
                unclassified[blob.strip().lower()[:60]] += 1
    # output
    out = sys.stdout if not args.out else open(args.out, "w", encoding="utf-8")
    print(f"# Pilot denominator (ward × vertical) — {len(files)} file(s)", file=out)
    print("", file=out)
    hdr = "| Ward | " + " | ".join(VERTICALS) + " | total |"
    print(hdr, file=out)
    print("|" + "---|" * (len(VERTICALS) + 2), file=out)
    for w in sorted(counts):
        c = counts[w]
        tot = sum(c.values())
        print(f"| {w} | " + " | ".join(str(c[v]) for v in VERTICALS) + f" | {tot} |", file=out)
    print("", file=out)
    print("## Grand totals", file=out)
    print("| vertical | count |", file=out)
    print("|---|---|", file=out)
    for v in VERTICALS + ["UNCLASSIFIED"]:
        print(f"| {v} | {grand[v]} |", file=out)
    if column_warnings:
        print("", file=out)
        print("## Warnings (fix schema then re-run)", file=out)
        for w in sorted(column_warnings):
            print("- " + w, file=out)
    print("", file=out)
    print("## Top unclassified descriptions (refine keyword rules)", file=out)
    for blob, n in unclassified.most_common(15):
        print(f"- {n:5d}  {blob}", file=out)
    if args.out:
        out.close()
        print("wrote", args.out)


def main():
    p = argparse.ArgumentParser(description="Bengaluru pilot denominator (W35)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    for name in ("inspect", "fetch", "map"):
        sp = sub.add_parser(name)
        sp.add_argument("directory")
        if name == "map":
            sp.add_argument("--out")
    args = p.parse_args()
    {"list": cmd_list, "inspect": cmd_inspect, "fetch": cmd_fetch, "map": cmd_map}[args.cmd](args)


if __name__ == "__main__":
    main()
