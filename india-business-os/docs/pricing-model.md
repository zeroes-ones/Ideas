# Pricing & Monetization Model — SaaS-first (business owners) + options for individual providers

> **Date:** 2026-09-08 · **Owner:** founder · **Status:** DECISION for business owners (scope-brief OQ9, 2026-09-08); **options captured for individual providers** (rung I) pending OQ-I3 / OQ-V2.
> **Grounds:** `research/market-deep-dive.md` §D1 · `research/individual-providers-gig.md` (I1–I3) · `research/individual-verification-trust.md` (L1–L4, OQ-V2) · `docs/validation-interviews.md` Script A §A4. Tags: `[VERIFIED]` ≥2 sources/robust survey · `[ESTIMATED]` single-source/inference · `[VERIFY]` primary research.

## 0. One-line model
**SaaS-first, paid by business owners**: recurring subscription for the merchant OS (Launch Copilot journeys + renewals calendar + verified badge/storefront/deals). Consumer side is free and is the growth engine. **Individuals who provide services get a separate option set (§2), not the same subscription** — their economics, verification semantics, and legal frame differ.

---

## 1. Business owners (shops/registered businesses, ladder rungs XS → M) — DECIDED

**Decision (founder, 2026-09-08):** recurring subscription paid by business owners; consumer side free. Recorded in `scope-brief.md` "Pricing model" + OQ9. `[ESTIMATED — pending H1–H6/W38 price validation]`

