# Bengaluru Pilot Market Map — Entry B single-city rollout ground truth

> **Date:** 2026-09-08 · **Status:** Pilot-geography research pass (feeds scope-brief geography + work-items supply ramp). Tags: `[VERIFIED]` / `[ESTIMATED]` / `[VERIFY at build]`.

## 1. Governance context — the city just restructured `[VERIFIED]`
- **Timeline:** Greater Bengaluru Governance Act 2024 → BBMP legally replaced by the **Greater Bengaluru Authority (GBA)** on **15 May 2025**; final notification establishing the **5 corporations (East/West/North/South/Central)** issued **2 Sep 2025**; BBMP dissolved with effect from **1 Sep 2025** `[VERIFIED — PNPC/GBA-sourced guides; bbmp.gov.in now serves GBA]`.
- **Wards:** final delimitation order **19 Nov 2025 → 369 wards** (Central 63, South 72, East 50, West 111, North 72) replacing the 198-ward BBMP map `[VERIFIED]`. **GBA/corporation elections were held Jun 2026** (SEC window 14–24 Jun; SC-mandated by 30 Jun); elected councils now seated → post-election (Aug 2026+) processes faster `[VERIFIED]`.
- **Trade licences today:** renewal FY26-27 under GBA circular — **1–5-year renewal option** (fee for selected years), penalty-free Feb 2026, +25% Mar, **+100% from 1 Apr 2026**; online-only via GBA portal/Seva Sindhu (Canara Bank challan offline); zoning (residential roads <40 ft → rejection), building-norm, waste/health conditions enforced across the 5 corporations; "Know Your New Corporation" tool available `[VERIFIED]`.
- **Data caveat:** the **OpenCity BBMP trade-licence dataset is BBMP-era (198-ward map)** → ward codes must be re-mapped to the 369-ward corporation structure at build time; legacy licence records may sit with a different successor office than expected `[VERIFIED — transition guides]`.
- **Planning implication:** licence-journey config must treat "which corporation/portal + which ward map" as dynamic fields; the dataset is a **count/floor source**, not a routing source.

## 2. Pilot licensing mechanics (KA) — sequence per shop type
| Step | Mechanics | Notes |
|---|---|---|
| Udyam / Udyam Assist | Free; PAN-based (or IME route via DA without PAN/GST) | Day-1, credit gate `[VERIFIED — UAP docs]` |
| GST (KA) | Goods >₹40L / services >₹20L threshold; e-comm day-1; 7-working-day registration (Sep-2025 reform) | **KA sensitivity:** 2025 UPI-based GST notices caused trader protests → expect compliance caution; enablement framing is non-negotiable `[VERIFIED — SBI Research/ET]` |
| Shops & Commercial Establishments (KA) | Labour-dept registration (state portal); annual returns; registers; EPFO/ESIC headcount cross-link FY25-26 `[VERIFIED]` | Micro self-certification precedent in MH; KA annual return norms `[VERIFY at build]` |
| Trade licence | Municipal — BBMP dissolved 1 Sep-2025; now the **5 GBA corporations**; online via GBA portal/Seva Sindhu; **1–5-year renewal option**; 100% penalty after 31 Mar | Ward map = **369 wards (Nov-2025 delimitation)**; licence category from Schedule X, KMC Act 1976 `[VERIFY at build: current per-corporation portal routing]` |
| FSSAI | Only where food sold (kirana-with-food, F&B pack) | Band conflict flagged earlier `[VERIFY]` |
| Sector licences | Drug licence (pharmacy pack, wave B) etc. | Out of v0.3 pilot set |

## 3. Pilot-unit design (proposal)
- **Unit = ward cluster** in a single corporation (minimises licence-portal variance). Recommended starting cluster: dense mixed-use wards with high shop mix (e.g., Koramangala/HSR, or Jayanagar/JP Nagar axis) — **`[VERIFY]` shortlist 3–4 candidate wards by OpenCity licence density before committing**.
- **Inclusion criteria:** shop in one of the 4 pilot verticals (kirana/grocery, appliance & electronics, electrical, auto-mechanic) × located in cluster × (licensed OR willing to formalise).
- **Denominator build (build-time task):** parse OpenCity BBMP licence CSVs → map trade-licence activity codes to the 4 verticals → ward counts. Kirana-style categories dominate retail licence counts `[ESTIMATED — typical municipal licence mix]`.
- **Illustrative sizing (NOT verified — method only):** if a ward carries ~300–600 trade-licensed premises and ~30–45% map to the 4 verticals, a 3-ward cluster yields **~270–800 eligible shops** `[ESTIMATED — replace with dataset computation]`. Our Entry-B gate is ≥100 verified merchants — feasible from one cluster if conversion ≥12–37% of eligible `[ESTIMATED]`.
- **Ground-truth sample:** field-walk 2–3 streets per ward (n ≈ 30–50 shops) to sanity-check licence-data coverage vs reality (unlicensed shops exist) `[plan item]`.

## 4. Demand side (catchment)
- Consumer catchment = walkable radius (kirana AOV ₹100–200 economics: no delivery economics at mass level `[VERIFIED — Redseer]`) → discovery must be **distance-first within the cluster**; pickup default, self-delivery optional.
- Bengaluru consumer base: UPI-native, quick-commerce-habituated (~51M QC users nationally `[VERIFIED]`) → the "trusted verified alternative" pitch must be explicit vs QC for urgent and vs Google Maps for discovery.

## 5. Risks & mitigations
| Risk | Mitigation |
|---|---|
| Licence-portal transition (BBMP→5 corps) | Dynamic portal/owner field; confirm per-corp ownership at build; open-data licence data may lag split |
| UPI→GST notice fear (KA-specific) | Enablement-first content; never fear-based; badge = benefit framing `[VERIFIED — SBI warning]` |
| Dataset freshness/coverage | OpenCity 2025 CSV + field sample; treat counts as floor |
| Governance churn (ward redraws) | Keep ward as soft tag, corporation as hard tag; don't hard-code ward IDs |

## 6. Open items `[VERIFY]`
1. Shortlist 3–4 candidate wards by OpenCity licence density (build-time task).
2. Confirm which corporation/portal now issues trade licences in the chosen wards.
3. Download + parse the 28 OpenCity CSVs → vertical-mapped denominator table.
4. KA S&E annual-return + registration portal specifics for 2026.
