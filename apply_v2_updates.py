# Script to build and update the Hoppin Lilac Grail Edition v2 with:
# 1. Images everywhere (no SVG rect covering cards!)
# 2. Circular Spinning Wheel with emojis, images, city selector, fast spin
# 3. Chapter 01 photo stack & Chapter 02 night atmosphere
# 4. Chapter 03 6-category image rows
# 5. Location area quick-filters and rich cards in directory
# 6. Full backend API integration

import os
import subprocess

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    content = f.read()

# -------------------------------------------------------------
# 1. FIX coverMedia: remove coverSVG from covering images!
# -------------------------------------------------------------
old_cover_media = """function coverImgURL(v){return VENUE_IMG[v.name]||'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';}
function coverMedia(v){
  const imgUrl=coverImgURL(v);
  return `<img src="${imgUrl}" alt="${esc(v.name)}" loading="lazy" onerror="this.style.display='none'">${coverSVG(v)}`;
}"""

new_cover_media = """function coverImgURL(v){return VENUE_IMG[v.name]||'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';}
function coverMedia(v){
  const imgUrl=coverImgURL(v);
  return `<img src="${imgUrl}" alt="${esc(v.name)}" loading="lazy" class="cimg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';">`;
}"""

assert old_cover_media in content, "old_cover_media not found"
content = content.replace(old_cover_media, new_cover_media)

# -------------------------------------------------------------
# 2. Add GUILD_DATA and Circular Wheel JS
# -------------------------------------------------------------
old_guilds_wheel_js = """/* =========================================================
   GUILDS 3D WHEEL
   ========================================================= */
function buildGuildsWheel() {
  const cats = Object.entries(CATS);
  const total = cats.length;
  return cats.map(([k, c], i) => {
    const angle = (i / total) * 360;
    return `<div class="wheel-item" style="--angle:${angle}deg" data-act="catgo" data-cat="${k}">
      ${totemSVG(CATCOL[k]?.kind || 'check', CATCOL[k]?.c || '#c4b5fd', CATCOL[k]?.c2 || '#7c3aed', 80)}
      <span>${c.label}</span>
    </div>`;
  }).join('');
}"""

new_guilds_wheel_js = """/* =========================================================
   GUILDS & ARENA CIRCULAR WHEEL DATA & INTERACTION
   ========================================================= */
const GUILD_DATA = {
  sports: {
    emoji: '🏸', label: 'Sports & Turfs', count: '18 venues',
    img: 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=400&q=80',
    areas: 'Indiranagar · Kilpauk · Koramangala'
  },
  pubs: {
    emoji: '🍺', label: 'Pubs & Brews', count: '13 taprooms',
    img: 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=400&q=80',
    areas: 'Indiranagar · Egmore · T. Nagar'
  },
  fitness: {
    emoji: '🏋️', label: 'Fitness & Gyms', count: '12 gyms',
    img: 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=400&q=80',
    areas: 'Indiranagar · Adyar · Alwarpet'
  },
  dining: {
    emoji: '☕', label: 'Dining & Cafes', count: '8 spots',
    img: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=400&q=80',
    areas: 'Besant Nagar · Central BLR · Mylapore'
  },
  gaming: {
    emoji: '🎲', label: 'Gaming & Arcades', count: '9 cafes',
    img: 'https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=400&q=80',
    areas: 'Egmore · Whitefield · Velachery'
  },
  clubs: {
    emoji: '🏃', label: 'Run & Social Clubs', count: '7 clubs',
    img: 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=400&q=80',
    areas: "Elliot's Beach · Cubbon Park"
  }
};

let wheelRotation = 0;
let isSpinningWheel = false;

function buildGuildsWheel() {
  const entries = Object.entries(GUILD_DATA);
  const total = entries.length;
  return entries.map(([k, g], i) => {
    const angle = (i / total) * 360;
    return `<div class="circle-item" style="--angle:${angle}deg" data-cat="${k}" data-act="wheel-item" tabindex="0" role="button" aria-label="${g.label}">
      <div class="circle-photo-pod">
        <img src="${g.img}" alt="${g.label}" loading="lazy">
        <div class="circle-emoji-badge">${g.emoji}</div>
      </div>
      <span class="circle-item-label">${g.label.split(' & ')[0]}</span>
      <span class="circle-item-count">${g.count}</span>
    </div>`;
  }).join('');
}

function updateWheelCenter(catKey) {
  const g = GUILD_DATA[catKey] || GUILD_DATA.sports;
  const em = $('#hubEmoji');
  const ti = $('#hubTitle');
  const co = $('#hubCount');
  if (em) em.textContent = g.emoji;
  if (ti) ti.textContent = g.label;
  if (co) co.textContent = g.count + ' · ' + g.areas;
  $$('.circle-item').forEach(el => el.classList.toggle('active', el.dataset.cat === catKey));
}

function spinWheelFast() {
  if (isSpinningWheel) return;
  isSpinningWheel = true;
  const disc = $('#circularDisc');
  if (!disc) return;
  
  const catKeys = Object.keys(GUILD_DATA);
  const randIdx = Math.floor(Math.random() * catKeys.length);
  const chosenCat = catKeys[randIdx];
  const fullTurns = 360 * (3 + Math.floor(Math.random() * 2));
  const targetAngle = 360 - (randIdx * (360 / catKeys.length));
  wheelRotation += fullTurns + (targetAngle - (wheelRotation % 360));
  
  disc.classList.add('spinning');
  disc.style.transform = `rotate(${wheelRotation}deg)`;
  toast('Spinning the wheel to find your arena... 🎲');
  
  setTimeout(() => {
    disc.classList.remove('spinning');
    isSpinningWheel = false;
    updateWheelCenter(chosenCat);
    S.cat = chosenCat;
    renderGrid();
    toast(`Landed on ${GUILD_DATA[chosenCat].label}! 🎉`);
  }, 2200);
}"""

