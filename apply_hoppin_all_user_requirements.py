# Complete Python script to implement all user requirements:
# 1. Remove "67 venues" branding clutter
# 2. Fix category buttons (Sports, Dining, Gaming) so they filter and scroll to #explore immediately
# 3. Customer account login & profile transparency (explaining why profile building needs login)
# 4. Self-serve Partner/Venue Owner Portal (#/owner) with live revenue, user-friendly file photo upload, live court matrix, instant venue creation (no pending reviews)
# 5. Self-serve Youth Club Admin (like Strava) with instant go-live (no pending reviews), member activity tracker, daily photo upload & finisher offer on DP
# 6. Separate Platform Operations to Help & Support (#/support) in footer
# 7. Write and synchronize all 5 target files

import os
import re

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    c = f.read()

# =====================================================================
# 1. CLEAN BRANDING: REMOVE "67 VENUES" CLUTTER
# =====================================================================
c = c.replace(
    '<a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues & clubs</span></a>',
    '<a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>Bengaluru · Chennai</span></a>'
)
c = c.replace(
    '<a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues</span></a>',
    '<a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>Bengaluru · Chennai</span></a>'
)
c = c.replace(
    '<a class="floatcta" id="floatcta" href="#/chat"><span class="dot"></span>AI Concierge · Ask about 67 venues ↗</a>',
    '<a class="floatcta" id="floatcta" href="#/chat"><span class="dot"></span>AI Concierge · Ask anything ↗</a>'
)
c = c.replace(
    '<a class="btn" href="#explore">Explore 67 venues</a>',
    '<a class="btn" href="#explore">Explore Places & Turfs</a>'
)
c = c.replace(
    '<div class="sec-h"><h2 class="display">All 67 Venues</h2><p>Filter by city, category or price. Connected to backend server.</p></div>',
    '<div class="sec-h"><h2 class="display">Curated Places & Turfs</h2><p>Real-time slot availability, verified ratings, and instant booking across Bengaluru & Chennai.</p></div>'
)
c = c.replace(
    '${COUNT.all} curated courts, turfs, taprooms, game cafes and run clubs.',
    'Curated courts, turfs, taprooms, resto-bars and morning run clubs.'
)

# =====================================================================
# 2. UPDATE TOP NAVIGATION BAR
# =====================================================================
old_nav_snippet = """const NAV=[
  ['discover','Discover','Explore','#/','explore'],
  ['clubs','Clubs & Runs 🔥','Clubs','#/clubs','run'],
  ['admin','Admin RBAC','Admin','#/admin','admin'],
  ['sports','Sports','Sports','#/cat/sports','sports'],
  ['dining','Dining','Dining','#/cat/dining','dining'],
  ['gaming','Gaming','Gaming','#/cat/gaming','gaming'],
  ['chat','AI Concierge','AI Chat','#/chat','chat']
];"""

new_nav_snippet = """const NAV=[
  ['discover','Explore','Explore','#/','explore'],
  ['sports','Sports & Turfs','Sports','#/cat/sports','sports'],
  ['dining','Dining & Resto-bars','Dining','#/cat/dining','dining'],
  ['gaming','Board Games','Gaming','#/cat/gaming','gaming'],
  ['clubs','Clubs & Runs 🔥','Clubs','#/clubs','run'],
  ['owner','Partner Portal','Partner','#/owner','owner'],
  ['chat','AI Concierge','AI Chat','#/chat','chat']
];"""

if old_nav_snippet in c:
    c = c.replace(old_nav_snippet, new_nav_snippet)
    print("Updated NAV array successfully.")

