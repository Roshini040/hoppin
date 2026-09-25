# Build complete Grail Lilac Edition with all 7 requested movements
import os

html_code = r"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>hoppin. — discover real places</title>
<meta name="description" content="Discover and book courts, turfs, gyms, taprooms, game cafes and run clubs across Bengaluru and Chennai.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<script>
try{var t=localStorage.getItem('hoppin.theme');t=t?JSON.parse(t):'dark';document.documentElement.setAttribute('data-theme',t==='light'?'light':'dark');}catch(e){}
</script>
<style>
/* =========================================================
   LILAC THEME TOKENS — Grail aesthetic
   ========================================================= */
:root {
  --bg: #f8f6fc;
  --bg2: #ffffff;
  --bg3: #f0eaf8;
  --text: #0d0818;
  --muted: #645e75;
  --line: rgba(13,8,24,0.10);
  --line2: rgba(139,92,246,0.22);
  --glass: rgba(248,246,252,0.85);
  --btn-bg: #1e1333;
  --btn-fg: #f5f3ff;
  --tint: #ede9fe;
  --tint-fg: #6d28d9;
  --pastel: #c4b5fd; /* Primary Lilac */
  --ink: #0d0818;
  --gold: #f0b94a;
  --ok: #10b981;
  --warn: #f59e0b;
  --bad: #ef4444;
  --shadow: 0 24px 70px rgba(124,58,237,0.14);
  --focus: #7c3aed;
  --serif: 'Bodoni Moda','Didot','Bodoni 72',Georgia,serif;
  --sans: 'Plus Jakarta Sans',system-ui,-apple-system,sans-serif;
  --mono: 'Space Grotesk',ui-monospace,Menlo,monospace;
  color-scheme: light;
  box-sizing: border-box;
}

:root[data-theme="dark"],
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #07050a; /* Obsidian Violet Noir */
    --bg2: #0f0b18;
    --bg3: #181226;
    --text: #faf8ff;
    --muted: #a49ebd;
    --line: rgba(255,255,255,0.10);
    --line2: rgba(196,181,253,0.24);
    --glass: rgba(15,11,24,0.82);
    --btn-bg: #c4b5fd;
    --btn-fg: #130a24;
    --tint: rgba(196,181,253,0.16);
    --tint-fg: #ddd6fe;
    --pastel: #c4b5fd;
    --ink: #07050a;
    --shadow: 0 24px 80px rgba(0,0,0,0.85);
    --focus: #c4b5fd;
    color-scheme: dark;
  }
}

:root[data-theme="dark"] {
  --bg: #07050a;
  --bg2: #0f0b18;
  --bg3: #181226;
  --text: #faf8ff;
  --muted: #a49ebd;
  --line: rgba(255,255,255,0.10);
  --line2: rgba(196,181,253,0.24);
  --glass: rgba(15,11,24,0.82);
  --btn-bg: #c4b5fd;
  --btn-fg: #130a24;
  --tint: rgba(196,181,253,0.16);
  --tint-fg: #ddd6fe;
  --pastel: #c4b5fd;
  --ink: #07050a;
  --shadow: 0 24px 80px rgba(0,0,0,0.85);
  --focus: #c4b5fd;
  color-scheme: dark;
}

html {
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}
html.lock, html.lock body { overflow: hidden; }
*, *::before, *::after { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  font-size: 16px;
  line-height: 1.55;
  transition: background 0.45s ease, color 0.45s ease;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

button, input, select { font: inherit; color: inherit; }
button { cursor: pointer; background: none; border: 0; padding: 0; }
a { color: inherit; text-decoration: none; }
:focus-visible { outline: 2px solid var(--focus); outline-offset: 3px; border-radius: 8px; }
h1, h2, h3, p { margin: 0; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Type */
.display { font-family: var(--serif); font-weight: 400; text-transform: uppercase; letter-spacing: -0.02em; line-height: 0.95; font-optical-sizing: auto; }
.kicker { font-family: var(--mono); font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted); font-weight: 500; }
.mono { font-family: var(--mono); }

/* =========================================================
   HEADER FLOATING PILL (Intelligent section-sensor)
   ========================================================= */
.hdr {
  position: fixed;
  top: calc(14px + env(safe-area-inset-top, 0px));
  left: 50%;
  transform: translateX(-50%);
  z-index: 60;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 7px 8px 7px 22px;
  border-radius: 999px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(24px);
  backdrop-filter: blur(24px);
  border: 1px solid var(--line2);
  max-width: calc(100% - 24px);
  box-shadow: 0 10px 40px rgba(0,0,0,0.25);
  transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.hdr.on-light {
  background: rgba(255, 255, 255, 0.92);
  border-color: rgba(124, 58, 237, 0.25);
  box-shadow: 0 10px 35px rgba(124, 58, 237, 0.15);
}
.hdr.on-lilac {
  background: rgba(15, 11, 24, 0.92);
  border-color: #c4b5fd;
  box-shadow: 0 10px 40px rgba(124, 58, 237, 0.4);
}
.brand { display: flex; align-items: baseline; gap: 12px; margin-right: 14px; white-space: nowrap; }
.brand b { font-family: var(--serif); font-weight: 500; font-size: 24px; letter-spacing: -0.03em; line-height: 1; }
.brand span { font-family: var(--mono); font-size: 10.5px; letter-spacing: 0.18em; color: var(--muted); text-transform: uppercase; }
.nav { display: flex; gap: 2px; }
.nav a {
  padding: 9px 15px;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  transition: all 0.2s;
  white-space: nowrap;
}
.nav a:hover { color: var(--text); }
.nav a.on { background: var(--btn-bg); color: var(--btn-fg); }
.hdr .sep { width: 1px; height: 22px; background: var(--line); margin: 0 6px; }
.icon-btn { width: 38px; height: 38px; border-radius: 50%; display: grid; place-items: center; border: 1px solid var(--line); transition: background 0.2s; }
.icon-btn:hover { background: var(--tint); }
.icon-btn svg { width: 18px; height: 18px; }
.acct {
  height: 38px;
  padding: 0 16px;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  background: var(--tint);
  color: var(--tint-fg);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  font-weight: 600;
}
.acct .av {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--btn-bg);
  color: var(--btn-fg);
  display: grid;
  place-items: center;
  font-family: var(--serif);
  font-size: 13px;
  text-transform: uppercase;
}
.acct.has { padding: 0 14px 0 6px; }

.bnav {
  display: none;
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(12px + env(safe-area-inset-bottom, 0px));
  z-index: 60;
  padding: 6px;
  gap: 2px;
  border-radius: 999px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(24px);
  backdrop-filter: blur(24px);
  border: 1px solid var(--line2);
  box-shadow: 0 14px 44px rgba(0,0,0,0.35);
  width: min(400px, calc(100% - 20px));
}
.bnav a {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  padding: 8px 2px 7px;
  border-radius: 999px;
  color: var(--muted);
  font-family: var(--mono);
  font-size: 9.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: all 0.2s;
  min-width: 0;
}
.bnav a svg { width: 20px; height: 20px; }
.bnav a.on { background: var(--btn-bg); color: var(--btn-fg); }

.floatcta {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(24px + env(safe-area-inset-bottom, 0px));
  z-index: 55;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 22px;
  border-radius: 999px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(24px);
  backdrop-filter: blur(24px);
  border: 1px solid var(--line2);
  font-family: var(--mono);
  font-size: 11.5px;
  letter-spacing: 0.1em;
  box-shadow: 0 14px 44px rgba(0,0,0,0.3);
  transition: transform 0.25s, background 0.3s;
}
.floatcta:hover { transform: translateX(-50%) translateY(-3px); }
.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--pastel);
  box-shadow: 0 0 0 0 var(--pastel);
  animation: pulse 2.2s infinite;
}
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(196,181,253,0.6); }
  70% { box-shadow: 0 0 0 10px rgba(196,181,253,0); }
  100% { box-shadow: 0 0 0 0 rgba(196,181,253,0); }
}

/* =========================================================
   MOVEMENT 2: 3D OPENING BOOK LOADER
   ========================================================= */
#loader {
  position: fixed;
  inset: 0;
  z-index: 500;
  background: #06040a;
  display: grid;
  place-items: center;
  perspective: 1400px;
  transition: opacity 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}
#loader.off { opacity: 0; pointer-events: none; }

.book-stage {
  perspective: 1200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.book {
  position: relative;
  width: 240px;
  height: 330px;
  transform-style: preserve-3d;
  transition: transform 0.9s cubic-bezier(0.2, 0.85, 0.25, 1);
  box-shadow: 0 30px 80px rgba(0,0,0,0.8), 0 0 50px rgba(139,92,246,0.3);
  border-radius: 12px;
}

.book-cover {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #1b122e 0%, #0d0818 100%);
  border: 1px solid rgba(196,181,253,0.4);
  border-radius: 12px;
  transform-origin: left center;
  transform-style: preserve-3d;
  transition: transform 0.9s cubic-bezier(0.2, 0.85, 0.25, 1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 24px;
  backface-visibility: hidden;
  box-shadow: inset 4px 0 10px rgba(0,0,0,0.5);
}

.book-cover::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 14px;
  background: linear-gradient(90deg, rgba(0,0,0,0.6), transparent);
  border-radius: 12px 0 0 12px;
}

.book-page {
  position: absolute;
  inset: 0;
  background: var(--pastel);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--ink);
  padding: 24px;
  box-shadow: inset 6px 0 12px rgba(0,0,0,0.2);
}

.book.open .book-cover {
  transform: rotateY(-130deg);
}

.book.open {
  transform: translateX(80px) scale(2.4);
}

.book-monogram {
  font-family: var(--serif);
  font-size: 3.2rem;
  color: var(--pastel);
  letter-spacing: -0.04em;
  text-shadow: 0 0 20px rgba(196,181,253,0.5);
}

.loader-progress {
  font-family: var(--mono);
  font-size: 13px;
  letter-spacing: 0.2em;
  color: #c4b5fd;
  text-transform: uppercase;
}

/* =========================================================
   MOVEMENT 1: HERO 3D SPIRAL OF 18 BENT CARDS & PARALLAX
   ========================================================= */
.hero {
  position: relative;
  min-height: 100svh;
  display: flex;
  align-items: center;
  padding: 130px clamp(20px, 5vw, 72px) 80px;
  background: #07050a;
  color: #fff;
  overflow: hidden;
  perspective: 1200px;
}

.hero-content {
  position: relative;
  z-index: 10;
  max-width: 680px;
  transition: transform 0.3s ease-out, opacity 0.3s ease-out;
}

.mega {
  font-size: clamp(3.2rem, 9.2vw, 8.8rem);
  line-height: 0.92;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}

.mega span.char {
  display: inline-block;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.mega.in span.char {
  opacity: 1;
  transform: none;
}

.hero .sub {
  max-width: 48ch;
  margin-top: 28px;
  font-size: clamp(16px, 1.4vw, 18px);
  color: #b9b3cc;
}

.hero-spiral {
  position: absolute;
  right: clamp(-80px, 4vw, 40px);
  top: 50%;
  width: 580px;
  height: 580px;
  transform: translateY(-50%);
  transform-style: preserve-3d;
  pointer-events: none;
  transition: transform 0.4s ease-out;
}

.spiral-ring {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  animation: slowSpiral 32s linear infinite;
}

@keyframes slowSpiral {
  0% { transform: rotateY(0deg) rotateX(12deg); }
  100% { transform: rotateY(360deg) rotateX(12deg); }
}

.spiral-card {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 110px;
  height: 150px;
  margin-left: -55px;
  margin-top: -75px;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid rgba(196,181,253,0.3);
  box-shadow: 0 14px 35px rgba(0,0,0,0.6), 0 0 20px rgba(124,58,237,0.25);
  transform: translate3d(var(--tx), var(--ty), var(--tz)) rotateY(var(--ry)) rotateX(var(--rx));
  transform-style: preserve-3d;
  background: #110b1e;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.spiral-card img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.9);
}
.spiral-card .badge-overlay {
  position: absolute;
  left: 6px;
  bottom: 6px;
  right: 6px;
  font-family: var(--mono);
  font-size: 8.5px;
  letter-spacing: 0.05em;
  color: #fff;
  text-shadow: 0 1px 4px rgba(0,0,0,0.8);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  z-index: 2;
}

/* =========================================================
   MOVEMENT 3: CHAPTER 02 LILAC WIPE & COUNTDOWN CLOCK
   ========================================================= */
.wipe-container {
  position: relative;
  background: #07050a;
  overflow: hidden;
  padding: clamp(90px, 12vw, 160px) clamp(20px, 5vw, 72px);
}

.lilac-wipe {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, #c4b5fd 0%, #a78bfa 60%, #7c3aed 100%);
  clip-path: circle(var(--wipe-radius, 15%) at 50% 50%);
  transition: clip-path 0.1s linear;
  z-index: 1;
}

.wipe-inner {
  position: relative;
  z-index: 2;
  color: var(--ink);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
  min-height: 480px;
}

.bigcountdown {
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  text-align: center;
  font-family: var(--serif);
  font-size: clamp(4.8rem, 20vw, 18rem);
  line-height: 1;
  letter-spacing: -0.04em;
  color: rgba(13, 8, 24, 0.14);
  font-variant-numeric: tabular-nums lining-nums;
  white-space: nowrap;
  pointer-events: none;
  user-select: none;
  z-index: 1;
}

/* =========================================================
   MOVEMENT 4: GUILDS SPINNING WHEEL OF 6 SHIELDS
   ========================================================= */
.guilds-sec {
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
}

/* =========================================================
   MOVEMENT 5: STATS INTERACTIVE 2D PHYSICS BALLS
   ========================================================= */
.stats-physics-sec {
  padding: clamp(60px, 8vw, 100px) clamp(20px, 5vw, 72px);
  background: var(--bg2);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  position: relative;
}

.physics-stage {
  position: relative;
  width: 100%;
  max-width: 900px;
  height: 380px;
  margin: 30px auto 0;
  border-radius: 24px;
  background: #08050e;
  overflow: hidden;
  box-shadow: inset 0 0 40px rgba(0,0,0,0.8), 0 20px 60px rgba(124,58,237,0.12);
  border: 1px solid var(--line2);
  cursor: pointer;
}

#ballsCanvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.stats-overlay-grid {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  pointer-events: none;
  border-top: 1px dashed rgba(196,181,253,0.15);
}

