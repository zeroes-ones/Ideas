# Lifecycle OS — Module Map (india_os_10, updated 2026-09-08 to two-sided)
**Date:** 2026-09-08 · **v0.2:** adds the customer-side module registry (D-series) and the two-role access model. Common core (works for all types A-Z) + vertical packs. Priorities: P0 = MVP slice, P1 = first-year, P2 = year-2, P3 = later. Monetization tags are assumptions `[ESTIMATED]`, finalized in vision/Scope Brief and `docs/pricing-model.md` (SaaS-first from business owners, 2026-09-08).

## 0. Two-role access model (v0.2)
One codebase/account base; a phone number can hold **both roles** (JWT claim `role=consumer|business` per session):
- **BusinessRole** — operates C1–C9 on their own BusinessProfile (owner surface; screens S1–S14).
- **ConsumerRole** — uses D1–D6 against **verified** merchant profiles (customer surface; screens S15+).
- Shared core: BusinessProfile (as Merchant), Orders, Payments-intent (UPI redirect), Reviews — no duplication of identity or order data.

## 1. Common-core module registry
| ID | Module | Stage(s) | Function | Priority | Monetization | Source seed |
|---|---|---|---|---|---|---|
| C1 | **Entity advisor** — quiz → recommendation (liability/funding/tax/ongoing-cost trade-offs, "wrong-entity warning") | S1→S2 | F1 | P0 (MVP) | Free (acquisition) | regulatory §7.1; competitive whitespace #5 |
| C2 | **Launch Copilot journeys** — guided prerequisite-ordered task engine per entity + state + type; doc readiness; official-portal deep links; govt-vs-professional fee transparency; status tracking | S2 | F3 | **P0 (MVP slice)** | Paid journey (e.g., ₹499–₹999 `[ESTIMATED]`) | user decision; regulatory §7.2 |
| C3 | **Profile & stage tracker** — one business profile that adapts the module surface as it climbs the growth rungs **I→XS→S→M→L** | all | — | P0 (MVP, thin) | Free | stage-model §0/§1 |
| C4 | **Document vault** — upload, organize, expiry/renewal tracking, checklist of docs per task | S2→S4 | F5 | P1 (thin in MVP) | Free (retention) | pool D1-style |
| C5 | **First-year compliance calendar** — INC-20A (180d), auditor (30d), AGM, DIR-3 KYC, GST returns, licence renewals, PF/ESI triggers; bilingual reminders | S3 | F2/F3 | P1 | Paid tier | competitive whitespace #2 |
| C6 | **Licence recommender** — type × state × employees × premises → vertical licence checklist | S2 | F3 | P1 | Free (tie to journeys) | regulatory §5 |
| C7 | **Ledger starter** (invoice/khata/GST-ready) — bridge to returns | S4 | F2 | P2 | Paid | incumbent lane (late) |
| C8 | **Expert layer / CA marketplace** — vetted, transparent, itemized; assisted filing | S2→S3 | F1/F3 | P2–P3 | Commission/referral | pool F1 trust layer |
| C9 | **Multi-state & scale modules** — branches, audit/board readiness, IEC, exports | S5→S6 | F1/F2 | P3 | — | competitive whitespace #6 |

