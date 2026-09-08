# Domain Model — Two-Surface MVP (idea-to-spec Phase 2, v0.3 bookings + deals)
**Version:** 0.3 · **Date:** 2026-09-08 · v0.2 added consumer/marketplace; v0.3 adds **service bookings** (listing kind, availability/slots) and **merchant deals**.

## 1. Entities & relationships (textual ERD)
```
Founder 1──1 BusinessProfile 1──n JourneyInstance 1──n TaskInstance
BusinessProfile n──1 Vertical (pack)        n──1 EntityType
TaskInstance n──1 TaskTemplate              n──1 LicenceRequirement*
JourneyInstance 1──n TaskInstance
TaskInstance 1──n StoredDocument
BusinessProfile 1──n DeadlineEvent
EntityQuizRun 1──1 BusinessProfile(optional)  n──1 EntityType(recommended)
ContentBlock (i18n) ← referenced by TaskTemplate/QuizQuestion/Option/GuidePage

— v0.2 marketplace side (shared core) —
Consumer 1──n SavedAddress           1──n Order
Order n──1 BusinessProfile(merchant) 1──n OrderItem 1──n PaymentIntent(0..1 active) 1──n Review(0..1 per order)
BusinessProfile(merchant) 1──n Listing 1──n OrderItem(snapshot)
Listing n──1 Vertical(pack)          Listing.kind ∈ goods|service
— v0.3 additions —
MerchantAvailability 1──n BusinessProfile    (weekly schedule → SlotView, derived)
Listing(service) 1──n SlotBooking(within Order)    Deal n──1 BusinessProfile(+optional listing-scope) 1──n Order.redeemedDealId(0..1)
VerificationBadge (derived view, no table) ← BusinessProfile.complianceState
```
*LicenceRequirement folded into TaskTemplate via `licenceBundleId` tag — see §4.

## 2. Entity data dictionary (core rows)
### Founder
| Field | Type | Req | Validation |
|---|---|---|---|
| id | uuid | Y | PK |
| phone | string E.164 | Y | unique; OTP auth |
| locale | enum en\|hi | Y | default en |
| createdAt | ts | Y | |
### BusinessProfile (the "one profile, adaptive surface" spine)
| Field | Type | Req | Validation / notes |
|---|---|---|---|
| id | uuid | Y | PK |
| founderId | fk | Y | unique per founder |
| businessName | string | N | ≤80 chars |
| state | enum[5] | Y* | MH,KA,DL,UP?,TN,GJ — resolved set; *required before licence tasks |
| cityDistrict | string | N | free text for licence hints |
| vertical | enum retail\|f&b | N | drives licence bundle |
| entityType | enum | N | set at entity selection |
| sizeClass | enum micro\|small | Y | from MSME inputs (employees/turnover bands) |
| employees | int | N | triggers EPFO/ESIC hints ≥10/20 |
| projectedTurnover | enum bands | N | drives GST-required flag (goods >₹40L, services >₹20L, special states lower) |
| sellsGoodsOnly | bool | N | GST threshold branch |
| interstate | bool | N | GST compulsory flag |
| ecommerceSeller | bool | N | GST compulsory day-1 flag |
| formalizationState | enum | Y | state machine §3 |
| progressPct | computed | N | completed tasks / total active tasks |
### EntityType (config, versioned)
Attributes: code(prop|opc|llp|pvt|partnership), liability(LIMITED|UNLIMITED), minPeople, fundingFit(bool), complianceLevel(1–5), taxNote, ongoingCostNote, licenceNotes. Content via ContentBlock (en/hi).
### JourneyTemplate / TaskTemplate (config — the content engine)
| TaskTemplate | fields: id, journeyType, order, prerequisiteIds[], kind(entityStep|gst|udyam|licence|postCoi|deadlineSeed), titleKey, bodyKey, docRequirementIds[], govtPortalUrl, govtFeeInr, professionalFeeHintInr, estDurationDays, licenceBundleId?, verticalTags[], stateTags[] |
### JourneyInstance
id, profileId, journeyType, status (per state machine), startedAt, completedAt, currentTaskId.
### TaskInstance
id, journeyId, templateId, status: locked→todo→inProgress→awaitingDocs→doneGovt→verified(done), notes, completedAt, markedBy(manual).
### StoredDocument
id, taskId, profileId, name, mime, size, storageKey(local), category(identity|address|photo|officeProof|licenceDoc), expiresAt?, uploadStatus.
### DeadlineEvent
id, profileId, kind(INC20A|AGM|auditor|dir3kyc|gstReturn|renewal|pfesi), dueDate, recurrence?, status(pending|done|missed), sourceTaskId?.
### EntityQuizRun
id, profileId, answers (map qid→optId), recommendedEntityType, scoreRationale (list of flagged trade-offs), completedAt. Rules: config-driven decision table (liability need, funding plan, solo/cofounder, revenue path, compliance appetite).
### ContentBlock (i18n)
id, key, locale(en|hi), text, updatedAt, status(translated|pending). Validation: validate-i18n script asserts en+hi parity for keys used by active content (reuses b2b-price-intel pattern).