assert old_guilds_wheel_js in content, "old_guilds_wheel_js not found"
content = content.replace(old_guilds_wheel_js, new_guilds_wheel_js)

# -------------------------------------------------------------
# 3. Update CSS for Circular Wheel, Chapter 01 photo collage, and Card imagery
# -------------------------------------------------------------
old_wheel_css = """.guilds-sec {
  padding: clamp(70px, 9vw, 120px) clamp(20px, 5vw, 72px);
  background: var(--bg);
  position: relative;
}
.wheel-wrap {
  position: relative;
  width: min(440px, 90vw);
  height: min(440px, 90vw);
  margin: 50px auto 0;
  perspective: 1000px;
}
.shield-wheel {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.15s ease-out;
}
.wheel-item {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 90px;
  height: 110px;
  margin-left: -45px;
  margin-top: -55px;
  transform: rotate(var(--angle)) translateY(-160px) rotate(calc(-1 * var(--angle)));
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.wheel-item:hover {
  transform: rotate(var(--angle)) translateY(-185px) rotate(calc(-1 * var(--angle))) scale(1.18);
}
.wheel-item span {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}"""

new_wheel_css = """/* =========================================================
   GUILDS & LOCATION TRUE CIRCULAR SPINNER
   ========================================================= */
.guilds-sec {
  padding: clamp(70px, 9vw, 120px) clamp(20px, 5vw, 72px);
  background: radial-gradient(circle at 50% 50%, #150c26 0%, var(--bg) 80%);
  position: relative;
  overflow: hidden;
  text-align: center;
}
.location-selector-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin: 24px auto 36px;
}
.wheel-stage {
  position: relative;
  width: min(530px, 92vw);
  height: min(530px, 92vw);
  margin: 0 auto;
  display: grid;
  place-items: center;
}
.wheel-outer-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 2px dashed rgba(196,181,253,0.32);
  box-shadow: 0 0 60px rgba(124,58,237,0.22), inset 0 0 40px rgba(139,92,246,0.12);
  pointer-events: none;
  animation: slowRingPulse 8s ease-in-out infinite alternate;
}
@keyframes slowRingPulse {
  0% { transform: scale(1); border-color: rgba(196,181,253,0.25); }
  100% { transform: scale(1.02); border-color: rgba(196,181,253,0.55); }
}
.circular-disc {
  position: absolute;
  inset: 16px;
  border-radius: 50%;
  background: radial-gradient(circle at center, rgba(32,20,54,0.75) 0%, rgba(13,8,24,0.95) 75%);
  border: 1px solid rgba(196,181,253,0.22);
  transition: transform 0.4s cubic-bezier(0.15, 0.9, 0.25, 1);
  transform-origin: center center;
  box-shadow: 0 20px 60px rgba(0,0,0,0.65);
  cursor: grab;
}
.circular-disc.spinning {
  transition: transform 2.2s cubic-bezier(0.12, 0.95, 0.22, 1);
}
.circular-disc:active { cursor: grabbing; }

.circle-item {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 104px;
  height: 104px;
  margin-left: -52px;
  margin-top: -52px;
  transform: rotate(var(--angle)) translateY(-190px) rotate(calc(-1 * var(--angle)));
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.3s;
}
.circle-item:hover, .circle-item.active {
  transform: rotate(var(--angle)) translateY(-200px) rotate(calc(-1 * var(--angle))) scale(1.15);
  filter: drop-shadow(0 0 18px rgba(196,181,253,0.9));
}
.circle-photo-pod {
  position: relative;
  width: 76px;
  height: 76px;
  border-radius: 50%;
  overflow: hidden;
  border: 2.5px solid #c4b5fd;
  box-shadow: 0 8px 24px rgba(0,0,0,0.65), 0 0 20px rgba(139,92,246,0.4);
  background: #181028;
}
.circle-photo-pod img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.circle-item:hover .circle-photo-pod img { transform: scale(1.14); }
.circle-emoji-badge {
  position: absolute;
  right: -2px;
  bottom: -2px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #0d0818;
  border: 1.5px solid #c4b5fd;
  display: grid;
  place-items: center;
  font-size: 15px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}
.circle-item-label {
  font-family: var(--mono);
  font-size: 10.5px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #faf8ff;
  font-weight: 600;
  white-space: nowrap;
  text-shadow: 0 2px 6px rgba(0,0,0,0.8);
}
.circle-item-count {
  font-family: var(--mono);
  font-size: 9px;
  color: #c4b5fd;
  letter-spacing: 0.08em;
}

/* CENTER HUB */
.wheel-center-hub {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 165px;
  height: 165px;
  border-radius: 50%;
  background: rgba(15, 10, 24, 0.94);
  border: 2px solid #c4b5fd;
  box-shadow: 0 0 40px rgba(196,181,253,0.4), inset 0 0 25px rgba(124,58,237,0.3);
  backdrop-filter: blur(20px);
  z-index: 15;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 14px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.25s, box-shadow 0.25s;
}
.wheel-center-hub:hover {
  transform: translate(-50%, -50%) scale(1.05);
  box-shadow: 0 0 50px rgba(196,181,253,0.6);
}
.hub-emoji {
  font-size: 32px;
  line-height: 1;
  margin-bottom: 4px;
  filter: drop-shadow(0 2px 8px rgba(196,181,253,0.5));
}
.hub-title {
  font-family: var(--serif);
  font-size: 13.5px;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  color: #fff;
  font-weight: 600;
  line-height: 1.1;
}
.hub-count {
  font-family: var(--mono);
  font-size: 9.5px;
  color: #c4b5fd;
  letter-spacing: 0.08em;
  margin-top: 3px;
  max-width: 18ch;
  line-height: 1.2;
}
.hub-cta {
  font-family: var(--mono);
  font-size: 8.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #130a24;
  background: #c4b5fd;
  padding: 3px 8px;
  border-radius: 999px;
  margin-top: 6px;
  font-weight: 600;
}

/* CHAPTER 01 PHOTO COLLAGE STACK */
.chap1-photo-stack {
  position: relative;
  height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.chap1-photo-card {
  position: absolute;
  width: 260px;
  height: 175px;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid rgba(196,181,253,0.3);
  box-shadow: 0 16px 40px rgba(0,0,0,0.7), 0 0 24px rgba(124,58,237,0.25);
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.chap1-photo-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.9);
}
.chap1-photo-card .chap1-badge {
  position: absolute;
  left: 10px;
  bottom: 10px;
  right: 10px;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(13,8,24,0.85);
  backdrop-filter: blur(10px);
  color: #c4b5fd;
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 600;
  border: 1px solid rgba(196,181,253,0.3);
}
.chap1-photo-card.p1 { transform: rotate(-7deg) translate(-40px, -60px); z-index: 1; }
.chap1-photo-card.p2 { transform: rotate(5deg) translate(30px, 10px); z-index: 2; }
.chap1-photo-card.p3 { transform: rotate(-2deg) translate(-10px, 70px); z-index: 3; }
.chap1-photo-stack:hover .chap1-photo-card.p1 { transform: rotate(-10deg) translate(-65px, -80px) scale(1.03); }
.chap1-photo-stack:hover .chap1-photo-card.p2 { transform: rotate(8deg) translate(50px, 15px) scale(1.05); }
.chap1-photo-stack:hover .chap1-photo-card.p3 { transform: rotate(-4deg) translate(-15px, 95px) scale(1.04); }

/* LOCATION AREA QUICK FILTERS */
.area-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 0 14px;
  margin-bottom: 20px;
}
.area-chip {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid var(--line2);
  background: var(--bg2);
  color: var(--muted);
  font-family: var(--mono);
  font-size: 11.5px;
  letter-spacing: 0.08em;
  white-space: nowrap;
  transition: all 0.2s;
}
.area-chip:hover { color: var(--text); background: var(--tint); }
.area-chip.on { background: var(--btn-bg); color: var(--btn-fg); border-color: transparent; font-weight: 600; }"""

