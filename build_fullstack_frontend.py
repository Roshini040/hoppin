# Generate complete fullstack Lilac Grail Edition with hover ball drop and full backend integration
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
   LILAC THEME TOKENS — Grail Aesthetic
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

/* Header floating pill */
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

/* 3D OPENING BOOK LOADER */
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
.book.open .book-cover { transform: rotateY(-130deg); }
.book.open { transform: translateX(80px) scale(2.4); }
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

/* HERO 3D SPIRAL OF 18 BENT CARDS & PARALLAX */
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
.mega.in span.char { opacity: 1; transform: none; }
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

/* CHAPTER 02 LILAC WIPE & COUNTDOWN CLOCK */
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

/* GUILDS SPINNING WHEEL OF 6 SHIELDS */
/* =========================================================
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

/* STATS INTERACTIVE 2D PHYSICS BALLS (CURSOR HOVER DROP) */
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
  cursor: crosshair;
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
  transition: transform 0.15s, color 0.15s;
  display: inline-block;
}
.stat-bucket span {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #c4b5fd;
  margin-top: 4px;
}

/* FOOTER WITH LIGHT RAYS & TALKING EMAIL */
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

/* TOTEMS: SQUEEZING BRACKETS & WORD RISE */
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
.bracket-counter.squeeze { transform: scaleX(0.7); }
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
.totem-word.active { transform: none; }
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

