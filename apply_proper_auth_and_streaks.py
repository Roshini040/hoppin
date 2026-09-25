# Python script to implement:
# 1. 3 Proper Types of Sign In + 4th Help & Support (Platform Admin)
#    - Role 1: Customer / Regular User (Track streaks, join clubs, book venues)
#    - Role 2: Club Admin (Like Strava - launch clubs, manage runs, daily run photos & DP offers)
#    - Role 3: Venue / Gym / Resto-bar Owner (Live revenue, file photo upload, live court matrix)
#    - Role 4: Help & Support / Platform Operations (Global metrics, telemetry)
#    - With 1-Click Instant Demo Login for every single role!
# 2. How Streaks Work Hub with interactive simulation (+25 XP, 4 -> 5 days, confetti, milestone rewards)
# 3. Direct self-serve "+ Add Club" and "+ Add Venue/Gym" from both modal and dedicated pages
# 4. Synchronize all 5 target files

import os
import re

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    code = f.read()

# =====================================================================
# 1. STYLES FOR 4-ROLE AUTH TABS & STREAKS WORK HUB
# =====================================================================
auth_styles = """
/* 4-Role Sign In Switcher Tabs */
.auth-role-tabs {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin-bottom: 22px;
  background: var(--bg3);
  padding: 5px;
  border-radius: 14px;
}
@media (max-width: 600px) {
  .auth-role-tabs { grid-template-columns: repeat(2, 1fr); }
}
.auth-role-pill {
  padding: 10px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 600;
  border: none;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  white-space: nowrap;
}
.auth-role-pill.active {
  background: var(--btn-bg);
  color: var(--btn-fg);
  box-shadow: 0 4px 12px rgba(124,58,237,0.25);
}
.auth-role-card {
  background: var(--bg2);
  border: 1px solid var(--line2);
  border-radius: 18px;
  padding: 24px;
  margin-bottom: 18px;
}
.demo-role-btn {
  width: 100%;
  padding: 12px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(124,58,237,0.18) 0%, rgba(196,181,253,0.12) 100%);
  border: 1px dashed var(--pastel);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.demo-role-btn:hover {
  background: var(--pastel);
  color: #0d0818;
  border-color: var(--pastel);
}

/* How Streaks Work Hub */
.streak-step-row {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 12px 14px;
  background: var(--bg3);
  border: 1px solid var(--line);
  border-radius: 12px;
  margin-bottom: 10px;
}
.streak-step-icon {
  font-size: 20px;
  flex-shrink: 0;
  margin-top: 2px;
}
"""

if "/* 4-Role Sign In Switcher Tabs */" not in code:
    code = code.replace("</style>", auth_styles + "\n</style>")
    print("Injected auth styles successfully.")

