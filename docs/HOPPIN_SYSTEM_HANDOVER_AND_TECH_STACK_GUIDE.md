# Hoppin — System Architecture, Technology Stack & Handover Guide

> **Document Version:** 1.0.0  
> **Target Platform:** Web (Vite + React), Backend (Node.js + Express), Database (Postgres / Supabase)  
> **Deployment Target:** Vercel (Frontend), Node.js / Docker (Backend)  
> **Target Markets:** Bengaluru (BLR) & Chennai (MAA)  
> **Status:** Production-Ready & Verified

---

## 1. Executive Overview

**Hoppin** (`hoppin.`) is a curated, real-time discovery and instant-booking platform designed for youth and urban enthusiasts across **Bengaluru and Chennai**. The platform connects users with verified sports turf courts, gym & sauna facilities, craft taprooms, resto-bars, board game lounges, and self-serve youth health & morning activity clubs (running, sunrise yoga, cycling pelotons, and midnight futsal).

### Core Pillars
1. **Curated Venues & Instant Slots**: Real-time hourly slot pricing, live occupancy matrices, and zero-friction checkout with Indian UPI (QR code, GPay, PhonePe, Paytm) and cards.
2. **Youth Health & Morning Activity Clubs**: Self-serve community club creation (like Strava) with instant go-live, member activity tracking, and morning run scheduling.
3. **Day-to-Day Status & Flash Offers on DP**: Venue owners and Club captains upload daily photos directly from their phone/device and post live status updates with flash discounts displayed exclusively on their pulsating **DP Story Ring**.
4. **4-Role Access Control (RBAC)**: Separated user flows for Customers, Club Admins, Venue/Gym Owners, and Platform Support Operations.
5. **Streaks & Engagement Gamification**: Daily activity habit tracker with XP progression (`🔥 4-Day Streak · 180 XP`) and milestone badge unlocks.
6. **RAG-Powered AI Concierge**: Semantic venue retrieval and conversational booking assistant with automatic city routing (`BLR` vs `MAA`).

---

## 2. Complete Technology Stack Matrix

| Layer | Technology | Version | Purpose & Description |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | **Vite + React** | `5.4.x` / `18.3.x` | Ultra-fast client build tool, HMR, and component tree |
| **Frontend UI Core** | **Vanilla CSS + CSS Variables** | CSS3 / Tokens | Custom **Grail Lilac & Obsidian Violet Noir** design system; zero Tailwind dependency for maximum performance and fluid 60fps animations |
| **Typography** | **Google Fonts** | Latest | `Bodoni Moda` (Editorial Serif), `Plus Jakarta Sans` (Geometric UI Sans), `Space Grotesk` (Technical Mono) |
| **Icons & Media** | **Custom Inline SVGs + Unsplash CDN** | SVG 2.0 | High-resolution curated imagery with zero layout shift |
| **Backend Runtime** | **Node.js** | `>= 18.x` | Fast, asynchronous server runtime environment |
| **API Framework** | **Express.js** | `4.19.x` | Robust RESTful routing engine, middleware pipeline, and CORS |
| **Language** | **TypeScript** | `5.5.x` | Strict type safety across server models and API contracts |
| **Execution Tool** | **tsx** | `4.16.x` | Real-time TypeScript execution with hot reload |
| **Database** | **PostgreSQL (Supabase)** | `15.x` / Supabase v2 | Relational schema with ACID compliance and row-level security |
| **Vector Extension** | **pgvector** | Extension | Vector similarity embeddings storage for semantic search |
| **Local Embeddings** | **@xenova/transformers** | `2.17.x` | Client-side/local embeddings engine; zero third-party latency |
| **LLM Provider** | **Claude 3.5 Sonnet / Local RAG** | SDK `0.32.x` | Semantic reasoning engine, conversational booking, slot holds |
| **Payment Gateway** | **Procedural UPI Engine + Stripe** | v16 | Indian UPI QR Code generator, VPA inputs (`@okhdfcbank`, `@okaxis`, `@paytm`), 1-click app deep-links, and fallback card processor |
| **Deployment / Hosting**| **Vercel** | Monorepo Engine | Automatic production builds, edge network distribution, HTTPS |
| **Version Control** | **Git / GitHub** | `2.49.x` | Distributed source code management on `main` branch |

---

## 3. Monorepo Architecture & Directory Layout

