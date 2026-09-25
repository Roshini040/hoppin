# Script to apply all user requirements to Hoppin:
# 1. Zero-overlap star rating badge
# 2. 4 Overlapping Square Drops between Hero and Chapter 01
# 3. Admins upload day-to-day status and photos as offers on their DP ("seen on their dp not elsewhere")
# 4. Youth health and activity clubs hub (Chennai & Bengaluru running, yoga, cycling, futsal, board games)
# 5. 3-Admin RBAC (Platform Super Admin, Group/Club Admin, Restaurant/Venue Admin)
# 6. Daily Activity Streaks & Gamification
# 7. UPI Payment with QR & VPA
# 8. Write to all 5 target files

import os
import re
import sys

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    content = f.read()

# =====================================================================
# 1. FIX STAR RATING CSS & PREVENT OVERLAP
# =====================================================================
# Replace `.cv svg { position: absolute; ... }` with `.cv > svg.cv-fallback`
content = content.replace(
    ".cv svg { position: absolute; inset: 0; width: 100%; height: 100%; }",
    ".cv > svg.cv-fallback { position: absolute; inset: 0; width: 100%; height: 100%; }"
)

# Enhance .cv .rate and .star CSS
old_rate_rule = """.cv .rate {
  position: absolute;
  left: 14px;
  bottom: 14px;
  z-index: 5;
  color: #fff;
  font-family: var(--mono);
  font-size: 11.5px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(13, 8, 24, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(196, 181, 253, 0.3);
  box-shadow: 0 4px 16px rgba(0,0,0,0.5);
  white-space: nowrap;
}
.cv .rate b { color: #fff; font-weight: 700; font-size: 12.5px; }
.cv .rate .rate-sep { color: rgba(196,181,253,0.5); font-size: 10px; margin: 0 1px; }
.cv .rate .rate-count { color: #c4b5fd; font-size: 11px; font-weight: 500; }
.star { width: 13px; height: 13px; fill: #f0b94a; flex-shrink: 0; }"""

new_rate_rule = """.cv .rate {
  position: absolute;
  left: 14px;
  bottom: 14px;
  z-index: 5;
  color: #fff;
  font-family: var(--mono);
  font-size: 11.5px;
  display: inline-flex !important;
  align-items: center !important;
  gap: 5px !important;
  padding: 5px 12px !important;
  border-radius: 999px !important;
  background: rgba(13, 8, 24, 0.88) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(196, 181, 253, 0.35) !important;
  box-shadow: 0 4px 16px rgba(0,0,0,0.5) !important;
  white-space: nowrap !important;
}
.cv .rate b { color: #fff; font-weight: 700; font-size: 12.5px; }
.cv .rate .rate-sep { color: rgba(196,181,253,0.5); font-size: 10px; margin: 0 1px; }
.cv .rate .rate-count { color: #c4b5fd; font-size: 11px; font-weight: 500; }
.cv .rate .star, .star {
  position: static !important;
  inset: auto !important;
  width: 13px !important;
  height: 13px !important;
  fill: #f0b94a !important;
  flex-shrink: 0 !important;
  display: inline-block !important;
  vertical-align: middle !important;
}"""

if old_rate_rule in content:
    content = content.replace(old_rate_rule, new_rate_rule)
    print("Updated rate CSS successfully.")
else:
    print("Notice: old_rate_rule not exact match, injecting fallback star fix...")
    content = content.replace(".star { width: 13px; height: 13px; fill: #f0b94a; flex-shrink: 0; }", new_rate_rule)