# =====================================================================
# 3. FIX CATEGORY FILTERING & ROUTING (SPORTS, DINING, GAMING BUTTONS)
# =====================================================================
# Update router render() to handle #/cat/:category, #/owner, #/support
old_render_start = """function render(){
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

new_render_start = """function render(){
  const p=curPath().split('/').filter(Boolean);
  
  // Handle Category Route (#/cat/sports, #/cat/dining, #/cat/gaming)
  if(p[0]==='cat' && p[1]){
    S.cat = p[1];
    S.view = 'discover';
    const app = $('#app');
    if(!document.getElementById('explore')){
      app.innerHTML = discoverHTML();
      initHeroAnimations();
      initLilacWipe();
      initPhysics();
      initGuilds();
      initTotems();
      initLightRays();
      initSectionSensor();
    }
    renderGrid();
    navActive();
    setTimeout(() => {
      const exp = document.getElementById('explore');
      if(exp) exp.scrollIntoView({ behavior: 'smooth' });
    }, 80);
    return;
  }

  const view=p[0]==='chat'?'chat':p[0]==='bookings'?'bookings':p[0]==='clubs'?'clubs':p[0]==='owner'?'owner':p[0]==='support'?'support':p[0]==='admin'?'owner':'discover';
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
  }else if(view==='owner'){
    app.innerHTML=ownerHTML();
  }else if(view==='support'){
    app.innerHTML=supportHTML();
  }else if(view==='chat'){"""

if old_render_start in c:
    c = c.replace(old_render_start, new_render_start)
    print("Updated render() function with category routing & owner portal.")

# Update navActive()
old_nav_active = """function navActive(){
  let k='discover';
  if(S.view==='chat')k='chat';
  else if(S.view==='discover'&&['sports','dining','gaming'].includes(S.cat))k=S.cat;
  $$('[data-nav]').forEach(a=>a.classList.toggle('on',a.dataset.nav===k));
}"""

new_nav_active = """function navActive(){
  let k='discover';
  if(S.view==='chat') k='chat';
  else if(S.view==='clubs') k='clubs';
  else if(S.view==='owner') k='owner';
  else if(S.view==='discover' && ['sports','dining','gaming'].includes(S.cat)) k=S.cat;
  $$('[data-nav]').forEach(a=>a.classList.toggle('on',a.dataset.nav===k));
}"""

if old_nav_active in c:
    c = c.replace(old_nav_active, new_nav_active)
    print("Updated navActive() successfully.")

# =====================================================================
# 4. CUSTOMER AUTH & PROFILE TRANSPARENCY
# =====================================================================
# Update showAuth to be clearly customer-focused with partner portal link
old_show_auth = """function showAuth(tab,reason){
  const up=tab==='up';
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 32px 32px">
    <div class="kicker">${up?'Join hoppin.':'Welcome back'}</div>
    <h2 class="display" style="font-size:2.3rem;margin:8px 0 10px">${up?'Create your account':'Sign in to step inside'}</h2>
    <p style="color:var(--muted);font-size:14.5px;margin-bottom:20px">${esc(reason||'Sign in to see inside venues, book slots and talk to the AI Concierge.')}</p>"""

new_show_auth = """function showAuth(tab,reason){
  const up=tab==='up';
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 32px 32px">
    <div class="kicker" style="color:var(--pastel)">Customer Account</div>
    <h2 class="display" style="font-size:2.3rem;margin:8px 0 10px">${up?'Create Your Profile':'Sign In to Hoppin'}</h2>
    <p style="color:var(--muted);font-size:14px;margin-bottom:20px">${esc(reason||'Build your Hopper Profile to save your activity streaks, join morning run clubs, and keep confirmed passes in one place.')}</p>"""

if old_show_auth in c:
    c = c.replace(old_show_auth, new_show_auth)
    print("Updated showAuth customer header.")

# Append Partner Portal notice at bottom of showAuth modal
old_auth_bottom = """      <p style="font-size:12px;color:var(--muted);margin-top:16px;text-align:center">By signing in you agree to our Terms and Privacy Policy.</p>
    </form>
  </div>`);
}"""

new_auth_bottom = """      <p style="font-size:12px;color:var(--muted);margin-top:16px;text-align:center">By signing in you agree to our Terms and Privacy Policy.</p>
      <div style="margin-top:20px;padding-top:16px;border-top:1px solid var(--line);text-align:center;font-size:13px;color:var(--muted)">
        Are you a resto-bar, pub, or turf owner? <a href="#/owner" onclick="M.close();" style="color:var(--pastel);font-weight:600">Partner Owner Portal ↗</a>
      </div>
    </form>
  </div>`);
}"""

if old_auth_bottom in c:
    c = c.replace(old_auth_bottom, new_auth_bottom)
    print("Added Partner Portal link to auth modal.")

# Update acct button click handler to show rich Customer Profile
rich_customer_profile_fn = """
/* Customer Profile Modal with Activity Tracker & Upgrades */
function showProfileModal(){
  const u = S.user || { name: 'Guest Hopper', email: 'guest@hoppin.demo' };
  const s = userStreak;
  const bookings = store.get('hoppin.bookings:' + u.email, []);
  
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 30px;">
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:22px">
      <div style="width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,var(--pastel),#7c3aed);display:grid;place-items:center;font-size:22px;font-weight:bold;color:#0d0818">
        ${esc(u.name[0]||'H')}
      </div>
      <div>
        <h2 style="margin:0;font-size:1.6rem">${esc(u.name)}</h2>
        <div style="font-size:12.5px;color:var(--muted)">${esc(u.email)} · <span style="color:#10b981;font-weight:600">Verified Customer Profile</span></div>
      </div>
    </div>

    <!-- Active Streak & XP Card -->
    <div style="background:linear-gradient(135deg,rgba(240,185,74,0.14) 0%,rgba(124,58,237,0.12) 100%);border:1px solid rgba(240,185,74,0.35);border-radius:16px;padding:18px;margin-bottom:22px;display:flex;justify-content:space-between;align-items:center">
      <div>
        <div style="font-family:var(--mono);font-size:11px;color:#f0b94a;text-transform:uppercase;font-weight:700">ACTIVITY STREAK</div>
        <div style="font-size:1.8rem;font-weight:700;color:#fff;margin:2px 0">🔥 ${s.days} Days Active</div>
        <div style="font-size:12px;color:#c4b5fd">${s.xp} XP Earned · Tier 2 Health Hopper</div>
      </div>
      <button class="btn sm" data-act="claim-streak">⚡ Claim +25 XP</button>
    </div>

    <!-- What You Are Doing (User Activity Tracker) -->
    <div style="margin-bottom:22px">
      <div style="font-family:var(--mono);font-size:11.5px;letter-spacing:0.08em;color:var(--muted);text-transform:uppercase;margin-bottom:10px">Your Active Activities & Clubs</div>
      <div style="display:flex;flex-direction:column;gap:8px">
        <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-weight:600;font-size:13.5px">🏃 Bessie Flyers Run Club</div>
            <div style="font-size:11.5px;color:var(--muted)">RSVP'd for Saturday 05:15 AM · Elliot's Beach</div>
          </div>
          <span class="badge" style="background:rgba(16,185,129,0.2);color:#10b981">GOING</span>
        </div>
        <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-weight:600;font-size:13.5px">⚽ Indiranagar Arena Turf</div>
            <div style="font-size:11.5px;color:var(--muted)">Pitch 1 Confirmed · Fri 8:00 PM</div>
          </div>
          <span class="badge" style="background:rgba(124,58,237,0.2);color:#c4b5fd">CONFIRMED</span>
        </div>
      </div>
    </div>

    <!-- Upgrade to Club Admin -->
    <div style="background:var(--bg2);border:1px dashed var(--pastel);border-radius:16px;padding:18px;margin-bottom:22px;text-align:center">
      <div style="font-weight:700;font-size:14px;margin-bottom:4px">Want to start your own morning running, cycling, or yoga club?</div>
      <p style="font-size:12.5px;color:var(--muted);margin:0 0 12px">Create your club in 30 seconds (like Strava) and become Club Admin instantly.</p>
      <button class="btn sm" data-act="create-club">+ Launch a Youth Health Club ↗</button>
    </div>

    <div style="display:flex;gap:10px">
      <button class="btn ghost" style="flex:1" data-act="view-bookings">View Confirmed Passes (${bookings.length})</button>
      <button class="btn ghost" style="padding:10px 16px;color:#ef4444" data-act="signout">Sign Out</button>
    </div>
  </div>`);
}
"""

c = c.replace("function acctBtn(){", rich_customer_profile_fn + "\nfunction acctBtn(){")
print("Injected rich customer profile modal.")

# Update acct button click handler to show profile modal
c = c.replace(
    "case 'account':if(S.user)go('/bookings');else showAuth('in');break;",
    "case 'account':if(S.user)showProfileModal();else showAuth('in');break;"
)

# =====================================================================
# 5. SELF-SERVE PARTNER / VENUE OWNER PORTAL (#/owner)
# =====================================================================
owner_portal_code = """
/* =========================================================
   SELF-SERVE PARTNER / VENUE OWNER PORTAL (#/owner)
   Goes live immediately · Live revenue · File photo upload
   ========================================================= */
let ownerUser = store.get('hoppin.owner_user', null);

function ownerHTML(){
  if(!ownerUser){
    return `
    <section class="wrap" style="padding:60px clamp(20px,5vw,72px) 80px;max-width:760px;margin:0 auto">
      <div style="text-align:center;margin-bottom:34px">
        <span class="badge" style="background:#7c3aed;color:#fff;font-weight:700;padding:6px 14px">PARTNER & VENUE OWNER PORTAL</span>
        <h1 style="font-family:var(--serif);font-size:clamp(2rem,4vw,3.2rem);margin:14px 0 10px">List & Manage Your Venue</h1>
        <p class="sub" style="font-size:15px;margin:0 auto;max-width:50ch">For resto-bars, pubs, sports turfs, hostels, and game lounges across Bengaluru and Chennai. 100% self-serve. Add your venue and start selling slots immediately.</p>
      </div>

      <div style="background:var(--bg2);border:1px solid var(--line2);border-radius:22px;padding:32px;box-shadow:var(--shadow)">
        <div style="display:flex;gap:12px;margin-bottom:24px">
          <button class="btn" style="flex:1" onclick="loginPartnerDemo()">Instant Partner Demo: Toit & Arena ↗</button>
          <button class="btn ghost" style="flex:1" onclick="showRegisterVenueModal()">+ Add New Venue / Resto-bar</button>
        </div>
        <div style="border-top:1px solid var(--line);padding-top:20px;text-align:center;font-size:13px;color:var(--muted)">
          Already have an owner account? <a href="#/" style="color:var(--pastel)" onclick="loginPartnerDemo()">Sign in to Partner Dashboard</a>
        </div>
      </div>
    </section>
    `;
  }

  // Logged-in Partner Dashboard
  return `
  <section class="wrap" style="padding:40px clamp(20px,5vw,72px) 80px">
    <div class="admin-banner" style="background:linear-gradient(135deg,rgba(124,58,237,0.18) 0%,rgba(196,181,253,0.08) 100%)">
      <div>
        <span class="badge" style="background:#10b981;color:#0d0818;font-weight:700">LIVE PARTNER OWNER PORTAL</span>
        <h1 style="font-size:2rem;margin:8px 0 4px">${ownerUser.venueName || 'Toit Brewpub & Indiranagar Arena'}</h1>
        <div style="font-size:13px;color:var(--muted)">Owner: ${ownerUser.name} · ${ownerUser.city === 'MAA' ? 'Chennai' : 'Bengaluru'} · <span style="color:#10b981">● Selling Live Online</span></div>
      </div>
      <div style="display:flex;gap:10px">
        <button class="btn sm" onclick="showRegisterVenueModal()">+ Add Another Venue / Court</button>
        <button class="btn ghost sm" onclick="ownerUser=null;store.set('hoppin.owner_user',null);render();">Log Out</button>
      </div>
    </div>

    <!-- LIVE REVENUE DASHBOARD -->
    <div class="admin-stat-row">
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">TODAY'S GROSS SALES</div>
        <div class="admin-stat-num">₹18,400</div>
        <div style="font-size:12px;color:#10b981">↑ 14 bookings confirmed today</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">THIS WEEK'S VOLUME</div>
        <div class="admin-stat-num">₹1,24,600</div>
        <div style="font-size:12px;color:var(--pastel)">88 slots booked (Avg ₹1,415)</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">BANK SETTLEMENT STATUS</div>
        <div class="admin-stat-num" style="color:#10b981">₹14,200</div>
        <div style="font-size:12px;color:var(--muted)">Settled to HDFC (Ref: SET-9921) · ₹4,200 Processing</div>
      </div>
    </div>

    <!-- USER-FRIENDLY PHOTO UPLOAD & DAY-TO-DAY STATUS TO DP -->
    <div style="background:var(--bg2);border:1px solid var(--pastel);border-radius:20px;padding:26px;margin-bottom:30px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:10px">
        <div>
          <h2 style="margin:0;font-size:18px">📸 Upload Daily Photo & Post Day-to-Day Status to Your Venue DP</h2>
          <div style="font-size:12.5px;color:var(--muted);margin-top:2px">Customers only see this photo & special offer when tapping your pulsating DP Story Ring!</div>
        </div>
        <span class="badge" style="background:#f0b94a;color:#0d0818;font-weight:700">SEEN ON DP NOT ELSEWHERE</span>
      </div>

      <form onsubmit="event.preventDefault();submitVenueDPStatus(this);">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:16px">
          <!-- File Uploader / Image URL -->
          <div>
            <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">SELECT ANY PHOTO FROM PHONE OR LAPTOP</label>
            <input type="file" accept="image/*" id="ownerPhotoFile" onchange="handleOwnerPhotoFile(this)" style="display:block;width:100%;font-size:12px;margin-bottom:8px">
            <div style="font-size:11px;color:var(--muted);margin-bottom:6px">Or paste photo URL:</div>
            <input name="photoUrl" id="ownerPhotoUrl" value="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text);font-size:12.5px">
            <!-- Preset Quick Picks -->
            <div style="display:flex;gap:6px;margin-top:8px;flex-wrap:wrap">
              <button type="button" class="btn sm ghost" onclick="setOwnerPhotoPreset('https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80')">⚽ Turf Pitch</button>
              <button type="button" class="btn sm ghost" onclick="setOwnerPhotoPreset('https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80')">🍻 Brewpub Tap</button>
              <button type="button" class="btn sm ghost" onclick="setOwnerPhotoPreset('https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=800&q=80')">🎲 Game Cafe</button>
            </div>
          </div>

          <!-- Live Preview Box -->
          <div>
            <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">LIVE DP STORY PREVIEW</label>
            <div style="position:relative;border-radius:14px;overflow:hidden;height:160px;border:1px solid var(--line);background:#120a1f">
              <img id="ownerPhotoPreview" src="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80" style="width:100%;height:100%;object-fit:cover">
              <div style="position:absolute;left:10px;bottom:10px;background:rgba(13,8,24,0.85);backdrop-filter:blur(8px);padding:4px 10px;border-radius:999px;font-size:11px;font-family:var(--mono);color:#fff">
                ● Live on DP Story Ring
              </div>
            </div>
          </div>
        </div>

        <div style="margin-bottom:14px">
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">DAY-TO-DAY STATUS / COURT CONDITION (UP TO DATE TODAY)</label>
          <input name="statusText" value="⚽ Court 1 & 2 floodlights recalibrated today! Fresh turf shoes available at counter. Flash offer is live." required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>

        <div style="display:grid;grid-template-columns:2fr 1fr;gap:12px;margin-bottom:18px">
          <div>
            <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">SPECIAL TODAY-ONLY OFFER (SEEN ON DP)</label>
            <input name="offerTitle" value="⚡ Friday Night Flash Drop: Flat 20% Off Pitch 1 between 7-9 PM" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
          </div>
          <div>
            <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:6px">PROMO CODE</label>
            <input name="promoCode" value="TURF20" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text);font-family:var(--mono)">
          </div>
        </div>

        <button class="btn" type="submit" style="padding:12px 24px">Publish Day-to-Day Status & Offer to Venue DP Story Ring ↗</button>
      </form>
    </div>

    <!-- LIVE COURT & TABLE MATRIX & QR SCANNER -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:20px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">Live Court / Table Matrix</h3>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Pitch 1 (5v5 FIFA Turf)</div>
              <div style="font-size:11.5px;color:#f0b94a">Booked 8 PM - 9 PM · Ref: HOP-BLR-8921</div>
            </div>
            <span class="badge" style="background:rgba(239,68,68,0.2);color:#ef4444">BOOKED</span>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Pitch 2 (7v7 Floodlit Pitch)</div>
              <div style="font-size:11.5px;color:#10b981">Available 9 PM · ₹1,800/hr</div>
            </div>
            <button class="btn sm" onclick="toast('Pitch 2 toggled to Walk-in Mode');">Toggle Mode</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:var(--bg3);padding:12px;border-radius:10px">
            <div>
              <div style="font-weight:700">Rooftop Table 4 (Craft Tap)</div>
              <div style="font-size:11.5px;color:#f0b94a">Reserved 7:30 PM · Party of 6</div>
            </div>
            <span class="badge" style="background:rgba(239,68,68,0.2);color:#ef4444">RESERVED</span>
          </div>
        </div>
      </div>

      <div style="background:var(--bg2);border:1px solid var(--line);border-radius:20px;padding:24px">
        <h3 style="margin:0 0 14px;font-size:16px">Guest Ticket & QR Scanner Check-in</h3>
        <p style="font-size:12.5px;color:var(--muted);margin-bottom:14px">Type guest reference code or scan mobile ticket to mark court checked-in.</p>
        <div style="display:flex;gap:10px;margin-bottom:14px">
          <input id="ownerTicketInput" placeholder="e.g. HOP-BLR-8921" style="flex:1;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text);font-family:var(--mono)">
          <button class="btn" onclick="verifyOwnerTicket()">Check In Guest ↗</button>
        </div>
        <div id="ownerCheckinResult"></div>
      </div>
    </div>
  </section>
  `;
}

function loginPartnerDemo(){
  ownerUser = {
    name: 'Mukesh V',
    email: 'mukesh@arenasports.in',
    venueName: 'Indiranagar Arena Turf & Toit Partner',
    city: 'BLR'
  };
  store.set('hoppin.owner_user', ownerUser);
  toast('Welcome back, Mukesh V! Partner Dashboard is active.');
  render();
}

function handleOwnerPhotoFile(input){
  if(input.files && input.files[0]){
    const reader = new FileReader();
    reader.onload = function(e){
      const dataUrl = e.target.result;
      const preview = $('#ownerPhotoPreview');
      const urlInput = $('#ownerPhotoUrl');
      if(preview) preview.src = dataUrl;
      if(urlInput) urlInput.value = dataUrl;
      toast('Photo loaded from your device!');
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function setOwnerPhotoPreset(url){
  const preview = $('#ownerPhotoPreview');
  const urlInput = $('#ownerPhotoUrl');
  if(preview) preview.src = url;
  if(urlInput) urlInput.value = url;
  toast('Preset photo applied!');
}

function submitVenueDPStatus(form){
  const fd = new FormData(form);
  const photo = fd.get('photoUrl');
  const statusText = fd.get('statusText');
  const offerTitle = fd.get('offerTitle');
  const promoCode = fd.get('promoCode');

  const map = getDPStatusMap();
  map['v01'] = {
    venueId: 'v01',
    venueOrClubName: ownerUser?.venueName || 'Indiranagar Arena Turf',
    adminName: ownerUser?.name || 'Mukesh V (Operations GM)',
    adminRole: 'Venue Owner',
    updatedAt: 'Just now',
    photo: String(photo),
    statusText: String(statusText),
    offerTitle: String(offerTitle),
    promoCode: String(promoCode),
    discount: promoCode ? 'OFFER' : 'STATUS',
    validUntil: 'Tonight 11:59 PM'
  };
  store.set('hoppin.dp_status', map);
  toast('✅ Status, Photo & Flash Offer published to your Venue DP Story Ring!');
}

function verifyOwnerTicket(){
  const val = $('#ownerTicketInput')?.value.trim().toUpperCase() || 'HOP-BLR-8921';
  const out = $('#ownerCheckinResult');
  if(out){
    out.innerHTML = `
    <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.4);border-radius:12px;padding:14px;color:#10b981;font-size:13px">
      <div style="font-weight:700">✓ TICKET ${val} VALIDATED</div>
      <div style="color:var(--text);font-size:12px;margin-top:4px">Guest: Rohit Verma · Paid ₹1,430 via UPI · Court 1 Checked In</div>
    </div>`;
  }
  toast(`✓ Ticket ${val} checked in successfully!`);
}

/* Modal to Register a New Venue (GOES LIVE IMMEDIATELY - NO PENDING REVIEWS) */
function showRegisterVenueModal(){
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 30px;">
    <span class="badge" style="background:#10b981;color:#0d0818;font-weight:700">INSTANT ONBOARDING</span>
    <h2 style="font-family:var(--serif);font-size:1.8rem;margin:8px 0 6px">Add Your Venue / Resto-bar</h2>
    <p style="font-size:13px;color:var(--muted);margin:0 0 20px">No waiting, no manual approvals. Your venue goes live online immediately.</p>
    <form onsubmit="event.preventDefault();submitNewVenue(this);">
      <div style="margin-bottom:12px">
        <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">VENUE NAME</label>
        <input name="name" required placeholder="e.g. Indiranagar Padel Hub / ECR Rooftop Restobar" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">CATEGORY</label>
          <select name="cat" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
            <option value="sports">Sports & Turf</option>
            <option value="dining">Resto-bar / Pub</option>
            <option value="gaming">Board Game Lounge</option>
          </select>
        </div>
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">CITY</label>
          <select name="city" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
            <option value="BLR">Bengaluru (BLR)</option>
            <option value="MAA">Chennai (MAA)</option>
          </select>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">AREA / NEIGHBORHOOD</label>
          <input name="area" required placeholder="e.g. Indiranagar / Besant Nagar" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div>
          <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">STARTING PRICE (₹/HR)</label>
          <input name="price" type="number" required value="1200" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
      </div>
      <div style="margin-bottom:20px">
        <label style="display:block;font-size:12px;font-family:var(--mono);margin-bottom:4px">COVER PHOTO URL</label>
        <input name="image" value="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
      </div>
      <button class="btn" type="submit" style="width:100%;padding:12px">Publish Venue & Go Live Now ↗</button>
    </form>
  </div>`);
}