assert old_wheel_css in content, "old_wheel_css not found"
content = content.replace(old_wheel_css, new_wheel_css)

# -------------------------------------------------------------
# 4. Update discoverHTML sections: Chapter 01, Chapter 02, Chapter 03, Chapter 04
# -------------------------------------------------------------
old_chap1_to_guilds = """  <!-- CHAPTER 01: Staggered Lines Rise -->
  <section class="sec wrap" style="background:#0a0612;color:#fff;padding:120px clamp(20px,5vw,72px)" id="chap1">
    <div class="kicker" style="color:#c4b5fd;margin-bottom:28px">Chapter 01 · About the problem</div>
    <h2 class="display" style="font-size:clamp(2.4rem,6vw,5.4rem);line-height:1.05">
      <div class="rv" style="margin-left:0">Plans live in the group chat.</div>
      <div class="rv" style="margin-left:clamp(0px, 12vw, 160px);margin-top:14px;color:#c4b5fd">Nobody books them.</div>
      <div class="rv" style="margin-left:clamp(0px, 24vw, 320px);margin-top:14px;color:#ddd6fe">Next weekend, always.</div>
    </h2>
    <p class="rv" style="max-width:44ch;margin:48px 0 0 clamp(0px, 24vw, 320px);color:#b9b3cc;font-size:16px">Someone says football. Someone asks which turf. Three days later the slots are gone. hoppin. puts the venue, the live slot and the price in one place.</p>
  </section>

  <!-- CHAPTER 02 LILAC WIPE & LIVE COUNTDOWN CLOCK -->
  <section class="wipe-container" id="wipeSection">
    <div class="lilac-wipe" id="lilacWipe"></div>
    <div class="bigcountdown" id="bigCountdown" aria-hidden="true">47:59:59</div>
    <div class="wipe-inner wrap">
      <div>
        <div class="kicker">Chapter 02 · Tonight</div>
        <h2 class="display" style="font-size:clamp(2.4rem,5.6vw,4.6rem);margin-top:14px">The clock is running.</h2>
      </div>
      <div>
        <p style="font-size:17px;margin-bottom:24px;max-width:38ch">The floodlights are on across the city. Slots disappear fast once the sun sets. Grab what's open tonight.</p>
        <button class="btn ink" data-act="tonight-on">See what is open tonight ↗</button>
      </div>
    </div>
  </section>

  <!-- CHAPTER 03: Rows with photo spring lerp & cycling headline shield -->
  <section class="sec wrap" id="chap3" style="background:var(--bg3)">
    <div class="sec-h">
      <div>
        <div class="kicker">Chapter 03 · The Journey</div>
        <h2 class="display" style="display:flex;align-items:center;gap:16px">
          It starts as one booking <span id="cycleShield">${totemSVG('check', '#c4b5fd', '#7c3aed', 46)}</span>
        </h2>
      </div>
      <p>Taprooms, board game cafes, floodlit pitches and sunrise run clubs.</p>
    </div>
    <div class="rows">
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">01 · Sports</small><b style="font-size:1.3rem;display:block;margin-top:6px">Book the pitch before it fills up.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">Hourly slots for football, badminton and tennis across Bengaluru and Chennai.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[0])}" alt="Sports"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="sports">Browse sports courts ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">02 · Taprooms</small><b style="font-size:1.3rem;display:block;margin-top:6px">Try the place you always walked past.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">House-brewed craft beers, rooftop gastrobar tables and unhurried evenings.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[12])}" alt="Pubs"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="pubs">Reserve table ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">03 · Gaming</small><b style="font-size:1.3rem;display:block;margin-top:6px">Bring the whole crew and split the bill.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">1,300+ board games, VR simulators and console booths.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[56])}" alt="Gaming"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="gaming">Pick game cafe ↗</button></div>
      </div>
    </div>
  </section>

  <!-- TOTEM INTERACTIVE WORDS & BRACKETS -->
  <section class="totem-stage wrap" id="totemSec">
    <div class="bracket-counter" id="bracketCounter">[ 01 / 06 ]</div>
    <div class="totem-word-mask">
      <div class="totem-word active" id="totemWord">SPORTS & TURFS</div>
    </div>
    <p style="color:var(--muted);font-size:14.5px">Move mouse left or right to switch scenes</p>
  </section>

  <!-- GUILDS SPINNING WHEEL -->
  <section class="guilds-sec wrap" id="guildsSec">
    <div style="text-align:center"><div class="kicker">Chapter 04 · The Guilds</div><h2 class="display" style="font-size:clamp(2.2rem,5vw,4.2rem);margin-top:10px">Choose your arena</h2><p style="color:var(--muted);margin-top:8px">Spin the wheel or scroll fast to accelerate.</p></div>
    <div class="wheel-wrap"><div class="shield-wheel" id="shieldWheel">${buildGuildsWheel()}</div></div>
  </section>"""