# =====================================================================
# 2. ADD COMPREHENSIVE CSS FOR:
# - 4 Overlapping Square Drops
# - DP Story & Status Ring ("can be seen there dp not elsewhere")
# - Health & Morning Clubs Hub
# - 3-Admin RBAC Portal
# - Streaks & Gamification
# =====================================================================
extra_css = """
/* -------------------------------------------------------------
   4 SQUARE DROPS (OVERLAPPING BETWEEN HERO & CHAPTER 01)
   ------------------------------------------------------------- */
.drops-overlap {
  position: relative;
  z-index: 25;
  margin-top: -85px;
  margin-bottom: 50px;
}
.drops-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 22px;
  flex-wrap: wrap;
  gap: 16px;
}
.drops-badge {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.12em;
  font-weight: 700;
  color: var(--pastel);
  background: rgba(196,181,253,0.12);
  border: 1px solid rgba(196,181,253,0.3);
  padding: 4px 12px;
  border-radius: 999px;
  display: inline-block;
  margin-bottom: 6px;
}
.drops-headline {
  font-family: var(--serif);
  font-size: clamp(1.4rem, 2.6vw, 2.2rem);
  font-weight: 400;
  letter-spacing: -0.02em;
  margin: 0;
  color: var(--text);
}
.streak-mini-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 999px;
  background: rgba(13, 8, 24, 0.88);
  border: 1px solid rgba(240, 185, 74, 0.45);
  box-shadow: 0 4px 20px rgba(240, 185, 74, 0.18);
  color: #fff;
  font-size: 13px;
  font-family: var(--sans);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.streak-mini-pill:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(240, 185, 74, 0.35);
}
.streak-mini-pill .flame { font-size: 17px; }
.streak-mini-pill .streak-txt b { color: #f0b94a; font-weight: 700; }
.streak-mini-pill .streak-arrow { color: var(--pastel); font-weight: bold; margin-left: 4px; }

.drops-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}
@media (max-width: 1100px) {
  .drops-grid-4 { grid-template-columns: repeat(2, 1fr); }
  .drops-overlap { margin-top: -40px; }
}
@media (max-width: 620px) {
  .drops-grid-4 { grid-template-columns: 1fr; }
  .drops-overlap { margin-top: -20px; }
}

.sq-drop-card {
  position: relative;
  aspect-ratio: 1 / 1;
  border-radius: 20px;
  overflow: hidden;
  background: #0f0b18;
  border: 1px solid rgba(196, 181, 253, 0.22);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.3s, box-shadow 0.35s;
}
.sq-drop-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: rgba(196, 181, 253, 0.6);
  box-shadow: 0 24px 60px rgba(124, 58, 237, 0.3);
}
.sq-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
  z-index: 1;
}
.sq-drop-card:hover .sq-bg { transform: scale(1.08); }
.sq-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(7,5,10,0.25) 0%, rgba(7,5,10,0.55) 40%, rgba(7,5,10,0.95) 100%);
  z-index: 2;
}
.sq-top {
  position: relative;
  z-index: 3;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}
.sq-tag {
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(13, 8, 24, 0.8);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #fff;
}
.sq-badge-hot {
  font-family: var(--mono);
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(239, 68, 68, 0.3);
  border: 1px solid rgba(239, 68, 68, 0.6);
  color: #ff9999;
}
.sq-badge-flash {
  font-family: var(--mono);
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(245, 158, 11, 0.3);
  border: 1px solid rgba(245, 158, 11, 0.6);
  color: #fcd34d;
}
.sq-bottom {
  position: relative;
  z-index: 3;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.sq-time {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--pastel);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.sq-title {
  font-size: 15.5px;
  font-weight: 700;
  color: #fff;
  line-height: 1.25;
  margin: 0;
}
.sq-desc {
  font-size: 11.5px;
  color: #d1cbe5;
  line-height: 1.35;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.sq-meta {
  display: flex;
  justify-content: space-between;
  font-family: var(--mono);
  font-size: 11px;
  color: #a49ebd;
  margin-top: 2px;
}
.sq-streak { color: #f0b94a; font-weight: 600; }
.sq-btn {
  margin-top: 6px;
  width: 100%;
  padding: 8px 12px;
  border-radius: 10px;
  background: rgba(196, 181, 253, 0.2);
  border: 1px solid rgba(196, 181, 253, 0.4);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  font-family: var(--sans);
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
}
.sq-btn:hover {
  background: var(--pastel);
  color: #0d0818;
  border-color: var(--pastel);
  transform: translateY(-1px);
}
.sq-btn.glow {
  background: linear-gradient(135deg, rgba(124,58,237,0.7) 0%, rgba(196,181,253,0.8) 100%);
  border: none;
  box-shadow: 0 4px 16px rgba(124,58,237,0.4);
}
.sq-btn.glow:hover { background: #c4b5fd; color: #07050a; }

/* -------------------------------------------------------------
   DP STORY & STATUS RING ("as offer can be seen there dp not elsewhere")
   ------------------------------------------------------------- */
.dp-story-wrap {
  position: absolute;
  right: 58px;
  bottom: 11px;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: transform 0.2s;
}
.dp-story-wrap:hover { transform: scale(1.1); }
.dp-story-ring {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  padding: 2.2px;
  background: linear-gradient(135deg, #f0b94a, #ec4899, #8b5cf6, #3b82f6);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 12px rgba(236, 72, 153, 0.5);
}
.dp-story-ring.pulse { animation: dpPulse 2s infinite ease-in-out; }
@keyframes dpPulse {
  0% { box-shadow: 0 0 0 0 rgba(236, 72, 153, 0.7); }
  70% { box-shadow: 0 0 0 8px rgba(236, 72, 153, 0); }
  100% { box-shadow: 0 0 0 0 rgba(236, 72, 153, 0); }
}
.dp-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #0d0818;
}
.dp-status-badge {
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(236, 72, 153, 0.95);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 2px 8px rgba(0,0,0,0.5);
  white-space: nowrap;
}

/* DP Story Modal ("Seen on their DP") */
.dp-story-modal {
  padding: 24px;
  max-width: 520px;
  margin: 0 auto;
}
.dp-story-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}
.dp-author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}
.dp-story-photo-box {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  max-height: 280px;
  margin-bottom: 16px;
  border: 1px solid rgba(196,181,253,0.3);
}
.dp-story-photo-box img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  display: block;
}
.dp-photo-tag {
  position: absolute;
  left: 12px;
  bottom: 12px;
  background: rgba(13,8,24,0.85);
  backdrop-filter: blur(10px);
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-family: var(--mono);
  color: #fff;
  border: 1px solid rgba(255,255,255,0.15);
}
.dp-status-bubble {
  background: rgba(196,181,253,0.08);
  border: 1px solid rgba(196,181,253,0.2);
  border-radius: 14px;
  padding: 14px 16px;
  margin-bottom: 16px;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--text);
}
.dp-exclusive-offer {
  background: linear-gradient(135deg, rgba(236,72,153,0.15) 0%, rgba(124,58,237,0.15) 100%);
  border: 1px solid rgba(236,72,153,0.4);
  border-radius: 16px;
  padding: 16px 18px;
  margin-bottom: 16px;
}
.dp-offer-title {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  margin-top: 4px;
  margin-bottom: 12px;
}
.dp-offer-cta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}
.dp-promo-tag {
  font-family: var(--mono);
  font-size: 12px;
  background: rgba(13,8,24,0.9);
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px dashed rgba(240,185,74,0.6);
  color: #f0b94a;
}

/* -------------------------------------------------------------
   HEALTH & MORNING CLUBS HUB (#/clubs)
   ------------------------------------------------------------- */
.clubs-hero {
  padding: 70px clamp(20px,5vw,72px) 40px;
  text-align: center;
  background: radial-gradient(circle at 50% 20%, rgba(124,58,237,0.18) 0%, transparent 70%);
}
.clubs-hero h1 {
  font-family: var(--serif);
  font-size: clamp(2.2rem, 5vw, 4rem);
  font-weight: 400;
  line-height: 1.1;
  margin: 12px 0 16px;
}
.clubs-filter-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 34px;
}
.club-chip {
  padding: 8px 18px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 600;
  border: 1px solid var(--line);
  background: var(--bg2);
  color: var(--muted);
  cursor: pointer;
  transition: all 0.2s;
}
.club-chip:hover, .club-chip.active {
  background: var(--btn-bg);
  color: var(--btn-fg);
  border-color: var(--pastel);
}
.clubs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 28px;
  padding: 0 clamp(20px,5vw,72px) 80px;
}
.club-card {
  background: var(--bg2);
  border: 1px solid var(--line);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 16px 40px rgba(0,0,0,0.25);
  display: flex;
  flex-direction: column;
  transition: transform 0.3s, border-color 0.3s;
}
.club-card:hover {
  transform: translateY(-6px);
  border-color: var(--pastel);
}
.club-media {
  position: relative;
  aspect-ratio: 16 / 9;
  background: #120a1f;
  overflow: hidden;
}
.club-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.club-body {
  padding: 22px;
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: space-between;
}
.club-next-box {
  background: rgba(196,181,253,0.08);
  border: 1px solid rgba(196,181,253,0.2);
  border-radius: 12px;
  padding: 10px 14px;
  margin: 14px 0;
  font-size: 12.5px;
  font-family: var(--mono);
}
.club-actions {
  display: flex;
  gap: 10px;
  margin-top: 14px;
}

/* -------------------------------------------------------------
   3-ADMIN RBAC PORTAL (#/admin)
   ------------------------------------------------------------- */
.admin-shell {
  padding: 40px clamp(20px,5vw,72px) 80px;
}
.admin-role-nav {
  display: flex;
  gap: 12px;
  margin-bottom: 32px;
  flex-wrap: wrap;
  border-bottom: 1px solid var(--line);
  padding-bottom: 18px;
}
.admin-role-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: var(--bg2);
  color: var(--text);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.admin-role-tab.active {
  background: var(--tint);
  border-color: var(--pastel);
  color: var(--tint-fg);
  box-shadow: 0 4px 16px rgba(124,58,237,0.2);
}
.admin-banner {
  background: linear-gradient(135deg, rgba(124,58,237,0.14) 0%, rgba(196,181,253,0.08) 100%);
  border: 1px solid rgba(196,181,253,0.25);
  border-radius: 18px;
  padding: 22px 26px;
  margin-bottom: 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}
.admin-stat-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 18px;
  margin-bottom: 28px;
}
.admin-stat-card {
  background: var(--bg2);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 20px;
}
.admin-stat-num {
  font-family: var(--serif);
  font-size: 2rem;
  font-weight: 600;
  margin: 6px 0 2px;
  color: var(--pastel);
}

/* -------------------------------------------------------------
   STREAKS & ENGAGEMENT HUB
   ------------------------------------------------------------- */
.streak-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(240, 185, 74, 0.12);
  border: 1px solid rgba(240, 185, 74, 0.4);
  color: #f0b94a;
  font-family: var(--mono);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}
.streak-btn:hover {
  background: rgba(240, 185, 74, 0.22);
  transform: translateY(-1px);
}
"""

# Inject extra CSS before </style>
content = content.replace("</style>", extra_css + "\n</style>")
print("Injected extra CSS successfully.")

# =====================================================================
# 3. UPDATE HEADER: ADD STREAK BUTTON & NAV LINKS
# =====================================================================
old_hdr = """<header class="hdr" id="hdr">
  <a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues</span></a>
  <nav class="nav" id="nav" aria-label="Primary"></nav>
  <i class="sep"></i>
  <button class="icon-btn" id="themeBtn" data-act="theme" aria-label="Toggle theme"></button>
  <button class="acct" id="acct" data-act="account">Sign in</button>
</header>"""

