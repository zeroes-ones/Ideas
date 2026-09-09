# Scope Brief — Two-Surface MVP (India Business OS) — Business Launch Copilot + Customer Trusted-Deals Marketplace
**Version:** 0.3 · **Date:** 2026-09-08 · **Status:** Draft for review (per idea-to-spec Phase 1)
**MVP = two full entry experiences** (founder decisions 2026-09-08): **Entry A — Business Launch Copilot** (v0.1, unchanged in direction) **+ Entry B — Customer Trusted + Deals**: verified discovery, **goods orders, service bookings, and merchant deals** — pilot verticals **kirana/grocery, appliance & electronics, electrical, auto-mechanic** (F&B deferred). One codebase, two role surfaces (vision.md v0.3; module-map.md §0/§2.5).

## Problem statement
**(A) Business side (v0.1):** first-time founders face a fragmented, jargon-heavy formalization journey (MCA/GST/Udyam/state portals), wrong-entity costs, opaque intermediaries, and first-year compliance traps.
**(B) Customer side (new):** Indian consumers ordering from local sellers can't tell who is **real, registered and compliant**, local trade shops (kirana, appliance/electrical, mechanics) have **no cheap way to be discovered or booked** and no way to run **trusted offers**, and big aggregators flood them with discounts from unverifiable sellers. Result: compliant SMBs get no advantage from formalizing, and the informal economy stays informal.

## Solution overview
One ecosystem, two surfaces. **Businesses** — from a very small street kirana to a mid-size multi-branch chain — are guided through registration & formalization (entity advisor → Launch Copilot journeys → first-year compliance calendar). Once a business reaches `formalizationState ≥ registered` with **no expired licences** for its vertical/state, it auto-earns a **verified badge**, a **storefront** (goods catalog + bookable service slots), and the ability to publish **deals**. **Customers** (pilot: Bengaluru + Hyderabad, run in parallel × grocery/appliance/electrical/mechanic) discover nearby **verified** merchants, browse real catalogs, **order goods or book service slots**, redeem **deals** (server-validated), pay via **UPI redirect through a payment aggregator (app never holds funds)** or pay-at-shop for services, and track fulfillment. Compliance becomes a growth asset: the badge is the supply-side gate, deals drive trial, bookings make services bookable.