new_chap1_to_guilds = """  <!-- CHAPTER 01: Staggered Lines Rise & Problem Showcase Photos -->
  <section class="sec wrap" style="background:#0a0612;color:#fff;padding:120px clamp(20px,5vw,72px)" id="chap1">
    <div class="kicker" style="color:#c4b5fd;margin-bottom:28px">Chapter 01 · About the problem</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:48px;align-items:center">
      <div>
        <h2 class="display" style="font-size:clamp(2.4rem,5.5vw,5rem);line-height:1.05">
          <div class="rv" style="margin-left:0">Plans live in the group chat.</div>
          <div class="rv" style="margin-left:clamp(0px, 8vw, 90px);margin-top:14px;color:#c4b5fd">Nobody books them.</div>
          <div class="rv" style="margin-left:clamp(0px, 16vw, 180px);margin-top:14px;color:#ddd6fe">Next weekend, always.</div>
        </h2>
        <p class="rv" style="max-width:44ch;margin:38px 0 0;color:#b9b3cc;font-size:16px;line-height:1.6">Someone says football. Someone asks which turf. Three days later the slots are gone. hoppin. puts the venue, the live slot and the price in one place with confirmed tickets.</p>
      </div>
      <div class="chap1-photo-stack" aria-label="Visual plans montage">
        <div class="chap1-photo-card p1">
          <img src="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=700&q=80" alt="Floodlit turf">
          <div class="chap1-badge">⚽ Friday 8:00 PM · Turf Booked</div>
        </div>
        <div class="chap1-photo-card p2">
          <img src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=700&q=80" alt="Taproom rooftop">
          <div class="chap1-badge">🍻 Saturday 7:30 PM · Table for 6</div>
        </div>
        <div class="chap1-photo-card p3">
          <img src="https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=700&q=80" alt="Board game shelf">
          <div class="chap1-badge">🎲 Sunday 4:00 PM · 1,300+ Games</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CHAPTER 02 LILAC WIPE & LIVE COUNTDOWN CLOCK -->
  <section class="wipe-container" id="wipeSection">
    <div style="position:absolute;inset:0;background-image:url('https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1400&q=80');background-size:cover;background-position:center;opacity:0.25;mix-blend-mode:luminosity;" aria-hidden="true"></div>
    <div class="lilac-wipe" id="lilacWipe"></div>
    <div class="bigcountdown" id="bigCountdown" aria-hidden="true">47:59:59</div>
    <div class="wipe-inner wrap">
      <div>
        <div class="kicker">Chapter 02 · Tonight</div>
        <h2 class="display" style="font-size:clamp(2.4rem,5.6vw,4.6rem);margin-top:14px">The clock is running.</h2>
      </div>
      <div>
        <p style="font-size:17px;margin-bottom:24px;max-width:38ch">The floodlights are on across the city. Slots disappear fast once the sun sets. Grab what's open tonight.</p>
        <button class="btn ink" data-act="tonight-on">See what is open tonight ↗</button>
      </div>
    </div>
  </section>

  <!-- CHAPTER 03: 6 Category Photo Rows with photo spring lerp & cycling shield -->
  <section class="sec wrap" id="chap3" style="background:var(--bg3)">
    <div class="sec-h">
      <div>
        <div class="kicker">Chapter 03 · The Journey</div>
        <h2 class="display" style="display:flex;align-items:center;gap:16px">
          It starts as one booking <span id="cycleShield">${totemSVG('check', '#c4b5fd', '#7c3aed', 46)}</span>
        </h2>
      </div>
      <p>Taprooms, board game cafes, floodlit pitches and sunrise run clubs.</p>
    </div>
    <div class="rows">
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">01 · Sports & Turfs</small><b style="font-size:1.3rem;display:block;margin-top:6px">Book the pitch before it fills up.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">Hourly slots for football, badminton and tennis across Bengaluru and Chennai.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[0])}" alt="Sports court"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="sports">Browse sports courts ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">02 · Taprooms & Brews</small><b style="font-size:1.3rem;display:block;margin-top:6px">Try the place you always walked past.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">House-brewed craft beers, rooftop gastrobar tables and unhurried evenings.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[12])}" alt="Pubs & Brews"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="pubs">Reserve table ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">03 · Gaming & Arcades</small><b style="font-size:1.3rem;display:block;margin-top:6px">Bring the whole crew and split the bill.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">1,300+ board games, VR simulators, and console booths.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[56])}" alt="Gaming & Board games"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="gaming">Pick game cafe ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">04 · Fitness & Gyms</small><b style="font-size:1.3rem;display:block;margin-top:6px">Sweat hard, then recover in pink salt.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">Luxury clubs, coached CrossFit boxes, and 24/7 strength gyms.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[4])}" alt="Fitness & Gyms"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="fitness">View fitness clubs ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">05 · Dining & Cafes</small><b style="font-size:1.3rem;display:block;margin-top:6px">Slow mornings, sea breeze and herbal coffee.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">Coastal Besant Nagar brunch, wine tables and slow afternoons.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[52])}" alt="Dining & Cafes"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="dining">Explore dining ↗</button></div>
      </div>
      <div class="row3 rv" data-spring-row>
        <div><small class="kicker">06 · Run & Social Clubs</small><b style="font-size:1.3rem;display:block;margin-top:6px">Show up at sunrise. Run together.</b><p style="color:var(--muted);font-size:14.5px;margin-top:10px">5:15 AM Elliot's Beach flyers, Cubbon Park yoga, and weekend cycling peloton.</p></div>
        <div class="th3"><img src="${coverImgURL(VENUES[61])}" alt="Run & Social Clubs"></div>
        <div><button class="btn ghost sm" data-act="catgo" data-cat="clubs">Join a club ↗</button></div>
      </div>
    </div>
  </section>

  <!-- TOTEM INTERACTIVE WORDS & BRACKETS -->
  <section class="totem-stage wrap" id="totemSec">
    <div class="bracket-counter" id="bracketCounter">[ 01 / 06 ]</div>
    <div class="totem-word-mask">
      <div class="totem-word active" id="totemWord">SPORTS & TURFS</div>
    </div>
    <p style="color:var(--muted);font-size:14.5px">Move mouse left or right to switch scenes</p>
  </section>

  <!-- CHAPTER 04: CHOOSE YOUR LOCATION & CIRCULAR SPINNING WHEEL -->
  <section class="guilds-sec wrap" id="guildsSec">
    <div class="kicker" style="color:var(--pastel)">Chapter 04 · Arena Wheel</div>
    <h2 class="display" style="font-size:clamp(2.3rem,5vw,4.4rem);margin-top:10px">Choose Your Arena & Location</h2>
    <p style="color:var(--muted);max-width:54ch;margin:10px auto 0;font-size:15px">Spin the circle, pick a vibe, and see the hottest spots across Bengaluru and Chennai.</p>
    
    <div class="location-selector-bar">
      <div class="seg" id="wheelCitySeg">
        <button class="on" data-act="wheel-city" data-city="all">📍 All Cities (67)</button>
        <button data-act="wheel-city" data-city="BLR">📍 Bengaluru (29)</button>
        <button data-act="wheel-city" data-city="MAA">📍 Chennai (38)</button>
      </div>
      <button class="btn sm" id="spinFastBtn" data-act="spin-fast">🎲 Spin Fast</button>
      <button class="btn sm ghost" data-act="random-pick">⚡ Random Pick</button>
    </div>

    <div class="wheel-stage" id="wheelStage">
      <div class="wheel-outer-ring"></div>
      <div class="circular-disc" id="circularDisc">
        ${buildGuildsWheel()}
      </div>
      <div class="wheel-center-hub" id="wheelCenterHub" data-act="explore-cat">
        <span class="hub-emoji" id="hubEmoji">🏸</span>
        <span class="hub-title" id="hubTitle">SPORTS & TURFS</span>
        <span class="hub-count" id="hubCount">18 Venues · Indiranagar</span>
        <span class="hub-cta">EXPLORE ARENAS ↗</span>
      </div>
    </div>
  </section>"""

