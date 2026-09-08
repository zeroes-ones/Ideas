# Individual Verification & Trust — How an individual becomes a "trusted person" in India

> **Date:** 2026-09-08 · **Status:** Research for the **ProBadge** trust tier (individual providers, rung I of `docs/stage-model.md` §0). An individual has no licences to verify — their trust = **who they are (ID), what they can do (skill), whether they are safe (background), and how they behave (ratings)**. This doc maps the reusable, low-cost rails India already provides.
> **Tags:** `[VERIFIED]` ≥2 sources/robust survey · `[ESTIMATED]` single-source/inference · `[VERIFY at build]`.

## 1. Why verification is the product (for individuals)
- Home-services trust is the category's core barrier — "letting a stranger into the home"; fraud/impersonation were historically common `[VERIFIED — YourStory case study, multiple]`.
- Platforms that won treated **vetting as a trust signal**: Urban Company filters onboarding (govt ID checks + police verification via AuthBridge + in-person interviews + skill assessments + references) and **accepts only ~25–30% of applicants** — the rejection rate itself became consumer trust `[VERIFIED — UC statements/YourStory]`. ~₹50,000/partner spent on initial training; NSDC/MSDE-certified curricula `[VERIFIED — UC statement]`.
- Individuals have **no premises-licence regime** (no S&E/trade licence) → without a verification layer they are invisible-but-risky; with one, they are the supply for rung-I → XS growth `[VERIFIED — individual-providers-gig.md]`.

## 2. The verification stack (L1–L4) — composable "ProBadge"
ProBadge = a **profile of small verified claims** (chips), each independently earned; consumers read what is actually proven. Do **not** merge into the compliance BusinessBadge (different semantics, LM2-style audit breaks).
| Layer | Claim | India rails (reuse, don't rebuild) | Cost/latency `[V unless noted]` |
|---|---|---|---|
| **L1 Identity** | "This is a real person, this is their face/name" | **Aadhaar eKYC** — OTP (₹1L/yr txn cap under RBI), biometric, or **face auth** (fastest-growing; 213Cr+ cumulative txns by Aug-2025; 2.21B auth txns Aug-2025 alone) `[VERIFIED]`. **DigiLocker** pulls of issuer-signed docs (676.3M users, 9.5B+ docs, Mar-2026) — no re-verification needed `[VERIFIED]`. On-arrival selfie match vs profile photo (UC used Azure face services) `[VERIFIED]` | World Bank: auth cost fell **$23 → ~$0.15/check** `[VERIFIED]` |
| **L2 Background** | "No adverse criminal record" | **State police portals** for character/police verification (KA: ksp.karnataka.gov.in; fee ₹50–200, 15–30 days) `[VERIFIED — CitizenNest]`; tenant/domestic-worker verification **mandatory** in Delhi/Maharashtra/Karnataka (fines up to ₹5,000, landlord-filed) `[VERIFIED]`. BGV vendors at scale (UC used **AuthBridge**; IDfy/Signzy class) | ₹50–200 govt; BGV vendor ~₹100–500/check `[ESTIMATED]` |
| **L3 Skill** | "Trained/qualified for the trade" | **ITI / NSDC** certificates; **PM Vishwakarma** (craftspeople: certificate + toolkit + credit; HelpRush onboarded beneficiaries via a Directorate of Industries letter) `[VERIFIED]`; platform-administered skill test/interview (UC model) `[VERIFIED]`; skill-cert issuance via DigiLocker varies `[VERIFY at build]` | Zero (govt schemes) + assessment cost |
| **L4 Behaviour** | "Consistent, accountable" | **Order-verified ratings** (already in our core, D6); risk-tiered re-verification cadence (RBI KYC analogy: high 2y / med 8y / low 10y, digital since Jun-2025) `[VERIFIED]`; **no adverse action on ratings alone** (Karnataka Gig Act) `[VERIFIED]`; portable worker ID (KA welfare board unique ID + e-Shram UAN) `[VERIFIED]` | Ops |

## 3. Both-sides trust (protect the provider too)
- Platforms that verify only workers create asymmetrical surveillance (APC case study: OTP + photos + location pings felt dehumanising; help centres unresponsive) `[VERIFIED — APC report]`. Design guardrail: **verify at onboarding + risk-triggered spot checks, not every job**; visible two-way accountability (consumer phone-verified + order history) protects women providers and reduces abuse `[VERIFIED — gig research: women's evening-job/safety constraints]`.

## 4. Privacy & legal guardrails (non-negotiable)
- **Never store Aadhaar numbers/biometrics** — verify via UIDAI/KYC response only; DPDP consent for each claim; documents pulled via DigiLocker stay issuer-signed references, not copies in our vault (unless user explicitly stores in their own vault).
- Karnataka Gig Workers Act 2025 obligations if we match individuals (register, portable IDs, 1–5% welfare fee, weekly payouts, IDRC) `[VERIFIED]` → person-pack pilot needs the legal gate (module-map §2.7).
- Verification must not be grounds for algorithmic black-box punishment; give workers visibility into why a flag fired (KA Act transparency) `[VERIFIED]`.

## 5. What this means for the product
1. **ProBadge chips L1→L4** on the I-rung profile: MVP person pack = **L1 (eKYC/DigiLocker) + L4 (order-verified ratings) + references**; add **L2 police verification for home-entry categories** (beautician, plumbing, AC/repair at home) and **L3 skill certs for regulated trades** (electrical) when the category demands.
2. **Cost model:** L1 ≈ free (¢15/check); L2 ₹50–200 govt or vendor at scale — **price into the person pack or subsidise at launch** (never a Justdial-style upfront lead cost; outcome-based principle stands).
3. **Verification travels (growth ladder):** the same verified claims follow the profile as it climbs I → XS (shop) → S; an individual who later opens a shop keeps L1–L4 history and adds compliance licences for the BusinessBadge — trust compounds in place `[stage-model §0]`.
4. **Consumer-side mirror:** consumers are phone-verified + have order history (light), so providers (esp. women) can judge who they're entering a home for — two-way trust is a differentiator vs UC's one-way model.

## 6. Open questions (adds to scope-brief)
- OQ-V1: Which person-pack categories carry L2 (police verification) by default at launch vs optional? (founder + W38 provider/consumer interviews; safety-sensitive categories first)
- OQ-V2: Who pays L2/L3 costs — provider, consumer opt-in premium, or launch subsidy? Validate WTP in interviews.
- OQ-V3: Re-verification cadence (annual ID re-confirm + rating floors) without violating the "no adverse action on ratings alone" rule — policy design `[VERIFY with lawyer]`.

## 7. Key sources (accessed 2026-09)
ShuftiPro digital-identity landscape (Aadhaar/DigiLocker/CKYCRR, RBI 2025 Master Direction); UIDAI auth stats (via ShuftiPro); World Bank eKYC cost finding; CitizenNest police/character-verification guide (state portals, fees, domestic-worker rules); Urban Company statements + YourStory/Arthnova case studies (vetting pipeline, AuthBridge, Azure face-match, NSDC/MSDE, ₹50k/partner, SOS/insurance, 25–30% acceptance); APC "Designing Domestic Work Platforms" case study (surveillance critique); HelpRush /trust + /government (KYC+SVE, PM Vishwakarma); prior gig research (individual-providers-gig.md; Karnataka Gig Act; earnings/safety).
