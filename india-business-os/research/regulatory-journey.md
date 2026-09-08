# Research Brief — Regulatory Journey: Starting & Formalizing a Business in India
**Date:** 2026-09-08 · **Status:** working draft, facts tagged `[VERIFIED]` (≥2 current sources, 2025–2026) / `[ESTIMATED]` (ranges or single source) / `[STALE-FLAG]` (conflicting older data seen in the wild). Re-verification pass scheduled in Phase 4.
**Purpose:** ground-truth substrate for the Launch Copilot MVP slice (india_os_02).

## 1. Entity options (the decision tree founders face)
| Entity | Legal basis | Min people | Liability | Compliance load | Reg. cost (all-in) `[ESTIMATED]` |
|---|---|---|---|---|---|
| Sole Proprietorship | No dedicated act | 1 | Unlimited | Lightest | ₹1,500–₹10,000 |
| Partnership firm | Partnership Act 1932 | 2 | Unlimited (joint) | Light | ₹2,000–₹8,000 |
| LLP | LLP Act 2008 | 2 designated partners | Limited | Light-Med (Form 8 by 30 Oct, Form 11 by 30 May; audit if turnover >₹40L or contribution >₹25L) | ₹5,000–₹10,000 |
| One Person Company (OPC) | Companies Act 2013 | 1 + nominee | Limited | Med (MGT-7A/AOC-4 annual) | ₹6,000–₹12,000 |
| Private Limited | Companies Act 2013 | 2 directors + 2 shareholders | Limited | Highest (ROC annual, AGM, audit, board minutes) | ₹6,000–₹17,000 |
| Section 8 (non-profit) | Companies Act 2013 | 3+ | Limited | High | ₹5,000+ |

Key selection filters `[VERIFIED]`: liability exposure → limited-liability form (LLP/OPC/Pvt); future equity funding → Pvt Ltd only (share-based); solo control → proprietorship/OPC; continuity after founder exit → LLP/OPC/company; tax: proprietorship = slab rate, LLP/firm = ~30% flat, companies 25%/22% + MAT nuances. **Wrong-entity cost:** Pvt Ltd has heavy annual ROC/audit burden even at zero revenue — a common first-time-founder mistake to be surfaced by an entity advisor.

## 2. Incorporation path for Pvt Ltd / OPC (MCA SPICe+) `[VERIFIED]`
1. **DSC Class 3** per director/partner (₹800–₹2,500; 1–3 yr validity; CAs: eMudhra/Sify/NSDL). 1–2 working days.
2. **DIN** — auto-allotted via SPICe+ (no separate fee).
3. **Name reservation** — SPICe+ Part A or RUN; ₹1,000 per attempt, up to 2 name proposals; approval 1–3 working days; name held 20 days.
4. **SPICe+ Part B** — single integrated filing bundling: incorporation, eMOA (INC-33), eAoA (INC-34), AGILE-PRO-S (GSTIN, EPFO, ESIC, Professional Tax, bank account opening), PAN+TAN (₹0–₹143).
5. **Fees:** MCA filing fee ~₹0 for authorized capital ≤ ₹1L (2025 update: near-zero up to ₹15L per one source `[ESTIMATED]`); stamp duty state-dependent ₹500–₹5,000+ (high: Punjab/Gujarat/Kerala; low: Delhi/Karnataka/TN `[ESTIMATED]`).
6. **Certificate of Incorporation + CIN** digitally; PAN/TAN included. Total govt+fees: **₹6,000–₹17,000 all-in** incl. professional help; **7–15 working days** typical.
7. 2026 MCA trend reported: digital name approval/DIN within 24h, AI-assisted MOA/AOA validation `[ESTIMATED — vendor claims, verify]`.

**Post-incorporation deadline traps (Pvt Ltd) `[VERIFIED]`** — ideal "first-year compliance calendar" content:
- Open current bank account (needed before INC-20A).
- **INC-20A** Declaration of Commencement of Business ≤ 180 days (penalty ₹50,000 + ₹1,000/day).
- First board meeting ≤ 30 days; **appoint statutory auditor ≤ 30 days**.
- Share certificates ≤ 2 months.
- Display CIN/name at premises & on letterheads/invoices.
- **Annual:** AGM ≤ 6 months after FY end; MGT-7/AOC-4 within 60/30 days of AGM (₹100/day late); DIR-3 KYC by 30 Sep; ≥4 board meetings/yr (gap ≤ 120 days); ITR by 31 Oct (audit) / 31 Jul. Miss 2+ years → ROC strike-off + director disqualification 5 yrs.

## 3. GST registration `[VERIFIED]`
- **Thresholds (normal states — incl. all 5 MVP states MH/KA/DL/TN/GJ):** goods ₹40L, services ₹20L; mixed goods+services → lower ₹20L applies for services component `[VERIFIED]`.
- **The "special category" nuance (Phase-4 resolved, matters only for future state expansion):** two distinct rules are commonly conflated — (a) constitutional special-category states with **services** threshold ₹10L (retained after 2019 amendment for Manipur, Mizoram, Nagaland, Tripura; other hill/NE states moved to ₹20L per amendment) and (b) Notification 10/2019 carving goods-suppliers **out of the ₹40L exemption** (i.e., ₹20L goods threshold) in Arunachal, Manipur, Meghalaya, Mizoram, Nagaland, **Puducherry, Telangana**, Sikkim, Tripura, Uttarakhand. Sources disagree on the current services list (TaxGuru statutory table vs 2026 practitioner summaries), so the rule engine should encode Notification 10/2019 + CGST §22/§24 with a `[VERIFY against CBIC]` flag **before any state outside the MVP five is enabled**. MVP scope unaffected (all 5 states are normal-category).
- **Compulsory regardless of turnover:** inter-state goods supply, e-commerce sellers/operators (Amazon/Flipkart/Meesho from day 1), RCM payers, casual/non-resident persons, TDS/TCS deductors, ISD, OIDAR providers.
- **Composition scheme** (lower compliance): goods ≤ ₹1.5Cr / services ≤ ₹50L turnover; 1% (0.5% CGST+0.5% SGST) traders; NOT for e-commerce sellers.
- Voluntary registration allowed (ITC + credibility). Portal free; approval ~3–7 working days. Non-registration penalty ≥ ₹10,000 or 10% of tax due.

