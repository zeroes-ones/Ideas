# Pilot Denominator — W35 Tooling & Method (Bengaluru, 4 pilot verticals)

> **Date:** 2026-09-08 · **Status:** W35 deliverable — runnable tool + method. Data source: **OpenCity "BBMP Trade Licenses Data 2025"** (CKAN `newdata.opencity.in`), ward-level licence CSVs per assembly constituency (28 files; updated 27-Apr-2026). Maps to `docs/work-items.md` W35–W40 and `research/bengaluru-pilot-map.md`.

## 1. What this is
A Python-3-stdlib tool (`scripts/pilot-denominator.py`) that:
1. **Lists/fetches** the OpenCity dataset resources via the CKAN API (`list`, `fetch`).
2. **Inspects** the real CSV schema before mapping (`inspect`) — column names must be eyeballed first.
3. **Maps** each licensed-premise row to one of the 4 pilot verticals by licence-description keywords and emits a **ward × vertical count table** + grand totals + top unclassified descriptions (`map`).

## 2. How to run (on a machine with internet)
```
python3 scripts/pilot-denominator.py list                       # see resources
mkdir -p /tmp/bbmp-licences
python3 scripts/pilot-denominator.py fetch /tmp/bbmp-licences   # download CSVs
python3 scripts/pilot-denominator.py inspect /tmp/bbmp-licences # verify columns
python3 scripts/pilot-denominator.py map /tmp/bbmp-licences --out research/pilot-denominator-output.md
```
Then refine the keyword rules in `RULES` using the "Top unclassified descriptions" block (expected: 2 passes to stabilise).

## 3. Mapping rules (v1, precedence-ordered)
| Vertical | Rule triggers (licence description/category text) |
|---|---|
| auto-mechanic | auto, automobile, vehicle, garage, motor, motorcycle, car(s), bike, scooter, two-/four-wheeler, tyre/tire, service station, auto electrician, spare parts, workshop |
| appliance & electronics | appliance(s), refrigerator, washing machine, fridge, air cond, microwave, TV, television, electronic(s), mobile, cell phone, computer, CCTV, telecom, phone, laptop |
| electrical | electrical, electrician, wiring, switchgear, lighting, hardware & electrical |
| kirana/grocery | kirana, grocery, provision, general merchant/store, supermarket, departmental, vegetable, fruit, milk, dairy, confectionery |

Precedence matters (e.g., **"auto electrician" → auto-mechanic**, not electrical). Anything unmatched = `UNCLASSIFIED` → surfaced for rule refinement. **12/12 unit tests + synthetic end-to-end pass** (see test transcript: `kirana & general merchant shop`, `mobile phone sales and repair`, `motor car garage workshop`, `tailoring shop → UNCLASSIFIED`).

## 4. Interpreting output (honest limits)
- **Floor estimate, not a census:** dataset is BBMP-era (198-ward map; BBMP dissolved 1-Sep-2025) → ward codes must be **re-mapped to the 369-ward / 5-corporation structure** (delimitation 19-Nov-2025) at build time `[VERIFIED — bengaluru-pilot-map.md §1]`.
- Unlicensed shops are absent by definition → **W36 field sample corrects coverage** (walk 2–3 streets/ward; expect unlicensed micro-shops, esp. kirana/mechanics).
- Licence descriptions are municipal categories (Schedule X, KMC Act 1976) — some rows use shop names only; classification accuracy improves after inspecting the real columns (`inspect`) and a rule-refinement pass.
- **Use:** ward shortlist (top vertical density), recruitment targets (W39/W40 funnel), consumer-launch gate planning (≥100 verified `[scope-brief]`).

## 5. Execution note (this environment)
The sandbox blocks outbound HTTP (CKAN calls return `http=000`), so the live fetch **must be run by the founder** on an internet-connected machine. All code paths were verified locally with a synthetic CSV (fetch/list need network; `map`/`inspect` fully tested).

## 6. Downstream (already in work-items)
- W36 field sample → corrects denominator for unlicensed shops.
- W37 portal-ownership verification (GBA/5-corps; done for facts, see bengaluru-pilot-map.md §1).
- W39 recruitment kit → W40 weekly ramp projection to the ≥100 gate.
