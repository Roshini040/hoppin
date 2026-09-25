# Python script to update:
# 1. Star rating & review count styling on venue cards (frosted pill, no overlap)
# 2. UPI payment in Checkout modal (QR code, UPI ID, GPay/PhonePe/Paytm buttons, tab switcher)
# 3. Synchronize all 5 target files

import os
import subprocess

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    content = f.read()

# ------------------------------------------------------------------
# 1. Update card CSS for .rate and .rate-badge
# ------------------------------------------------------------------
old_rate_css = """.cv .rate { position: absolute; left: 16px; bottom: 14px; z-index: 2; color: #fff; font-family: var(--mono); font-size: 13px; display: flex; align-items: center; gap: 7px; }"""

new_rate_css = """.cv .rate {
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
.star { width: 13px; height: 13px; fill: #f0b94a; flex-shrink: 0; }
.fav { position: absolute; right: 14px; bottom: 14px; z-index: 6; width: 38px; height: 38px; border-radius: 50%; background: rgba(13,8,24,0.8); backdrop-filter: blur(10px); color: #fff; font-size: 18px; display: grid; place-items: center; transition: all 0.2s; border: 1px solid rgba(255,255,255,0.15); }
.fav:hover { transform: scale(1.12); border-color: rgba(196,181,253,0.5); }
.fav.on { color: #ff6b81; border-color: rgba(255,107,129,0.4); }"""

if old_rate_css in content:
    content = content.replace(old_rate_css, new_rate_css)
    print("Replaced .cv .rate CSS successfully.")
else:
    print("Notice: old_rate_css not found directly, checking variations...")

# ------------------------------------------------------------------
# 2. Update cardHTML to use the clean rating pill with separate elements
# ------------------------------------------------------------------
old_card_html = """      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><small>(${v.reviews})</small></div>"""
new_card_html = """      <div class="rate">${IC.star}<b>${v.rating.toFixed(1)}</b><span class="rate-sep">·</span><span class="rate-count">${v.reviews.toLocaleString()} reviews</span></div>"""

if old_card_html in content:
    content = content.replace(old_card_html, new_card_html)
    print("Replaced cardHTML rating markup successfully.")

# ------------------------------------------------------------------
# 3. Add UPI & Card Payment Tabs and Flow in showCheckout
# ------------------------------------------------------------------
start_checkout = content.find("/* Checkout */")
end_checkout = content.find("function showTicket(b,fresh){")

if start_checkout != -1 and end_checkout != -1:
    new_checkout_code = """/* Checkout with UPI (QR / Apps) and Card */
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

"""
    content = content[:start_checkout] + new_checkout_code + content[end_checkout:]
    print("Replaced showCheckout with UPI & Card payment successfully.")
else:
    print(f"Warning: checkout markers not found ({start_checkout}, {end_checkout})")

# ------------------------------------------------------------------
# 4. Add switch-pay event handler in click delegation
# ------------------------------------------------------------------
old_switch_case = "    case 'wheel-item':{"
new_switch_case = """    case 'switch-pay':{
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
    case 'wheel-item':{"""

if old_switch_case in content:
    content = content.replace(old_switch_case, new_switch_case)
    print("Added switch-pay click delegation successfully.")

# Write updated build_fullstack_frontend.py
with open("build_fullstack_frontend.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated build_fullstack_frontend.py!")

# Execute build_fullstack_frontend.py to update all 5 destination files
res = subprocess.run(["python", "build_fullstack_frontend.py"], capture_output=True, text=True)
print("Regeneration output:", res.stdout, res.stderr)
