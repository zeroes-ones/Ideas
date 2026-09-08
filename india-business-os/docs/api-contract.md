# API Contract — Two-Surface MVP (idea-to-spec Phase 3, v0.3)
**Version:** 0.3 · **Date:** 2026-09-08 · Base path: `/v1` · Auth: bearer JWT from phone-OTP (dev: mock). All timestamps ISO-8601 UTC. Errors use RFC 7807-style `{code, message, details?}`.

## Conventions
- **Pagination:** `?page=1&limit=20` → `{items, page, limit, total}`. Sorting params documented per endpoint.
- **Idempotency:** POST document uploads and POST orders accept `Idempotency-Key` header; retries safe.
- **AuthN/AuthZ:** all endpoints except `POST /auth/*` require bearer token. JWT carries `sub` (account) and `role: consumer|business`. A phone number can hold both roles; each request is scoped to the presented role + resource ownership (403 otherwise). Business endpoints require `role=business` + ownership of `profileId`; consumer endpoints require `role=consumer`.
- **Error codes:** `400 validation_error`, `401 unauthenticated`, `403 forbidden`, `404 not_found`, `409 conflict` (e.g., quiz already completed), `413 payload_too_large`, `429 rate_limited`, `500 internal`.

## Endpoints

### Auth
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| POST | /auth/otp/request | `{phone}` | `{requestId, ttlSec}` | Rate-limited per phone (429) |
| POST | /auth/otp/verify | `{requestId, code}` | `{token, founder?}` | 401 on bad code; dev mock code `123456` |

### Business profile
| Method | Path | Req | Resp |
|---|---|---|---|
| POST | /profiles | `{businessName?, state?, vertical?, sizeClass?, employees?, projectedTurnover?, sellsGoodsOnly?, interstate?, ecommerceSeller?}` | `Profile` |
| GET | /profiles/{id} | — | `Profile` + `formalizationState`, `progressPct` |
| PATCH | /profiles/{id} | partial fields | `Profile` |

Validation rules: `state ∈ {MH,KA,DL,TN,GJ}` (MVP resolved set — 5 states, all GST normal-category; UP excluded from MVP: separate S&E portal, revisit at state expansion); `sizeClass ∈ {micro,small}`; `projectedTurnover` band drives `gstRequired` computed flag server-side per regulatory rules (goods ₹40L/services ₹20L thresholds; compulsory flags for interstate/ecommerce).

### Entity advisor quiz
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| POST | /profiles/{id}/quiz | `{}` | `{runId, questions:[{qid,titleKey,options:[{oid,labelKey,hintKey?}]}], totalSteps}` | Creates run; 409 if completed run exists |
| POST | /profiles/{id}/quiz/{runId}/answers | `{answers:[{qid,oid}]}` | `{complete, nextQid?}` | Partial saves allowed; idempotent per qid |
| GET | /profiles/{id}/quiz/{runId}/recommendation | — | `{recommendedEntityType, rationale:[{dimension, findingKey, weight}], alternatives:[{entityType, tradeOffKey}], disclaimerKey, consultProfessionalUrl}` | 409 if quiz incomplete |

Decision logic = config decision table (liability need, funding plan, solo/co-founders, revenue path, compliance appetite). On recommendation accept → PATCH profile.entityType + transitions state `quizDone→entitySelected`.

### Journeys & tasks
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| GET | /profiles/{id}/journeys | — | `[{journeyType, titleKey, status, progressPct, nextTaskId}]` | Active set derived from profile (entity type + vertical + state + gst flags) |
| POST | /profiles/{id}/journeys/{journeyType}/start | `{}` | `Journey` | Instantiates template → TaskInstances (locked ordering) |
| GET | /journeys/{journeyId} | — | `Journey` + tasks[] (each: template fields + status + docs[]) | 404 if not owner |
| PATCH | /tasks/{taskId} | `{status?, notes?}` | `Task` | Transitions per state machine; `doneGovt` requires mandatory docs attached else 422 (`awaitDocs`); 409 on illegal transition |
| POST | /tasks/{taskId}/unlock-check | `{}` | `{unlocked, missingPrerequisites:[taskIds]}` | Optional helper |