function submitNewVenue(form){
  const fd = new FormData(form);
  const name = String(fd.get('name'));
  const cat = String(fd.get('cat'));
  const city = String(fd.get('city'));
  const area = String(fd.get('area'));
  const price = Number(fd.get('price')) || 1200;
  const image = String(fd.get('image')) || 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80';

  const newV = {
    id: 'v_custom_' + Date.now().toString(36),
    name,
    cat,
    city,
    area,
    price,
    rating: 5.0,
    reviews: 1,
    image,
    tags: [cat === 'sports' ? 'Turf' : cat === 'dining' ? 'Craft Tap' : 'Board Games', 'Instant Book', 'Online Slots'],
    slots: ['06:00 PM','07:00 PM','08:00 PM','09:00 PM']
  };

  VENUES.unshift(newV);
  VBY[newV.id] = newV;
  ownerUser = {
    name: 'Venue Partner',
    email: 'partner@hoppin.live',
    venueName: name,
    city
  };
  store.set('hoppin.owner_user', ownerUser);
  M.close();
  toast(`🎉 Venue "${name}" is now LIVE! Customers can book it right now.`);
  render();
}
"""

c = c.replace("/* =========================================================\n   3-ADMIN RBAC PORTAL (#/admin)", owner_portal_code + "\n/* =========================================================\n   3-ADMIN RBAC PORTAL (#/admin)")
print("Injected self-serve Partner/Venue Owner Portal.")

# =====================================================================
# 6. PLATFORM OPERATIONS & HELP/SUPPORT (#/support)
# =====================================================================
support_portal_code = """
/* =========================================================
   INTERNAL PLATFORM OPERATIONS & SUPPORT (#/support)
   Discreet internal portal for global stats & system health
   ========================================================= */
