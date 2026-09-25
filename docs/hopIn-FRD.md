# hopIn — Functional Requirements Document (FRD)
**Version 1.0 · Draft for review**

---

## 1. What this document is

You gave me two prototypes that turned out to be two different products under the same name:

- **"HOPPIN'"** — a sports-court booking platform (badminton, cricket, football, tennis) with a consumer app, a venue-owner/partner app, and an admin console.
- **"hopIn"** — a restaurant/pub/gaming-venue discovery app for Bengaluru & Chennai with an AI chat assistant.

You asked me to merge them. Below is that merged product, written up as a real FRD: one venue-booking platform that covers **restaurants, pubs, gaming venues, and sports courts**, discoverable and bookable by a consumer, manageable by a venue owner, and overseen by an admin — with the AI chat assistant as the discovery layer on top of all of it.

This is a working draft — Section 12 lists the calls I made where the two prototypes disagreed, so you can correct anything before we build.

---

## 2. Product vision

**hopIn is a single app to discover and book any "place to go" in a city** — whether that's dinner, drinks, an arcade, or a badminton court — with an AI assistant that can recommend and book on your behalf, not just show you a list.

One brand, one consumer app, one booking flow, four venue types.

---

## 3. Who uses it (3 apps, 1 platform)

| App | User | Core job |
|---|---|---|
| **Consumer app** | Diner / player / gamer | Discover venues, chat with the AI assistant, book a table/slot/court, pay, manage bookings |
| **Partner app** | Venue owner/manager | List a venue, manage slots/tables, accept bookings, track revenue & reviews |
| **Admin console** | hopIn ops team | Approve venues, manage users, monitor platform revenue & health |

---

## 4. Venue model (the merge, concretely)

Everything is a **Venue** with a **category**, and each category just changes what "booking" means:

| Category | Example (from your mockups) | What gets booked |
|---|---|---|
| Restaurant | Dakshin Delight, Chennai Spice, North Star | A table, for a party size & time |
| Pub / Bar | Pub Royale | A table, for a party size & time |
| Gaming venue | Game On!, Pixel Play | A console/station or time slot |
| Sports court | SportZone Badminton Academy | A court, for a sport & time slot |

All four share one data model (venue profile, photos, location, price tier, rating) and one booking engine (slot → summary → payment → confirmation). Category only determines the labels and the slot picker shown to the user.

