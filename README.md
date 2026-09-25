# hoppin. · Bengaluru & Chennai

> **Step Out. Show Up.**  
> Real-time platform to discover and book verified turf courts, resto-bars, gyms, board game cafes, and youth health & morning run clubs across Bengaluru and Chennai.

---

## ✨ Features & Architecture

- **4 Overlapping Square Drops**: Floating bridge showcasing top youth health clubs, midnight turfs, and rooftop brewery takeovers.
- **Youth Health & Morning Activity Clubs (like Strava)**:
  - 🌅 5:15 AM Sunrise Run Clubs (e.g. Bessie Flyers, CORSO BLR)
  - 🧘 Dawn Park Yoga (Cubbon Park)
  - 🚴 Weekend Coastal Cycling Pelotons (ECR Ciclo)
  - ⚽ Midnight Floodlit Futsal & Turf Sports
  - 100% self-serve: anyone can launch a club and become **Club Captain / Admin** instantly.
- **Day-to-Day Status & Offers on DP ("Seen on their DP not elsewhere")**:
  - Venue owners and Club captains upload fresh daily photos from their phone or device.
  - Post live morning status & exclusive flash offers directly to their pulsating **DP Story Ring**.
- **Role-Based Access Control (RBAC)**:
  1. 👤 **Customer / Regular Hopper**: Book turfs, gyms, resto-bars, earn streaks, join morning runs.
  2. 🏃 **Club Admin**: Manage morning runs, attendee rosters, and broadcast bulletins.
  3. 🏟️ **Venue / Resto-bar Owner**: Live revenue analytics (₹18,400/day), court availability matrix, QR ticket scanner.
  4. 🛠️ **Help & Support / Platform HQ**: System telemetry and operational monitoring.
- **Activity Streaks & Gamification**:
  - Habit tracking with live XP progress (`🔥 4-Day Streak · 180 XP`).
  - Milestone perks: Early Bird, Turf Master, Tap Hopper.
  - Interactive simulation & claim button.
- **Instant UPI & Card Checkout**:
  - Procedural QR code generator.
  - 1-click GPay, PhonePe, Paytm links and custom UPI ID inputs (`@okhdfcbank`, `@okaxis`, etc.).
- **RAG-Powered AI Concierge**:
  - Semantic venue & club search with real-time slot pricing and hold capabilities.

---

## 🚀 Quick Start (Local Run)

### 1. Install Dependencies
```bash
npm install
```

### 2. Run the Development Servers
- **Web App (Vite)**:
  ```bash
  npm run dev
  ```
  App will open on `http://localhost:5173/`

- **Backend API (Express + TypeScript)**:
  ```bash
  npm run dev:server
  ```
  API runs on `http://localhost:4000/`

---

## 📦 Production Build

```bash
npm run build
```
Builds the production-ready bundle into `apps/web/dist/`.

---

## 🌐 Deploy to Vercel

### Option A: Via GitHub (Recommended)
1. Push your repository to GitHub (see instructions below).
2. Go to [Vercel Dashboard](https://vercel.com/roshini040s-projects) and click **"Add New Project"**.
3. Select your GitHub repository (`hoppin`).
4. Vercel will automatically detect `vercel.json`:
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build --workspace=apps/web`
   - **Output Directory**: `apps/web/dist`
5. Click **Deploy**! Your app will be live on Vercel with automatic HTTPS.

### Option B: Via Vercel CLI
```bash
npx vercel
```
Follow the interactive prompts to link and deploy in 60 seconds.

---

## 🐙 Push to GitHub

```bash
# 1. Stage all files
git add .

# 2. Commit
git commit -m "feat: complete hoppin fullstack with youth clubs, 4-role auth, streaks, and upi checkout"

# 3. Rename branch to main
git branch -M main

# 4. Link your remote repository (create 'hoppin' on https://github.com/new first)
git remote add origin https://github.com/Roshini040/hoppin.git

# 5. Push to GitHub
git push -u origin main
```
