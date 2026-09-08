# Work Items — Two-Surface MVP (idea-to-spec Phase 5, v0.3)
**Version:** 0.3 · **Date:** 2026-09-08 · Slicing: user-story-mapping, breadth-first. **Two entry experiences** (founder decision): Entry A = business Launch Copilot (W1–W16, v0.1), Entry B = customer trusted + deals marketplace — verified discovery, **goods orders, service bookings, deals** (W17–W34). Sequencing principle: **supply before demand** — Entry A slices land first, Entry B builds on verified merchants. Sizes: S ≤3d, M ≤5d, L ≤10d (solo dev).

## Slice 1 — Walking skeleton (vertical: EN, Pvt Ltd journey, no auth)
Goal: a founder can answer the quiz and walk a complete Pvt Ltd formalize journey marking tasks done.
| ID | Story | Size | Deps |
|---|---|---|---|
| W1 | As a first-time founder, I want a phone-only login (dev mock OTP) so that I can return to my setup. (S2) | S | — |
| W2 | As a founder, I want to create my business profile (name/state/size/turnover) so the app adapts to me. (S3) | S | W1 |
| W3 | As a founder, I want a 6-question entity quiz with plain-language options so I can get a recommendation. (S4, S5) | M | W2 |
| W4 | As a founder, I want to see a recommendation with trade-offs incl. ongoing compliance cost warning, and accept it. (S5) | M | W3 |
| W5 | As a founder, I want a Pvt Ltd incorporation journey (DSC → name → SPICe+ → COI) with prerequisite-locked ordered tasks, each explaining what/why/docs/govt-fee and linking the official MCA portal, so I can complete registration myself. (S6–S8) | L | W4 |
| W6 | As a founder, I want to mark a task "completed on the portal" (manual milestone) and see journey progress advance. (S7) | S | W5 |
| AC W5: task content bilingual keys exist (EN authored; HI marked pending); govtFee + asOf + disclaimer displayed; illegal transitions blocked (locked until prerequisites done). | | | |

## Slice 2 — Meat (docs, GST/Udyam/post-COI, deadlines, EN core completion)
| ID | Story | Size | Deps |
|---|---|---|---|
| W7 | As a founder, I want to upload required docs per task (Aadhaar/PAN/address proof/photos/NOC) with capture-from-camera so my readiness is tracked; task can't be marked doneGovt until mandatory docs attached. (S8, S10) | L | W6 |
| W8 | As a founder, I want a GST journey (threshold logic: goods ₹40L / services ₹20L; compulsory flags for interstate/e-commerce) + Udyam journey + post-COI tasks (bank account, INC-20A) derived from my profile. | L | W5, W6 |
| W9 | As a founder, I want a deadlines calendar seeded from my registration dates (INC-20A +180d, auditor +30d, DIR-3 KYC Sep-30, GST cadence) with missed-flagging and reminders. (S11) | M | W7, W8 |
| W10 | As a founder, I want an EN⇄HI language toggle that re-renders all screens from content keys. (all screens) | L | W5 (i18n infra) |
| W11 | As a founder, I want offline read access to my journeys and queued uploads on reconnect. | M | W7 |
| AC W9: INC-20A due = COI milestone + 180d computed and displayed as countdown; missed = auto-flag daily job. AC W10: validate-i18n script passes (EN+HI key parity) in CI. | | | |

## Slice 3 — Polish & packs (local trade/service licence bundles, transparency, edge states)
| ID | Story | Size | Deps |
|---|---|---|---|
| W12 | As a founder of a local trade/service shop (**grocery, appliance & electronics, electrical, auto-mechanic**) in MH/KA/DL/TN/GJ, I want my vertical's licence pack converted into journey tasks (S&E, trade licence, FSSAI-where-applicable, GST/Udyam sequence per module-map §2 config), so I don't miss local requirements. (S9) | L | W8 |
| W13 | As a founder, I want the govt-fee vs professional-fee transparency widget + look-alike-portal warnings on Udyam/GST tasks. (S8) | S | W7 |
| W14 | As a founder, I want full empty/error/edge states across screens (no data, 422 missing docs, offline, 409 completed quiz). | M | Slice 2 |
| W15 | As a founder, I want Hindi content shipped for highest-traffic journeys (entity quiz, GST, Udyam, FSSAI) with EN fallback + pending badges elsewhere. | L | W10 |
| W16 | As the operator, I want the 5-state licence-rule matrix and fee figures versioned as config with `asOf` so content stays correct. (domain-model §4/§5) | M | W12 |
| AC W12: bundle configs are data-only (no code change per state); AC W16: Phase-4 re-verification produces a config patch, not schema change. | | | |

## Entry B — Customer trusted + deals marketplace (v0.3 stories)
Goal: a consumer in either pilot city (Bengaluru + Hyderabad, in parallel) can discover verified merchants across **grocery, appliance & electronics, electrical, auto-mechanic**, order goods, **book service slots**, redeem **deals**, track, and review. Requires Entry A W7/W8/W12 outputs (profile → registered → licences) so real merchants can be verified.