assert old_chap1_to_guilds in content, "old_chap1_to_guilds not found"
content = content.replace(old_chap1_to_guilds, new_chap1_to_guilds)

# -------------------------------------------------------------
# 5. Update Directory: Add Area quick-filter chips above the grid
# -------------------------------------------------------------
old_explore_ctrl = """    <div class="ctrl">
      <div class="ctrl-row"><div class="seg" id="cityseg"><button class="on" data-city="all" data-act="city">All (67)</button><button data-city="BLR" data-act="city">Bengaluru (29)</button><button data-city="MAA" data-act="city">Chennai (38)</button></div></div>
      <div class="ctrl-row">
        <label class="search"><span class="sr">Search</span>${IC.search}<input id="q" type="search" placeholder="Search venues, sports, areas…" value="${esc(S.q)}"></label>
        <button class="pill" data-act="tonight-toggle">Open today</button>
      </div>
      <div class="pills" id="catpills">
        <button class="pill on" data-act="cat" data-cat="all">All</button>
        ${Object.entries(CATS).map(([k, c]) => `<button class="pill" data-act="cat" data-cat="${k}">${c.label}</button>`).join('')}
      </div>
    </div>"""

new_explore_ctrl = """    <div class="ctrl">
      <div class="ctrl-row"><div class="seg" id="cityseg"><button class="on" data-city="all" data-act="city">All (67)</button><button data-city="BLR" data-act="city">Bengaluru (29)</button><button data-city="MAA" data-act="city">Chennai (38)</button></div></div>
      <div class="ctrl-row">
        <label class="search"><span class="sr">Search</span>${IC.search}<input id="q" type="search" placeholder="Search venues, sports, areas…" value="${esc(S.q)}"></label>
        <button class="pill" data-act="tonight-toggle">Open today</button>
      </div>
      <div class="pills" id="catpills">
        <button class="pill on" data-act="cat" data-cat="all">All Arenas</button>
        ${Object.entries(CATS).map(([k, c]) => `<button class="pill" data-act="cat" data-cat="${k}">${c.label}</button>`).join('')}
      </div>
      <div class="area-chips" id="areaChips">
        <button class="area-chip on" data-act="area" data-area="all">📍 All Neighborhoods</button>
        <button class="area-chip" data-act="area" data-area="Indiranagar">Indiranagar (11)</button>
        <button class="area-chip" data-act="area" data-area="Koramangala">Koramangala (6)</button>
        <button class="area-chip" data-act="area" data-area="Kilpauk">Kilpauk (4)</button>
        <button class="area-chip" data-act="area" data-area="Adyar">Adyar (7)</button>
        <button class="area-chip" data-act="area" data-area="T. Nagar">T. Nagar (5)</button>
        <button class="area-chip" data-act="area" data-area="Besant Nagar">Besant Nagar (3)</button>
        <button class="area-chip" data-act="area" data-area="Velachery">Velachery (4)</button>
        <button class="area-chip" data-act="area" data-area="Whitefield">Whitefield (3)</button>
        <button class="area-chip" data-act="area" data-area="OMR">OMR (3)</button>
      </div>
    </div>"""

