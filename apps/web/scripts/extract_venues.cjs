const fs = require('fs');
const path = require('path');

const sqlPath = path.resolve('supabase/seed/seed_venues.sql');
const sql = fs.readFileSync(sqlPath, 'utf-8');

// Regex to capture each venue value tuple
const rowRegex = /\((?:'((?:[^']|'')*)'|NULL),\s*(?:'((?:[^']|'')*)'|NULL),\s*(?:'((?:[^']|'')*)'|NULL),\s*(?:'((?:[^']|'')*)'|NULL),\s*(\d+|NULL),\s*([\d\.]+|NULL),\s*(\d+|NULL),\s*(?:array\[(.*?)\]|NULL),\s*(?:'((?:[^']|'')*)'|NULL),\s*(true|false)\)/g;

const venues = [];
let match;

// Curated high quality Unsplash photos matching categories
const categoryPhotos = {
  sports: [
    'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=800&q=80', // badminton
    'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=800&q=80', // football turf
    'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80', // gym/turf
    'https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=800&q=80', // basketball/court
    'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80'  // tennis/badminton
  ],
  gym: [
    'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80'
  ],
  pub: [
    'https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1543007630-9710e4a00a20?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1538488254700-2e955b9c4500?auto=format&fit=crop&w=800&q=80'
  ],
  restaurant: [
    'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=800&q=80'
  ],
  gaming: [
    'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1612287232230-65c27f3f269a?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1580234811497-9df7fd2f357e?auto=format&fit=crop&w=800&q=80'
  ],
  club: [
    'https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1483721310020-03333e577078?auto=format&fit=crop&w=800&q=80'
  ]
};

let idx = 0;
while ((match = rowRegex.exec(sql)) !== null) {
  idx++;
  const name = match[1] ? match[1].replace(/''/g, "'") : '';
  const category = match[2] ? match[2].replace(/''/g, "'") : 'other';
  const city = match[3] ? match[3].replace(/''/g, "'") : 'Bengaluru';
  const area = match[4] ? match[4].replace(/''/g, "'") : '';
  const priceTier = match[5] && match[5] !== 'NULL' ? parseInt(match[5]) : 2;
  const rating = match[6] && match[6] !== 'NULL' ? parseFloat(match[6]) : Number((4.3 + (idx % 6) * 0.1).toFixed(1));
  const reviewCount = match[7] && match[7] !== 'NULL' ? parseInt(match[7]) : (35 + (idx * 17) % 210);
  const tagsStr = match[8] || '';
  const tags = tagsStr
    ? tagsStr.split(',').map(s => s.trim().replace(/^'|'$/g, '').replace(/''/g, "'")).filter(Boolean)
    : [];
  const description = match[9] ? match[9].replace(/''/g, "'") : '';
  const isLive = match[10] === 'true';

  const photos = categoryPhotos[category] || categoryPhotos.sports;
  const photo = photos[idx % photos.length];

  // Generate realistic time slots for booking
  const slots = [
    { id: `slot-${idx}-1`, time: '07:00 AM - 08:00 AM', price: priceTier * 400, available: true },
    { id: `slot-${idx}-2`, time: '09:00 AM - 10:00 AM', price: priceTier * 400, available: true },
    { id: `slot-${idx}-3`, time: '05:00 PM - 06:00 PM', price: priceTier * 500, available: idx % 3 !== 0 },
    { id: `slot-${idx}-4`, time: '07:00 PM - 08:00 PM', price: priceTier * 600, available: true },
    { id: `slot-${idx}-5`, time: '08:30 PM - 09:30 PM', price: priceTier * 600, available: idx % 2 === 0 },
  ];

  venues.push({
    id: `venue-${idx}`,
    name,
    category,
    city,
    area,
    priceTier,
    rating,
    reviewCount,
    tags,
    description,
    isLive,
    photo,
    slots,
  });
}

console.log(`Extracted ${venues.length} venues successfully!`);

const outputContent = `// Auto-generated from supabase/seed/seed_venues.sql (67 venues)
export interface Slot {
  id: string;
  time: string;
  price: number;
  available: boolean;
}

export interface Venue {
  id: string;
  name: string;
  category: 'club' | 'gym' | 'sports' | 'gaming' | 'pub' | 'restaurant' | string;
  city: 'Bengaluru' | 'Chennai' | string;
  area: string;
  priceTier: number;
  rating: number;
  reviewCount: number;
  tags: string[];
  description: string;
  isLive: boolean;
  photo: string;
  slots: Slot[];
}

export const VENUES_DATA: Venue[] = ${JSON.stringify(venues, null, 2)};
`;

const outDir = path.resolve('apps/web/src/data');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}
fs.writeFileSync(path.join(outDir, 'venues.ts'), outputContent, 'utf-8');
console.log('Saved to apps/web/src/data/venues.ts');
