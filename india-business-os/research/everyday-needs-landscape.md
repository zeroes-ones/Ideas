# Everyday-Needs Landscape — Customer Need × Business Type × Owner Need (India)

> **Date:** 2026-09-08 · **Status:** Research synthesis for pack-brainstorming (feeds `docs/module-map.md` §2.7)
> **Companion docs:** `two-sided-wants-gaps.md` (owner wants × customer wants × gap matrix) · `regulatory-journey.md` · `competitive-map.md`
> **Policy:** every claim tagged `[VERIFIED]` (≥2 independent sources or official), `[ESTIMATED]` (1 source / inference), `[VERIFY at build]` (conflict or state-specific). Monetary figures are `[as of]` the cited period. Method follows the library's loop-and-graph discipline (see §1).

## 1. Method: loops & graphs

**Graph model.** Nodes = `N` customer everyday-needs, `B` business types serving them, `O` owner-needs (what a shop needs to run/comply/grow), `M` our modules. Edges: `N→B` *served by*, `B→O` *requires*, `O→M` *covered by*, `B→M` *fits*. Every `B` also carries two attributes: size skew (very small → medium) and lifecycle stage pull (Start/Formalize/Comply/Run/Grow).

**Loop protocol.** Each iteration: (1) expand the frontier node set via web research; (2) tag every claim; (3) prune duplicates and low-fit types; (4) **gate** — continue only if the loop added ≥1 cluster or ≥2 new B-types with source support, else stop. Iteration log in §2 keeps the loops auditable, mirroring the "evals as merge gates" idea in `BEYOND-LOOPS-GRAPHS.md`: no unverified claim ships into the pack matrix.

## 2. Iteration log

| Loop | Expanded | Key verified inputs | Gate result |
|---|---|---|---|
| I1 | `N` set (consumption ground truth) | HCES 2023-24: food ≈40% urban / ≈47% rural spend `[VERIFIED]`; beverages+processed = largest food sub-category (≈10–11%) `[VERIFIED]`; rural durables spend/capita/mo +217% over a decade (₹170→₹540) `[VERIFIED]`; urban ~50% of food budget out-of-home/prepared (Deloitte-FICCI) `[VERIFIED]`; food services ₹7.76T by FY28 at 8.1% CAGR, organised segment 13.2% (NRAI) `[VERIFIED]`; ~70% households essentials-constrained → India 1/2/3 segmentation (Blume/Indus Valley 2025) `[VERIFIED]`; premiumisation concentrated in top decile (Kotak: urban top-10% multiples on durables/jewellery/education) `[VERIFIED]` | Pass → 12 clusters |
| I2 | `B` licence regimes for regulated types | Pharmacy: Drug licence Form 20/21 under D&C Act 1940/Rules 1945; registered pharmacist physically present mandatory; premises ≥10 sqm; perpetual validity via Rule 63 amendment (eff. Jan-2024) but 5-year retention fee `[VERIFIED]`; govt fee ₹1,500–3,000 typical (state-varying ₹250–6,000) `[VERIFIED]`; ONDLS portal (states vary) `[VERIFIED]`; inspection 30–60 days `[VERIFIED]`; selling without licence → up to 3 yrs imprisonment (Sec 27) `[VERIFIED]`. Salon/barber/parlour: S&E + municipal trade licence (some cities health-trade); no national special licence `[VERIFIED]`; fee ₹500–5,000 by city `[VERIFIED]`; GST 18% beauty services `[VERIFIED]`. Coaching/tuition: no central licence; MoE Jan-2024 coaching guidelines + state/municipal registration variance `[VERIFIED]`; S&E applies; GST 18% coaching (schooling exempt) `[VERIFIED]`. Trade licence: municipal, 1 premises = 1 licence, annual renewal common (Q1 window) `[VERIFIED]`; change of name/address/ownership → amendment `[VERIFIED]`. S&E: 5 mandatory registers; annual returns (DL/KA/TN); MH micro self-certification; **EPFO/ESIC headcount cross-linkage FY25-26 → quarterly reconciliation needed** `[VERIFIED]` | Pass; flags → `[VERIFY at build]` |
| I3 | `O` owner-need profiles & digital-readiness | Pharmacy: dedicated billing/inventory/expiry software already normalised and paid (₹10k–30k setup) `[VERIFIED]`; franchise push (MedPlus/Apollo etc.) `[VERIFIED]`; startup ₹5–12L `[VERIFIED]`. Salon: booking-platform listing habit common `[VERIFIED]`; recurring annual trade-licence renewal + health-cert expiry trap (30–60 day validity) `[VERIFIED]`. Trade-licence delays caused by wrong portal (≈40% anecdote) `[VERIFIED — vendor claim, treat as signal]`; S&E delay cost example ₹1,500 licence → ₹14.5k penalty exposure `[VERIFIED — worked example]` | Pass → O-matrix |
| I4 | Fit scoring, pruning, waves | Pruned: financial agents (IRDAI/regulated, partner later), cab/driver apps (app-exclusive), agriculture-input shops (fertiliser licence, rural), clinics/diagnostics (clinical licensing, healthcare partner later), schools/institutions (heavy licensing; coaching only) | Pass → 4 waves; 0 new B-types vs I3 → stop |