## 3. State machines
**BusinessProfile.formalizationState:** `ideation → quizDone → entitySelected → docsReady → filed → registered → postCoiDone → operational`
- filed = user marked SPICe+/GST/Udyam application submitted on portal
- registered = COI / GSTIN / URN / licence obtained (milestone events SM3)
- operational = INC-20A + bank account + first licence in hand
- All transitions manual (user "I did it on the portal"), except quizDone (system on quiz completion).

**JourneyInstance.status:** `notStarted → active → completed`; abandon allowed from active (kept, resumable).

**TaskInstance.status:** `locked (prerequisites unmet) → todo → inProgress → awaitDocs (needs upload/readiness) → doneGovt (user confirms portal step done) → verified` (doneGovt auto→verified after required docs attached; else stays awaitDocs).

**DeadlineEvent.status:** pending → done | missed (auto-flag when dueDate < today && not done).

## 4. Licence bundling rule
Vertical × state × size → licenceBundle → ordered TaskTemplates. Example (F&B, KA, Micro): [FSSAI Basic|State, S&E, trade licence, GST-if-applicable, Udyam, fire NOC-hint]. Represented as config rows `LicenceBundle {bundleId, vertical, state, tasks[]}` — pure data, no code change per vertical/state (module-map §3 principle).

## 5. Design decisions
- Content = config + i18n ContentBlock → validates bilingual parity, trivially versioned, and lets journeys ship without a CMS (solo-build constraint).
- No server-side portal integrations: statuses are user-confirmed (keeps liability + scope in check; scope-brief OUT list).
- All monetary fields are display-only estimates with `[as of]` + disclaimer; correctness maintained by content versioning + Phase-4 re-verification.

