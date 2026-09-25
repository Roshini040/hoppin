import re

with open('build_hoppin_with_images.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add api helper right after toast function
api_helper = '''const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
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
}'''

code = code.replace(
    '''const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
function toast(msg){const t=$('#toast');t.textContent=msg;t.classList.add('show');clearTimeout(toast._t);toast._t=setTimeout(()=>t.classList.remove('show'),2400);}''',
    api_helper
)


# 2. Update submitAuth to be async and call backend
old_submit_auth = '''function submitAuth(form){
  const mode=form.dataset.mode;const fd=new FormData(form);
  const email=String(fd.get('email')||'').trim().toLowerCase();const pw=String(fd.get('pw')||'');const name=String(fd.get('name')||'').trim();
  const err=m=>{$('#autherr').textContent=m;};
  if(!/^\S+@\S+\.\S+$/.test(email))return err('Enter a valid email address.');
  if(pw.length<6)return err('Password needs at least 6 characters.');
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
}'''

new_submit_auth = '''async function submitAuth(form){
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
}'''

code = code.replace(old_submit_auth, new_submit_auth)

# 3. Update submitPay to call backend API
old_submit_pay = '''    const bk={ref:o.ref||newRef(),venueId:o.venueId,iso:o.iso,slot:o.slot,price:o.price,fee:o.fee,total:o.total,at:Date.now(),last4:num.slice(-4)};
    const list=store.get('hoppin.bookings:'+S.user.email,[]);list.unshift(bk);store.set('hoppin.bookings:'+S.user.email,list);
    showTicket(bk,true);
    if(S.view==='chat'){pushAssistant({text:`Payment received. <strong>${esc(VBY[bk.venueId].name)}</strong> is confirmed for ${esc(dayLabel(bk.iso))} at ${bk.slot}. Your ticket is in My bookings.`});}
    if(S.view==='bookings')renderBookings();'''

new_submit_pay = '''    (async()=>{
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
    })();'''

code = code.replace(old_submit_pay, new_submit_pay)

# 4. Update sendChat to call backend RAG API
old_send_chat = '''function sendChat(text){
  text=text.trim();if(!text)return;
  S.chat.push({role:'u',text});const s=$('#stream');s.insertAdjacentHTML('beforeend',msgHTML({role:'u',text}));
  const typing=document.createElement('div');typing.className='msg a';typing.innerHTML='<div class="av">h</div><div class="bd"><div class="typing"><i></i><i></i><i></i></div></div>';s.appendChild(typing);scrollBottom();
  const res=answer(text);
  setTimeout(()=>{typing.remove();pushAssistant(res);},reduceMotion?50:650);
}'''

new_send_chat = '''async function sendChat(text){
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
}'''

code = code.replace(old_send_chat, new_send_chat)

# 5. Update renderBookings to sync from backend
old_render_bookings = '''function renderBookings(){
  const list=bookings(),up=list.filter(b=>!isPastB(b)),pa=list.filter(isPastB),sv=saved().map(id=>VBY[id]).filter(Boolean);'''

new_render_bookings = '''async function renderBookings(){
  if(S.user){
    const bRes=await api('/bookings?email='+encodeURIComponent(S.user.email));
    if(bRes&&Array.isArray(bRes.bookings)){
      store.set('hoppin.bookings:'+S.user.email,bRes.bookings);
    }
  }
  const list=bookings(),up=list.filter(b=>!isPastB(b)),pa=list.filter(isPastB),sv=saved().map(id=>VBY[id]).filter(Boolean);'''

code = code.replace(old_render_bookings, new_render_bookings)

# 6. Update demo-login and other actions to call backend
old_demo = '''case 'demo-login':{const users=store.get('hoppin.users',{});if(!users['guest@hoppin.demo']){users['guest@hoppin.demo']={name:'Guest',pw:btoa('guest-demo')};store.set('hoppin.users',users);}finishAuth({email:'guest@hoppin.demo',name:'Guest'});break;}'''

new_demo = '''case 'demo-login':{(async()=>{
      const res=await api('/auth/guest','POST');
      const u=res?.user||{email:'guest@hoppin.demo',name:'Guest'};
      finishAuth(u);
    })();break;}'''

code = code.replace(old_demo, new_demo)

# Update reschedule action
old_resched = '''function reschedule(ref,iso,slot){const k='hoppin.bookings:'+S.user.email,l=store.get(k,[]),b=l.find(x=>x.ref===ref);if(!b)return;b.iso=iso;b.slot=slot;store.set(k,l);toast('Booking moved. Any price difference is settled at the venue.');showTicket(b,false);if(S.view==='bookings')renderBookings();}'''

new_resched = '''async function reschedule(ref,iso,slot){
  api('/bookings/'+encodeURIComponent(ref)+'/reschedule','POST',{iso,slot});
  const k='hoppin.bookings:'+S.user.email,l=store.get(k,[]),b=l.find(x=>x.ref===ref);
  if(!b)return;b.iso=iso;b.slot=slot;store.set(k,l);
  toast('Booking moved. Any price difference is settled at the venue.');
  showTicket(b,false);if(S.view==='bookings')renderBookings();
}'''

code = code.replace(old_resched, new_resched)

# Update cancel action
old_cancel = '''case 'cancel':{if(a.dataset.arm!=='1'){a.dataset.arm='1';a.textContent='Tap again to cancel';break;}
      const k='hoppin.bookings:'+S.user.email;store.set(k,store.get(k,[]).filter(x=>x.ref!==a.dataset.ref));M.close();toast('Booking cancelled. Refund in 3 to 5 days (demo).');if(S.view==='bookings')renderBookings();else renderGrid&&S.view==='discover'&&renderGrid();break;}'''

new_cancel = '''case 'cancel':{if(a.dataset.arm!=='1'){a.dataset.arm='1';a.textContent='Tap again to cancel';break;}
      api('/bookings/'+encodeURIComponent(a.dataset.ref)+'/cancel','POST');
      const k='hoppin.bookings:'+S.user.email;store.set(k,store.get(k,[]).filter(x=>x.ref!==a.dataset.ref));M.close();toast('Booking cancelled. Refund in 3 to 5 days (demo).');if(S.view==='bookings')renderBookings();else renderGrid&&S.view==='discover'&&renderGrid();break;}'''

code = code.replace(old_cancel, new_cancel)

# Update rate action
old_rate = '''case 'rate':{const R=store.get('hoppin.reviews',{});R[a.dataset.ref]=+a.dataset.n;store.set('hoppin.reviews',R);$$('#rstars .pill').forEach((x,i)=>x.classList.toggle('on',i<+a.dataset.n));toast('Thanks for rating');break;}'''

new_rate = '''case 'rate':{api('/bookings/'+encodeURIComponent(a.dataset.ref)+'/rate','POST',{rating:+a.dataset.n});const R=store.get('hoppin.reviews',{});R[a.dataset.ref]=+a.dataset.n;store.set('hoppin.reviews',R);$$('#rstars .pill').forEach((x,i)=>x.classList.toggle('on',i<+a.dataset.n));toast('Thanks for rating');break;}'''

code = code.replace(old_rate, new_rate)

# Update save action
old_save = '''case 'save':{const id=a.dataset.id;let l=saved();const on=!l.includes(id);l=on?[...l,id]:l.filter(x=>x!==id);store.set('hoppin.saved',l);a.classList.toggle('on',on);a.setAttribute('aria-pressed',on);toast(on?'Saved to your list':'Removed from saved');if(S.cat==='saved')renderGrid();break;}'''

new_save = '''case 'save':{const id=a.dataset.id;let l=saved();const on=!l.includes(id);l=on?[...l,id]:l.filter(x=>x!==id);store.set('hoppin.saved',l);api('/saved/toggle','POST',{email:S.user?.email||'guest@hoppin.demo',venueId:id});a.classList.toggle('on',on);a.setAttribute('aria-pressed',on);toast(on?'Saved to your list':'Removed from saved');if(S.cat==='saved')renderGrid();break;}'''

code = code.replace(old_save, new_save)

# Update promo action
old_promo = '''case 'promo':{const o=showCheckout.order,c=$('#pcode').value.trim().toUpperCase(),P={HOPPIN20:o.price*.2,FIRST50:50,CREW100:100};if(!P[c]){toast('That code is not valid.');break;}o.disc=Math.round(Math.min(P[c],o.price));o.total=o.price+o.fee-o.disc;$('#lines').innerHTML=linesHTML(o);$('#payBtn span').textContent='Pay '+inr(o.total);toast('Code applied: '+c);break;}'''

new_promo = '''case 'promo':{(async()=>{
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
    })();break;}'''

code = code.replace(old_promo, new_promo)

with open('build_hoppin_with_images.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_hoppin_with_images.py successfully!")