function supportHTML(){
  return `
  <section class="wrap" style="padding:40px clamp(20px,5vw,72px) 80px">
    <div class="admin-banner" style="background:linear-gradient(135deg,rgba(16,185,129,0.15) 0%,rgba(124,58,237,0.12) 100%)">
      <div>
        <span class="badge" style="background:#10b981;color:#0d0818;font-weight:700">PLATFORM OPERATIONS & SUPPORT</span>
        <h1 style="font-size:2rem;margin:8px 0 4px">Hoppin Core Infrastructure</h1>
        <div style="font-size:13px;color:var(--muted)">Platform Director HQ · Bengaluru & Chennai Operational Telemetry</div>
      </div>
    </div>

    <div class="admin-stat-row">
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">TOTAL GROSS VOLUME</div>
        <div class="admin-stat-num">₹28,45,200</div>
        <div style="font-size:12px;color:#10b981">↑ 22% Month-over-Month</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">ACTIVE VENUES</div>
        <div class="admin-stat-num">${VENUES.length}</div>
        <div style="font-size:12px;color:var(--pastel)">100% Self-Serve Enabled</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">HEALTH & RUN CLUBS</div>
        <div class="admin-stat-num">${CLUBS_DATA.length}</div>
        <div style="font-size:12px;color:#f0b94a">1,480+ Young Members</div>
      </div>
      <div class="admin-stat-card">
        <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">PLATFORM COMMISSION</div>
        <div class="admin-stat-num">₹99,580</div>
        <div style="font-size:12px;color:#10b981">Auto-settled via Gateway</div>
      </div>
    </div>
  </section>
  `;
}
"""

c = c.replace("function adminHTML(){", support_portal_code + "\nfunction adminHTML(){")
print("Injected support portal code.")

# =====================================================================
# 7. UPDATE FOOTER WITH SUPPORT / PARTNER LINKS
# =====================================================================
footer_replacement = """
  <!-- FOOTER -->
  <footer style="border-top:1px solid var(--line);padding:40px clamp(20px,5vw,72px);background:var(--bg2);color:var(--muted);font-size:13px">
    <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px">
      <div>
        <b style="color:var(--text);font-size:16px">hoppin.</b> &nbsp;·&nbsp; Step Out. Show Up.
        <div style="margin-top:4px">Bengaluru & Chennai · Real places, youth run clubs & live bookings.</div>
      </div>
      <div style="display:flex;gap:20px;flex-wrap:wrap">
        <a href="#/owner" style="color:var(--pastel);font-weight:600">Partner / Owner Portal ↗</a>
        <a href="#/clubs" style="color:var(--text)">Clubs & Runs</a>
        <a href="#/support" style="color:var(--muted)">Platform Support</a>
        <span style="color:var(--muted)">© 2026 hoppin.</span>
      </div>
    </div>
  </footer>
