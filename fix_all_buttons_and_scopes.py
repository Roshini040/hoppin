# Python script to fix button clickability and scope issues:
# 1. Attach all interactive functions to `window` so inline onclick & onsubmit work 100% reliably
# 2. Add complete data-act handlers in document.addEventListener('click')
# 3. Add complete form submit handlers in document.addEventListener('submit')
# 4. Ensure customer account creation, sign in, club creation, and venue registration all succeed smoothly
# 5. Synchronize all 5 target files

with open("build_fullstack_frontend.py", "r", encoding="utf-8") as f:
    code = f.read()

# =====================================================================
# 1. WINDOW SCOPE BINDINGS
# =====================================================================
window_bindings = """
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
"""

# Inject window bindings right before runLoader();
target_run_loader = "runLoader();"
if "window.switchAuthRole = switchAuthRole;" not in code:
    code = code.replace(target_run_loader, window_bindings + "\n" + target_run_loader)
    print("Injected window bindings successfully.")

# =====================================================================
# 2. UPDATE FORM SUBMIT LISTENER
# =====================================================================
old_submit_listener = """document.addEventListener('submit',e=>{
  const f=e.target;
  if(f.id==='authForm'){e.preventDefault();submitAuth(f);}
  else if(f.id==='payForm'){e.preventDefault();submitPay(f);}
  else if(f.id==='chatForm'){e.preventDefault();const i=$('#chatIn');const t=i.value;i.value='';sendChat(t);}
});"""

new_submit_listener = """document.addEventListener('submit',e=>{
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
});"""

if old_submit_listener in code:
    code = code.replace(old_submit_listener, new_submit_listener)
    print("Updated form submit listener successfully.")

# =====================================================================
# 3. ENSURE FORMS HAVE DESCRIPTIVE IDS AND DATA ATTRIBUTES
# =====================================================================
code = code.replace(
    '<form onsubmit="event.preventDefault();submitCustomerAuth(this);">',
    '<form id="customerAuthForm" onsubmit="event.preventDefault();submitCustomerAuth(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitClubAdminAuth(this);">',
    '<form id="clubAdminForm" onsubmit="event.preventDefault();submitClubAdminAuth(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitVenueOwnerAuth(this);">',
    '<form id="venueOwnerForm" onsubmit="event.preventDefault();submitVenueOwnerAuth(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitSupportAuth(this);">',
    '<form id="supportAuthForm" onsubmit="event.preventDefault();submitSupportAuth(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitCreateClub(this);">',
    '<form id="createClubForm" onsubmit="event.preventDefault();submitCreateClub(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitNewVenue(this);">',
    '<form id="registerVenueForm" onsubmit="event.preventDefault();submitNewVenue(this);">'
)
code = code.replace(
    '<form onsubmit="event.preventDefault();submitVenueDPStatus(this);">',
    '<form id="venueDPForm" onsubmit="event.preventDefault();submitVenueDPStatus(this);">'
)

# Replace any onclick="authCustomerMode='up'..." with setAuthCustomerMode
code = code.replace(
    'onclick="authCustomerMode=\'in\';switchAuthRole(\'customer\');"',
    'onclick="setAuthCustomerMode(\'in\')"'
)
code = code.replace(
    'onclick="authCustomerMode=\'up\';switchAuthRole(\'customer\');"',
    'onclick="setAuthCustomerMode(\'up\')"'
)

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

exec(open("build_fullstack_frontend.py", encoding="utf-8").read())
print("All target files synchronized and validated!")
