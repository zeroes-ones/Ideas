# Research Brief — Consolidated (india_os_07)
**Date:** 2026-09-08 · Consolidates `regulatory-journey.md` + `competitive-map.md` + internal asset audit.

## 1. Internal asset audit (captured 2026-09-08)
- **`b2b-price-intel` project** (no longer present in this workspace as of today; patterns below were captured earlier in-session and are advisory, not hard dependencies):
  - Stack: TypeScript (strict, `tsc --noEmit` typecheck), Node ≥20 with `--experimental-strip-types` test runner, zero-runtime-dependency PWA (manifest + service worker in `src/app/`), domain folders per bounded context (`khata`, `storefront`, `supplier`, `price`, `dashboard`, `shop`).
  - i18n: dedicated `src/i18n/` with per-module `validate-i18n` script (catches missing/extra keys) — **reusable pattern for the EN+Hindi core**.
  - Spec discipline: 5-doc pattern (`scope-brief.md`, `domain-model.md`, `api-contract.md`, `screen-inventory.md`, `work-items.md`) + per-domain `validate-*` scripts — the house style this project will mirror.
- **18-idea brainstorm pool** (`.brainstorm-session/` artifacts were removed externally; pool content retained in-session) → folded into the module map below.
- **Skills library** at `/Users/sp.vm/Documents/Projects/Skills` (299 skills): idea-to-spec, brainstorming, product-strategist, saas-monetization-strategist, enterprise-pricing-strategist, localization-engineer, compliance-officer, tax-strategist, accountant, business-strategist, customer-onboarding-specialist, ux-researcher → methodology + content substrate for Phases 2–3.

## 2. Consolidated insights
- **Founder pain is fragmentation + opacity**: 4–6 portals (MCA, GST, Udyam, state labour, municipal, FoSCoS), each English-heavy with its own login; no cross-portal sequencing; fees split govt vs professional and opaque; paid look-alike sites prey on first-timers. Post-registration, deadline anxiety (INC-20A 180d, auditor 30d, AGM, DIR-3 KYC, renewals) is the recurring retention surface.
- **Incumbents are filing transactions or tax software**; nobody owns the guided adaptive lifecycle, proactive first-year calendar, or bilingual tier-2/3 UX. Their model structurally under-serves "what's due next quarter" (documented industry admission).
- **Segments** (for the size × type matrix):
  - Micro (proprietorship/OPC, ≤10 employees, ₹<40L): formalization-first; needs Udyam+GST+S&E guidance and cheap compliance. Largest volume.
  - Small (LLP/Pvt Ltd, 10–99 emp): compliance calendar + licence renewals + payroll triggers (EPFO at 20+, ESIC at 10+).
  - Medium (Pvt Ltd, 100+ emp, ₹>100Cr): multi-state branches (per-state S&E/GST), audit, board compliance — served later via packs.
  - Business types A-Z → **vertical packs** = licence/registration bundles (retail/kirana, F&B, services/consulting, e-comm seller, manufacturing, gig/freelance…).

## 3. Seed module map (common core + vertical packs) — drafted for Phase 2
**Common core (all types, S→M→L):**
| Module | Stage | Source seed |
|---|---|---|
| Entity advisor (quiz → recommendation w/ ongoing-cost warnings) | Start → Formalize | pool A/B (entity decision), regulatory §7.1 |
| Launch Copilot (guided registration journeys, task engine, doc readiness, official links, govt-fee transparency) | Formalize | **MVP slice** |
| First-year compliance calendar (INC-20A, auditor, AGM, DIR-3 KYC, GST returns, renewals; bilingual reminders) | Comply | competitive whitespace #2 |
| Document vault (upload, expiry/renewal tracking) | Comply → Run | pool D1-style |
| Ledger starter (invoice/khata/GST-ready, deferred to run phase) | Run | pool A2/E1-ish; incumbent lane, later |
| Marketplace enablement later: expert-assisted filing, CA marketplace (vetted, transparent) | Grow | pool F1-style trust layer |

**Vertical packs (A-Z, added per traction):** Retail/kirana (S&E + trade licence + GST + Udyam; later price-intel via b2b-price-intel pattern), F&B (FSSAI + fire/health NOC + eating-house), Services/consulting, E-commerce seller (GST day-1), Manufacturing (consent/foam/etc.), Freelance/gig.

## 4. Open questions & Phase-4 re-verification list
Status: Phase 4 re-verification run 2026-09-08.
1. ~~GST special-category state list discrepancy~~ **RESOLVED** — two distinct rules (services ₹10L constitutional special-category; Notification 10/2019 goods carve-outs incl. Puducherry/Telangana at ₹20L). All 5 MVP states are normal-category (goods ₹40L/services ₹20L) → MVP unaffected; encode both rules with a CBIC-verify flag before enabling any other state. (regulatory-journey.md §3 updated.)
2. ~~MSME classification~~ **RESOLVED** — Apr-01-2025 criteria (micro ≤₹2.5Cr/₹10Cr; small ≤₹25Cr/₹100Cr; medium ≤₹125Cr/₹500Cr) corroborated by multiple Nov-2025 sources (Tally, SMFG, Motilal Oswal); stale pre-2025 figures still circulate online → content-hygiene rule stands: always tag `asOf` and re-verify on publish.
3. MCA "24h DIN/name approval, AI MOA/AOA matching" 2026 claims — **vendor-sourced only `[ESTIMATED]`**; keep as vendor-claim in content, do not publish as official timeline; in-app timelines use 1–3 working days (name) / 7–15 days (full registration) which are multi-source `[VERIFIED]`.
4. ~~FSSAI tier bands + FoSTaC~~ **RESOLVED** — tiers Basic ≤₹12L ₹100 / State ₹12L–₹20Cr ₹2,000–5,000 / Central >₹20Cr ₹7,500 corroborated (Regikart 2026-06, VirtualAuditor 2026-04); FoSTaC training mandatory for food handlers. (regulatory-journey.md §5 patched.)
5. ~~S&E validity by state~~ **RESOLVED** — 5-yr most states, Maharashtra 1-yr (RTI wiki 2026-04 + corroboration). State portal links per MVP state still to be collected in build. (regulatory-journey.md §5 patched.)
6. Persona/pricing validation with ≥5 founder interviews — **NOT DONE (explicitly deferred to founder)**; success metrics in scope-brief.md §SM1–SM6 assume current targets.

## 5. Source index (top-level)
MCA/SPICe+ incorporation guides (citizennest, cessassociates, pkcconsultancy 2026), GST: CGST Act §22/§24 references via ClearTax/TaxGuru/Motilal Oswal/Godrej Capital 2025, Udyam: portal guidance via Motilal Oswal/Tally/TaxGuru 2025-11, licensing: Regikart (2026-06), Virtual Auditor (2026-04), RTI wiki S&E (2026-04), Petpooja restaurant compliance; competitive: Vakilsearch 2026 rankings/comparisons, Legalsuvidha 2026 comparisons, eBizFiling 2026-02.
