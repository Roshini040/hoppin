# Python script to build the complete hoppin-poc.html with real curated images
import os

html_content = r'''<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>hoppin. — discover real places</title>
<meta name="description" content="Discover and book courts, turfs, gyms, taprooms, game cafes and run clubs across Bengaluru and Chennai.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<script>
try{var t=localStorage.getItem('hoppin.theme');t=t?JSON.parse(t):'dark';document.documentElement.setAttribute('data-theme',t==='light'?'light':'dark');}catch(e){}
</script>
<style>
/* =========================================================
   TOKENS — light (warm cream paper) is base, dark (noir) overrides
   ========================================================= */
:root{
  --bg:#f7f4ec; --bg2:#ffffff; --bg3:#efeadf;
  --text:#121216; --muted:#5b5d55;
  --line:rgba(0,0,0,.10); --line2:rgba(0,0,0,.2);
  --glass:rgba(255,252,246,.8);
  --btn-bg:#14210f; --btn-fg:#f7f4ec;
  --tint:#dcefc3; --tint-fg:#24401a;
  --gold:#9a6b10; --ok:#0c8a5f; --warn:#b4570f; --bad:#b3261e;
  --shadow:0 24px 70px rgba(40,40,10,.16);
  --focus:#14210f;
  --pastel:#cdeea6; --ink:#13200f;
  --serif:'Bodoni Moda','Didot','Bodoni 72',Georgia,serif;
  --sans:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  --mono:'Space Grotesk',ui-monospace,SFMono-Regular,Menlo,monospace;
  color-scheme:light;
  box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#000; --bg2:#0e100d; --bg3:#171a14;
    --text:#f4f1ea; --muted:#9da295;
    --line:rgba(255,255,255,.10); --line2:rgba(255,255,255,.18);
    --glass:rgba(14,16,13,.78);
    --btn-bg:#cdf3a6; --btn-fg:#142010;
    --tint:rgba(205,243,166,.14); --tint-fg:#cdf3a6;
    --gold:#f0b94a; --ok:#34d399; --warn:#f0b94a; --bad:#ff7a70;
    --shadow:0 24px 80px rgba(0,0,0,.7);
    --focus:#cdf3a6; color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#000; --bg2:#0e100d; --bg3:#171a14;
  --text:#f4f1ea; --muted:#9da295;
  --line:rgba(255,255,255,.10); --line2:rgba(255,255,255,.18);
  --glass:rgba(14,16,13,.78);
  --btn-bg:#cdf3a6; --btn-fg:#142010;
  --tint:rgba(205,243,166,.14); --tint-fg:#cdf3a6;
  --gold:#f0b94a; --ok:#34d399; --warn:#f0b94a; --bad:#ff7a70;
  --shadow:0 24px 80px rgba(0,0,0,.7);
  --focus:#cdf3a6; color-scheme:dark;
}
html{scroll-padding-top:env(safe-area-inset-top,0px);scroll-behavior:smooth;-webkit-text-size-adjust:100%}
html.lock,html.lock body{overflow:hidden}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);font-size:16px;line-height:1.55;transition:background .45s ease,color .45s ease;-webkit-font-smoothing:antialiased;overflow-x:hidden}
button,input,select{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--focus);outline-offset:3px;border-radius:8px}
h1,h2,h3,p{margin:0}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* type */
.display{font-family:var(--serif);font-weight:400;text-transform:uppercase;letter-spacing:-.02em;line-height:.95;font-optical-sizing:auto}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);font-weight:500}
.mono{font-family:var(--mono)}

/* =========================================================
   HEADER (desktop floating pill) + BOTTOM CAPSULE (phone)
   ========================================================= */
.hdr{position:fixed;top:calc(14px + env(safe-area-inset-top,0px));left:50%;transform:translateX(-50%);z-index:60;display:flex;align-items:center;gap:6px;padding:7px 8px 7px 22px;border-radius:999px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line);max-width:calc(100% - 24px);box-shadow:0 10px 40px rgba(0,0,0,.18);transition:background .45s}
.brand{display:flex;align-items:baseline;gap:12px;margin-right:14px;white-space:nowrap}
.brand b{font-family:var(--serif);font-weight:500;font-size:24px;letter-spacing:-.03em;line-height:1}
.brand span{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;color:var(--muted);text-transform:uppercase}
.nav{display:flex;gap:2px}
.nav a{padding:9px 15px;border-radius:999px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);transition:background .2s,color .2s;white-space:nowrap}
.nav a:hover{color:var(--text)}
.nav a.on{background:var(--btn-bg);color:var(--btn-fg)}
.hdr .sep{width:1px;height:22px;background:var(--line);margin:0 6px}
.icon-btn{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);transition:background .2s}
.icon-btn:hover{background:var(--tint)}
.icon-btn svg{width:18px;height:18px}
.acct{height:38px;padding:0 16px;border-radius:999px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;background:var(--tint);color:var(--tint-fg);display:inline-flex;align-items:center;gap:8px;white-space:nowrap}
.acct .av{width:24px;height:24px;border-radius:50%;background:var(--btn-bg);color:var(--btn-fg);display:grid;place-items:center;font-family:var(--serif);font-size:13px;text-transform:uppercase}
.acct.has{padding:0 14px 0 6px}

.bnav{display:none;position:fixed;left:50%;transform:translateX(-50%);bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:60;padding:6px;gap:2px;border-radius:999px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line2);box-shadow:0 14px 44px rgba(0,0,0,.35);width:min(400px,calc(100% - 20px))}
.bnav a{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;padding:8px 2px 7px;border-radius:999px;color:var(--muted);font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;transition:background .2s,color .2s;min-width:0}
.bnav a svg{width:20px;height:20px}
.bnav a.on{background:var(--btn-bg);color:var(--btn-fg)}

.floatcta{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(24px + env(safe-area-inset-bottom,0px));z-index:55;display:flex;align-items:center;gap:12px;padding:12px 22px;border-radius:999px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line2);font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;box-shadow:0 14px 44px rgba(0,0,0,.3);transition:transform .25s,background .3s}
.floatcta:hover{transform:translateX(-50%) translateY(-3px)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 0 var(--ok);animation:pulse 2.2s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(52,211,153,.5)}70%{box-shadow:0 0 0 9px rgba(52,211,153,0)}100%{box-shadow:0 0 0 0 rgba(52,211,153,0)}}

/* =========================================================
   BUTTONS / CONTROLS
   ========================================================= */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:15px 28px;border-radius:999px;background:var(--btn-bg);color:var(--btn-fg);font-weight:600;font-size:14.5px;letter-spacing:.01em;transition:transform .2s,opacity .2s,filter .2s;min-height:50px}
.btn:hover{transform:translateY(-2px);filter:brightness(1.05)}
.btn:disabled{opacity:.38;cursor:not-allowed;transform:none}
.btn.ghost{background:transparent;color:var(--text);border:1px solid var(--line2)}
.btn.ink{background:var(--ink);color:var(--pastel)}
.btn.block{width:100%}
.btn.sm{padding:10px 18px;min-height:40px;font-size:13px}
.btn .spin{width:16px;height:16px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.seg{display:inline-flex;padding:4px;border-radius:999px;border:1px solid var(--line);background:var(--bg2);gap:2px;max-width:100%;overflow-x:auto;scrollbar-width:none}
.seg::-webkit-scrollbar{display:none}
.seg button{padding:10px 18px;border-radius:999px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);white-space:nowrap;transition:background .2s,color .2s}
.seg button.on{background:var(--btn-bg);color:var(--btn-fg)}
.pills{display:flex;gap:8px;flex-wrap:wrap}
.pill{padding:10px 17px;border-radius:999px;border:1px solid var(--line2);font-size:13px;font-weight:500;color:var(--text);transition:all .2s;white-space:nowrap}
.pill:hover{background:var(--tint)}
.pill.on{background:var(--tint);color:var(--tint-fg);border-color:transparent;font-weight:600}
.search{position:relative;flex:1;min-width:220px}
.search svg{position:absolute;left:18px;top:50%;transform:translateY(-50%);width:16px;height:16px;color:var(--muted)}
.search input{width:100%;height:50px;padding:0 20px 0 46px;border-radius:999px;border:1px solid var(--line2);background:var(--bg2);font-family:var(--mono);font-size:13px;letter-spacing:.03em}
.search input::placeholder{color:var(--muted)}
.select{height:50px;padding:0 42px 0 20px;border-radius:999px;border:1px solid var(--line2);background:var(--bg2) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' fill='none' stroke='%23888' stroke-width='2'%3E%3Cpath d='m1 1 5 5 5-5'/%3E%3C/svg%3E") no-repeat right 18px center;-webkit-appearance:none;appearance:none;font-family:var(--mono);font-size:12px;letter-spacing:.06em}
.badge{display:inline-flex;align-items:center;gap:6px;padding:5px 11px;border-radius:999px;font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;background:rgba(0,0,0,.55);color:#f4f1ea;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.tag{padding:5px 11px;border-radius:999px;background:var(--tint);color:var(--tint-fg);font-size:12px;font-weight:500}

/* =========================================================
   HERO
   ========================================================= */
.hero{position:relative;min-height:100svh;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:clamp(28px,5vw,72px);align-items:center;padding:130px clamp(20px,5vw,72px) 70px;overflow:hidden}
.hero-l{min-width:0}
.hero .kicker{margin-bottom:26px}
.hero h1{font-size:clamp(2.6rem,7vw,6.4rem);max-width:13ch}
.hero .sub{max-width:46ch;margin-top:30px;font-size:clamp(15px,1.4vw,18px);color:var(--muted);position:relative;z-index:2}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px;position:relative;z-index:2}
.hero .fine{margin-top:18px;font-size:13px;color:var(--muted);position:relative;z-index:2}

.wrap{padding:0 clamp(20px,5vw,72px)}
.sec{padding:clamp(64px,9vw,120px) 0}
.sec-h{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:38px}
.sec-h h2{font-size:clamp(2.1rem,5.4vw,4.6rem);max-width:15ch}
.sec-h p{max-width:34ch;color:var(--muted);font-size:15px}
.cats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.ct{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:36px;min-height:230px;padding:22px;border-radius:26px;color:var(--ink);text-align:left;overflow:hidden;transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.ct:hover{transform:translateY(-6px)}
.ct .band{position:absolute;right:0;top:0;width:62%;height:100%;opacity:.55;-webkit-mask-image:linear-gradient(90deg,transparent,#000 60%);mask-image:linear-gradient(90deg,transparent,#000 60%);transition:transform .7s cubic-bezier(.2,.8,.2,1)}
.ct:hover .band{transform:scale(1.08)}
.ct .em{position:relative;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-size:26px;line-height:1;background:color-mix(in srgb,var(--ink) 12%,transparent)}
.ct .tx{position:relative}
.ct h3{font-family:var(--serif);font-weight:400;font-size:clamp(1.6rem,2.3vw,2.2rem);text-transform:uppercase;letter-spacing:-.02em;line-height:1}
.ct p{font-size:13.5px;margin-top:8px;opacity:.82;max-width:24ch}
.ct .n{margin-top:14px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;display:block}
.live{border:1px solid var(--line2);border-radius:30px;background:var(--bg2);padding:14px;position:relative}
.live-h{display:flex;justify-content:space-between;align-items:center;padding:8px 10px 12px}
.live-h .k{display:flex;align-items:center;gap:10px}
.lrow{display:flex;align-items:center;gap:12px;width:100%;padding:10px;border-radius:20px;text-align:left;transition:background .2s}
.lrow:hover{background:var(--tint)}
.lrow .th{width:46px;height:46px;border-radius:14px;overflow:hidden;flex:none;position:relative}
.lrow .th svg{position:absolute;inset:0;width:100%;height:100%}
.lrow b{display:block;font-family:var(--serif);font-weight:400;font-size:1.02rem;text-transform:uppercase;letter-spacing:-.01em;line-height:1.08}
.lrow small{font-size:12px;color:var(--muted)}
.lrow .tm{margin-left:auto;flex:none;padding:6px 11px;border-radius:999px;background:var(--tint);color:var(--tint-fg);font-family:var(--mono);font-size:11.5px;letter-spacing:.04em;white-space:nowrap}
.hsearch{display:flex;gap:8px;margin-top:30px;max-width:520px;padding:6px;border-radius:999px;border:1px solid var(--line2);background:var(--bg2)}
.hsearch input{flex:1;min-width:0;height:46px;padding:0 18px;background:transparent;border:0;font-family:var(--mono);font-size:13px;letter-spacing:.03em}
.hsearch input:focus{outline:none}
.hsearch input::placeholder{color:var(--muted)}

/* tonight chapter */
.chapter{background:var(--pastel);color:var(--ink);position:relative;overflow:hidden;padding:clamp(72px,10vw,140px) clamp(20px,5vw,72px)}
.chapter .kicker{color:color-mix(in srgb,var(--ink) 70%,transparent)}
.bigclock{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;font-family:var(--serif);font-size:clamp(4.4rem,21.5vw,22rem);line-height:1;letter-spacing:-.04em;color:color-mix(in srgb,var(--ink) 13%,transparent);font-variant-numeric:tabular-nums lining-nums;white-space:nowrap;user-select:none;pointer-events:none}
.chapter .in{position:relative;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:end;min-height:min(60vh,520px)}
.chapter h2{font-size:clamp(2rem,5vw,4.2rem);max-width:12ch}
.chapter p{max-width:38ch;font-size:16px;color:color-mix(in srgb,var(--ink) 82%,transparent);margin-bottom:22px}

/* explore */
.ctrl{display:flex;flex-direction:column;gap:16px;margin-bottom:30px}
.ctrl-row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.count-line{display:flex;align-items:center;gap:12px;margin-bottom:20px;color:var(--muted);font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;flex-wrap:wrap}
.count-line button{padding:4px 12px;border-radius:999px;background:var(--tint);color:var(--tint-fg)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:18px}
.card{position:relative;border-radius:26px;background:var(--bg2);border:1px solid var(--line);overflow:hidden;display:flex;flex-direction:column;cursor:pointer;transition:transform .3s cubic-bezier(.2,.8,.2,1),border-color .3s,box-shadow .3s}
.card:hover{transform:translateY(-5px);border-color:var(--line2);box-shadow:var(--shadow)}
.cv{position:relative;aspect-ratio:4/3;overflow:hidden;background:#222}
.cv>svg{position:absolute;inset:0;width:100%;height:100%}
.cv::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.28) 0%,rgba(0,0,0,0) 36%,rgba(0,0,0,.72) 100%)}
.cv .b1{position:absolute;left:14px;top:14px;display:flex;gap:6px;z-index:2;flex-wrap:wrap}
.cv .rate{position:absolute;left:16px;bottom:14px;z-index:2;color:#fff;font-family:var(--mono);font-size:13px;letter-spacing:.04em;display:flex;align-items:center;gap:7px}
.cv .rate small{opacity:.75}
.cv .lock{position:absolute;right:14px;top:14px;z-index:2;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:rgba(0,0,0,.55);color:#fff;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.cv .lock svg{width:15px;height:15px}
.star{width:14px;height:14px;fill:#f0b94a}
.cb{padding:20px 20px 22px;display:flex;flex-direction:column;gap:12px;flex:1}
.cb h3{font-family:var(--serif);font-weight:400;font-size:1.65rem;letter-spacing:-.02em;text-transform:uppercase;line-height:1}
.cb .loc{font-size:13.5px;color:var(--muted);display:flex;justify-content:space-between;gap:8px}
.cb .tags{display:flex;gap:6px;flex-wrap:wrap}
.cb .go{margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:10px;padding-top:6px}
.cb .price{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--muted)}
.cb .price b{color:var(--text);font-size:15px;font-weight:600}
.empty{grid-column:1/-1;text-align:center;padding:70px 20px;border:1px dashed var(--line2);border-radius:26px}
.empty h3{font-family:var(--serif);font-size:2rem;text-transform:uppercase;margin-bottom:10px;font-weight:400}
.empty p{color:var(--muted);margin-bottom:22px}

footer.ft{padding:90px clamp(20px,5vw,72px) 150px;border-top:1px solid var(--line)}
.ft .big{font-family:var(--serif);font-size:clamp(3.4rem,14vw,12rem);letter-spacing:-.04em;line-height:.9;font-weight:400}
.ft .row{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-top:36px;color:var(--muted);font-size:13.5px}

/* =========================================================
   REAL VENUE IMAGERY STYLES (OVER SVG TOTEMS)
   ========================================================= */
.cv img, .vcover img, .th img, .fc img, .th3 img, .lrow .th img, .order .th img, .trow .th img, .hit .th img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  transition: transform .6s cubic-bezier(.2,.8,.2,1);
}
.card:hover .cv img {
  transform: scale(1.08);
}
.cv>svg, .vcover>svg, .th>svg, .fc>svg, .th3>svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

/* =========================================================
   MODAL / SHEET
   ========================================================= */
.ov{position:fixed;inset:0;z-index:100;display:grid;place-items:center;padding:20px;background:rgba(0,0,0,.62);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);animation:fade .25s ease}
.ov.out{animation:fadeout .22s ease forwards}
@keyframes fade{from{opacity:0}}
@keyframes fadeout{to{opacity:0}}
.sheet{position:relative;width:min(1020px,100%);max-height:calc(100dvh - 40px);overflow:auto;overscroll-behavior:contain;background:var(--bg2);color:var(--text);border:1px solid var(--line2);border-radius:32px;box-shadow:var(--shadow);animation:pop .35s cubic-bezier(.2,.8,.2,1);outline:none}
.sheet.sm{width:min(470px,100%)}
.sheet.md{width:min(560px,100%)}
.ov.out .sheet{animation:popout .22s ease forwards}
@keyframes pop{from{opacity:0;transform:translateY(24px) scale(.97)}}
@keyframes popout{to{opacity:0;transform:translateY(16px) scale(.98)}}
.grab{display:none;width:44px;height:5px;border-radius:9px;background:var(--line2);margin:10px auto 0;touch-action:none;position:relative}
.grab::before{content:"";position:absolute;inset:-14px -30px}
.x{position:absolute;right:16px;top:16px;z-index:5;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:rgba(0,0,0,.55);color:#fff;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);font-size:22px;line-height:1}
.x.plain{background:var(--bg3);color:var(--text)}
.vgrid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}
.vgrid>*{min-width:0}
.vleft{border-right:1px solid var(--line)}
.vcover{position:relative;aspect-ratio:16/11;overflow:hidden}
.vcover>svg{position:absolute;inset:0;width:100%;height:100%}
.vcover::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25),rgba(0,0,0,0) 40%,rgba(0,0,0,.6))}
.vcover .b1{position:absolute;left:18px;bottom:16px;z-index:2;display:flex;gap:6px;flex-wrap:wrap}
.vinfo{padding:26px 28px 32px;display:flex;flex-direction:column;gap:14px}
.vinfo h2{font-family:var(--serif);font-weight:400;font-size:clamp(1.9rem,3.4vw,2.8rem);text-transform:uppercase;letter-spacing:-.02em;line-height:.98}
.meta{display:flex;gap:14px;flex-wrap:wrap;align-items:center;color:var(--muted);font-size:14px}
.meta .r{display:flex;align-items:center;gap:6px;color:var(--text);font-weight:600}
.vinfo p{color:var(--muted);font-size:15px;max-width:52ch}
.vright{padding:28px;display:flex;flex-direction:column;gap:18px}
.vright h4{margin:0;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:500}
.days{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}
.days::-webkit-scrollbar{display:none}
.day{flex:0 0 auto;min-width:74px;padding:10px 12px;border-radius:18px;border:1px solid var(--line2);text-align:center;transition:all .2s}
.day b{display:block;font-family:var(--serif);font-weight:400;font-size:22px;line-height:1.1}
.day span{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.day.on{background:var(--btn-bg);color:var(--btn-fg);border-color:transparent}
.day.on span{color:inherit;opacity:.8}
.slots{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:8px}
.slot{padding:12px 8px 11px;border-radius:16px;border:1px solid var(--line2);display:flex;flex-direction:column;align-items:center;gap:2px;transition:all .18s;position:relative}
.slot .t{font-family:var(--mono);font-size:13px;letter-spacing:.02em;font-weight:500}
.slot .p{font-size:12px;color:var(--muted)}
.slot .f{position:absolute;top:-8px;right:8px;font-size:9.5px;font-family:var(--mono);letter-spacing:.08em;text-transform:uppercase;background:var(--warn);color:#fff;padding:2px 7px;border-radius:99px}
.slot:not(:disabled):hover{border-color:var(--text)}
.slot.on{background:var(--btn-bg);color:var(--btn-fg);border-color:transparent}
.slot.on .p{color:inherit;opacity:.8}
.slot:disabled{opacity:.4;cursor:not-allowed;text-decoration:line-through;text-decoration-thickness:1px}
.slot.yours:disabled{text-decoration:none;opacity:.7;background:var(--tint);border-color:transparent}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--muted)}
.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:middle}
.bookbar{margin-top:auto;position:sticky;bottom:0;background:var(--bg2);padding:14px 0 2px;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:14px}
.bookbar .sum{font-size:13px;color:var(--muted);line-height:1.35}
.bookbar .sum b{display:block;color:var(--text);font-size:19px;font-weight:600;font-family:var(--sans)}

/* forms */
.pad{padding:34px 32px 32px}
.pad h2{font-family:var(--serif);font-weight:400;font-size:2.3rem;text-transform:uppercase;letter-spacing:-.02em;line-height:.98;margin:8px 0 10px}
.pad .lead{color:var(--muted);font-size:14.5px;margin-bottom:20px}
.tabs{display:flex;padding:4px;border-radius:999px;background:var(--bg3);margin-bottom:20px}
.tabs button{flex:1;padding:10px;border-radius:999px;font-size:13.5px;font-weight:600;color:var(--muted);transition:all .2s}
.tabs button.on{background:var(--btn-bg);color:var(--btn-fg)}
.f{display:flex;flex-direction:column;gap:6px;margin-bottom:14px;flex:1;min-width:0}
.f label{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.f input{height:50px;padding:0 16px;border-radius:16px;border:1px solid var(--line2);background:var(--bg);font-size:15px;width:100%;transition:border-color .2s}
.f input:focus{outline:none;border-color:var(--text)}
.frow{display:flex;gap:12px}
.err{color:var(--bad);font-size:13.5px;margin:-2px 0 12px;min-height:0}
.linkbtn{display:block;margin:14px auto 0;font-size:13.5px;color:var(--muted);text-decoration:underline;text-underline-offset:3px}
.testnote{display:flex;gap:10px;padding:12px 14px;border-radius:16px;background:var(--tint);color:var(--tint-fg);font-size:12.5px;line-height:1.45;margin-bottom:16px}
.order{display:flex;gap:14px;padding:14px;border-radius:20px;border:1px solid var(--line);margin-bottom:16px;align-items:center}
.order .th{width:64px;height:64px;border-radius:14px;overflow:hidden;flex:none;position:relative}
.order .th svg{position:absolute;inset:0;width:100%;height:100%}
.order b{font-family:var(--serif);font-weight:400;font-size:1.15rem;text-transform:uppercase;letter-spacing:-.01em;display:block;line-height:1.1}
.order span{font-size:13px;color:var(--muted)}
.lines{font-size:14px;margin-bottom:18px}
.lines div{display:flex;justify-content:space-between;padding:6px 0;color:var(--muted)}
.lines div.tot{color:var(--text);font-weight:700;font-size:16px;border-top:1px solid var(--line);margin-top:6px;padding-top:12px}
.stripe-tag{display:flex;align-items:center;justify-content:center;gap:8px;font-size:12px;color:var(--muted);margin-top:14px}

/* ticket */
.done{padding:34px 28px 30px;text-align:center}
.done .kicker{color:var(--ok)}
.done h2{font-family:var(--serif);font-weight:400;font-size:2.4rem;text-transform:uppercase;letter-spacing:-.02em;line-height:.98;margin:8px 0 22px}
.tk{position:relative;max-width:340px;margin:0 auto 24px;border-radius:22px;background:var(--pastel);color:var(--ink);text-align:left;transform-origin:50% 0;animation:tick .8s cubic-bezier(.2,.9,.25,1.15) both;filter:drop-shadow(0 20px 30px rgba(0,0,0,.28))}
@keyframes tick{0%{opacity:0;transform:translateY(-40px) rotate(-6deg) scale(.9)}60%{opacity:1;transform:translateY(6px) rotate(1.5deg) scale(1.01)}100%{transform:none}}
.tk .top{padding:20px 22px 16px;position:relative}
.tk .top .kicker{color:color-mix(in srgb,var(--ink) 70%,transparent)}
.tk h3{padding-right:62px;font-family:var(--serif);font-weight:400;font-size:1.7rem;text-transform:uppercase;letter-spacing:-.02em;line-height:1;margin:6px 0 12px}
.tk .row{display:flex;justify-content:space-between;gap:10px;font-size:13.5px}
.tk .row b{font-weight:600}
.tk .perf{height:0;border-top:2px dashed color-mix(in srgb,var(--ink) 35%,transparent);margin:0 14px;position:relative}
.tk .perf::before,.tk .perf::after{content:"";position:absolute;top:-12px;width:22px;height:22px;border-radius:50%;background:var(--bg2)}
.tk .perf::before{left:-25px}.tk .perf::after{right:-25px}
.tk .bot{padding:16px 22px 20px;display:flex;justify-content:space-between;align-items:center;gap:14px}
.tk .ref{font-family:var(--mono);font-size:19px;letter-spacing:.14em;font-weight:600}
.tk .bot small{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;opacity:.7;display:block}
.stamp{position:absolute;right:16px;top:14px;width:58px;height:58px;border-radius:50%;background:var(--ink);color:var(--pastel);display:grid;place-items:center;animation:stamp .5s .55s cubic-bezier(.2,1.6,.4,1) both}
@keyframes stamp{from{opacity:0;transform:scale(2.4) rotate(-30deg)}to{opacity:1;transform:rotate(-10deg)}}
.stamp svg{width:28px;height:28px}

/* =========================================================
   CHAT
   ========================================================= */
.chat{max-width:860px;margin:0 auto;padding:118px 20px 220px}
.chat-h{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:26px}
.chat-h h1{font-size:clamp(2.4rem,6vw,4.6rem)}
.chips{display:flex;gap:8px;overflow-x:auto;padding:2px 0 6px;scrollbar-width:none;margin-bottom:28px}
.chips::-webkit-scrollbar{display:none}
.chips button{flex:none;padding:10px 16px;border-radius:999px;border:1px solid var(--line2);font-size:13.5px;transition:all .2s;white-space:nowrap}
.chips button:hover{background:var(--tint);color:var(--tint-fg);border-color:transparent}
.stream{display:flex;flex-direction:column;gap:22px}
.msg{max-width:100%;animation:rise .35s ease both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}}
.msg.u{align-self:flex-end;max-width:82%;padding:12px 20px;border-radius:999px;background:var(--btn-bg);color:var(--btn-fg);font-size:15px}
.msg.a{display:flex;gap:14px;align-items:flex-start}
.msg.a .av{flex:none;width:34px;height:34px;border-radius:50%;background:var(--pastel);color:var(--ink);display:grid;place-items:center;font-family:var(--serif);font-size:18px;font-weight:500;margin-top:2px}
.msg.a .bd{flex:1;min-width:0}
.msg.a .tx{font-size:16px;line-height:1.6}
.msg.a .tx strong{font-weight:700}
.typing{display:inline-flex;gap:5px;padding:12px 0}
.typing i{width:7px;height:7px;border-radius:50%;background:var(--muted);animation:blink 1.1s infinite}
.typing i:nth-child(2){animation-delay:.15s}.typing i:nth-child(3){animation-delay:.3s}
@keyframes blink{0%,80%,100%{opacity:.25;transform:none}40%{opacity:1;transform:translateY(-3px)}}
.hits{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin-top:14px}
.hit{display:flex;gap:12px;align-items:center;padding:10px;border-radius:20px;border:1px solid var(--line);background:var(--bg2);text-align:left;transition:border-color .2s,transform .2s}
.hit:hover{border-color:var(--line2);transform:translateY(-2px)}
.hit .th{width:52px;height:52px;border-radius:14px;overflow:hidden;flex:none;position:relative}
.hit .th svg{position:absolute;inset:0;width:100%;height:100%}
.hit b{display:block;font-family:var(--serif);font-weight:400;font-size:1.02rem;text-transform:uppercase;letter-spacing:-.01em;line-height:1.05}
.hit span{font-size:12px;color:var(--muted)}
.tool{margin-top:14px;padding:14px 16px;border-radius:20px;border:1px solid var(--line2);background:var(--bg2);display:flex;gap:14px;align-items:center;flex-wrap:wrap;justify-content:space-between}
.tool .fn{font-family:var(--mono);font-size:12px;letter-spacing:.04em;display:flex;align-items:center;gap:9px}
.tool .fn em{font-style:normal;padding:3px 9px;border-radius:99px;background:var(--tint);color:var(--tint-fg);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase}
.tool .ref{font-family:var(--mono);font-size:13px;letter-spacing:.14em;font-weight:600}
details.trace{margin-top:12px;border:1px solid var(--line);border-radius:20px;background:var(--bg2);overflow:hidden}
details.trace summary{cursor:pointer;padding:12px 18px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);list-style:none;display:flex;justify-content:space-between}
details.trace summary::-webkit-details-marker{display:none}
details.trace summary::after{content:"+";font-size:16px;line-height:1}
details.trace[open] summary::after{content:"–"}
.trace .in{padding:2px 18px 18px;display:flex;flex-direction:column;gap:14px;font-size:13px}
.trace .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.trace code,.trace pre{font-family:var(--mono);font-size:12px;background:var(--bg3);padding:10px 12px;border-radius:12px;display:block;white-space:pre-wrap;word-break:break-word;margin:0}
.trace table{width:100%;border-collapse:collapse;font-size:12.5px}
.trace td{padding:7px 0;border-bottom:1px solid var(--line)}
.trace td:first-child{font-family:var(--mono);color:var(--gold);width:64px}
.trace td:last-child{text-align:right;color:var(--muted)}
.trace .note{color:var(--muted);font-size:12px}
.inbar{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(22px + env(safe-area-inset-bottom,0px));z-index:58;width:min(860px,calc(100% - 24px))}
.inbar form{display:flex;gap:8px;padding:7px;border-radius:999px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line2);box-shadow:0 14px 44px rgba(0,0,0,.3)}
.inbar input{flex:1;min-width:0;height:48px;padding:0 20px;background:transparent;border:0;font-size:15px}
.inbar input:focus{outline:none}
.inbar input::placeholder{color:var(--muted)}

/* bookings */
.pp{max-width:1000px;margin:0 auto;padding:130px 20px 160px}
.pp h1{font-size:clamp(2.4rem,7vw,5.4rem);margin:12px 0 34px}
.tlist{display:flex;flex-direction:column;gap:10px}
.trow{display:flex;gap:16px;align-items:center;padding:14px;border-radius:22px;border:1px solid var(--line);background:var(--bg2);text-align:left;width:100%;transition:border-color .2s}
.trow:hover{border-color:var(--line2)}
.trow .th{width:60px;height:60px;border-radius:16px;overflow:hidden;flex:none;position:relative}
.trow .th svg{position:absolute;inset:0;width:100%;height:100%}
.trow b{font-family:var(--serif);font-weight:400;font-size:1.25rem;text-transform:uppercase;letter-spacing:-.01em;display:block;line-height:1.05}
.trow span{font-size:13px;color:var(--muted)}
.trow .rf{margin-left:auto;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-align:right}
#toast{position:fixed;left:50%;bottom:calc(92px + env(safe-area-inset-bottom,0px));transform:translate(-50%,14px);z-index:200;padding:12px 20px;border-radius:999px;background:var(--btn-bg);color:var(--btn-fg);font-size:14px;font-weight:600;opacity:0;pointer-events:none;transition:all .3s}
#toast.show{opacity:1;transform:translate(-50%,0)}


.palmenu{position:fixed;top:calc(70px + env(safe-area-inset-top,0px));left:50%;transform:translateX(-50%);z-index:70;display:none;flex-direction:column;gap:4px;padding:8px;border-radius:26px;background:var(--glass);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line2);box-shadow:0 20px 60px rgba(0,0,0,.4);width:min(280px,calc(100% - 24px))}
.palmenu.open{display:flex;animation:pop .25s cubic-bezier(.2,.8,.2,1)}
.palmenu .kicker{padding:8px 12px 6px}
.palmenu button{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:18px;text-align:left;transition:background .2s}
.palmenu button:hover{background:var(--tint)}
.palmenu button.on{background:var(--tint);box-shadow:inset 0 0 0 1px var(--line2)}
.palmenu b{font-weight:600;font-size:14px;display:block;line-height:1.2}
.palmenu small{color:var(--muted);font-size:12px}
.sw{display:flex;flex:none}
.sw i{width:18px;height:18px;border-radius:50%;margin-left:-6px;border:2px solid var(--bg2)}
.sw i:first-child{margin-left:0}

/* =========================================================
   RESPONSIVE
   ========================================================= */
@media (max-width:1023px){
  .cats{grid-template-columns:repeat(2,1fr)}
  .hero{grid-template-columns:minmax(0,1fr)}
  .chapter .in{grid-template-columns:1fr}
  .nav a{padding:9px 11px}
  .brand span{display:none}
}
@media (max-width:767px){
  .hdr{top:calc(10px + env(safe-area-inset-top,0px));padding:6px 6px 6px 18px;width:calc(100% - 20px);justify-content:space-between}
  .nav,.hdr .sep,.floatcta{display:none}
  .brand{margin:0}
  .brand span{display:inline}
  .bnav{display:flex}
  .hero{min-height:auto;padding:112px 20px 50px;gap:34px}
  .hero h1{font-size:clamp(2.5rem,13.6vw,4rem)}
  .cats{gap:10px}
  .ct{min-height:170px;padding:16px;border-radius:22px;gap:22px}
  .ct .em{width:42px;height:42px;font-size:21px}
  .ct p{font-size:12.5px}
  .sec-h{margin-bottom:26px}
  .search{min-width:100%}
  .ctrl-row .select{flex:1}
  .card{border-radius:24px}
  footer.ft{padding-bottom:140px}
  .ov{place-items:end center;padding:0}
  .sheet,.sheet.sm,.sheet.md{width:100%;max-height:93dvh;border-radius:30px 30px 0 0;animation:slideup .4s cubic-bezier(.2,.85,.25,1)}
  .ov.out .sheet{animation:slidedown .25s ease forwards}
  @keyframes slideup{from{transform:translateY(100%)}}
  @keyframes slidedown{to{transform:translateY(100%)}}
  .grab{display:block}
  .vgrid{grid-template-columns:minmax(0,1fr)}
  .vleft{border-right:0}
  .vcover{aspect-ratio:16/8}
  .vinfo{padding:20px 20px 12px}
  .vright{padding:8px 20px 20px}
  .bookbar{padding-bottom:calc(6px + env(safe-area-inset-bottom,0px))}
  .pad{padding:18px 22px 28px}
  .pad h2{font-size:2rem}
  .x{top:22px;right:14px}
  .chat{padding:88px 14px 250px}
  .inbar{bottom:calc(84px + env(safe-area-inset-bottom,0px))}
  .msg.u{max-width:90%}
  .pp{padding:96px 16px 150px}
  .trow .rf{display:none}
  .bigclock{font-size:clamp(3.4rem,20vw,7rem)}
}
@media (max-width:420px){
  .brand span{display:none!important}
  .frow{flex-direction:column;gap:0}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
.fav{position:absolute;right:14px;bottom:12px;z-index:3;width:38px;height:38px;border-radius:50%;background:rgba(0,0,0,.55);color:#fff;font-size:18px;display:grid;place-items:center;transition:transform .2s,color .2s}.fav:hover{transform:scale(1.12)}.fav.on{color:#ff6b81}
.crew{text-align:left;max-width:340px;margin:0 auto 22px;padding:16px;border:1px solid var(--line);border-radius:20px}.crewrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:8px;font-size:13px;color:var(--muted)}.crewrow b{color:var(--text)}.pill:disabled{opacity:.4;cursor:not-allowed}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.stat{padding:16px;border-radius:20px;border:1px solid var(--line);background:var(--bg2)}.stat b{display:block;font-family:var(--serif);font-size:1.7rem;font-weight:400}.stat span{font-size:12px;color:var(--muted)}@media(max-width:600px){.stats{grid-template-columns:repeat(2,1fr)}}
.lab,.lab2{position:absolute;top:22px;left:clamp(20px,5vw,72px);right:clamp(20px,5vw,72px);display:flex;justify-content:space-between;font-size:13px;font-weight:600;z-index:3}
.lab2{position:static;margin-bottom:26px;color:var(--muted)}
.hero .lab{top:calc(84px + env(safe-area-inset-top,0px));color:var(--muted)}
.hero{background:#000;color:#fff}.hero .sub,.hero .fine{color:#b9b3cc}
.mega{font-size:clamp(3rem,9.4vw,9rem);max-width:none;line-height:.92}
.hero-l,.live{position:relative;z-index:2}
.floaters{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.fl{position:absolute;transform:translate(var(--px,0),var(--py,0)) rotate(var(--r));animation:drift 8s ease-in-out infinite alternate;transition:transform .5s ease-out}
@keyframes drift{to{margin-top:-24px}}
.fc{position:relative;aspect-ratio:3/4;border-radius:14px;overflow:hidden;box-shadow:0 18px 50px rgba(124,58,237,.35);border:1px solid rgba(255,255,255,.14)}
.fc svg{position:absolute;inset:0;width:100%;height:100%}
.fc b{position:absolute;left:8px;right:8px;bottom:8px;font-size:11px;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.7);z-index:2}
.story{position:relative;padding:clamp(100px,13vw,180px) clamp(20px,5vw,72px)}
.story.dark{background:#000;color:#fff}.story.light{background:#f6f4fb;color:#0a0612}
.stag{font-size:clamp(2.2rem,6.4vw,5.8rem);max-width:none}.stag span{display:block}.stag span:nth-child(2){margin-left:16%}.stag span:nth-child(3){margin-left:30%}
.sp{max-width:44ch;margin:52px 0 0 30%;color:#b9b3cc;font-size:16px}
.story.light h2{font-size:clamp(2rem,5.4vw,4.8rem);max-width:18ch}
.rows{margin-top:60px}.row3{display:grid;grid-template-columns:1.2fr .7fr 1fr;gap:28px;align-items:center;padding:28px 0;border-top:1px solid rgba(10,6,18,.16)}
.row3 small{display:block;color:#6b6480;font-size:13px}.row3 b{font-size:1.25rem;display:block;margin-top:4px}.row3 i{display:block;margin-top:38px;font-style:normal;color:#6b6480;font-size:13px}.row3 p{color:#4d4763;font-size:15px}
.th3{aspect-ratio:4/3;border-radius:8px;overflow:hidden;position:relative;max-width:230px}.th3 svg{position:absolute;inset:0;width:100%;height:100%}
.fin{text-align:center;display:flex;flex-direction:column;align-items:center;gap:22px;min-height:70vh;justify-content:center}.fin h2{font-size:clamp(2.6rem,8vw,7.4rem)}.fin p{color:#b9b3cc}
.chapter .lab{color:var(--ink)}
.rv{opacity:0;transform:translateY(46px);transition:opacity .9s cubic-bezier(.2,.8,.2,1),transform .9s cubic-bezier(.2,.8,.2,1)}.rv.in{opacity:1;transform:none}.stag .rv:nth-child(2){transition-delay:.12s}.stag .rv:nth-child(3){transition-delay:.24s}
#loader{position:fixed;inset:0;z-index:400;background:var(--pastel);display:grid;place-items:center;transition:opacity .5s}#loader.off{opacity:0;pointer-events:none}.lc{display:grid;gap:12px;justify-items:center;font-family:var(--serif);color:#0a0612;letter-spacing:.08em;font-size:14px}
@media(max-width:767px){.fl:nth-child(n+4){display:none}.stag span:nth-child(n){margin-left:0}.sp{margin-left:0}.row3{grid-template-columns:1fr}.hero .lab{top:78px}.fl{opacity:.28}}
</style>
</head>
<body>

<header class="hdr" id="hdr">
  <a class="brand" href="#/" aria-label="hoppin. home"><b>hoppin.</b><span>· 67 venues</span></a>
  <nav class="nav" id="nav" aria-label="Primary"></nav>
  <i class="sep"></i>
  <button class="icon-btn" id="themeBtn" data-act="theme" aria-label="Toggle light or dark theme"></button>
  <button class="icon-btn" id="palBtn" data-act="palmenu" aria-label="Choose colour palette" aria-haspopup="true"></button>
  <button class="acct" id="acct" data-act="account">Sign in</button>
</header>
<div class="palmenu" id="palmenu" role="menu"></div>

<main id="app"></main>

<nav class="bnav" id="bnav" aria-label="Primary mobile"></nav>
<a class="floatcta" id="floatcta" href="#/chat"><span class="dot"></span>AI Concierge · Ask about 67 venues ↗</a>
<div id="toast" role="status" aria-live="polite"></div>

<script>
(()=>{'use strict';
/* =========================================================
   UTILITIES
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
const API_URL='http://localhost:4000/api';
async function api(path,method='GET',body=null){
  try{
    const res=await fetch(API_URL+path,{
      method,
      headers:{'Content-Type':'application/json'},
      body:body?JSON.stringify(body):undefined
    });
    if(res.ok)return await res.json();
    const err=await res.json().catch(()=>({}));
    return {_err:err.error||'Server error'};
  }catch(e){return null;}
}

/* icons */
const IC={
  sun:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  moon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4 8.5 8.5 0 1 0 20 14.5Z"/></svg>',
  lock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
  search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  star:'<svg class="star" viewBox="0 0 24 24"><path d="m12 2 3 6.6 7.2.7-5.4 4.8 1.6 7.1L12 17.4 5.6 21.2l1.6-7.1L1.8 9.3 9 8.6z"/></svg>',
  explore:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
  sports:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3.5 9c5 1 12 1 17 0M3.5 15c5-1 12-1 17 0M12 3c-3 4-3 14 0 18"/></svg>',
  dining:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3v7a2 2 0 0 0 2 2v9M10 3v7a2 2 0 0 1-2 2M6 3v0M18 21V3c-2.5 1.5-3.5 4.5-3.5 8H18"/></svg>',
  gaming:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><circle cx="8.5" cy="8.5" r="1" fill="currentColor"/><circle cx="15.5" cy="8.5" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/><circle cx="8.5" cy="15.5" r="1" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1" fill="currentColor"/></svg>',
  chat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 12a8.5 8.5 0 0 1-12.4 7.5L3.5 20.5l1.1-4.2A8.5 8.5 0 1 1 20.5 12Z"/></svg>',
  check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
  card:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="M2.5 10h19"/></svg>',
  info:'<svg width="18" height="18" style="flex:none;margin-top:1px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.01"/></svg>'
};

/* =========================================================
   DATA — 67 venues (Bengaluru 29 · Chennai 38)
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
  sports:{sub:'Courts & floodlit turfs',emoji:'🏸',kind:'check',c:'#7fe7ff',c2:'#3fc4e8'},
  fitness:{sub:'Gyms, CrossFit & studios',emoji:'🏋️',kind:'wave',c:'#ffb877',c2:'#f28f3d'},
  pubs:{sub:'Taprooms, brewpubs & bars',emoji:'🍻',kind:'stripe',c:'#c9a6ff',c2:'#a274f5'},
  dining:{sub:'Cafes, wine bars & dinner',emoji:'🍽️',kind:'dots',c:'#ffd66b',c2:'#eeb01c'},
  gaming:{sub:'Board game cafes & VR arenas',emoji:'🎲',kind:'diamond',c:'#93aaff',c2:'#6484f2'},
  clubs:{sub:'Run clubs, yoga & cycling',emoji:'🏃',kind:'chev',c:'#8ff0c0',c2:'#4fd69a'}
};
const AREA={
  'Indiranagar':[12.9784,77.6408],'Koramangala':[12.9352,77.6245],'Whitefield':[12.9698,77.7500],'Central Bengaluru':[12.9716,77.5946],'Bengaluru':[12.9716,77.5946],'Cubbon Park':[12.9763,77.5929],'Bidadi':[12.8330,77.4030],
  'Kilpauk':[13.0836,80.2420],'T. Nagar':[13.0418,80.2341],'Velachery':[12.9815,80.2180],'Vanagaram':[13.0500,80.1500],'Thiruvanmiyur':[12.9830,80.2594],'Puzhuthivakkam':[12.9700,80.1900],'Chromepet':[12.9516,80.1462],'Anna Nagar':[13.0850,80.2101],'OMR':[12.9000,80.2270],'Perungudi':[12.9650,80.2461],'Adyar':[13.0012,80.2565],'Alwarpet':[13.0339,80.2510],'Egmore':[13.0732,80.2609],'Porur':[13.0382,80.1565],'Mylapore':[13.0368,80.2676],'Besant Nagar':[13.0002,80.2707],'Nungambakkam':[13.0569,80.2425],'Periamet':[13.0827,80.2707],'Guindy':[13.0067,80.2206],'Chennai':[13.0827,80.2707],'Elliot\'s Beach':[13.0002,80.2707],'Velachery Mall':[12.9807,80.2185]
};
const RAW=[
 // ---- Bengaluru (29)
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
 // ---- Chennai (38)
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
 ['Chennai Runners (Bessie Flyers)','MAA',"Elliot's Beach",'clubs',['Running','5:15 AM','Beachfront'],'Bessie Flyers meet at 5:15 AM on Elliot\'s Beach. Show up, run together, get breakfast after.',{slots:['05:15 AM']}],
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

/* =========================================================
   DATES, SLOTS, AVAILABILITY
   ========================================================= */
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
function pickSlot(v,o={}){
  let days=validDays(v,14);
  if(o.date==='today')days=days.filter(d=>d===todayISO());
  else if(o.date==='tomorrow'){const t=new Date();t.setDate(t.getDate()+1);days=days.filter(d=>d===toISO(t));}
  else if(typeof o.wd==='number')days=days.filter(d=>fromISO(d).getDay()===o.wd);
  for(const iso of days){
    let c=v.slots.filter(s=>isOpenState(avail(v,iso,s).state));
    if(o.window==='am')c=c.filter(s=>toMin(s)<12*60);
    if(o.window==='pm')c=c.filter(s=>toMin(s)>=17*60);
    if(!c.length)continue;
    if(typeof o.minute==='number')c.sort((a,b)=>Math.abs(toMin(a)-o.minute)-Math.abs(toMin(b)-o.minute));
    return {iso,slot:c[0]};
  }
  return null;
}
function newRef(){const a='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';let s='HP-';for(let i=0;i<6;i++)s+=a[Math.floor(Math.random()*a.length)];return s;}

/* =========================================================
   CURATED HIGH-DEFINITION VENUE IMAGERY
   ========================================================= */
const VENUE_IMG = {
  // Specific Bengaluru Venues
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
  'YUKI Pan-Asian': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=900&q=80',
  'Colosseum E-Sports': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
  'IONA VR Simulators': 'https://images.unsplash.com/photo-1592478411213-6153e4ebc07d?auto=format&fit=crop&w=900&q=80',
  'Fun City': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80',
  'WonderLa Arcade': 'https://images.unsplash.com/photo-1612287232230-65c27f3f269a?auto=format&fit=crop&w=900&q=80',
  'Cubbon Park Yoga Flow Meetup': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=900&q=80',
  'The Amateur League (TAL)': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=900&q=80',

  // Specific Chennai Venues
  'Tiki Taka Football Academy & Turf · Kilpauk': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Tiki Taka Football Academy & Turf · T. Nagar': 'https://images.unsplash.com/photo-1529900748604-07564a03e7a6?auto=format&fit=crop&w=900&q=80',
  'Tiki Taka Football Academy & Turf · Velachery': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'FC Marina Turf & Football Academy · Vanagaram': 'https://images.unsplash.com/photo-1551958219-acbc608c6377?auto=format&fit=crop&w=900&q=80',
  'FC Marina Turf & Football Academy · Thiruvanmiyur': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Spark Football Academy': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=900&q=80',
  'Playpro7 Sport Turf': 'https://images.unsplash.com/photo-1529900748604-07564a03e7a6?auto=format&fit=crop&w=900&q=80',
  'El Clasico Football Turf': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80',
  'Estilio Sports Academy': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=900&q=80',
  'Dugout Indoor Arena · OMR': 'https://images.unsplash.com/photo-1531415074868-036b107e775a?auto=format&fit=crop&w=900&q=80',
  'Dugout Indoor Arena · Velachery Mall': 'https://images.unsplash.com/photo-1531415074868-036b107e775a?auto=format&fit=crop&w=900&q=80',
  'Plug N Play by Munchow': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=900&q=80',
  'SDAT Tennis Stadium': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=900&q=80',
  'Nehru Indoor Stadium': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=900&q=80',
  'Cult Adyar': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80',
  'Cult Alwarpet': 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=900&q=80',
  'Cult T. Nagar': 'https://images.unsplash.com/photo-1574680096145-d05b474e2155?auto=format&fit=crop&w=900&q=80',
  "Women's Gym · Adyar": 'https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=900&q=80',
  'The Madras Taproom': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=900&q=80',
  "Watson's": 'https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=900&q=80',
  'Shout Bar & Cafe': 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=900&q=80',
  'Slounge (Lemon Tree Shimona)': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=900&q=80',
  'The Alwarpet Taproom': 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=900&q=80',
  'Atte · Glocal Cafe': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=900&q=80',
  'The Old Potion House': 'https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=900&q=80',
  'Zha Cafe': 'https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=900&q=80',
  'Untangle House of Puzzles': 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=900&q=80',
  'Gameistry': 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=900&q=80',
  'The Board Room': 'https://images.unsplash.com/photo-1580234811497-9df7fd2f357e?auto=format&fit=crop&w=900&q=80',
  'The Board Game Lounge': 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=900&q=80',
  'GameOn Cafe': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80',
  'Gamesync': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
  'Chennai Runners (Bessie Flyers)': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=900&q=80',
  'CORSO Run Club': 'https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=900&q=80',
  'Dream Runners': 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=900&q=80',
  'VAMOS Run Club': 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=900&q=80',
  'Ciclo Cafe Community': 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=900&q=80',
  'WCCG Cycling Group': 'https://images.unsplash.com/photo-1541625602330-2277a4c46182?auto=format&fit=crop&w=900&q=80'
};

function coverImgURL(v) {
  if (VENUE_IMG[v.name]) return VENUE_IMG[v.name];
  // Tag-based fallbacks
  if (v.tags.includes('Badminton') || v.tags.includes('Racquets')) return 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Football') || v.tags.includes('Turf')) return 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Tennis')) return 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Sauna') || v.tags.includes('Luxury')) return 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('CrossFit')) return 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Board games') || v.tags.includes('1,300+ board games')) return 'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('VR') || v.tags.includes('E-sports')) return 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Yoga')) return 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Running')) return 'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Cycling')) return 'https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Craft beer') || v.tags.includes('Brewpub')) return 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Cocktails') || v.tags.includes('Gastrobar')) return 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=900&q=80';
  if (v.tags.includes('Beachside') || v.tags.includes('Cafe')) return 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=900&q=80';
  if (v.cat === 'fitness') return 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80';
  if (v.cat === 'dining') return 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=900&q=80';
  if (v.cat === 'pubs') return 'https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=900&q=80';
  if (v.cat === 'gaming') return 'https://images.unsplash.com/photo-1580234811497-9df7fd2f357e?auto=format&fit=crop&w=900&q=80';
  if (v.cat === 'clubs') return 'https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=900&q=80';
  return 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=900&q=80';
}

function coverMedia(v){
  const url = coverImgURL(v);
  return `<img src="${url}" alt="${esc(v.name)}" loading="lazy" onerror="this.style.display='none'">${coverSVG(v)}`;
}

/* =========================================================
   TOTEM ART — heraldic shields (Grail-style), generated per venue
   ========================================================= */
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
function totem(kind,a,b,center,size,rot){
  const id='p'+(++uid);const ink=INK;
  return `<svg viewBox="0 0 100 112" width="${size||100}" style="transform:rotate(${rot||0}deg)" aria-hidden="true"><defs>${pat(kind,id,a,b)}</defs><path d="${SHIELD}" fill="url(#${id})" stroke="${ink}" stroke-width="3" stroke-linejoin="round"/><circle cx="50" cy="52" r="24" fill="${a}" stroke="${ink}" stroke-width="3"/>${center}</svg>`;
}
const initials=n=>{const w=n.replace(/[^A-Za-z0-9' &]/g,' ').split(/\s+/).filter(x=>x&&!/^(the|&|of|by)$/i.test(x));return ((w[0]||'H')[0]+(w[1]?w[1][0]:'')).toUpperCase();};
const coverCache={};
function coverSVG(v){
  if(coverCache[v.id])return coverCache[v.id];
  const P=CATCOL[v.cat];const R=rng(hashStr(v.id+v.name));const id='c'+(++uid);const id2='d'+(++uid);
  const k1=KINDS[Math.floor(R()*KINDS.length)];const k2=KINDS[Math.floor(R()*KINDS.length)];
  const ink=INK;const rot=Math.round((R()-.5)*22);const sx=170+Math.round(R()*70);const sy=120+Math.round(R()*30);
  const bx=R()>.5?-40:260, by=Math.round(R()*90)+10;
  const svg=`<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>${pat(k1,id,P.c,P.c2)}${pat(k2,id2,P.c2,P.c)}</defs><rect width="400" height="300" fill="${P.c}"/><circle cx="${bx+100}" cy="${by+100}" r="140" fill="url(#${id})" opacity=".9"/><rect x="0" y="${R()>.5?0:210}" width="400" height="90" fill="url(#${id2})" opacity=".55"/><g transform="translate(${sx} ${sy}) rotate(${rot}) scale(1.55) translate(-50 -56)"><path d="${SHIELD}" fill="${P.c}" stroke="${ink}" stroke-width="2.4" stroke-linejoin="round"/><path d="${SHIELD}" fill="url(#${id2})" opacity=".85" transform="translate(50 56) scale(.86) translate(-50 -56)"/><circle cx="50" cy="52" r="26" fill="#f7f4ec" stroke="${ink}" stroke-width="2.4"/><text x="50" y="62" text-anchor="middle" font-family="Bodoni Moda,Didot,Georgia,serif" font-size="30" fill="${ink}">${initials(v.name)}</text></g></svg>`;
  return coverCache[v.id]=svg;
}

/* =========================================================
   STATE
   ========================================================= */
const S={user:null,city:'all',cat:'all',q:'',sort:'rating',tonight:false,view:'discover',chatCity:'BLR',chat:[],lastHits:[],pending:null,maxp:0,minr:0,geo:null};

/* =========================================================
   PALETTES — futuristic options, switchable live
   ========================================================= */
let INK='#0a0f2c';
const PAL={
 violet:{name:'Violet',note:'Black, white & violet',ink:'#0a0612',pastel:'#c4b5fd',
  cat:{sports:['#a78bfa','#7c3aed'],fitness:['#ffffff','#ddd6fe'],pubs:['#c4b5fd','#8b5cf6'],dining:['#ede9fe','#c4b5fd'],gaming:['#8b5cf6','#6d28d9'],clubs:['#f5f3ff','#a78bfa']},
  dark:{bg:'#000000',bg2:'#0c0a12',bg3:'#171325',text:'#ffffff',muted:'#a49fb8',line:'rgba(255,255,255,.1)',line2:'rgba(196,181,253,.24)',glass:'rgba(12,10,18,.78)',btn:'#7c3aed',btnfg:'#ffffff',tint:'rgba(139,92,246,.2)',tintfg:'#c4b5fd'},
  light:{bg:'#faf9ff',bg2:'#ffffff',bg3:'#efeaff',text:'#0a0612',muted:'#5f5a75',line:'rgba(10,6,18,.1)',line2:'rgba(10,6,18,.2)',glass:'rgba(250,249,255,.84)',btn:'#0a0612',btnfg:'#ffffff',tint:'#ede9fe',tintfg:'#5b21b6'}},
 ion:{name:'Ion',note:'Electric blue, cyan & violet',ink:'#0a0f2c',pastel:'#b9c8ff',
  cat:{sports:['#7fe7ff','#3fc4e8'],fitness:['#ffb877','#f28f3d'],pubs:['#c9a6ff','#a274f5'],dining:['#ffd66b','#eeb01c'],gaming:['#93aaff','#6484f2'],clubs:['#8ff0c0','#4fd69a']},
  dark:{bg:'#02030a',bg2:'#0b0e1a',bg3:'#141a2e',text:'#eef1fb',muted:'#9aa3bd',line:'rgba(190,205,255,.11)',line2:'rgba(190,205,255,.2)',glass:'rgba(10,13,26,.78)',btn:'#b9c9ff',btnfg:'#0a0f2c',tint:'rgba(185,201,255,.15)',tintfg:'#b9c9ff'},
  light:{bg:'#f4f6fc',bg2:'#ffffff',bg3:'#e8ecf8',text:'#0c1022',muted:'#565d78',line:'rgba(10,15,44,.1)',line2:'rgba(10,15,44,.2)',glass:'rgba(248,249,255,.82)',btn:'#0a0f2c',btnfg:'#f4f6fc',tint:'#dfe6ff',tintfg:'#1d2f8a'}},
 solar:{name:'Solar',note:'Hot orange, coral & gold',ink:'#2b0f06',pastel:'#ffc7a3',
  cat:{sports:['#ffa64d','#f27d1a'],fitness:['#ff8676','#ec5a48'],pubs:['#ffd35a','#eeb01c'],dining:['#ffcaa0','#f0a06a'],gaming:['#ff9b71','#e8703f'],clubs:['#f6e27a','#d9bd3a']},
  dark:{bg:'#050302',bg2:'#110b08',bg3:'#1d140e',text:'#f8f0e9',muted:'#aa9d93',line:'rgba(255,220,190,.11)',line2:'rgba(255,220,190,.2)',glass:'rgba(17,11,8,.78)',btn:'#ffb488',btnfg:'#2b0f06',tint:'rgba(255,180,136,.15)',tintfg:'#ffb488'},
  light:{bg:'#faf5ef',bg2:'#ffffff',bg3:'#f2e8dc',text:'#1a0e08',muted:'#6b5a4e',line:'rgba(43,15,6,.1)',line2:'rgba(43,15,6,.2)',glass:'rgba(255,250,244,.82)',btn:'#2b0f06',btnfg:'#faf5ef',tint:'#ffe1cc',tintfg:'#8a3a10'}},
 chrome:{name:'Chrome',note:'Silver with one electric pop',ink:'#0d1016',pastel:'#dde3ec',
  cat:{sports:['#a8d4ff','#6fb2f5'],fitness:['#ffd27a','#f0b03a'],pubs:['#eceff4','#b9c1cf'],dining:['#d8def0','#a3add0'],gaming:['#8d9bff','#5e6ff0'],clubs:['#b9f0e0','#7fd4bd']},
  dark:{bg:'#050506',bg2:'#0d0e11',bg3:'#17191e',text:'#f2f4f7',muted:'#9a9fa8',line:'rgba(255,255,255,.1)',line2:'rgba(255,255,255,.19)',glass:'rgba(13,14,17,.78)',btn:'#e6ebf3',btnfg:'#0d1016',tint:'rgba(230,235,243,.13)',tintfg:'#e6ebf3'},
  light:{bg:'#f3f4f6',bg2:'#ffffff',bg3:'#e6e9ee',text:'#101319',muted:'#5a606b',line:'rgba(13,16,22,.1)',line2:'rgba(13,16,22,.2)',glass:'rgba(250,251,252,.82)',btn:'#0d1016',btnfg:'#f3f4f6',tint:'#e3e7ee',tintfg:'#2a3140'}},
 turf:{name:'Turf',note:'Pistachio green',ink:'#13200f',pastel:'#cdeea6',
  cat:{sports:['#bfe98f','#86c955'],fitness:['#ffa78c','#f27b5e'],pubs:['#f3c265','#d9922a'],dining:['#f7d98f','#e0b24a'],gaming:['#b6c2ff','#8496f0'],clubs:['#ffc2a0','#f29a6f']},
  dark:{bg:'#000000',bg2:'#0e100d',bg3:'#171a14',text:'#f4f1ea',muted:'#9da295',line:'rgba(255,255,255,.1)',line2:'rgba(255,255,255,.18)',glass:'rgba(14,16,13,.78)',btn:'#cdf3a6',btnfg:'#142010',tint:'rgba(205,243,166,.14)',tintfg:'#cdf3a6'},
  light:{bg:'#f7f4ec',bg2:'#ffffff',bg3:'#efeadf',text:'#121216',muted:'#5b5d55',line:'rgba(0,0,0,.1)',line2:'rgba(0,0,0,.2)',glass:'rgba(255,252,246,.8)',btn:'#14210f',btnfg:'#f7f4ec',tint:'#dcefc3',tintfg:'#24401a'}}
};
let palKey='violet';
function palVars(t,f){return `--bg:${t.bg};--bg2:${t.bg2};--bg3:${t.bg3};--text:${t.text};--muted:${t.muted};--line:${t.line};--line2:${t.line2};--glass:${t.glass};--btn-bg:${t.btn};--btn-fg:${t.btnfg};--tint:${t.tint};--tint-fg:${t.tintfg};--focus:${f};`;}
function applyPalette(k,rerender){
  const P=PAL[k]||PAL.violet;palKey=PAL[k]?k:'violet';INK=P.ink;
  Object.keys(P.cat).forEach(x=>{CATCOL[x].c=P.cat[x][0];CATCOL[x].c2=P.cat[x][1];});
  let st=document.getElementById('palstyle');if(!st){st=document.createElement('style');st.id='palstyle';document.head.appendChild(st);}
  st.textContent=`:root,:root[data-theme="light"]{${palVars(P.light,P.light.btn)}--pastel:${P.pastel};--ink:${P.ink};}
:root[data-theme="dark"]{${palVars(P.dark,P.dark.btn)}--pastel:${P.pastel};--ink:${P.ink};}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){${palVars(P.dark,P.dark.btn)}--pastel:${P.pastel};--ink:${P.ink};}}`;
  for(const id in coverCache)delete coverCache[id];
  store.set('hoppin.palette2',palKey);
  if(rerender){const y=window.scrollY;lastKey='';render();window.scrollTo(0,y);}
  renderPalMenu();
}
function renderPalMenu(){
  const m=$('#palmenu');if(!m)return;
  m.innerHTML='<div class="kicker">Palette</div>'+Object.entries(PAL).map(([k,P])=>`<button role="menuitem" class="${k===palKey?'on':''}" data-act="pal" data-k="${k}"><span class="sw">${['sports','fitness','pubs','gaming'].map(x=>`<i style="background:${P.cat[x][0]}"></i>`).join('')}</span><span><b>${P.name}</b><small>${P.note}</small></span></button>`).join('');
  const pb=$('#palBtn');if(pb)pb.innerHTML=`<span class="sw" style="margin-left:6px">${['sports','pubs','gaming'].map(x=>`<i style="background:${PAL[palKey].cat[x][0]};width:13px;height:13px;margin-left:-5px"></i>`).join('')}</span>`;
}
(function boot(){const s=store.get('hoppin.session',null);if(s){const users=store.get('hoppin.users',{});if(users[s]){S.user={email:s,name:users[s].name};}}})();

/* =========================================================
   SHELL: header, nav, theme
   ========================================================= */
const NAV=[['discover','Discover','Explore','#/','explore'],['sports','Sports','Sports','#/cat/sports','sports'],['dining','Dining','Dining','#/cat/dining','dining'],['gaming','Gaming','Gaming','#/cat/gaming','gaming'],['chat','AI Concierge','AI Chat','#/chat','chat']];
$('#nav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${n[1]}</a>`).join('');
$('#bnav').innerHTML=NAV.map(n=>`<a href="${n[3]}" data-nav="${n[0]}">${IC[n[4]]}<span>${n[2]}</span></a>`).join('');
function navActive(){
  let k='discover';
  if(S.view==='chat')k='chat';
  else if(S.view==='discover'&&['sports','dining','gaming'].includes(S.cat))k=S.cat;
  else if(S.view==='bookings')k='';
  $$('[data-nav]').forEach(a=>a.classList.toggle('on',a.dataset.nav===k));
}
function themeIcon(){const t=document.documentElement.getAttribute('data-theme');$('#themeBtn').innerHTML=t==='light'?IC.moon:IC.sun;$('#themeBtn').setAttribute('aria-label',t==='light'?'Switch to dark theme':'Switch to light theme');}
function toggleTheme(){const t=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',t);store.set('hoppin.theme',t);themeIcon();}
function acctBtn(){const a=$('#acct');if(S.user){a.classList.add('has');a.innerHTML=`<span class="av">${esc(S.user.name[0]||'H')}</span>Bookings`;}else{a.classList.remove('has');a.textContent='Sign in';}}
themeIcon();acctBtn();applyPalette(store.get('hoppin.palette2','violet'),false);

/* =========================================================
   MODAL SYSTEM (desktop card / mobile bottom sheet)
   ========================================================= */
const M={ov:null,sheet:null,prevFocus:null,
  show(html,cls){
    if(!M.ov){
      M.prevFocus=document.activeElement;
      M.ov=document.createElement('div');M.ov.className='ov';
      M.ov.innerHTML='<div class="sheet" role="dialog" aria-modal="true" tabindex="-1"></div>';
      M.ov.addEventListener('mousedown',e=>{if(e.target===M.ov)M.close();});
      document.body.appendChild(M.ov);document.documentElement.classList.add('lock');
      M.sheet=$('.sheet',M.ov);
    }
    M.sheet.className='sheet '+(cls||'');M.sheet.style.animation='none';M.sheet.style.transform='';
    M.sheet.innerHTML='<div class="grab" data-grab></div>'+html;
    M.sheet.scrollTop=0;
    requestAnimationFrame(()=>{M.sheet.style.animation='';});
    const f=$('input:not([type=hidden])',M.sheet);(f||M.sheet).focus({preventScroll:true});
  },
  close(){
    if(!M.ov)return;const ov=M.ov;M.ov=null;ov.classList.add('out');
    document.documentElement.classList.remove('lock');
    setTimeout(()=>ov.remove(),230);
    try{M.prevFocus&&M.prevFocus.focus({preventScroll:true});}catch(e){}
  }
};
document.addEventListener('keydown',e=>{if(e.key==='Escape')M.close();});
/* drag-to-dismiss on the sheet handle (phone) */
(function(){let y0=null,dy=0;
  document.addEventListener('touchstart',e=>{const g=e.target.closest('[data-grab]');if(!g||!M.sheet)return;y0=e.touches[0].clientY;dy=0;M.sheet.style.transition='none';},{passive:true});
  document.addEventListener('touchmove',e=>{if(y0==null||!M.sheet)return;dy=Math.max(0,e.touches[0].clientY-y0);M.sheet.style.transform=`translateY(${dy}px)`;},{passive:true});
  document.addEventListener('touchend',()=>{if(y0==null||!M.sheet){y0=null;return;}const s=M.sheet;s.style.transition='transform .25s ease';if(dy>110)M.close();else s.style.transform='';y0=null;});
})();

/* =========================================================
   AUTH (demo: accounts live in this browser only)
   ========================================================= */
function requireAuth(reason,then){
  if(S.user){then();return;}
  S.pending=then;showAuth('in',reason);
}
function showAuth(tab,reason){
  const up=tab==='up';
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div class="pad">
    <div class="kicker">${up?'Join hoppin.':'Welcome back'}</div>
    <h2>${up?'Create your account':'Sign in to step inside'}</h2>
    <p class="lead">${esc(reason||'Browsing is free. Sign in to see inside venues, book slots and talk to the AI Concierge.')}</p>
    <div class="tabs" role="tablist"><button class="${up?'':'on'}" data-act="auth-tab" data-tab="in" role="tab">Sign in</button><button class="${up?'on':''}" data-act="auth-tab" data-tab="up" role="tab">Create account</button></div>
    <form id="authForm" data-mode="${up?'up':'in'}" novalidate>
      ${up?`<div class="f"><label for="an">Name</label><input id="an" name="name" autocomplete="name" placeholder="Your name"></div>`:''}
      <div class="f"><label for="ae">Email</label><input id="ae" name="email" type="email" autocomplete="email" placeholder="you@example.com"></div>
      <div class="f"><label for="ap">Password</label><input id="ap" name="pw" type="password" autocomplete="${up?'new-password':'current-password'}" placeholder="At least 6 characters"></div>
      <div class="err" id="autherr" role="alert"></div>
      <button class="btn block" type="submit">${up?'Create account':'Sign in'}</button>
    </form>
    <button class="linkbtn" data-act="demo-login">Skip and explore as a demo guest</button>
  </div>`,'sm');
}
function finishAuth(user){
  S.user=user;store.set('hoppin.session',user.email);acctBtn();M.close();toast('Signed in as '+user.name);
  const p=S.pending;S.pending=null;
  render(); if(p)setTimeout(p,260);
}
async function submitAuth(form){
  const mode=form.dataset.mode;const fd=new FormData(form);
  const email=String(fd.get('email')||'').trim().toLowerCase();const pw=String(fd.get('pw')||'');const name=String(fd.get('name')||'').trim();
  const err=m=>{$('#autherr').textContent=m;};
  if(!/^\S+@\S+\.\S+$/.test(email))return err('Enter a valid email address.');
  if(pw.length<6)return err('Password needs at least 6 characters.');
  
  // Call backend API
  const res=await api(mode==='up'?'/auth/signup':'/auth/login','POST',{name,email,password:pw});
  if(res&&!res._err&&res.user){
    const users=store.get('hoppin.users',{});
    users[email]={name:res.user.name,pw:btoa(unescape(encodeURIComponent(pw)))};
    store.set('hoppin.users',users);
    return finishAuth(res.user);
  }
  if(res&&res._err)return err(res._err);

  // Local fallback
  const users=store.get('hoppin.users',{});
  if(mode==='up'){
    if(!name)return err('Add your name so we can put it on your tickets.');
    if(users[email])return err('That email already has an account. Sign in instead.');
    users[email]={name,pw:btoa(unescape(encodeURIComponent(pw)))};store.set('hoppin.users',users);
    finishAuth({email,name});
  }else{
    const u=users[email];
    if(!u||u.pw!==btoa(unescape(encodeURIComponent(pw))))return err('Email or password is wrong. Check both, or create an account.');
    finishAuth({email,name:u.name});
  }
}
function signOut(){S.user=null;store.set('hoppin.session',null);acctBtn();S.chat=[];S.lastHits=[];go('/');toast('Signed out');}

/* =========================================================
   VENUE DETAIL + BOOKING
   ========================================================= */
let B=null;
function stars(v){return `<span class="r">${IC.star}${v.rating.toFixed(1)}</span><span>${v.reviews.toLocaleString('en-IN')} reviews</span>${myRate(v)}`;}
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
        <div class="meta">${stars(v)}<span>${esc(v.area)}, ${CITY[v.city].name}</span></div>
        <div class="tags">${v.tags.map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>
        <p>${esc(v.desc)}</p>
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
    return `<button class="slot ${a.state} ${B.slot===s?'on':''}" data-act="slot" data-slot="${s}" ${dis?'disabled':''} aria-pressed="${B.slot===s}"><span class="t">${s}</span><span class="p">${lab}</span>${a.state==='few'?`<span class="f">${a.left} left</span>`:''}</button>`;}).join('');
  const sel=B.slot&&avail(v,B.iso,B.slot);
  if(sel&&!isOpenState(sel.state))B.slot=null;
  const price=B.slot?slotPrice(v,B.slot):null;
  $('#vright').innerHTML=`
    <div><h4>Pick a day</h4><div class="days" style="margin-top:10px">${days.map(d=>{const x=fromISO(d);return `<button class="day ${d===B.iso?'on':''}" data-act="day" data-iso="${d}" aria-pressed="${d===B.iso}"><span>${d===todayISO()?'Today':WD[x.getDay()]}</span><b>${x.getDate()}</b><span>${MO[x.getMonth()]}</span></button>`;}).join('')}</div></div>
    <div><h4>Pick a time</h4><div class="slots" style="margin-top:10px">${slotBtns}</div></div>
    <div class="legend"><span><i style="background:var(--ok)"></i>Open</span><span><i style="background:var(--warn)"></i>Filling fast</span><span><i style="background:var(--line2)"></i>Full or passed</span></div>
    <div class="bookbar">
      <div class="sum">${B.slot?`${dayLabel(B.iso)==='today'?'Today':dayLabel(B.iso)==='tomorrow'?'Tomorrow':dayLabel(B.iso)}, ${B.slot}<b>${inr(price)}</b>`:'Choose a slot to continue<b>&nbsp;</b>'}</div>
      <button class="btn" data-act="reserve" ${B.slot?'':'disabled'}>${B.resched?'Move booking here':'Reserve slot'}</button>
    </div>`;
}

/* ---------- Stripe-style checkout (test-mode UI; no real charge) ---------- */
const FEE=30;
function showCheckout(order){
  if(isBooked(order.venueId,order.iso,order.slot)){toast('You already booked this slot.');return;}
  const v=VBY[order.venueId];order.fee=FEE;order.disc=order.disc||0;order.total=order.price+FEE-order.disc;
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div class="pad">
    <div class="kicker">Secure checkout</div>
    <h2>Pay to confirm</h2>
    <div class="order"><div class="th">${coverMedia(v)}</div><div><b>${esc(v.name)}</b><span>${esc(dayLabel(order.iso)==='today'?'Today':dayLabel(order.iso)==='tomorrow'?'Tomorrow':dayLabel(order.iso))} · ${order.slot} · ${esc(v.area)}</span></div></div>
    <div class="lines" id="lines">${linesHTML(order)}</div>
    <div class="testnote">${IC.info}<span>Test mode. No real charge. Use card <b>4242 4242 4242 4242</b>, any future expiry, any CVC. <b>4000 0000 0000 0002</b> simulates a decline.</span></div>
    <div class="frow" style="align-items:flex-end"><div class="f"><label for="pcode">Promo code</label><input id="pcode" placeholder="HOPPIN20, FIRST50 or CREW100" autocomplete="off"></div><button type="button" class="btn ghost sm" style="margin-bottom:14px" data-act="promo">Apply</button></div>
    <form id="payForm" novalidate>
      <div class="f"><label for="pe">Email for your ticket</label><input id="pe" name="email" type="email" value="${esc(S.user?S.user.email:'')}" autocomplete="email"></div>
      <div class="f"><label for="pc">Card number</label><input id="pc" name="card" inputmode="numeric" autocomplete="cc-number" placeholder="4242 4242 4242 4242" maxlength="23"></div>
      <div class="frow"><div class="f"><label for="px">Expiry</label><input id="px" name="exp" inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" maxlength="7"></div><div class="f"><label for="pv">CVC</label><input id="pv" name="cvc" inputmode="numeric" autocomplete="cc-csc" placeholder="123" maxlength="4"></div></div>
      <div class="f"><label for="pn">Name on card</label><input id="pn" name="cname" autocomplete="cc-name" value="${esc(S.user?S.user.name:'')}"></div>
      <div class="err" id="payerr" role="alert"></div>
      <button class="btn block" type="submit" id="payBtn">${IC.card}<span>Pay ${inr(order.total)}</span></button>
    </form>
    <div class="stripe-tag">${IC.lock} Payments by Stripe · demo checkout</div>
    <button class="linkbtn" data-act="back-venue">Back to slots</button>
  </div>`,'md');
  showCheckout.order=order;
}
const luhn=n=>{let s=0,d=false;for(let i=n.length-1;i>=0;i--){let x=+n[i];if(d){x*=2;if(x>9)x-=9;}s+=x;d=!d;}return s%10===0;};
function submitPay(form){
  const o=showCheckout.order;const fd=new FormData(form);const err=m=>{$('#payerr').textContent=m;};
  const num=String(fd.get('card')).replace(/\D/g,'');const exp=String(fd.get('exp')).replace(/\D/g,'');const cvc=String(fd.get('cvc')).replace(/\D/g,'');
  if(!/^\S+@\S+\.\S+$/.test(String(fd.get('email')).trim()))return err('Enter the email where we should send the ticket.');
  if(num.length<13||!luhn(num))return err('That card number is not valid. Check it and try again.');
  const mm=+exp.slice(0,2),yy=2000+ +exp.slice(2,4);const now=new Date();
  if(exp.length<4||mm<1||mm>12||yy<now.getFullYear()||(yy===now.getFullYear()&&mm<now.getMonth()+1))return err('The expiry date is missing or in the past.');
  if(cvc.length<3)return err('Enter the 3 or 4 digit security code.');
  const btn=$('#payBtn');btn.disabled=true;btn.innerHTML='<span class="spin"></span><span>Processing…</span>';err('');
  setTimeout(()=>{
    if(num==='4000000000000002'){btn.disabled=false;btn.innerHTML=IC.card+'<span>Pay '+inr(o.total)+'</span>';return err('Your card was declined. Try a different card.');}
    if(num==='4000000000009995'){btn.disabled=false;btn.innerHTML=IC.card+'<span>Pay '+inr(o.total)+'</span>';return err('Insufficient funds on this card. Try a different card.');}
    (async()=>{
      // Call backend API to record booking
      const bkRes=await api('/bookings','POST',{
        venueId:o.venueId,iso:o.iso,slot:o.slot,partySize:1,
        userEmail:S.user.email,userName:S.user.name,card:num,
        disc:o.disc||0,promoCode:$('#pcode')?.value?.trim()
      });
      const bk=bkRes?.booking||{ref:o.ref||newRef(),venueId:o.venueId,iso:o.iso,slot:o.slot,price:o.price,fee:o.fee,total:o.total,at:Date.now(),last4:num.slice(-4)};
      const list=store.get('hoppin.bookings:'+S.user.email,[]);list.unshift(bk);store.set('hoppin.bookings:'+S.user.email,list);
      showTicket(bk,true);
      if(S.view==='chat'){pushAssistant({text:`Payment received. <strong>${esc(VBY[bk.venueId].name)}</strong> is confirmed for ${esc(dayLabel(bk.iso))} at ${bk.slot}. Your ticket is in My bookings.`});}
      if(S.view==='bookings')renderBookings();
    })();
  },1500);
}
function qrSVG(seed){
  const N=21,R=rng(hashStr(seed));let d='';
  const inF=(x,y)=>(x<8&&y<8)||(x>12&&y<8)||(x<8&&y>12);
  for(let y=0;y<N;y++)for(let x=0;x<N;x++){if(!inF(x,y)&&R()>.52)d+=`M${x} ${y}h1v1h-1z`;}
  const f=(x,y)=>`<path d="M${x} ${y}h7v7h-7z" fill="none" stroke="${INK}" stroke-width="1"/><path d="M${x+2} ${y+2}h3v3h-3z" fill="${INK}"/>`;
  return `<svg viewBox="-.5 -.5 22 22" width="74" height="74" shape-rendering="crispEdges"><path d="${d}" fill="${INK}"/>${f(.5,.5)}${f(13.5,.5)}${f(.5,13.5)}</svg>`;
}
function showTicket(b,fresh){
  const v=VBY[b.venueId];const dl=dayLabel(b.iso);
  M.show(`<button class="x plain" data-act="close" aria-label="Close">×</button>
  <div class="done">
    <div class="kicker">${fresh?'Payment received':'Your ticket'}</div>
    <h2>${fresh?'You’re in.':'Ticket'}</h2>
    <div class="tk">
      <div class="top"><div class="kicker">${esc(CITY[v.city].name)} · ${esc(CATS[v.cat].label)}</div><h3>${esc(v.name)}</h3>
        <div class="row"><span>${esc(dl==='today'?'Today':dl==='tomorrow'?'Tomorrow':dl)}</span><b>${b.slot}</b></div>
        <div class="row" style="margin-top:4px"><span>${esc(v.area)}</span><b>${inr(b.total)} paid</b></div>
        ${fresh?`<div class="stamp">${IC.check}</div>`:''}</div>
      <div class="perf"></div>
      <div class="bot"><div><small>Reference</small><div class="ref">${b.ref}</div></div>${qrSVG(b.ref)}</div>
    </div>
    ${crewHTML(b,v)}<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">
      <button class="btn" data-act="to-bookings">View my tickets</button>
      ${fresh?'':`<button class="btn ghost" data-act="resched" data-ref="${b.ref}">Reschedule</button><button class="btn ghost" data-act="rebook" data-id="${b.venueId}">Book again</button><button class="btn ghost" data-act="cancel" data-ref="${b.ref}">Cancel booking</button>`}<button class="btn ghost" data-act="close">Done</button>
    </div>
  </div>`,'sm');
}

/* =========================================================
   DISCOVER
   ========================================================= */
function filtered(){
  const q=S.q.trim().toLowerCase().split(/\s+/).filter(Boolean);
  let a=VENUES.filter(v=>{
    if(S.city!=='all'&&v.city!==S.city)return false;
    if(S.cat==='saved'){if(!saved().includes(v.id))return false;}else if(S.cat!=='all'&&v.cat!==S.cat)return false;
    if(S.tonight&&!openTonight(v).length)return false;if(S.maxp&&v.price>S.maxp)return false;if(S.minr&&v.rating<S.minr)return false;
    if(q.length){const hay=(v.name+' '+v.area+' '+CITY[v.city].name+' '+CATS[v.cat].label+' '+v.tags.join(' ')).toLowerCase();if(!q.every(t=>hay.includes(t)))return false;}
    return true;});
  if(S.sort==='rating')a.sort((x,y)=>y.rating-x.rating||y.reviews-x.reviews);
  else if(S.sort==='reviews')a.sort((x,y)=>y.reviews-x.reviews);
  else if(S.sort==='near'&&S.geo)a.sort((x,y)=>dist(x)-dist(y));else a.sort((x,y)=>x.price-y.price);
  return a;
}
const saved=()=>store.get('hoppin.saved',[]);
const dist=v=>{const r=x=>x*Math.PI/180,[a,b]=S.geo;return 6371*Math.acos(Math.min(1,Math.sin(r(a))*Math.sin(r(v.lat))+Math.cos(r(a))*Math.cos(r(v.lat))*Math.cos(r(v.lng-b))));};
const km=v=>dist(v).toFixed(1);
function getGeo(){const fail=()=>{toast('Location is blocked here. Allow it in your browser to sort by distance.');S.sort='rating';const e=$('#sort');if(e)e.value='rating';renderGrid();};
  try{navigator.geolocation.getCurrentPosition(p=>{S.geo=[p.coords.latitude,p.coords.longitude];renderGrid();},fail,{timeout:8000});}catch(e){fail();}}
const linesHTML=o=>`<div><span>Slot</span><span>${inr(o.price)}</span></div><div><span>Booking fee</span><span>${inr(o.fee)}</span></div>${o.disc?`<div><span>Promo</span><span>−${inr(o.disc)}</span></div>`:''}<div class="tot"><span>Total</span><span>${inr(o.total)}</span></div>`;
function calURL(b,v){const st=new Date(fromISO(b.iso).getTime()+toMin(b.slot)*6e4),en=new Date(st.getTime()+36e5),f=d=>d.getFullYear()+String(d.getMonth()+1).padStart(2,'0')+String(d.getDate()).padStart(2,'0')+'T'+String(d.getHours()).padStart(2,'0')+String(d.getMinutes()).padStart(2,'0')+'00';
  return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent(v.name+' (hoppin.)')+'&dates='+f(st)+'/'+f(en)+'&location='+encodeURIComponent(v.name+', '+v.area)+'&details='+encodeURIComponent('Ref '+b.ref);}
const isPastB=b=>new Date(fromISO(b.iso).getTime()+toMin(b.slot)*6e4)<Date.now();
function myRate(v){const R=store.get('hoppin.reviews',{});const b=bookings().find(x=>x.venueId===v.id&&R[x.ref]);return b?`<span>You rated ★${R[b.ref]}</span>`:'';}
function crewHTML(b,v){const past=isPastB(b),r=store.get('hoppin.reviews',{})[b.ref]||0;
  return `<div class="crew" data-total="${b.total}"><div class="kicker" style="margin-bottom:8px">Bring your crew</div>
  <div class="crewrow"><button class="pill" data-act="crewn" data-d="-1" aria-label="Fewer people">−</button><b id="crewn">4</b><button class="pill" data-act="crewn" data-d="1" aria-label="More people">+</button><span>people · <b id="crewamt">${inr(b.total/4)}</b> each</span></div>
  <div class="crewrow"><button class="btn sm" data-act="share" data-ref="${b.ref}">Share invite</button><a class="btn ghost sm" target="_blank" rel="noopener" href="${calURL(b,v)}">Add to calendar</a></div>
  <textarea id="sharetxt" readonly hidden rows="3" style="width:100%;margin-top:6px;border-radius:12px;padding:8px;background:var(--bg);color:var(--text);border:1px solid var(--line2)"></textarea>
  <div class="kicker" style="margin:14px 0 8px">${past?'Rate your visit':'Reviews open after your slot'}</div>
  <div class="crewrow" id="rstars">${[1,2,3,4,5].map(n=>`<button class="pill ${r>=n?'on':''}" data-act="rate" data-ref="${b.ref}" data-n="${n}" ${past?'':'disabled'}>★</button>`).join('')}</div></div>`;}
async function reschedule(ref,iso,slot){
  api('/bookings/'+encodeURIComponent(ref)+'/reschedule','POST',{iso,slot});
  const k='hoppin.bookings:'+S.user.email,l=store.get(k,[]),b=l.find(x=>x.ref===ref);
  if(!b)return;b.iso=iso;b.slot=slot;store.set(k,l);
  toast('Booking moved. Any price difference is settled at the venue.');
  showTicket(b,false);if(S.view==='bookings')renderBookings();
}

function cardHTML(v){
  const locked=!S.user;const sv=saved().includes(v.id);
  return `<article class="card" tabindex="0" data-act="venue" data-id="${v.id}">
    <div class="cv">${coverMedia(v)}
      <div class="b1"><span class="badge">${CITY[v.city].short}</span><span class="badge">${CATS[v.cat].label.split(' & ')[0]}</span></div>
      ${locked?`<span class="lock" title="Sign in to see inside">${IC.lock}</span>`:''}
      <button class="fav ${sv?'on':''}" data-act="save" data-id="${v.id}" aria-pressed="${sv}" aria-label="Save ${esc(v.name)}">♥</button>
      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><small>(${v.reviews.toLocaleString('en-IN')})</small></div>
    </div>
    <div class="cb">
      <h3>${esc(v.name)}</h3>
      <div class="loc"><span>${esc(v.area)}</span><span>${S.geo?km(v)+' km · ':''}${CITY[v.city].name}</span></div>
      <div class="tags">${v.tags.slice(0,3).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>
      <div class="go"><span class="price">from <b>${inr(v.price)}</b></span><button class="btn sm" data-act="venue" data-id="${v.id}">View slots &amp; reserve ↗</button></div>
    </div></article>`;
}
function renderGrid(){
  const list=filtered();
  $('#count').innerHTML=`<span>${list.length} venue${list.length===1?'':'s'}</span>${S.tonight?`<button data-act="tonight-off">Open tonight ✕</button>`:''}`;
  $('#grid').innerHTML=list.length?list.map(cardHTML).join(''):`<div class="empty"><h3>Nothing here yet</h3><p>No venue matches these filters. Try a wider search or clear them.</p><button class="btn" data-act="reset">Clear filters</button></div>`;
  $$('#catpills .pill').forEach(p=>p.classList.toggle('on',p.dataset.cat===S.cat));
  $$('#cityseg button').forEach(b=>b.classList.toggle('on',b.dataset.city===S.city));$$('[data-act="tonight-toggle"]').forEach(b=>b.classList.toggle('on',S.tonight));
  navActive();
}
function catTile(k){
  const C=CATCOL[k];const id='t'+(++uid);const n=VENUES.filter(v=>v.cat===k).length;
  return `<button class="ct" style="background:${C.c}" data-act="catgo" data-cat="${k}"><svg class="band" viewBox="0 0 200 200" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>${pat(C.kind,id,C.c,C.c2)}</defs><rect width="200" height="200" fill="url(#${id})"/></svg><span class="em" aria-hidden="true">${C.emoji}</span><span class="tx"><h3>${CATS[k].label}</h3><p>${C.sub}</p><span class="n">${n} venues ↗</span></span></button>`;
}
function liveHTML(){
  const iso=todayISO();const now=nowMin();
  let rows=VENUES.map(v=>{const o=openTonight(v).filter(s=>toMin(s)>now);return o.length?{v,s:o[0],m:toMin(o[0])}:null;}).filter(Boolean);
  rows.sort((a,b)=>a.m-b.m||b.v.rating-a.v.rating);
  let title='Open today';
  if(!rows.length){title='Open tomorrow';rows=VENUES.map(v=>{const n=nextOpen(v);return n?{v,s:n.slot,m:toMin(n.slot)}:null;}).filter(Boolean).sort((a,b)=>a.m-b.m||b.v.rating-a.v.rating);}
  rows=rows.slice(0,5);
  return `<div class="live-h"><span class="kicker" style="display:flex;align-items:center;gap:10px"><span class="dot"></span>${title}</span><span class="kicker">Next slot</span></div>`+
    rows.map(r=>`<button class="lrow" data-act="venue" data-id="${r.v.id}"><span class="th">${coverMedia(r.v)}</span><span><b>${esc(r.v.name)}</b><small>${esc(r.v.area)}, ${CITY[r.v.city].short} · ${inr(r.v.price)}</small></span><span class="tm">${r.s}</span></button>`).join('');
}
function floaters(){
  const vs=[...Object.keys(CATS).map(k=>VENUES.find(v=>v.cat===k)),VENUES[9],VENUES[40]];
  const pos=[[44,58,-12,150],[56,10,8,120],[66,66,-6,170],[78,14,14,130],[88,58,-10,140],[50,32,9,110],[72,36,-8,120],[92,22,12,110]];
  return vs.map((v,i)=>{const [x,y,r,w]=pos[i];return `<div class="fl" style="left:${x}%;top:${y}%;--r:${r}deg;width:${w}px;animation-delay:-${i*1.3}s" data-d="${(i%3+1)*6}"><div class="fc">${coverMedia(v)}<b>${esc(v.name.split(' · ')[0])}</b></div></div>`;}).join('');
}
function s1HTML(){return `<section class="story dark"><div class="lab"><span>About the problem</span><span>Chapter 01</span></div>
  <h2 class="display stag"><span class="rv">Plans live in the group chat.</span><span class="rv">Nobody books them.</span><span class="rv">Next weekend, always.</span></h2>
  <p class="rv sp">Someone says football. Someone asks which turf. Three days later the slots are gone. hoppin. puts the venue, the time and the price in one place, so the plan survives the chat.</p></section>`;}
function s3HTML(){
  const pick=k=>VENUES.find(v=>v.cat===k);
  const rows=[['To book the turf before it fills up.','Live slots for tonight, tomorrow and the weekend. Prices shown up front.','sports'],['To try the place you always walked past.','Taprooms, board game cafes and run clubs, sorted by neighbourhood.','pubs'],['To bring the whole crew and split the bill.','Book once, share the invite, see what each person owes.','gaming']];
  return `<section class="story light"><div class="lab"><span>About the journey</span><span>Chapter 04</span></div>
  <h2 class="display rv">It starts as one booking. It rarely stays that way.</h2>
  <div class="rows">${rows.map((r,i)=>`<div class="row3 rv"><div><small>A chance</small><b>${r[0]}</b><i>0${i+1}</i></div><div class="th3">${coverMedia(pick(r[2]))}</div><p>${r[1]}</p></div>`).join('')}</div></section>`;}
function motion(){
  if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}}),{threshold:.15});$$('.rv').forEach(x=>io.observe(x));}else $$('.rv').forEach(x=>x.classList.add('in'));
  const h=$('#top');if(h&&!reduceMotion)h.addEventListener('mousemove',e=>{const x=e.clientX/innerWidth-.5,y=e.clientY/innerHeight-.5;$$('.fl').forEach(f=>{const d=+f.dataset.d;f.style.setProperty('--px',(x*d*-3)+'px');f.style.setProperty('--py',(y*d*-3)+'px');});});
}
function loader(){try{let seen=null;try{seen=sessionStorage.getItem('hp.l');sessionStorage.setItem('hp.l','1');}catch(e){}if(seen||reduceMotion)return;
  const L=document.createElement('div');L.id='loader';L.innerHTML=`<div class="lc"><svg viewBox="0 0 100 112" width="72"><path d="${SHIELD}" fill="#f7f4ff" stroke="#0a0612" stroke-width="3"/><text x="50" y="66" text-anchor="middle" font-family="Bodoni Moda,Georgia,serif" font-size="34" fill="#0a0612">h.</text></svg><b id="lp">LOADING 0%</b></div>`;document.body.appendChild(L);
  let n=0;const t=setInterval(()=>{n=Math.min(100,n+7);const e=$('#lp');if(e)e.textContent='LOADING '+n+'%';if(n>=100){clearInterval(t);setTimeout(()=>{L.classList.add('off');setTimeout(()=>L.remove(),500);},250);}},45);}catch(e){const l=$('#loader');l&&l.remove();}}
function discoverHTML(){
  const opens=VENUES.filter(v=>openTonight(v).length).length;
  const catPills=[['all','All'],...Object.entries(CATS).map(([k,c])=>[k,c.label]),['saved','♥ Saved']];
  return `
  <section class="hero" id="top"><div class="lab"><span>hoppin. · Bengaluru + Chennai</span><span>${COUNT.all} venues</span></div><div class="floaters" aria-hidden="true">${floaters()}</div>
    <div class="hero-l">
      <h1 class="display mega">Step out.<br>Show up.</h1>
      <p class="sub">${COUNT.all} curated courts, turfs, taprooms, game cafes and run clubs across Bengaluru and Chennai. Pick a slot. Show up.</p>
      <form class="hsearch" id="heroForm" role="search"><label class="sr" for="hq">Search venues</label><input id="hq" placeholder="Search venues or areas" autocomplete="off"><button class="btn sm" type="submit">Search</button></form>
      <div class="cta"><a class="btn ghost" href="#/chat">Ask the AI Concierge</a></div>
      <p class="fine">Browsing is free. Sign in to see inside a venue, book, or chat with the concierge.</p>
    </div>
    <aside class="live" aria-label="Open today">${liveHTML()}</aside>
  </section>

  ${s1HTML()}
  <section class="sec wrap" id="cats"><div class="lab2"><span>About the scenes</span><span>Chapter 02</span></div>
    <div class="sec-h"><h2 class="display">Pick your scene. It shapes your week.</h2><p>Six ways to get out of the house. Tap one to filter the list below.</p></div>
    <div class="cats">${Object.keys(CATS).map(catTile).join('')}</div>
  </section>

  <section class="chapter" id="tonight"><div class="lab"><span>About tonight</span><span>Chapter 03</span></div>
    <div class="bigclock" id="clock" aria-hidden="true">00:00:00</div>
    <div class="in">
      <div><div class="kicker">Tonight</div><h2 class="display" style="margin-top:14px">The clock is running.</h2></div>
      <div>
        <p>${opens?`<b>${opens} of ${COUNT.all} venues</b> still have a slot open today. Slots go fast once the floodlights are on.`:`Nothing left today. Tomorrow's first slots open from 5:15 AM.`}</p>
        <button class="btn ink" data-act="tonight-on">${opens?'See what is open tonight':'Browse tomorrow'}</button>
      </div>
    </div>
  </section>

  ${s3HTML()}
  <section class="sec wrap" id="explore">
    <div class="sec-h"><h2 class="display">Where to next?</h2><p>Filter by city, category or vibe. Prices are per slot.</p></div>
    <div class="ctrl">
      <div class="ctrl-row"><div class="seg" id="cityseg" role="group" aria-label="City">
        <button data-city="all" data-act="city">All (${COUNT.all})</button><button data-city="BLR" data-act="city">Bengaluru (${COUNT.BLR})</button><button data-city="MAA" data-act="city">Chennai (${COUNT.MAA})</button></div></div>
      <div class="ctrl-row"><label class="search"><span class="sr">Search venues</span>${IC.search}<input id="q" type="search" placeholder="Search venues, areas, tags…" value="${esc(S.q)}" autocomplete="off"></label>
        <label><span class="sr">Sort</span><select class="select" id="sort"><option value="rating">Sort: Rating</option><option value="reviews">Sort: Reviews</option><option value="price">Sort: Price, low to high</option><option value="near">Sort: Near me</option></select></label>
        <label><span class="sr">Max price</span><select class="select" id="fprice"><option value="0">Any price</option><option value="500">Up to ₹500</option><option value="800">Up to ₹800</option><option value="1200">Up to ₹1,200</option></select></label>
        <label><span class="sr">Min rating</span><select class="select" id="frate"><option value="0">Any rating</option><option value="4.3">4.3 and up</option><option value="4.6">4.6 and up</option></select></label>
        <button class="pill" data-act="tonight-toggle">Open today</button></div>
      <div class="pills" id="catpills">${catPills.map(([k,l])=>`<button class="pill" data-act="cat" data-cat="${k}">${l}</button>`).join('')}</div>
    </div>
    <div class="count-line" id="count"></div>
    <div class="grid" id="grid"></div>
  </section>
  <section class="story dark fin"><div class="lab"><span>Get out there</span><span>Chapter 05</span></div><h2 class="display rv">Stop meaning to.<br>Start booking.</h2><p class="rv">Pick a slot, bring your crew, show up.</p><button class="btn" data-scroll="explore">Browse venues</button></section>
  ${footerHTML()}`;
}
function footerHTML(){return `<footer class="ft"><div class="big">hoppin.</div><div class="row"><span>Discover real places. Step out into the city.</span><span>Bengaluru · Chennai</span><span>Demo build: payments run in test mode.</span></div></footer>`;}
let clockT=null;
function startClock(){clearInterval(clockT);const tick=()=>{const c=$('#clock');if(!c){clearInterval(clockT);return;}const d=new Date();c.textContent=[d.getHours(),d.getMinutes(),d.getSeconds()].map(n=>String(n).padStart(2,'0')).join(':');};tick();clockT=setInterval(tick,1000);}

/* =========================================================
   AI CONCIERGE (demo retriever standing in for pgvector + Claude)
   ========================================================= */
const STOP=new Set('a an the in at on for to of and or with me my i is are it near best any some good place places show find looking want need can you please tonight today tomorrow morning evening night around under below than less book reserve hold grab that this one do does what where which get'.split(' '));
const CATWORDS={
  sports:['badminton','football','turf','turfs','soccer','cricket','tennis','court','courts','5v5','futsal','pitch','floodlit','floodlights','sport','sports','shuttle'],
  fitness:['gym','gyms','workout','crossfit','sauna','fitness','weights','hiit','train','training','cult'],
  pubs:['pub','pubs','beer','beers','brew','brews','brewpub','taproom','bar','bars','cocktail','cocktails','drinks','drink','craft','rooftop','gastrobar','lounge'],
  dining:['cafe','cafes','café','coffee','dinner','lunch','brunch','food','restaurant','dining','eat','wine','breakfast','beachside'],
  gaming:['board','boardgame','boardgames','game','games','gaming','vr','arcade','esports','e-sports','puzzle','puzzles','simulator','simulators'],
  clubs:['run','runs','running','runner','runners','yoga','cycling','cycle','club','clubs','community','meetup','marathon','league']
};
const stem=w=>w.length>3?w.replace(/(es|s)$/,''):w;
const AREAS_LOWER=[...new Set(VENUES.map(v=>v.area.toLowerCase()))].filter(a=>!['chennai','bengaluru'].includes(a));
function parseQuery(q){
  const low=q.toLowerCase().replace(/[’]/g,"'");
  const info={raw:q,low,city:null,areas:[],cats:{},price:null,window:null,minute:null,date:null,wd:null,book:/\b(book|reserve|hold|grab|lock)\b/.test(low)};
  if(/\b(bengaluru|bangalore|blr)\b/.test(low))info.city='BLR';
  else if(/\b(chennai|maa)\b/.test(low))info.city='MAA';
  AREAS_LOWER.forEach(a=>{if(low.includes(a))info.areas.push(a);});
  if(!info.city&&info.areas.length){const v=VENUES.find(v=>v.area.toLowerCase()===info.areas[0]);if(v)info.city=v.city;}
  const toks=low.split(/[^a-z0-9'é\-]+/).filter(Boolean);
  info.toks=toks;
  toks.forEach(t=>{for(const [c,ws] of Object.entries(CATWORDS)){if(ws.includes(t))info.cats[c]=(info.cats[c]||0)+1;}});
  const pm=/(?:under|below|less than|within|upto|up to)\s*(?:rs\.?|₹|inr)?\s*(\d{3,5})/.exec(low);if(pm)info.price=+pm[1];
  const tm=/\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b/.exec(low);if(tm){let h=(+tm[1])%12;if(tm[3]==='pm')h+=12;info.minute=h*60+ +(tm[2]||0);}
  if(/\bmorning|sunrise|early\b/.test(low))info.window='am';
  if(/\bevening|tonight|night|after work\b/.test(low))info.window='pm';
  if(/\btoday|tonight\b/.test(low))info.date='today';else if(/\btomorrow\b/.test(low))info.date='tomorrow';
  const wi=['sunday','monday','tuesday','wednesday','thursday','friday','saturday'].findIndex(d=>low.includes(d));if(wi>=0)info.wd=wi;
  return info;
}
function retrieve(info,scopeCity){
  let pool=VENUES.filter(v=>!scopeCity||v.city===scopeCity);
  const qt=info.toks.filter(t=>!STOP.has(t)&&t.length>1).map(stem);
  const scored=pool.map(v=>{
    const name=v.name.toLowerCase(),area=v.area.toLowerCase(),tags=v.tags.join(' ').toLowerCase(),desc=v.desc.toLowerCase();
    let s=0;
    qt.forEach(t=>{if(name.includes(t))s+=3;if(area.includes(t))s+=3;if(tags.includes(t))s+=2;if(desc.includes(t))s+=1;});
    if(info.areas.some(a=>area===a))s+=5;
    s+=4*(info.cats[v.cat]||0);
    if(info.window==='am'&&v.slots.some(x=>toMin(x)<12*60))s+=.5;
    if(info.window==='pm'&&v.slots.some(x=>toMin(x)>=17*60))s+=.5;
    if(info.price&&v.price>info.price)s=0;
    return {v,s};
  }).filter(x=>x.s>0);
  scored.sort((a,b)=>b.s-a.s||b.v.rating-a.v.rating);
  return scored;
}
function resolveTarget(info){
  const q=info.low;const qt=new Set(info.toks.filter(t=>!/^(first|second|third|top|1st|2nd|3rd|one|last)$/.test(t)).map(stem));
  let best=null,bs=0;
  VENUES.forEach(v=>{
    const nt=v.name.toLowerCase().replace(/[^a-z0-9' ]+/g,' ').split(/\s+/).filter(w=>w.length>2&&!STOP.has(w)&&!['the','club','run','and'].includes(w)).map(stem);
    if(!nt.length)return;const hit=nt.filter(w=>qt.has(w)).length;const sc=hit/nt.length;
    const bonus=(S.lastHits.includes(v.id)?.1:0)+(info.areas.includes(v.area.toLowerCase())?.15:0);
    if(hit>0&&sc+bonus>bs){bs=sc+bonus;best=v;}
  });
  if(best&&bs>=.5)return best;
  const ord=/\b(first|top|1st|#1|number one)\b/.test(q)?0:/\b(second|2nd|#2)\b/.test(q)?1:/\b(third|3rd|#3)\b/.test(q)?2:null;
  if(ord!==null&&S.lastHits[ord])return VBY[S.lastHits[ord]];
  if(S.lastHits.length)return VBY[S.lastHits[0]];
  return null;
}
function answer(q){
  const info=parseQuery(q);const low=info.low;
  if(info.areas.length||info.city){const c=info.city;if(c&&c!==S.chatCity){S.chatCity=c;syncCitySeg();}}
  const scope=S.chatCity;
  if(/^(hi|hello|hey|yo|help)\b/.test(low.trim())&&low.trim().length<14){
    return {text:`Hi ${esc(S.user.name.split(' ')[0])}. I only know the ${COUNT.all} venues on hoppin. Ask for a sport, a neighbourhood, a vibe, a time or a budget. Try “football turf under 1200 tonight”.`};
  }
  if(/how many (venues|places)/.test(low))return {text:`${COUNT.all} venues: ${COUNT.BLR} in Bengaluru and ${COUNT.MAA} in Chennai, across sports, fitness, pubs, dining, gaming and clubs.`};

  /* booking intent -> tool call */
  if(info.book){
    const v=resolveTarget(info);
    if(!v)return {text:`Which venue should I book? Ask me for a place first, then say “book the first one at 7 PM”.`};
    const pick=pickSlot(v,{date:info.date,wd:info.wd,window:info.window,minute:info.minute});
    if(!pick)return {text:`<strong>${esc(v.name)}</strong> has no open slot that matches. Try a different time, or ask me for alternatives nearby.`,hits:[v.id]};
    const ref=newRef();const amt=slotPrice(v,pick.slot);
    S.lastHits=[v.id];
    return {text:`Held <strong>${pick.slot}</strong> ${esc(dayLabel(pick.iso))} at <strong>${esc(v.name)}</strong> (${esc(v.area)}) for ${inr(amt)}. The hold lasts 10 minutes. Pay to confirm.`,
      tool:{name:'book_venue',args:{venue_id:v.id,date:pick.iso,slot:pick.slot},result:{status:'held',ref,amount_inr:amt,expires_in:'10:00'},order:{venueId:v.id,iso:pick.iso,slot:pick.slot,price:amt,ref}},
      trace:{query:q,hits:[{v,d:0.19}],tool:true}};
  }

  /* retrieval */
  const scored=retrieve(info,scope);
  if(!scored.length){
    return {text:`I couldn't find that among the ${COUNT.all} venues on hoppin. Try a sport, a neighbourhood or a vibe, for example “rooftop beer in Indiranagar” or “board games in Egmore”. You can also switch city above.`,trace:{query:q,hits:[],tool:false}};
  }
  const top=scored[0].s;const hits=scored.filter((x,i)=>i<3&&(x.s>=top*.4)).map(x=>({v:x.v,d:+(0.62-0.4*(x.s/top)+((hashStr(x.v.id)%40)/1000)).toFixed(3)}));
  hits.sort((a,b)=>a.d-b.d);
  S.lastHits=hits.map(h=>h.v.id);
  const first=hits[0].v;const n=nextOpen(first);
  const pick=pickSlot(first,{date:info.date,wd:info.wd,window:info.window,minute:info.minute})||n;
  let t=`${hits.length>1?`Here are ${hits.length} good fits in ${CITY[scope].name}. `:''}<strong>${esc(first.name)}</strong> (${esc(first.area)}) is the closest match: ${inr(first.price)}, rated ${first.rating.toFixed(1)}${pick?`, next open slot ${pick.slot} ${esc(dayLabel(pick.iso))}`:''}.`;
  if(hits.length>1)t+=` Also worth a look: ${hits.slice(1).map(h=>`<strong>${esc(h.v.name)}</strong>`).join(' and ')}.`;
  t+=` Say “book the first one at 7 PM” and I’ll hold it.`;
  return {text:t,hits:hits.map(h=>h.v.id),trace:{query:q,hits,tool:false}};
}
function syncCitySeg(){$$('#chatcity button').forEach(b=>b.classList.toggle('on',b.dataset.cc===S.chatCity));}
function traceHTML(t,tool){
  if(!t)return '';
  return `<details class="trace"><summary>Inspect pipeline</summary><div class="in">
    <div><div class="k">1 · Embed query</div><code>“${esc(t.query)}” → 384-d vector · all-MiniLM-L6-v2</code></div>
    <div><div class="k">2 · match_venues · cosine distance · top ${Math.max(t.hits.length,1)}</div>${t.hits.length?`<table>${t.hits.map(h=>`<tr><td>${h.d.toFixed(3)}</td><td><b>${esc(h.v.name)}</b> <span style="color:var(--muted)">${esc(h.v.area)}</span></td><td>${h.v.id}</td></tr>`).join('')}</table>`:'<code>0 rows above threshold</code>'}</div>
    <div><div class="k">3 · Model</div><code>${tool?`tool_use: book_venue(${esc(JSON.stringify(tool.args))})`:'Answer grounded only in the rows above. No tool call.'}</code></div>
    <div class="note">Demo build: retrieval runs in your browser with a keyword scorer standing in for pgvector, so distances are illustrative.</div></div></details>`;
}
function msgHTML(m,id){
  if(m.role==='u')return `<div class="msg u">${esc(m.text)}</div>`;
  const hits=(m.hits||[]).map(i=>VBY[i]).map(v=>`<button class="hit" data-act="venue" data-id="${v.id}"><span class="th">${coverMedia(v)}</span><span><b>${esc(v.name)}</b><span>${esc(v.area)} · ${inr(v.price)} · ★ ${v.rating.toFixed(1)}</span></span></button>`).join('');
  const tool=m.tool?`<div class="tool"><div class="fn"><em>Tool</em>book_venue() → ${m.tool.result.status}</div><div class="ref">${m.tool.result.ref}</div><button class="btn sm" data-act="pay-hold" data-mi="${id}">Pay ${inr(m.tool.result.amount_inr+FEE)} to confirm</button></div>`:'';
  return `<div class="msg a"><div class="av">h</div><div class="bd"><div class="tx">${m.text}</div>${hits?`<div class="hits">${hits}</div>`:''}${tool}${traceHTML(m.trace,m.tool)}</div></div>`;
}
function scrollBottom(){window.scrollTo({top:document.documentElement.scrollHeight,behavior:reduceMotion?'auto':'smooth'});}
function pushAssistant(m){m.role='a';S.chat.push(m);const s=$('#stream');if(s){s.insertAdjacentHTML('beforeend',msgHTML(m,S.chat.length-1));scrollBottom();}}
async function sendChat(text){
  text=text.trim();if(!text)return;
  S.chat.push({role:'u',text});const s=$('#stream');s.insertAdjacentHTML('beforeend',msgHTML({role:'u',text}));
  const typing=document.createElement('div');typing.className='msg a';typing.innerHTML='<div class="av">h</div><div class="bd"><div class="typing"><i></i><i></i><i></i></div></div>';s.appendChild(typing);scrollBottom();
  
  // Try backend RAG API first
  let res=null;
  try{
    const r=await api('/chat','POST',{
      userId:S.user?.email||'usr_guest',
      city:S.chatCity,
      message:text,
      history:S.chat.map(m=>({role:m.role==='u'?'user':'assistant',content:m.text}))
    });
    if(r&&r.text){
      res={
        text:r.text,
        hits:r.hits||[],
        tool:r.tool,
        trace:r.trace
      };
      if(r.hits&&r.hits.length)S.lastHits=r.hits;
    }
  }catch(e){}

  if(!res)res=answer(text);
  setTimeout(()=>{typing.remove();pushAssistant(res);},reduceMotion?20:350);
}
function chatHTML(){
  const chips=[['🏸','Badminton in Indiranagar'],['⚽','Floodlit football turfs'],['🎲','Board game cafes in Chennai'],['🍻','Craft beer tonight'],['🏃','Sunday run clubs']];
  return `<div class="chat">
    <div class="chat-h"><div><div class="kicker">AI Concierge</div><h1 class="display" style="margin-top:12px">Ask, then go.</h1></div>
      <div class="seg" id="chatcity" role="group" aria-label="City"><button data-act="chatcity" data-cc="BLR">BLR</button><button data-act="chatcity" data-cc="MAA">MAA</button></div></div>
    <div class="chips" id="chips">${chips.map(c=>`<button data-act="chip" data-t="${esc(c[1])}">${c[0]} ${c[1]}</button>`).join('')}</div>
    <div class="stream" id="stream" aria-live="polite"></div>
  </div>
  <div class="inbar"><form id="chatForm" autocomplete="off"><label class="sr" for="chatIn">Message the concierge</label><input id="chatIn" placeholder="Ask for a place, a time, a budget…"><button class="btn" type="submit">Send</button></form></div>`;
}

/* =========================================================
   PASSPORT
   ========================================================= */
function bookingsHTML(){
  return `<div class="pp"><div class="kicker">My bookings</div><h1 class="display">Your tickets</h1><div id="ppbody"></div></div>${footerHTML()}`;
}
async function renderBookings(){
  if(S.user){
    const bRes=await api('/bookings?email='+encodeURIComponent(S.user.email));
    if(bRes&&Array.isArray(bRes.bookings)){
      store.set('hoppin.bookings:'+S.user.email,bRes.bookings);
    }
  }
  const list=bookings(),up=list.filter(b=>!isPastB(b)),pa=list.filter(isPastB),sv=saved().map(id=>VBY[id]).filter(Boolean);
  const row=b=>{const v=VBY[b.venueId];return `<button class="trow" data-act="ticket" data-i="${list.indexOf(b)}"><span class="th">${coverMedia(v)}</span><span><b>${esc(v.name)}</b><span>${esc(dayTitle(b.iso))} · ${b.slot} · ${esc(v.area)}</span></span><span class="rf">${b.ref}<br><span style="font-family:var(--sans);letter-spacing:0">${inr(b.total)}</span></span></button>`;};
  const sec=(t,a)=>a.length?`<div class="kicker" style="margin:26px 0 12px">${t}</div><div class="tlist">${a.map(row).join('')}</div>`:'';
  $('#ppbody').innerHTML=`<p style="color:var(--muted);margin:-14px 0 24px">${esc(S.user.name)} · ${esc(S.user.email)}</p>
  <div class="stats"><div class="stat"><b>${up.length}</b><span>Upcoming</span></div><div class="stat"><b>${pa.length}</b><span>Past</span></div><div class="stat"><b>${sv.length}</b><span>Saved</span></div><div class="stat"><b>${inr(list.reduce((t,b)=>t+b.total,0))}</b><span>Spent</span></div></div>
  ${list.length?sec('Upcoming',up)+sec('Past',pa):`<div class="empty" style="grid-column:auto"><h3>No tickets yet</h3><p>Book a slot and your ticket will show up here.</p><a class="btn" href="#/">Find a place</a></div>`}
  ${sv.length?`<div class="kicker" style="margin:34px 0 12px">Saved places</div><div class="hits">${sv.map(v=>`<button class="hit" data-act="venue" data-id="${v.id}"><span class="th">${coverMedia(v)}</span><span><b>${esc(v.name)}</b><span>${esc(v.area)} · ${inr(v.price)}</span></span></button>`).join('')}</div>`:''}
  <div style="margin-top:40px"><button class="btn ghost" data-act="signout">Sign out</button></div>`;
}

/* =========================================================
   ROUTER + RENDER
   ========================================================= */
let ROUTE=null;
function curPath(){return ROUTE!=null?ROUTE:(location.hash.replace(/^#/,'')||'/');}
function go(p){ROUTE=p;try{if(location.hash!=='#'+p)location.hash=p;}catch(e){}render();}
function parseRoute(){const p=curPath().split('/').filter(Boolean);
  if(p[0]==='chat')return {view:'chat'};if(p[0]==='bookings'||p[0]==='passport')return {view:'bookings'};
  if(p[0]==='cat'&&CATS[p[1]])return {view:'discover',cat:p[1]};return {view:'discover'};}
function render(){
  const r=parseRoute();
  if((r.view==='chat'||r.view==='bookings')&&!S.user){
    const target=curPath();ROUTE='/';try{location.hash='/';}catch(e){}
    S.view='discover';renderView(parseRoute());
    S.pending=()=>go(target);
    showAuth('in',r.view==='chat'?'Sign in to chat with the AI Concierge.':'Sign in to see your bookings.');return;
  }
  renderView(r);
}
let lastKey='';
function renderView(r){
  S.view=r.view;document.body.classList.toggle('is-chat',r.view==='chat');
  $('#floatcta').style.display=(r.view==='discover'&&innerWidth>=768)?'':'none';
  const app=$('#app');
  if(r.view==='discover'){
    const key='discover';
    if(r.cat)S.cat=r.cat;
    if(lastKey!==key||!$('#grid')){app.innerHTML=discoverHTML();$('#sort').value=S.sort;$('#fprice').value=S.maxp;$('#frate').value=S.minr;bindDiscover();startClock();}
    renderGrid();
    if(r.cat){setTimeout(()=>{const e=$('#explore');e&&e.scrollIntoView({behavior:reduceMotion?'auto':'smooth'});},60);}
    else if(lastKey!==key)window.scrollTo(0,0);
    lastKey=key;
  }else if(r.view==='chat'){
    lastKey='chat';clearInterval(clockT);app.innerHTML=chatHTML();syncCitySeg();
    if(!S.chat.length)S.chat.push({role:'a',text:`Hi ${esc(S.user.name.split(' ')[0])}. I only know the ${COUNT.all} venues on hoppin, so every answer is grounded in real listings. Ask me for a place, a time or a budget, or tap a prompt above.`});
    $('#stream').innerHTML=S.chat.map((m,i)=>msgHTML(m,i)).join('');window.scrollTo(0,0);
  }else{
    lastKey='bookings';clearInterval(clockT);app.innerHTML=bookingsHTML();renderBookings();window.scrollTo(0,0);
  }
  navActive();
}
function bindDiscover(){
  motion();
  $('#q').addEventListener('input',e=>{S.q=e.target.value;renderGrid();});
  $('#sort').addEventListener('change',e=>{S.sort=e.target.value;if(S.sort==='near'&&!S.geo)return getGeo();renderGrid();});
  $('#fprice').addEventListener('change',e=>{S.maxp=+e.target.value;renderGrid();});
  $('#frate').addEventListener('change',e=>{S.minr=+e.target.value;renderGrid();});
}
window.addEventListener('hashchange',()=>{const h=location.hash.replace(/^#/,'')||'/';if(h==='explore'||h===ROUTE)return;ROUTE=h;render();});
window.addEventListener('resize',()=>{if(S.view==='discover')$('#floatcta').style.display=innerWidth>=768?'':'none';});

/* =========================================================
   EVENT DELEGATION
   ========================================================= */
document.addEventListener('click',e=>{
  if(!e.target.closest('#palmenu')&&!e.target.closest('#palBtn'))$('#palmenu').classList.remove('open');
  const lk=e.target.closest('a[href^="#/"]');if(lk){e.preventDefault();go(lk.getAttribute('href').slice(1));return;}
  const sc=e.target.closest('[data-scroll]');
  if(sc){e.preventDefault();const t=document.getElementById(sc.dataset.scroll);t&&t.scrollIntoView({behavior:reduceMotion?'auto':'smooth'});return;}
  const a=e.target.closest('[data-act]');if(!a)return;
  const act=a.dataset.act;
  switch(act){
    case 'theme':toggleTheme();break;
    case 'palmenu':$('#palmenu').classList.toggle('open');break;
    case 'pal':applyPalette(a.dataset.k,true);$('#palmenu').classList.remove('open');toast('Palette: '+PAL[a.dataset.k].name);break;
    case 'account':if(S.user)go('/bookings');else{S.pending=null;showAuth('in');}break;
    case 'close':M.close();break;
    case 'auth-tab':showAuth(a.dataset.tab,$('.pad .lead')&&$('.pad .lead').textContent);break;
    case 'demo-login':{(async()=>{
      const res=await api('/auth/guest','POST');
      const u=res?.user||{email:'guest@hoppin.demo',name:'Guest'};
      finishAuth(u);
    })();break;}
    case 'venue':openVenue(a.dataset.id);break;
    case 'city':S.city=a.dataset.city;renderGrid();break;
    case 'cat':S.cat=a.dataset.cat;renderGrid();break;
    case 'catgo':S.cat=a.dataset.cat;renderGrid();$('#explore').scrollIntoView({behavior:reduceMotion?'auto':'smooth'});break;
    case 'tonight-on':S.tonight=true;renderGrid();$('#explore').scrollIntoView({behavior:reduceMotion?'auto':'smooth'});break;
    case 'tonight-off':S.tonight=false;renderGrid();break;
    case 'reset':S.city='all';S.cat='all';S.q='';S.tonight=false;S.maxp=0;S.minr=0;$('#q').value='';$('#fprice').value=0;$('#frate').value=0;renderGrid();break;
    case 'tonight-toggle':S.tonight=!S.tonight;renderGrid();break;
    case 'day':B.iso=a.dataset.iso;B.slot=null;renderBooking();break;
    case 'slot':B.slot=a.dataset.slot;renderBooking();break;
    case 'reserve':{const v=VBY[B.id];if(B.resched){reschedule(B.resched,B.iso,B.slot);break;}showCheckout({venueId:B.id,iso:B.iso,slot:B.slot,price:slotPrice(v,B.slot)});break;}
    case 'back-venue':{const o=showCheckout.order;showVenue(o.venueId,{iso:o.iso,slot:o.slot});break;}
    case 'to-bookings':M.close();go('/bookings');break;
    case 'ticket':showTicket(bookings()[+a.dataset.i],false);break;
    case 'signout':signOut();break;
    case 'chatcity':S.chatCity=a.dataset.cc;syncCitySeg();break;
    case 'chip':sendChat(a.dataset.t);break;
    case 'save':{const id=a.dataset.id;let l=saved();const on=!l.includes(id);l=on?[...l,id]:l.filter(x=>x!==id);store.set('hoppin.saved',l);api('/saved/toggle','POST',{email:S.user?.email||'guest@hoppin.demo',venueId:id});a.classList.toggle('on',on);a.setAttribute('aria-pressed',on);toast(on?'Saved to your list':'Removed from saved');if(S.cat==='saved')renderGrid();break;}
    case 'cancel':{if(a.dataset.arm!=='1'){a.dataset.arm='1';a.textContent='Tap again to cancel';break;}
      api('/bookings/'+encodeURIComponent(a.dataset.ref)+'/cancel','POST');
      const k='hoppin.bookings:'+S.user.email;store.set(k,store.get(k,[]).filter(x=>x.ref!==a.dataset.ref));M.close();toast('Booking cancelled. Refund in 3 to 5 days (demo).');if(S.view==='bookings')renderBookings();else renderGrid&&S.view==='discover'&&renderGrid();break;}
    case 'promo':{(async()=>{
      const o=showCheckout.order,c=$('#pcode').value.trim().toUpperCase();
      const pRes=await api('/promos/apply','POST',{code:c,amount:o.price});
      if(pRes&&pRes.valid){
        o.disc=pRes.discount;
        o.total=o.price+o.fee-o.disc;
        $('#lines').innerHTML=linesHTML(o);
        $('#payBtn span').textContent='Pay '+inr(o.total);
        toast('Code applied: '+c+' ('+pRes.description+')');
        return;
      }
      const P={HOPPIN20:o.price*.2,FIRST50:50,CREW100:100};
      if(!P[c]){toast('That code is not valid.');return;}
      o.disc=Math.round(Math.min(P[c],o.price));o.total=o.price+o.fee-o.disc;
      $('#lines').innerHTML=linesHTML(o);$('#payBtn span').textContent='Pay '+inr(o.total);toast('Code applied: '+c);
    })();break;}
    case 'crewn':{const n=Math.min(12,Math.max(2,+$('#crewn').textContent+ +a.dataset.d));$('#crewn').textContent=n;$('#crewamt').textContent=inr(a.closest('.crew').dataset.total/n);break;}
    case 'share':{const b=bookings().find(x=>x.ref===a.dataset.ref),v=VBY[b.venueId],n=+$('#crewn').textContent;const t=`Join me at ${v.name} (${v.area}) · ${dayTitle(b.iso)}, ${b.slot} · ${inr(b.total/n)} each. Booked on hoppin. Ref ${b.ref}`;
      (async()=>{try{if(navigator.share){await navigator.share({title:'hoppin. invite',text:t});return;}}catch(x){if(x.name==='AbortError')return;}try{await navigator.clipboard.writeText(t);toast('Invite copied');}catch(x){const ta=$('#sharetxt');ta.hidden=false;ta.value=t;ta.select();toast('Copy the invite text below');}})();break;}
    case 'rate':{api('/bookings/'+encodeURIComponent(a.dataset.ref)+'/rate','POST',{rating:+a.dataset.n});const R=store.get('hoppin.reviews',{});R[a.dataset.ref]=+a.dataset.n;store.set('hoppin.reviews',R);$$('#rstars .pill').forEach((x,i)=>x.classList.toggle('on',i<+a.dataset.n));toast('Thanks for rating');break;}
    case 'resched':{const b=bookings().find(x=>x.ref===a.dataset.ref);showVenue(b.venueId);B.resched=b.ref;renderBooking();toast('Pick a new day and time');break;}
    case 'rebook':{const id=a.dataset.id;M.close();setTimeout(()=>showVenue(id),260);break;}
    case 'pay-hold':{const m=S.chat[+a.dataset.mi];if(m&&m.tool)showCheckout({...m.tool.order});break;}
  }
});

document.addEventListener('submit',e=>{
  const f=e.target;
  if(f.id==='authForm'){e.preventDefault();submitAuth(f);}
  else if(f.id==='payForm'){e.preventDefault();submitPay(f);}
  else if(f.id==='heroForm'){e.preventDefault();S.q=$('#hq').value;S.cat='all';S.city='all';S.tonight=false;$('#q').value=S.q;renderGrid();$('#explore').scrollIntoView({behavior:reduceMotion?'auto':'smooth'});}
  else if(f.id==='chatForm'){e.preventDefault();const i=$('#chatIn');const t=i.value;i.value='';sendChat(t);}
});
document.addEventListener('input',e=>{
  const t=e.target;
  if(t.name==='card'){const d=t.value.replace(/\D/g,'').slice(0,19);t.value=d.replace(/(.{4})/g,'$1 ').trim();}
  if(t.name==='exp'){let d=t.value.replace(/\D/g,'').slice(0,4);if(d.length>2)d=d.slice(0,2)+' / '+d.slice(2);t.value=d;}
  if(t.name==='cvc')t.value=t.value.replace(/\D/g,'').slice(0,4);
});

document.addEventListener('keydown',e=>{if(e.key==='Enter'&&e.target.classList&&e.target.classList.contains('card'))e.target.click();});
loader();
render();
})();
</script>
</body>
</html>
'''

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
      f.write(html_content)
    print(f"Successfully wrote {len(html_content)} bytes to {t}")
  except Exception as e:
    print(f"Error writing {t}: {e}")