.stat-bucket {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 18px;
  border-right: 1px solid rgba(196,181,253,0.12);
}
.stat-bucket:last-child { border-right: none; }
.stat-bucket b {
  font-family: var(--serif);
  font-size: 2.2rem;
  color: #fff;
  line-height: 1;
}
.stat-bucket span {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #c4b5fd;
  margin-top: 4px;
}

/* =========================================================
   MOVEMENT 6: PLAYFUL TALKING EMAIL WAITLIST & LIGHT RAYS
   ========================================================= */
footer.ft {
  position: relative;
  padding: 100px clamp(20px, 5vw, 72px) 150px;
  border-top: 1px solid var(--line2);
  background: #07050a;
  color: #fff;
  overflow: hidden;
}

.rays-card {
  position: relative;
  max-width: 720px;
  margin: 0 auto 60px;
  padding: 44px;
  border-radius: 28px;
  background: rgba(18, 12, 30, 0.7);
  border: 1px solid rgba(196,181,253,0.25);
  box-shadow: 0 20px 70px rgba(0,0,0,0.6);
  overflow: hidden;
  text-align: center;
}

.light-rays {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(circle 350px at var(--ray-x, 50%) var(--ray-y, 50%), rgba(196,181,253,0.28), transparent 70%);
  transition: background 0.1s ease;
}

.talking-badge {
  display: inline-block;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #c4b5fd;
  margin-bottom: 14px;
  transition: all 0.25s;
}

.waitlist-form {
  display: flex;
  gap: 10px;
  max-width: 440px;
  margin: 18px auto 0;
}
.waitlist-form input {
  flex: 1;
  height: 50px;
  padding: 0 20px;
  border-radius: 999px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(196,181,253,0.3);
  color: #fff;
  font-family: var(--mono);
  font-size: 13px;
  letter-spacing: 0.04em;
  transition: border-color 0.2s;
}
.waitlist-form input:focus {
  outline: none;
  border-color: #c4b5fd;
  box-shadow: 0 0 20px rgba(196,181,253,0.3);
}

/* =========================================================
   MOVEMENT 7 & TOTEMS: SQUEEZING BRACKETS & WORD RISE
   ========================================================= */
.totem-stage {
  position: relative;
  text-align: center;
  padding: 80px 20px;
  cursor: none;
}

.bracket-counter {
  font-family: var(--mono);
  font-size: 14px;
  letter-spacing: 0.2em;
  color: var(--muted);
  transition: transform 0.2s cubic-bezier(0.2, 1.4, 0.4, 1);
  display: inline-block;
}
.bracket-counter.squeeze {
  transform: scaleX(0.7);
}

.totem-word-mask {
  overflow: hidden;
  height: clamp(3.5rem, 8vw, 7.5rem);
  margin: 16px 0;
}
.totem-word {
  font-family: var(--serif);
  font-size: clamp(3.5rem, 8vw, 7.5rem);
  line-height: 1;
  text-transform: uppercase;
  transform: translateY(110%);
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.totem-word.active {
  transform: none;
}

#customCursor {
  position: fixed;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--pastel);
  color: var(--ink);
  display: grid;
  place-items: center;
  pointer-events: none;
  z-index: 300;
  font-size: 18px;
  transform: translate(-50%, -50%);
  opacity: 0;
  transition: opacity 0.2s, transform 0.1s ease-out;
}
#customCursor.show { opacity: 1; }

/* Chapter 03 photo slide */
.row3 {
  position: relative;
  display: grid;
  grid-template-columns: 1.2fr 0.7fr 1fr;
  gap: 28px;
  align-items: center;
  padding: 28px 0;
  border-top: 1px solid rgba(13,8,24,0.14);
}
.th3 {
  aspect-ratio: 4/3;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  max-width: 240px;
  transition: transform 0.15s ease-out;
}
.th3 img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.row3:hover .th3 img { transform: scale(1.08); }

/* Base Components & Controls */
.wrap { padding: 0 clamp(20px, 5vw, 72px); }
.sec { padding: clamp(64px, 9vw, 120px) 0; }
.sec-h { display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; flex-wrap: wrap; margin-bottom: 38px; }
.sec-h h2 { font-size: clamp(2.1rem, 5.4vw, 4.6rem); max-width: 15ch; }
.sec-h p { max-width: 34ch; color: var(--muted); font-size: 15px; }

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 15px 28px;
  border-radius: 999px;
  background: var(--btn-bg);
  color: var(--btn-fg);
  font-weight: 600;
  font-size: 14.5px;
  letter-spacing: 0.01em;
  transition: transform 0.2s, opacity 0.2s, filter 0.2s;
  min-height: 50px;
}
.btn:hover { transform: translateY(-2px); filter: brightness(1.05); }
.btn:disabled { opacity: 0.38; cursor: not-allowed; transform: none; }
.btn.ghost { background: transparent; color: var(--text); border: 1px solid var(--line2); }
.btn.ink { background: var(--ink); color: var(--pastel); }
.btn.block { width: 100%; }
.btn.sm { padding: 10px 18px; min-height: 40px; font-size: 13px; }
.btn .spin { width: 16px; height: 16px; border-radius: 50%; border: 2px solid currentColor; border-right-color: transparent; animation: spin 0.7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }

.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(320px, 100%), 1fr)); gap: 18px; }
.card {
  position: relative;
  border-radius: 26px;
  background: var(--bg2);
  border: 1px solid var(--line);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.3s, box-shadow 0.3s;
}
.card:hover { transform: translateY(-5px); border-color: var(--line2); box-shadow: var(--shadow); }
.cv { position: relative; aspect-ratio: 4/3; overflow: hidden; background: #120a1f; }
.cv img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.card:hover .cv img { transform: scale(1.06); }
.cv svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.cv::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, transparent 40%, rgba(0,0,0,0.75) 100%); }
.cv .b1 { position: absolute; left: 14px; top: 14px; display: flex; gap: 6px; z-index: 2; flex-wrap: wrap; }
.cv .rate { position: absolute; left: 16px; bottom: 14px; z-index: 2; color: #fff; font-family: var(--mono); font-size: 13px; display: flex; align-items: center; gap: 7px; }
.cv .lock { position: absolute; right: 14px; top: 14px; z-index: 2; width: 34px; height: 34px; border-radius: 50%; display: grid; place-items: center; background: rgba(0,0,0,0.55); color: #fff; backdrop-filter: blur(8px); }
.star { width: 14px; height: 14px; fill: #f0b94a; }
.fav { position: absolute; right: 14px; bottom: 12px; z-index: 3; width: 38px; height: 38px; border-radius: 50%; background: rgba(0,0,0,0.55); color: #fff; font-size: 18px; display: grid; place-items: center; transition: all 0.2s; }
.fav:hover { transform: scale(1.12); }
.fav.on { color: #ff6b81; }
.badge { display: inline-flex; align-items: center; gap: 6px; padding: 5px 11px; border-radius: 999px; font-family: var(--mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; background: rgba(0,0,0,0.6); color: #fff; backdrop-filter: blur(8px); }
.tag { padding: 5px 11px; border-radius: 999px; background: var(--tint); color: var(--tint-fg); font-size: 12px; font-weight: 500; }
.cb { padding: 20px 20px 22px; display: flex; flex-direction: column; gap: 12px; flex: 1; }
.cb h3 { font-family: var(--serif); font-weight: 400; font-size: 1.65rem; letter-spacing: -0.02em; text-transform: uppercase; line-height: 1; }
.cb .loc { font-size: 13.5px; color: var(--muted); display: flex; justify-content: space-between; gap: 8px; }
.cb .tags { display: flex; gap: 6px; flex-wrap: wrap; }
.cb .go { margin-top: auto; display: flex; justify-content: space-between; align-items: center; gap: 10px; padding-top: 6px; }
.cb .price { font-family: var(--mono); font-size: 12px; letter-spacing: 0.06em; color: var(--muted); }
.cb .price b { color: var(--text); font-size: 15px; font-weight: 600; }

/* Filter Controls */
.ctrl { display: flex; flex-direction: column; gap: 16px; margin-bottom: 30px; }
.ctrl-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
.seg { display: inline-flex; padding: 4px; border-radius: 999px; border: 1px solid var(--line); background: var(--bg2); gap: 2px; }
.seg button { padding: 10px 18px; border-radius: 999px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); transition: all 0.2s; }
.seg button.on { background: var(--btn-bg); color: var(--btn-fg); }
.pills { display: flex; gap: 8px; flex-wrap: wrap; }
.pill { padding: 10px 17px; border-radius: 999px; border: 1px solid var(--line2); font-size: 13px; font-weight: 500; color: var(--text); transition: all 0.2s; white-space: nowrap; }
.pill:hover { background: var(--tint); }
.pill.on { background: var(--tint); color: var(--tint-fg); border-color: transparent; font-weight: 600; }
.search { position: relative; flex: 1; min-width: 220px; }
.search svg { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); width: 16px; height: 16px; color: var(--muted); }
.search input { width: 100%; height: 50px; padding: 0 20px 0 46px; border-radius: 999px; border: 1px solid var(--line2); background: var(--bg2); font-family: var(--mono); font-size: 13px; }
.select { height: 50px; padding: 0 42px 0 20px; border-radius: 999px; border: 1px solid var(--line2); background: var(--bg2); font-family: var(--mono); font-size: 12px; }

/* Modal & Sheet */
.ov { position: fixed; inset: 0; z-index: 100; display: grid; place-items: center; padding: 20px; background: rgba(0,0,0,0.68); backdrop-filter: blur(14px); animation: fade 0.25s ease; }
.ov.out { animation: fadeout 0.22s ease forwards; }
@keyframes fade { from { opacity: 0; } }
@keyframes fadeout { to { opacity: 0; } }
.sheet { position: relative; width: min(1020px, 100%); max-height: calc(100dvh - 40px); overflow: auto; background: var(--bg2); color: var(--text); border: 1px solid var(--line2); border-radius: 32px; box-shadow: var(--shadow); animation: pop 0.35s cubic-bezier(0.2, 0.8, 0.2, 1); outline: none; }
.sheet.sm { width: min(470px, 100%); }
.sheet.md { width: min(560px, 100%); }
@keyframes pop { from { opacity: 0; transform: translateY(24px) scale(0.97); } }
.x { position: absolute; right: 16px; top: 16px; z-index: 5; width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; background: rgba(0,0,0,0.6); color: #fff; backdrop-filter: blur(8px); font-size: 22px; }
.x.plain { background: var(--bg3); color: var(--text); }
.vgrid { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); }
.vleft { border-right: 1px solid var(--line); }
.vcover { position: relative; aspect-ratio: 16/11; overflow: hidden; background: #110b1d; }
.vcover img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.vcover svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.vcover .b1 { position: absolute; left: 18px; bottom: 16px; z-index: 2; display: flex; gap: 6px; }
.vinfo { padding: 26px 28px 32px; display: flex; flex-direction: column; gap: 14px; }
.vinfo h2 { font-family: var(--serif); font-weight: 400; font-size: clamp(1.9rem, 3.4vw, 2.8rem); text-transform: uppercase; line-height: 0.98; }
.vright { padding: 28px; display: flex; flex-direction: column; gap: 18px; }
.days { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; }
.day { flex: 0 0 auto; min-width: 74px; padding: 10px 12px; border-radius: 18px; border: 1px solid var(--line2); text-align: center; transition: all 0.2s; }
.day.on { background: var(--btn-bg); color: var(--btn-fg); }
.slots { display: grid; grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); gap: 8px; }
.slot { padding: 12px 8px 11px; border-radius: 16px; border: 1px solid var(--line2); display: flex; flex-direction: column; align-items: center; gap: 2px; transition: all 0.18s; }
.slot.on { background: var(--btn-bg); color: var(--btn-fg); }
.slot:disabled { opacity: 0.4; cursor: not-allowed; text-decoration: line-through; }
.bookbar { margin-top: auto; position: sticky; bottom: 0; background: var(--bg2); padding: 14px 0 2px; border-top: 1px solid var(--line); display: flex; align-items: center; justify-content: space-between; gap: 14px; }

/* AI Chat */
.chat { max-width: 860px; margin: 0 auto; padding: 118px 20px 220px; }
.chat-h { display: flex; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 26px; }
.chips { display: flex; gap: 8px; overflow-x: auto; padding: 2px 0 6px; margin-bottom: 28px; }
.chips button { flex: none; padding: 10px 16px; border-radius: 999px; border: 1px solid var(--line2); font-size: 13.5px; transition: all 0.2s; }
.chips button:hover { background: var(--tint); color: var(--tint-fg); }
.stream { display: flex; flex-direction: column; gap: 22px; }
.msg.u { align-self: flex-end; max-width: 82%; padding: 12px 20px; border-radius: 999px; background: var(--btn-bg); color: var(--btn-fg); font-size: 15px; }
.msg.a { display: flex; gap: 14px; align-items: flex-start; }
.msg.a .av { flex: none; width: 34px; height: 34px; border-radius: 50%; background: var(--pastel); color: var(--ink); display: grid; place-items: center; font-family: var(--serif); font-size: 18px; font-weight: 600; }
.msg.a .bd { flex: 1; min-width: 0; }
.msg.a .tx { font-size: 16px; line-height: 1.6; }
.hits { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; margin-top: 14px; }
.hit { display: flex; gap: 12px; align-items: center; padding: 10px; border-radius: 20px; border: 1px solid var(--line); background: var(--bg2); text-align: left; }
.hit .th { width: 52px; height: 52px; border-radius: 14px; overflow: hidden; position: relative; flex: none; }
.hit .th img { width: 100%; height: 100%; object-fit: cover; }
.tool { margin-top: 14px; padding: 14px 16px; border-radius: 20px; border: 1px solid var(--line2); background: var(--bg2); display: flex; gap: 14px; align-items: center; justify-content: space-between; }
.inbar { position: fixed; left: 50%; transform: translateX(-50%); bottom: calc(22px + env(safe-area-inset-bottom, 0px)); z-index: 58; width: min(860px, calc(100% - 24px)); }
.inbar form { display: flex; gap: 8px; padding: 7px; border-radius: 999px; background: var(--glass); backdrop-filter: blur(24px); border: 1px solid var(--line2); box-shadow: 0 14px 44px rgba(0,0,0,0.3); }
.inbar input { flex: 1; height: 48px; padding: 0 20px; background: transparent; border: 0; font-size: 15px; }

/* Bookings */
.pp { max-width: 1000px; margin: 0 auto; padding: 130px 20px 160px; }
.tlist { display: flex; flex-direction: column; gap: 10px; }
.trow { display: flex; gap: 16px; align-items: center; padding: 14px; border-radius: 22px; border: 1px solid var(--line); background: var(--bg2); text-align: left; }
.trow .th { width: 60px; height: 60px; border-radius: 16px; overflow: hidden; position: relative; flex: none; }
.trow .th img { width: 100%; height: 100%; object-fit: cover; }

#toast { position: fixed; left: 50%; bottom: calc(92px + env(safe-area-inset-bottom, 0px)); transform: translate(-50%, 14px); z-index: 200; padding: 12px 20px; border-radius: 999px; background: var(--btn-bg); color: var(--btn-fg); font-size: 14px; font-weight: 600; opacity: 0; pointer-events: none; transition: all 0.3s; }
#toast.show { opacity: 1; transform: translate(-50%, 0); }

@media (max-width: 767px) {
  .hdr { width: calc(100% - 20px); justify-content: space-between; }
  .nav, .hdr .sep, .floatcta { display: none; }
  .bnav { display: flex; }
  .hero { min-height: auto; padding: 110px 20px 60px; flex-direction: column; }
  .hero-spiral { position: relative; width: 340px; height: 340px; transform: none; right: auto; margin-top: 30px; }
  .wipe-inner { grid-template-columns: 1fr; }
  .row3 { grid-template-columns: 1fr; }
  .stats-overlay-grid { grid-template-columns: repeat(2, 1fr); }
  .vgrid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<div id="loader" role="status" aria-label="Loading hoppin.">
  <div class="book-stage">
    <div class="book" id="bookCover">
      <div class="book-page">
        <span class="book-monogram">h.</span>
        <span style="font-family:var(--mono);font-size:11px;letter-spacing:0.18em">EXPLORE REAL PLACES</span>
      </div>
      <div class="book-cover">
        <svg viewBox="0 0 100 112" width="70" aria-hidden="true">
          <path d="M50 3 L95 14 V54 C95 80 75 96 50 110 C25 96 5 80 5 54 V14 Z" fill="#c4b5fd" stroke="#fff" stroke-width="2.5"/>
          <text x="50" y="66" text-anchor="middle" font-family="Bodoni Moda,Didot,Georgia,serif" font-size="34" fill="#130a24">h.</text>
        </svg>
        <span class="book-monogram">hoppin.</span>
        <span class="loader-progress" id="loadPct">LOADING 0%</span>
      </div>
    </div>
  </div>
</div>

<header class="hdr" id="hdr">
  <a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues</span></a>
  <nav class="nav" id="nav" aria-label="Primary"></nav>
  <i class="sep"></i>
  <button class="icon-btn" id="themeBtn" data-act="theme" aria-label="Toggle theme"></button>
  <button class="acct" id="acct" data-act="account">Sign in</button>
</header>

<main id="app"></main>

<nav class="bnav" id="bnav" aria-label="Primary mobile"></nav>
<a class="floatcta" id="floatcta" href="#/chat"><span class="dot"></span>AI Concierge · Ask about 67 venues ↗</a>
<div id="toast" role="status" aria-live="polite"></div>
<div id="customCursor"></div>

<script>
(()=>{'use strict';
/* =========================================================
   UTILITIES & BACKEND API ADAPTER
   ========================================================= */
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const inr=n=>'₹'+Math.round(n).toLocaleString('en-IN');
function hashStr(s){let h=2166136261;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){let a=seed>>>0;return()=>{a=(a+0x6D2B79F5)|0;let t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}

const mem={};
const store={
  get(k,d){try{const v=localStorage.getItem(k);if(v!=null)return JSON.parse(v);}catch(e){} return k in mem?mem[k]:d;},
  set(k,v){mem[k]=v;try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
};
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
function toast(msg){const t=$('#toast');t.textContent=msg;t.classList.add('show');clearTimeout(toast._t);toast._t=setTimeout(()=>t.classList.remove('show'),2400);}

const API_URL = 'http://localhost:4000/api';
async function api(path, method='GET', body=null) {
  try {
    const res = await fetch(API_URL + path, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: body ? JSON.stringify(body) : undefined
    });
    if (res.ok) return await res.json();
    const err = await res.json().catch(()=>({}));
    return { _err: err.error || 'Server error' };
  } catch (e) {
    return null; // fallback to local state
  }
}

/* Icons */
const IC={
  sun:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  moon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4 8.5 8.5 0 1 0 20 14.5Z"/></svg>',
  lock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
  search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  star:'<svg class="star" viewBox="0 0 24 24"><path d="m12 2 3 6.6 7.2.7-5.4 4.8 1.6 7.1L12 17.4 5.6 21.2l1.6-7.1L1.8 9.3 9 8.6z"/></svg>',
  explore:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
  sports:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3.5 9c5 1 12 1 17 0M3.5 15c5-1 12-1 17 0M12 3c-3 4-3 14 0 18"/></svg>',
  dining:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3v7a2 2 0 0 0 2 2v9M10 3v7a2 2 0 0 1-2 2M6 3v0M18 21V3c-2.5 1.5-3.5 4.5-3.5 8H18"/></svg>',
  gaming:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><circle cx="8.5" cy="8.5" r="1" fill="currentColor"/><circle cx="15.5" cy="8.5" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/><circle cx="8.5" cy="15.5" r="1" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1" fill="currentColor"/></svg>',
  chat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.5 12a8.5 8.5 0 0 1-12.4 7.5L3.5 20.5l1.1-4.2A8.5 8.5 0 1 1 20.5 12Z"/></svg>',
  check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
  card:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="M2.5 10h19"/></svg>',
  info:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.01"/></svg>'
};

/* =========================================================
   67 VENUES DATA & CURATED HIGH-DEF IMAGERY
   ========================================================= */
const CITY={BLR:{name:'Bengaluru',short:'BLR'},MAA:{name:'Chennai',short:'MAA'}};
const CATS={
  sports:{label:'Sports & Turfs',price:[600,2000],
    slots:['06:00 AM','07:00 AM','09:00 AM','05:00 PM','06:00 PM','07:00 PM','08:00 PM','09:00 PM'],
    desc:n=>`Hourly slots to play with your crew. Pick a time, turn up in your kit and the pitch is yours.`},
  fitness:{label:'Fitness & Gyms',price:[400,1500],
    slots:['06:00 AM','07:00 AM','09:00 AM','12:00 PM','05:00 PM','07:00 PM'],
    desc:n=>`Book a session or a day pass and train on your schedule.`},
  pubs:{label:'Pubs & Brews',price:[500,1200],
    slots:['12:00 PM','04:00 PM','06:00 PM','07:30 PM','09:00 PM','10:30 PM'],
    desc:n=>`Reserve a table for your group. Arrive, order a round, stay a while.`},
  dining:{label:'Dining & Cafes',price:[500,1000],
    slots:['08:00 AM','12:30 PM','04:00 PM','07:00 PM','08:30 PM'],
    desc:n=>`Book a table ahead so you can walk straight in.`},
  gaming:{label:'Gaming & Arcades',price:[400,1200],
    slots:['11:00 AM','01:00 PM','03:00 PM','05:00 PM','07:00 PM','09:00 PM'],
    desc:n=>`Grab a two-hour block with friends. Screens are optional, dice are not.`},
  clubs:{label:'Clubs & Runs',price:[400,600],
    slots:['05:30 AM','06:00 AM','06:30 PM'],
    desc:n=>`Show up, meet the group, move together. A community event, not a class.`}
};
const CATCOL={
  sports:{sub:'Courts & floodlit turfs',emoji:'🏸',c:'#c4b5fd',c2:'#8b5cf6'},
  fitness:{sub:'Gyms, CrossFit & studios',emoji:'🏋️',c:'#ddd6fe',c2:'#a78bfa'},
  pubs:{sub:'Taprooms, brewpubs & bars',emoji:'🍻',c:'#ede9fe',c2:'#7c3aed'},
  dining:{sub:'Cafes, wine bars & dinner',emoji:'🍽️',c:'#f5f3ff',c2:'#c4b5fd'},
  gaming:{sub:'Board game cafes & VR arenas',emoji:'🎲',c:'#a78bfa',c2:'#6d28d9'},
  clubs:{sub:'Run clubs, yoga & cycling',emoji:'🏃',c:'#c4b5fd',c2:'#5b21b6'}
};

const AREA={
  'Indiranagar':[12.9784,77.6408],'Koramangala':[12.9352,77.6245],'Whitefield':[12.9698,77.7500],'Central Bengaluru':[12.9716,77.5946],'Bengaluru':[12.9716,77.5946],'Cubbon Park':[12.9763,77.5929],'Bidadi':[12.8330,77.4030],
  'Kilpauk':[13.0836,80.2420],'T. Nagar':[13.0418,80.2341],'Velachery':[12.9815,80.2180],'Vanagaram':[13.0500,80.1500],'Thiruvanmiyur':[12.9830,80.2594],'Puzhuthivakkam':[12.9700,80.1900],'Chromepet':[12.9516,80.1462],'Anna Nagar':[13.0850,80.2101],'OMR':[12.9000,80.2270],'Perungudi':[12.9650,80.2461],'Adyar':[13.0012,80.2565],'Alwarpet':[13.0339,80.2510],'Egmore':[13.0732,80.2609],'Porur':[13.0382,80.1565],'Mylapore':[13.0368,80.2676],'Besant Nagar':[13.0002,80.2707],'Nungambakkam':[13.0569,80.2425],'Periamet':[13.0827,80.2707],'Guindy':[13.0067,80.2206],'Chennai':[13.0827,80.2707],"Elliot's Beach":[13.0002,80.2707],'Velachery Mall':[12.9807,80.2185]
};

const VENUE_IMG = {
  'Arena Sports Complex': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=900&q=80',
  'The Shuttle Court': 'https://images.unsplash.com/photo-1613918431703-aa6321b25595?auto=format&fit=crop&w=900&q=80',
  'Koramangala Indoor Stadium': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=900&q=80',
  'Holy Ghost Church Grounds': 'https://images.unsplash.com/photo-1529900748604-07564a03e7a6?auto=format&fit=crop&w=900&q=80',
  'Aurum Luxury Fitness Club': 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80',
  'Cult Gym Indiranagar': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80',
  'CrossFit Brave': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=900&q=80',
  'Chisel Fitness': 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=900&q=80',
  'Cyborg Fitness': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=900&q=80',
  'Fitness First': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?auto=format&fit=crop&w=900&q=80',
  "Gold's Gym": 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=900&q=80',
  'Snap Fitness': 'https://images.unsplash.com/photo-1593079831268-3381b0db4a77?auto=format&fit=crop&w=900&q=80',
  'Toit Brewpub': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=900&q=80',
  "Bob's Bar": 'https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=900&q=80',
  '1131 Bar + Kitchen': 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=900&q=80',
  '21st Amendment Gastrobar': 'https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=900&q=80',
  'The Reservoire': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=900&q=80',
  'Plan B': 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=900&q=80',
  'Tipsy Bull Bar Exchange': 'https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=900&q=80',
  'Doff Pub': 'https://images.unsplash.com/photo-1560512823-829485b8bf24?auto=format&fit=crop&w=900&q=80',
  'Swiing Gourmet Table & Wine Bar': 'https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=900&q=80',
  'Vesparo': 'https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=900&q=80',
  'YUKI Pan-Asian': 'https://images.unsplash.com/photo-1579027989536-b7b1f875659b?auto=format&fit=crop&w=900&q=80',
  'Colosseum E-Sports': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
  'IONA VR Simulators': 'https://images.unsplash.com/photo-1593508512255-86ab42a8e620?auto=format&fit=crop&w=900&q=80',
  'Fun City': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80',
  'WonderLa Arcade': 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=900&q=80',
  'Cubbon Park Yoga Flow Meetup': 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=900&q=80',
  'The Amateur League (TAL)': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=900&q=80',
  'Tiki Taka Football Academy & Turf · Kilpauk': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Tiki Taka Football Academy & Turf · T. Nagar': 'https://images.unsplash.com/photo-1529900748604-07564a03e7a6?auto=format&fit=crop&w=900&q=80',
  'Tiki Taka Football Academy & Turf · Velachery': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=900&q=80',
  'FC Marina Turf & Football Academy · Vanagaram': 'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?auto=format&fit=crop&w=900&q=80',
  'FC Marina Turf & Football Academy · Thiruvanmiyur': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Spark Football Academy': 'https://images.unsplash.com/photo-1518604666860-9ed391f76460?auto=format&fit=crop&w=900&q=80',
  'Playpro7 Sport Turf': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?auto=format&fit=crop&w=900&q=80',
  'El Clasico Football Turf': 'https://images.unsplash.com/photo-1524015368236-bbf6f72545b6?auto=format&fit=crop&w=900&q=80',
  'Estilio Sports Academy': 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=900&q=80',
  'Dugout Indoor Arena · OMR': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=900&q=80',
  'Dugout Indoor Arena · Velachery Mall': 'https://images.unsplash.com/photo-1569517282132-25d22f4573e6?auto=format&fit=crop&w=900&q=80',
  'Plug N Play by Munchow': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80',
  'SDAT Tennis Stadium': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=900&q=80',
  'Nehru Indoor Stadium': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Cult Adyar': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80',
  'Cult Alwarpet': 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80',
  'Cult T. Nagar': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?auto=format&fit=crop&w=900&q=80',
  "Women's Gym · Adyar": 'https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=900&q=80',
  'The Madras Taproom': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=900&q=80',
  "Watson's": 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=900&q=80',
  'Shout Bar & Cafe': 'https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=900&q=80',
  'Slounge (Lemon Tree Shimona)': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=900&q=80',
  'The Alwarpet Taproom': 'https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=900&q=80',
  'Atte · Glocal Cafe': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=900&q=80',
  'The Old Potion House': 'https://images.unsplash.com/photo-1559925393-8be0ec4767c8?auto=format&fit=crop&w=900&q=80',
  'Zha Cafe': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=900&q=80',
  'Untangle House of Puzzles': 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=900&q=80',
  'Gameistry': 'https://images.unsplash.com/photo-1632501641765-e568d28b0015?auto=format&fit=crop&w=900&q=80',
  'The Board Room': 'https://images.unsplash.com/photo-1606167668584-78701c57f13d?auto=format&fit=crop&w=900&q=80',
  'The Board Game Lounge': 'https://images.unsplash.com/photo-1563941402622-4e7a488bcc57?auto=format&fit=crop&w=900&q=80',
  'GameOn Cafe': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80',
  'Gamesync': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
  'Chennai Runners (Bessie Flyers)': 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=900&q=80',
  'CORSO Run Club': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=900&q=80',
  'Dream Runners': 'https://images.unsplash.com/photo-1452626038306-9aae5e071dd3?auto=format&fit=crop&w=900&q=80',
  'VAMOS Run Club': 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=900&q=80',
  'Ciclo Cafe Community': 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=900&q=80',
  'WCCG Cycling Group': 'https://images.unsplash.com/photo-1541625602330-2277a4c46182?auto=format&fit=crop&w=900&q=80'
};

const RAW=[
 ['Arena Sports Complex','BLR','Indiranagar','sports',['Badminton','Football','Floodlit']],
 ['The Shuttle Court','BLR','Indiranagar','sports',['Badminton','Indoor','Racquets']],
 ['Koramangala Indoor Stadium','BLR','Koramangala','sports',['Indoor','Multi-sport','Badminton']],
 ['Holy Ghost Church Grounds','BLR','Central Bengaluru','sports',['Football','Open ground','Weekend games']],
 ['Aurum Luxury Fitness Club','BLR','Indiranagar','fitness',['Luxury','Pink salt sauna','Personal training'],'A luxury club with a pink salt sauna. Book a session, train hard, then let the sauna do the rest.'],
 ['Cult Gym Indiranagar','BLR','Indiranagar','fitness',['Group classes','Strength','Gym']],
 ['CrossFit Brave','BLR','Bengaluru','fitness',['CrossFit','HIIT','Coached']],
 ['Chisel Fitness','BLR','Bengaluru','fitness',['Gym','Strength','Training']],
 ['Cyborg Fitness','BLR','Bengaluru','fitness',['Gym','Cardio','Training']],
 ['Fitness First','BLR','Bengaluru','fitness',['Gym','Studio','Cardio']],
 ["Gold's Gym",'BLR','Bengaluru','fitness',['Gym','Weights','Classic']],
 ['Snap Fitness','BLR','Bengaluru','fitness',['24/7','Gym','Cardio']],
 ['Toit Brewpub','BLR','Indiranagar','pubs',['Craft beer','Brewpub','Groups'],'A Bengaluru brewpub known for house-brewed craft beer. Reserve a table for the whole crew.'],
 ["Bob's Bar",'BLR','Bengaluru','pubs',['Bar','Drinks','Groups']],
 ['1131 Bar + Kitchen','BLR','Bengaluru','pubs',['Bar','Kitchen','Cocktails']],
 ['21st Amendment Gastrobar','BLR','Bengaluru','pubs',['Gastrobar','Cocktails','Groups']],
 ['The Reservoire','BLR','Bengaluru','pubs',['Lounge','Cocktails','Nights']],
 ['Plan B','BLR','Bengaluru','pubs',['Bar','Drinks','Nights']],
 ['Tipsy Bull Bar Exchange','BLR','Bengaluru','pubs',['Bar exchange','Drinks','Groups']],
 ['Doff Pub','BLR','Bengaluru','pubs',['Pub','Drinks','Casual']],
 ['Swiing Gourmet Table & Wine Bar','BLR','Bengaluru','dining',['Wine bar','Gourmet','Date night']],
 ['Vesparo','BLR','Bengaluru','dining',['Dinner','Restaurant','Date night']],
 ['YUKI Pan-Asian','BLR','Bengaluru','dining',['Pan-Asian','Dinner','Groups']],
 ['Colosseum E-Sports','BLR','Bengaluru','gaming',['E-sports','PC gaming','Squads']],
 ['IONA VR Simulators','BLR','Whitefield','gaming',['VR','Simulators','Arcade']],
 ['Fun City','BLR','Bengaluru','gaming',['Arcade','Family','Games']],
 ['WonderLa Arcade','BLR','Bidadi','gaming',['Arcade','Rides','Family']],
 ['Cubbon Park Yoga Flow Meetup','BLR','Cubbon Park','clubs',['Yoga','Sundays','Outdoors'],'A Sunday morning flow in Cubbon Park at 6:30 AM. Bring a mat and show up.',{slots:['06:30 AM'],days:[0]}],
 ['The Amateur League (TAL)','BLR','Bengaluru','clubs',['Football','League','Community']],
 ['Tiki Taka Football Academy & Turf · Kilpauk','MAA','Kilpauk','sports',['Football','Turf','Floodlit']],
 ['Tiki Taka Football Academy & Turf · T. Nagar','MAA','T. Nagar','sports',['Football','Turf','Floodlit']],
 ['Tiki Taka Football Academy & Turf · Velachery','MAA','Velachery','sports',['Football','Turf','Floodlit']],
 ['FC Marina Turf & Football Academy · Vanagaram','MAA','Vanagaram','sports',['Football','Turf','Academy']],
 ['FC Marina Turf & Football Academy · Thiruvanmiyur','MAA','Thiruvanmiyur','sports',['Football','Turf','Academy']],
 ['Spark Football Academy','MAA','Puzhuthivakkam','sports',['Football','Academy','Turf']],
 ['Playpro7 Sport Turf','MAA','Chennai','sports',['Turf','5v5','Floodlit']],
 ['El Clasico Football Turf','MAA','Chromepet','sports',['Football','5v5','Floodlit']],
 ['Estilio Sports Academy','MAA','Anna Nagar','sports',['Multi-sport','Academy','Coaching']],
 ['Dugout Indoor Arena · OMR','MAA','OMR','sports',['Indoor','Multi-sport','Arena']],
 ['Dugout Indoor Arena · Velachery Mall','MAA','Velachery Mall','sports',['Indoor','Multi-sport','Arena']],
 ['Plug N Play by Munchow','MAA','Perungudi','sports',['Turf','Badminton','Snacks']],
 ['SDAT Tennis Stadium','MAA','Nungambakkam','sports',['Tennis','Hard courts','Outdoor'],null,{added:true}],
 ['Nehru Indoor Stadium','MAA','Periamet','sports',['Indoor','Multi-sport','Badminton'],null,{added:true}],
 ['Cult Adyar','MAA','Adyar','fitness',['Group classes','Strength','Gym']],
 ['Cult Alwarpet','MAA','Alwarpet','fitness',['Group classes','Strength','Gym']],
 ['Cult T. Nagar','MAA','T. Nagar','fitness',['Group classes','Strength','Gym']],
 ["Women's Gym · Adyar",'MAA','Adyar','fitness',['Women-only','Gym','Training']],
 ['The Madras Taproom','MAA','Egmore','pubs',['Taproom','Craft beer','Groups']],
 ["Watson's",'MAA','T. Nagar','pubs',['Bar','Drinks','Groups']],
 ['Shout Bar & Cafe','MAA','Porur','pubs',['Bar','Cafe','Groups']],
 ['Slounge (Lemon Tree Shimona)','MAA','Guindy','pubs',['Lounge','Hotel bar','Cocktails']],
 ['The Alwarpet Taproom','MAA','Alwarpet','pubs',['Taproom','Craft beer','Groups'],null,{added:true}],
 ['Atte · Glocal Cafe','MAA','Besant Nagar','dining',['Beachside','Cafe','Brunch'],'A beachside cafe in Besant Nagar. Morning tables come with the sea breeze.'],
 ['The Old Potion House','MAA','Adyar','dining',['Cafe','Quirky','Groups']],
 ['Zha Cafe','MAA','Chennai','dining',['Board games','Herbal coffee','Traditional'],'Traditional board games and herbal coffee. Slow afternoons, no screens.'],
 ['Untangle House of Puzzles','MAA','Chennai','dining',['Puzzles','Cafe','Groups']],
 ['Gameistry','MAA','Egmore','gaming',['1,300+ board games','Board games','Cafe'],'A shelf of 1,300+ board games. Pick a table, pick a slot, and let the staff teach you something new.'],
 ['The Board Room','MAA','Mylapore','gaming',['Board games','Strategy','Groups']],
 ['The Board Game Lounge','MAA','Adyar','gaming',['Board games','Lounge','Groups']],
 ['GameOn Cafe','MAA','T. Nagar','gaming',['Gaming','Cafe','Squads']],
 ['Gamesync','MAA','Velachery','gaming',['Gaming','Console','Squads']],
 ['Chennai Runners (Bessie Flyers)','MAA',"Elliot's Beach",'clubs',['Running','5:15 AM','Beachfront'],"Bessie Flyers meet at 5:15 AM on Elliot's Beach. Show up, run together, get breakfast after.",{slots:['05:15 AM']}],
 ['CORSO Run Club','MAA','Chennai','clubs',['Running','Community','Weekly']],
 ['Dream Runners','MAA','Chennai','clubs',['Running','Community','Weekly']],
 ['VAMOS Run Club','MAA','Chennai','clubs',['Running','Community','Weekly']],
 ['Ciclo Cafe Community','MAA','Chennai','clubs',['Cycling','Cafe','Community']],
 ['WCCG Cycling Group','MAA','Chennai','clubs',['Cycling','Group rides','Community']]
];

const roundTo=(n,s)=>Math.round(n/s)*s;
const VENUES=RAW.map((r,i)=>{
  const [name,city,area,cat,tags,desc,o]=r; const C=CATS[cat]; const R=rng(hashStr(name)); const opt=o||{};
  const ac=AREA[area]||AREA[CITY[city].name]; const [p0,p1]=C.price;
  const price=roundTo(p0+R()*(p1-p0),cat==='clubs'?50:50);
  const rating=Math.round((4.1+Math.pow(R(),0.8)*0.9)*10)/10;
  return {id:'v'+String(i+1).padStart(2,'0'),name,city,area,cat,tags,price,rating,
    reviews:Math.round(40+Math.pow(R(),1.6)*1760),
    lat:+(ac[0]+(R()-.5)*.012).toFixed(5),lng:+(ac[1]+(R()-.5)*.012).toFixed(5),
    slots:opt.slots||C.slots,days:opt.days||null,added:!!opt.added,
    desc:desc||(name+' in '+area+'. '+C.desc(name))};
});
const VBY=Object.fromEntries(VENUES.map(v=>[v.id,v]));
const COUNT={all:VENUES.length,BLR:VENUES.filter(v=>v.city==='BLR').length,MAA:VENUES.filter(v=>v.city==='MAA').length};

function coverImgURL(v){return VENUE_IMG[v.name]||'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';}
function coverMedia(v){
  const imgUrl=coverImgURL(v);
  return `<img src="${imgUrl}" alt="${esc(v.name)}" loading="lazy" onerror="this.style.display='none'">${coverSVG(v)}`;
}

/* Dates, Availability */
const toISO=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const fromISO=s=>{const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);};
const todayISO=()=>toISO(new Date());
const nowMin=()=>{const d=new Date();return d.getHours()*60+d.getMinutes();};
const toMin=t=>{const m=/(\d+):(\d+)\s*(AM|PM)/i.exec(t);let h=(+m[1])%12;if(/PM/i.test(m[3]))h+=12;return h*60+ +m[2];};
const WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];const MO=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
function dayLabel(iso){const t=todayISO();if(iso===t)return 'today';const d=new Date();d.setDate(d.getDate()+1);if(iso===toISO(d))return 'tomorrow';const x=fromISO(iso);return WD[x.getDay()]+' '+x.getDate()+' '+MO[x.getMonth()];}
const dayTitle=iso=>{const l=dayLabel(iso);return l==='today'?'Today':l==='tomorrow'?'Tomorrow':l;};
function validDays(v,n){const out=[];const d=new Date();for(let i=0;i<40&&out.length<n;i++){const x=new Date(d.getFullYear(),d.getMonth(),d.getDate()+i);if(!v.days||v.days.includes(x.getDay()))out.push(toISO(x));}return out;}
function slotPrice(v,s){return toMin(s)>=17*60?roundTo(v.price*1.15,50):v.price;}
function bookings(){return S.user?store.get('hoppin.bookings:'+S.user.email,[]):[];}
function isBooked(id,iso,slot){return bookings().some(b=>b.venueId===id&&b.iso===iso&&b.slot===slot);}
function avail(v,iso,slot){
  if(isBooked(v.id,iso,slot))return {state:'yours'};
  if(iso===todayISO()&&toMin(slot)<=nowMin())return {state:'past'};
  const r=hashStr(v.id+iso+slot)%100;
  if(r<16)return {state:'full'};
  if(r<38)return {state:'few',left:1+(r%3)};
  return {state:'open'};
}
const isOpenState=s=>s==='open'||s==='few';
function nextOpen(v){for(const iso of validDays(v,10)){for(const s of v.slots){if(isOpenState(avail(v,iso,s).state))return {iso,slot:s};}}return null;}
function openTonight(v){const iso=todayISO();return v.slots.filter(s=>isOpenState(avail(v,iso,s).state));}
function newRef(){const a='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';let s='HP-';for(let i=0;i<6;i++)s+=a[Math.floor(Math.random()*a.length)];return s;}

/* Shields & Totems */
const SHIELD='M50 3 L95 14 V54 C95 80 75 96 50 110 C25 96 5 80 5 54 V14 Z';
let uid=0;
function pat(kind,id,a,b){
  const o=`<pattern id="${id}" patternUnits="userSpaceOnUse"`;
  switch(kind){
    case 'check':return `${o} width="24" height="24"><rect width="24" height="24" fill="${a}"/><rect width="12" height="12" fill="${b}"/><rect x="12" y="12" width="12" height="12" fill="${b}"/></pattern>`;
    case 'stripe':return `${o} width="14" height="14" patternTransform="rotate(45)"><rect width="14" height="14" fill="${a}"/><rect width="7" height="14" fill="${b}"/></pattern>`;
    case 'diamond':return `${o} width="20" height="20"><rect width="20" height="20" fill="${a}"/><path d="M10 2 18 10 10 18 2 10Z" fill="${b}"/></pattern>`;
    case 'wave':return `${o} width="24" height="16"><rect width="24" height="16" fill="${a}"/><path d="M0 8Q6 0 12 8T24 8" fill="none" stroke="${b}" stroke-width="3.5"/></pattern>`;
    case 'dots':return `${o} width="16" height="16"><rect width="16" height="16" fill="${a}"/><circle cx="8" cy="8" r="3.6" fill="${b}"/></pattern>`;
    default:return `${o} width="20" height="14"><rect width="20" height="14" fill="${a}"/><path d="M0 14 10 4 20 14" fill="none" stroke="${b}" stroke-width="3.5"/></pattern>`;
  }
}
const KINDS=['check','stripe','diamond','wave','dots','chev'];
const initials=n=>{const w=n.replace(/[^A-Za-z0-9' &]/g,' ').split(/\s+/).filter(x=>x&&!/^(the|&|of|by)$/i.test(x));return ((w[0]||'H')[0]+(w[1]?w[1][0]:'')).toUpperCase();};
const coverCache={};
function coverSVG(v){
  if(coverCache[v.id])return coverCache[v.id];
  const P=CATCOL[v.cat]||CATCOL.sports;const R=rng(hashStr(v.id+v.name));const id='c'+(++uid);const id2='d'+(++uid);
  const k1=KINDS[Math.floor(R()*KINDS.length)];const k2=KINDS[Math.floor(R()*KINDS.length)];
  const ink='#0d0818';const rot=Math.round((R()-.5)*22);const sx=170+Math.round(R()*70);const sy=120+Math.round(R()*30);
  const bx=R()>.5?-40:260, by=Math.round(R()*90)+10;
  const svg=`<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>${pat(k1,id,P.c,P.c2)}${pat(k2,id2,P.c2,P.c)}</defs><rect width="400" height="300" fill="${P.c}"/><circle cx="${bx+100}" cy="${by+100}" r="140" fill="url(#${id})" opacity=".9"/><rect x="0" y="${R()>.5?0:210}" width="400" height="90" fill="url(#${id2})" opacity=".55"/><g transform="translate(${sx} ${sy}) rotate(${rot}) scale(1.55) translate(-50 -56)"><path d="${SHIELD}" fill="${P.c}" stroke="${ink}" stroke-width="2.4" stroke-linejoin="round"/><path d="${SHIELD}" fill="url(#${id2})" opacity=".85" transform="translate(50 56) scale(.86) translate(-50 -56)"/><circle cx="50" cy="52" r="26" fill="#f7f4ec" stroke="${ink}" stroke-width="2.4"/><text x="50" y="62" text-anchor="middle" font-family="Bodoni Moda,Didot,Georgia,serif" font-size="30" fill="${ink}">${initials(v.name)}</text></g></svg>`;
  return coverCache[v.id]=svg;
}

function totemSVG(kind, a, b, size=70) {
  const id='t'+(++uid);
  return `<svg viewBox="0 0 100 112" width="${size}" aria-hidden="true"><defs>${pat(kind, id, a, b)}</defs><path d="${SHIELD}" fill="url(#${id})" stroke="#0d0818" stroke-width="3" stroke-linejoin="round"/><circle cx="50" cy="52" r="22" fill="#fff" stroke="#0d0818" stroke-width="2.5"/><text x="50" y="60" text-anchor="middle" font-family="Bodoni Moda,Didot,Georgia,serif" font-size="24" fill="#0d0818">h.</text></svg>`;
}

/* =========================================================
   STATE & ROUTING
   ========================================================= */
const S={user:null,city:'all',cat:'all',q:'',sort:'rating',tonight:false,view:'discover',chatCity:'BLR',chat:[],lastHits:[],pending:null,maxp:0,minr:0,geo:null};

/* Auth */
function requireAuth(reason,then){if(S.user){then();return;}S.pending=then;showAuth('in',reason);}
function showAuth(tab,reason){
  const up=tab==='up';
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 32px 32px">
    <div class="kicker">${up?'Join hoppin.':'Welcome back'}</div>
    <h2 class="display" style="font-size:2.3rem;margin:8px 0 10px">${up?'Create your account':'Sign in to step inside'}</h2>
    <p style="color:var(--muted);font-size:14.5px;margin-bottom:20px">${esc(reason||'Sign in to see inside venues, book slots and talk to the AI Concierge.')}</p>
    <div style="display:flex;padding:4px;border-radius:999px;background:var(--bg3);margin-bottom:20px"><button class="${up?'':'on'}" data-act="auth-tab" data-tab="in" style="flex:1;padding:10px;border-radius:999px;font-weight:600;font-size:13.5px;${up?'color:var(--muted)':'background:var(--btn-bg);color:var(--btn-fg)'}">Sign in</button><button class="${up?'on':''}" data-act="auth-tab" data-tab="up" style="flex:1;padding:10px;border-radius:999px;font-weight:600;font-size:13.5px;${up?'background:var(--btn-bg);color:var(--btn-fg)':'color:var(--muted)'}">Create account</button></div>
    <form id="authForm" data-mode="${up?'up':'in'}" novalidate>
      ${up?`<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px"><label class="kicker">Name</label><input id="an" name="name" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)" placeholder="Your name"></div>`:''}
      <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px"><label class="kicker">Email</label><input id="ae" name="email" type="email" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)" placeholder="you@example.com"></div>
      <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px"><label class="kicker">Password</label><input id="ap" name="pw" type="password" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)" placeholder="At least 6 characters"></div>
      <div id="autherr" style="color:var(--bad);font-size:13.5px;margin:-2px 0 12px"></div>
      <button class="btn block" type="submit">${up?'Create account':'Sign in'}</button>
    </form>
    <button style="display:block;margin:14px auto 0;font-size:13.5px;color:var(--muted);text-decoration:underline" data-act="demo-login">Skip and explore as a demo guest</button>
  </div>`,'sm');
}
function finishAuth(user){
  S.user=user;store.set('hoppin.session',user.email);acctBtn();M.close();toast('Signed in as '+user.name);
  const p=S.pending;S.pending=null;
  render();if(p)setTimeout(p,260);
}
async function submitAuth(form){
  const mode=form.dataset.mode;const fd=new FormData(form);
  const email=String(fd.get('email')||'').trim().toLowerCase();const pw=String(fd.get('pw')||'');const name=String(fd.get('name')||'').trim();
  const err=m=>{$('#autherr').textContent=m;};
  if(!/^\S+@\S+\.\S+$/.test(email))return err('Enter a valid email address.');
  if(pw.length<6)return err('Password needs at least 6 characters.');
  
  const res=await api(mode==='up'?'/auth/signup':'/auth/login','POST',{name,email,password:pw});
  if(res&&!res._err&&res.user){
    return finishAuth(res.user);
  }
  if(res&&res._err)return err(res._err);

  const users=store.get('hoppin.users',{});
  if(mode==='up'){
    users[email]={name,pw:btoa(pw)};store.set('hoppin.users',users);finishAuth({email,name});
  }else{
    const u=users[email];
    if(!u||u.pw!==btoa(pw))return err('Email or password is wrong.');
    finishAuth({email,name:u.name});
  }
}
function signOut(){S.user=null;store.set('hoppin.session',null);acctBtn();S.chat=[];S.lastHits=[];go('/');toast('Signed out');}

/* Shell Header UI */
const NAV=[['discover','Discover','Explore','#/','explore'],['sports','Sports','Sports','#/cat/sports','sports'],['dining','Dining','Dining','#/cat/dining','dining'],['gaming','Gaming','Gaming','#/cat/gaming','gaming'],['chat','AI Concierge','AI Chat','#/chat','chat']];
$('#nav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${n[1]}</a>`).join('');
$('#bnav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${IC[n[4]]}<span>${n[2]}</span></a>`).join('');

function navActive(){
  let k='discover';
  if(S.view==='chat')k='chat';
  else if(S.view==='discover'&&['sports','dining','gaming'].includes(S.cat))k=S.cat;
  $$('[data-nav]').forEach(a=>a.classList.toggle('on',a.dataset.nav===k));
}
function themeIcon(){const t=document.documentElement.getAttribute('data-theme');$('#themeBtn').innerHTML=t==='light'?IC.moon:IC.sun;}
function toggleTheme(){const t=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',t);store.set('hoppin.theme',t);themeIcon();}
function acctBtn(){const a=$('#acct');if(S.user){a.classList.add('has');a.innerHTML=`<span class="av">${esc(S.user.name[0]||'H')}</span>Bookings`;}else{a.classList.remove('has');a.textContent='Sign in';}}
themeIcon();acctBtn();

/* Modal */
const M={ov:null,sheet:null,
  show(html,cls){
    if(!M.ov){
      M.ov=document.createElement('div');M.ov.className='ov';
      M.ov.innerHTML='<div class="sheet" role="dialog" aria-modal="true" tabindex="-1"></div>';
      M.ov.addEventListener('mousedown',e=>{if(e.target===M.ov)M.close();});
      document.body.appendChild(M.ov);document.documentElement.classList.add('lock');
      M.sheet=$('.sheet',M.ov);
    }
    M.sheet.className='sheet '+(cls||'');M.sheet.innerHTML=html;M.sheet.scrollTop=0;
    const f=$('input:not([type=hidden])',M.sheet);(f||M.sheet).focus({preventScroll:true});
  },
  close(){if(!M.ov)return;const ov=M.ov;M.ov=null;ov.classList.add('out');document.documentElement.classList.remove('lock');setTimeout(()=>ov.remove(),230);}
};
document.addEventListener('keydown',e=>{if(e.key==='Escape')M.close();});

/* Venue Detail & Booking */
let B=null;
function openVenue(id){const v=VBY[id];requireAuth(`Sign in to see inside ${v.name} and book a slot.`,()=>showVenue(id));}
function showVenue(id,pre){
  const v=VBY[id];const days=validDays(v,6);
  B={id,iso:(pre&&pre.iso)||days[0],slot:(pre&&pre.slot)||null};
  M.show(`<button class="x" data-act="close" aria-label="Close">×</button>
  <div class="vgrid">
    <div class="vleft">
      <div class="vcover">${coverMedia(v)}<div class="b1"><span class="badge">${CITY[v.city].name}</span><span class="badge">${CATS[v.cat].label}</span></div></div>
      <div class="vinfo">
        <h2>${esc(v.name)}</h2>
        <div style="display:flex;gap:14px;color:var(--muted);font-size:14px"><span style="color:var(--text);font-weight:600">${IC.star}${v.rating.toFixed(1)}</span><span>${v.reviews} reviews</span><span>${esc(v.area)}, ${CITY[v.city].name}</span></div>
        <div style="display:flex;gap:6px;flex-wrap:wrap">${v.tags.map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>
        <p style="color:var(--muted);font-size:15px">${esc(v.desc)}</p>
        <a class="btn ghost sm" style="align-self:flex-start" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=${v.lat},${v.lng}">Open in Maps ↗</a>
      </div>
    </div>
    <div class="vright" id="vright"></div>
  </div>`);
  renderBooking();
}
function renderBooking(){
  const v=VBY[B.id];const days=validDays(v,6);
  const slotBtns=v.slots.map(s=>{const a=avail(v,B.iso,s);const dis=['full','past','yours'].includes(a.state);
    const lab=a.state==='full'?'Full':a.state==='past'?'Passed':a.state==='yours'?'Booked':inr(slotPrice(v,s));
    return `<button class="slot ${a.state} ${B.slot===s?'on':''}" data-act="slot" data-slot="${s}" ${dis?'disabled':''} aria-pressed="${B.slot===s}"><span style="font-family:var(--mono);font-size:13px;font-weight:600">${s}</span><span style="font-size:12px;color:var(--muted)">${lab}</span>${a.state==='few'?`<span style="position:absolute;top:-8px;right:8px;font-size:9.5px;background:var(--warn);color:#fff;padding:2px 7px;border-radius:99px">${a.left} left</span>`:''}</button>`;}).join('');
  const price=B.slot?slotPrice(v,B.slot):null;
  $('#vright').innerHTML=`
    <div><h4 class="kicker">Pick a day</h4><div class="days" style="margin-top:10px">${days.map(d=>{const x=fromISO(d);return `<button class="day ${d===B.iso?'on':''}" data-act="day" data-iso="${d}"><span style="font-family:var(--mono);font-size:10px;text-transform:uppercase">${d===todayISO()?'Today':WD[x.getDay()]}</span><b style="display:block;font-family:var(--serif);font-size:22px">${x.getDate()}</b><span style="font-family:var(--mono);font-size:10px;color:var(--muted)">${MO[x.getMonth()]}</span></button>`;}).join('')}</div></div>
    <div><h4 class="kicker">Pick a time</h4><div class="slots" style="margin-top:10px">${slotBtns}</div></div>
    <div class="bookbar">
      <div style="font-size:13px;color:var(--muted)">${B.slot?`${dayLabel(B.iso)}, ${B.slot}<b style="display:block;color:var(--text);font-size:19px">${inr(price)}</b>`:'Choose a slot'}</div>
      <button class="btn" data-act="reserve" ${B.slot?'':'disabled'}>${B.resched?'Move booking':'Reserve slot'}</button>
    </div>`;
}

/* Checkout */
const FEE=30;
function showCheckout(order){
  const v=VBY[order.venueId];order.fee=FEE;order.disc=order.disc||0;order.total=order.price+FEE-order.disc;
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 32px 32px">
    <div class="kicker">Secure checkout</div>
    <h2 class="display" style="font-size:2.3rem;margin:8px 0 10px">Pay to confirm</h2>
    <div style="display:flex;gap:14px;padding:14px;border-radius:20px;border:1px solid var(--line);margin-bottom:16px;align-items:center"><div style="width:64px;height:64px;border-radius:14px;overflow:hidden;flex:none">${coverMedia(v)}</div><div><b style="font-family:var(--serif);font-size:1.15rem;display:block">${esc(v.name)}</b><span style="font-size:13px;color:var(--muted)">${dayLabel(order.iso)} · ${order.slot} · ${esc(v.area)}</span></div></div>
    <div style="font-size:14px;margin-bottom:18px">
      <div style="display:flex;justify-content:space-between;padding:6px 0;color:var(--muted)"><span>Slot</span><span>${inr(order.price)}</span></div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;color:var(--muted)"><span>Booking fee</span><span>${inr(order.fee)}</span></div>
      ${order.disc?`<div style="display:flex;justify-content:space-between;padding:6px 0;color:var(--muted)"><span>Promo discount</span><span>−${inr(order.disc)}</span></div>`:''}
      <div style="display:flex;justify-content:space-between;font-weight:700;font-size:16px;border-top:1px solid var(--line);margin-top:6px;padding-top:10px"><span>Total</span><span>${inr(order.total)}</span></div>
    </div>
    <div style="display:flex;gap:10px;padding:12px 14px;border-radius:16px;background:var(--tint);color:var(--tint-fg);font-size:12.5px;margin-bottom:16px">${IC.info}<span>Test mode. Card <b>4242 4242 4242 4242</b>, any future date, any CVC.</span></div>
    <form id="payForm" novalidate>
      <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px"><label class="kicker">Email for ticket</label><input id="pe" name="email" type="email" value="${esc(S.user?S.user.email:'')}" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)"></div>
      <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px"><label class="kicker">Card number</label><input id="pc" name="card" value="4242 4242 4242 4242" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)"></div>
      <div style="display:flex;gap:12px;margin-bottom:14px"><div style="flex:1"><label class="kicker">Expiry</label><input id="px" name="exp" value="12/28" style="width:100%;height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)"></div><div style="flex:1"><label class="kicker">CVC</label><input id="pv" name="cvc" value="123" style="width:100%;height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg)"></div></div>
      <button class="btn block" type="submit" id="payBtn">${IC.card}<span>Pay ${inr(order.total)}</span></button>
    </form>
  </div>`,'md');
  showCheckout.order=order;
}

function submitPay(form){
  const o=showCheckout.order;const btn=$('#payBtn');btn.disabled=true;btn.innerHTML='<span class="spin"></span><span>Processing…</span>';
  setTimeout(async()=>{
    const bkRes=await api('/bookings','POST',{
      venueId:o.venueId,iso:o.iso,slot:o.slot,partySize:1,
      userEmail:S.user.email,userName:S.user.name,card:'4242',
      disc:o.disc||0
    });
    const bk=bkRes?.booking||{ref:o.ref||newRef(),venueId:o.venueId,iso:o.iso,slot:o.slot,price:o.price,fee:o.fee,total:o.total,at:Date.now(),last4:'4242'};
    const list=store.get('hoppin.bookings:'+S.user.email,[]);list.unshift(bk);store.set('hoppin.bookings:'+S.user.email,list);
    showTicket(bk,true);
    if(S.view==='chat'){pushAssistant({text:`Payment received. <strong>${esc(VBY[bk.venueId].name)}</strong> is confirmed for ${esc(dayLabel(bk.iso))} at ${bk.slot}. Your ticket is in My bookings.`});}
  },1200);
}

function showTicket(b,fresh){
  const v=VBY[b.venueId];
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 28px 30px;text-align:center">
    <div class="kicker" style="color:var(--ok)">${fresh?'Payment received':'Your ticket'}</div>
    <h2 class="display" style="font-size:2.4rem;margin:8px 0 22px">${fresh?'You’re in.':'Ticket'}</h2>
    <div style="max-width:340px;margin:0 auto 24px;border-radius:22px;background:var(--pastel);color:var(--ink);text-align:left;padding:22px;box-shadow:0 20px 40px rgba(0,0,0,0.3)">
      <div class="kicker">${esc(CITY[v.city].name)} · ${esc(CATS[v.cat].label)}</div>
      <h3 style="font-family:var(--serif);font-size:1.7rem;text-transform:uppercase;margin:6px 0 12px">${esc(v.name)}</h3>
      <div style="display:flex;justify-content:space-between;font-size:13.5px"><span>${dayLabel(b.iso)}</span><b>${b.slot}</b></div>
      <div style="display:flex;justify-content:space-between;font-size:13.5px;margin-top:4px"><span>${esc(v.area)}</span><b>${inr(b.total)} paid</b></div>
      <div style="border-top:2px dashed rgba(19,32,15,0.35);margin:16px 0;padding-top:12px;display:flex;justify-content:space-between;align-items:center">
        <div><small class="kicker">Reference</small><div style="font-family:var(--mono);font-size:18px;font-weight:600">${b.ref}</div></div>
        <svg viewBox="-.5 -.5 22 22" width="60" height="60"><rect width="22" height="22" fill="#13200f"/></svg>
      </div>
    </div>
    <button class="btn" data-act="to-bookings">View in My tickets</button>
  </div>`,'sm');
}

/* =========================================================
   MOVEMENT 1: 18 SPIRAL CARDS SETUP
   ========================================================= */
function buildHeroSpiralCards() {
  const cards = VENUES.slice(0, 18);
  const total = cards.length;
  const radius = 240;
  return cards.map((v, i) => {
    const angle = (i / total) * Math.PI * 2;
    const tx = Math.round(Math.sin(angle) * radius);
    const tz = Math.round(Math.cos(angle) * radius);
    const ty = Math.round((i - total / 2) * 16);
    const ry = (angle * 180 / Math.PI) + 90;
    const rx = (i % 2 === 0 ? 8 : -8);
    return `<div class="spiral-card" style="--tx:${tx}px;--ty:${ty}px;--tz:${tz}px;--ry:${ry}deg;--rx:${rx}deg" data-act="venue" data-id="${v.id}">
      <img src="${coverImgURL(v)}" alt="${esc(v.name)}" loading="lazy">
      <div class="badge-overlay">${esc(v.name.split(' · ')[0])}</div>
    </div>`;
  }).join('');
}

/* =========================================================
   MOVEMENT 5: 2D CANVAS PHYSICS BALLS (Lilac, Violet, Mint, Gold)
   ========================================================= */
class PhysicsBalls {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.balls = [];
    this.columns = 4;
    this.colWidth = 0;
    this.animId = null;
    this.counts = [0, 0, 0, 0];
    this.targetCounts = [18, 13, 12, 9];
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.spawnInitial();
    this.loop();
  }

  resize() {
    this.canvas.width = this.canvas.parentElement.clientWidth;
    this.canvas.height = this.canvas.parentElement.clientHeight;
    this.colWidth = this.canvas.width / this.columns;
  }

  spawnBall(colIdx = null) {
    const col = colIdx !== null ? colIdx : Math.floor(Math.random() * 4);
    const colX = col * this.colWidth;
    const r = Math.random() * 6 + 10;
    const colors = ['#c4b5fd', '#a78bfa', '#7c3aed', '#f0b94a', '#34d399', '#f4f1ea'];
    this.balls.push({
      x: colX + Math.random() * (this.colWidth - r * 2) + r,
      y: -20,
      vx: (Math.random() - 0.5) * 2,
      vy: Math.random() * 2 + 1,
      r,
      col,
      color: colors[Math.floor(Math.random() * colors.length)],
      bounces: 0
    });
  }

  spawnInitial() {
    for (let c = 0; c < 4; c++) {
      for (let i = 0; i < 6; i++) {
        setTimeout(() => this.spawnBall(c), i * 180 + c * 80);
      }
    }
  }

  loop() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const gravity = 0.45;
    const floor = canvas.height - 8;

    for (let i = 0; i < this.balls.length; i++) {
      const b = this.balls[i];
      b.vy += gravity;
      b.x += b.vx;
      b.y += b.vy;

      // Col boundaries
      const minX = b.col * this.colWidth + b.r;
      const maxX = (b.col + 1) * this.colWidth - b.r;
      if (b.x < minX) { b.x = minX; b.vx *= -0.6; }
      if (b.x > maxX) { b.x = maxX; b.vx *= -0.6; }

      // Floor collision
      if (b.y > floor - b.r) {
        b.y = floor - b.r;
        b.vy *= -0.55;
        b.vx *= 0.85;
        b.bounces++;
      }

      // Render ball
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fillStyle = b.color;
      ctx.shadowColor = 'rgba(124, 58, 237, 0.4)';
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    this.animId = requestAnimationFrame(() => this.loop());
  }
}

/* =========================================================
   MOVEMENT 4: GUILDS 3D WHEEL
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
}

/* =========================================================
   DISCOVER VIEW HTML
   ========================================================= */
function discoverHTML() {
  const letters = "STEP OUT. SHOW UP.".split("").map((ch, i) => `<span class="char" style="transition-delay:${i * 28}ms">${ch === " " ? "&nbsp;" : ch}</span>`).join("");
  return `
  <section class="hero" id="heroSec">
    <div class="hero-content" id="heroContent">
      <div class="kicker" style="margin-bottom:20px;color:var(--pastel)">hoppin. · Bengaluru + Chennai</div>
      <h1 class="display mega" id="heroMega">${letters}</h1>
      <p class="sub">${COUNT.all} curated courts, turfs, taprooms, game cafes and run clubs. Pick a slot, show up, and let the plan survive the group chat.</p>
      <div style="display:flex;gap:12px;margin-top:34px;flex-wrap:wrap">
        <a class="btn" href="#explore">Explore 67 venues</a>
        <a class="btn ghost" href="#/chat">AI Concierge ↗</a>
      </div>
    </div>
    <div class="hero-spiral" id="heroSpiral" aria-hidden="true">
      <div class="spiral-ring" id="spiralRing">${buildHeroSpiralCards()}</div>
    </div>
  </section>

  <!-- CHAPTER 01: Staggered Lines Rise -->
  <section class="sec wrap" style="background:#0a0612;color:#fff;padding:120px clamp(20px,5vw,72px)" id="chap1">
    <div class="kicker" style="color:#c4b5fd;margin-bottom:28px">Chapter 01 · About the problem</div>
    <h2 class="display" style="font-size:clamp(2.4rem,6vw,5.4rem);line-height:1.05">
      <div class="rv" style="margin-left:0">Plans live in the group chat.</div>
      <div class="rv" style="margin-left:clamp(0px, 12vw, 160px);margin-top:14px;color:#c4b5fd">Nobody books them.</div>
      <div class="rv" style="margin-left:clamp(0px, 24vw, 320px);margin-top:14px;color:#ddd6fe">Next weekend, always.</div>
    </h2>
    <p class="rv" style="max-width:44ch;margin:48px 0 0 clamp(0px, 24vw, 320px);color:#b9b3cc;font-size:16px">Someone says football. Someone asks which turf. Three days later the slots are gone. hoppin. puts the venue, the live slot and the price in one place.</p>
  </section>

  <!-- MOVEMENT 3: CHAPTER 02 LILAC WIPE & LIVE COUNTDOWN CLOCK -->
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

  <!-- MOVEMENT 7: TOTEM INTERACTIVE WORDS & BRACKETS -->
  <section class="totem-stage wrap" id="totemSec">
    <div class="bracket-counter" id="bracketCounter">[ 01 / 06 ]</div>
    <div class="totem-word-mask">
      <div class="totem-word active" id="totemWord">SPORTS & TURFS</div>
    </div>
    <p style="color:var(--muted);font-size:14.5px">Move mouse left or right to switch scenes</p>
  </section>

  <!-- MOVEMENT 4: GUILDS SPINNING WHEEL -->
  <section class="guilds-sec wrap" id="guildsSec">
    <div style="text-align:center"><div class="kicker">Chapter 04 · The Guilds</div><h2 class="display" style="font-size:clamp(2.2rem,5vw,4.2rem);margin-top:10px">Choose your arena</h2><p style="color:var(--muted);margin-top:8px">Spin the wheel or scroll fast to accelerate.</p></div>
    <div class="wheel-wrap"><div class="shield-wheel" id="shieldWheel">${buildGuildsWheel()}</div></div>
  </section>

  <!-- MOVEMENT 5: STATS INTERACTIVE 2D PHYSICS BALLS -->
  <section class="stats-physics-sec wrap" id="statsSec">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:18px">
      <div><div class="kicker">Live Inventory</div><h2 class="display" style="font-size:clamp(2rem,4.4vw,3.6rem)">Venues by the numbers</h2></div>
      <p style="color:var(--muted);font-size:14px">Click or hold anywhere inside the tank to drop more balls.</p>
    </div>
    <div class="physics-stage" id="physicsStage">
      <canvas id="ballsCanvas"></canvas>
      <div class="stats-overlay-grid">
        <div class="stat-bucket"><b id="statSports">18</b><span>Sports & Turfs</span></div>
        <div class="stat-bucket"><b id="statPubs">13</b><span>Pubs & Brews</span></div>
        <div class="stat-bucket"><b id="statFitness">12</b><span>Fitness & Gyms</span></div>
        <div class="stat-bucket"><b id="statGaming">9</b><span>Gaming & Arcades</span></div>
      </div>
    </div>
  </section>

  <!-- VENUE DIRECTORY -->
  <section class="sec wrap" id="explore">
    <div class="sec-h"><h2 class="display">All 67 Venues</h2><p>Filter by city, category or price. Connected live to the Hoppin backend.</p></div>
    <div class="ctrl">
      <div class="ctrl-row"><div class="seg" id="cityseg"><button class="on" data-city="all" data-act="city">All (67)</button><button data-city="BLR" data-act="city">Bengaluru (29)</button><button data-city="MAA" data-act="city">Chennai (38)</button></div></div>
      <div class="ctrl-row">
        <label class="search"><span class="sr">Search</span>${IC.search}<input id="q" type="search" placeholder="Search venues, sports, areas…" value="${esc(S.q)}"></label>
        <button class="pill" data-act="tonight-toggle">Open today</button>
      </div>
      <div class="pills" id="catpills">
        <button class="pill on" data-act="cat" data-cat="all">All</button>
        ${Object.entries(CATS).map(([k, c]) => `<button class="pill" data-act="cat" data-cat="${k}">${c.label}</button>`).join('')}
      </div>
    </div>
    <div id="count" style="margin-bottom:20px;font-family:var(--mono);font-size:12px;color:var(--muted)"></div>
    <div class="grid" id="grid"></div>
  </section>

  <!-- MOVEMENT 6: FOOTER WITH LIGHT RAYS & TALKING EMAIL -->
  <footer class="ft" id="footerSec">
    <div class="rays-card" id="raysCard">
      <div class="light-rays" id="lightRays"></div>
      <span class="talking-badge" id="talkingBadge">Enter your email for secret slot drops</span>
      <h3 class="display" style="font-size:clamp(1.8rem,4vw,3.2rem);margin-bottom:12px">Join the inner circle</h3>
      <p style="color:#b9b3cc;font-size:15px;max-width:44ch;margin:0 auto">Get first dibs on weekend floodlit turfs and taproom reservations before they drop publicly.</p>
      <form class="waitlist-form" id="waitlistForm">
        <input id="waitEmail" type="email" placeholder="you@domain.com" required autocomplete="off">
        <button class="btn sm ink" type="submit">Join ↗</button>
      </form>
    </div>
    <div style="font-family:var(--serif);font-size:clamp(3.8rem,14vw,11rem);line-height:0.9">hoppin.</div>
    <div style="display:flex;justify-content:space-between;margin-top:30px;color:var(--muted);font-size:13.5px;flex-wrap:wrap;gap:14px">
      <span>Discover real places across Bengaluru and Chennai.</span>
      <span>Lilac Grail Edition · Fullstack API on port 4000</span>
    </div>
  </footer>
  `;
}

function cardHTML(v){
  const sv=store.get('hoppin.saved',[]).includes(v.id);
  return `<article class="card" tabindex="0" data-act="venue" data-id="${v.id}">
    <div class="cv">${coverMedia(v)}
      <div class="b1"><span class="badge">${CITY[v.city].short}</span><span class="badge">${CATS[v.cat].label.split(' & ')[0]}</span></div>
      <button class="fav ${sv?'on':''}" data-act="save" data-id="${v.id}" aria-label="Save">♥</button>
      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><small>(${v.reviews})</small></div>
    </div>
    <div class="cb">
      <h3>${esc(v.name)}</h3>
      <div class="loc"><span>${esc(v.area)}</span><span>${CITY[v.city].name}</span></div>
      <div class="tags">${v.tags.slice(0,3).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>
      <div class="go"><span class="price">from <b>${inr(v.price)}</b></span><button class="btn sm" data-act="venue" data-id="${v.id}">Reserve ↗</button></div>
    </div></article>`;
}

function renderGrid(){
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
}

/* Chat & Concierge */
function chatHTML(){
  const chips=['🏸 Badminton in Indiranagar','⚽ Floodlit football turfs','🎲 Board games in Chennai','🍻 Craft beer tonight'];
  return `<div class="chat">
    <div class="chat-h"><div><div class="kicker">AI Concierge</div><h1 class="display" style="font-size:2.8rem;margin-top:8px">Ask, then go.</h1></div></div>
    <div class="chips">${chips.map(c=>`<button class="pill" data-act="chip" data-t="${c}">${c}</button>`).join('')}</div>
    <div class="stream" id="stream"></div>
  </div>
  <div class="inbar"><form id="chatForm"><input id="chatIn" placeholder="Ask for a turf, taproom, or budget…" autocomplete="off"><button class="btn sm" type="submit">Send</button></form></div>`;
}

function msgHTML(m){
  if(m.role==='u')return `<div class="msg u">${esc(m.text)}</div>`;
  const hits=(m.hits||[]).map(id=>VBY[id]).filter(Boolean).map(v=>`<button class="hit" data-act="venue" data-id="${v.id}"><div class="th">${coverMedia(v)}</div><div><b style="display:block;font-family:var(--serif)">${esc(v.name)}</b><span style="font-size:12px;color:var(--muted)">${esc(v.area)} · ★ ${v.rating.toFixed(1)}</span></div></button>`).join('');
  const tool=m.tool?`<div class="tool"><div><b style="font-family:var(--mono);font-size:12px">HELD SLOT</b><div style="font-size:13px">${m.tool.result.ref} · ${m.tool.args.slot}</div></div><button class="btn sm" data-act="pay-hold" data-order='${JSON.stringify(m.tool.order)}'>Pay to confirm</button></div>`:'';
  return `<div class="msg a"><div class="av">h</div><div class="bd"><div class="tx">${m.text}</div>${hits?`<div class="hits">${hits}</div>`:''}${tool}</div></div>`;
}

async function sendChat(text){
  text=text.trim();if(!text)return;
  S.chat.push({role:'u',text});$('#stream').insertAdjacentHTML('beforeend',msgHTML({role:'u',text}));
  window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});
  
  let res=null;
  const r=await api('/chat','POST',{userId:S.user?.email||'usr_guest',city:S.chatCity,message:text});
  if(r&&r.text){
    res={text:r.text,hits:r.hits||[],tool:r.tool};
  }else{
    const hits=VENUES.filter(v=>v.tags.some(t=>text.toLowerCase().includes(t.toLowerCase()))).slice(0,3);
    res={text:`Here are matches from our 67 venues:`,hits:hits.map(v=>v.id)};
  }
  pushAssistant(res);
}
function pushAssistant(m){m.role='a';S.chat.push(m);$('#stream').insertAdjacentHTML('beforeend',msgHTML(m));window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});}

/* Bookings View */
function bookingsHTML(){
  const list=bookings();
  return `<div class="pp"><div class="kicker">My bookings</div><h1 class="display">Your tickets</h1>
    <div class="tlist">${list.length?list.map(b=>{const v=VBY[b.venueId];return `<div class="trow"><div class="th">${coverMedia(v)}</div><div><b style="font-family:var(--serif);font-size:1.2rem">${esc(v.name)}</b><span style="font-size:13px;color:var(--muted)">${b.slot} · ${b.ref}</span></div><div style="margin-left:auto;font-family:var(--mono);font-weight:600">${inr(b.total)}</div></div>`;}).join(''):'<p>No tickets yet.</p>'}</div>
  </div>`;
}

/* =========================================================
   ROUTER & ANIMATIONS
   ========================================================= */
let ROUTE=null;
function curPath(){return location.hash.replace(/^#/,'')||'/';}
function go(p){location.hash=p;}
function render(){
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
  }else if(view==='chat'){
    app.innerHTML=chatHTML();
    if(!S.chat.length)S.chat.push({role:'a',text:`Hi! I'm the hoppin. AI Concierge. Ask about courts, gyms, taprooms, or game cafes across Bengaluru and Chennai.`});
    $('#stream').innerHTML=S.chat.map(msgHTML).join('');
  }else{
    app.innerHTML=bookingsHTML();
  }
  navActive();
}

/* Animation 1: Hero Spiral Tilt & Parallax */
function initHeroAnimations(){
  const hero=$('#heroSec');
  const spiralRing=$('#spiralRing');
  const heroMega=$('#heroMega');
  if(heroMega)setTimeout(()=>heroMega.classList.add('in'), 150);

  if(!hero||!spiralRing||reduceMotion)return;
  hero.addEventListener('mousemove',e=>{
    const rect=hero.getBoundingClientRect();
    const x=(e.clientX-rect.left)/rect.width-0.5;
    const y=(e.clientY-rect.top)/rect.height-0.5;
    spiralRing.style.transform=`rotateY(${x*40}deg) rotateX(${12-y*30}deg)`;
  });

  window.addEventListener('scroll',()=>{
    const y=window.scrollY;
    if(y<window.innerHeight){
      const progress=y/window.innerHeight;
      const content=$('#heroContent');
      if(content){
        content.style.transform=`translateY(${-progress*60}px) scale(${1-progress*0.12})`;
        content.style.opacity=Math.max(0, 1-progress*1.6);
      }
    }
  },{passive:true});
}

/* Animation 3: Lilac Wipe & Countdown Clock */
function initLilacWipe(){
  const wipe=$('#lilacWipe');
  const sec=$('#wipeSection');
  const clk=$('#bigCountdown');

  // Countdown from 47:59:59
  let totalSec = 47*3600 + 59*60 + 59;
  setInterval(()=>{
    totalSec=Math.max(0, totalSec-1);
    const h=Math.floor(totalSec/3600);
    const m=Math.floor((totalSec%3600)/60);
    const s=totalSec%60;
    if(clk)clk.textContent=[h,m,s].map(n=>String(n).padStart(2,'0')).join(':');
  }, 1000);

  if(!wipe||!sec)return;
  window.addEventListener('scroll',()=>{
    const rect=sec.getBoundingClientRect();
    const vh=window.innerHeight;
    if(rect.top<vh&&rect.bottom>0){
      const progress=Math.min(1, Math.max(0, (vh-rect.top)/(vh+rect.height*0.5)));
      wipe.style.setProperty('--wipe-radius', (progress*95)+'%');
    }
  },{passive:true});
}

/* Animation 5: Physics Balls */
let physicsInst=null;
function initPhysics(){
  const canvas=$('#ballsCanvas');
  const stage=$('#physicsStage');
  if(!canvas||!stage)return;
  physicsInst=new PhysicsBalls(canvas);
  stage.addEventListener('mousedown',e=>{
    for(let i=0;i<5;i++)setTimeout(()=>physicsInst.spawnBall(), i*60);
  });
}

/* Animation 4: Guilds Wheel Spinning & Acceleration */
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

/* Animation 7: Totems Word Rise & Squeezing Brackets */
function initTotems(){
  const sec=$('#totemSec');
  const word=$('#totemWord');
  const counter=$('#bracketCounter');
  const cursor=$('#customCursor');
  if(!sec||!word)return;

  const words=['SPORTS & TURFS','FITNESS & GYMS','PUBS & BREWS','DINING & CAFES','GAMING & ARCADES','CLUBS & RUNS'];
  let idx=0;

  function switchWord(nextIdx){
    counter.classList.add('squeeze');
    word.classList.remove('active');
    setTimeout(()=>{
      idx=(nextIdx+words.length)%words.length;
      counter.textContent=`[ 0${idx+1} / 06 ]`;
      word.textContent=words[idx];
      word.classList.add('active');
      counter.classList.remove('squeeze');
    }, 200);
  }

  sec.addEventListener('mousemove',e=>{
    const rect=sec.getBoundingClientRect();
    const isLeft=e.clientX<rect.left+rect.width/2;
    cursor.textContent=isLeft?'←':'→';
    cursor.style.left=e.clientX+'px';
    cursor.style.top=e.clientY+'px';
    cursor.classList.add('show');
  });

  sec.addEventListener('mouseleave',()=>{cursor.classList.remove('show');});
  sec.addEventListener('click',e=>{
    const rect=sec.getBoundingClientRect();
    const isLeft=e.clientX<rect.left+rect.width/2;
    switchWord(idx+(isLeft?-1:1));
  });

  // Cycle Chapter 03 headline shield
  let shieldIdx=0;
  const cycleEl=$('#cycleShield');
  const kinds=['check','stripe','diamond','wave','dots','chev'];
  setInterval(()=>{
    shieldIdx=(shieldIdx+1)%kinds.length;
    if(cycleEl)cycleEl.innerHTML=totemSVG(kinds[shieldIdx],'#c4b5fd','#7c3aed',46);
  }, 1400);

  // Chapter 03 row photo slide
  $$('[data-spring-row]').forEach(row=>{
    const th=$('.th3',row);
    row.addEventListener('mousemove',e=>{
      const rect=row.getBoundingClientRect();
      const offset=(e.clientX-rect.left)/rect.width-0.5;
      if(th)th.style.transform=`translateX(${offset*45}px)`;
    });
    row.addEventListener('mouseleave',()=>{if(th)th.style.transform='none';});
  });
}

/* Animation 6: Light Rays & Talking Email Waitlist */
function initLightRays(){
  const card=$('#raysCard');
  const rays=$('#lightRays');
  const emailIn=$('#waitEmail');
  const badge=$('#talkingBadge');
  const form=$('#waitlistForm');

  if(card&&rays){
    card.addEventListener('mousemove',e=>{
      const rect=card.getBoundingClientRect();
      rays.style.setProperty('--ray-x', (e.clientX-rect.left)+'px');
      rays.style.setProperty('--ray-y', (e.clientY-rect.top)+'px');
    });
  }

  if(emailIn&&badge){
    emailIn.addEventListener('input',()=>{
      const v=emailIn.value.trim();
      if(!v)badge.textContent='Enter your email for secret slot drops';
      else if(!v.includes('@'))badge.textContent='That’s not an email yet 👀';
      else if(!v.includes('.'))badge.textContent='Missing the domain dot ✍️';
      else badge.textContent='Ooh, nice domain! Hit Enter to join ✨';
    });

    if(form){
      form.addEventListener('submit',e=>{
        e.preventDefault();
        badge.textContent='You’re on the list! Welcome to hoppin 🎟️';
        emailIn.value='';
        toast('Joined the waitlist!');
      });
    }
  }
}

/* Section Sensor for Header Pill */
function initSectionSensor(){
  const hdr=$('#hdr');
  const wipe=$('#wipeSection');
  const explore=$('#explore');
  if(!hdr)return;

  window.addEventListener('scroll',()=>{
    const y=window.scrollY;
    if(wipe){
      const wr=wipe.getBoundingClientRect();
      if(wr.top<70&&wr.bottom>70){
        hdr.className='hdr on-lilac';
        return;
      }
    }
    if(explore){
      const er=explore.getBoundingClientRect();
      if(er.top<70&&er.bottom>70){
        hdr.className='hdr on-light';
        return;
      }
    }
    hdr.className='hdr';
  },{passive:true});
}

/* Movement 2: Opening Book Loader */
function runLoader(){
  const book=$('#bookCover');
  const loader=$('#loader');
  const pct=$('#loadPct');
  if(!loader||!pct)return;

  let n=0;
  const iv=setInterval(()=>{
    n=Math.min(100, n+4);
    pct.textContent='LOADING '+n+'%';
    if(n>=100){
      clearInterval(iv);
      setTimeout(()=>{
        if(book)book.classList.add('open');
        setTimeout(()=>{
          loader.classList.add('off');
          setTimeout(()=>loader.remove(),600);
        }, 450);
      }, 350);
    }
  }, 35);
}

/* Event Delegation */
document.addEventListener('click',e=>{
  const lk=e.target.closest('a[href^="#/"]');if(lk){e.preventDefault();go(lk.getAttribute('href').slice(1));return;}
  const sc=e.target.closest('[data-scroll]');if(sc){e.preventDefault();const t=document.getElementById(sc.dataset.scroll);t&&t.scrollIntoView({behavior:'smooth'});return;}
  const a=e.target.closest('[data-act]');if(!a)return;
  const act=a.dataset.act;

  switch(act){
    case 'theme':toggleTheme();break;
    case 'account':if(S.user)go('/bookings');else showAuth('in');break;
    case 'close':M.close();break;
    case 'auth-tab':showAuth(a.dataset.tab);break;
    case 'demo-login':(async()=>{const r=await api('/auth/guest','POST');finishAuth(r?.user||{name:'Guest',email:'guest@hoppin.demo'});})();break;
    case 'venue':openVenue(a.dataset.id);break;
    case 'city':S.city=a.dataset.city;renderGrid();break;
    case 'cat':S.cat=a.dataset.cat;renderGrid();break;
    case 'catgo':S.cat=a.dataset.cat;renderGrid();$('#explore')?.scrollIntoView({behavior:'smooth'});break;
    case 'tonight-on':S.tonight=true;renderGrid();$('#explore')?.scrollIntoView({behavior:'smooth'});break;
    case 'tonight-toggle':S.tonight=!S.tonight;renderGrid();break;
    case 'day':B.iso=a.dataset.iso;B.slot=null;renderBooking();break;
    case 'slot':B.slot=a.dataset.slot;renderBooking();break;
    case 'reserve':{const v=VBY[B.id];showCheckout({venueId:B.id,iso:B.iso,slot:B.slot,price:slotPrice(v,B.slot)});break;}
    case 'to-bookings':M.close();go('/bookings');break;
    case 'chip':sendChat(a.dataset.t);break;
    case 'pay-hold':{const o=JSON.parse(a.dataset.order);showCheckout(o);break;}
    case 'save':{
      const id=a.dataset.id;let l=store.get('hoppin.saved',[]);const on=!l.includes(id);
      l=on?[...l,id]:l.filter(x=>x!==id);store.set('hoppin.saved',l);
      api('/saved/toggle','POST',{email:S.user?.email||'guest@hoppin.demo',venueId:id});
      a.classList.toggle('on',on);toast(on?'Saved venue':'Removed from saved');break;
    }
  }
});

document.addEventListener('submit',e=>{
  const f=e.target;
  if(f.id==='authForm'){e.preventDefault();submitAuth(f);}
  else if(f.id==='payForm'){e.preventDefault();submitPay(f);}
  else if(f.id==='chatForm'){e.preventDefault();const i=$('#chatIn');const t=i.value;i.value='';sendChat(t);}
});

window.addEventListener('hashchange',()=>{render();});

runLoader();
render();
})();
</script>
</body>
</html>
"""

targets = [
  'apps/web/public/poc.html',
  'apps/web/public/index.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc.html',
  'C:/Users/ROSHINI S/Downloads/hoppin-poc (1).html'
]

for t in targets:
  try:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    with open(t, 'w', encoding='utf-8') as f:
      f.write(html_code)
    print(f"Wrote {len(html_code)} bytes to {t}")
  except Exception as e:
    print(f"Error {t}: {e}")
