# Screen Inventory — Two-Surface MVP (idea-to-spec Phase 4, v0.3)
**Version:** 0.3 · **Date:** 2026-09-08 · Client: PWA (mobile-first). Every screen: route, data deps (API on mount), states (loading/empty/error/edge), actions. A11y baseline: heading hierarchy, focus management on route change, ARIA landmarks, min 48px touch targets, Hindi uses same component tree (ContentBlock-driven). Part A = business owner surface (S1–S15 + S14a/b managers); Part B = customer surface (S16–S24).

## S1 · Onboarding / language
- Route `/welcome` · Deps: none · Toggle EN/HI → `GET /content/keys?prefix=ui` preview.
- States: first-run vs returning (redirect `/home`).
- Actions: choose locale → request OTP.
- Edge: no network → cached copy + retry.

## S2 · OTP login
- Route `/login` · Deps: `POST /auth/otp/request`, `/auth/otp/verify`.
- States: requestId waiting, resend cooldown (30s), wrong-code error (401), rate-limit (429).
- Actions: enter phone (E.164, India +91 default), enter 6-digit code.
- A11y: code fields auto-advance, errors linked via aria-describedby.

## S3 · Home / stage dashboard
- Route `/home` · Deps: `GET /profiles/{id}` (+journeys).
- States: empty (no profile → "Start your business setup" CTA); active (progress ring, formalizationState chip, next task card, deadline countdown, quiz banner if no recommendation).
- Actions: continue journey, open deadlines, add/verify milestone ("I got my COI/GSTIN/URN").
- Edge: milestone form validates identifier format loosely (COI CIN pattern, GSTIN 15-char, URN 16-digit) — hint, not enforcement.

## S4 · Entity quiz (multi-step)
- Route `/quiz` · Deps: `POST …/quiz`, `answers`, `recommendation`.
- States: step progress (n/total), per-question option select with hints; back/edit allowed; completion → recommendation screen; 409 if completed.
- Actions: answer → next; final → recommendation fetch.
- Edge: Hindi persona — plain-language micro-copy per option; "why this question?" tooltip.

## S5 · Recommendation card
- Route `/quiz/recommendation` · Deps: `GET …/recommendation`.
- States: loading; empty (incomplete → prompt).
- Content: recommended entityType + 3–5 rationale chips (liability, funding, control, compliance load incl. **ongoing annual cost warning** e.g., Pvt Ltd ROC/audit at zero revenue), alternatives w/ trade-offs, disclaimer + "Consult a professional" link.
- Actions: Accept (PATCH profile.entityType → unlocks journeys) | Compare alternatives.

## S6 · Journey list
- Route `/journeys` · Deps: `GET …/journeys`.
- States: empty ("No journeys yet — complete the entity quiz"); grouped by stage: Formalize (incorporation/GST/Udyam), Post-registration (bank, INC-20A), Licences (vertical pack bundle — grocery/appliance/electrical/mechanic configs).
- Actions: start journey (`POST …/start`), resume active.

## S7 · Journey detail (task timeline)
- Route `/journeys/:id` · Deps: `GET /journeys/{id}`.
- States: vertical timeline of TaskInstances with lock/todo/in-progress/done states; current task highlighted; prerequisite lock explanation ("Complete DSC step first").
- Actions: open task, mark milestone done.
- Edge: many tasks → collapsed groups w/ counts; offline → cached tasks.

## S8 · Task detail
- Route `/tasks/:id` · Deps: `GET /journeys/{id}` (parent), `GET /tasks/{id}/documents`.
- Content blocks: what/why (EN/HI), **doc readiness checklist**, current govt fee + professional-fee hint + `as of` + disclaimer, official portal deep link (open-in-browser), est. duration, look-alike-portal warning banner for Udyam/GST.
- Actions: upload docs (camera/gallery; capture helper for Aadhaar/PAN photos), mark "Completed on portal" (doneGovt), add note.
- States/edges: missing mandatory docs → 422 prompt listing missing; wrong file type/size → inline error; retry upload.

## S9 · Licence pack view
- Route `/licences` · Deps: journeys filtered licenceBundle.
- Content: pack summary (vertical × state), each licence: what/why/renewal period/est fee/portal link; FSSAI tier hint by turnover band.
- Actions: convert licence → task in journey; expiry reminders on docs with expiresAt.

