const fs = require('fs');
const path = require('path');

const originalHtml = fs.readFileSync('C:/Users/ROSHINI S/Downloads/hoppin-poc.html', 'utf-8');

// CSS rule to support images seamlessly over the svg totems
const imageCSS = `
/* =========================================================
   REAL VENUE IMAGES WITH TOTEM FALLBACK
   ========================================================= */
.cv img, .vcover img, .th img, .fc img, .th3 img, .lrow .th img, .order .th img, .trow .th img, .hit .th img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.card:hover .cv img {
  transform: scale(1.08);
}
.vcover img {
  z-index: 1;
}
.th img, .fc img, .th3 img {
  z-index: 1;
}
`;

// Insert the CSS rule before </style>
let updatedHtml = originalHtml.replace('</style>', `${imageCSS}\n</style>`);

// Image mapping dictionary and helper functions
const imageJS = `
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

function coverMedia(v) {
  const url = coverImgURL(v);
  return \`<img src="\${url}" alt="\${esc(v.name)}" loading="lazy" onerror="this.style.display='none'">\${coverSVG(v)}\`;
}
`;

// Replace coverSVG(v) with coverMedia(v) across the file
updatedHtml = updatedHtml.replace(
  'function coverSVG(v){',
  `${imageJS}\nfunction coverSVG(v){`
);

// In cardHTML: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace('${coverSVG(v)}', '${coverMedia(v)}');

// In showVenue: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace('${coverSVG(v)}', '${coverMedia(v)}');

// In showCheckout: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace('${coverSVG(v)}', '${coverMedia(v)}');

// In liveHTML: replace ${coverSVG(r.v)} with ${coverMedia(r.v)}
updatedHtml = updatedHtml.replace('${coverSVG(r.v)}', '${coverMedia(r.v)}');

// In msgHTML: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace('${coverSVG(v)}', '${coverMedia(v)}');

// In floaters: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace('${coverSVG(v)}', '${coverMedia(v)}');

// In s3HTML: replace ${coverSVG(pick(r[2]))} with ${coverMedia(pick(r[2]))}
updatedHtml = updatedHtml.replace('${coverSVG(pick(r[2]))}', '${coverMedia(pick(r[2]))}');

// In renderBookings: replace ${coverSVG(v)} with ${coverMedia(v)}
updatedHtml = updatedHtml.replace(/\$\{coverSVG\(v\)\}/g, '${coverMedia(v)}');

// Write out to all target files
fs.writeFileSync('C:/Users/ROSHINI S/Downloads/hoppin-poc.html', updatedHtml, 'utf-8');
fs.writeFileSync('C:/Users/ROSHINI S/Downloads/hoppin-poc (1).html', updatedHtml, 'utf-8');
fs.writeFileSync('apps/web/public/poc.html', updatedHtml, 'utf-8');
fs.writeFileSync('apps/web/public/index.html', updatedHtml, 'utf-8');

console.log('Successfully added real photos and saved to all target locations!');