**Cities at launch:** Bengaluru & Chennai (per the hopIn mockups; the HOPPIN' mockup only listed Bengaluru — Chennai is added platform-wide).

---

## 5. Consumer app — functional requirements

### 5.1 Onboarding & auth
- Splash screen → onboarding carousel (what hopIn does)
- Phone number entry → OTP verification (real SMS OTP, not mocked)
- City selection (Bengaluru / Chennai), changeable later from home

### 5.2 Discover / Home
- Hero search bar: search venues, cuisines, sports, or areas
- City filter ("All Cities" / Bengaluru / Chennai)
- Category tabs: **Discover · Restaurants · Gaming · Sports · Chat**
- "Popular near you" venue cards: photo, category badge, rating + review count, name, area, price tier (₹/₹₹/₹₹₹), cuisine/sport tag

### 5.3 Search & filters
- Filter by category, cuisine/sport type, price tier, rating, area
- Sort by rating, distance, price

### 5.4 Venue detail page
- Photos, description, category-specific info (cuisine for restaurants, sport + court type for sports venues)
- Rating & reviews
- Availability / slot picker
- "Book now" CTA

### 5.5 Booking flow
1. Select slot (table/time for dining, court/time for sports, station/time for gaming)
2. Booking summary (venue, slot, party size/players, price breakdown)
3. Payment (see 5.7)
4. Confirmation screen with booking ID (e.g. `HOP-4821-BLR`)

### 5.6 AI chat assistant
- Persistent "hopIn Assistant" chat, marked Online
- Natural-language venue discovery: *"Find South Indian restaurants"*, *"Best pubs in Indiranagar"*, *"Gaming places near me"*
- Can complete a booking inside the chat (*"Book a table for tonight"*) — not just recommend
- Suggested quick-reply chips for common intents
- Voice input supported (mic icon in mockup)

### 5.7 Payments
- In-app payment screen: UPI, card, wallet (India-first — Razorpay or similar)
- Real transactions, receipts stored against the booking

### 5.8 My Bookings
- Tabs: Upcoming / Past / Cancelled
- Cancel/reschedule from here (policy TBD — see open questions)

### 5.9 Profile
- Name, email, booking count, amount saved/spent, saved venues

### 5.10 Look & feel
- **Both a light and a dark theme**, toggle in the top nav (sun/moon icon, as in your screenshots)
- Clean, minimal — dark neutral background, single accent color, generous whitespace, rounded cards. No visual clutter.

---

## 6. Partner (venue owner) app — functional requirements

- **Partner registration**: business details, venue category, documents → "Join 500+ venues" onboarding
- **Dashboard**: venue live/offline status, today's snapshot
- **Venue management**: photos, description, pricing, slot/table/court inventory & hours
- **Bookings & slots**: today's bookings, upcoming, incoming requests (accept/decline)
- **Revenue & payouts**: earnings summary, export, payout history
- **Reviews & ratings**: view and respond to reviews

---

## 7. Admin console — functional requirements

- **Admin login** (separate from consumer/partner auth — staff accounts)
- **Dashboard**: platform-wide snapshot (bookings today, revenue, active venues, active users)
- **Venue management**: approve/suspend venues, view all listings (mockup shows 567 active venues)
- **User management**: view/manage registered users (mockup shows 45,678 users), export
- **Analytics**: revenue & commission, category breakdown, booking trends, user growth, peak-hours chart, export

---

## 8. Data model (high level)

```
User (consumer)
 ├─ id, phone, name, email, city, created_at
 └─ Booking[]

Venue
 ├─ id, name, category [restaurant|pub|gaming|sports], city, area
 ├─ price_tier, rating, review_count, photos[], description
 ├─ owner_id → PartnerUser
 └─ SlotInventory[]  (tables / courts / stations, per date+time)

Booking
 ├─ id (e.g. HOP-4821-BLR), user_id, venue_id, slot_id
 ├─ party_size / sport_type / station, datetime, status [upcoming|past|cancelled]
 └─ Payment

Payment
 ├─ booking_id, amount, method, status, transaction_ref

PartnerUser (venue owner/manager)
 ├─ id, venue_id, business_details, payout_account

AdminUser
 ├─ id, role, permissions

Review
 ├─ venue_id, user_id, rating, text, created_at
```

---

## 9. Non-functional requirements

- **Real auth**: phone + OTP for consumers, email/password (or SSO) for partners & admin, proper session/token handling — not mocked
- **Real database**: relational, source of truth for venues/bookings/payments
- **Payments**: PCI-aware — never store raw card data; use a payment gateway's hosted flow/tokenization
- **Responsive**: mobile-first for consumer app (matches your phone-frame mockup); partner & admin can be responsive web
- **Theming**: light + dark mode, system-preference aware, user-toggleable
- **Availability**: booking slot data must be consistent (no double-booking a table/court)
- **Scalable to more cities/categories later** without a data-model rewrite (category is a field, not a separate schema)

---

## 10. Recommended tech stack

You said: **real app (auth, DB, real bookings)** but **keep hosting simple**. Those two constraints together point at one clear stack — frontend and backend fully separated, so the frontend stays "just deploy to Vercel/Netlify" simple, while a managed backend service gives you real auth/DB/payments without you running servers:

| Layer | Recommendation | Why |
|---|---|---|
| Frontend (consumer + partner) | **React + Vite** (or Next.js) | Matches your existing HTML/CSS design direction, deploys as a static/SPA build |
| Hosting | **Vercel or Netlify** | One-command deploy, free tier, custom domain, exactly the "simple" hosting you asked for |
| Backend / DB / Auth | **Supabase** (managed Postgres + Auth + Storage + Edge Functions) | Real database and real phone-OTP auth without you managing a server; still "simple" — no infra to host yourself |
| Payments | **Razorpay** | India-first, UPI + cards + wallets, matches the ₹ pricing in your mockups |
| Admin console | Same React app, separate route/role-gated, or a small separate app if it grows | Keeps one codebase early on |
| AI chat assistant | Claude API (function-calling into your booking backend) | Natural-language search + can actually execute a booking, not just suggest |

This gives you a genuinely production-capable app while every piece of hosting stays "push to deploy."

---

## 11. Suggested phased roadmap

**Phase 1 — MVP**
- Consumer app: auth, discover/search, venue detail, booking flow, payments, my bookings, profile, light/dark theme
- Basic partner app: registration, venue listing, bookings view
- One city fully seeded with real venues (start with Bengaluru, add Chennai)

**Phase 2**
- AI chat assistant with real booking execution
- Partner revenue/payouts, reviews management
- Admin console

**Phase 3**
- Analytics, growth features, more cities, more venue categories

---

## 12. Calls I made merging the two prototypes — please confirm or correct

1. **Branding**: used "hopIn" (the newer, cleaner dark-theme direction) rather than "HOPPIN'" — confirm this is the one you want going forward.
2. **Sports courts folded in as a 4th venue category** alongside restaurants/pubs/gaming, rather than a separate app.
3. **Chennai added platform-wide** (the sports-court mockup only had Bengaluru).
4. **Cancellation/refund policy** — not specified in either mockup, needs a decision before Phase 1 payments go live.
5. **Partner app scope** — assumed it applies to all 4 venue categories, not just sports venues as originally mocked.

---

## 12a. Addendum — fitness categories added (post-v1.0)

Two new venue categories were added alongside the original four, keeping restaurants/pubs/gaming/sports intact:

| Category | Examples | What "booking" means |
|---|---|---|
| `gym` | Gyms, fitness studios (HIIT, CrossFit, yoga) | Day pass or class slot |
| `club` | Running/jogging/cycling clubs — recurring group meetups, not fixed venues | Join a session, up to group capacity |

**Schema change this required:** the original `slots` table assumed one booking per slot
(a table or a court). Clubs and gym classes need *many* people sharing one slot up to a
capacity (e.g. 20 spots on a Saturday run). `slots.is_booked` (boolean) was replaced with
`slots.booked_count` (int) checked against `capacity`, and the booking service now does an
optimistic-lock update so two people joining at the same instant can't both take the last spot.

## 12b. Addendum — social, rewards & positioning (post-v1.0)

**Positioning:** Hoppin is now explicitly aimed at **16-30 year olds**, framed around health/fitness/social activity (gyms, run clubs, sports) with dining/gaming/pubs as the social layer around it — not a generic listings app.

**North star for UX:** as simple and familiar as WhatsApp/Instagram. If a screen needs explaining, it's too complex.

**New requirement — in-app chat (1:1 and group):** the point is that planning never has to leave Hoppin for WhatsApp. One conversation model handles both:
- **1:1 chat** — message another user directly
- **Group chat** — for a club/session (e.g. every run-club session can have its own group thread), or any user-created group
- Real-time-feeling, simple message list — not a feature-heavy chat platform

**New requirement — rewards & gamification:** stars/points for completing bookings, streak bonuses for consistency (e.g. showing up to run club 3 weeks running), and unlockable badges (first booking, category explorer, etc.) — the mechanic that makes checking the app a habit, not just a utility.

**Reconfirmed from earlier:** owner/partner photo management for their venue (already in scope, Section 6), light + dark mode, both mobile and web (already in scope, Section 5.10).

**Schema added:** `supabase/migrations/0003_social_and_rewards.sql` — `conversations`, `conversation_participants`, `messages`, `point_events` (an append-only ledger, not a mutable balance, so history is never lost), `badges`, `user_badges`.

**Where this sits in the roadmap:** this is enough new surface area (a chat system, a rewards engine) that it becomes its own phase rather than folding into Phase 2:
- **Phase 2** stays as scoped: AI chat assistant (booking-focused), partner revenue/payouts/reviews, admin console
- **Phase 3 (new):** in-app social chat (1:1 + group), rewards/points/badges/streaks
- **Phase 4** (was Phase 3): analytics, growth, more cities/categories

## 13. Next steps

1. You confirm/correct Section 12.
2. I scaffold the actual project (React + Vite frontend, Supabase schema, Vercel deploy config) — both light and dark themes built in from the start.
3. We build screen-by-screen starting with Phase 1.