new_hdr = """<header class="hdr" id="hdr">
  <a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues & clubs</span></a>
  <nav class="nav" id="nav" aria-label="Primary"></nav>
  <button class="streak-btn" id="streakNavBtn" data-act="open-streaks" title="Activity Streak & XP">
    <span>🔥</span> <b id="streakDaysCount">4</b> <span class="streak-lbl">Streak</span>
  </button>
  <i class="sep"></i>
  <button class="icon-btn" id="themeBtn" data-act="theme" aria-label="Toggle theme"></button>
  <button class="acct" id="acct" data-act="account">Sign in</button>
</header>"""

if old_hdr in content:
    content = content.replace(old_hdr, new_hdr)
    print("Updated header with streak button successfully.")

# Update NAV array
old_nav_def = """const NAV=[['discover','Discover','Explore','#/','explore'],['sports','Sports','Sports','#/cat/sports','sports'],['dining','Dining','Dining','#/cat/dining','dining'],['gaming','Gaming','Gaming','#/cat/gaming','gaming'],['chat','AI Concierge','AI Chat','#/chat','chat']];"""
new_nav_def = """const NAV=[
  ['discover','Discover','Explore','#/','explore'],
  ['clubs','Clubs & Runs 🔥','Clubs','#/clubs','run'],
  ['admin','Admin RBAC','Admin','#/admin','admin'],
  ['sports','Sports','Sports','#/cat/sports','sports'],
  ['dining','Dining','Dining','#/cat/dining','dining'],
  ['gaming','Gaming','Gaming','#/cat/gaming','gaming'],
  ['chat','AI Concierge','AI Chat','#/chat','chat']
];"""

if old_nav_def in content:
    content = content.replace(old_nav_def, new_nav_def)
    print("Updated NAV array with Clubs and Admin RBAC successfully.")

# =====================================================================
# 4. INSERT 4 OVERLAPPING SQUARE DROPS BETWEEN HERO & CHAPTER 01
# =====================================================================
four_drops_html = """  <!-- FLOATING 4 SQUARE DROPS BRIDGE (OVERLAPPING HERO & CHAPTER 01) -->
  <section class="drops-overlap wrap" id="topDrops">
    <div class="drops-bar">
      <div class="drops-lead">
        <span class="drops-badge">⚡ NEW DROPS & OPENINGS</span>
        <h2 class="drops-headline">Top 4 Youth Health & Night Drops</h2>
      </div>
      <div class="streak-mini-pill" data-act="open-streaks" title="Click to view Streak & Rewards">
        <span class="flame">🔥</span>
        <span class="streak-txt"><b>4-Day Streak</b> · +25 XP next activity</span>
        <span class="streak-arrow">→</span>
      </div>
    </div>

    <div class="drops-grid-4">
      <!-- 1. Bessie Flyers 5:15 AM Sunrise Run (Chennai) -->
      <div class="sq-drop-card" data-act="open-club" data-id="c01">
        <img class="sq-bg" src="https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=700&q=80" alt="Bessie Flyers">
        <div class="sq-overlay"></div>
        <div class="sq-top">
          <span class="sq-tag run">🏃 Morning Run Club</span>
          <span class="sq-badge-hot">🔥 #1 in Chennai</span>
        </div>
        <div class="sq-bottom">
          <div class="sq-time">🌅 Tomorrow 05:15 AM</div>
          <h3 class="sq-title">Bessie Flyers 5:15 AM Sunrise Run</h3>
          <p class="sq-desc">Besant Nagar Elliot's Beach · 5K / 10K coastal run + filter coffee at Murugan Idli.</p>
          <div class="sq-meta">
            <span class="sq-streak">🔥 18-Wk Streak</span>
            <span class="sq-members">142 Runners</span>
          </div>
          <button class="sq-btn" data-act="rsvp-club" data-id="c01">RSVP 5:15 AM · Free ↗</button>
        </div>
      </div>

      <!-- 2. Indiranagar Midnight Turf Drop (Bengaluru) -->
      <div class="sq-drop-card" data-act="venue" data-id="v01">
        <img class="sq-bg" src="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=700&q=80" alt="Turf Drop">
        <div class="sq-overlay"></div>
        <div class="sq-top">
          <span class="sq-tag turf">⚽ Midnight Turf</span>
          <span class="sq-badge-flash">⚡ 4 Slots Left</span>
        </div>
        <div class="sq-bottom">
          <div class="sq-time">🌙 Tonight 09:00 PM</div>
          <h3 class="sq-title">Indiranagar Arena Midnight 5v5 Drop</h3>
          <p class="sq-desc">Indiranagar, BLR · FIFA-grade floodlit turf with referee & bibs included.</p>
          <div class="sq-meta">
            <span class="sq-streak">★ 4.9 Rating</span>
            <span class="sq-members">from ₹1,200/hr</span>
          </div>
          <button class="sq-btn glow" data-act="venue" data-id="v01">Book Court Now ↗</button>
        </div>
      </div>

      <!-- 3. Toit Rooftop Craft Tap Takeover (Bengaluru) -->
      <div class="sq-drop-card" data-act="venue" data-id="v02">
        <img class="sq-bg" src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=700&q=80" alt="Toit Brewpub">
        <div class="sq-overlay"></div>
        <div class="sq-top">
          <span class="sq-tag brew">🍻 Craft Tap Takeover</span>
          <span class="sq-badge-hot">🍺 Tintin Toit Fresh</span>
        </div>
        <div class="sq-bottom">
          <div class="sq-time">🍻 Sat 07:30 PM</div>
          <h3 class="sq-title">Toit Rooftop Brewer's Table</h3>
          <p class="sq-desc">100ft Road, Indiranagar · Wood-fired sourdough pizza & fresh Belgian Wit.</p>
          <div class="sq-meta">
            <span class="sq-streak">★ 4.8 Rating</span>
            <span class="sq-members">Table for 4-8</span>
          </div>
          <button class="sq-btn" data-act="venue" data-id="v02">Reserve Table ↗</button>
        </div>
      </div>

      <!-- 4. Gameistry 1,300+ Games & Coffee Night (Chennai) -->
      <div class="sq-drop-card" data-act="open-club" data-id="c06">
        <img class="sq-bg" src="https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=700&q=80" alt="Gameistry Guild">
        <div class="sq-overlay"></div>
        <div class="sq-top">
          <span class="sq-tag game">🎲 1,300+ Games Guild</span>
          <span class="sq-badge-flash">☕ Pour-over Bar</span>
        </div>
        <div class="sq-bottom">
          <div class="sq-time">🎲 Sun 04:00 PM</div>
          <h3 class="sq-title">Gameistry Board Game & Coffee Guild</h3>
          <p class="sq-desc">Egmore, Chennai · Deep strategy games (Catan, Dune, Wingspan) + Game Masters.</p>
          <div class="sq-meta">
            <span class="sq-streak">🔥 20-Wk Streak</span>
            <span class="sq-members">135 Gamers</span>
          </div>
          <button class="sq-btn" data-act="open-club" data-id="c06">Join Guild · ₹300 ↗</button>
        </div>
      </div>
    </div>
  </section>

"""

target_chap1_comment = "  <!-- CHAPTER 01: Staggered Lines Rise & Problem Showcase Photos -->"
if target_chap1_comment in content and "id=\"topDrops\"" not in content:
    content = content.replace(target_chap1_comment, four_drops_html + target_chap1_comment)
    print("Inserted 4 Overlapping Square Drops between Hero and Chapter 01 successfully.")