```
hoppin/
├── apps/
│   ├── web/                         # Main User, Club & Partner Web Application
│   │   ├── index.html               # Production Single Page App (Grail Lilac Theme)
│   │   ├── src/                     # React application source (pages, components)
│   │   ├── public/                  # Static assets and POC fallbacks
│   │   ├── package.json             # Web workspace configuration
│   │   └── vite.config.ts           # Vite build & proxy settings
│   ├── partner/                     # Dedicated Partner & Venue Operations App
│   └── admin/                       # Internal Admin & Analytics Console
├── server/                          # Shared Express Backend API
│   ├── src/
│   │   ├── index.ts                 # Server entrypoint & route registration
│   │   ├── routes/
│   │   │   ├── venues.ts            # Venue queries, city filters, detail views
│   │   │   ├── clubs.ts             # Youth health clubs, RSVPs, club creation
│   │   │   ├── admin.ts             # 4-role RBAC endpoints & telemetry
│   │   │   ├── bookings.ts          # Reservation creation, ticket verification
│   │   │   ├── auth.ts              # Authentication & session verification
│   │   │   ├── chat.ts              # RAG AI Concierge chat endpoint
│   │   │   ├── promos.ts            # Discount codes & flash drop validation
│   │   │   └── saved.ts             # User bookmarking & favorites
│   │   ├── services/
│   │   │   ├── store.ts             # In-memory verified venue repository
│   │   │   ├── bookingService.ts    # Slot hold & expiration mechanics
│   │   │   └── rag/
│   │   │       ├── chatAgent.ts     # Intelligent fallback reasoning agent
│   │   │       ├── retrieve.ts      # Semantic search & city auto-detection
│   │   │       └── embed.ts         # Vector generation
│   │   └── config/db.ts             # Supabase & Postgres connection pool
│   └── package.json                 # Backend workspace configuration
├── supabase/
│   ├── migrations/                  # Schema SQL migrations (venues, clubs, users)
│   └── seed/                        # Verified venues seed dataset
├── docs/                            # Architectural specifications & handover documentation
├── .gitignore                       # Production ignore filters (node_modules, dist)
├── package.json                     # Monorepo workspace configuration & build scripts
├── README.md                        # Quick start, push, and hosting instructions
└── vercel.json                      # Vercel deployment & rewrite rules
```

---

## 4. Key Functional Modules & Business Logic

### A. 4-Role Access Control (RBAC) Hub
The platform provides 4 distinct user identities with dedicated permissions:

```
                               ┌───────────────────────────┐
                               │     Hoppin Auth Hub       │
                               └─────────────┬─────────────┘
                                             │
      ┌──────────────────┬───────────────────┼───────────────────┐
      │                  │                   │                   │
      ▼                  ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  1. Customer │   │2. Club Admin │   │3. Venue Owner│   │4. Support HQ │
├──────────────┤   ├──────────────┤   ├──────────────┤   ├──────────────┤
│• Book slots  │   │• Run clubs   │   │• Resto-bars  │   │• Operations  │
│• Streaks & XP│   │• Morning 5AM │   │• Sports turf │   │• Telemetry   │
│• Join clubs  │   │• Post DP perk│   │• Live revenue│   │• Audit logs  │
│• User pass   │   │• Member list │   │• Court matrix│   │• Multi-city  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

1. **Customer (Regular Hopper)**:
   - Profile building, habit tracking, mobile ticket passport.
   - Upgrade capability: Can click `+ Launch a Youth Health Club` anytime to become a Club Admin.
2. **Club Admin (Like Strava Clubs)**:
   - Self-serve club launch with **instant go-live** (zero manual approval required).
   - Upload daily run photos directly from phone/laptop.
   - Member roster with attendance check-in buttons that award +20 Streak XP.
3. **Venue / Resto-bar / Gym Owner**:
   - Self-serve onboarding with **instant go-live** (zero pending reviews).
   - Live revenue analytics: Today's Gross (₹18,400), Weekly Volume (₹1,24,600), HDFC Bank Settlement status.
   - Upload daily venue photos via native file picker or URL with real-time preview.
   - Real-time Court/Table Matrix (Available, Booked, Walk-in Only).
   - QR Scanner / Reference ticket validator (e.g. `HOP-BLR-8921`).
4. **Help & Support / Platform Operations (4th)**:
   - Internal operational telemetry (Gross Volume: ₹28,45,200, 67 venues, 18 clubs).
   - Relocated discreetly to the footer (`#/support`) to keep consumer UX clean.

---

### B. Day-to-Day Status & Flash Offers on DP
*"As offer can be seen on their DP not elsewhere"*