## 3. N — household everyday-need clusters

| ID | Cluster | Demand signal | Exemplar B-types | Product-lever fit |
|---|---|---|---|---|
| N1 | Grocery & daily essentials | Largest wallet (food 40/47%); 70% households value-constrained `[V]` | Kirana, supermarket, veg/fruit, dairy, meat/fish, bakery | Deals (mass), verified, recurring orders |
| N2 | Food, out-of-home & delivery | ~50% urban food budget outside home; ₹7.76T by FY28 `[V]` | Restaurant, dhaba, cloud kitchen, tiffin, QSR, mithai | Hygiene badge, FSSAI, table/order booking |
| N3 | Medicines & health essentials | Health wallet 6.1% CPI weight, rising `[V]`; regulated | Pharmacy/medical store, generic store, Ayurveda shop | **Badge = trust-critical**, compliance depth, expiry tracking |
| N4 | Personal grooming & beauty | Large recurring discretionary; 18% GST services `[V]` | Salon, barber, beauty parlour, spa | Booking slots, hygiene badge, loyalty |
| N5 | Vehicle ownership & movement | Autos +3.1pp wallet share `[V]`; 2W/4W ubiquity `[V]` | Garage, tyre shop, car wash, spares | Booking (service slots), quote-before-service, badge vs overcharge fear |
| N6 | Home systems upkeep & repairs | Urban housing stock aging; highly informal supply `[E]` | Electrician, plumber, carpenter, pest control, cleaning (individuals/agencies) | Booking, verified, upfront estimates |
| N7 | Electronics & connected life | Mobiles +3.6pp wallet; durables rural +217% `[V]` | Mobile shop/repair, appliance repair, computer, CCTV | Repair booking, parts-trust badge, deals |
| N8 | Household durables & big-ticket | Durables surge; top-decile premium `[V]` | Furniture, hardware/paint, appliance retail, mattress | Deals, catalog, verified (avoid fakes) |
| N9 | Wardrobe & fabric care | Clothing share down but absolute large `[V]` | Tailor, garment shop, laundry, dry-cleaning | Booking/pickup, quality badge |
| N10 | Learning & skilling | Education 7% urban spend; coaching booming `[V]` | Tuition/coaching, hobby classes, computer centre | Booking (batches), fee transparency, legitimacy badge |
| N11 | Occasions, events & celebrations | Discretionary, seasonal, top-decile-skewed `[V]` | Catering, tent/decor, photography, florist, DJ | Quote-based booking, deals pre-festival |
| N12 | Errands, communication & admin | Ubiquitous micro-services `[E]` | Printing/photocopy, courier/parcel, DTH/cable, stationery | Long tail — config later |

## 4. B — business-type directory (with licence, owner-need emphasis, wave)

Waves: **A** = live pilot · **B** = next packs · **C** = wave-3 candidates · **D** = watchlist/adjacency.
Licence bundle shorthand: **S&E** Shop & Establishment · **T** municipal trade licence · **GST** registration trigger · **U** Udyam · sector licences spelled out. Size skew: `micro→small→med`.