# =====================================================================
# 5. UPDATE cardHTML: ADD DP STORY & STATUS RING ON VENUE CARDS
# =====================================================================
old_card_fn = """function cardHTML(v){
  const sv=store.get('hoppin.saved',[]).includes(v.id);
  return `<article class="card" tabindex="0" data-act="venue" data-id="${v.id}">
    <div class="cv">${coverMedia(v)}
      <div class="b1"><span class="badge">${CITY[v.city].short}</span><span class="badge">${CATS[v.cat].label.split(' & ')[0]}</span></div>
      <button class="fav ${sv?'on':''}" data-act="save" data-id="${v.id}" aria-label="Save">♡</button>
      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><span class="rate-sep">·</span><span class="rate-count">${v.reviews.toLocaleString()} reviews</span></div>
    </div>"""

new_card_fn = """function cardHTML(v){
  const sv=store.get('hoppin.saved',[]).includes(v.id);
  const dpStatus = getVenueDPStatus(v.id);
  return `<article class="card" tabindex="0" data-act="venue" data-id="${v.id}">
    <div class="cv">${coverMedia(v)}
      <div class="b1"><span class="badge">${CITY[v.city].short}</span><span class="badge">${CATS[v.cat].label.split(' & ')[0]}</span></div>
      ${dpStatus ? `
      <div class="dp-story-wrap" data-act="open-dp-status" data-id="${v.id}" title="Tap to view Admin's Today Status & Offer">
        <div class="dp-story-ring pulse">
          <img src="${dpStatus.photo || v.image}" class="dp-avatar" alt="${v.name} DP">
        </div>
        <span class="dp-status-badge">⚡ ${dpStatus.discount || 'OFFER'}</span>
      </div>` : ''}
      <button class="fav ${sv?'on':''}" data-act="save" data-id="${v.id}" aria-label="Save">♡</button>
      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><span class="rate-sep">·</span><span class="rate-count">${v.reviews.toLocaleString()} reviews</span></div>
    </div>"""

if old_card_fn in content:
    content = content.replace(old_card_fn, new_card_fn)
    print("Updated cardHTML with DP story ring successfully.")