assert old_explore_ctrl in content, "old_explore_ctrl not found"
content = content.replace(old_explore_ctrl, new_explore_ctrl)

# -------------------------------------------------------------
# 6. Update S state to include area filter and update renderGrid
# -------------------------------------------------------------
old_state = "const S={user:null,city:'all',cat:'all',q:'',sort:'rating',tonight:false,view:'discover',chatCity:'BLR',chat:[],lastHits:[],pending:null,maxp:0,minr:0,geo:null};"
new_state = "const S={user:null,city:'all',cat:'all',area:'all',q:'',sort:'rating',tonight:false,view:'discover',chatCity:'BLR',chat:[],lastHits:[],pending:null,maxp:0,minr:0,geo:null};"
content = content.replace(old_state, new_state)

old_render_grid = """function renderGrid(){
  const q=S.q.trim().toLowerCase();
  let list=VENUES.filter(v=>{
    if(S.city!=='all'&&v.city!==S.city)return false;
    if(S.cat!=='all'&&v.cat!==S.cat)return false;
    if(S.tonight&&!openTonight(v).length)return false;
    if(q){const hay=(v.name+' '+v.area+' '+CITY[v.city].name+' '+CATS[v.cat].label).toLowerCase();if(!hay.includes(q))return false;}
    return true;
  });
  $('#count').textContent=`SHOWING ${list.length} VENUES`;
  $('#grid').innerHTML=list.map(cardHTML).join('');
  $$('#cityseg button').forEach(b=>b.classList.toggle('on',b.dataset.city===S.city));
  $$('#catpills .pill').forEach(b=>b.classList.toggle('on',b.dataset.cat===S.cat));
}"""