| B-type | Cluster | Licence bundle `[VERIFY at build for city]` | GST trigger | Size | Digital readiness | O emphasis (owner-needs §5) | Wave |
|---|---|---|---|---|---|---|---|
| Kirana / grocery | N1 | S&E+T(+U) | >₹40L goods (else optional) | micro→med | med-high (UPI/billing) | O3 O4 O6 O10 O11 | **A** |
| Appliance & electronics retail+service | N7/N8 | S&E+T(+U) | >₹40L | micro→med | med | O3 O4 O5 O10 | **A** |
| Electrical shop / contractor | N6 | S&E+T; **contractor licence for bigger electrical jobs** `[V flag]` | services ₹20L | micro→small | low-med | O2 O4 O9 | **A** |
| Auto-mechanic / garage | N5 | S&E+T (workshop) | services ₹20L | micro→small | low | O2 O4 O9 O10 | **A** |
| Pharmacy / medical store | N3 | **Drug licence Form 20/21** + pharmacist + S&E+T; FSSAI if wellness/foods; GSTIN even for exempt meds `[V]` | GSTIN needed day-1 (exempt ≠ unregistered) `[V]` | small→med | **high (pays for software)** `[V]` | O1 O2 O4 O6 O9 | **B (flagship)** |
| Salon / barber / parlour | N4 | S&E+T (health-trade in some cities) `[V]` | services >₹20L | micro→small | med (booking habit) `[V]` | O1 O2 O4 O10 | **B** |
| Restaurant / dhaba / cloud kitchen / tiffin | N2 | S&E+T+**FSSAI** (by turnover) + fire NOC as applicable `[V]` | services >₹20L | micro→med | med | O1 O2 O4 O10 | **B** |
| Mobile & electronics repair | N7 | S&E+T | services >₹20L | micro→small | med | O2 O4 O9 O10 | **B** |
| Tailor / laundry / dry-clean | N9 | S&E+T `[E]` | services ₹20L / goods ₹40L | micro→small | low-med | O2 O4 O10 | **C** |
| Tyre / car wash / spares | N5 | S&E+T `[E]` | mixed | micro→small | low-med | O2 O4 O9 | **C** |
| Home-services agency (plumber/electrician/carpenter/pest/cleaning) | N6 | S&E+T; contractor licence per trade for bigger works `[V flag]` | services ₹20L | micro→med | med (aggregator-listed) | O2 O4 O9 O10 | **C** |
| Hardware / paint / furniture / mattress | N8 | S&E+T(+U) | goods >₹40L | small→med | med | O3 O4 O6 O8 O11 | **C** |
| Tuition / coaching / hobby class | N10 | S&E; municipal registration variance `[V]`; no central licence `[V]` | services >₹20L | micro→small | med | O1 O2 O4 O10 | **C** |
| Catering / tent / photo / florist / DJ | N11 | S&E+T; FSSAI for catering `[E]` | services ₹20L | micro→small | low-med | O2 O4 O10 | **C** |
| Printing / photocopy / courier / stationery | N12 | S&E+T `[E]` | mixed | micro→small | med | O2 O3 | **C** |
| Bakery / dairy / meat-fish shop | N1/N2 | S&E+T+FSSAI (incl. licensing requirements per type) `[V]` | goods | micro→small | low-med | O1 O2 O4 | **C** |
| Clinic / diagnostics / gym | — | **Clinical licensing; healthcare partner later** | services | small→med | med | — | **D** |
| Insurance / fintech agents | — | IRDAI / regulated `[V]` | services | micro | high | — | **D** |

### 4.1 I-class — individual service providers & home-based owner cases (no premises licence)
New node class from `research/individual-providers-gig.md` `[VERIFIED]`: individual providers are **not** covered by the shop licence regime (no S&E/trade licence applies to a plumber working from home). Their trust stack = identity + skill cert + references + ratings, not registrations; many straddle shops (a mechanic *with* a shop also does mobile calls).
| B-type | Cluster | Verification/formal stack | Size | Digital readiness | Wave | Notes |
|---|---|---|---|---|---|---|
| Mobile mechanic / electrician / appliance tech (individual, no shop) | N5/N6/N7 | Udyam/UAP (free) → GST >₹20L services; skill certs (ITI/NSDC); state contractor licence for bigger electrical jobs `[VERIFY]` | micro | med | **B/C (overlaps pilot verticals)** | MVP must handle shop-with-mobile-service cleanly; ProBadge semantics |
| Beautician / barber at home / visit | N4 | Informal; hygiene norms; booking fit | micro | med | C | Safety-sensitive (women pros) |
| Home kitchen / tiffin / caterer-from-home | N2 | FSSAI home-kitchen; Udyam/UAP | micro | low-med | C | F&B pack variant |
| Tuition/coaching at home | N10 | Municipal variance; S&E if staff `[V]` | micro | med | C | Booking fit |
| Craftspeople (PM Vishwakarma) | N6/N7-ish | Scheme onboarding via Udyam/UAP `[V]` | micro | low | D | Partner rails exist |
| Freelancer (design/dev/consulting) | — | GST for B2B/ITC pulls | micro | high | D | Different product; watch |
Gig context: **12M gig workers FY25 → 23.5M by 2029-30** `[V]`; home services >98% offline (~$50-60B); platform workers earn 2.5× informal yet **40% earn <₹15k/mo** `[V]`; trust = the category bottleneck. Karnataka Gig Act 2025 (welfare fee 1–5%, portable worker IDs) = **legal watch item before we match individuals as a marketplace** `[V]`.

| Agriculture-input shops | — | Fert./seed licences; rural `[E]` | goods | micro | low | — | **D** |
| Driver/transport apps | — | App-exclusive economics `[E]` | services | micro | high | — | **D** |

