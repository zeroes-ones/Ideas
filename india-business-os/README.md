# India Business OS — project home (working title)

A **two-sided "super app" for Indian local commerce**: one app where a shop owner goes from *starting* to *compliant* to *growing*, and their customers get *trusted, nearby* shops with orders, service bookings and genuine deals. The bet, in one line: **compliance becomes a growth asset** — the shops this app helps formalize automatically become the verified supply that customers buy from (the badge is the bridge).

> Status: **research + spec complete (v0.3), pre-build**. Every claim in this folder is tagged `[VERIFIED]` / `[ESTIMATED]` / `[VERIFY at build]`. Research dates: Sep-2026. Author: session agent for the founder. If you are new to this folder, start with the three reading paths below.

---

## 1. The idea in 3 sentences
1. **Business side (Entry A)** — a **Launch Copilot** that guides *any* India shop (very small → medium, A–Z of types) through entity choice → registration (Udyam/GST/company/S&E) → licences, then keeps it compliant with a renewals calendar. It guides; it never files or holds money.
2. **Customer side (Entry B)** — neighbours discover **verified** merchants (badge only while compliant), order goods, **book service slots** (mechanic/appliance/electrical), and redeem **merchant deals** — all hyperlocal (pickup/self-delivery; no wallet, no fleet).
3. **The loop** — customer sees the badge → prefers the compliant shop → more shops formalize to earn the badge → supply and demand feed each other. *External research backs this: 40% of customers already ask shops for proof of registration (IFMR), 47% wait for deals (Rukam), kirana still holds 91% of grocery (Redseer).*

## 2. How to read this folder

### Path 0 — "Show a partner" (30 minutes) ⭐
1. **`PARTNER-BRIEF.md`** — readable overview with diagrams: idea, loop, market, monetization (SaaS-first + individual options), pilot plan, and the decision register to review with partners.
2. **`docs/partner-feedback-log.md`** — capture sheet for each partner session (decisions reviewed, their view, quotes, actions).

### Path 1 — "What is this?" (10 minutes)
1. `vision.md` — the umbrella: personas, pillars, metrics, risks.
2. `docs/scope-brief.md` — the MVP contract: IN, OUT, metrics (SM/CM/LM), assumptions, open questions.
3. `docs/module-map.md` §0 + §2.7 — how the product is built as config, and the pack roadmap (waves A–D).

### Path 2 — "Why would it work?" (research, ~1 hour)
Read in this order; each file ends with implications:
1. `research/two-sided-wants-gaps.md` — owner wants × customer wants × the 8 gaps we fill. **Start here** — this is the "help each other" thesis with data.
2. `research/everyday-needs-landscape.md` — 12 need clusters × business types × waves A–D.
3. `research/market-deep-dive.md` — who already serves owners & at what price (Vyapar/OkCredit/Justdial/ONDC) — why we *don't* build billing/leads.
4. `research/regulatory-journey.md` — the licence/registration ground truth the copilot teaches.
5. `research/competitive-map.md` — incumbents vs our whitespace.
6. `research/bengaluru-pilot-map.md` — the city, post-BBMP split: 5 corporations, 369 wards.
7. `research/hyderabad-pilot-map.md` — Hyderabad (TS/GHMC) pilot research — partial web pass done 2026-09-08 (licences, S&E, gig Act 2026 verified); W35b denominator still pending `[VERIFY]`.

### Path 3 — "Let's validate/build it" (action)
1. `docs/work-items.md` — W1–W40 story map (Entry A skeleton → Entry B marketplace → bookings/deals → **W35–W40 pilot-data & validation sprint**).
2. `docs/validation-interviews.md` — scripts (merchant + consumer) with hypotheses H1–H6 and outreach invites.
3. `docs/field-sample-sheet.md` — W36 street-walk protocol to ground-truth the licence data.
4. `docs/pilot-recruitment-playbook.md` — how to reach the ≥100-verified gate (OQ2 answered).
5. `scripts/pilot-denominator.py` + `research/pilot-denominator.md` — **first executable step (W35)**: fetch the OpenCity licence CSVs → ward × vertical counts. Run it on an internet-connected machine (this sandbox blocks outbound HTTP); paste the output back to refine the mapping.