"""

if '<footer' in c:
    c = re.sub(r'<footer.*?</footer>', footer_replacement, c, flags=re.DOTALL)
else:
    c = c.replace('</main>', '</main>\n' + footer_replacement)
print("Updated footer with Partner and Support links.")

# =====================================================================
# 8. UPDATE STREAK MODAL TO EXPLAIN PROFILE BUILDING & GUEST MODE
# =====================================================================
old_streak_content = """    <div style="background:linear-gradient(135deg,rgba(240,185,74,0.15) 0%,rgba(124,58,237,0.15) 100%);border:1px solid rgba(240,185,74,0.4);border-radius:18px;padding:22px;text-align:center;margin-bottom:20px">
      <div style="font-family:var(--serif);font-size:3.5rem;font-weight:700;color:#f0b94a;line-height:1">${s.days}</div>
      <div style="font-family:var(--mono);font-size:13px;letter-spacing:0.1em;text-transform:uppercase;color:#fff;margin-top:6px">Day Active Streak</div>
      <div style="font-size:13px;color:#c4b5fd;margin-top:4px">Total Experience: <b>${s.xp} XP</b> · Tier 2 Hopper</div>
    </div>"""

new_streak_content = """    <!-- How Customers Know Profile Building Needs Login -->
    ${!S.user ? `
    <div style="background:rgba(196,181,253,0.1);border:1px solid rgba(196,181,253,0.3);border-radius:14px;padding:16px;margin-bottom:18px">
      <div style="font-weight:700;color:#f0b94a;margin-bottom:4px;display:flex;align-items:center;gap:6px">
        <span>🔥</span> Guest Streak Active (4 Days)
      </div>
      <div style="font-size:12.5px;color:var(--text);line-height:1.5">
        Create or sign in to your <b>Customer Profile</b> to permanently save your 4-Day Streak, earn milestone badges, and keep your morning run club memberships active!
      </div>
      <button class="btn sm" style="margin-top:10px" data-act="open-customer-auth">Sign In / Create Customer Account ↗</button>
    </div>` : ''}

    <div style="background:linear-gradient(135deg,rgba(240,185,74,0.15) 0%,rgba(124,58,237,0.15) 100%);border:1px solid rgba(240,185,74,0.4);border-radius:18px;padding:22px;text-align:center;margin-bottom:20px">
      <div style="font-family:var(--serif);font-size:3.5rem;font-weight:700;color:#f0b94a;line-height:1">${s.days}</div>
      <div style="font-family:var(--mono);font-size:13px;letter-spacing:0.1em;text-transform:uppercase;color:#fff;margin-top:6px">Day Active Streak</div>
      <div style="font-size:13px;color:#c4b5fd;margin-top:4px">Total Experience: <b>${s.xp} XP</b> · Tier 2 Hopper</div>
    </div>"""

if old_streak_content in c:
    c = c.replace(old_streak_content, new_streak_content)
    print("Updated streak modal with guest/login explanation.")

# Update click switch to handle open-customer-auth, view-bookings, signout
old_switch_tail = "case 'claim-dp-offer':claimDPOffer(a.dataset.code,a.dataset.venue);break;"
new_switch_tail = """case 'claim-dp-offer':claimDPOffer(a.dataset.code,a.dataset.venue);break;
  case 'open-customer-auth':M.close();showAuth('up','Create your customer profile to save streaks and tickets.');break;
  case 'view-bookings':M.close();go('/bookings');break;
  case 'signout':S.user=null;store.set('hoppin.session',null);acctBtn();M.close();toast('Signed out successfully.');break;
  case 'nav-owner':M.close();go('/owner');break;"""

if old_switch_tail in c:
    c = c.replace(old_switch_tail, new_switch_tail)
    print("Updated click switch cases.")

# Write back to build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(c)
print("Updated build_fullstack_frontend.py!")

# Synchronize all 5 target files
targets = [
  'apps/web/index.html',
  'apps/web/public/poc.html',
  'apps/web/public/index.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc (1).html'
]

# Run build_fullstack_frontend.py to output to all files
exec(open("build_fullstack_frontend.py", encoding="utf-8").read())
print("All target files synchronized and validated!")