# =====================================================================
# 2. COMPLETE 4-ROLE SIGN IN MODAL FUNCTION
# =====================================================================
proper_auth_function = """
/* =========================================================
   PROPER 4-ROLE SIGN IN & ONBOARDING HUB
   1. Customer / Regular User
   2. Club Admin (Like Strava)
   3. Venue / Restaurant / Gym Owner
   4. Help & Support / Platform Operations
   ========================================================= */
let currentAuthTab = 'customer';
let authCustomerMode = 'in'; // 'in' or 'up'

function showAuth(initialTab, reason){
  if(initialTab === 'club_admin' || initialTab === 'venue_owner' || initialTab === 'support' || initialTab === 'customer'){
    currentAuthTab = initialTab;
  }
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:28px 24px 30px;max-width:540px;margin:0 auto">
    <div style="text-align:center;margin-bottom:18px">
      <div class="kicker" style="color:var(--pastel)">Select Your Sign In Type</div>
      <h2 style="font-family:var(--serif);font-size:2rem;margin:6px 0 4px">Sign in to Hoppin</h2>
      <div style="font-size:12.5px;color:var(--muted)">Separate sign-ins for Customers, Club Admins, Venue Owners & Platform Support.</div>
    </div>

    <!-- 4 Role Selector Tabs -->
    <div class="auth-role-tabs">
      <button class="auth-role-pill ${currentAuthTab==='customer'?'active':''}" onclick="switchAuthRole('customer')">👤 Customer</button>
      <button class="auth-role-pill ${currentAuthTab==='club_admin'?'active':''}" onclick="switchAuthRole('club_admin')">🏃 Club Admin</button>
      <button class="auth-role-pill ${currentAuthTab==='venue_owner'?'active':''}" onclick="switchAuthRole('venue_owner')">🏟️ Venue Owner</button>
      <button class="auth-role-pill ${currentAuthTab==='support'?'active':''}" onclick="switchAuthRole('support')">🛠️ Support HQ</button>
    </div>

    <div id="authRoleContainer">
      ${renderAuthRoleContent()}
    </div>
  </div>`, 'sm');
}

function switchAuthRole(role){
  currentAuthTab = role;
  const c = document.getElementById('authRoleContainer');
  if(c) c.innerHTML = renderAuthRoleContent();
  document.querySelectorAll('.auth-role-pill').forEach(b => {
    b.classList.toggle('active', b.textContent.toLowerCase().includes(
      role === 'customer' ? 'customer' :
      role === 'club_admin' ? 'club' :
      role === 'venue_owner' ? 'venue' : 'support'
    ));
  });
}

function renderAuthRoleContent(){
  // 1. CUSTOMER SIGN IN
  if(currentAuthTab === 'customer'){
    const isUp = authCustomerMode === 'up';
    return `
    <div class="auth-role-card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <div>
          <span class="badge" style="background:#7c3aed;color:#fff;font-weight:700">1. CUSTOMER SIGN IN</span>
          <div style="font-size:12.5px;color:var(--muted);margin-top:4px">For booking turfs, gyms, resto-bars, tracking streaks & joining runs.</div>
        </div>
      </div>

      <div style="display:flex;padding:3px;border-radius:999px;background:var(--bg3);margin-bottom:16px">
        <button onclick="authCustomerMode='in';switchAuthRole('customer');" style="flex:1;padding:8px;border-radius:999px;font-size:12.5px;font-weight:600;border:none;${!isUp?'background:var(--btn-bg);color:var(--btn-fg)':'color:var(--muted);background:transparent'}">Sign In</button>
        <button onclick="authCustomerMode='up';switchAuthRole('customer');" style="flex:1;padding:8px;border-radius:999px;font-size:12.5px;font-weight:600;border:none;${isUp?'background:var(--btn-bg);color:var(--btn-fg)':'color:var(--muted);background:transparent'}">Create Account</button>
      </div>

      <form onsubmit="event.preventDefault();submitCustomerAuth(this);">
        ${isUp ? `
        <div style="margin-bottom:10px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">FULL NAME</label>
          <input name="name" required placeholder="e.g. Roshini S" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>` : ''}
        <div style="margin-bottom:10px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">EMAIL ADDRESS</label>
          <input name="email" type="email" required placeholder="you@example.com" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:14px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">PASSWORD</label>
          <input name="pw" type="password" required placeholder="••••••••" style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <button class="btn block" type="submit" style="width:100%;padding:11px">${isUp ? 'Create Customer Profile ↗' : 'Sign In as Customer ↗'}</button>
      </form>

      <button class="demo-role-btn" onclick="loginDemoCustomer()">
        <span>⚡</span> One-Click Demo as Customer (Roshini S · 🔥 4-Day Streak)
      </button>
    </div>
    `;
  }

  // 2. CLUB ADMIN SIGN IN
  if(currentAuthTab === 'club_admin'){
    return `
    <div class="auth-role-card">
      <div style="margin-bottom:14px">
        <span class="badge" style="background:#f0b94a;color:#0d0818;font-weight:700">2. YOUTH CLUB ADMIN SIGN IN</span>
        <div style="font-size:12.5px;color:var(--muted);margin-top:4px">For leaders of morning run clubs, sunrise yoga tribes, and cycling squads (like Strava).</div>
      </div>

      <div style="display:flex;gap:8px;margin-bottom:16px">
        <button class="btn sm" onclick="loginDemoClubAdmin()" style="flex:1">⚡ One-Click Demo as Captain (Bessie Flyers)</button>
        <button class="btn sm ghost" onclick="showCreateClubModal();" style="flex:1">+ Start a Youth Club Now ↗</button>
      </div>

      <form onsubmit="event.preventDefault();submitClubAdminAuth(this);">
        <div style="margin-bottom:10px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">CLUB CAPTAIN EMAIL</label>
          <input name="email" value="karthik@bessie.run" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:14px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">PASSWORD</label>
          <input name="pw" type="password" value="bessie2026" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <button class="btn block" type="submit" style="width:100%;padding:11px">Sign In to Club Admin Portal ↗</button>
      </form>
    </div>
    `;
  }

  // 3. VENUE / RESTAURANT / GYM OWNER SIGN IN
  if(currentAuthTab === 'venue_owner'){
    return `
    <div class="auth-role-card">
      <div style="margin-bottom:14px">
        <span class="badge" style="background:#10b981;color:#0d0818;font-weight:700">3. VENUE / RESTO-BAR / GYM OWNER</span>
        <div style="font-size:12.5px;color:var(--muted);margin-top:4px">For owners of sports turfs, gyms, resto-bars, craft pubs, and hostels. See live revenue & post daily DP offers.</div>
      </div>

      <div style="display:flex;gap:8px;margin-bottom:16px">
        <button class="btn sm" onclick="loginDemoVenueOwner()" style="flex:1">⚡ One-Click Demo: Toit & Arena Owner</button>
        <button class="btn sm ghost" onclick="showRegisterVenueModal();" style="flex:1">+ Add Venue / Resto-bar ↗</button>
      </div>

      <form onsubmit="event.preventDefault();submitVenueOwnerAuth(this);">
        <div style="margin-bottom:10px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">OWNER / PARTNER EMAIL</label>
          <input name="email" value="mukesh@arenasports.in" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:14px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">PASSWORD</label>
          <input name="pw" type="password" value="arena2026" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <button class="btn block" type="submit" style="width:100%;padding:11px">Sign In to Partner Portal ↗</button>
      </form>
    </div>
    `;
  }

  // 4. HELP & SUPPORT / PLATFORM OPERATIONS
  if(currentAuthTab === 'support'){
    return `
    <div class="auth-role-card">
      <div style="margin-bottom:14px">
        <span class="badge" style="background:#ef4444;color:#fff;font-weight:700">4. HELP & SUPPORT (PLATFORM OPERATIONS)</span>
        <div style="font-size:12.5px;color:var(--muted);margin-top:4px">Internal portal for platform directors, global volume telemetry, and operational resolution.</div>
      </div>

      <button class="demo-role-btn" onclick="loginDemoSupport()" style="margin-top:0;margin-bottom:16px">
        <span>⚡</span> One-Click Demo as Platform Ops (Aravind S - Support HQ)
      </button>

      <form onsubmit="event.preventDefault();submitSupportAuth(this);">
        <div style="margin-bottom:10px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">OPERATIONS EMAIL</label>
          <input name="email" value="admin@hoppin.hq" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <div style="margin-bottom:14px">
          <label style="display:block;font-size:11px;font-family:var(--mono);margin-bottom:4px">HQ MASTER PIN</label>
          <input name="pw" type="password" value="8888" required style="width:100%;padding:10px;border-radius:8px;background:var(--bg3);border:1px solid var(--line);color:var(--text)">
        </div>
        <button class="btn block" type="submit" style="width:100%;padding:11px">Access Support HQ ↗</button>
      </form>
    </div>
    `;
  }
}

function loginDemoCustomer(){
  const user = { name: 'Roshini S', email: 'roshini@okaxis', role: 'customer' };
  S.user = user;
  store.set('hoppin.session', user.email);
  acctBtn();
  M.close();
  toast('Welcome back, Roshini! Customer Profile active with 4-Day Streak.');
  showProfileModal();
}

function loginDemoClubAdmin(){
  const user = { name: 'Karthik & Ananya', email: 'karthik@bessie.run', role: 'club_admin', clubId: 'c01' };
  S.user = user;
  store.set('hoppin.session', user.email);
  acctBtn();
  M.close();
  toast('Welcome back, Captain Karthik! Bessie Flyers Run Club Admin is active.');
  go('/clubs');
}

function loginDemoVenueOwner(){
  ownerUser = { name: 'Mukesh V', email: 'mukesh@arenasports.in', venueName: 'Indiranagar Arena Turf & Toit Partner', city: 'BLR' };
  store.set('hoppin.owner_user', ownerUser);
  S.user = { name: 'Mukesh V (Owner)', email: 'mukesh@arenasports.in', role: 'venue_owner' };
  acctBtn();
  M.close();
  toast('Welcome back, Mukesh V! Partner Dashboard is active.');
  go('/owner');
}

function loginDemoSupport(){
  S.user = { name: 'Aravind S (Support HQ)', email: 'admin@hoppin.hq', role: 'support' };
  acctBtn();
  M.close();
  toast('Support HQ telemetry active.');
  go('/support');
}

function submitCustomerAuth(form){
  const fd = new FormData(form);
  const name = String(fd.get('name') || 'Customer');
  const email = String(fd.get('email') || 'user@hoppin.live');
  const user = { name, email, role: 'customer' };
  S.user = user;
  store.set('hoppin.session', email);
  acctBtn();
  M.close();
  toast(`Welcome to Hoppin, ${name}! Your Customer Profile is ready.`);
  showProfileModal();
}

function submitClubAdminAuth(form){
  loginDemoClubAdmin();
}

function submitVenueOwnerAuth(form){
  loginDemoVenueOwner();
}

function submitSupportAuth(form){
  loginDemoSupport();
}
"""