## S10 · Documents vault
- Route `/documents` · Deps: `GET …/documents` per task + local index.
- States: empty (guidance: what to keep: Aadhaar, PAN, address proof, photos, NOC); expiry warnings (e.g., DSC validity).
- Actions: view list, delete (confirm), re-upload.

## S11 · Deadlines calendar
- Route `/deadlines` · Deps: `GET …/deadlines?status=pending`.
- Content: upcoming (INC-20A countdown, auditor, DIR-3 KYC Sep-30, GST cadence monthly/quarterly, licence renewals); missed flagged red.
- Actions: mark done, add custom reminder (device), seed refresh.
- Edge: empty → "Set your registration date to compute INC-20A" helper.

## S12 · Settings / profile
- Route `/settings` · Deps: PATCH profile.
- Fields: business name, state, vertical, size fields, locale, notifications.
- Actions: language toggle (S1 parity), logout, delete account.

## S13 · Guide pages (SEO content)
- Route `/guides/:slug` · Deps: `GET /guides/{slug}?locale=`.
- Public, no auth; mirrors journey content; CTA → login → resume journey.
- States: 404 page for unknown slug; i18n pending marker (content falls back to EN).

## S14 · Business order inbox (owner surface addition)
- Route `/business/orders` · Deps: `GET /business/orders?status=` (polling + push-later).
- States: empty ("No orders yet — your storefront is live once you're verified"); tabs by status (new/paid/fulfilling/completed).
- Actions: accept (`POST …/accept`), fulfill, decline (with reason); per order: line items, consumer note, delivery type, payment badge (paid/UPI/POD).
- Edge: badge suspended → banner "Storefront hidden until compliance restored" + link to fix deadlines.

## S14a · Availability manager (v0.3, business)
- Route `/business/availability` · Deps: GET/PUT `/business/me/availability`.
- Content: weekly template editor — per day: work hours, slot length, breaks; service listings without availability flagged "not bookable".
- States: empty (defaults Mon–Sat 10:00–19:00); unsaved changes warning.
- Actions: save template (PUT) → slots auto-derive; toggle per-day off.
- A11y: time inputs with clear labels (EN/HI); no color-only state.

## S14b · Deals manager (v0.3, business)
- Route `/business/deals` · Deps: deals CRUD (`POST/GET /business/me/deals`, `PATCH/DELETE /deals/{id}`).
- Content: list of deals (status chips: active/scheduled/expired/paused), create form: type (₹ off / % off), scope (whole shop / specific listing), value, start/end, cap.
- States: empty ("Publish your first offer — deals appear in Nearby Deals"); listing picker limited to merchant's own active listings.
- Actions: create, pause/resume, delete (only future deals — 409 if started).
- Edge: attempted edit after validFrom → 409 inline; consumer-protection hint: show as offer price, no MRP-crossed claims.

## S15 · Role gate / switch (v0.2)
- Route `/role` · Deps: account roles from token.
- Content: two tiles — "I run a business" (business surface) / "I want to buy" (consumer surface); switch persists per session; same phone can hold both.
- States: first-login (choose) vs returning (last role default + switch affordance in profile).

---
# Part B — Customer surface (v0.3, screens S16–S24)
Customer UX persona: Priya (Bengaluru pilot, grocery/appliance/electrical/mechanic, UPI-native). All consumer screens require merchant **verified** filter default on.

## S16 · Consumer home / discovery
- Route `/c` · Deps: `GET /discover?lat=&lng=&vertical=&verified=true&q=`, deals rail `GET /discover/deals`.
- Content: location (pincode/geo consent), vertical chips (**grocery · appliances · electrical · auto care**), verified badge legend ("Registered & compliant"), **"Nearby Deals" rail** (top 5 active deals w/ merchant + offer + validity), search, merchant cards (name, distance, badge, **deals count**, category tags).
- Actions: tap deal → merchant storefront (deal pre-attached) or S24; vertical chip filters list.
- States: empty (no verified merchants nearby → explainer + CTA "Are you a shop owner? Get verified" — the two-sided loop); loading skeleton; offline → cached last results.
- A11y: map/list toggle later; card tap targets ≥48px.

