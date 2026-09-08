# Field Sample Sheet — W36 Ground-Truth Pass (Bengaluru pilot wards)

> **Date:** 2026-09-08 · **Status:** Ready for use after W35 data fetch · Companion: `research/pilot-denominator.md` (tool), `research/bengaluru-pilot-map.md` (wards/governance), `docs/pilot-recruitment-playbook.md` (W39 uses this list).
> **Purpose:** correct the licence-dataset floor for unlicensed shops; verify ward shortlist; harvest contact + WhatsApp willingness for W38 interviews and W39 recruitment. Runs per ward; ~30–50 shops/ward.

## 1. Protocol
1. **Pick streets per ward (3)** — one main commercial road, one interior/residential-lane stretch, one market/cluster (or busiest 500 m). Record street + time-of-day (morning 9–11 / evening 6–8 catches kirana; weekend for services).
2. **Walk order, not cherry-picking** — record every ground-floor shop on the chosen stretch that fits *or could fit* the pilot set; note OTHER for the rest (helps understand pack mix).
3. **Observe first, ask second** — licence certs are usually displayed (trade licence/S&E/GST/FSSAI); note what you can see *before* asking.
4. **Ask only 3 things** (≤2 min/shop): licence status if not visible, which billing/khata app they use, and "may I WhatsApp you about a free pilot?" (consent).
5. **No photos of people; no Aadhaar/PAN**; shop phone only with consent. Store as CSV, not in a shared cloud.

## 2. Capture table (one row per shop)
| # | Street | Vertical | Licences seen (T/S/G/F/none) | Apps seen (U/Q/K/V/None) | WhatsApp OK? (Y/N) | Owner-est staff | Notes |
|---|---|---|---|---|---|---|---|
| 01 |  | G/A/E/M/O(+F food flag) |  |  |  |  |  |

**Codes:** Vertical — G kirana/grocery · A appliance & electronics · E electrical · M auto-mechanic · O other. Append `+F` if kirana/other sells food (FSSAI relevance).
Licences — T trade licence · S S&E (shop act) · G GST · F FSSAI · n none visible.
Apps — U UPI QR (any) · Q WhatsApp Business · K khata/billing app (Vyapar/OkCredit/Khatabook) · V other · None.

**Example row:** `01 | 5th Main Koramangala | G+F | T,S | U,Q | Y | 2 | sells milk+snacks; wants "more regular customers"; Hindi+Kan work` .

## 3. Per-ward tally (fill after walk)
| Ward | Street set | Shops walked | G | A | E | M | O | Licensed (T/S) | Unlicensed-est | WhatsApp-OK | Coverage note |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Coverage formula (per ward):** compare licence-list count (W35 dataset, same streets) `D` vs licensed found `L`:
- Coverage = `L / D` (target ≥80%; else dataset may lag the corporation transition → flag in W36 notes, don't silently trust).
- Estimated total in-vertical in ward ≈ `dataset_count_in_ward × (shops_walked / licensed_found_among_matching)` adjusted for unlicensed adds — keep it simple: report **licensed (dataset), licensed (field), unlicensed (field)** as three numbers per ward; planning uses all three (W40).

## 4. Field notes to capture (free text per street)
1. Any shop type you expected but rarely found (gap vs dataset categories)?
2. Dominant language mix (affects recruitment copy)?
3. Two owner *requests* heard most often (feeds W38 hypothesis weights + W39 value props)?

## 5. Hand-off
- CSV → `research/field-sample-<ward>-<YYYYMMDD>.csv` (keep outside repo if preferred; path noted in W36 notes).
- Merge result: update `research/pilot-denominator.md` output table with field-corrected ward numbers; shortlist final pilot wards; seed W39 approach list (WhatsApp-OK column) and W38 interview pool (prefer WhatsApp-OK + 2 per vertical).
