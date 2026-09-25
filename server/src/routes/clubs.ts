import { Router } from 'express';

export const clubsRouter = Router();

export interface Club {
  id: string;
  name: string;
  city: 'BLR' | 'MAA';
  cityName: 'Bengaluru' | 'Chennai';
  area: string;
  category: 'running' | 'yoga' | 'cycling' | 'sports' | 'gaming';
  time: string;
  days: string;
  members: number;
  activeStreak: number;
  captain: string;
  desc: string;
  image: string;
  nextMeetup: string;
  attendees: string[];
}

let CLUBS: Club[] = [
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
    attendees: ['karthik@bessie.run', 'ananya@bessie.run', 'roshini@okaxis']
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
    desc: 'A gentle morning vinyasa flow on the grass under the bamboo groves of Cubbon Park. Open to all levels. Bring your mat, breathe the fresh morning air, and start the week grounded.',
    image: 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80',
    nextMeetup: 'Sunday, 06:30 AM · Bamboo Grove',
    attendees: ['priya@cubbon.yoga', 'arun@blr.run']
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
    desc: 'Paced city runs through the tree-lined boulevards of Koramangala and Indiranagar. Structured training for 10k and half-marathon runners with warm-up drills and hydration stations.',
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

// GET /api/clubs
clubsRouter.get('/', (req, res) => {
  const { city } = req.query;
  let list = CLUBS;
  if (city && city !== 'all') {
    list = list.filter(c => c.city === String(city).toUpperCase());
  }
  res.json({ clubs: list, total: list.length });
});

// POST /api/clubs (Create club)
clubsRouter.post('/', (req, res) => {
  const { name, city, area, category, time, days, captain, desc, image } = req.body;
  if (!name || !city || !area) {
    return res.status(400).json({ error: 'Name, city, and area are required to create a club.' });
  }

  const newClub: Club = {
    id: 'c' + String(CLUBS.length + 1).padStart(2, '0'),
    name: String(name).trim(),
    city: city.toUpperCase() === 'MAA' ? 'MAA' : 'BLR',
    cityName: city.toUpperCase() === 'MAA' ? 'Chennai' : 'Bengaluru',
    area: String(area).trim(),
    category: category || 'running',
    time: time || '06:00 AM',
    days: days || 'Weekends',
    members: 1,
    activeStreak: 1,
    captain: captain || 'Community Captain',
    desc: desc || `A health and activity club in ${area}. Show up, stay active, and build streaks together.`,
    image: image || 'https://images.unsplash.com/photo-1502680390469-be75c86b636f?auto=format&fit=crop&w=800&q=80',
    nextMeetup: `Next ${days || 'Saturday'} · ${time || '06:00 AM'} · ${area}`,
    attendees: []
  };

  CLUBS.unshift(newClub);
  res.json({ success: true, club: newClub, message: `Club "${newClub.name}" created successfully!` });
});

// POST /api/clubs/:id/rsvp
clubsRouter.post('/:id/rsvp', (req, res) => {
  const { id } = req.params;
  const { email } = req.body;
  const club = CLUBS.find(c => c.id === id);
  if (!club) return res.status(404).json({ error: 'Club not found' });

  const userEmail = email || 'guest@hoppin.demo';
  const hasRsvp = club.attendees.includes(userEmail);

  if (hasRsvp) {
    club.attendees = club.attendees.filter(e => e !== userEmail);
    club.members = Math.max(1, club.members - 1);
  } else {
    club.attendees.push(userEmail);
    club.members++;
    club.activeStreak++;
  }

  res.json({
    success: true,
    rsvpd: !hasRsvp,
    attendeesCount: club.attendees.length,
    streakXpAwarded: !hasRsvp ? 20 : 0,
    message: !hasRsvp ? `RSVP confirmed for ${club.name}! +20 Streak XP 🔥` : 'RSVP cancelled'
  });
});