## S17 · Merchant storefront (customer view)
- Route `/c/merchants/:id` · Deps: `GET /merchants/{id}/storefront`.
- Content: header (name, vertical, verified badge + "licences up to date · GST registered" summary, **active deals chips**), licence/trust panel (list w/ validity), listings grid (**goods & services**: services show "Book" affordance + duration + price-basis).
- Actions: browse, tap listing → S18; **redeem deal** (auto-attached offer chip); contact merchant (call/WhatsApp link, phone shown only when consented by merchant).
- States: unverified merchant → 404/undiscoverable; listings empty → "Shop opens soon" (merchant may be onboarded but not cataloged).

## S18 · Listing detail (goods & service)
- Route `/c/listings/:id` · Deps: listing GET (via storefront).
- **Goods:** photo, name, unit, price (GST-inclusive flag), stock status, description (EN/HI); qty stepper → add to cart.
- **Service:** photo, name, duration, price or "estimate at visit", serves-at (shop / my location), description; **Book** → S19 checkout with slot picker (`GET /merchants/{id}/slots?date=` for next 7 days), notes field (e.g., complaint description).
- Deal chip (if listing-scoped deal active) shown with validity → pre-attached at checkout.
- States: no availability configured → "Bookings not open yet — call to arrange"; slot unavailable → greyed.

## S19 · Cart & checkout (goods) / booking request (service)
- Route `/c/checkout` · Deps: POST /orders on place.
- **Goods:** items + server-priced totals, delivery type (pickup / merchant delivery / POD toggle), saved address or new, **apply deal** (choose from merchant's valid deals), DPDP consent on first order.
- **Service:** slot confirm (date/time chosen), serves-at + address (if at-home), notes, deal auto-applied; payment method fixed **pay-at-shop** (no UPI intent).
- States: price-changed → totals refresh; stock-out flagged; deal expired between cart & place → 422 inline with reason; slot taken → 409 → refetch slots.
- Actions: Place order → S20 (goods w/ UPI/POD) or straight to S21 tracking (service booking).

## S20 · UPI payment
- Route `/c/pay/:orderId` · Deps: `POST …/payment-intent` → redirect/deep link to UPI app.
- States: initiated → redirected; return handling shows `payment-status` (poll) with clear "we're confirming" screen (never trust client); success → S21; failed/expired → retry or switch to POD (order back to placed).
- Edge: 15-min expiry countdown; user abandons UPI app → resume state.

## S21 · Order tracking
- Route `/c/orders/:id` · Deps: GET order + timeline (poll).
- Content: status stepper (goods: placed→paid→accepted→fulfilled→completed; **service: booked→confirmed→service done→completed**), ETA note (merchant-provided), cancel button while allowed, call merchant.
- Actions: confirm completion (goods delivery; **service done**) → then review prompt (S22).

## S22 · Review
- Route `/c/orders/:id/review` · Deps: POST review.
- Content: star rating + optional comment (order-verified; one per order).
- States: not completed → 409 prompt; already reviewed → view own review.

## S23 · Consumer profile / addresses
- Route `/c/settings` · Deps: addresses CRUD, consent, role switch, erasure (DELETE /me).
- Content: saved addresses, language toggle, "I also run a business → switch role", data & privacy (consent record, erasure request).

## S24 · Nearby Deals feed (v0.3)
- Route `/c/deals` · Deps: `GET /discover/deals?lat=&lng=&vertical=` (pagination).
- Content: list of active verified-merchant deals (offer headline, merchant, listing-scope tag, distance, valid-until); filter by vertical; sort by distance/newest.
- States: empty ("No live offers nearby right now — new deals appear as shops get verified").
- Actions: tap deal → merchant storefront with deal pre-attached → S18/S19; save-for-later (local).

## Cross-cutting states (v0.2 additions)
- **Role-based:** routes under `/business/*` and `/c/*` enforce JWT role; unauthenticated → S1/S2 login then S15 role gate.
- **Trust UI:** verified badge is a single shared component (icon+text, no color-only); hovering/tapping shows licence summary + `verifiedAt`; suspension instantly hides badges (LM2).
- **Bilingual:** consumer high-traffic screens (S16, S17, S19, S20) HI-first priority per scope-brief assumptions.
- **Offline (v0.1):** PWA cache for S1/S3/S6/S7/S8 read paths; writes queue with sync on reconnect (docs upload deferred); consumer discovery (S16) caches last results.
- **A11y (v0.1):** EN/HI font stack (Noto Sans / Noto Sans Devanagari), no color-only status (icon+text), form errors with aria-live; verified badge text+icon (never color-only).