### Documents
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| POST | /tasks/{taskId}/documents | multipart `{file, category}` | `{docId, uploadStatus}` | max 10 MB; pdf/jpg/png; virus-scan hook (later); idempotency key |
| GET | /tasks/{taskId}/documents | — | `[{docId,name,mime,size,category,expiresAt}]` | Metadata only (client renders local) |
| DELETE | /documents/{docId} | — | 204 | Owner-only |

### Deadlines
| Method | Path | Req | Resp |
|---|---|---|---|
| GET | /profiles/{id}/deadlines | `?status=pending&from=...` | `[{id,kind,dueDate,recurrence?,status,sourceTaskId?}]` |
| POST | /deadlines/{id}/done | `{}` | 204 |
| POST | /profiles/{id}/deadlines/seed | `{}` | `[DeadlineEvent]` | Creates calendar seed from registration milestones (INC-20A +180d, auditor +30d, DIR-3 KYC Sep-30, GST cadence, renewals) |

### Content / i18n
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| GET | /content/keys | `?prefix=journey.gst&locale=hi` | `{keys:[{key,en,hi,status}]}` | Powering EN⇄HI toggle; status `translated\|pending` |
| GET | /guides/{slug} | `?locale=` | `GuidePage {slug,titleKey,blocks[]}` | SEO content pages |
| GET | /meta/fees | — | `{items:[{code,govtFeeInr,asOf,disclaimerKey}]}` | Fee transparency widget + look-alike-portal warning |

## Failure modes covered (idea-to-spec RP-style)
- Task marked done without docs → 422 awaitDocs (explicit remediation).
- Quiz re-run after completion → 409 with pointer to recommendation.
- GST-required computed but profile missing state → 400 (licence tasks need state).
- Document upload wrong type/size → 400/413 with allowed list in error details.
- Missed deadline computed daily by job → status `missed` + reminder push.

---
# Part B — Marketplace endpoints (v0.3 consumer + business-order surface)
Consumer endpoints require `role=consumer`; business-order endpoints require `role=business` + merchant ownership.

## Consumer — discovery & storefront
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| GET | /discover | `?lat=&lng=&vertical=retail\|f&b&q=&verified=true&page=` | `{items:[{merchantId,name,badge:{verified,verifiedAt},distanceM,vertical,tags}],page…}` | verified-only default true; distance computed client-side from geo or server via pin-code centroid `[ESTIMATED]`; no PII exposure |
| GET | /merchants/{profileId}/storefront | — | `{merchantId,name,verified:{…},licenceSummary:[{licence,validTill,status}],contact:{phoneShown?},listings:[…]}` | Only served when verified (else 404 — unverifiable merchants are undiscoverable) |
| GET | /merchants/{profileId}/listings | `?category=&page=` | `Listing[]` | active only |

## Consumer — orders & payments
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| POST | /orders | `{merchantId,items:[{listingId,qty}],deliveryType,pod:bool,addressId}` | `Order` | Idempotency-key; validates merchant verified + listings active + stock; 422 on mismatch; computes totals server-side |
| GET | /orders/{id} | — | `Order` + timeline | owner-only |
| POST | /orders/{id}/cancel | `{}` | `Order` | only before `accepted`; 409 otherwise |
| POST | /orders/{id}/payment-intent | `{}` | `{intentId,redirectUrl\|upiDeepLink,amountInr,expiresAt}` | creates PaymentIntent (409 if active one exists); POD orders skip |
| GET | /orders/{id}/payment-status | — | `{status}` | client polling fallback |
| POST | /orders/{id}/confirm-delivery | `{}` | `Order` | consumer completes order (esp. POD) |
| POST | /orders/{id}/review | `{rating,comment?}` | `Review` | only when `completed`; one per order (409); merchant never sees reviewer identity in MVP |

## Payments (PA partner webhook — signature-verified)
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| POST | /payments/webhook | PA payload | 200 `{received}` | Public endpoint; verify PA signature (X-…-Signature + shared secret); **only transition to `succeeded`**; idempotent by providerRef; never trust client redirect |