**What the subscription must plausibly contain** (tier candidates; open — being tested in Script A §A4 Q14):
1. **Renewals calendar** — never miss a filing/renewal/fine (C5 sticky value; the market's "who reminds me about my next ROC filing?" gap, competitive-map §2.2)
2. **Verified badge presence** (badge + storefront + deals visibility — the growth asset)
3. **Launch Copilot journeys** (setup/registration guidance; possibly the onboarding/landing offer rather than the recurring core)

**Price anchors from research `[VERIFIED — market-deep-dive.md §D1]`:** billing tools = owners pay **₹500–4,000/yr**; Vyapar mobile ≈ ₹629–1,799/yr; OkCredit free (₹0 anchor); compliance bought as **events at ₹500–15k** (Clear/IndiaFilings/Vakilsearch). **Anchor resistance to any monthly fee is the core pricing risk.** Interview ladder under test: ₹49 / ₹99 / ₹149 / ₹199 / ₹299 per month (validation-interviews A4 Q13) → feeds the OQ9 price band + tier design.

**Anti-patterns (binding, unchanged):** no per-lead/listing fees (Justdial lesson, market-deep-dive D3/D5); never monetize consumers; transparent fees; never a paid look-alike of govt portals.

---

## 2. Individual service providers (rung I) — options under consideration

### 2.1 Why a *different* monetization set, not the business subscription
- **Earnings reality:** 40% of gig workers earn **<₹15k/mo**; all-cohort average ≈ ₹32k/mo (mostly part-time); platform gig ≈ ₹138/hr vs ₹54 informal (2.5×); home-services full-time ≈ ₹70–80k/mo net `[VERIFIED — Econ Survey 2025-26, Redseer 2026, UC disclosures]`. A ₹99–299/mo subscription is trivial for the full-timer but real for the 40% under ₹15k.
- **Today's monetization of individuals is hated:** upfront lead fees ₹40–250/lead + ₹3,000/mo subscriptions regardless of conversion + eroding commissions (partner example ₹55–60k/mo → ₹13k) `[VERIFIED — Mint/Forbes/NASSCOM-Foundation analyses]`. New entrants signal the opposite: **ProNearMe zero-upfront, commission-only** (150 AC pros/8 wks, May-2026); **HelpRush public pro pages + 20/12/8% tiers**; Swiggy Pyng "verified professionals" `[VERIFIED — vendor sources, directional]`.
- **No premises-licence regime** for individuals → trust = **ProBadge chips** (L1 identity / L2 background / L3 skill / L4 behaviour), not a compliance badge (individual-verification-trust.md). Monetization can't ride a "compliance calendar" for someone with no licences.
- **Legal frame:** if we *match* individuals as an aggregator in KA → Karnataka Gig Act 2025 obligations (Welfare Board registration, portable worker IDs, **1–5% welfare fee per payout**, weekly payouts, IDRC >50 workers) `[VERIFIED — individual-providers-gig.md §3]`. **Legal gate before marketplace-style matching (OQ-I2).**

### 2.2 The option set (research-grounded)
| Option | What it is | Evidence for/against | Fit vs guardrails |
|---|---|---|---|
| **A. Free verified core → outcome-linked later** | ProBadge profile (L1 eKYC + L4 order-verified ratings) free; platform earns an order-linked fee only when the provider actually transacts | For: ProNearMe zero-upfront traction; HelpRush tiered commission; UC-partner backlash to lead fees; worker demand for predictable earnings & customer ownership (gig-research §5) | Strong — outcome-based principle, no upfront cost to the poorest cohort, no lead-selling |
| **B. ProBadge subscription (light tier)** | e.g. ₹99–199/mo incl. profile + storefront/scheduling tools + amortized re-verification | For: matches SaaS-first; absorbable by full-timers (₹70–80k/mo). Against: ₹3,000/mo subscription precedent is hated; weak for <₹15k/mo cohort | OK only after value proven (option A first); must show visible ongoing value (badge travels, rebookings) |
| **C. Commission/order-fee from day one** | % per completed job | HelpRush 20/12/8% tiers exist `[VERIFIED]`; commission-only = ProNearMe model | Conflicts with pure "SaaS-first" framing for individuals; **aggregator trigger → KA Gig Act** — legal gate first |
| **D. Verification cost pass-through** | L1 ≈ **$0.15/check** (free-class); L2 police verification **₹50–200** govt or ₹100–500 vendor; L3 via govt schemes (ITI/NSDC/PM Vishwakarma) ₹0 + assessment `[VERIFIED — individual-verification-trust.md L1–L3]` | — | Who pays = OQ-V2: provider (entry cost), launch subsidy (trust supply needs density), consumer opt-in premium, or bundled into A/B |

**Directional recommendation (for founder to confirm, NOT yet decided):** **A first** — free ProBadge core for wave-C individual pilots (consistent with guardrails + the market's away-from-upfront-fees signal + worker economics); **B** only for cohorts whose earnings justify it once value is proven; **C** legal-gated (OQ-I2) and later; **D** priced per category after OQ-V2 interviews. L2 for home-entry categories only (beautician/plumbing/AC-at-home) per OQ-V1.

### 2.3 Open decisions (owner: founder, resolved via interviews)
- **OQ-I3 (individual-providers-gig.md):** A vs B vs C for individual providers → validate with a **provider variant of Script A** (price-ladder + "what would you pay for" probes); extend validation-interviews.md.
- **OQ-V2 (individual-verification-trust.md):** who pays L2/L3 verification costs.
- **OQ-I2:** legal review gate before any individual-matching marketplace (KA Gig Act).

---

## 3. Guardrails (binding across ALL options — business and individual)
Never hold funds (RBI PPI — payment via PA redirect only); **no per-lead charges of any kind**; never monetize consumers; outcome-linked monetization only; badge hides on non-compliance (business) and ProBadge stays **chips, never merged** into the compliance badge (LM2 audit); transparent fees; KA Gig Act obligations respected before any aggregator-style matching.

## 4. Validation hooks (where each open item gets answered)
| Item | Resolved by | Tool |
|---|---|---|
| Business price band + tier contents | H4 (merchant interviews) | validation-interviews.md Script A §A4 Q13–Q14 |
| Provider option (OQ-I3) | Provider-variant Script A (to be written) | extend validation-interviews.md |
| Verification cost bearer (OQ-V2) | Provider + consumer WTP probes | extend validation-interviews.md |
| Aggregator legal status (OQ-I2) | Lawyer review before individual onboarding | — |

## 5. Traceability
- Decision recorded: `scope-brief.md` (Pricing model assumption; OQ9 struck through) · `market-deep-dive.md` (override notes §D1, impl #2) · README §5.
- This doc consolidates the decision + individual options; amend it (not the research files) when OQ-I3/OQ-V2 resolve.
