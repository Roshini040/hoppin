# Script to format Chapter 01 compact small overlapping cards and ensure 3D wheel has images
import os
import subprocess

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure chap1-photo-stack CSS is present
chap1_css = """
/* CHAPTER 01 COMPACT OVERLAPPING CARDS */
.chap1-photo-stack {
  position: relative;
  width: 210px;
  height: 180px;
  margin: 10px auto 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.chap1-photo-card {
  position: absolute;
  width: 155px;
  height: 110px;
  border-radius: 14px;
  overflow: hidden;
  border: 1.5px solid rgba(196,181,253,0.4);
  box-shadow: 0 14px 30px rgba(0,0,0,0.8), 0 0 20px rgba(124,58,237,0.3);
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
  background: #110b1e;
}
.chap1-photo-card img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.9);
}
.chap1-photo-card .chap1-badge {
  position: absolute;
  left: 6px;
  bottom: 6px;
  right: 6px;
  padding: 4px 8px;
  border-radius: 999px;
  background: rgba(13,8,24,0.92);
  backdrop-filter: blur(8px);
  color: #c4b5fd;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 600;
  border: 1px solid rgba(196,181,253,0.3);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  z-index: 2;
}
.chap1-photo-card.p1 { transform: rotate(-8deg) translate(-22px, -20px); z-index: 1; }
.chap1-photo-card.p2 { transform: rotate(5deg) translate(16px, -4px); z-index: 2; }
.chap1-photo-card.p3 { transform: rotate(-2deg) translate(-4px, 18px); z-index: 3; }
.chap1-photo-stack:hover .chap1-photo-card.p1 { transform: rotate(-12deg) translate(-36px, -28px) scale(1.04); }
.chap1-photo-stack:hover .chap1-photo-card.p2 { transform: rotate(8deg) translate(28px, -6px) scale(1.05); }
.chap1-photo-stack:hover .chap1-photo-card.p3 { transform: rotate(-4deg) translate(-6px, 30px) scale(1.04); }
"""

# Place chap1_css right before /* STATS INTERACTIVE 2D PHYSICS BALLS
if ".chap1-photo-stack" not in content:
    idx = content.find("/* STATS INTERACTIVE 2D PHYSICS BALLS")
    if idx != -1:
        content = content[:idx] + chap1_css + "\n" + content[idx:]
        print("Added chap1 CSS.")
    else:
        print("Warning: stats marker not found for CSS insertion.")
else:
    print("chap1 CSS already present.")

# 2. Update Chapter 01 HTML to have smooth flex-wrap layout
old_chap1_html = """  <!-- CHAPTER 01: Staggered Lines Rise & Problem Showcase Photos -->
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
  </section>"""

new_chap1_html = """  <!-- CHAPTER 01: Staggered Lines Rise & Problem Showcase Photos -->
  <section class="sec wrap" style="background:#0a0612;color:#fff;padding:120px clamp(20px,5vw,72px)" id="chap1">
    <div class="kicker" style="color:#c4b5fd;margin-bottom:28px">Chapter 01 · About the problem</div>
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:40px">
      <div style="flex:1;min-width:min(440px, 100%)">
        <h2 class="display" style="font-size:clamp(2.4rem,5.5vw,5rem);line-height:1.05">
          <div class="rv" style="margin-left:0">Plans live in the group chat.</div>
          <div class="rv" style="margin-left:clamp(0px, 8vw, 90px);margin-top:14px;color:#c4b5fd">Nobody books them.</div>
          <div class="rv" style="margin-left:clamp(0px, 16vw, 180px);margin-top:14px;color:#ddd6fe">Next weekend, always.</div>
        </h2>
        <p class="rv" style="max-width:44ch;margin:38px 0 0;color:#b9b3cc;font-size:16px;line-height:1.6">Someone says football. Someone asks which turf. Three days later the slots are gone. hoppin. puts the venue, the live slot and the price in one place with confirmed tickets.</p>
      </div>
      <div class="chap1-photo-stack" aria-label="Visual plans montage">
        <div class="chap1-photo-card p1">
          <img src="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=500&q=80" alt="Turf">
          <div class="chap1-badge">⚽ Fri 8 PM · Turf Booked</div>
        </div>
        <div class="chap1-photo-card p2">
          <img src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=500&q=80" alt="Taproom">
          <div class="chap1-badge">🍻 Sat 7:30 PM · Table for 6</div>
        </div>
        <div class="chap1-photo-card p3">
          <img src="https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=500&q=80" alt="Games">
          <div class="chap1-badge">🎲 Sun 4 PM · 1,300+ Games</div>
        </div>
      </div>
    </div>
  </section>"""

if old_chap1_html in content:
    content = content.replace(old_chap1_html, new_chap1_html)
    print("Updated Chapter 01 HTML layout.")
else:
    print("Warning: old_chap1_html not matched exactly, checking if already updated.")

# Save updated build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(content)

# Execute build_fullstack_frontend.py to update all target files
res = subprocess.run(["python", "build_fullstack_frontend.py"], capture_output=True, text=True)
print("Regeneration output:", res.stdout, res.stderr)