## Business — catalog & order inbox (owner surface additions)
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| GET | /business/me | — | `{profile, verification:{badged,reason?,since}}` | badge health (B1) |
| POST | /business/me/listings | Listing fields | `Listing` | merchant-owner; vertical+state validated |
| PATCH | /listings/{id} | price/stock/active/name… | `Listing` | owner-only |
| DELETE | /listings/{id} | — | 204 | soft-delete |
| GET | /business/orders | `?status=placed\|paid\|accepted…` | `Order[]` | merchant inbox (B0) |
| POST | /business/orders/{id}/accept | `{}` | `Order` | only when `paid` or `placed`(pod) |
| POST | /business/orders/{id}/fulfill | `{}` | `Order` | sets fulfilled; consumer confirm completes |
| POST | /business/orders/{id}/decline | `{reasonKey?}` | `Order` | before fulfillment; paid → auto-refund later (P2) |

## Consumer — addresses & consent (DPDP)
| Method | Path | Req | Resp |
|---|---|---|---|
| POST | /me/addresses · GET/PATCH/DELETE /me/addresses/{id} | address fields | SavedAddress / 204 |
| POST | /me/consent | `{dpdpConsent:true, purposeIds[]}` | `{acceptedAt}` |
| DELETE | /me (right-to-erasure) | `{}` | 204 (removes consumer PII; keeps anonymized order history for merchant records where legally required) |

## v0.2 failure modes added
- Order on unverified merchant → 403/404 (undiscoverable; direct-ID access denied).
- PaymentIntent expiry (15-min TTL job) → order returns to `placed`; retry or POD.
- Webhook replay/forgery → signature check 401; duplicate providerRef → idempotent 200.
- Order cancel after accept → 409 with instruction (decline flow).
- Listing price change between cart & place → server recomputes totals at POST /orders from current listings (snapshot); client cart is advisory.
- Review on non-completed order → 409; second review → 409.

---
# Part C — v0.3 service bookings & deals endpoints

## Business — availability & slots
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| PUT | /business/me/availability | `{days:[{dayOfWeek,workStart,workEnd,slotDurationMin,breaks?}]}` | `Availability` | replaces weekly template; service listings must have availability to be bookable (400 otherwise) |
| GET | /business/me/availability | — | `Availability` | |
| GET | /merchants/{id}/slots | `?date=YYYY-MM-DD` | `{date,slots:[{start,end,available}]}` | consumer-facing read; derived SlotView; only for verified merchants |

## Business — deals (merchant CRUD, verified merchants only)
| Method | Path | Req | Resp |
|---|---|---|---|
| POST | /business/me/deals | `{listingId?,kind:flatOff\|percentOff,value,validFrom,validTo,redemptionCap?}` | `Deal` (validations: merchant verified, validTo>validFrom, value>0, listingId belongs to merchant) |
| GET | /business/me/deals | `?active=` | `Deal[]` |
| PATCH | /deals/{id} | partial (value/period/cap/active) | `Deal` |
| DELETE | /deals/{id} | — | 204 |

## Consumer — slots, deals & booking orders
| Method | Path | Req | Resp | Notes |
|---|---|---|---|---|
| GET | /discover/deals | `?lat=&lng=&vertical=&page=` | `{items:[{dealId,merchantId,name,kind,value,validTo,listingId?,distanceM}]}` | nearby-deals feed; verified merchants with active deals only |
| POST | /orders | goods: `{merchantId,items[],deliveryType,addressId?,dealId?}` · service: `{merchantId,listingId(service),slotStart,servesAt,notes?,dealId?}` | `Order` | unified; server validates deal (§domain 9.4) and slot availability (optimistic, 409 on conflict); computes totals incl. dealAmountInr |
| GET | /merchants/{id}/deals | — | `Deal[]` active | shown on storefront |
| POST | /orders/{id}/cancel | `{}` | `Order` | goods: until accepted; service: until accepted (slot released) |

Failure modes (v0.3): deal invalid/expired/scope-mismatch/cap-exhausted/stacking → 422 w/ reasonKey; slot conflict → 409 `slot_taken` (client re-fetches slots); service listing without availability → 400; deal PATCH past validFrom not allowed (409, integrity).
