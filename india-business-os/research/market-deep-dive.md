# Market Deep-Dive — Competitive Depth, Network Rails, Discovery Trust, Sizing (India local commerce + SMB lifecycle)

> **Date:** 2026-09-08 · **Status:** Consolidates loops D1–D4; companion to `everyday-needs-landscape.md` and `two-sided-wants-gaps.md`. Tags: `[VERIFIED]` ≥2 sources / robust survey · `[ESTIMATED]` single-source/inference · `[VERIFY]` needs primary research.

## D1. Competitive & pricing depth — what owners already pay

**Billing/ledger incumbents (the "Run" layer is crowded and cheap/free):**
| Player | Product | Pricing evidence | Monetization |
|---|---|---|---|
| Vyapar | GST billing + inventory (mobile/desktop) | Mobile Silver ≈₹629/yr, Gold ≈₹719/yr (1-yr, India); desktop+mobile Gold ≈₹3,869/yr; free tier; "1M+ businesses" `[VERIFIED — vyaparapp.in, resellers, maqtoob Jul-2026]` | Freemium subscription; multi-device/sync upsell |
| OkCredit | udhar khata ledger | Basic free forever (unlimited entries); Premium = ad-free, multi-device, GST billing, unlimited SMS; 11 languages `[VERIFIED — okcredit.in]` | Free core → credit/fintech (not software fees) |
| Khatabook | khata + payments | Free-ledger model (same as OkCredit) `[ESTIMATED]` | Fintech/credit |
| Tally Prime / Zoho Books | accounting for grown SMEs | Tally ₹18k+/yr class; Zoho from ~₹9/user/mo `[ESTIMATED]` | B2B SaaS |

**Compliance-marketplace incumbents** (from `competitive-map.md`): Clear, IndiaFilings, Vakilsearch, LegalRaasta sell **one-off assisted filings** (Udyam/incorporation/GST) at ₹500–₹15k/event `[VERIFIED — earlier map]`. They own the *event*, not the lifecycle, and have no consumer-side loop.

**Owner-side pricing conclusion:** owners pay **₹500–4,000/yr** for serious billing tools; free tiers are the acquisition hook; **compliance is bought as events, not subscriptions** → market data points to journey-priced entry (Launch Copilot ₹499–999 class, benchmarked to Vyapar mobile) with retention via the renewals calendar, not an annual SaaS fee for shops that never bill digitally. **Override (founder, 2026-09-08): product monetization decided SaaS-first from business owners** (recurring subscription; consumer side free as growth engine — see `docs/scope-brief.md` "Pricing model"). The market facts above still anchor the achievable price point; monthly willingness-to-pay remains an interview question (H1–H6/W38), not a settled conclusion.

## D2. Network rails & ecosystem — ONDC and the platform fights

- ONDC crossed **500M cumulative transactions** (Jul-2026); FY26 = 218M (vs 0.2M FY23); **>200k active retail merchants**, 1M+ service providers; mobility/metro/agri expansion `[VERIFIED — DPIIT via Moneycontrol Aug-2026]`.
- **DigiDukaan** (govt kirana-onboarding) has ~13k kiranas in Hyderabad/Jaipur only `[VERIFIED]`; **MSME TEAM** ₹277.35Cr FY25-27 (50% women-owned target) `[VERIFIED]`.
- **Zoho invested ₹70Cr** in ONDC; its finance suite (Vikra seller app, Zoho Books/Inventory/Commerce) is the integration entry point for MSME sellers `[VERIFIED — YourStory/ET May-2026]`.
- 13k–200k ONDC merchants vs **~1.3Cr kiranas** `[ESTIMATED — widely cited ~12–13M]` → even the state-backed network has barely dented local retail onboarding.
- QC brands (Zepto/Blinkit/Instamart) partner kiranas as micro-fulfilment; Grant Thornton: 40% of kiranas open to QC partnership, 20% only with ops/tech support `[VERIFIED — Apr-2026]`.

**Implication:** ONDC is a *rail, not a moat* — it adds no compliance/verification layer, no lifecycle OS, no badge. Our differentiation (compliance → badge → trust) is orthogonal; ONDC is a potential *distribution channel* for the business side (catalogue export) and a risk only if we tried to be "another marketplace". Watch: Zoho+ONDC seller tools competing for the same "help the shop digitize" wallet as us in the Run layer — but not in Formalize/Comply.

## D3. Discovery & trust — how customers find local businesses today

