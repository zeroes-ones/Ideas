# Hyderabad Pilot Research Stub — Parallel pilot city (Telangana/GHMC)

> **Date:** 2026-09-08 · **Status:** PARTIAL RESEARCH PASS RUN 2026-09-08 (web): GHMC trade-licence + Telangana S&E + gig-Act status now `[VERIFIED]` below; denominator open-data availability and zone granularity remain `[VERIFY]`. Everything untagged is **assumption**. Run the W35b pass before freezing Hyderabad config.
> **Tags:** `[VERIFIED]` · `[ESTIMATED]` · `[VERIFY]` — same discipline as every research doc. Purpose: give partners/founder the honest starting point and the exact research checklist.

## 1. Why Hyderabad (parallel pilot city)
- Same 4 pilot verticals (kirana/grocery, appliance & electronics, electrical, auto-mechanic) in an **additional state regime** → proves the "city = config pack" design (different licences, portals, municipality) early `[design assumption]`.
- **Legal posture for the individual-provider roadmap — UPDATED 2026-09-08:** Telangana's **Platform-Based Gig Workers (Registration, Social Security & Welfare) Act, 2026** was passed 30-Mar-2026, assented 1-May-2026, guidelines finalised Aug-2026, **in force from ~15-Aug-2026** `[VERIFIED — Telangana Today/ANI 30-Mar-2026; Deccan Chronicle 4-Aug-2026]`. Aggregator obligations: Welfare-Board registration within 45 days of commencement, worker unique IDs, **1–2% welfare levy on transaction value** (vs Karnataka's 1–5%), quarterly electronic returns, IDRC for platforms ≥100 workers, penalties ₹50k/₹1L/₹1.5L then 5× arrears. **Both pilot states now regulate platform work** — the "lower-regulatory testbed" claim is obsolete; contrast is now levy/obligation *depth* (KA 1–5% vs TS 1–2%), not presence-vs-absence. Legal gate (OQ-I2) applies in BOTH cities.
- Founder decision (2026-09-08): Hyderabad runs **in parallel with Bengaluru from day one** (both cities gate independently at ≥100 verified merchants).
- **Market ground truth (formalization gap):** GHMC identified **2.49L non-compliant non-residential properties of 3.17L** (Dec-2024) and ordered enforcement — a ~78% trade-licence compliance gap, a strong formalization-whitespace signal for the city `[VERIFIED — RegisterKaro citing GHMC enforcement, Dec-2024]`.