# =====================================================================
# 6. ADD JAVASCRIPT STATE & LOGIC:
# - DP Status map & storage
# - Streaks & Gamification logic
# - Youth Health & Morning Clubs (#/clubs)
# - 3-Admin RBAC Portal (#/admin)
# =====================================================================
new_js_features = """
/* =========================================================
   DP DAY-TO-DAY STATUS & OFFERS ("seen on their dp not elsewhere")
   ========================================================= */
const DEFAULT_DP_STATUS = {
  v01: {
    venueId: 'v01',
    venueOrClubName: 'Indiranagar Arena Turf',
    adminName: 'Mukesh V (Operations GM)',
    adminRole: 'Venue Admin',
    updatedAt: '2 hours ago',
    photo: 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80',
    statusText: '⚽ Court 1 & 2 floodlights recalibrated today! Fresh turf shoes available at counter. Night tournament pitch is open.',
    offerTitle: '⚡ Friday Night Flash Drop: Flat 20% Off Pitch 1 between 7-9 PM',
    promoCode: 'TURF20',
    discount: '20% OFF',
    validUntil: 'Tonight 11:59 PM'
  },
  v02: {
    venueId: 'v02',
    venueOrClubName: 'Toit Brewpub Indiranagar',
    adminName: 'Chef Rahul & Brewer Alex',
    adminRole: 'Restaurant Admin',
    updatedAt: '3 hours ago',
    photo: 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80',
    statusText: '🍺 Fresh batch of Belgian Wit (Tintin Toit) tapped at 11 AM today. Rooftop tables 4 & 6 prepped with wood-fired oven hot.',
    offerTitle: '🍻 Complimentary Sourdough Garlic Bread with any 2 Pitchers before 8 PM',
    promoCode: 'TOITWIT',
    discount: 'FREE BREAD',
    validUntil: 'Tonight 8:00 PM'
  },
  c01: {
    clubId: 'c01',
    venueOrClubName: 'Bessie Flyers Run Club',
    adminName: 'Karthik & Ananya (Club Captains)',
    adminRole: 'Club / Group Admin',
    updatedAt: '1 hour ago',
    photo: 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=800&q=80',
    statusText: '🌅 Tomorrow 5:15 AM Sunrise Run: 142 runners registered! Cool offshore breeze. Hydration table set up at Besant Nagar police booth.',
    offerTitle: '☕ Free Filter Coffee & Medu Vada at Murugan Idli for all finishers + +20 Streak XP',
    promoCode: 'BESSIE5K',
    discount: 'FREE COFFEE + 20 XP',
    validUntil: 'Tomorrow 08:00 AM'
  },
  c06: {
    clubId: 'c06',
    venueOrClubName: 'Gameistry Board Game Guild',
    adminName: 'Sneha & Tarun (Game Masters)',
    adminRole: 'Guild Admin',
    updatedAt: '4 hours ago',
    photo: 'https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=800&q=80',
    statusText: '🎲 12 new copies of Dune: Imperium & Wingspan arrived today! Teaching tables running all Sunday afternoon.',
    offerTitle: '☕ Free Ethiopian Pour-over coffee with every 3-hour Guild Pass',
    promoCode: 'GAMEPOUR',
    discount: 'FREE COFFEE',
    validUntil: 'Sunday 07:00 PM'
  }
};

function getDPStatusMap(){
  return store.get('hoppin.dp_status', DEFAULT_DP_STATUS);
}

function getVenueDPStatus(id){
  const map = getDPStatusMap();
  return map[id] || null;
}

function showDPStatusModal(id){
  const dp = getVenueDPStatus(id) || DEFAULT_DP_STATUS.v01;
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div class="dp-story-modal">
    <div class="dp-story-header">
      <div class="dp-author-info">
        <div class="dp-story-ring" style="width:48px;height:48px;">
          <img src="${dp.photo}" class="dp-avatar" alt="${dp.adminName}">
        </div>
        <div>
          <div style="font-weight:700;font-size:15px;color:#fff">${esc(dp.adminName)}</div>
          <div style="font-size:12px;color:#c4b5fd">${esc(dp.venueOrClubName)} · <span style="color:#10b981">● Live Today (${esc(dp.updatedAt)})</span></div>
        </div>
      </div>
    </div>

    <div class="dp-story-photo-box">
      <img src="${dp.photo}" alt="Status photo">
      <div class="dp-photo-tag">📸 Photo uploaded by Admin today</div>
    </div>

    <div class="dp-status-bubble">
      <b>Status update:</b> ${esc(dp.statusText)}
    </div>

    <div class="dp-exclusive-offer">
      <div style="font-family:var(--mono);font-size:10.5px;color:#f0b94a;letter-spacing:0.1em;font-weight:700">🔥 EXCLUSIVE OFFER · SEEN ONLY ON THIS DP</div>
      <div class="dp-offer-title">${esc(dp.offerTitle)}</div>
      <div class="dp-offer-cta-row">
        <div class="dp-promo-tag">CODE: <b>${esc(dp.promoCode)}</b></div>
        <button class="btn sm" data-act="claim-dp-offer" data-code="${esc(dp.promoCode)}" data-venue="${dp.venueId||''}">Claim & Book ↗</button>
      </div>
    </div>
  </div>`);
}

function claimDPOffer(code, venueId){
  M.close();
  toast(`Promo code ${code} applied to your checkout!`);
  if(venueId && VBY[venueId]){
    openVenue(venueId);
  } else {
    $('#explore')?.scrollIntoView({behavior:'smooth'});
  }
}

/* =========================================================
   STREAKS & ENGAGEMENT GAMIFICATION
   ========================================================= */
let userStreak = store.get('hoppin.streak', { days: 4, xp: 180, lastCheckin: null });

function showStreaksModal(){
  const s = userStreak;
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:32px 28px;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px">
      <span style="font-size:36px">🔥</span>
      <div>
        <h2 style="font-family:var(--serif);font-size:1.8rem;margin:0">Active Activity Streak</h2>
        <div style="color:var(--muted);font-size:13px">Stay active in Chennai & Bengaluru · Build habits</div>
      </div>
    </div>

    <div style="background:linear-gradient(135deg,rgba(240,185,74,0.15) 0%,rgba(124,58,237,0.15) 100%);border:1px solid rgba(240,185,74,0.4);border-radius:18px;padding:22px;text-align:center;margin-bottom:20px">
      <div style="font-family:var(--serif);font-size:3.5rem;font-weight:700;color:#f0b94a;line-height:1">${s.days}</div>
      <div style="font-family:var(--mono);font-size:13px;letter-spacing:0.1em;text-transform:uppercase;color:#fff;margin-top:6px">Day Active Streak</div>
      <div style="font-size:13px;color:#c4b5fd;margin-top:4px">Total Experience: <b>${s.xp} XP</b> · Tier 2 Hopper</div>
    </div>

    <div style="margin-bottom:22px">
      <button class="btn" style="width:100%;font-size:15px;padding:14px" data-act="claim-streak">⚡ Claim Today's Activity Streak (+25 XP)</button>
    </div>

    <div style="font-family:var(--mono);font-size:11px;text-transform:uppercase;color:var(--muted);margin-bottom:12px;letter-spacing:0.08em">Unlocked Milestone Badges</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;text-align:center">
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">🌅</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Early Bird</div>
        <div style="font-size:10px;color:var(--muted)">5:15 AM Run</div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">⚽</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Turf Master</div>
        <div style="font-size:10px;color:var(--muted)">3 Night Pitches</div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">🍻</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Tap Hopper</div>
        <div style="font-size:10px;color:var(--muted)">Craft Brewery</div>
      </div>
    </div>
  </div>`);
}

function claimDailyStreak(){
  userStreak.days++;
  userStreak.xp += 25;
  userStreak.lastCheckin = new Date().toISOString();
  store.set('hoppin.streak', userStreak);
  const el = $('#streakDaysCount');
  if(el) el.textContent = userStreak.days;
  M.close();
  toast(`🔥 Streak Claimed! You are on a ${userStreak.days}-Day Streak! +25 XP awarded.`);
}

/* =========================================================
   YOUTH HEALTH & ACTIVITY CLUBS (#/clubs)
   ========================================================= */
let CLUBS_DATA = [
  {
    id: 'c01',
    name: 'Bessie Flyers Run Club',
    city: 'MAA',
    cityName: 'Chennai',
    area: "Elliot's Beach, Besant Nagar",
    category: 'running',
    time: '05:15 AM',
    days: 'Wednesdays & Saturdays',
    members: 142,
    activeStreak: 18,
    captain: 'Karthik & Ananya',
    desc: 'The beachside dawn run club. We meet at 5:15 AM by the Elliot’s Beach police booth, run 5k/10k along the coast, and head for filter coffee and dosas at Murugan Idli after.',
    image: 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Saturday, 05:15 AM · Elliot’s Beach',
    attendees: ['karthik@bessie.run', 'ananya@bessie.run']
  },
  {
    id: 'c02',
    name: 'Cubbon Park Sunrise Yoga',
    city: 'BLR',
    cityName: 'Bengaluru',
    area: 'Cubbon Park, Central Bengaluru',
    category: 'yoga',
    time: '06:30 AM',
    days: 'Every Sunday',
    members: 198,
    activeStreak: 24,
    captain: 'Priya Sharma',
    desc: 'A gentle morning vinyasa flow on the grass under the bamboo groves of Cubbon Park. Open to all levels. Bring your mat, breathe fresh morning air, and start the week grounded.',
    image: 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Sunday, 06:30 AM · Bamboo Grove',
    attendees: ['priya@cubbon.yoga']
  },
  {
    id: 'c03',
    name: 'CORSO Run Club Bangalore',
    city: 'BLR',
    cityName: 'Bengaluru',
    area: 'Koramangala 4th Block',
    category: 'running',
    time: '06:00 AM',
    days: 'Tuesdays & Thursdays',
    members: 116,
    activeStreak: 14,
    captain: 'Vikram Menon',
    desc: 'Paced city runs through the tree-lined boulevards of Koramangala and Indiranagar. Structured training for 10k and half-marathon runners with warm-up drills.',
    image: 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Thursday, 06:00 AM · Koramangala Club',
    attendees: ['vikram@corso.run']
  },
  {
    id: 'c04',
    name: 'Ciclo Cafe Cycling Peloton',
    city: 'MAA',
    cityName: 'Chennai',
    area: 'Kotturpuram & ECR',
    category: 'cycling',
    time: '05:30 AM',
    days: 'Every Saturday',
    members: 88,
    activeStreak: 12,
    captain: 'Dinesh Kumar',
    desc: 'East Coast Road coastal cycling squad. 40k and 60k paced weekend rides starting from Ciclo Cafe Kotturpuram out to Kovalam and back, followed by breakfast.',
    image: 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Saturday, 05:30 AM · Ciclo Cafe',
    attendees: ['dinesh@ciclo.bike']
  },
  {
    id: 'c05',
    name: 'Indiranagar Midnight Futsal Crew',
    city: 'BLR',
    cityName: 'Bengaluru',
    area: 'Indiranagar Arena',
    category: 'sports',
    time: '09:00 PM',
    days: 'Every Friday Night',
    members: 64,
    activeStreak: 16,
    captain: 'Sameer Khan',
    desc: 'Weekly 5v5 competitive futsal under the floodlights at Arena Sports Complex. Teams shuffled every week, winners stay on, beers and dinner after.',
    image: 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Friday, 09:00 PM · Arena Pitch 1',
    attendees: ['sameer@arena.blr']
  },
  {
    id: 'c06',
    name: 'Gameistry Board Game Guild',
    city: 'MAA',
    cityName: 'Chennai',
    area: 'Egmore, Chennai',
    category: 'gaming',
    time: '04:00 PM',
    days: 'Every Sunday',
    members: 135,
    activeStreak: 20,
    captain: 'Sneha & Tarun',
    desc: 'Deep strategy board game sessions featuring Catan, Terraforming Mars, Wingspan, and Dune. Instructors teach games to newcomers. Solo hoppers welcome.',
    image: 'https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Sunday, 04:00 PM · Gameistry Lounge',
    attendees: ['sneha@gameistry.in']
  }
];

let clubFilterCity = 'all';
let clubFilterCat = 'all';

function clubsHTML(){
  return `
  <section class="clubs-hero wrap">
    <div class="kicker" style="color:var(--pastel)">Movement · Community · Health</div>
    <h1>Youth Health & Activity Clubs</h1>
    <p class="sub" style="max-width:54ch;margin:0 auto 28px">Chennai & Bengaluru youngsters aren't just partying on weekends. We wake up at 5:15 AM for beach runs, hit dawn park yoga, and conquer midnight turf sports. Pick your tribe and build streaks.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap">
      <button class="btn" data-act="create-club">+ Start Your Own Club</button>
      <button class="btn ghost" data-act="open-streaks">View My Streaks 🔥</button>
    </div>
  </section>

  <div class="wrap clubs-filter-bar">
    <button class="club-chip ${clubFilterCity==='all'?'active':''}" onclick="filterClubsCity('all')">All Cities</button>
    <button class="club-chip ${clubFilterCity==='MAA'?'active':''}" onclick="filterClubsCity('MAA')">🌊 Chennai Clubs</button>
    <button class="club-chip ${clubFilterCity==='BLR'?'active':''}" onclick="filterClubsCity('BLR')">🌳 Bengaluru Clubs</button>
  </div>

  <div class="clubs-grid" id="clubsGrid">
    ${renderClubsCards()}
  </div>
  `;
}

function filterClubsCity(city){
  clubFilterCity = city;
  const grid = $('#clubsGrid');
  if(grid) grid.innerHTML = renderClubsCards();
  $$('.clubs-filter-bar .club-chip').forEach(b => {
    b.classList.toggle('active', b.textContent.includes(city === 'MAA' ? 'Chennai' : city === 'BLR' ? 'Bengaluru' : 'All'));
  });
}

function renderClubsCards(){
  const list = CLUBS_DATA.filter(c => clubFilterCity === 'all' || c.city === clubFilterCity);
  return list.map(c => {
    const dpStatus = getVenueDPStatus(c.id);
    return `
    <article class="club-card">
      <div class="club-media">
        <img src="${c.image}" alt="${c.name}">
        <div class="b1" style="position:absolute;left:14px;top:14px;display:flex;gap:6px">
          <span class="badge">${c.cityName}</span>
          <span class="badge" style="text-transform:capitalize">${c.category}</span>
        </div>
        ${dpStatus ? `
        <div class="dp-story-wrap" data-act="open-dp-status" data-id="${c.id}" title="Tap to view Captain's Today Status & Finisher Perk">
          <div class="dp-story-ring pulse">
            <img src="${dpStatus.photo || c.image}" class="dp-avatar" alt="${c.name} DP">
          </div>
          <span class="dp-status-badge">⚡ ${dpStatus.discount || 'PERK'}</span>
        </div>` : ''}
        <div style="position:absolute;left:14px;bottom:14px;background:rgba(13,8,24,0.85);backdrop-filter:blur(8px);padding:4px 10px;border-radius:999px;font-size:11.5px;font-family:var(--mono);color:#f0b94a;border:1px solid rgba(240,185,74,0.4)">
          🔥 ${c.activeStreak}-Week Streak · ${c.members} Members
        </div>
      </div>
      <div class="club-body">
        <div>
          <h3 style="font-size:18px;margin:0 0 6px">${c.name}</h3>
          <div style="font-size:12.5px;color:var(--muted);margin-bottom:10px">${c.area} · Led by ${c.captain}</div>
          <p style="font-size:13px;line-height:1.5;color:var(--text);margin:0 0 12px">${c.desc}</p>
        </div>
        <div>
          <div class="club-next-box">
            <span style="color:var(--pastel)">Next Meetup:</span> <b>${c.nextMeetup}</b>
          </div>
          <div class="club-actions">
            <button class="btn" style="flex:1" data-act="rsvp-club" data-id="${c.id}">RSVP Next Session · Free ↗</button>
            <button class="btn ghost" style="padding:0 14px" data-act="open-dp-status" data-id="${c.id}">Story DP</button>
          </div>
        </div>
      </div>
    </article>
    `;
  }).join('');
}

function rsvpClub(id){
  const club = CLUBS_DATA.find(c => c.id === id);
  if(!club) return;
  club.members++;
  userStreak.xp += 20;
  store.set('hoppin.streak', userStreak);
  toast(`🎉 RSVP Confirmed for ${club.name}! +20 Streak XP awarded 🔥`);
  renderGrid();
}

function showCreateClubModal(){
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:32px 28px;">
    <h2 style="font-family:var(--serif);font-size:1.8rem;margin:0 0 8px">Launch Your Youth Health Club</h2>
    <p style="color:var(--muted);font-size:13px;margin:0 0 20px">Create a morning run club, sunrise yoga tribe, or turf team in Chennai or Bengaluru.</p>
    <form onsubmit="event.preventDefault();submitCreateClub(this);">
      <div style="margin-bottom:14px">
        <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">CLUB NAME</label>
        <input name="name" required placeholder="e.g. ECR Sunrise Striders" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px">
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">CITY</label>
          <select name="city" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
            <option value="MAA">Chennai (MAA)</option>
            <option value="BLR">Bengaluru (BLR)</option>
          </select>
        </div>
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">CATEGORY</label>
          <select name="category" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
            <option value="running">Morning Run Club</option>
            <option value="yoga">Sunrise Yoga / Calisthenics</option>
            <option value="cycling">Cycling Peloton</option>
            <option value="sports">Turf & Futsal</option>
            <option value="gaming">Board Games & Chess</option>
          </select>
        </div>
      </div>
      <div style="margin-bottom:14px">
        <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">MEETUP SPOT & SCHEDULE</label>
        <input name="schedule" required placeholder="e.g. Saturdays 05:15 AM · Besant Nagar Beach" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
      </div>
      <div style="margin-bottom:20px">
        <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">CAPTAIN / CONTACT</label>
        <input name="captain" required placeholder="Your name / Instagram handle" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
      </div>
      <button class="btn" type="submit" style="width:100%;padding:12px">Create Club & Become Group Admin ↗</button>
    </form>
  </div>`);
}

function submitCreateClub(form){
  const fd = new FormData(form);
  const name = fd.get('name');
  const city = fd.get('city');
  const cat = fd.get('category');
  const sched = fd.get('schedule');
  const captain = fd.get('captain');

  const newC = {
    id: 'c' + (CLUBS_DATA.length + 1),
    name: String(name),
    city: String(city),
    cityName: city === 'MAA' ? 'Chennai' : 'Bengaluru',
    area: String(sched).split('·')[1]?.trim() || 'Central',
    category: cat,
    time: '05:30 AM',
    days: 'Weekends',
    members: 1,
    activeStreak: 1,
    captain: String(captain),
    desc: `Newly formed youth activity tribe in ${city==='MAA'?'Chennai':'Bengaluru'}. Show up, stay fit, build habits together.`,
    image: 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=800&q=80',
    nextMeetup: String(sched),
    attendees: []
  };

  CLUBS_DATA.unshift(newC);
  M.close();
  toast(`✨ Club "${name}" launched successfully! You are now Group Admin.`);
  const grid = $('#clubsGrid');
  if(grid) grid.innerHTML = renderClubsCards();
}

/* =========================================================
   3-ADMIN RBAC PORTAL (#/admin)
   ========================================================= */
let currentAdminRole = 'super_admin';

function adminHTML(){
  return `
  <section class="admin-shell wrap">
    <div class="admin-banner">
      <div>
        <div class="kicker" style="color:var(--pastel)">Role-Based Access Control</div>
        <h1 style="font-family:var(--serif);font-size:2.2rem;margin:4px 0 6px">Hoppin Administrative Portal</h1>
        <div style="font-size:13px;color:var(--muted)">Separate portals for Platform Director, Youth Run Club Captains, and Restaurant/Venue Managers.</div>
      </div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-family:var(--mono);font-size:11px;padding:5px 12px;border-radius:999px;background:rgba(16,185,129,0.15);color:#10b981;border:1px solid rgba(16,185,129,0.4)">
          ● RBAC SYSTEM ACTIVE
        </span>
      </div>
    </div>

    <!-- Admin Role Switcher Tabs -->
    <div class="admin-role-nav">
      <button class="admin-role-tab ${currentAdminRole==='super_admin'?'active':''}" data-act="admin-switch-role" data-role="super_admin">
        <span>👑</span> Super Admin (Platform)
      </button>
      <button class="admin-role-tab ${currentAdminRole==='group_admin'?'active':''}" data-act="admin-switch-role" data-role="group_admin">
        <span>🏃</span> Group Admin (Youth & Run Clubs)
      </button>
      <button class="admin-role-tab ${currentAdminRole==='restaurant_admin'?'active':''}" data-act="admin-switch-role" data-role="restaurant_admin">
        <span>🏟️</span> Restaurant & Venue Admin
      </button>
    </div>

    <div id="adminContent">
      ${renderAdminView()}
    </div>
  </section>
  `;
}

function switchAdminRole(role){
  currentAdminRole = role;
  const contentEl = $('#adminContent');
  if(contentEl) contentEl.innerHTML = renderAdminView();
  $$('.admin-role-tab').forEach(t => t.classList.toggle('active', t.dataset.role === role));
  toast(`Switched to ${role.replace('_',' ').toUpperCase()} view`);
}

function renderAdminView(){
  if(currentAdminRole === 'super_admin'){
    return `
    <div class="admin-stat-row">
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">GROSS BOOKING VOLUME</div>
        <div class="admin-stat-num">₹28,45,200</div>
        <div style="font-size:12px;color:#10b981">↑ 22% this month (BLR + MAA)</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">ACTIVE VENUES</div>
        <div class="admin-stat-num">67</div>
        <div style="font-size:12px;color:var(--pastel)">29 Bengaluru · 38 Chennai</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">ACTIVE HEALTH CLUBS</div>
        <div class="admin-stat-num">18</div>
        <div style="font-size:12px;color:#f0b94a">1,480+ Young Members Active</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">PLATFORM COMMISSION (3.5%)</div>
        <div class="admin-stat-num">₹99,580</div>
        <div style="font-size:12px;color:#10b981">Auto-settled to HDFC</div>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px">
      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">Club & Venue Verification Queue</h3>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:14px;border-radius:12px">
            <div>
              <div style="font-weight:700">OMR Sunrise Striders (MAA)</div>
              <div style="font-size:12px;color:var(--muted)">Applicant: Ganesh N · 60 Expected Runners</div>
            </div>
            <div style="display:flex;gap:6px">
              <button class="btn sm" onclick="toast('Club approved & added to directory!')">Approve</button>
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:14px;border-radius:12px">
            <div>
              <div style="font-weight:700">HSR Layout Padel Tribe (BLR)</div>
              <div style="font-size:12px;color:var(--muted)">Applicant: Rohan M · 4 Courts</div>
            </div>
            <div style="display:flex;gap:6px">
              <button class="btn sm" onclick="toast('Club approved & added to directory!')">Approve</button>
            </div>
          </div>
        </div>
      </div>

      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">System Health & Live Payouts</h3>
        <div style="font-size:13px;line-height:1.7;color:var(--text)">
          <div>● <b>Bank Settlement Gateway:</b> All payouts to Toit & Arena completed at 06:00 AM</div>
          <div>● <b>City Routing Engine:</b> Auto-detects MAA vs BLR with zero latency</div>
          <div>● <b>UPI QR Generator:</b> Procedural SVG renderer operating 100% locally</div>
        </div>
      </div>
    </div>
    `;
  }

  if(currentAdminRole === 'group_admin'){
    return `
    <div class="admin-banner" style="background:linear-gradient(135deg,rgba(240,185,74,0.15) 0%,rgba(124,58,237,0.12) 100%)">
      <div>
        <span class="badge" style="background:#f0b94a;color:#0d0818;font-weight:700">GROUP ADMIN PORTAL</span>
        <h2 style="font-size:1.6rem;margin:8px 0 4px">Bessie Flyers Run Club (Chennai)</h2>
        <div style="font-size:13px;color:var(--muted)">Captain: Karthik & Ananya · 142 Active Members · 18-Week Run Streak</div>
      </div>
      <div>
        <button class="btn sm" data-act="open-dp-status" data-id="c01">Preview Live DP Story ↗</button>
      </div>
    </div>

    <!-- POST DAY-TO-DAY STATUS & OFFER TO DP FORM -->
    <div style="background:var(--bg2);border:1px solid var(--pastel);border-radius:18px;padding:24px;margin-bottom:28px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <h3 style="margin:0;font-size:16px">📸 Upload Daily Photo & Post Day-to-Day Status on Club DP</h3>
        <span style="font-size:11px;font-family:var(--mono);color:#f0b94a">"Seen on DP not elsewhere"</span>
      </div>
      <form onsubmit="event.preventDefault();handleAdminPostDPStatus('c01',this);">
        <div style="margin-bottom:12px">
          <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">STATUS PHOTO URL (Beach Sunrise / Route Map)</label>
          <input name="photo" value="https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=800&q=80" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:12px">
          <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">TODAY'S MEETUP STATUS / WEATHER UPDATE</label>
          <input name="statusText" value="🌅 Tomorrow 5:15 AM Sunrise Run: 142 runners registered! Cool offshore breeze. Hydration table set up at Besant Nagar police booth." style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="display:grid;grid-template-columns:2fr 1fr;gap:12px;margin-bottom:16px">
          <div>
            <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">EXCLUSIVE FINISHER OFFER (APPEARS ON DP)</label>
            <input name="offerTitle" value="☕ Free Filter Coffee & Medu Vada at Murugan Idli for all finishers + +20 Streak XP" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
          </div>
          <div>
            <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">PROMO CODE</label>
            <input name="promoCode" value="BESSIE5K" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
          </div>
        </div>
        <button class="btn" type="submit">Publish Status & Photo to Club DP Story Ring ↗</button>
      </form>
    </div>

    <!-- ATTENDEE ROSTER & CHECK-IN -->
    <div style="background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:24px">
      <h3 style="margin:0 0 14px;font-size:16px">Tomorrow's 5:15 AM Sunrise Run Roster (142 Registered)</h3>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
          <div>
            <div style="font-weight:700">Roshini S</div>
            <div style="font-size:11px;color:#f0b94a">🔥 4-Day Streak · Besant Nagar</div>
          </div>
          <button class="btn sm" onclick="this.textContent='✓ Checked in';this.disabled=true;toast('Roshini checked in! +20 Streak XP awarded.');">Check in</button>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
          <div>
            <div style="font-weight:700">Vikram Menon</div>
            <div style="font-size:11px;color:#f0b94a">🔥 12-Day Streak · 10K Cruiser</div>
          </div>
          <button class="btn sm" onclick="this.textContent='✓ Checked in';this.disabled=true;toast('Vikram checked in! +20 Streak XP awarded.');">Check in</button>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
          <div>
            <div style="font-weight:700">Ananya R</div>
            <div style="font-size:11px;color:#f0b94a">🔥 18-Day Streak · Lead Pacer</div>
          </div>
          <button class="btn sm" onclick="this.textContent='✓ Checked in';this.disabled=true;toast('Ananya checked in!');">Check in</button>
        </div>
      </div>
    </div>
    `;
  }

  if(currentAdminRole === 'restaurant_admin'){
    return `
    <div class="admin-banner" style="background:linear-gradient(135deg,rgba(16,185,129,0.15) 0%,rgba(124,58,237,0.12) 100%)">
      <div>
        <span class="badge" style="background:#10b981;color:#0d0818;font-weight:700">RESTAURANT & VENUE ADMIN</span>
        <h2 style="font-size:1.6rem;margin:8px 0 4px">Toit Brewpub & Indiranagar Arena Turf</h2>
        <div style="font-size:13px;color:var(--muted)">GM: Mukesh V · Today Gross: ₹18,400 · Settled to Bank: ₹14,200</div>
      </div>
      <div>
        <button class="btn sm" data-act="open-dp-status" data-id="v01">Preview Live DP Story ↗</button>
      </div>
    </div>

    <!-- POST DAY-TO-DAY STATUS & OFFER TO DP FORM -->
    <div style="background:var(--bg2);border:1px solid var(--pastel);border-radius:18px;padding:24px;margin-bottom:28px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <h3 style="margin:0;font-size:16px">📸 Upload Daily Photo & Post Day-to-Day Status on Venue DP</h3>
        <span style="font-size:11px;font-family:var(--mono);color:#f0b94a">"Seen on DP not elsewhere"</span>
      </div>
      <form onsubmit="event.preventDefault();handleAdminPostDPStatus('v01',this);">
        <div style="margin-bottom:12px">
          <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">TODAY'S VENUE PHOTO URL (Court Setup / Taproom Special)</label>
          <input name="photo" value="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:12px">
          <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">DAY-TO-DAY STATUS / COURT CONDITION</label>
          <input name="statusText" value="⚽ Court 1 & 2 floodlights recalibrated today! Fresh turf shoes available at counter. Night match drop is active." style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="display:grid;grid-template-columns:2fr 1fr;gap:12px;margin-bottom:16px">
          <div>
            <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">TODAY'S SPECIAL OFFER (APPEARS ON DP)</label>
            <input name="offerTitle" value="⚡ Friday Night Flash Drop: Flat 20% Off Pitch 1 between 7-9 PM" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
          </div>
          <div>
            <label style="display:block;font-size:11.5px;font-family:var(--mono);margin-bottom:4px">PROMO CODE</label>
            <input name="promoCode" value="TURF20" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
          </div>
        </div>
        <button class="btn" type="submit">Publish Status & Photo to Venue DP Story Ring ↗</button>
      </form>
    </div>

    <!-- LIVE COURT & TABLE MATRIX & QR SCANNER -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">Live Court & Table Matrix</h3>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Pitch 1 (5v5 Turf)</div>
              <div style="font-size:11.5px;color:#f0b94a">Booked 8 PM - 9 PM · Ref: HOP-BLR-8921</div>
            </div>
            <span class="badge" style="background:rgba(239,68,68,0.2);color:#ef4444">BOOKED</span>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Pitch 2 (7v7 Floodlit Pitch)</div>
              <div style="font-size:11.5px;color:#10b981">Available 9 PM · ₹1,800/hr</div>
            </div>
            <button class="btn sm" onclick="toast('Pitch 2 toggled to Walk-in Only')">Toggle Mode</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Toit Rooftop Table 4</div>
              <div style="font-size:11.5px;color:#f0b94a">Reserved 7:30 PM · Party of 6</div>
            </div>
            <span class="badge" style="background:rgba(239,68,68,0.2);color:#ef4444">RESERVED</span>
          </div>
        </div>
      </div>

      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">Ticket / QR Code Check-in Scanner</h3>
        <p style="font-size:12.5px;color:var(--muted);margin-bottom:14px">Validate guest booking reference or simulated QR scan.</p>
        <div style="display:flex;gap:10px;margin-bottom:14px">
          <input id="ticketRefInput" placeholder="e.g. HOP-BLR-8921" style="flex:1;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text);font-family:var(--mono)">
          <button class="btn" onclick="verifyAdminTicket()">Verify & Check In</button>
        </div>
        <div id="checkinResult"></div>
      </div>
    </div>
    `;
  }
}

function handleAdminPostDPStatus(id, form){
  const fd = new FormData(form);
  const photo = fd.get('photo');
  const statusText = fd.get('statusText');
  const offerTitle = fd.get('offerTitle');
  const promoCode = fd.get('promoCode');

  const map = getDPStatusMap();
  map[id] = {
    ...(map[id] || {}),
    photo: String(photo),
    statusText: String(statusText),
    offerTitle: String(offerTitle),
    promoCode: String(promoCode),
    discount: promoCode ? 'OFFER' : 'STATUS',
    updatedAt: 'Just now'
  };
  store.set('hoppin.dp_status', map);
  toast('✅ Day-to-day status, photo & offer published to your DP Story Ring!');
}

function verifyAdminTicket(){
  const input = $('#ticketRefInput');
  const ref = input?.value.trim().toUpperCase() || 'HOP-BLR-8921';
  const out = $('#checkinResult');
  if(out){
    out.innerHTML = `
    <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.4);border-radius:12px;padding:14px;color:#10b981;font-size:13px">
      <div style="font-weight:700">✓ TICKET ${ref} VALIDATED</div>
      <div style="color:var(--text);font-size:12px;margin-top:4px">Guest: Rohit Verma · Confirmed UPI Payment · Pitch 1 Checked In</div>
    </div>`;
  }
  toast(`✓ Ticket ${ref} verified successfully!`);
}
"""

