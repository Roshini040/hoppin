import os, re, json

# Read build_hoppin_with_images.py to extract RAW, CATS, CITY, AREA, VENUE_IMG
with open('build_hoppin_with_images.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract VENUE_IMG dictionary
m_img = re.search(r'const VENUE_IMG = \{([\s\S]*?)\n\};', content)
venue_img_text = m_img.group(0) if m_img else "const VENUE_IMG = {};"

# Let's create server/src/services/store.ts
store_ts = '''import fs from 'fs';
import path from 'path';

export interface Venue {
  id: string;
  name: string;
  city: 'BLR' | 'MAA';
  cityName: 'Bengaluru' | 'Chennai';
  area: string;
  cat: 'sports' | 'fitness' | 'pubs' | 'dining' | 'gaming' | 'clubs';
  tags: string[];
  price: number;
  rating: number;
  reviews: number;
  lat: number;
  lng: number;
  slots: string[];
  days: number[] | null;
  desc: string;
  image: string;
  added?: boolean;
}

export interface User {
  id: string;
  email: string;
  name: string;
  passwordHash: string;
  createdAt: number;
}

export interface Booking {
  id: string; // Ref e.g. HP-XXXXXX
  ref: string;
  userId?: string;
  userEmail: string;
  userName?: string;
  venueId: string;
  venueName: string;
  cityName: string;
  area: string;
  iso: string;
  slot: string;
  partySize: number;
  price: number;
  fee: number;
  disc: number;
  total: number;
  status: 'upcoming' | 'past' | 'cancelled';
  createdAt: number;
  last4?: string;
  rating?: number;
}

export interface Review {
  id: string;
  bookingRef: string;
  venueId: string;
  userEmail: string;
  rating: number;
  comment?: string;
  createdAt: number;
}

export interface SlotAvailability {
  slot: string;
  state: 'open' | 'few' | 'full' | 'past' | 'yours';
  price: number;
  left?: number;
}

''' + venue_img_text + '''

const CITY = {
  BLR: { name: 'Bengaluru', short: 'BLR' },
  MAA: { name: 'Chennai', short: 'MAA' }
};

const CATS = {
  sports: {
    label: 'Sports & Turfs',
    price: [600, 2000],
    slots: ['06:00 AM', '07:00 AM', '09:00 AM', '05:00 PM', '06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM'],
    desc: (n: string) => `Hourly slots to play with your crew. Pick a time, turn up in your kit and the pitch is yours.`
  },
  fitness: {
    label: 'Fitness & Gyms',
    price: [400, 1500],
    slots: ['06:00 AM', '07:00 AM', '09:00 AM', '12:00 PM', '05:00 PM', '07:00 PM'],
    desc: (n: string) => `Book a session or a day pass and train on your schedule.`
  },
  pubs: {
    label: 'Pubs & Brews',
    price: [500, 1200],
    slots: ['12:00 PM', '04:00 PM', '06:00 PM', '07:30 PM', '09:00 PM', '10:30 PM'],
    desc: (n: string) => `Reserve a table for your group. Arrive, order a round, stay a while.`
  },
  dining: {
    label: 'Dining & Cafes',
    price: [500, 1000],
    slots: ['08:00 AM', '12:30 PM', '04:00 PM', '07:00 PM', '08:30 PM'],
    desc: (n: string) => `Book a table ahead so you can walk straight in.`
  },
  gaming: {
    label: 'Gaming & Arcades',
    price: [400, 1200],
    slots: ['11:00 AM', '01:00 PM', '03:00 PM', '05:00 PM', '07:00 PM', '09:00 PM'],
    desc: (n: string) => `Grab a two-hour block with friends. Screens are optional, dice are not.`
  },
  clubs: {
    label: 'Clubs & Runs',
    price: [400, 600],
    slots: ['05:30 AM', '06:00 AM', '06:30 PM'],
    desc: (n: string) => `Show up, meet the group, move together. A community event, not a class.`
  }
};

const AREA: Record<string, [number, number]> = {
  'Indiranagar': [12.9784, 77.6408],
  'Koramangala': [12.9352, 77.6245],
  'Whitefield': [12.9698, 77.7500],
  'Central Bengaluru': [12.9716, 77.5946],
  'Bengaluru': [12.9716, 77.5946],
  'Cubbon Park': [12.9763, 77.5929],
  'Bidadi': [12.8330, 77.4030],
  'Kilpauk': [13.0836, 80.2420],
  'T. Nagar': [13.0418, 80.2341],
  'Velachery': [12.9815, 80.2180],
  'Vanagaram': [13.0500, 80.1500],
  'Thiruvanmiyur': [12.9830, 80.2594],
  'Puzhuthivakkam': [12.9700, 80.1900],
  'Chromepet': [12.9516, 80.1462],
  'Anna Nagar': [13.0850, 80.2101],
  'OMR': [12.9000, 80.2270],
  'Perungudi': [12.9650, 80.2461],
  'Adyar': [13.0012, 80.2565],
  'Alwarpet': [13.0339, 80.2510],
  'Egmore': [13.0732, 80.2609],
  'Porur': [13.0382, 80.1565],
  'Mylapore': [13.0368, 80.2676],
  'Besant Nagar': [13.0002, 80.2707],
  'Nungambakkam': [13.0569, 80.2425],
  'Periamet': [13.0827, 80.2707],
  'Guindy': [13.0067, 80.2206],
  'Chennai': [13.0827, 80.2707],
  "Elliot's Beach": [13.0002, 80.2707],
  'Velachery Mall': [12.9807, 80.2185]
};

const RAW: Array<[string, 'BLR' | 'MAA', string, keyof typeof CATS, string[], string?, any?]> = [
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
  ['SDAT Tennis Stadium','MAA','Nungambakkam','sports',['Tennis','Hard courts','Outdoor'],undefined,{added:true}],
  ['Nehru Indoor Stadium','MAA','Periamet','sports',['Indoor','Multi-sport','Badminton'],undefined,{added:true}],
  ['Cult Adyar','MAA','Adyar','fitness',['Group classes','Strength','Gym']],
  ['Cult Alwarpet','MAA','Alwarpet','fitness',['Group classes','Strength','Gym']],
  ['Cult T. Nagar','MAA','T. Nagar','fitness',['Group classes','Strength','Gym']],
  ["Women's Gym · Adyar",'MAA','Adyar','fitness',['Women-only','Gym','Training']],
  ['The Madras Taproom','MAA','Egmore','pubs',['Taproom','Craft beer','Groups']],
  ["Watson's",'MAA','T. Nagar','pubs',['Bar','Drinks','Groups']],
  ['Shout Bar & Cafe','MAA','Porur','pubs',['Bar','Cafe','Groups']],
  ['Slounge (Lemon Tree Shimona)','MAA','Guindy','pubs',['Lounge','Hotel bar','Cocktails']],
  ['The Alwarpet Taproom','MAA','Alwarpet','pubs',['Taproom','Craft beer','Groups'],undefined,{added:true}],
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

function hashStr(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function rng(seed: number) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const roundTo = (n: number, s: number) => Math.round(n / s) * s;

export function buildDefaultVenues(): Venue[] {
  return RAW.map((r, i) => {
    const [name, city, area, cat, tags, desc, o] = r;
    const C = CATS[cat];
    const R = rng(hashStr(name));
    const opt = o || {};
    const ac = AREA[area] || AREA[CITY[city].name];
    const [p0, p1] = C.price;
    const price = roundTo(p0 + R() * (p1 - p0), cat === 'clubs' ? 50 : 50);
    const rating = Math.round((4.1 + Math.pow(R(), 0.8) * 0.9) * 10) / 10;
    const image = (VENUE_IMG as Record<string, string>)[name] || 'https://images.unsplash.com/photo-1540497077202-7c8a3999166f?auto=format&fit=crop&w=900&q=80';
    return {
      id: 'v' + String(i + 1).padStart(2, '0'),
      name,
      city,
      cityName: CITY[city].name as 'Bengaluru' | 'Chennai',
      area,
      cat,
      tags,
      price,
      rating,
      reviews: Math.round(40 + Math.pow(R(), 1.6) * 1760),
      lat: +(ac[0] + (R() - .5) * .012).toFixed(5),
      lng: +(ac[1] + (R() - .5) * .012).toFixed(5),
      slots: opt.slots || C.slots,
      days: opt.days || null,
      added: !!opt.added,
      desc: desc || (name + ' in ' + area + '. ' + C.desc(name)),
      image
    };
  });
}

export function toISO(d: Date): string {
  return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
}

export function fromISO(s: string): Date {
  const [y, m, d] = s.split('-').map(Number);
  return new Date(y, m - 1, d);
}

export function todayISO(): string {
  return toISO(new Date());
}

export function nowMin(): number {
  const d = new Date();
  return d.getHours() * 60 + d.getMinutes();
}

export function toMin(t: string): number {
  const m = /(\\d+):(\\d+)\\s*(AM|PM)/i.exec(t);
  if (!m) return 0;
  let h = (+m[1]) % 12;
  if (/PM/i.test(m[3])) h += 12;
  return h * 60 + +m[2];
}

export function slotPrice(v: Venue, s: string): number {
  return toMin(s) >= 17 * 60 ? roundTo(v.price * 1.15, 50) : v.price;
}

export function validDays(v: Venue, n: number): string[] {
  const out: string[] = [];
  const d = new Date();
  for (let i = 0; i < 40 && out.length < n; i++) {
    const x = new Date(d.getFullYear(), d.getMonth(), d.getDate() + i);
    if (!v.days || v.days.includes(x.getDay())) out.push(toISO(x));
  }
  return out;
}

export function newRef(): string {
  const a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let s = 'HP-';
  for (let i = 0; i < 6; i++) s += a[Math.floor(Math.random() * a.length)];
  return s;
}

// Persistent Storage Class
class DataStore {
  public venues: Venue[] = [];
  public users: Record<string, User> = {};
  public bookings: Booking[] = [];
  public reviews: Record<string, number> = {};
  public saved: Record<string, string[]> = {};
  private dataFile: string;

  constructor() {
    this.dataFile = path.resolve(process.cwd(), 'server', 'data', 'store.json');
    this.load();
  }

  private load() {
    try {
      if (fs.existsSync(this.dataFile)) {
        const raw = fs.readFileSync(this.dataFile, 'utf-8');
        const data = JSON.parse(raw);
        this.venues = Array.isArray(data.venues) && data.venues.length ? data.venues : buildDefaultVenues();
        this.users = data.users || {};
        this.bookings = data.bookings || [];
        this.reviews = data.reviews || {};
        this.saved = data.saved || {};
        console.log(`[DataStore] Loaded ${this.venues.length} venues, ${Object.keys(this.users).length} users, ${this.bookings.length} bookings.`);
        return;
      }
    } catch (e) {
      console.warn('[DataStore] Could not load store.json, reinitializing default dataset.', e);
    }

    this.venues = buildDefaultVenues();
    // Default demo guest user
    const guestEmail = 'guest@hoppin.demo';
    this.users[guestEmail] = {
      id: 'usr_guest',
      email: guestEmail,
      name: 'Guest',
      passwordHash: Buffer.from('guest-demo').toString('base64'),
      createdAt: Date.now()
    };
    this.save();
    console.log(`[DataStore] Initialized store with ${this.venues.length} venues.`);
  }

  public save() {
    try {
      const dir = path.dirname(this.dataFile);
      if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
      const payload = {
        venues: this.venues,
        users: this.users,
        bookings: this.bookings,
        reviews: this.reviews,
        saved: this.saved
      };
      fs.writeFileSync(this.dataFile, JSON.stringify(payload, null, 2), 'utf-8');
    } catch (e) {
      console.error('[DataStore] Failed to write store.json:', e);
    }
  }

  public getVenue(id: string): Venue | undefined {
    return this.venues.find(v => v.id === id);
  }

  public getSlotAvailability(v: Venue, iso: string, slot: string, userEmail?: string): SlotAvailability {
    const isBookedByUser = userEmail && this.bookings.some(b => b.userEmail === userEmail && b.venueId === v.id && b.iso === iso && b.slot === slot && b.status !== 'cancelled');
    if (isBookedByUser) {
      return { slot, state: 'yours', price: slotPrice(v, slot) };
    }

    if (iso === todayISO() && toMin(slot) <= nowMin()) {
      return { slot, state: 'past', price: slotPrice(v, slot) };
    }

    // Check count of active bookings for this slot
    const slotBookings = this.bookings.filter(b => b.venueId === v.id && b.iso === iso && b.slot === slot && b.status !== 'cancelled');
    if (slotBookings.length >= 3) {
      return { slot, state: 'full', price: slotPrice(v, slot) };
    }

    const r = hashStr(v.id + iso + slot) % 100;
    if (r < 16 && slotBookings.length > 0) {
      return { slot, state: 'full', price: slotPrice(v, slot) };
    }
    if (r < 38 || slotBookings.length > 0) {
      const left = Math.max(1, 3 - slotBookings.length);
      return { slot, state: 'few', price: slotPrice(v, slot), left };
    }

    return { slot, state: 'open', price: slotPrice(v, slot) };
  }

  public getVenueSlots(venueId: string, iso: string, userEmail?: string): SlotAvailability[] {
    const v = this.getVenue(venueId);
    if (!v) return [];
    return v.slots.map(s => this.getSlotAvailability(v, iso, s, userEmail));
  }

  public openTonight(v: Venue): string[] {
    const iso = todayISO();
    return v.slots.filter(s => {
      const a = this.getSlotAvailability(v, iso, s);
      return a.state === 'open' || a.state === 'few';
    });
  }

  public nextOpen(v: Venue): { iso: string; slot: string } | null {
    for (const iso of validDays(v, 10)) {
      for (const s of v.slots) {
        const a = this.getSlotAvailability(v, iso, s);
        if (a.state === 'open' || a.state === 'few') return { iso, slot: s };
      }
    }
    return null;
  }
}

export const store = new DataStore();
'''

with open('server/src/services/store.ts', 'w', encoding='utf-8') as f:
    f.write(store_ts)

print("Successfully wrote server/src/services/store.ts")
