import { Router } from 'express';
import { store, Venue, todayISO, toMin } from '../services/store';

export const venuesRouter = Router();

function dist(lat1: number, lon1: number, lat2: number, lon2: number): number {
  const r = (x: number) => x * Math.PI / 180;
  return 6371 * Math.acos(
    Math.min(1, Math.sin(r(lat1)) * Math.sin(r(lat2)) + Math.cos(r(lat1)) * Math.cos(r(lat2)) * Math.cos(r(lon2 - lon1)))
  );
}

// GET /venues or GET /api/venues
venuesRouter.get('/', (req, res) => {
  const { city, cat, category, q, sort, maxPrice, minRating, tonight, lat, lng } = req.query;

  let list = [...store.venues];

  // City filter
  if (city && city !== 'all' && city !== 'All') {
    const c = String(city).toUpperCase();
    if (c === 'BLR' || c === 'BENGALURU') {
      list = list.filter(v => v.city === 'BLR' || v.cityName.toLowerCase() === 'bengaluru');
    } else if (c === 'MAA' || c === 'CHENNAI') {
      list = list.filter(v => v.city === 'MAA' || v.cityName.toLowerCase() === 'chennai');
    }
  }

  // Category filter
  const categoryFilter = cat || category;
  if (categoryFilter && categoryFilter !== 'all' && categoryFilter !== 'All') {
    const cf = String(categoryFilter).toLowerCase();
    list = list.filter(v => v.cat.toLowerCase() === cf || (cf === 'gym' && v.cat === 'fitness') || (cf === 'restaurant' && v.cat === 'dining') || (cf === 'pub' && v.cat === 'pubs'));
  }

  // Search query filter
  if (q && String(q).trim()) {
    const terms = String(q).toLowerCase().split(/\s+/).filter(Boolean);
    list = list.filter(v => {
      const hay = (v.name + ' ' + v.area + ' ' + v.cityName + ' ' + v.cat + ' ' + v.tags.join(' ') + ' ' + v.desc).toLowerCase();
      return terms.every(t => hay.includes(t));
    });
  }

  // Max price filter
  if (maxPrice && Number(maxPrice) > 0) {
    const mp = Number(maxPrice);
    list = list.filter(v => v.price <= mp);
  }

  // Min rating filter
  if (minRating && Number(minRating) > 0) {
    const mr = Number(minRating);
    list = list.filter(v => v.rating >= mr);
  }

  // Open tonight filter
  if (tonight === 'true' || tonight === '1') {
    list = list.filter(v => store.openTonight(v).length > 0);
  }

  // Sorting
  const sortBy = String(sort || 'rating');
  if (sortBy === 'rating') {
    list.sort((a, b) => b.rating - a.rating || b.reviews - a.reviews);
  } else if (sortBy === 'reviews') {
    list.sort((a, b) => b.reviews - a.reviews);
  } else if (sortBy === 'price') {
    list.sort((a, b) => a.price - b.price);
  } else if (sortBy === 'near' && lat && lng) {
    const ulat = Number(lat);
    const ulng = Number(lng);
    list.sort((a, b) => dist(ulat, ulng, a.lat, a.lng) - dist(ulat, ulng, b.lat, b.lng));
  }

  res.json(list);
});

// GET /venues/:id/slots?date=YYYY-MM-DD&email=user@example.com
venuesRouter.get('/:id/slots', (req, res) => {
  const venue = store.getVenue(req.params.id);
  if (!venue) return res.status(404).json({ error: 'Venue not found' });

  const iso = (req.query.date as string) || (req.query.iso as string) || todayISO();
  const email = req.query.email as string | undefined;

  const slots = store.getVenueSlots(venue.id, iso, email);
  res.json({ venueId: venue.id, iso, slots });
});

// GET /venues/:id
venuesRouter.get('/:id', (req, res) => {
  const venue = store.getVenue(req.params.id);
  if (!venue) return res.status(404).json({ error: 'Venue not found' });

  const iso = todayISO();
  const slots = store.getVenueSlots(venue.id, iso);

  res.json({
    ...venue,
    currentSlots: slots
  });
});