## 4. Udyam (MSME) registration `[VERIFIED]`
- **Free, online-only, Aadhaar+OTP+PAN**; no document upload (portal auto-fetches ITR/GST/turnover data); one registration per business; lifetime validity (update on change); URN + QR certificate. 15–30 min typical. **Beware look-alike paid sites** (a documented real-world trap to warn users about).
- Eligible entities: proprietorship, HUF, partnership, company, LLP, co-op, society, trust. Sectors: manufacturing, services, **retail & wholesale trade (eligible since 02 Jul 2021 — loan/tender benefits)**.
- **Classification, revised 01 Apr 2025 `[VERIFIED — multiple Nov 2025 sources]`:** Micro: investment ≤ ₹2.5Cr **and** turnover ≤ ₹10Cr · Small: ≤ ₹25Cr / ≤ ₹100Cr · Medium: ≤ ₹125Cr / ≤ ₹500Cr. `[STALE-FLAG: several pages still publish pre-2025 limits (₹1/₹5Cr micro etc.) — our content engine must use the 2025+ criteria and warn users against outdated info.]`
- Benefits: priority-sector/CGTMSE credit, **45-day delayed-payment protection (MSMED Act §15–24)**, GeM tender preference, subsidies (PMEGP etc.), TReDS.

## 5. State & local licences (the "vertical pack" layer) `[VERIFIED unless noted]`
| Licence | Scope | Fee (indicative) | Renewal / notes |
|---|---|---|---|
| **Shop & Establishment** | Every commercial establishment (even single-person) under state S&E Act; register ≤ 30 days of opening | ₹100–₹2,000 (state/employees; some states to ₹5,000) | 5 yrs most states; **Maharashtra 1 yr** `[VERIFIED]`; display + renew; labour dept. Penalties to ₹50,000 + prosecution |
| **Trade licence** | Municipal (BMC/BBMP/GHMC/MCD…), activity-specific | ₹1,000–₹10,000 city-wise | Periodic/1-yr renewal; separate from S&E |
| **FSSAI** | All food businesses (FoSCoS portal) | Basic ≤₹12L turnover: ₹100 · State ₹12L–₹20Cr: ₹2,000–₹5,000 · Central >₹20Cr: ₹7,500 `[VERIFIED — Regikart 2026-06 + VirtualAuditor 2026-04 agree]` | 1–5 yr validity; renew 30 days pre-expiry; **FoSTaC food-handler training mandatory** for applicants; no licence = fine to ₹5L + imprisonment (FSS Act §59/§63) |
| **Professional tax** | Only states levying it (MH, KA, TN, WB…) — employer registers when it has employees | ≤ ₹2,500/employee/yr | State-specific |
| **EPFO / ESIC** | 20+ employees (EPF); 10+ in notified areas (ESI) | % contributions | Monthly |
| **Fire NOC, health NOC, signage** | City/state + activity dependent | ₹2,000–₹15,000 | E.g., F&B in metros |

Vertical licence bundles that power "A-Z packs": **retail/kirana** = S&E + trade licence + GST + Udyam; **F&B** = FSSAI + S&E + trade licence + fire/health NOC + GST; **services/consulting** = S&E + GST-if-applicable + professional tax-if-employees + Udyam; **e-commerce seller** = GST day 1 (TCS) + Udyam + S&E-if-office. Restaurant example: 8–14 licences/registrations before opening `[ESTIMATED]`.

## 6. Typical totals (for UX: "cost & time to launch" estimates)
- Proprietorship micro stack (Udyam + GST + S&E): ₹1,000–₹8,000, days–2 weeks.
- Pvt Ltd full stack to operating: ₹6,000–₹17,000 registration + ~2–4 months total calendar if licence applications run parallel; **first-year compliance ₹20,000–₹40,000** (ROC, GST filing fees, ITR, audit) `[ESTIMATED]`.

## 7. Implied product requirements (feeds MVP spec)
1. **Entity advisor** — decision quiz surfacing liability/funding/tax/compliance trade-offs + ongoing-cost warnings (Pvt Ltd burden at zero revenue).
2. **Guided sequence engine** — prerequisite-ordered task lists (DSC → name → SPICe+ → post-COI → bank → INC-20A…), each task = what/why/docs/deadline/govt-link.
3. **Licence/vertical pack recommender** — by business type + state + employees + premises.
4. **First-year compliance calendar** — INC-20A, auditor, AGM, DIR-3 KYC, GST returns, licence renewals, EPFO/ESIC — with proactive bilingual reminders (the #1 recurring-pain surface incumbents under-serve).
5. **Bilingual EN+Hindi** content layer; plain-language explanations of every govt portal step.
6. **Trust guardrails** — warn against paid look-alike portals; distinguish govt fees (₹0–₹5,000) from professional fees (transparent, itemized).