## 2. Vertical packs (A-Z — added per traction & validation, not day 1)
**v0.3 pilot set (founder decision 2026-09-08):** Entry B pilots the example local-trade set — **kirana/grocery, appliance & electronics, electrical, auto-mechanic** (F&B pack stays available for later pilots). All packs are config (licence bundles + NIC hints + catalog shapes), layered on the C-series core.
| Pack | Focus types | Licence/registration bundle (from regulatory research) | Notes/verifies `[VERIFY at build]` |
|---|---|---|---|
| **Kirana / grocery & general store** | Goods-led retail | Udyam (free, day-1) → GST (goods >₹40L, or e-comm/inter-state) → S&E (premises) → trade licence (municipal) → current account | **FSSAI basic only if selling food items** (packaged snacks etc.); two 2026 sources conflict on the new basic-registration turnover band (₹12L vs ₹1.5Cr from Apr-2026) → `[VERIFY against FSSAI/FoSCoS]` |
| **Appliance & electronics shop** | Goods + service (install/repair) | Udyam → GST → S&E → trade licence (electronics activity code) → current account | Service income rides mixed goods+service GST logic; no sector licence for retail+repair `[VERIFY state: installation-only contractors may need state contractor licence]` |
| **Electrical shop** | Goods (fittings) + service (wiring jobs) | Udyam → GST → S&E → trade licence | Retail OK; **electrical contracting work → state electrical contractor licence** `[VERIFY state/city]` |
| **Auto mechanic / garage** | Service-led + parts | Udyam → GST (services ₹20L / goods ₹40L; dominant-stream logic) → S&E → trade licence | Pollution/consent NOC only for larger workshops (paint/body) `[VERIFY city]`; parts vs labour split matters for GST |
| F&B (restaurant / cloud kitchen) | Food businesses | FSSAI tier + S&E + trade licence + fire/health NOC + GST + eating-house where applicable | **Deferred from v0.3 pilot**; pack defined, ships later |
| E-commerce seller | Marketplace sellers | GST day-1 (TCS) + Udyam + S&E-if-office | Later |
| Manufacturing / Creator etc. | — | (registry rows from v0.2 retained) | Later |

Pack selection rule: each pack = a **licence bundle definition + NIC-code hints + tailored journey order**, layered on the same C1–C8 core — no separate codebase.

## 2.5 Customer-side module registry (v0.2 → v0.3)
| ID | Module | Consumer journey step | Priority | Monetization | Notes |
|---|---|---|---|---|---|
| D1 | **Discovery & search** — location + vertical + **verified-only filter** + query; list w/ distance | Discover | P0 | Free (acquisition) | Single-city pilot (Bengaluru) |
| D2 | **Verified storefront** — badge, licence summary, "registered & compliant" proof, contact | Consider | P0 | Free; promoted placement = paid later | Badge from shared verification rule (C3-derived) |
| D3 | **Catalog & listings** — **goods AND services** items w/ price or price-basis, stock, photos; merchant-managed (manual entry MVP) | Browse | P0 | Free | Service listings carry duration/price-basis (see D9); no POS integration MVP |
| D4 | **Order & booking bridge** — cart order **or service booking** → accept → fulfill → complete; timeline shared both sides | Order/Book | P0 | No take-rate — bundled value of the merchant OS subscription (SaaS-first, 2026-09-08) | Touches business Run side (S14 inbox; appointment tab) |
| D5 | **UPI payment intent** — PA-partner redirect, webhook verify, expiry; **never holds funds** | Pay | P1 | PA fees passed/absorbed | POD/manual fallback until PA onboarding; service bookings default pay-at-shop |
| D6 | **Ratings & reviews** — post-completion, order-verified only | Repeat | P1 | Trust asset | Moderation + dispute flow later |
| D7 | Loyalty-lite (stamps/offers) | Repeat | P2 | — | Future |
| D8 | **Deals & promotions (v0.3)** — merchant-created offers (flat ₹ / % off), validity window, optional listing-scope + caps; surfaced in discovery ("nearby deals") & storefront; server-validated at checkout | Consider → Order | **P0** | Free in MVP; promoted deals later | Anti-fake-deal guardrails: real-time validation, no false-MRP claims, `validFrom/To` |
| D9 | **Service bookings & availability (v0.3)** — merchant weekly availability → date/time slots; booking orders w/ confirm/decline; pay-at-shop default | Book | **P0** | Free | Appliance/electrical installs & mechanic repair; no-show policy = merchant confirm + reminders |
Consumer journey: **Discover → Consider → Browse → Order/Book → Pay → Track → Repeat** (deals ride Discover & Consider).

## 2.6 Shared bridge modules (both roles)
| ID | Module | Sides | Priority |
|---|---|---|---|
| B0 | Orders core (state machine + timeline events; goods + service-booking variants) | D4 ↔ business inbox | P0 |
| B1 | Verification badge rule + daily recompute job | D2 ↔ C3 compliance state | P0 |
| B2 | Reviews core (order-verified) | D6 ↔ merchant reputation | P1 |
| B3 | Deals engine (server-validated at checkout) | D8 ↔ order totals | P0 (v0.3) |