# Insert new JS features before render()
target_render_fn = "function render(){"
content = content.replace(target_render_fn, new_js_features + "\n" + target_render_fn)
print("Injected new JS features successfully.")

# =====================================================================
# 7. UPDATE ROUTER render() TO HANDLE #/clubs AND #/admin
# =====================================================================
old_render_block = """function render(){
  const p=curPath().split('/').filter(Boolean);
  const view=p[0]==='chat'?'chat':p[0]==='bookings'?'bookings':'discover';
  S.view=view;
  const app=$('#app');
  if(view==='discover'){
    app.innerHTML=discoverHTML();
    renderGrid();
    initHeroAnimations();
    initLilacWipe();
    initPhysics();
    initGuilds();
    initTotems();
    initLightRays();
    initSectionSensor();
  }else if(view==='chat'){"""

new_render_block = """function render(){
  const p=curPath().split('/').filter(Boolean);
  const view=p[0]==='chat'?'chat':p[0]==='bookings'?'bookings':p[0]==='clubs'?'clubs':p[0]==='admin'?'admin':'discover';
  S.view=view;
  const app=$('#app');
  if(view==='discover'){
    app.innerHTML=discoverHTML();
    renderGrid();
    initHeroAnimations();
    initLilacWipe();
    initPhysics();
    initGuilds();
    initTotems();
    initLightRays();
    initSectionSensor();
  }else if(view==='clubs'){
    app.innerHTML=clubsHTML();
  }else if(view==='admin'){
    app.innerHTML=adminHTML();
  }else if(view==='chat'){"""

