# Revert spin wheel to the original 3D shield wheel, but with category photos and emojis inside each shield
import os
import subprocess

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS: replace guilds circular CSS with the 3D shield wheel CSS (with image support)
guilds_css_search = """/* =========================================================
   GUILDS & LOCATION TRUE CIRCULAR SPINNER
   ========================================================= */"""

# Find start of guilds CSS and end before stats-physics-sec
start_css = content.find("/* =========================================================\n   GUILDS & LOCATION TRUE CIRCULAR SPINNER")
if start_css == -1:
    start_css = content.find(".guilds-sec {")
end_css = content.find("/* STATS INTERACTIVE 2D PHYSICS BALLS")

new_3d_wheel_css = """/* =========================================================
   GUILDS 3D WHEEL OF 6 SHIELDS WITH IMAGES & EMOJIS
   ========================================================= */
.guilds-sec {
  padding: clamp(70px, 9vw, 120px) clamp(20px, 5vw, 72px);
  background: var(--bg);
  position: relative;
  text-align: center;
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
  width: 96px;
  height: 122px;
  margin-left: -48px;
  margin-top: -61px;
  transform: rotate(var(--angle)) translateY(-165px) rotate(calc(-1 * var(--angle)));
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.3s;
}
.wheel-item:hover {
  transform: rotate(var(--angle)) translateY(-185px) rotate(calc(-1 * var(--angle))) scale(1.18);
  filter: drop-shadow(0 0 24px rgba(196,181,253,0.75));
}
.shield-frame {
  filter: drop-shadow(0 10px 24px rgba(0,0,0,0.65));
  transition: transform 0.3s ease;
}
.wheel-item:hover .shield-frame {
  transform: scale(1.06);
}
.wheel-item span {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text);
  font-weight: 600;
  white-space: nowrap;
}

"""

if start_css != -1 and end_css != -1:
    content = content[:start_css] + new_3d_wheel_css + content[end_css:]
    print("Replaced wheel CSS successfully.")
else:
    print(f"Warning: CSS markers not found ({start_css}, {end_css})")

# 2. Update buildGuildsWheel: original 3D wheel items with image and emoji inside the shield
start_js = content.find("/* =========================================================\n   GUILDS & ARENA CIRCULAR WHEEL DATA & INTERACTION")
if start_js == -1:
    start_js = content.find("const GUILD_DATA = {")
end_js = content.find("/* =========================================================\n   DISCOVER VIEW HTML")

new_3d_wheel_js = """/* =========================================================
   GUILDS 3D WHEEL WITH IMAGES & EMOJIS INSIDE SHIELDS
   ========================================================= */
const GUILD_DATA = {
  sports: { emoji: '🏸', label: 'Sports & Turfs', img: 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=400&q=80' },
  pubs: { emoji: '🍺', label: 'Pubs & Brews', img: 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=400&q=80' },
  fitness: { emoji: '🏋️', label: 'Fitness & Gyms', img: 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=400&q=80' },
  dining: { emoji: '☕', label: 'Dining & Cafes', img: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=400&q=80' },
  gaming: { emoji: '🎲', label: 'Gaming & Arcades', img: 'https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=400&q=80' },
  clubs: { emoji: '🏃', label: 'Run & Social Clubs', img: 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=400&q=80' }
};

function buildGuildsWheel() {
  const cats = Object.entries(CATS);
  const total = cats.length;
  return cats.map(([k, c], i) => {
    const angle = (i / total) * 360;
    const g = GUILD_DATA[k] || { emoji: '✨', img: 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=400&q=80' };
    return `<div class="wheel-item" style="--angle:${angle}deg" data-act="catgo" data-cat="${k}" tabindex="0" role="button" aria-label="${c.label}">
      <div class="shield-frame">
        <svg viewBox="0 0 100 112" width="86" height="98" aria-hidden="true">
          <defs>
            <clipPath id="sc-${k}">
              <path d="M50 3 L95 14 V54 C95 80 75 96 50 110 C25 96 5 80 5 54 V14 Z"/>
            </clipPath>
          </defs>
          <path d="M50 3 L95 14 V54 C95 80 75 96 50 110 C25 96 5 80 5 54 V14 Z" fill="#130a24" stroke="#c4b5fd" stroke-width="2.5"/>
          <image href="${g.img}" x="0" y="0" width="100" height="112" preserveAspectRatio="xMidYMid slice" clip-path="url(#sc-${k})"/>
          <circle cx="50" cy="52" r="18" fill="rgba(13,8,24,0.75)" stroke="#c4b5fd" stroke-width="1.8"/>
          <text x="50" y="58" text-anchor="middle" font-size="16">${g.emoji}</text>
        </svg>
      </div>
      <span>${c.label}</span>
    </div>`;
  }).join('');
}

"""

if start_js != -1 and end_js != -1:
    content = content[:start_js] + new_3d_wheel_js + content[end_js:]
    print("Replaced wheel JS successfully.")
else:
    print(f"Warning: JS markers not found ({start_js}, {end_js})")

# 3. Update discoverHTML Chapter 04 Section: revert to the 3D spinning wheel container
start_sec = content.find("<!-- CHAPTER 04: CHOOSE YOUR LOCATION & CIRCULAR SPINNING WHEEL -->")
end_sec = content.find("<!-- STATS INTERACTIVE 2D PHYSICS BALLS")

new_3d_wheel_html = """<!-- CHAPTER 04: GUILDS 3D SPINNING WHEEL -->
  <section class="guilds-sec wrap" id="guildsSec">
    <div style="text-align:center">
      <div class="kicker">Chapter 04 · The Guilds</div>
      <h2 class="display" style="font-size:clamp(2.2rem,5vw,4.2rem);margin-top:10px">Choose your arena</h2>
      <p style="color:var(--muted);margin-top:8px">Spin the wheel or scroll fast to accelerate.</p>
    </div>
    <div class="wheel-wrap">
      <div class="shield-wheel" id="shieldWheel">
        ${buildGuildsWheel()}
      </div>
    </div>
  </section>

  """

if start_sec != -1 and end_sec != -1:
    content = content[:start_sec] + new_3d_wheel_html + content[end_sec:]
    print("Replaced wheel HTML successfully.")
else:
    print(f"Warning: HTML markers not found ({start_sec}, {end_sec})")

# 4. Revert initGuilds to original 3D spinning motion with speed acceleration on scroll
start_init = content.find("/* Guilds Circular Wheel Interaction */")
end_init = content.find("/* Totems Word Rise & Squeezing Brackets */")

new_init_guilds = """/* Guilds 3D Wheel Spin & Scroll Acceleration */
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
}

"""

if start_init != -1 and end_init != -1:
    content = content[:start_init] + new_init_guilds + content[end_init:]
    print("Replaced initGuilds successfully.")
else:
    print(f"Warning: initGuilds markers not found ({start_init}, {end_init})")

# Save updated build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_fullstack_frontend.py!")

# Run it to regenerate all target files
res = subprocess.run(["python", "build_fullstack_frontend.py"], capture_output=True, text=True)
print("Execution output:", res.stdout, res.stderr)