## 5. O — owner-needs and coverage

| O | Owner need | Universal? | Covered by (M) | Notes |
|---|---|---|---|---|
| O1 | Start: entity + sector licences | every type | C1 Launch Copilot + pack config | Pharmacy pharmacist prerequisite, FSSAI bands `[VERIFY]` |
| O2 | Comply: calendar, renewals, registers | every type | C5 calendar; S&E registers; **EPFO/ESIC cross-link reconciliation** `[V]` | Trade licence annual renewal; drug retention 5-yr; health cert expiry traps `[V]` |
| O3 | Catalog & digital presence | goods+sellers | D2/D3 | Deals rail entry point |
| O4 | Orders + bookings intake | service/retail | D4/D9 | Salon/garage/coaching booking fits `[V]` |
| O5 | Payments (UPI/POS/collect) | every type | D4 (PA redirect) | POD fallback |
| O6 | Inventory & purchase (expiry mgmt) | goods | C7-later; **b2b-price-intel synergy** | Pharmacy expiry mgmt is paid-software proof `[V]` |
| O7 | Bookkeeping & GST | every type | C7 later | Invoicing expected |
| O8 | People (hiring, PF/ESI at 10/20) | employers | C8 later | S&E cross-linkage makes this urgent at growth |
| O9 | Credit & insurance eligibility | growth-stage | pack-level content (Udyam as key) | Udyam is the free gate to MSME credit `[V]` |
| O10 | Marketing, deals, repeat | all | D8 deals + WhatsApp-adjacent | Deals most valuable in N1/N2/N4 `[V]` |
| O11 | Delivery/logistics | goods | OUT (partner/aggregator) | Keep OUT of MVP |

## 6. Pack waves & module deltas

| Wave | Packs | Why this wave | Module deltas (vs. today) |
|---|---|---|---|
| A (live) | Kirana/grocery · appliance & electronics · electrical · auto-mechanic | Founder's examples; supply gate | — |
| B | **Pharmacy** (flagship) · salon/barber · F&B eat-out · mobile/electronics repair | Regulated/trust-heavy → badge max value; booking habit exists (salon); pharmacy already pays for software; all are S&E+T + ≤1 sector licence → Launch Copilot extension is mostly **content config** | C1 pack rows (drug-licence pre-reqs incl. pharmacist), C5 renewal events (drug retention 5-yr, health cert), D9 slot booking for salon/repair, D8 for F&B/wellness; **pharmacy expiry/inventory later C7** |
| C | Vehicle-adjacent · home services · hardware/furniture · coaching · events · fabric care · printing/courier | Broadens "everyday needs" coverage; needs marketplaces/quote flows | D9 quote-style booking; D8 seasonal deals; GST trigger guidance mixed goods/services |
| D (watch) | Clinics/diagnostics · agents · agri-inputs · drivers | Regulated or app-exclusive or rural | none now; revisit with partners |

**Horizontal insight (core monetization):** S&E + trade-licence renewal + registers + Udyam + GST returns are *near-universal* — the renewals calendar (O2) is the stickiest core feature across all waves; employee headcount reconciliation (EPFO/ESIC cross-link) becomes urgent at >10–20 staff and is our growth trigger to the "Run" stage.

## 7. Open questions & verify-at-build flags

- `[VERIFY at build]` drug-licence fee slabs + ONDLS vs state portal for each MVP state (Maharashtra/Delhi/Gujarat are NOT on NLD per CDSCO — separate portals `[VERIFIED]`).
- `[VERIFY at build]` FSSAI band thresholds (conflicting 2026 sources) for N2/N9 food rows.
- `[VERIFY at build]` health-trade licence vs plain trade licence for salons per city; health-cert validity windows.
- `[VERIFY at build]` coaching registration rules per target state (variance).
- `[ESTIMATED]` digital-readiness scores are directional; confirm in founder interviews per pack.

## 8. Key sources (accessed 2026-09)

MoSPI HCES 2023-24 + revamped CPI (base 2024) coverage (Outlook Business, RBI Bulletin, MoSPI); ET commentary on HCES durables; Blume/Indus Valley Annual Report 2025; Kotak MF "The Great Consumption Shift" (May-2026); Deloitte-FICCI food report + NRAI India Food Services Report 2024 (via WION); VakilSearch/Agile/LegalTax/LegalDev/IIFL/Shriram/Aswas pharmacy licence guides; LegalSuvidha salon + S&E guides; ClearlyComply S&E; Dingg beauty-parlour state guide; JETRO/TCG coaching & beauty regulation briefs; SetupFiling trade licence; Sumvaad trade licence.