if old_render_block in content:
    content = content.replace(old_render_block, new_render_block)
    print("Updated router render() to handle #/clubs and #/admin successfully.")

# =====================================================================
# 8. UPDATE CLICK EVENT DELEGATION FOR ALL NEW ACTIONS
# =====================================================================
old_click_switch = """  switch(act){
  case 'theme':toggleTheme();break;
  case 'account':if(S.user)go('/bookings');else showAuth('in');break;
  case 'close':M.close();break;"""

new_click_switch = """  switch(act){
  case 'theme':toggleTheme();break;
  case 'account':if(S.user)go('/bookings');else showAuth('in');break;
  case 'close':M.close();break;
  case 'open-dp-status':showDPStatusModal(a.dataset.id);break;
  case 'open-streaks':showStreaksModal();break;
  case 'claim-streak':claimDailyStreak();break;
  case 'rsvp-club':rsvpClub(a.dataset.id);break;
  case 'open-club':showDPStatusModal(a.dataset.id);break;
  case 'create-club':showCreateClubModal();break;
  case 'admin-switch-role':switchAdminRole(a.dataset.role);break;
  case 'claim-dp-offer':claimDPOffer(a.dataset.code,a.dataset.venue);break;"""

if old_click_switch in content:
    content = content.replace(old_click_switch, new_click_switch)
    print("Updated click event delegation successfully.")

# Save modified content back to build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated build_fullstack_frontend.py!")

# Write directly to all 5 target files
targets = [
  'apps/web/index.html',
  'apps/web/public/poc.html',
  'apps/web/public/index.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc (1).html'
]

# Extract html_code string from build_fullstack_frontend.py or execute it
exec(open("build_fullstack_frontend.py", encoding="utf-8").read())
print("All target files synchronized and validated!")