### Slice B0 — marketplace core (badge + catalog + orders)
| ID | Story | Size | Deps |
|---|---|---|---|
| W17 | As a merchant, I want my storefront to auto-activate with a **verified badge** when my profile is registered with no expired licences, and hide automatically on suspension, so compliance drives my visibility. (B1) | M | W7, W12, W16 |
| W18 | As a merchant, I want to create/manage listings (name, price, GST-inclusive flag, unit, stock, photo, category) for my vertical so customers see my real catalog. (S14-add, API business listings) | M | W17 |
| W19 | As a merchant, I want an order inbox to accept / fulfill / decline orders so I control my operations. (S14) | M | W17, W18 |
| AC W17: badge = derived view (formalizationState ≥ registered ∧ no missed required deadlines ∧ no expired licence docs); daily recompute job + instant hide on suspension (LM2 test). | | | |

### Slice B1 — consumer journey (discovery → order → track)
| ID | Story | Size | Deps |
|---|---|---|---|
| W20 | As a consumer, I want to log in with my phone and choose the **customer side** (role gate) so I can discover verified shops. (S15) | S | W1 (auth shared) |
| W21 | As a consumer in a pilot city, I want to see verified merchants near me filterable by vertical (**grocery · appliances · electrical · auto care**) and searchable, so I can find a trustworthy shop. (S16) | M | W17, seeded merchants |
| W22 | As a consumer, I want to open a merchant storefront showing the verified badge + licence summary + catalog, so I can trust and choose. (S17) | M | W18, W21 |
| W23 | As a consumer, I want to add items and place an order (pickup / merchant delivery / POD) with my saved address, so the merchant can prepare it. (S18, S19) | L | W19, W22 |
| W24 | As a consumer, I want order tracking with a status timeline and cancel-while-allowed, so I know what's happening. (S21) | M | W23 |
| AC W22: unverified merchant direct-ID access → 404; badge shows licence summary + verifiedAt. AC W23: totals recomputed server-side at POST /orders (listing snapshot). | | | |

### Slice B2 — payments + reviews (UPI via PA, trust loop)
| ID | Story | Size | Deps |
|---|---|---|---|
| W25 | As a consumer, I want to pay by **UPI redirect** through the payment aggregator (or choose POD before PA onboarding), so I can complete my order without the app holding funds. (S20) | L | W23, PA onboarding |
| W26 | As the operator, I want signature-verified PA webhooks as the only path to mark payment succeeded (with 15-min intent expiry + retry), so payment state is trustworthy. | M | W25 |
| W27 | As a consumer, I want to rate my completed order (order-verified, one per order) so quality signals accumulate for others. (S22) | S | W24 |
| W28 | As the operator, I want a weekly badge-integrity audit (LM2) and discovery funnel instrumentation (CM1–CM4, LM1), so trust and the loop are measurable from day 1. | S | W17, W25, W27 |
| AC W25: no wallet/fund holding (scope-brief OUT); PaymentIntent expires 15 min → order returns to placed; POD default until PA live. AC W28: events for CM1/CM2/CM3/CM4 + LM1 defined and emitted. | | | |

### Slice B3 — bookings, deals & pilot packs (v0.3)
| ID | Story | Size | Deps |
|---|---|---|---|
| W29 | As a merchant, I want to add **service listings** (duration, price-basis, serves-at) and set my **weekly availability**, so customers can book me. (S14a; domain §9.1–9.2) | M | W18 |
| W30 | As a consumer, I want to pick a date/time slot from a merchant's available slots and place a **service booking** (pay-at-shop), track confirmation, and complete when the job is done. (S18/S19/S21; domain §9.3/9.5) | L | W19, W29 |
| W31 | As a merchant, I want to create **deals** (₹ off / % off, whole shop or listing, validity, cap) and pause/resume them, so I can attract nearby customers. (S14b; domain §9.4) | L | W17, W18 |
| W32 | As a consumer, I want a **Nearby Deals** feed (home rail + list view) and storefront deal chips, with deals **server-validated at checkout** and applied to my total. (S16/S17/S19/S24; API Part C) | M | W23, W31 |
| W33 | As the operator, I want the **4 pilot pack configs** (kirana/grocery, appliance & electronics, electrical, auto-mechanic) shipped — licence bundles, NIC hints, catalog seeds, service-serving defaults — as data-only config with `[VERIFY]` markers. (module-map §2) | M | W16 |
| W34 | As the operator, I want CM5/CM6 (booking confirmed rate, deal-attributed orders) instrumented and the slot-conflict/deal-validation failure paths tested. | S | W30, W32 |
| AC W29: service listing not bookable until availability saved (400). AC W30: slot race → 409 slot_taken; decline releases slot. AC W32: expired/scope-mismatch/cap-exhausted deals → 422 with reasonKey; no deal stacking. AC W33: pack rows are config-only (no code per vertical). | | | |

