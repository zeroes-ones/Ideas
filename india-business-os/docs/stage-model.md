# Lifecycle OS — Stage × Function × Size Model (india_os_09)
**Date:** 2026-09-08 · Status: draft for vision review. This is the substrate for "one app that adapts as the business grows **I → XS → S → M → L → Corp**, for any type A-Z."

## 0. The growth ladder (business side) — from individual earner to corporation
The business side is a **climb, not a static size**. The same person starts solo and, rung by rung, becomes a shop, then an employer, then a company. Each rung changes the legal form, the statutory triggers and what the OS activates — and **the profile should never make the user restart**: rungs upgrade in place, retaining documents, history and (on the customer side) the earned badge.
| Rung | Who | Typical form | Key triggers to move up | What unlocks at this rung (OS modules) |
|---|---|---|---|---|
| **I — Individual / solo earner** | TaskRabbit-class provider, home-based maker, street vendor | None / informal; Udyam **Assist** (via bank/DA, no PAN/GST) `[VERIFIED]`; e-Shram for gig; ProBadge = identity+skill cert (wave C, legal-gated) | Sells enough to want customers/trust/credit | ProBadge, availability + booking (D9), UPI collection; Launch Copilot "start light" (Udyam/UAP day-1) |
| **XS — Very small / street-micro shop** | Kirana, single-tech shop, home kitchen | Proprietorship; S&E + trade licence; GST optional < ₹40L/₹20L `[VERIFIED]` | Fixed premises → S&E/trade licence; regular customers | BusinessBadge (compliance-derived), catalog/orders/deals, renewals calendar seed |
| **S — Small** | Shop with staff (1–9) | Proprietorship/OPC/LLP; GST past thresholds or e-comm | GST crossing; hiring (ESIC at 10, EPFO at 20) `[VERIFIED]` | Full Comply calendar (GSTR, licence renewals), people triggers, credit readiness (Udyam) |
| **M — Medium** | Multi-outlet / employer (10–99) | LLP/Pvt Ltd; MSME Small class ≤₹25Cr/₹100Cr | EPFO/ESIC active; branches; audit at ₹1Cr/₹10Cr `[VERIFIED]` | Payroll bridge, branch config, statutory audit prep, loan/TReDS/GeM |
| **L — Large** | 100–249, beyond micro | Pvt Ltd full governance | Medium class ≤₹125Cr/₹500Cr | Board/audit/ESOPs/export (IEC) packs — Phase 3+ |
| **Corp** | 250+, group structures | Listed-scale corporate | Beyond MSME | Out of scope; hand-off note in roadmap |

**Design rule:** the OS *is* the growth rails — when a trigger fires (premises lease signed, 10th employee, turnover band crossed, first branch), the profile upgrades rung and activates the next module set. Graduation events are the product's north-star moment ("you're no longer a shop — here's what changes").
Size segments (per MSME Apr-2025 criteria + statutory triggers):
- **Micro** — investment ≤ ₹2.5Cr & turnover ≤ ₹10Cr; 0–9 employees; proprietorship/OPC/LLP dominant; GST optional below ₹40L/₹20L.
- **Small** — ≤ ₹25Cr / ≤ ₹100Cr; 10–99 employees; EPFO at 20+, ESIC at 10+ (notified areas); tax audit at ₹1Cr (₹10Cr digital) `[VERIFIED]`.
- **Medium** — ≤ ₹125Cr / ≤ ₹500Cr; 100–249 employees; Pvt Ltd compliance full stack (AGM, audit, board minutes).
- **Large / Corp** — beyond MSME; outside MVP scope (Phase 3+ packs).
| # | Stage | Definition | Trigger to enter |
|---|---|---|---|
## 1. Lifecycle stages (the adaptive spine)
| # | Stage | Definition | Trigger to enter |
|---|---|---|---|
| S1 | **Start** | Idea, viability, name/brand, choosing structure | "I want to start a business" |
| S2 | **Formalize** | Entity registration + PAN/TAN + GST + Udyam + vertical licences → legally operational | Decision on entity (or "I already sell informally") |
| S3 | **Comply** | Ongoing statutory: ROC/LLP filings, GST returns, ITR, DIR-3 KYC, licence renewals, PF/ESI once thresholds hit | Certificate of Incorporation / first GST return |
| S4 | **Run** | Daily ops: invoicing, khata/ledger, payments, documents, basic payroll, insurance | First customer/sale |
| S5 | **Grow** | Credit (MSME loans, TReDS), new markets (e-comm/GeM), hiring past PF/ESI thresholds, branches | Crossing scale triggers (employees ≥10/20, turnover bands) |
| S6 | **Scale** | Multi-state/entity, statutory audit, board governance, ESOPs, exports | Medium/large size (MSME Medium class; >₹100Cr turnover `[ESTIMATED]`) |

## 2. Function areas (columns — the A-Z of business needs)
F1 Legal & statutory · F2 Tax & finance · F3 Registrations & licences · F4 People & payroll · F5 Operations & documents · F6 Growth, credit & markets · F7 Risk & insurance

## 3. The matrix (which cell = which capability the OS must own)
| Stage | F1 Legal | F2 Tax | F3 Reg & licences | F4 People | F5 Ops/doc | F6 Growth | F7 Risk |
|---|---|---|---|---|---|---|---|
| S1 Start | Entity advisor (liability/funding/tax trade-offs) | Projected GST applicability | Licence pre-check by type+state | — | — | Viability checklist | — |
| S2 Formalize | MOA/AOA, deed prep guidance | PAN/TAN (via SPICe+), GST reg. | **Launch Copilot journeys** (DSC→SPICe+→post-COI→Udyam→licences) | — | Document readiness & vault seed | Bank account opening | — |
| S3 Comply | ROC/LLP annual filings | GSTR-1/3B, ITR, composition | Renewal calendar (S&E, FSSAI, trade) | PF/ESI triggers | Deadline alerts | — | — |
| S4 Run | Contract templates | Invoicing→returns bridge | — | Basic payroll, appointment letters | Ledger/khata, docs vault | UPI/payment links | Business insurance nudge |
| S5 Grow | Branch/entity conversion | Tax planning at bands | Multi-state registrations | Hiring compliance pack | Inventory basics | MSME credit, TReDS, GeM, e-comm seller | — |
| S6 Scale | Board & audit readiness | Statutory audit, transfer pricing (later) | Exports (IEC) | ESOPs | Governance data room | Capital raise readiness | — |

## 4. What this means for product shape
- **One profile, many stages**: the app tracks the business's stage and unlocks modules; micro-sole-trader sees a light Formalize/Comply surface, a scaling Pvt Ltd sees the full matrix.
- **v0.2 note:** this model governs the **business-owner side**. The customer side has its own journey (Discover → Consider → Browse → Order → Pay → Track → Repeat) documented in module-map.md §2.5 and screens S16–S24; the two connect via the verified-merchant badge (module-map §3).
- **MVP slice** = the S2 (Formalize) row for rungs I→XS→S + the S3 (Comply) calendar seed — "Launch Copilot (register & formalize)" per user decision, with rung-I onboarding (Udyam Assist) as the growth entry point. Everything else is roadmap.
- Row/column weights will be re-tuned after founder validation (Phase 4 open question #6).
