# Vision — "India Business OS" → Two-Sided Super App (working title)
**Date:** 2026-09-08 · **Version:** 0.3 (four-pillar customer side) · Author: session agent for the founder
**Status:** Vision updated at decision gate (2026-09-08). Founder decisions: positioning = Lifecycle OS for business owners **+ consumer side**; "2 verticals" = **two user sides** (customers vs business owners); MVP = **two full entry experiences**; consumer value = **trusted + deals + nearby deals**: verified discovery + goods orders + **service bookings** + **merchant deals**, piloting **kirana/grocery, appliance & electronics, electrical, auto-mechanic** (F&B deferred); scale ladder **very small (street/micro) → small → medium → large**.

## 1. Vision statement
A two-sided ecosystem (a "super app" in the making) on **one shared core**:
- **Business-owner side**: guide anyone — from an **individual earner** (solo provider, home-based maker) up through **very small → small → medium → large → corporate** — through registration & formalization (Launch Copilot), then stay with them as they comply, run, and grow on one adaptive growth ladder (`docs/stage-model.md` §0) — any business type A-Z via vertical packs (this side is speced in v0.1 and unchanged in direction).
- **Customer side**: let consumers find **nearby businesses that are verified** (registered, GST/Udyam/licences current) **and deal-ready** — browse real catalogs **and bookable services** (repair, installation), place goods orders or **book service slots**, grab **nearby deals**, pay via UPI (or pay-at-shop for services), and track fulfillment. **Trust + value is the differentiator** ("badged, compliant, and offers nearby") rather than competing on breadth or discounts with big aggregators.
The two sides are a loop: businesses the OS helps formalize become the verified supply that customers order from; customer demand rewards merchants for staying compliant — compliance becomes a growth asset, not a tax.

## 2. Personas (specific)
**Business side (unchanged from v0.1):**
- **Sunita** (38, tier-2/3 → now Bengaluru pilot): runs a small kirana/grocery shop, formalizing to take digital orders + offers; Hindi-first, wants honest guidance + the customer-facing badge.
- **Rohan** (29, Bengaluru): salaried side-founder choosing entity correctly; English-first.
**Customer side (new):**
- **Priya** (34, Bengaluru): orders groceries/meals online; switched off by unverifiable sellers and fake listings; wants a shop she can check is **real, licensed, GST-registered** before ordering, **books the local mechanic/appliance repair by slot**, and **grabs a genuine nearby deal** without discount tricks; UPI-native, values speed + local options.

## 3. Product summary (the two entry experiences = MVP)
- **Entry A — Business (Launch Copilot)**: entity advisor → guided registration journeys (MCA/GST/Udyam/licences) → first-year compliance calendar → later run/grow modules. v0.1 spec unchanged.
- **Entry B — Customer (Trusted + Deals)**: role-gated discovery of nearby **badged** merchants (badge = formalizationState ≥ registered + no expired licences/deadlines); storefront with real catalog & prices **for goods and services**; **goods orders** and **service bookings** (date/time slots for mechanic, appliance install/repair, electrical jobs — pay-at-shop default); **merchant-created deals** surfaced as a "nearby deals" feed and on storefronts, server-validated at checkout; **UPI payment via PA redirect (app never holds funds)**; order/booking status timeline; post-completion ratings. Pilot cities: **Bengaluru + Hyderabad — both from day one, in parallel** × **kirana/grocery, appliance & electronics, electrical, auto-mechanic** (very small street shops through mid-size multi-branch in later packs).
- Same phone number can hold both roles; one codebase, two surfaces (PWA role switch).

## 4. Decision record
- Concept A (Guided Lifecycle OS) won v0.1 scoring; **v0.2 extends it with a consumer surface** — user decision. Two-role architecture (single codebase + role gate) chosen over two separate apps: shared BusinessProfile/order core, cheaper to operate solo.
- Consumer **near-term** = verified discovery + UPI orders. **North-star** (wallet, multi-service, broader commerce) explicitly deferred — holding money requires RBI PPI/PA licensing; MVP uses a PA partner's UPI redirect and never touches funds. DPDP Act applies → phone-only PII, consent-based.