## 2. Governance & licence ground truth — partially verified (mirror of Bengaluru §1)
| Item | Bengaluru (done) | Hyderabad (status) |
|---|---|---|
| Municipal body | 5 corporations post-BBMP split; 369 wards `[VERIFIED — bengaluru-pilot-map.md]` | **GHMC** issues trade licences under Telangana Municipalities Act 2019; online via ghmc.gov.in "Online Services" since 28-Oct-2025 (previously MeeSeva-only); TIN (Trade Identification Number) per premise `[VERIFIED — The Hindu/Siasat/DC Oct-2025]`. Ward count + zone/circle map for clusters `[VERIFY]` |
| Trade-licence data source | OpenCity BBMP licence CSVs (W35) | GHMC portal is application/self-service; **no known open CSV** → denominator likely needs the W36 street walk + GHMC records request, not a bulk file `[VERIFY — treat as no-open-data until disproven]` |
| **Trade-licence calendar (city-pack config!)** | KA-specific regime (see bengaluru doc) | **Calendar-year validity (1 Jan–31 Dec); renewal/new applications due ~1 Dec; no penalty to ~20 Dec; +25% to ~19 Feb; +50% after** `[VERIFIED — Telangana Today Nov-2025]` → Dec is Hyderabad's renewal cluster for the C5 calendar |
| Shop & Establishment regime | Karnataka S&E (labour dept) | **Telangana S&E (Act 1988), TS Labour Dept portal (labour.telangana.gov.in): Form I → Form II, fully digital, deemed approval 30 days, 3–7 working-day typical. Fees by employee bracket ₹100 (0 emp) → ₹500 (1–5) → ₹1,000 (6–10) → ₹2,000 (11–20) → ₹5,000 (21–50) → ₹10,000 (51–100). Annual renewal to 31-Dec (late: +25% Dec 2–31, +50% after 1-Jan). ₹1,000/day operating-without-certificate penalty** `[VERIFIED — Keka TS Form I guide; IndiaFilings Jun-2026]` |
| **Telugu name-board photo required** for S&E | N/A | **Registration + amendments require a Telugu name-board photo** `[VERIFIED — Keka/CharteredOne/IndiaFilings]` → a real, documented Telugu-content requirement for the Launch Copilot content pack (not just consumer i18n) |
| Udyam/GST/FSSAI | Central portals (same as Bengaluru) | Same central portals ✅ (no state variance) |
| Professional tax | KA regime | **Telangana professional tax enrolment triggers on first hire** (alongside S&E) `[VERIFIED — pnpcglobal/RegisterKaro]` → add to employee-trigger config |
| Local sensitivity | KA UPI→GST notice protests → enablement framing mandatory `[VERIFIED]` | TS equivalent risk scan (2024–26 trader/compliance news, incl. gig-worker union strikes Aug-2026) `[VERIFY]` |
| Language | EN + Hindi | **EN + Hindi + Telugu — now VERIFIED as needed** for business side (Telugu name board is a licence requirement); consumer-screen i18n decision still `[VERIFY — interviews]` |

## 3. Denominator & cluster method (mirror)
- W35b (work-items): GHMC trade-licence data → map activity codes to the 4 verticals → zone/circle counts → shortlist 3–4 candidate clusters by vertical density. **Constraint:** no confirmed open GHMC CSV → plan for street-walk-heavy denominator (W36 protocol) unless a data source turns up `[VERIFY]`.
- Note: Hyderabad's administrative unit for a "cluster" may be GHMC **zone/circle** rather than ward — confirm unit granularity before cloning the Bengaluru cluster plan `[VERIFY]`.

## 4. What this changes in the product/docs (already updated 2026-09-08)
- City = config pack: `scope-brief.md` pilot geography + OQ10; `PARTNER-BRIEF.md` §9/§13/§15; `work-items.md` W35b; `vision.md` pilot line; `validation-interviews.md` screeners; `marketplace-audit.md` Gap A (per-city + per-cluster gate).
- **New verified city-pack config facts:** Hyderabad trade-licence + S&E both renew on the **calendar year (Dec cluster)** → C5 renewals-calendar content; Telugu name-board photo = document requirement in Launch Copilot journeys; professional-tax trigger on first hire; TS Gig Act 2026 = second-state regulatory regime for individual providers (levy 1–2%).

## 5. Open items for the Hyderabad pass (owner: founder/research)
1. ~~GHMC trade-licence data~~ → **portal is online but no open CSV confirmed** — sub-question: any GHMC/TS open-data release or scrape-able directory? Else denominator = street-walk + records request `[VERIFY]`
2. ~~Telangana S&E portal & fees~~ → **RESOLVED** (see §2) `[VERIFIED]`
3. GHMC zone/circle map + vertical density per unit — still needed for the cluster gate `[VERIFY]`
4. Telugu i18n: business side needed `[VERIFIED]`; consumer-screen i18n need `[VERIFY — interviews]`
5. Telangana trader/compliance-sensitivity scan (framing calibration; incl. Aug-2026 gig strikes context) `[VERIFY]`
6. ~~Gig/draft-Act watch~~ → **RESOLVED: TS Act 2026 passed & in force (~15-Aug-2026)** — replace with implementation watch: Welfare-Board rules, levy collection mechanics, aggregator-registration portal `[VERIFY — re-check quarterly]`