new_render_grid = """function renderGrid(){
  const q=S.q.trim().toLowerCase();
  let list=VENUES.filter(v=>{
    if(S.city!=='all'&&v.city!==S.city)return false;
    if(S.cat!=='all'&&v.cat!==S.cat)return false;
    if(S.area&&S.area!=='all'&&!v.area.toLowerCase().includes(S.area.toLowerCase()))return false;
    if(S.tonight&&!openTonight(v).length)return false;
    if(q){const hay=(v.name+' '+v.area+' '+CITY[v.city].name+' '+CATS[v.cat].label).toLowerCase();if(!hay.includes(q))return false;}
    return true;
  });
  const countEl=$('#count');
  if(countEl)countEl.textContent=`SHOWING ${list.length} OF ${VENUES.length} REAL VENUES WITH HIGH-RES PHOTOS`;
  const gridEl=$('#grid');
  if(gridEl)gridEl.innerHTML=list.length?list.map(cardHTML).join(''):'<div style="grid-column:1/-1;text-align:center;padding:60px 20px;color:var(--muted)"><p style="font-size:18px">No venues found for this filter.</p><button class="btn sm" style="margin-top:14px" onclick="S.city=\\'all\\';S.cat=\\'all\\';S.area=\\'all\\';S.q=\\'\\';renderGrid();">Reset all filters</button></div>';
  $$('#cityseg button').forEach(b=>b.classList.toggle('on',b.dataset.city===S.city));
  $$('#catpills .pill').forEach(b=>b.classList.toggle('on',b.dataset.cat===S.cat));
  $$('#areaChips .area-chip').forEach(b=>b.classList.toggle('on',b.dataset.area===(S.area||'all')));
}"""