## Target users
- **Entry A**: Sunita-type formalizer (Hindi-first, tier-2/3 → now also pilot-city), Rohan-type side-founder (EN, metro), and **individual providers starting at rung I** (solo earner → micro shop). Business side serves the full ladder **I → XS → S → M** in MVP scope (L/Corp = roadmap; see stage-model §0). States {MH, KA, DL, TN, GJ}.
- **Entry B (new):** Priya-type consumer — 28–45, urban (pilot city: Bengaluru/Hyderabad), UPI-native, wants trusted local shops, **service bookings (mechanic/appliance/electrical)**, and **genuine nearby deals**. Uses the customer surface; may also hold a business role.
- Pilot geography: **Entry A** = 5 states (regulatory, online/central portals). **Entry B** = pilot cities **Bengaluru (KA) and Hyderabad (TS) — both from day one, run in parallel** × verticals **kirana/grocery, appliance & electronics, electrical, auto-mechanic** (founder's example set; F&B deferred). **City = a config pack** (licence sets, portals, municipality) exactly like vertical packs — two cities is the earliest proof of that design. Business side serves the **individual → very small (street/micro) → small → medium ladder** (stage-model §0; L/Corp = roadmap); Entry B supply gate ≥100 verified merchants **per city** `[ESTIMATED]`. Parallel pilots double the supply-ramp/field effort — founder capacity is the binding constraint (see W39 sizing).
  - Pilot unit = **ward cluster within one of the 5 GBA municipal corporations** (BBMP dissolved 1-Sep-2025; **369 wards** from Nov-2025 delimitation; elections held Jun-2026 `[VERIFIED — research/bengaluru-pilot-map.md §1]`). Denominator = **OpenCity BBMP trade-licence CSVs** (BBMP-era 198-ward map — re-map at build) → verticals at build time. KA-specific: **UPI→GST notice sensitivity** (2025 trader protests) → enablement framing mandatory `[VERIFIED — SBI Research]`. · Hyderabad (TS) mirror unit — research pass run 2026-09-08, see `research/hyderabad-pilot-map.md`: GHMC trade-licence regime (online portal, calendar-year renewal, Dec cluster), TS S&E (Form I→II, Telugu name-board requirement, fees by headcount), Telugu i18n needed; **Telangana Gig Workers Act 2026 passed 30-Mar-2026, assented May-2026, in force ~15-Aug-2026 (1–2% welfare levy) `[VERIFIED — 2026-09-08 web pass]`** → both pilot states now regulate platform work (KA 1–5% vs TS 1–2% levy) — the OQ-I2 legal gate applies in BOTH cities.

## Success metrics (two-sided; leading → lagging)
| ID | Metric | Target | Side |
|---|---|---|---|
| SM1–SM6 | v0.1 funnel: quiz completion → journey start → registered ≤45d → D30 → clarity CSAT → NPS | as v0.1 | Business |
| CM1 | Discovery view → storefront open | ≥40% | Customer |
| CM2 | Storefront → order placed | ≥15% | Customer |
| CM3 | Order placed → completed (paid/delivered) | ≥60% | Customer |
| CM4 | Repeat order/booking ≤30 days | ≥25% of first-order buyers | Customer |
| CM5 | Service booking requested → confirmed by merchant | ≥50% | Customer |
| CM6 | Orders placed with a valid deal | ≥10% of orders by month 3 | Customer |
| LM1 | % orders from merchants onboarded via app (≤90d of activation) | ≥40% by month 3 | Ecosystem |
| LM2 | No consumer-facing badge on an out-of-compliance merchant (weekly audit) | 100% | Trust |

Pre-launch proxies (ITS9): usability tests — 5 business founders complete entity quiz + first journey task unassisted; 5 consumers complete discovery→order in pilot sandbox with seeded merchants.

## Scope boundaries
**IN (MVP, Entry A + Entry B):**
- Entry A v0.1 IN list (auth/OTP bilingual, profile+stage, entity advisor, journey engine w/ Pvt Ltd/OPC/LLP/proprietorship + GST/Udyam/S&E paths, task content + official links + manual milestones, document vault, fee transparency, post-registration deadline seed) — **unchanged**.
- Entry B: role gate + role switch; consumer discovery (location/vertical/**verified filter**/search + **nearby-deals feed**); verified merchant storefront (badge + licence summary + contact + active deals); **goods listings** (manual entry, price w/ GST flag, stock, photos) **and service listings** (price-basis + duration); **goods orders (cart→place)** and **service bookings (slot pick from merchant availability → request → merchant confirm)**; order/booking status timeline; **UPI payment via PA redirect** for goods (POD/manual fallback pre-PA) and **pay-at-shop for service bookings**; **merchant deals engine** (flat ₹/% off, validFrom/To, listing-scope optional, caps — server-validated at checkout); business order inbox (accept/fulfill/decline) with appointments tab; **availability manager** (weekly schedule → slots); post-completion ratings (order-verified); seeded demo merchants for pilot.
- Badge rule + daily recompute (B1) and order core (B0) as shared services.

**OUT (explicit non-goals):** wallet/escrow/funds holding (RBI PPI — never); payment-gateway operations (PA partner only); delivery fleet/logistics (merchant self-delivery / pickup / POD); full coupon/affiliate/offers-API machinery (deals = merchant-created simple offers only); dynamic pricing or cashback/loyalty programs; promoted placements/ads (paid later); **Justdial-style paid-lead selling / directory PPL (anti-pattern: charge for customers who transact, never for fake leads)**; **billing/ledger/GST-invoicing suites (Vyapar/OkCredit-class — Run layer is a free/cheap red ocean `[VERIFIED — research/market-deep-dive.md §D1]`)**: multi-city consumer rollout; verticals beyond **kirana/grocery, appliance & electronics, electrical, auto-mechanic** on the customer side (F&B deferred); real-time MCA/GST status scraping; CA marketplace; team accounts; manufacturing/creator packs.

## Assumptions (validate Phase 4/founder)
- Solo builder TS/Node/PWA; one codebase two roles; i18n EN+HI (consumer screens: storefront/checkout priority for HI).
- Payments: UPI intent redirect via a chosen payment aggregator; webhook signature verification; **no fund holding**; POD/manual until PA onboarding. `[RBI PA/UPI model — verify partner onboarding in build]`
- Catalog: manual listing entry by merchants in MVP (seeded + assisted); goods + service listings; **service availability = weekly schedule configured by merchant**; no POS/inventory integration.
- Deals (MVP scope): flat ₹ or % off, optional listing-scope, `validFrom/To`, optional redemption cap; presented as "offer price" (no MRP-crossed claims) `[VERIFY consumer-protection display norms]`.
- Service bookings default **pay-at-shop**; no prepay/deposit until PA economics decided (P1).
- Verified badge = derived view from compliance state (formalizationState ≥ registered ∧ no expired required licences/deadlines for vertical+state); recomputed daily + on state change.
- Consumer MVP quality gate: launch a city's consumer surface only when ≥100 verified merchants exist **in that city** — Bengaluru and Hyderabad gate independently, in parallel `[ESTIMATED]`.
- Size ladder: business side serves the **growth ladder I → XS → S → M** (individual/solo earner incl. Udyam-Assist + ProBadge path → very small street/micro, turnover < GST thresholds → small → medium; stage-model §0); L/Corp = roadmap. Pack/licence config is rung-aware (employees/turnover triggers EPFO/ESIC/audit/PF hints; graduation events upgrade the profile in place, never restart).
- **Pricing model — SaaS-first from business owners (founder decision 2026-09-08) `[ESTIMATED — pending H1–H6/W38 price validation]`:** recurring subscription paid by **business owners** for the merchant OS (Launch Copilot journeys + renewals calendar + verified badge/storefront/deals presence); the consumer side stays free and is the growth engine. Research context `[VERIFIED — market-deep-dive.md §D1]` still anchors the price point: compliance is event-priced today (Clear/IndiaFilings/Vakilsearch sell one-off assisted filings) and billing tools anchor merchants near ₹0 (Vyapar mobile ~₹629–1,799/yr; OkCredit free) → expect anchor resistance to a monthly fee; the subscription's job is calendar value (fines/filings avoided) + growth value (badge → orders). Never per-lead charges; never monetize consumers. **Individuals (rung I) = ₹0 free verified core (OQ-I3 resolved 2026-09-08); businesses XS→L pay the subscription — full model in `docs/pricing-model.md`.**
- **Discovery positioning (from `[VERIFIED — market-deep-dive.md §D3]`):** wedge = verified-compliance tied to discovery — Google Maps has reach but no compliance signal/loop; Justdial lost trust (paid leads); ONDC has no trust layer. We are not "another directory/marketplace".

## Open questions (owner: founder / research)
1. PA partner selection & fee economics for MVP orders (owner: founder).
2. Pilot supply ramp: target verified-merchant count + acquisition path to reach the ≥100 gate (owner: founder). **Plan now exists:** `docs/pilot-recruitment-playbook.md` + work items W35–W40 (denominator from OpenCity licence data → field sample → outreach kit → weekly funnel).
3. Consumer demand validation: verified badge vs **deals pull** vs **booking convenience** — which drives first orders? ≥10 interviews + pilot A/B (owner: founder).
4. Service availability & booking workflow readiness of mechanics/appliance shops (do they keep a calendar? slot model vs call-first) (owner: founder).
5. Deal rules MVP scope + no-show/reminder policy for bookings (owner: founder).
6. Catalog sourcing: assisted manual entry vs seeded catalogs per vertical (owner: founder).
7. Delivery model for pilot: pickup/self-delivery/POD mix (owner: founder).
8. v0.1 OQs retained: quiz logic validation, pricing, hosting/auth/OTP; + pack-licence `[VERIFY]` items from module-map §2 (owner: founder/research).
9. ~~Journey vs subscription~~ → **model resolved (founder, 2026-09-08): SaaS-first, paid by business owners** (see Pricing model assumption above). Remaining validation: monthly price point (vs ₹0 free tiers of Vyapar/OkCredit) and what a subscription must include to justify recurring payment (calendar alone? badge/storefront/deals tiers?) — H1–H6 / W38 interviews (owner: founder).
10. Governance-timing risk: BBMP→5-corporation licence-portal transition — confirm which body issues trade licences in chosen Bengaluru wards before pilot config freeze; Hyderabad: GHMC trade-licence routing + Telangana S&E regime `[VERIFY]` (owner: founder/research).

---
## Appendix A — Spec quality checklist (idea-to-spec ITS, run 2026-09-08 v0.3)
- [x] ITS1 Scope Brief w/ both entry experiences, two-sided metrics, in/out, open Qs → this doc.
- [x] ITS2 Domain model incl. consumer/order/payment/review entities + **service booking & deal entities/states** → domain-model.md.
- [x] ITS3 API contract w/ role-scoped authN/authZ, consumer + business-order endpoints → api-contract.md.
- [x] ITS6 Screen inventory: business S1–S15 (incl. order inbox + role gate + manager screens) + customer S16–S24 w/ states & a11y → screen-inventory.md.
- [x] ITS7 MVP boundary explicit (two entry experiences IN; wallet/logistics/coupon-machinery OUT).
- [x] ITS8 Work items: two-entry slices, sequenced (supply before demand), sized → work-items.md.
- [x] ITS9 Pre-launch proxies (usability tests: founder quiz→task; consumer goods order **+ service booking + deal redemption** in pilot sandbox).
- [x] Cross-doc consistency (v0.3 run): role model, badge rule, metric IDs (SM/CM/LM incl. CM5/CM6), pilot verticals (grocery/appliance/electrical/mechanic) aligned across vision/module-map/scope/domain/api/screens/work-items.
- [ ] ITS4/5/10/11/12: data provenance itemization, NFRs, change control, founder sign-off, post-mortem — deferred as v0.1 (Appendix A of v0.1).