## 2.7 Everyday-needs pack roadmap (waves A–D) — from `research/everyday-needs-landscape.md`
Loop-and-graph research (2026-09-08) over customer everyday-needs × business types × owner-needs produced a 4-wave pack roadmap. All packs remain **config on the C-series core** (licence bundles + journey order + catalog shapes); no new user flows per vertical.
| Wave | Packs | Signal | Deltas vs today |
|---|---|---|---|
| **A (live)** | Kirana/grocery · appliance & electronics · electrical · auto-mechanic | Founder example set; supply gate | — |
| **B (next)** | **Pharmacy/medical store (flagship)** · salon/barber/parlour · F&B eat-out (restaurant/dhaba/cloud kitchen/tiffin) · mobile & electronics repair | Regulated/trust-heavy → badge max value; pharmacy already pays for billing/expiry software `[VERIFIED]`; salon booking-platform habit `[VERIFIED]`; all are S&E+T + ≤1 sector licence → mostly content config | C1 pack rows (drug-licence pre-reqs incl. pharmacist; FSSAI band `[VERIFY]`), C5 renewals (drug retention 5-yr; health-cert windows), D9 slots for salon/repair, D8 for F&B/wellness |
| **C (wave-3)** | Vehicle-adjacent (tyre/car wash/spares) · home-services agencies · hardware/paint/furniture · coaching/tuition · events (catering/tent/photo) · fabric care (tailor/laundry) · printing/courier · **person packs (individual providers: mobile mechanic/electrician/appliance tech, home beautician/barber, home-kitchen/tiffin, tuition-at-home)** | Broadens everyday-needs coverage + the "make money" side (individuals) | D9 quote-style booking; D8 seasonal deals; mixed goods/services GST guidance; **ProBadge tier** = identity+skill-cert verification (NOT compliance licences — distinct trust semantics from the shop badge) `[individual-providers-gig.md]`; **legal gate: Karnataka Gig Workers Act 2025 obligations before functioning as a matching marketplace for individuals** `[VERIFIED]` |
| **D (watch)** | Clinics/diagnostics · insurance/fintech agents · agri-inputs · drivers | Regulated, app-exclusive, or rural | none; revisit with partners |
**Horizontal insight:** S&E + trade-licence renewal + registers + Udyam + GST are near-universal across every wave → the **renewals/people calendar (C5 + O2/O8)** is the stickiest core asset; EPFO/ESIC headcount cross-linkage (FY25-26 `[VERIFIED]`) is the growth trigger into the Run stage. Badge value peaks in trust/health verticals (pharmacy, F&B, salon); booking fit peaks in appointment-driven trades (salon, repair, garage, coaching, events).
**Two-sided validation (from `research/two-sided-wants-gaps.md`):** customer-led formalisation is externally recommended (40% of registered nano-enterprises say customers ask for proof of registration; IFMR LEAD `[VERIFIED]`) — the badge is the bridge between owner want (trusted visibility) and customer want (proof of quality). Customers wait for deals (47% `[VERIFIED]`) while owners have no offer tooling → D8 addresses a documented gap. Deals + badge + bookings are all "help each other" levers, not invented features.

## 3. Key architecture principle (feeds domain model)
Module activation is **data-driven**: `BusinessProfile {stage, sizeClass, entityType, state, businessType/vertical, employees, hasGst, …}` → rules engine selects active journeys/tasks/calendar items. Vertical packs add `bundle` rules, never new user flows. This keeps the MVP generic while the product *feels* A-Z specific.
**v0.2 addition — the same profile drives the consumer side:** a profile that reaches `formalizationState ≥ registered` with no expired licences becomes a **verified merchant** (badge) automatically; its catalogue + licence summary feed the consumer storefront (D2/D3) with **no separate merchant profile**. Compliance state is thus the supply-side gate for the marketplace.
**v0.3 addition — the profile carries a growth rung (`I→XS→S→M→L→Corp`, stage-model §0):** module activation and licence bundles are rung-aware; graduation events (premises, GST crossing, 10th/20th employee, first branch) upgrade the rung **in place** — the same profile that starts as an individual earner (ProBadge, wave C) can become a compliant shop (BusinessBadge) without restarting, keeping history, documents and earned reputation.