/* Chapter 03 row photo slide */
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
.cv > svg.cv-fallback { position: absolute; inset: 0; width: 100%; height: 100%; }
.cv::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, transparent 40%, rgba(0,0,0,0.75) 100%); }
.cv .b1 { position: absolute; left: 14px; top: 14px; display: flex; gap: 6px; z-index: 2; flex-wrap: wrap; }
.cv .rate {
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
}
.fav { position: absolute; right: 14px; bottom: 14px; z-index: 6; width: 38px; height: 38px; border-radius: 50%; background: rgba(13,8,24,0.8); backdrop-filter: blur(10px); color: #fff; font-size: 18px; display: grid; place-items: center; transition: all 0.2s; border: 1px solid rgba(255,255,255,0.15); }
.fav:hover { transform: scale(1.12); border-color: rgba(196,181,253,0.5); }
.fav.on { color: #ff6b81; border-color: rgba(255,107,129,0.4); }
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
.slot { padding: 12px 8px 11px; border-radius: 16px; border: 1px solid var(--line2); display: flex; flex-direction: column; align-items: center; gap: 2px; transition: all 0.18s; position: relative; }
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
  <a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>Bengaluru · Chennai</span></a>
  <nav class="nav" id="nav" aria-label="Primary"></nav>
  <button class="streak-btn" id="streakNavBtn" data-act="open-streaks" title="Activity Streak & XP">
    <span>🔥</span> <b id="streakDaysCount">4</b> <span class="streak-lbl">Streak</span>
  </button>
  <i class="sep"></i>
  <button class="icon-btn" id="themeBtn" data-act="theme" aria-label="Toggle theme"></button>
  <button class="acct" id="acct" data-act="account">Sign in</button>
</header>

<main id="app"></main>

<nav class="bnav" id="bnav" aria-label="Primary mobile"></nav>
<a class="floatcta" id="floatcta" href="#/chat"><span class="dot"></span>AI Concierge · Ask anything ↗</a>
<div id="toast" role="status" aria-live="polite"></div>
<div id="customCursor"></div>

<script>
(()=>{'use strict';
/* =========================================================
   UTILITIES & FULLSTACK BACKEND API ADAPTER
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
    try {
      const res2 = await fetch('/api' + path, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: body ? JSON.stringify(body) : undefined
      });
      if (res2.ok) return await res2.json();
    } catch (e2) {}
    return null;
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
   67 VENUES DATA & CURATED HIGH-DEF PHOTOGRAPHY
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
  return `<img src="${imgUrl}" alt="${esc(v.name)}" loading="lazy" class="cimg" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';">`;
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
const S={user:null,city:'all',cat:'all',area:'all',q:'',sort:'rating',tonight:false,view:'discover',chatCity:'BLR',chat:[],lastHits:[],pending:null,maxp:0,minr:0,geo:null};

/* Auth */
function requireAuth(reason,then){if(S.user){then();return;}S.pending=then;showAuth('in',reason);}

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
        <button onclick="setAuthCustomerMode('in')" style="flex:1;padding:8px;border-radius:999px;font-size:12.5px;font-weight:600;border:none;${!isUp?'background:var(--btn-bg);color:var(--btn-fg)':'color:var(--muted);background:transparent'}">Sign In</button>
        <button onclick="setAuthCustomerMode('up')" style="flex:1;padding:8px;border-radius:999px;font-size:12.5px;font-weight:600;border:none;${isUp?'background:var(--btn-bg);color:var(--btn-fg)':'color:var(--muted);background:transparent'}">Create Account</button>
      </div>

      <form id="customerAuthForm" onsubmit="event.preventDefault();submitCustomerAuth(this);">
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

      <form id="clubAdminForm" onsubmit="event.preventDefault();submitClubAdminAuth(this);">
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

      <form id="venueOwnerForm" onsubmit="event.preventDefault();submitVenueOwnerAuth(this);">
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

      <form id="supportAuthForm" onsubmit="event.preventDefault();submitSupportAuth(this);">
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
const NAV=[
  ['discover','Explore','Explore','#/','explore'],
  ['sports','Sports','Sports','#/cat/sports','sports'],
  ['dining','Dining','Dining','#/cat/dining','dining'],
  ['gaming','Games','Games','#/cat/gaming','gaming'],
  ['clubs','Clubs 🔥','Clubs','#/clubs','run'],
  ['owner','Partner ↗','Partner','#/owner','owner'],
  ['chat','AI Chat','AI Chat','#/chat','chat']
];
$('#nav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${n[1]}</a>`).join('');
$('#bnav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${IC[n[4]]}<span>${n[2]}</span></a>`).join('');

function navActive(){
  let k='discover';
  if(S.view==='chat') k='chat';
  else if(S.view==='clubs') k='clubs';
  else if(S.view==='owner') k='owner';
  else if(S.view==='discover' && ['sports','dining','gaming'].includes(S.cat)) k=S.cat;
  $$('[data-nav]').forEach(a=>a.classList.toggle('on',a.dataset.nav===k));
}
function themeIcon(){const t=document.documentElement.getAttribute('data-theme');$('#themeBtn').innerHTML=t==='light'?IC.moon:IC.sun;}
function toggleTheme(){const t=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',t);store.set('hoppin.theme',t);themeIcon();}

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
async function showVenue(id,pre){
  const v=VBY[id];const days=validDays(v,6);
  B={id,iso:(pre&&pre.iso)||days[0],slot:(pre&&pre.slot)||null};
  
  // Try fetching slots live from backend
  const backendSlots = await api(`/venues/${id}/slots?date=${B.iso}&email=${encodeURIComponent(S.user?.email||'')}`);
  
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
  renderBooking(backendSlots?.slots);
}

function renderBooking(liveSlots=null){
  const v=VBY[B.id];const days=validDays(v,6);
  const slotBtns=v.slots.map(s=>{
    let a = avail(v, B.iso, s);
    if(liveSlots){
      const match = liveSlots.find(ls=>ls.slot===s);
      if(match) a = match;
    }
    const dis=['full','past','yours'].includes(a.state);
    const lab=a.state==='full'?'Full':a.state==='past'?'Passed':a.state==='yours'?'Booked':inr(slotPrice(v,s));
    return `<button class="slot ${a.state} ${B.slot===s?'on':''}" data-act="slot" data-slot="${s}" ${dis?'disabled':''} aria-pressed="${B.slot===s}"><span style="font-family:var(--mono);font-size:13px;font-weight:600">${s}</span><span style="font-size:12px;color:var(--muted)">${lab}</span>${a.state==='few'?`<span style="position:absolute;top:-8px;right:8px;font-size:9.5px;background:var(--warn);color:#fff;padding:2px 7px;border-radius:99px">${a.left} left</span>`:''}</button>`;
  }).join('');

  const price=B.slot?slotPrice(v,B.slot):null;
  $('#vright').innerHTML=`
    <div><h4 class="kicker">Pick a day</h4><div class="days" style="margin-top:10px">${days.map(d=>{const x=fromISO(d);return `<button class="day ${d===B.iso?'on':''}" data-act="day" data-iso="${d}"><span style="font-family:var(--mono);font-size:10px;text-transform:uppercase">${d===todayISO()?'Today':WD[x.getDay()]}</span><b style="display:block;font-family:var(--serif);font-size:22px">${x.getDate()}</b><span style="font-family:var(--mono);font-size:10px;color:var(--muted)">${MO[x.getMonth()]}</span></button>`;}).join('')}</div></div>
    <div><h4 class="kicker">Pick a time</h4><div class="slots" style="margin-top:10px">${slotBtns}</div></div>
    <div class="bookbar">
      <div style="font-size:13px;color:var(--muted)">${B.slot?`${dayLabel(B.iso)}, ${B.slot}<b style="display:block;color:var(--text);font-size:19px">${inr(price)}</b>`:'Choose a slot'}</div>
      <button class="btn" data-act="reserve" ${B.slot?'':'disabled'}>${B.resched?'Move booking':'Reserve slot'}</button>
    </div>`;
}

/* Checkout with UPI (QR / Apps) and Card */
const FEE=30;
let currentPayMode = 'upi';

function showCheckout(order){
  const v=VBY[order.venueId];
  order.fee=FEE;
  order.disc=order.disc||0;
  order.total=order.price+FEE-order.disc;
  currentPayMode = 'upi';

  // Procedural QR SVG for UPI payment
  const qrSvg = `<svg viewBox="0 0 100 100" width="136" height="136" aria-label="UPI QR Code">
    <rect width="100" height="100" fill="#ffffff" rx="8"/>
    <!-- Position Detection Patterns (Corners) -->
    <rect x="8" y="8" width="24" height="24" fill="#0d0818" rx="3"/>
    <rect x="12" y="12" width="16" height="16" fill="#ffffff" rx="2"/>
    <rect x="16" y="16" width="8" height="8" fill="#0d0818" rx="1"/>
    
    <rect x="68" y="8" width="24" height="24" fill="#0d0818" rx="3"/>
    <rect x="72" y="12" width="16" height="16" fill="#ffffff" rx="2"/>
    <rect x="76" y="16" width="8" height="8" fill="#0d0818" rx="1"/>
    
    <rect x="8" y="68" width="24" height="24" fill="#0d0818" rx="3"/>
    <rect x="12" y="72" width="16" height="16" fill="#ffffff" rx="2"/>
    <rect x="16" y="76" width="8" height="8" fill="#0d0818" rx="1"/>
    
    <!-- Procedural Data Modules -->
    <rect x="36" y="8" width="6" height="6" fill="#0d0818"/>
    <rect x="46" y="8" width="6" height="6" fill="#0d0818"/>
    <rect x="56" y="8" width="6" height="6" fill="#0d0818"/>
    <rect x="36" y="18" width="6" height="6" fill="#0d0818"/>
    <rect x="46" y="24" width="6" height="6" fill="#0d0818"/>
    <rect x="56" y="18" width="6" height="6" fill="#0d0818"/>
    <rect x="8" y="36" width="6" height="6" fill="#0d0818"/>
    <rect x="18" y="46" width="6" height="6" fill="#0d0818"/>
    <rect x="8" y="56" width="6" height="6" fill="#0d0818"/>
    <rect x="36" y="36" width="28" height="28" fill="#7c3aed" rx="5"/>
    <text x="50" y="54" text-anchor="middle" font-family="Plus Jakarta Sans,sans-serif" font-size="12" font-weight="bold" fill="#ffffff">UPI</text>
    <rect x="68" y="36" width="6" height="6" fill="#0d0818"/>
    <rect x="78" y="46" width="6" height="6" fill="#0d0818"/>
    <rect x="88" y="36" width="6" height="6" fill="#0d0818"/>
    <rect x="36" y="68" width="6" height="6" fill="#0d0818"/>
    <rect x="46" y="78" width="6" height="6" fill="#0d0818"/>
    <rect x="56" y="68" width="6" height="6" fill="#0d0818"/>
    <rect x="68" y="68" width="6" height="6" fill="#0d0818"/>
    <rect x="78" y="78" width="6" height="6" fill="#0d0818"/>
    <rect x="88" y="88" width="6" height="6" fill="#0d0818"/>
  </svg>`;

  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div style="padding:34px 32px 32px">
    <div class="kicker" style="color:var(--pastel)">Secure instant checkout</div>
    <h2 class="display" style="font-size:2.3rem;margin:8px 0 10px">Confirm & Pay</h2>
    
    <!-- Venue booking summary card -->
    <div style="display:flex;gap:14px;padding:14px;border-radius:20px;border:1px solid var(--line2);background:var(--bg3);margin-bottom:18px;align-items:center">
      <div style="width:68px;height:68px;border-radius:14px;overflow:hidden;flex:none;position:relative">${coverMedia(v)}</div>
      <div>
        <b style="font-family:var(--serif);font-size:1.2rem;display:block">${esc(v.name)}</b>
        <span style="font-size:13px;color:var(--muted)">📅 ${dayLabel(order.iso)} · ⏰ ${order.slot} · 📍 ${esc(v.area)}</span>
      </div>
    </div>
    
    <!-- Price breakdown -->
    <div style="font-size:14px;margin-bottom:20px;background:var(--bg);padding:14px 18px;border-radius:18px;border:1px solid var(--line)">
      <div style="display:flex;justify-content:space-between;padding:5px 0;color:var(--muted)"><span>Court/Venue Slot</span><span style="font-family:var(--mono)">${inr(order.price)}</span></div>
      <div style="display:flex;justify-content:space-between;padding:5px 0;color:var(--muted)"><span>Platform Fee</span><span style="font-family:var(--mono)">${inr(order.fee)}</span></div>
      ${order.disc?`<div style="display:flex;justify-content:space-between;padding:5px 0;color:var(--ok)"><span>Promo Discount</span><span style="font-family:var(--mono)">−${inr(order.disc)}</span></div>`:''}
      <div style="display:flex;justify-content:space-between;font-weight:700;font-size:17px;border-top:1px dashed var(--line);margin-top:8px;padding-top:10px">
        <span>Amount Payable</span>
        <span style="color:var(--pastel);font-family:var(--mono)">${inr(order.total)}</span>
      </div>
    </div>

    <!-- Payment Method Selector Tabs -->
    <div style="display:flex;gap:6px;margin-bottom:18px;background:var(--bg3);padding:4px;border-radius:999px;border:1px solid var(--line2)">
      <button type="button" id="tabUPI" data-act="switch-pay" data-mode="upi" style="flex:1;padding:11px 14px;border-radius:999px;font-family:var(--mono);font-size:12px;font-weight:600;letter-spacing:0.06em;background:var(--btn-bg);color:var(--btn-fg);transition:all 0.2s">📱 UPI (QR / Apps)</button>
      <button type="button" id="tabCard" data-act="switch-pay" data-mode="card" style="flex:1;padding:11px 14px;border-radius:999px;font-family:var(--mono);font-size:12px;font-weight:600;letter-spacing:0.06em;color:var(--muted);transition:all 0.2s">💳 Credit / Debit Card</button>
    </div>

    <form id="payForm" novalidate>
      <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px">
        <label class="kicker">Email for ticket & receipt</label>
        <input id="pe" name="email" type="email" value="${esc(S.user?S.user.email:'')}" placeholder="you@domain.com" required style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-family:var(--mono);font-size:13px">
      </div>

      <!-- UPI Payment View -->
      <div id="upiView" style="display:block">
        <div style="display:flex;flex-direction:column;align-items:center;padding:18px;border-radius:22px;border:1px solid var(--line2);background:var(--bg);margin-bottom:16px;text-align:center">
          <div style="font-family:var(--mono);font-size:10.5px;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);margin-bottom:10px">Scan & Pay via any UPI App</div>
          <div style="padding:10px;background:#fff;border-radius:18px;box-shadow:0 10px 30px rgba(0,0,0,0.25);margin-bottom:12px">
            ${qrSvg}
          </div>
          <div style="display:flex;align-items:center;gap:6px;font-family:var(--mono);font-size:13px;font-weight:600;color:var(--text)">
            <span>hoppin.pay@okhdfcbank</span>
            <button type="button" style="color:var(--pastel);font-size:11px;text-decoration:underline;cursor:pointer" onclick="navigator.clipboard?.writeText('hoppin.pay@okhdfcbank');toast('UPI ID copied!');">Copy</button>
          </div>
          <span style="font-size:12px;color:var(--muted);margin-top:4px">Instant confirmation via Google Pay · PhonePe · Paytm · Cred</span>
        </div>

        <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:16px">
          <label class="kicker">Or Enter your VPA / UPI ID</label>
          <input id="upiId" name="upiId" placeholder="e.g. mobile@paytm or user@okhdfcbank" value="roshini@okaxis" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-family:var(--mono);font-size:13px">
          <div style="display:flex;gap:6px;margin-top:2px;flex-wrap:wrap">
            <button type="button" class="tag" style="cursor:pointer" onclick="$('#upiId').value=$('#upiId').value.split('@')[0]+'@okhdfcbank'">@okhdfcbank</button>
            <button type="button" class="tag" style="cursor:pointer" onclick="$('#upiId').value=$('#upiId').value.split('@')[0]+'@okaxis'">@okaxis</button>
            <button type="button" class="tag" style="cursor:pointer" onclick="$('#upiId').value=$('#upiId').value.split('@')[0]+'@paytm'">@paytm</button>
            <button type="button" class="tag" style="cursor:pointer" onclick="$('#upiId').value=$('#upiId').value.split('@')[0]+'@ybl'">@ybl</button>
          </div>
        </div>

        <div style="display:flex;gap:8px;margin-bottom:16px">
          <button type="button" class="pill" style="flex:1;text-align:center" onclick="toast('Opening Google Pay...')">🟢 Google Pay</button>
          <button type="button" class="pill" style="flex:1;text-align:center" onclick="toast('Opening PhonePe...')">🟣 PhonePe</button>
          <button type="button" class="pill" style="flex:1;text-align:center" onclick="toast('Opening Paytm...')">🔵 Paytm</button>
        </div>

        <button class="btn block" type="submit" id="payBtn" style="background:#7c3aed;color:#fff">
          ⚡ Pay ${inr(order.total)} with UPI
        </button>
      </div>

      <!-- Card Payment View -->
      <div id="cardView" style="display:none">
        <div style="display:flex;gap:10px;padding:12px 14px;border-radius:16px;background:var(--tint);color:var(--tint-fg);font-size:12.5px;margin-bottom:16px">
          ${IC.info}<span>Card test mode: <b>4242 4242 4242 4242</b>, any future expiry date, any 3-digit CVC.</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:14px">
          <label class="kicker">Card number</label>
          <input id="pc" name="card" value="4242 4242 4242 4242" style="height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-family:var(--mono);font-size:13px">
        </div>
        <div style="display:flex;gap:12px;margin-bottom:18px">
          <div style="flex:1">
            <label class="kicker">Expiry</label>
            <input id="px" name="exp" value="12/28" style="width:100%;height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-family:var(--mono);font-size:13px">
          </div>
          <div style="flex:1">
            <label class="kicker">CVC</label>
            <input id="pv" name="cvc" value="123" style="width:100%;height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-family:var(--mono);font-size:13px">
          </div>
        </div>
        <button class="btn block" type="submit" id="payCardBtn">
          ${IC.card}<span>Pay ${inr(order.total)} with Card</span>
        </button>
      </div>
    </form>
  </div>`,'md');
  showCheckout.order=order;
}

function submitPay(form){
  const o=showCheckout.order;
  const btn = currentPayMode === 'upi' ? $('#payBtn') : $('#payCardBtn');
  if(btn){
    btn.disabled=true;
    btn.innerHTML='<span class="spin"></span><span>Verifying & Confirming…</span>';
  }

  const userEmail = $('#pe')?.value?.trim() || S.user?.email || 'roshini@hoppin.demo';
  const payDetail = currentPayMode === 'upi' ? `UPI (${$('#upiId')?.value || 'user@okaxis'})` : 'Card 4242';

  setTimeout(async()=>{
    const bkRes=await api('/bookings','POST',{
      venueId:o.venueId,iso:o.iso,slot:o.slot,partySize:1,
      userEmail,userName:S.user?.name||'Roshini',
      card:currentPayMode==='upi'?'UPI':'4242',
      paymentMethod:payDetail,
      disc:o.disc||0
    });
    const bk=bkRes?.booking||{
      ref:o.ref||newRef(),venueId:o.venueId,iso:o.iso,slot:o.slot,
      price:o.price,fee:o.fee,total:o.total,at:Date.now(),
      paymentMethod:payDetail,
      last4:currentPayMode==='upi'?'UPI':'4242'
    };
    const list=store.get('hoppin.bookings:'+userEmail,[]);
    list.unshift(bk);
    store.set('hoppin.bookings:'+userEmail,list);
    showTicket(bk,true);
    if(S.view==='chat'){
      pushAssistant({text:`🎉 Payment received via <strong>${payDetail}</strong>. Confirmed <strong>${esc(VBY[bk.venueId].name)}</strong> for ${esc(dayLabel(bk.iso))} at ${bk.slot}. Reference: <strong>${bk.ref}</strong>. View ticket in My tickets!`});
    }
  }, 950);
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
   HERO 18 SPIRAL CARDS SETUP
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
   STATS 2D PHYSICS BALLS (HOVER CURSOR DROP - NO CLICK REQUIRED)
   ========================================================= */
class PhysicsBalls {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.balls = [];
    this.columns = 4;
    this.colWidth = 0;
    this.animId = null;
    this.counts = [18, 13, 12, 9];
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.spawnInitial();
    this.loop();
  }

  resize() {
    if (!this.canvas.parentElement) return;
    this.canvas.width = this.canvas.parentElement.clientWidth;
    this.canvas.height = this.canvas.parentElement.clientHeight;
    this.colWidth = this.canvas.width / this.columns;
  }

  spawnBallAt(cursorX) {
    if (this.colWidth <= 0) this.resize();
    const col = Math.min(3, Math.max(0, Math.floor(cursorX / (this.colWidth || 1))));
    const r = Math.random() * 5 + 9;
    const colors = ['#c4b5fd', '#a78bfa', '#7c3aed', '#f0b94a', '#34d399', '#f4f1ea', '#e9d5ff', '#ddd6fe'];
    const minX = col * this.colWidth + r + 2;
    const maxX = (col + 1) * this.colWidth - r - 2;
    const spawnX = Math.min(maxX, Math.max(minX, cursorX + (Math.random() - 0.5) * 16));

    this.balls.push({
      x: spawnX,
      y: -15,
      vx: (Math.random() - 0.5) * 2,
      vy: Math.random() * 3.5 + 2.5,
      r,
      col,
      color: colors[Math.floor(Math.random() * colors.length)],
      bounces: 0
    });

    // Increment bucket count & animate stat badge
    this.counts[col]++;
    const ids = ['statSports', 'statPubs', 'statFitness', 'statGaming'];
    const el = document.getElementById(ids[col]);
    if (el) {
      el.textContent = this.counts[col];
      el.style.transform = 'scale(1.22)';
      el.style.color = '#c4b5fd';
      setTimeout(() => {
        if (el) {
          el.style.transform = 'scale(1)';
          el.style.color = '#fff';
        }
      }, 140);
    }

    // Limit total balls for 60fps
    if (this.balls.length > 140) {
      this.balls.shift();
    }
  }

  spawnInitial() {
    for (let c = 0; c < 4; c++) {
      for (let i = 0; i < 5; i++) {
        setTimeout(() => this.spawnBallAt((c + 0.5) * (this.colWidth || 160)), i * 140 + c * 60);
      }
    }
  }

  loop() {
    const { ctx, canvas } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const gravity = 0.42;
    const floor = canvas.height - 6;

    for (let i = 0; i < this.balls.length; i++) {
      const b = this.balls[i];
      b.vy += gravity;
      b.x += b.vx;
      b.y += b.vy;

      // Col boundaries
      const minX = b.col * this.colWidth + b.r;
      const maxX = (b.col + 1) * this.colWidth - b.r;
      if (b.x < minX) { b.x = minX; b.vx *= -0.55; }
      if (b.x > maxX) { b.x = maxX; b.vx *= -0.55; }

      // Floor collision with realistic settling
      if (b.y > floor - b.r) {
        b.y = floor - b.r;
        b.vy *= -0.50;
        b.vx *= 0.86;
        b.bounces++;
      }

      // Ball to ball collision within same column
      for (let j = i + 1; j < this.balls.length; j++) {
        const o = this.balls[j];
        if (o.col !== b.col) continue;
        const dx = o.x - b.x;
        const dy = o.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const minDist = b.r + o.r;
        if (dist < minDist && dist > 0) {
          const overlap = (minDist - dist) * 0.5;
          const nx = dx / dist;
          const ny = dy / dist;
          b.x -= nx * overlap;
          b.y -= ny * overlap;
          o.x += nx * overlap;
          o.y += ny * overlap;
          b.vx -= nx * 0.18;
          b.vy -= ny * 0.18;
          o.vx += nx * 0.18;
          o.vy += ny * 0.18;
        }
      }

      // Render ball with lilac glow
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fillStyle = b.color;
      ctx.shadowColor = 'rgba(139, 92, 246, 0.45)';
      ctx.shadowBlur = 10;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    this.animId = requestAnimationFrame(() => this.loop());
  }
}

/* =========================================================
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
      <p class="sub">Curated courts, turfs, taprooms, resto-bars and morning run clubs. Pick a slot, show up, and let the plan survive the group chat.</p>
      <div style="display:flex;gap:12px;margin-top:34px;flex-wrap:wrap">
        <a class="btn" href="#explore">Explore Places & Turfs</a>
        <a class="btn ghost" href="#/chat">AI Concierge ↗</a>
      </div>
    </div>
    <div class="hero-spiral" id="heroSpiral" aria-hidden="true">
      <div class="spiral-ring" id="spiralRing">${buildHeroSpiralCards()}</div>
    </div>
  </section>

  <!-- FLOATING 4 SQUARE DROPS BRIDGE (OVERLAPPING HERO & CHAPTER 01) -->
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

  <!-- CHAPTER 01: Staggered Lines Rise & Problem Showcase Photos -->
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

  <!-- CHAPTER 04: GUILDS 3D SPINNING WHEEL -->
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

  <!-- STATS INTERACTIVE 2D PHYSICS BALLS (HOVER CURSOR DROP) -->
  <section class="stats-physics-sec wrap" id="statsSec">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:18px">
      <div><div class="kicker">Live Inventory</div><h2 class="display" style="font-size:clamp(2rem,4.4vw,3.6rem)">Venues by the numbers</h2></div>
      <p style="color:var(--muted);font-size:14px">Keep your cursor over the tank — balls will continuously rain and stack!</p>
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
    <div class="sec-h"><h2 class="display">All 67 Venues</h2><p>Filter by city, category or price. Connected live to the Hoppin backend API.</p></div>
    <div class="ctrl">
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
    </div>
    <div id="count" style="margin-bottom:20px;font-family:var(--mono);font-size:12px;color:var(--muted)"></div>
    <div class="grid" id="grid"></div>
  </section>

  <!-- FOOTER WITH LIGHT RAYS & TALKING EMAIL -->
  
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

  `;
}

function cardHTML(v){
  const sv=store.get('hoppin.saved',[]).includes(v.id);
  return `<article class="card" tabindex="0" data-act="venue" data-id="${v.id}">
    <div class="cv">${coverMedia(v)}
      <div class="b1"><span class="badge">${CITY[v.city].short}</span><span class="badge">${CATS[v.cat].label.split(' & ')[0]}</span></div>
      <button class="fav ${sv?'on':''}" data-act="save" data-id="${v.id}" aria-label="Save">♥</button>
      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><span class="rate-sep">·</span><span class="rate-count">${v.reviews.toLocaleString()} reviews</span></div>
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
    if(S.area&&S.area!=='all'&&!v.area.toLowerCase().includes(S.area.toLowerCase()))return false;
    if(S.tonight&&!openTonight(v).length)return false;
    if(q){const hay=(v.name+' '+v.area+' '+CITY[v.city].name+' '+CATS[v.cat].label).toLowerCase();if(!hay.includes(q))return false;}
    return true;
  });
  const countEl=$('#count');
  if(countEl)countEl.textContent=`SHOWING ${list.length} OF ${VENUES.length} REAL VENUES WITH HIGH-RES PHOTOS`;
  const gridEl=$('#grid');
  if(gridEl)gridEl.innerHTML=list.length?list.map(cardHTML).join(''):'<div style="grid-column:1/-1;text-align:center;padding:60px 20px;color:var(--muted)"><p style="font-size:18px">No venues found for this filter.</p><button class="btn sm" style="margin-top:14px" onclick="S.city=\'all\';S.cat=\'all\';S.area=\'all\';S.q=\'\';renderGrid();">Reset all filters</button></div>';
  $$('#cityseg button').forEach(b=>b.classList.toggle('on',b.dataset.city===S.city));
  $$('#catpills .pill').forEach(b=>b.classList.toggle('on',b.dataset.cat===S.cat));
  $$('#areaChips .area-chip').forEach(b=>b.classList.toggle('on',b.dataset.area===(S.area||'all')));
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
    <form id="createClubForm" onsubmit="event.preventDefault();submitCreateClub(this);">
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

      <form id="venueDPForm" onsubmit="event.preventDefault();submitVenueDPStatus(this);">
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
    <form id="registerVenueForm" onsubmit="event.preventDefault();submitNewVenue(this);">
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

/* =========================================================
   3-ADMIN RBAC PORTAL (#/admin)
   ========================================================= */
let currentAdminRole = 'super_admin';


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

function render(){
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
  }else if(view==='chat'){
    app.innerHTML=chatHTML();
    if(!S.chat.length)S.chat.push({role:'a',text:`Hi! I'm the hoppin. AI Concierge. Ask about courts, gyms, taprooms, or game cafes across Bengaluru and Chennai.`});
    $('#stream').innerHTML=S.chat.map(msgHTML).join('');
  }else{
    app.innerHTML=bookingsHTML();
  }
  navActive();
}

/* Hero Spiral Tilt & Parallax */
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

/* Lilac Wipe & Countdown Clock */
function initLilacWipe(){
  const wipe=$('#lilacWipe');
  const sec=$('#wipeSection');
  const clk=$('#bigCountdown');

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

/* Physics Balls (BALLS FALL CONTINUOUSLY ON HOVER - NO CLICK REQUIRED) */
let physicsInst=null;
function initPhysics(){
  const canvas=$('#ballsCanvas');
  const stage=$('#physicsStage');
  if(!canvas||!stage)return;
  physicsInst=new PhysicsBalls(canvas);

  let hoverInterval = null;
  let currentX = stage.clientWidth / 2;

  stage.addEventListener('mouseenter', (e) => {
    const rect = stage.getBoundingClientRect();
    currentX = e.clientX - rect.left;
    if (hoverInterval) clearInterval(hoverInterval);
    // Continuous stream of falling balls while hovering
    hoverInterval = setInterval(() => {
      if (physicsInst) physicsInst.spawnBallAt(currentX);
    }, 110);
  });

  stage.addEventListener('mousemove', (e) => {
    const rect = stage.getBoundingClientRect();
    currentX = e.clientX - rect.left;
    // Spawn immediate ball upon moving cursor across columns
    if (Math.random() > 0.28) {
      if (physicsInst) physicsInst.spawnBallAt(currentX);
    }
  });

  stage.addEventListener('mouseleave', () => {
    if (hoverInterval) {
      clearInterval(hoverInterval);
      hoverInterval = null;
    }
  });
}

/* Guilds 3D Wheel Spin & Scroll Acceleration */
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

/* Totems Word Rise & Squeezing Brackets */
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

/* Light Rays & Talking Email Waitlist */
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

/* Opening Book Loader */
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
    case 'account':if(S.user)showProfileModal();else showAuth('customer');break;
    case 'close':M.close();break;
    case 'open-streaks':showStreaksModal();break;
    case 'create-club':showCreateClubModal();break;
    case 'register-venue':showRegisterVenueModal();break;
    case 'open-dp-status':showDPStatusModal(a.dataset.id);break;
    case 'open-club':showDPStatusModal(a.dataset.id);break;
    case 'rsvp-club':rsvpClub(a.dataset.id);break;
    case 'claim-streak':simulateActivityStreakCheckin();break;
    case 'claim-dp-offer':claimDPOffer(a.dataset.code,a.dataset.venue);break;
    case 'open-customer-auth':M.close();showAuth('customer');break;
    case 'view-bookings':M.close();go('/bookings');break;
    case 'signout':S.user=null;store.set('hoppin.session',null);acctBtn();M.close();toast('Signed out successfully.');render();break;
    case 'nav-owner':M.close();go('/owner');break;
    case 'admin-switch-role':switchAdminRole(a.dataset.role);break;
    case 'auth-tab':showAuth(a.dataset.tab);break;
    case 'demo-login':(async()=>{const r=await api('/auth/guest','POST');finishAuth(r?.user||{name:'Guest',email:'guest@hoppin.demo'});})();break;
    case 'venue':openVenue(a.dataset.id);break;
    case 'city':S.city=a.dataset.city;renderGrid();break;
    case 'cat':S.cat=a.dataset.cat;renderGrid();break;
    case 'catgo':S.cat=a.dataset.cat;renderGrid();$('#explore')?.scrollIntoView({behavior:'smooth'});break;
    case 'switch-pay':{
      const mode = a.dataset.mode;
      currentPayMode = mode;
      const tU = $('#tabUPI'); const tC = $('#tabCard');
      const vU = $('#upiView'); const vC = $('#cardView');
      if(mode==='upi'){
        if(tU){tU.style.background='var(--btn-bg)';tU.style.color='var(--btn-fg)';}
        if(tC){tC.style.background='none';tC.style.color='var(--muted)';}
        if(vU)vU.style.display='block';
        if(vC)vC.style.display='none';
      }else{
        if(tC){tC.style.background='var(--btn-bg)';tC.style.color='var(--btn-fg)';}
        if(tU){tU.style.background='none';tU.style.color='var(--muted)';}
        if(vC)vC.style.display='block';
        if(vU)vU.style.display='none';
      }
      break;
    }
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
    case 'area':S.area=a.dataset.area;renderGrid();break;
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
  else if(f.id==='customerAuthForm'){e.preventDefault();submitCustomerAuth(f);}
  else if(f.id==='clubAdminForm'){e.preventDefault();submitClubAdminAuth(f);}
  else if(f.id==='venueOwnerForm'){e.preventDefault();submitVenueOwnerAuth(f);}
  else if(f.id==='supportAuthForm'){e.preventDefault();submitSupportAuth(f);}
  else if(f.id==='createClubForm'){e.preventDefault();submitCreateClub(f);}
  else if(f.id==='registerVenueForm'){e.preventDefault();submitNewVenue(f);}
  else if(f.id==='venueDPForm'){e.preventDefault();submitVenueDPStatus(f);}
});

window.addEventListener('hashchange',()=>{render();});


// Expose all interactive functions to window so inline onclick and onsubmit work seamlessly
window.switchAuthRole = switchAuthRole;
window.setAuthCustomerMode = function(mode){ authCustomerMode = mode; switchAuthRole('customer'); };
window.submitCustomerAuth = submitCustomerAuth;
window.submitClubAdminAuth = submitClubAdminAuth;
window.submitVenueOwnerAuth = submitVenueOwnerAuth;
window.submitSupportAuth = submitSupportAuth;
window.loginDemoCustomer = loginDemoCustomer;
window.loginDemoClubAdmin = loginDemoClubAdmin;
window.loginDemoVenueOwner = loginDemoVenueOwner;
window.loginDemoSupport = loginDemoSupport;
window.showCreateClubModal = showCreateClubModal;
window.submitCreateClub = submitCreateClub;
window.showRegisterVenueModal = showRegisterVenueModal;
window.submitNewVenue = submitNewVenue;
window.simulateActivityStreakCheckin = simulateActivityStreakCheckin;
window.filterClubsCity = filterClubsCity;
window.rsvpClub = rsvpClub;
window.handleOwnerPhotoFile = handleOwnerPhotoFile;
window.setOwnerPhotoPreset = setOwnerPhotoPreset;
window.submitVenueDPStatus = submitVenueDPStatus;
window.verifyOwnerTicket = verifyOwnerTicket;
window.showDPStatusModal = showDPStatusModal;
window.showStreaksModal = showStreaksModal;
window.showProfileModal = showProfileModal;
window.showAuth = showAuth;
window.loginPartnerDemo = loginPartnerDemo;

runLoader();
render();
})();
</script>
</body>
</html>
"""

targets = [
  'apps/web/index.html',
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
    print(f"Successfully wrote {len(html_code)} bytes to {t}")
  except Exception as e:
    print(f"Error writing {t}: {e}")