assert old_render_grid in content, "old_render_grid not found"
content = content.replace(old_render_grid, new_render_grid)

# -------------------------------------------------------------
# 7. Add click handlers inside switch(act)
# -------------------------------------------------------------
old_cases = """    case 'catgo':S.cat=a.dataset.cat;renderGrid();$('#explore')?.scrollIntoView({behavior:'smooth'});break;"""

new_cases = """    case 'catgo':S.cat=a.dataset.cat;renderGrid();$('#explore')?.scrollIntoView({behavior:'smooth'});break;
    case 'wheel-item':{
      const cat=a.dataset.cat;
      updateWheelCenter(cat);
      S.cat=cat;
      renderGrid();
      break;
    }
    case 'spin-fast':spinWheelFast();break;
    case 'random-pick':{
      const catKeys=Object.keys(GUILD_DATA);
      const chosenCat=catKeys[Math.floor(Math.random()*catKeys.length)];
      updateWheelCenter(chosenCat);
      S.cat=chosenCat;
      renderGrid();
      toast(`Selected ${GUILD_DATA[chosenCat].label} ⚡`);
      $('#explore')?.scrollIntoView({behavior:'smooth'});
      break;
    }
    case 'wheel-city':{
      const city=a.dataset.city;
      S.city=city;
      $$('#wheelCitySeg button').forEach(b=>b.classList.toggle('on',b.dataset.city===city));
      $$('#cityseg button').forEach(b=>b.classList.toggle('on',b.dataset.city===city));
      renderGrid();
      toast(`Filtered locations to ${city==='all'?'All Cities':city==='BLR'?'Bengaluru':'Chennai'}`);
      break;
    }
    case 'explore-cat':$('#explore')?.scrollIntoView({behavior:'smooth'});break;
    case 'area':S.area=a.dataset.area;renderGrid();break;"""

assert old_cases in content, "old_cases not found"
content = content.replace(old_cases, new_cases)

# -------------------------------------------------------------
# 8. Update initGuilds to support circular rotation & mouse hover
# -------------------------------------------------------------
old_init_guilds = """/* Guilds Wheel Spinning & Acceleration */
function initGuilds(){
  const wheel=$('#shieldWheel');
  const sec=$('#guildsSec');
  if(!wheel||!sec)return;
  let angle=0, speed=0.4;
  function spin(){
    angle+=speed;
    speed=Math.max(0.4, speed*0.96);
    wheel.style.transform=`rotate(${angle}deg)`;
    requestAnimationFrame(spin);
  }
  spin();

  window.addEventListener('scroll',()=>{
    speed+=0.8;
  },{passive:true});
}"""

new_init_guilds = """/* Guilds Circular Wheel Interaction */
function initGuilds(){
  const disc=$('#circularDisc');
  const sec=$('#guildsSec');
  if(!disc||!sec)return;

  updateWheelCenter('sports');

  let autoSpeed=0.18;
  function idleRotate(){
    if(!isSpinningWheel){
      wheelRotation += autoSpeed;
      disc.style.transform = `rotate(${wheelRotation}deg)`;
    }
    requestAnimationFrame(idleRotate);
  }
  idleRotate();

  window.addEventListener('scroll',()=>{
    if(!isSpinningWheel){
      wheelRotation += 1.4;
    }
  },{passive:true});

  // Hover over item slows down and shows preview
  $$('.circle-item').forEach(item=>{
    item.addEventListener('mouseenter',()=>{
      autoSpeed = 0.04;
      updateWheelCenter(item.dataset.cat);
    });
    item.addEventListener('mouseleave',()=>{
      autoSpeed = 0.18;
    });
  });
}"""

assert old_init_guilds in content, "old_init_guilds not found"
content = content.replace(old_init_guilds, new_init_guilds)

# Write updated build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated build_fullstack_frontend.py successfully!")

# Run it to write to all target files
res = subprocess.run(["python", "build_fullstack_frontend.py"], capture_output=True, text=True)
print("Execution result:", res.stdout, res.stderr)