## 6. v0.2 Marketplace entity dictionary (new core rows)
### Consumer
| Field | Type | Req | Validation |
|---|---|---|---|
| id | uuid | Y | PK |
| phone | E.164 | Y | unique; same account base as Founder (both roles allowed) |
| locale | en\|hi | Y | |
| defaultAddressId | fk | N | → SavedAddress |
### SavedAddress
id, consumerId(fk), label(home/work), line1/2, city, state(∈5), pincode(6-digit), geo?{lat,lng optional}, isDefault. Req: line1+pincode+state.
### Listing (merchant catalog item)
| Field | Type | Req | Notes |
|---|---|---|---|
| id | uuid | Y | |
| merchantId | fk BusinessProfile | Y | |
| vertical | retail\|f&b | Y | pack-consistent |
| nameKey / name | string | Y | ≤60 chars; bilingual name optional |
| descriptionKey | string | N | i18n block |
| priceInr | decimal(2) | Y | >0 |
| gstInclusive | bool | Y | display flag (fee math is merchant's) |
| unit | string | N | kg/pc/meal… |
| stockStatus | inStock\|low\|out | Y | manual |
| imageKey | string | N | upload ref |
| active | bool | Y | soft-hide |
| categoryTag | string | N | vertical taxonomy hint |
Uniqueness: (merchantId, vertical, name) active-listing.
### Order
| Field | Type | Req | Notes |
|---|---|---|---|
| id | uuid | Y | |
| consumerId | fk | Y | |
| merchantId | fk BusinessProfile | Y | snapshot merchantName+verifiedAt? (keeps history) |
| items[] | OrderItem[] | Y | snapshot unitPrice, qty, listingName |
| amounts | {subtotal, discount?, total} | Y | decimal(2) |
| deliveryType | pickup\|merchantDelivery\|pod | Y | pod = pay-on-delivery (no UPI intent) |
| status | enum | Y | state machine §7 |
| timeline[] | {event, at, byRole} | Y | audit trail shared both sides |
| created/updatedAt | ts | Y | |
### OrderItem: orderId, listingId (nullable for deleted), listingName snapshot, unitPriceInr snapshot, qty, lineTotal (computed, GST-inclusive as listed).
### PaymentIntent
| Field | Type | Req | Notes |
|---|---|---|---|
| id | uuid | Y | |
| orderId | fk | Y | one active per order |
| provider | paId | Y | aggregator partner |
| amountInr | decimal(2) | Y | |
| status | initiated→redirected→succeeded→failed→expired | Y | §7 |
| upiDeepLink / redirectUrl | string | N | PA-provided |
| providerRef | string | N | set on webhook |
| expiresAt | ts | Y | ~15 min |
| webhookVerifiedAt | ts | N | signature-verified callback |
### Review: id, orderId (unique), consumerId, merchantId, rating(1–5, req), comment(≤500, opt), status(pending→published|hidden), createdAt. Only for completed orders; one per order.

## 7. v0.2 State machines
**Order.status:** `cart(optional client-side) → placed → paymentInitiated → paid → accepted → fulfilled → completed`
- Branch: `placed → cancelled` (consumer, before accept); `paid → declined → refunded (refund via PA, later)`; `paymentInitiated → paymentFailed → placed (retry)` or `paymentExpired → placed`; `accepted → declined` by merchant → notify + refund-if-paid (later); `fulfilled → completed` on consumer confirm (POD: `placed → accepted → fulfilled(pod) → completed-on-delivery`).
- All transitions append timeline events (byRole: consumer|merchant|system).

**PaymentIntent.status:** initiated → redirected (user sent to UPI) → succeeded | failed | expired (15-min TTL; job). Webhook (signature-verified) is the only transition to succeeded; client redirect-return is cosmetic only.

**VerificationBadge (derived, no table):** `badged = profile.formalizationState ∈ {registered, postCoiDone, operational} ∧ no DeadlineEvent(status=missed) of kind required-for-vertical/state ∧ no expired required licence (via TaskInstance/licence doc expiry) ∧ profile not suspended`. Recompute: on formalizationState change + daily job; expose `verifiedAt`. Suspension: any missed mandatory deadline or expired licence flips badge off (LM2).

## 8. v0.2 design decisions
- **No fund holding**: PaymentIntent only creates the PA redirect; settlement is merchant↔PA. MVP failure handling = order returns to `placed` for retry/POD — no auto-refund flows (scope-brief OUT).
- **History over joins**: Order/OrderItem snapshot names+prices so merchant catalog edits never rewrite order history (audit + reviews integrity).
- **Reviews order-verified only** (completion-gated) — anti-fake review baseline; moderation + merchant dispute flow deferred (P2).
- DPDP: consumer PII = phone + addresses only; consent captured at first order; deletion endpoint required (settings).

## 9. v0.3 Deltas — service bookings & deals (modifications only; §6/§7 remain authoritative for base fields)
### 9.1 Listing gains `kind`
`kind ∈ goods|service` (default goods). **Service listings** add: `priceBasis ∈ fixed|estimateAtVisit`, `durationMin` (slot length, default 30), `servesAt ∈ shop|consumerLocation|both` (mechanic: atShop; appliance/electrical install: consumerLocation), `active` semantics unchanged. Goods listings unchanged.
### 9.2 New: MerchantAvailability (weekly template) + SlotView (derived)
- **MerchantAvailability**: merchantId, dayOfWeek(0–6), workStart, workEnd, slotDurationMin, breaks[] (optional), bufferMin. One row set per merchant (config-driven, no calendar UI complexity in MVP).
- **SlotView (derived, not stored):** for a given date, slots = [workStart, workEnd) split by slotDurationMin **minus** slots already held by non-cancelled service orders. Exposed read-only via API; race resolved at booking (optimistic concurrency: one active booking request per slot → 409 on conflict).
### 9.3 Order covers service bookings
Order gains: `kind ∈ goods|service` (from primary item), `slotStart` (service, nullable), `visitType ∈ pickup|merchantDelivery|consumerLocation|atShop` (goods: pickup/merchantDelivery; service: atShop/consumerLocation), `redeemedDealId` (nullable), `dealAmountInr` (computed discount applied to total; stored for audit). Goods order = items[] as before; service order = single service item + slot.
### 9.4 New: Deal
id, merchantId (fk BusinessProfile, must be verified), optional listingId (scope), kind ∈ flatOff|percentOff, valueInr/valuePct, validFrom, validTo, redemptionCap (optional), redeemedCount (incremented atomically at order placement), active (soft on/off), createdAt. **Server-side validation at checkout:** merchant verified ∧ within [validFrom, validTo] ∧ listing-scope matches ∧ cap not exhausted ∧ one deal per order → else 422 with reason. Deal never stacks.
### 9.5 State-machine extensions (§7 Order)
- Service-booking branch: `placed(booked) → accepted(confirmed with slot) → fulfilled(service performed) → completed`; cancel allowed until `accepted`; `declined` by merchant returns slot to SlotView (no payment to unwind — pay-at-shop default). Timeline events record slot + deal applied.
- PaymentIntent unchanged (goods only in MVP; service pay-at-shop → no intent).
### 9.6 Design-decision additions
- **Deals are real-time validated, never stored-discount-at-checkout without checks** (B3 deals engine) — anti-abuse baseline + offer-price framing `[VERIFY display norms]`.
- **Slots are derived + race-safe** (optimistic) rather than a booking calendar table — keeps MVP storage simple; availability is merchant-declared weekly config.
- Service **no-show handling**: merchant confirm step + reminders; no-show history per consumer kept (fair-use later); no prepay in MVP.