## 3. Map of every file
| File | It answers | Open when |
|---|---|---|
| `vision.md` | What are we building and why (two-sided) | First / strategy reviews |
| `docs/scope-brief.md` | What is IN/OUT, success metrics, open questions | Any scope debate |
| `docs/pricing-model.md` | Monetization: SaaS-first decision (business owners) + individual-provider options (OQ-I3/OQ-V2) | Pricing/monetization debates |
| **`PARTNER-BRIEF.md`** | **Readable overview w/ diagrams for partners (Path 0)** | **Show a partner / investor** |
| **`docs/partner-feedback-log.md`** | **Capture sheet for partner sessions** | **After each partner meeting** |
| `docs/marketplace-audit.md` | Marketplace cold-start/liquidity/trust audit + unit-econ gaps (skill-assisted) | Before build / pricing finalization |
| `docs/journey-flows.md` | Role journeys & **40 real-time scenarios (8 per actor: customer/individual/small/medium/large)** with flows + economics | Partner reviews · UX design · W38 scripts |
| `docs/changelog.md` | Project history log (date → what changed → why → OQ/decision resolved) | Any session end / decision day |
| `docs/module-map.md` | Which modules, config packs, waves A–D | Architecture/pack planning |
| `docs/stage-model.md` | Lifecycle stages S1–S6 × functions × **growth ladder I→XS→S→M→L→Corp** | Understanding "one app that adapts" |
| `docs/domain-model.md` | Entities + state machines (incl. bookings/deals) | Build/API work |
| `docs/api-contract.md` | REST endpoints, auth, failure modes | Build/API work |
| `docs/screen-inventory.md` | 26 screens, routes, states (EN/HI) | Build/UX work |
| `docs/work-items.md` | Story map W1–W40, sizes, sequencing | Sprint planning |
| `docs/validation-interviews.md` | Interview scripts + invites (H1–H6) | Pre-build validation |
| `docs/field-sample-sheet.md` | W36 street-walk capture protocol | Field work |
| `docs/pilot-recruitment-playbook.md` | How to get ≥100 verified merchants | Supply ramp (W39) |
| `research/regulatory-journey.md` | Licences/registration facts | Content/legal config |
| `research/individual-providers-gig.md` | Gig/home-services workforce + person-pack design + KA Gig Act watch | Individual-provider decisions |
| `research/competitive-map.md` | Incumbents + whitespace | Positioning |
| `research/everyday-needs-landscape.md` | Need clusters × B-types × waves | Pack decisions |
| `research/two-sided-wants-gaps.md` | Owner/customer wants + gap matrix | Thesis/validation |
| `research/market-deep-dive.md` | Competitive pricing, ONDC, sizing | Investor/founder review |
| `research/bengaluru-pilot-map.md` | Bengaluru governance + pilot unit | Pilot planning |
| `research/hyderabad-pilot-map.md` | Hyderabad (TS/GHMC) pilot research — partial pass done (licences/S&E/gig Act `[VERIFIED]`); denominator W35b `[VERIFY]` | Parallel pilot-city planning (W35b) |
| `research/pilot-denominator.md` | W35 method + limits | Running W35 |
| `research/research-brief.md` | Consolidated insights + open Qs | Research sweep |
| `scripts/pilot-denominator.py` | Fetches/maps licence data → ward counts | W35 execution |

## 4. Idea keys — the vocabulary to hold in your head
- **Two-sided loop** — merchants formalize → get verified → badge → customers buy → more merchants formalize. *"Compliance = growth asset."* Everything traces to this.
- **Entry A / Entry B** — business Launch Copilot / customer marketplace. One codebase, one account (a phone can hold both roles).
- **Common core + packs** — C1–C9 modules work for *any* type; verticals (kirana, appliance, electrical, mechanic…) are **config** (licence bundles + journey order), never separate code. Customer side rides D1–D9; bridges B0–B3 connect sides.
- **Waves A–D** — A = pilot now (founder's 4 examples) · B = pharmacy/salon/F&B/mobile-repair (data-picked) · C = broader everyday needs · D = watchlist.
- **Badge = supply gate** — auto-derived from compliance state; auto-hides if out of compliance; consumers default to verified-only discovery.
- **Guardrails (non-negotiables)** — never holds funds (RBI PPI); guides, never files; badge hides on non-compliance; order-verified reviews only; deals server-validated (no fake MRP claims); bookings pay-at-shop; ≥100 verified merchants before consumer launch; compliance messaging = enablement, never fear; no paid-lead selling; no billing/ledger suites.
- **Evidence discipline** — `[VERIFIED]` (≥2 sources), `[ESTIMATED]` (1 source/inference), `[VERIFY at build]` (state-specific/conflicted). Research docs list sources + dates at the bottom. Treat untagged numbers as untrusted.

## 5. State of the plan & what's open
- **Done:** research (6 files) + full spec (5-doc pattern + stage model + module map + vision) through v0.3 + validation tools + W35 tooling.
- **Open decisions (founder)** — scope-brief OQs 1–10: PA partner & fees; which hook (badge/deals/bookings) converts first (OQ3 → H1–H6 interviews); booking workflow readiness of mechanics; deal/no-show rules; **OQ9 resolved → SaaS-first from business owners (2026-09-08); remaining = monthly price point + subscription tiers, validate in H1–H6** · **OQ-I3 resolved → individuals (rung I) ₹0 free verified core, businesses XS→L pay SaaS (2026-09-08; `docs/pricing-model.md`)**; licence-portal routing — Bengaluru 5 corporations + Hyderabad GHMC/TS (OQ10); Hyderabad field pass = W35b + `research/hyderabad-pilot-map.md`.
- **First executable step:** run W35 (`scripts/pilot-denominator.py`), then W36 field walk, then W38 interviews — all tooled and cross-linked.

## 6. Version control & changelog conventions
- **Repo:** `zeroes-ones/Ideas` (private). Keep everything for this project inside it; commit often, in **logical units**, one type per commit:
  - `research: …` — research/*.md findings (tagged `[VERIFIED]/[ESTIMATED]`, sources at bottom)
  - `spec: …` — scope/module/domain/api/screens changes that alter the contract
  - `decision: …` — founder decisions recorded in scope-brief OQs / pricing-model (date + tag)
  - `validation: …` — interview scripts, field tools, work-item updates
  - `partner: …` — partner briefs, feedback logs, journey flows
  - `chore: …` — scaffolding, housekeeping (no product content)
- **Keep docs in sync:** when a decision changes, update the doc that owns it *and* its cross-references (README map, PARTNER-BRIEF §15) in the same commit.
- **History log:** new entries go to `docs/changelog.md` (date → what changed → why → which OQ/decision it resolves).