## Pilot data & validation sprint (W35+, data-grounded, runs parallel to build)
Source of truth: `research/bengaluru-pilot-map.md` (denominator + governance) · `research/hyderabad-pilot-map.md` (TS/GHMC mirror) · `docs/validation-interviews.md` (H1–H6) · scope-brief OQ2/OQ9/OQ10. Sizes: S ≤3d · M ≤5d.
| ID | Story | Size | Deps |
|---|---|---|---|
| W35 | As the operator, I want the **pilot denominator computed from the OpenCity BBMP trade-licence CSVs** (28 constituencies → map licence activity codes to the 4 verticals → ward counts) and a **shortlist of 3–4 candidate wards** by vertical density, so recruitment targets are real numbers not guesses. (bengaluru-pilot-map §3/§6) | M | — |
| W35b | As the operator, I want the **Hyderabad denominator from GHMC/Telangana trade-licence data** (city pack, parallel to W35), so Hyderabad recruitment targets are real numbers (sources `[VERIFY]` in research/hyderabad-pilot-map.md). | M | W35 |
| W36 | As the operator, I want a **field ground-truth sample** (walk 2–3 streets/ward, n≈30–50 shops; capture vertical, licence state, digital tools) to sanity-check licence-data coverage vs reality, so the denominator is trustworthy. (Sheet: `docs/field-sample-sheet.md`) | M | W35 |
| W37 | As the operator, I want the **licence-portal ownership confirmed per candidate corporation** (BBMP→5-corps transition; which body issues trade licences today) and KA S&E 2026 specifics, so journey config freezes against the right portal. (scope-brief OQ10) | S | W35 |
| W38 | As the founder, I want **≥10 merchant + ≥10 consumer validation interviews run** (Scripts A/B in `docs/validation-interviews.md`, incl. Appendix outreach messages) across the 4 verticals + pilot catchment, with debriefs coded to H1–H6, resolving OQ3 (badge vs deals vs bookings) and OQ9 (SaaS price band + tier contents — model resolved SaaS-first, 2026-09-08). | M | — |
| W39 | As the operator, I want the **recruitment kit live** (bilingual outreach message + referral ask, per `docs/pilot-recruitment-playbook.md`) and a tracked funnel: approached → interested → journey started → verified, so the ≥100-verified gate has a weekly number. | S | W35, W38 |
| W40 | As the operator, I want the **≥100-verified-merchant supply ramp projection** (per-ward conversion from W35/W36/W39 rates) reviewed weekly vs the consumer-launch gate (scope-brief OQ2/LM1). | S | W35, W39 |
| AC W35: denominator table = licence counts per vertical per ward with source CSV + date. AC W36: sample notes ≥80% coverage match or documented gap. AC W38: exit criteria met per validation-interviews (≥60% positive per hook) or scope-brief OQ reopened. AC W39: funnel dashboard shows approached→verified counts. | | | |

## Sequencing & value/effort (v0.3)
- **Entry A**: W1→W6 skeleton (~2.5–3 wks) → W7/W8 → W9/W10 → W11 → slice-3 (W12–W16).
- **Pilot data & validation (parallel)**: W35 denominator → W36 field sample → W37 portal verification → W38 interviews → W39 recruitment kit → W40 ramp projection.
- **Entry B**: W17/W18/W19 (marketplace core, ~2 wks) once Entry A reaches "registered" merchants → W20–W24 consumer journey (~3 wks) → W25–W28 payments/trust (~2 wks) → **W29/W30 bookings, W31/W32 deals, W33 pilot packs, W34 instrumentation** (~3 wks).
- Revised solo timeline: **≈ 10–12 weeks** to demonstrable closed loops in BOTH pilot cities (Bengaluru + Hyderabad in parallel — two cities at once doubles supply-ramp/field effort, so the city packs, denominators and merchant onboarding must run as parallel tracks; excludes founder validation gates and PA onboarding).
- **Deferred (out of MVP, scope-brief OUT):** wallet/escrow; delivery fleet; ads/promotions (beyond merchant self-serve deals); coupon/affiliate machinery; dynamic pricing/cashback/loyalty; multi-city consumer; real portal integrations; CA marketplace; team accounts; F&B + other vertical packs (config-ready).

## Traceability (v0.3 additions)
- Stories → screens: W29(S14a) W30(S18,S19,S21) W31(S14b) W32(S16,S17,S19,S24) W33(pack config) W34(instrumentation).
- Stories → API: W29(availability + service listings) W30(slots + service POST /orders) W31(deals CRUD) W32(discover/deals + deal at checkout) W33(meta/config) W34(events).
- Stories → domain: service Listing kind + MerchantAvailability/SlotView (W29/W30), booking order branch (W30), Deal entity + validation (W31/W32), CM5/CM6 → scope-brief metrics (W34).
- v0.1–v0.2 traceability (W1–W28) unchanged.