- **Concept**: Emulates an Instagram/WhatsApp story circle around the venue/club avatar (DP).
- **Presentation**: Pulsating neon gradient border (`.dp-story-ring.pulse`) and floating discount badge (e.g., `⚡ 20% OFF` or `⚡ FREE COFFEE`).
- **Modal View**:
  - Full-resolution photo uploaded by the admin/owner today.
  - Verification tag: e.g., *"Uploaded 2 hours ago by Mukesh V (Operations GM)"*.
  - Status update: e.g., *"⚽ Court 1 & 2 floodlights recalibrated today! Fresh turf shoes available."*
  - Flash Offer Box: Exclusive today-only promo code with a 1-click **"Claim Offer & Book"** button that automatically applies the discount to checkout!

---

### C. Youth Health & Activity Clubs (Chennai & Bengaluru Trend)
Addresses the cultural shift where youngsters wake up at 5:15 AM for coastal beach runs, sunrise park yoga, cycling pelotons, and midnight futsal:
- **Featured Clubs**:
  - 🌅 *Bessie Flyers Run Club* (Besant Nagar Elliot's Beach, Chennai · 5:15 AM)
  - 🧘 *Cubbon Park Sunrise Yoga* (Bamboo Grove, Bengaluru · 6:30 AM)
  - 🏃 *CORSO Run Club Bangalore* (Koramangala 4th Block · 6:00 AM)
  - 🚴 *Ciclo Cafe Cycling Peloton* (Kotturpuram & ECR, Chennai · 5:30 AM)
  - ⚽ *Indiranagar Midnight Futsal Crew* (Arena Complex, Bengaluru · 9:00 PM)
  - 🎲 *Gameistry Board Game Guild* (Egmore, Chennai · 4:00 PM)
- **Actions**:
  - `RSVP Next Session · Free` (instant toggle, updates attendee count, awards +20 XP).
  - `+ Start Your Own Club` (self-serve launch modal with instant go-live).

---

### D. Activity Streaks & Gamification Engine
- **Active Streak Counter**: Persistent flame icon in sticky nav (`🔥 4 Streak`).
- **How Streaks & XP Work**:
  1. *Daily App Check-in*: +25 XP
  2. *Join a Morning Run Club*: +20 XP
  3. *Book a Turf, Gym, or Resto-bar*: +30 XP
  4. *On-site Venue / Beach Check-in*: +50 XP
- **Milestone Rewards**:
  - 🌅 *Early Bird Badge* (10% off turf court bookings)
  - ⚽ *Turf Master Badge* (Free filter coffee & medu vada at Murugan Idli after 5K run)
  - 🍻 *Tap Hopper Badge* (20% off craft pitchers or court slots)
- **Interactive Simulation**: Dedicated test button inside the modal (`⚡ Click to Test / Claim Today's Activity Streak`) that simulates streak progression (4 ➔ 5 Days, 205 XP) with visual celebratory toast.

---

### E. Instant UPI & Card Checkout
- Built specifically for the Indian payments ecosystem:
  - **Procedural High-Resolution QR Code**: Scannable by any UPI application.
  - **1-Click Deep Links**: Google Pay, PhonePe, Paytm.
  - **Custom VPA Validation**: Auto-formats `@okhdfcbank`, `@okaxis`, `@paytm`, `@ybl`.
  - **Instant Verification**: Generates immutable booking reference (e.g. `HOP-BLR-8921`) and adds pass to user's profile.

---

## 5. API Endpoints Reference

All API routes are mounted under `/api/` (with backward-compatible fallbacks at root):

| Method | Endpoint | Description | Request Body / Query |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | Service health status & venue count | None |
| `GET` | `/api/venues` | Retrieve all 67 venues with city/cat filter | `?city=BLR&cat=sports` |
| `GET` | `/api/venues/:id` | Detailed venue profile & available slots | None |
| `GET` | `/api/clubs` | Retrieve health & morning activity clubs | `?city=all` |
| `POST` | `/api/clubs` | Create new youth club (instant go-live) | `{ name, city, category, schedule, captain }` |
| `POST` | `/api/clubs/:id/rsvp` | RSVP toggle for club meetup & streak XP | `{ email }` |
| `GET` | `/api/admin/roles` | RBAC identities & capability profiles | None |
| `GET` | `/api/admin/data` | Role-specific dashboard metrics | `?role=restaurant_admin` |
| `POST` | `/api/admin/venue/status`| Toggle court/table live availability | `{ resourceId, status }` |
| `POST` | `/api/admin/ticket/checkin`| Validate booking reference code | `{ ticketRef: "HOP-BLR-8921" }` |
| `POST` | `/api/chat` | RAG AI Concierge conversational turn | `{ message, city, history }` |
| `POST` | `/api/bookings` | Create confirmed venue reservation | `{ venueId, slot, date, paymentMethod }` |
| `POST` | `/api/auth/login` | Authenticate customer/partner | `{ email, password }` |

---

## 6. How to Run Locally

### Prerequisites
- Node.js `>= 18.0.0`
- npm `>= 9.0.0`

### Step 1: Install Dependencies
```bash
npm install
```

### Step 2: Start Development Servers
```bash
# Terminal 1: Run Vite Frontend Client (Port 5173)
npm run dev

# Terminal 2: Run Express Backend Server (Port 4000)
npm run dev:server
```

### Step 3: Access Applications
- **Consumer Web App**: `http://localhost:5173/`
- **Partner Portal**: `http://localhost:5173/#/owner`
- **Clubs Hub**: `http://localhost:5173/#/clubs`
- **Backend API Health**: `http://localhost:4000/api/health`

---

## 7. How to Push to GitHub & Deploy on Vercel

### Step 1: Push to GitHub
Repository target: [github.com/Roshini040](https://github.com/Roshini040)

```powershell
# Inside project directory:
git add .
git commit -m "feat: complete hoppin fullstack platform with clubs, 4-role rbac, and upi"
git branch -M main
git remote add origin https://github.com/Roshini040/hoppin.git
git push -u origin main
```

### Step 2: Host on Vercel
Vercel Dashboard: [vercel.com/roshini040s-projects](https://vercel.com/roshini040s-projects)

1. Click **Add New...** ➔ **Project**.
2. Select repository `hoppin` and click **Import**.
3. Vercel automatically detects `vercel.json`:
   - **Framework**: Vite
   - **Build Command**: `npm run build --workspace=apps/web`
   - **Output Directory**: `apps/web/dist`
4. Click **Deploy**. The application will be live globally with an SSL-secured URL.

---

## 8. State Persistence & LocalStorage Keys

The web application stores key states locally to guarantee continuous offline resilience:

| Key | Type | Description |
| :--- | :--- | :--- |
| `hoppin.theme` | `'dark' \| 'light'` | Active UI theme (Obsidian Violet Noir default) |
| `hoppin.session` | `string` | Logged-in user email |
| `hoppin.streak` | `{ days, xp, lastCheckin }` | Active activity habit counter & XP |
| `hoppin.owner_user` | `{ name, email, venueName, city }` | Logged-in venue owner profile |
| `hoppin.dp_status` | `Record<string, DPStatus>` | Day-to-day status updates, photos & offers |
| `hoppin.saved` | `string[]` | Array of bookmarked venue IDs |
| `hoppin.bookings:<email>`| `Booking[]` | User's confirmed mobile pass tickets |

---

## 9. Verification & Acceptance Checklist

- [x] **Branding**: Clean `hoppin. Bengaluru · Chennai` header without repetitive "67 venues" badges.
- [x] **Category Filtering**: Clicking Sports, Dining, and Games instantly filters cards and smoothly scrolls to `#explore`.
- [x] **Star Rating Overlap Fixed**: Frosted pill badge (`★ 4.8 · 1,240 reviews`) with zero overlap.
- [x] **4-Role Sign In Hub**: Customer, Club Admin, Venue Owner, and Support HQ with 1-click instant demo access.
- [x] **Customer Profile**: Displays user streak, joined clubs, confirmed booking passes, and club launch button.
- [x] **How Streaks Work Hub**: 4-step explanation, milestone rewards, and interactive simulation button (+25 XP, 4 ➔ 5 days).
- [x] **Self-Serve Club Creation**: Anyone can launch a youth club with instant go-live.
- [x] **Self-Serve Venue Onboarding**: Venue owners can register resto-bars or turfs with instant go-live.
- [x] **Partner Owner Dashboard**: Live gross revenue (₹18,400 today), weekly volume, HDFC bank settlement, file photo upload, and court matrix.
- [x] **Day-to-Day Status on DP**: Photo upload from device and flash offer displayed exclusively on the DP story ring.
- [x] **UPI Checkout**: High-res procedural QR code, VPA auto-suggestions, and 1-click GPay/PhonePe/Paytm links.
- [x] **AI Concierge**: Verified recommendations across Bengaluru & Chennai with slot pricing and holds.
- [x] **Repository Cleanliness**: Scratch scripts removed; branch set to `main`; `vercel.json` configured.

---
*Document approved and verified for project handover.*