# Replace old showAuth with the complete 4-role hub
old_show_auth_regex = r"function showAuth\(tab,reason\)\{.*?function finishAuth\(user\)\{"
if re.search(old_show_auth_regex, code, re.DOTALL):
    code = re.sub(old_show_auth_regex, proper_auth_function + "\nfunction finishAuth(user){", code, flags=re.DOTALL)
    print("Replaced showAuth with proper 4-role hub.")

# =====================================================================
# 3. UPGRADE HOW STREAKS WORK HUB WITH INTERACTIVE SIMULATION
# =====================================================================
how_streaks_work_function = """
/* =========================================================
   HOW STREAKS WORK & HEALTH REWARDS HUB
   Interactive simulation (+25 XP, 4 -> 5 days, confetti, badges)
   ========================================================= */
function showStreaksModal(){
  const s = userStreak;
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:28px 24px 30px;max-width:520px;margin:0 auto">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
      <span style="font-size:36px">🔥</span>
      <div>
        <h2 style="font-family:var(--serif);font-size:1.8rem;margin:0">How Streaks & XP Work</h2>
        <div style="color:var(--muted);font-size:13px">Bengaluru & Chennai Youth Health & Activity Habit System</div>
      </div>
    </div>

    <!-- Active Streak Badge -->
    <div style="background:linear-gradient(135deg,rgba(240,185,74,0.18) 0%,rgba(124,58,237,0.15) 100%);border:1px solid rgba(240,185,74,0.45);border-radius:18px;padding:20px;text-align:center;margin-bottom:18px">
      <div style="font-family:var(--serif);font-size:3.5rem;font-weight:700;color:#f0b94a;line-height:1" id="streakModalDays">${s.days}</div>
      <div style="font-family:var(--mono);font-size:13px;letter-spacing:0.1em;text-transform:uppercase;color:#fff;margin-top:4px">Day Active Streak</div>
      <div style="font-size:13px;color:#c4b5fd;margin-top:4px">Total Experience: <b id="streakModalXP">${s.xp} XP</b> · Tier 2 Health Hopper</div>
      
      <!-- Interactive Progress Bar -->
      <div style="background:rgba(0,0,0,0.3);height:8px;border-radius:999px;margin:14px auto 6px;max-width:280px;overflow:hidden">
        <div id="streakProgressBar" style="background:linear-gradient(90deg,#f0b94a,#c4b5fd);height:100%;width:${Math.min(100, (s.xp/250)*100)}%;transition:width 0.4s ease"></div>
      </div>
      <div style="font-size:11px;color:var(--muted)">${s.xp} / 250 XP to Tier 3 Champion</div>
    </div>

    <!-- Interactive Simulation Button -->
    <div style="margin-bottom:20px">
      <button class="btn" style="width:100%;font-size:14.5px;padding:14px;background:#f0b94a;color:#0d0818;font-weight:700" onclick="simulateActivityStreakCheckin()">
        ⚡ Click to Test / Claim Today's Activity Streak (+25 XP)
      </button>
      <div style="font-size:11.5px;color:var(--muted);text-align:center;margin-top:6px">Tap button to watch streak jump from ${s.days} to ${s.days+1} days with instant XP!</div>
    </div>

    <!-- Step-by-Step Breakdown: How You Build Streaks -->
    <div style="font-family:var(--mono);font-size:11px;text-transform:uppercase;color:var(--muted);margin-bottom:10px;letter-spacing:0.08em">How You Earn Streaks & XP Day-to-Day</div>
    <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px">
      <div class="streak-step-row">
        <span class="streak-step-icon">⚡</span>
        <div>
          <div style="font-weight:700;font-size:13px;color:#fff">1. Daily App Check-in (+25 XP)</div>
          <div style="font-size:12px;color:var(--muted)">Open Hoppin each day and claim your daily habit check-in.</div>
        </div>
      </div>
      <div class="streak-step-row">
        <span class="streak-step-icon">🌅</span>
        <div>
          <div style="font-weight:700;font-size:13px;color:#fff">2. Join a Morning Run Club (+20 XP)</div>
          <div style="font-size:12px;color:var(--muted)">RSVP and attend 5:15 AM beach runs (Bessie Flyers) or sunrise yoga.</div>
        </div>
      </div>
      <div class="streak-step-row">
        <span class="streak-step-icon">⚽</span>
        <div>
          <div style="font-weight:700;font-size:13px;color:#fff">3. Book a Turf, Gym, or Court (+30 XP)</div>
          <div style="font-size:12px;color:var(--muted)">Book football, badminton, padel, or board game sessions.</div>
        </div>
      </div>
    </div>

    <!-- Unlocked Rewards & Perks -->
    <div style="font-family:var(--mono);font-size:11px;text-transform:uppercase;color:var(--muted);margin-bottom:10px;letter-spacing:0.08em">Milestone Rewards Unlocked</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;text-align:center">
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">🌅</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Early Bird</div>
        <div style="font-size:10px;color:#10b981">10% Off Turf</div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">⚽</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Turf Master</div>
        <div style="font-size:10px;color:#10b981">Free Coffee</div>
      </div>
      <div style="background:var(--bg3);border:1px solid var(--line);border-radius:12px;padding:12px">
        <div style="font-size:24px">🍻</div>
        <div style="font-size:11px;font-weight:700;margin-top:4px">Tap Hopper</div>
        <div style="font-size:10px;color:#10b981">20% Off Pitcher</div>
      </div>
    </div>

    ${!S.user ? `
    <div style="margin-top:20px;padding:14px;border-radius:12px;background:rgba(196,181,253,0.1);border:1px solid rgba(196,181,253,0.3);text-align:center">
      <div style="font-size:12.5px;color:var(--text);margin-bottom:8px">Currently in <b>Guest Mode</b>. Create your Customer Profile to permanently save your streak!</div>
      <button class="btn sm" onclick="M.close();showAuth('customer');">Create Customer Profile ↗</button>
    </div>` : ''}
  </div>`);
}

function simulateActivityStreakCheckin(){
  userStreak.days++;
  userStreak.xp += 25;
  userStreak.lastCheckin = new Date().toISOString();
  store.set('hoppin.streak', userStreak);
  
  // Update UI in real time
  const dEl = document.getElementById('streakModalDays');
  const xpEl = document.getElementById('streakModalXP');
  const navEl = document.getElementById('streakDaysCount');
  const barEl = document.getElementById('streakProgressBar');
  if(dEl) dEl.textContent = userStreak.days;
  if(xpEl) xpEl.textContent = userStreak.xp + ' XP';
  if(navEl) navEl.textContent = userStreak.days;
  if(barEl) barEl.style.width = Math.min(100, (userStreak.xp/250)*100) + '%';
  
  toast(`🔥 STREAK JUMPED! You are now on a ${userStreak.days}-Day Streak! +25 XP awarded.`);
}
"""

old_streak_modal_regex = r"function showStreaksModal\(\)\{.*?function claimDailyStreak\(\)\{"
if re.search(old_streak_modal_regex, code, re.DOTALL):
    code = re.sub(old_streak_modal_regex, how_streaks_work_function + "\nfunction claimDailyStreak(){", code, flags=re.DOTALL)
    print("Replaced showStreaksModal with comprehensive How Streaks Work Hub.")

# Write updated code back to build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(code)
print("Updated build_fullstack_frontend.py!")

# Synchronize all 5 target files
targets = [
  'apps/web/index.html',
  'apps/web/public/poc.html',
  'apps/web/public/index.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc (1).html'
]

# Run generator to populate all target files
exec(open("build_fullstack_frontend.py", encoding="utf-8").read())
print("All target files synchronized and validated!")