- Consumer discovery = **Google Business Profile (Maps) + category apps** (Justdial services, Zomato food, Practo health, Urban Company home services) `[VERIFIED — multiple 2025-26 local-SEO sources]`; ~half of Google searches have local intent; "near me" queries >5× growth; Hindi local search +90% YoY (Google India) `[VERIFIED — SEO industry, Google-cited]`; 76% of voice searches local (BrightLocal) `[VERIFIED]`.
- **Justdial trust is broken**: sustained 1–2★ user reviews citing fake/unusable paid leads, aggressive sales, refund traps (₹17k–28.5k packages, ECS auto-debits) `[VERIFIED — SmartCustomer/Wanderlog review aggregates]`; pay-per-lead model mismatches small cash flows.
- **>40% of small businesses have no meaningful online presence**; digital marketing seen as expensive/complex `[VERIFIED — discovery-crisis analysis citing industry research; ESTIMATED precision]`.
- 88% of Indian consumers trust online reviews ~as much as personal recommendations (LSA 2024) `[VERIFIED]`; 83% check Google reviews `[VERIFIED]`.
- Emerging: AI/chat discovery (ChatGPT/Gemini pull local entities; Bing→Copilot feed) and **WhatsApp-native discovery** (Bino et al. — instant listings/bookings + real-time offers) `[VERIFIED — vendor claims, directional]`.

**Implication:** the discovery layer owners pay for (Justdial PPL, GBP SEO agencies) is exactly where trust is missing — **no platform ties verified-compliance to discovery**. Google Maps has the reach but no verified-compliance signal and no transaction loop; Justdial has lost trust; ONDC has no trust layer. This is the wedge our badge-led discovery owns.

## D4. Market sizing anchors (TAM/SAM/SOM scaffolding — `[VERIFY]` with primary data before investor use)

| Anchor | Value | Source tag |
|---|---|---|
| Udyam + Udyam Assist registrations | **6.3Cr+ enterprises** (2026) | `[VERIFIED]` (Udyamita/DPIIT-cited) |
| Active GST registrations | **1.52Cr** (Jul-2025) | `[VERIFIED]` (SBI Research) |
| Kirana share of grocery | **91% CY2025 → ~86% CY2030**; grocery toward ₹1T; 233M low-mid households; ₹100–200 AOV | `[VERIFIED]` (Redseer Jan-2026) |
| QC user base | ~51M (late-2025) vs 2.2M (2021) | `[VERIFIED]` (Redseer/Dezerv) |
| MSME digital divide | 53.8% use ≥1 tool; 46.2% fully offline | `[VERIFIED]` (n=7,835) |
| Food services | ₹7.76T by FY28; 8.5M→10.3M employed | `[VERIFIED]` (NRAI) |
| Local/location services market | ~$1.52B, ~3× by 2030 | `[ESTIMATED — vendor-cited]` |
| **Bengaluru pilot denominator** | Kirana/shop + service-trade counts by ward/vertical **not yet collected** | `[VERIFY]` — needs BBMP/KA data pass |

**Sizing logic for the pitch (later):** TAM = India's 6.3Cr MSMEs × lifecycle value; SAM (first wedge) = shops in pilot states/verticals needing formalization+compliance; SOM = Bengaluru pilot shop count + their consumers. A defensible SOM needs one more research pass (BBMP trade-licence counts, KA S&E registrations by industry, ward-level vertical density).

## Strategic implications (for the docs)

1. **Run layer is a red ocean** (Vyapar free/OkCredit free + fintech) — do not build billing/ledger in MVP; badge, deals, bookings, compliance are the uncontested layers (`scope-brief` OUT list already reflects this).
2. **Compliance is event-priced** in the market today → market data favours journey-priced entry `[pricing benchmark Vyapar/OkCredit]`; **founder decision (2026-09-08) = SaaS-first from business owners** (scope-brief "Pricing model") — keep journey pricing viable as the onboarding/landing offer and the renewals calendar (C5) as subscription retention, but validate monthly WTP in H1–H6 before freezing tiers.
3. **Discovery's trust vacuum is our customer-side opening**: verified-badge discovery ≠ Justdial (no compliance), ≠ Google (no loop), ≠ ONDC (no trust layer) → position against all three explicitly.
4. **ONDC = future export rail for merchant catalogues** (P2), not an MVP competitor; monitor Zoho's seller-tooling as the closest long-run "Run-layer" rival with capital.
5. **Justdial PPL economics are the cautionary tale** for merchant monetization: never charge shops for fake leads; charge for outcomes (customers actually transacting) — aligns with our order-linked model.

## Open items
- Bengaluru pilot market map (BBMP trade-licence counts, KA S&E by industry, vertical density per ward) `[VERIFY]`.
- Primary pricing validation: what would a kirana pay monthly for badge + deals + orders (vs ₹0 for Vyapar/OkCredit free tiers)?
- Re-check ONDC retail momentum in Bengaluru specifically before deciding catalogue-export P2 timing.