## 5. Packaging & monetization — SaaS-first from business owners (founder decision 2026-09-08; full capture in `docs/pricing-model.md`)
- Business side: **recurring subscription paid by business owners** for the merchant OS (Launch Copilot journeys + renewals calendar + verified badge/storefront/deals). Consumer side is free = growth engine. No per-order take-rate, no paid listings/placement, no consumer subscription.
- Individual providers (rung I, ProBadge): **₹0 free verified core — DECIDED 2026-09-08** (no subscription, no commission, no lead fees for solo earners; the ladder monetizes at graduation to XS+). Verification govt fees (L2, home-entry) bearer = **OQ-V2 open** — see `docs/pricing-model.md` §2.
- Guardrails: transparent fees; never a paid look-alike of govt portals; no per-lead charges; never monetize consumers. `[ESTIMATED — price band/tiers pending H1–H6]`

## 6. Success metrics (two-sided)
| ID | Metric | Target | Side |
|---|---|---|---|
| SM1–SM6 | v0.1 business funnel (quiz→registered→D30→CSAT→NPS) | as speced | Business |
| CM1 | Discovery view → storefront open | ≥40% | Customer |
| CM2 | Storefront → order placed | ≥15% | Customer |
| CM3 | Order placed → completed (paid/delivered) | ≥60% | Customer |
| CM4 | Repeat order/booking within 30 days | ≥25% of first-order buyers | Customer |
| CM5 | Service booking requested → confirmed by merchant | ≥50% | Customer |
| CM6 | Orders placed with a valid deal | ≥10% of orders by month 3 | Customer |
| LM1 | Loop: % orders from merchants onboarded via the app (≤90 days of merchant activation) | ≥40% by month 3 | Ecosystem |
| LM2 | Badge integrity: no consumer-facing badge on an out-of-compliance merchant (audit, weekly) | 100% | Trust |

## 7. MVP boundaries (two entry experiences)
**IN:** Entry A (v0.1 scope) · Entry B: role gate, discovery (location/vertical/verified filter + **Nearby Deals**), storefront w/ badge + catalog (**goods & services**) + deal chips, **goods orders + service bookings (slot + pay-at-shop)**, UPI redirect payment via PA, order/booking status, delivery notes (pickup / self-delivery / POD), basic ratings; pilot Bengaluru + Hyderabad (parallel, from day one) × **grocery, appliance & electronics, electrical, auto-mechanic**.
**OUT (explicit):** wallet/escrow/funds holding; delivery fleet/logistics; payment gateway operations (PA partner only); consumer subscriptions; coupon/affiliate machinery, dynamic pricing, cashback/loyalty; ads; multi-city consumer rollout; verticals beyond the 4 pilot packs (F&B etc.); team accounts; real-time portal integrations.

## 8. Risks & mitigations (additions to v0.1)
1. **Chicken-and-egg** → sequencing: business side (supply) first; consumer pilot only in a city/vertical where ≥N verified merchants exist (target ≥100 `[ESTIMATED]`); measure LM1 from day 1.
2. **Payments** → no fund holding; UPI intent redirect via PA; webhook signature verification; POD/manual fallback before PA onboarding.
3. **Badge integrity/trust abuse** → badge is a derived view recomputed daily + on compliance-state change; suspension on expiry; review moderation (no anonymous abuse); DMCA-style merchant dispute flow (later).
4. **Discovery competition** (Swiggy/Zomato/Zepto/PhonePe/Paytm/Google) → compete on **verification + local SMB loop**, not breadth or discounts `[ESTIMATED positioning]`; single-city focus for learning.
5. **Regulatory** → DPDP consent + minimal PII; no payment intermediation; content currency discipline (v0.1 risks retained).
6. **Deal integrity (v0.3)** → deals are real-time validated offers (`validFrom/To`, caps, listing-scope); no fake-MRP claims — present as "offer price" with legal framing `[VERIFY consumer-protection/MRP display norms at build]`; merchant abusing deals loses deal capability (not badge) first.
7. **Booking no-shows (v0.3)** → service bookings default pay-at-shop; merchant confirms slots; consumer + merchant reminders; no-show history shown to merchants (fair-use policy P1); deposit/prepay for no-show-prone services deferred with PA.

## 9. Open validation questions
Consumer demand test (would a "verified & compliant" badge change ordering behavior? ≥10 interviews); **deal pull test (does "nearby deals" drive first orders vs trust badge alone?)**; **booking demand test (slot booking vs call/WhatsApp for repair services — mechanics' workflow readiness)**; pilot city confirm; PA partner selection; catalog + **service-availability** sourcing (manual vs assisted); delivery model for pilot (self-delivery/pickup/POD); no-show & reminder policy; FSSAI basic band for kirana packs `[VERIFY]`.
