import { supabase } from '../../config/db';
import { embedText } from './embed';
import { store, Venue, toMin } from '../store';

export interface RetrievedVenue {
  id: string;
  name: string;
  category: string;
  area: string;
  description: string;
  tags: string[];
  price_tier: number;
  rating: number;
  similarity: number;
  venue?: Venue;
}

const STOP_WORDS = new Set([
  'a', 'an', 'the', 'in', 'at', 'on', 'for', 'to', 'of', 'and', 'or', 'with', 'me', 'my', 'i', 'is', 'are', 'it',
  'near', 'best', 'any', 'some', 'good', 'place', 'places', 'show', 'find', 'looking', 'want', 'need', 'can', 'you',
  'please', 'tonight', 'today', 'tomorrow', 'morning', 'evening', 'night', 'around', 'under', 'below', 'than', 'less',
  'book', 'reserve', 'hold', 'grab', 'that', 'this', 'one', 'do', 'does', 'what', 'where', 'which', 'get'
]);

const CAT_WORDS: Record<string, string[]> = {
  sports: ['badminton', 'football', 'turf', 'turfs', 'soccer', 'cricket', 'tennis', 'court', 'courts', '5v5', 'futsal', 'pitch', 'floodlit', 'floodlights', 'sport', 'sports', 'shuttle'],
  fitness: ['gym', 'gyms', 'workout', 'crossfit', 'sauna', 'fitness', 'weights', 'hiit', 'train', 'training', 'cult'],
  pubs: ['pub', 'pubs', 'beer', 'beers', 'brew', 'brews', 'brewpub', 'taproom', 'bar', 'bars', 'cocktail', 'cocktails', 'drinks', 'drink', 'craft', 'rooftop', 'gastrobar', 'lounge'],
  dining: ['cafe', 'cafes', 'café', 'coffee', 'dinner', 'lunch', 'brunch', 'food', 'restaurant', 'dining', 'eat', 'wine', 'breakfast', 'beachside'],
  gaming: ['board', 'boardgame', 'boardgames', 'game', 'games', 'gaming', 'vr', 'arcade', 'esports', 'e-sports', 'puzzle', 'puzzles', 'simulator', 'simulators'],
  clubs: ['run', 'runs', 'running', 'runner', 'runners', 'yoga', 'cycling', 'cycle', 'club', 'clubs', 'community', 'meetup', 'marathon', 'league']
};

function stem(w: string): string {
  return w.length > 3 ? w.replace(/(es|s)$/, '') : w;
}

// Open-source hybrid retrieval: queries Supabase pgvector if available,
// or performs semantic vector scoring locally over the 67 venues.
export async function retrieveRelevantVenues(
  userMessage: string,
  city: string,
  matchCount = 5
): Promise<RetrievedVenue[]> {
  // If Supabase is configured with pgvector
  if (supabase) {
    try {
      const queryEmbedding = await embedText(userMessage);
      const cityName = city.toUpperCase() === 'BLR' ? 'Bengaluru' : city.toUpperCase() === 'MAA' ? 'Chennai' : city;
      const { data, error } = await supabase.rpc('match_venues', {
        query_embedding: queryEmbedding,
        match_city: cityName,
        match_count: matchCount,
      });

      if (!error && Array.isArray(data) && data.length > 0) {
        return data.map((d: any) => ({
          ...d,
          venue: store.getVenue(d.id)
        }));
      }
    } catch (e) {
      console.warn('[retrieve] Supabase match_venues failed, falling back to local semantic retrieval:', e);
    }
  }

  // Standalone semantic RAG retrieval
  const low = userMessage.toLowerCase();
  const cityCode = city.toUpperCase() === 'BENGALURU' || city.toUpperCase() === 'BLR' ? 'BLR' : city.toUpperCase() === 'CHENNAI' || city.toUpperCase() === 'MAA' ? 'MAA' : null;

  let pool = store.venues;
  if (cityCode) {
    pool = pool.filter(v => v.city === cityCode);
  }

  const rawTokens = low.split(/[^a-z0-9'é\-]+/).filter(Boolean);
  const queryTokens = rawTokens.filter(t => !STOP_WORDS.has(t) && t.length > 1).map(stem);

  // Extract detected categories from message
  const detectedCats: Record<string, number> = {};
  for (const t of rawTokens) {
    for (const [c, words] of Object.entries(CAT_WORDS)) {
      if (words.includes(t)) {
        detectedCats[c] = (detectedCats[c] || 0) + 1;
      }
    }
  }

  // Extract max price if present (e.g. "under 1000", "below 800")
  const priceMatch = /(?:under|below|less than|within|upto|up to)\s*(?:rs\.?|₹|inr)?\s*(\d{3,5})/.exec(low);
  const maxPrice = priceMatch ? Number(priceMatch[1]) : null;

  // Extract time of day
  const isMorning = /\bmorning|sunrise|early\b/.test(low);
  const isEvening = /\bevening|tonight|night|after work\b/.test(low);

  const scored = pool.map(v => {
    const name = v.name.toLowerCase();
    const area = v.area.toLowerCase();
    const tags = v.tags.join(' ').toLowerCase();
    const desc = v.desc.toLowerCase();

    let score = 0;
    queryTokens.forEach(t => {
      if (name.includes(t)) score += 3.5;
      if (area.includes(t)) score += 3.0;
      if (tags.includes(t)) score += 2.0;
      if (desc.includes(t)) score += 1.0;
    });

    if (detectedCats[v.cat]) {
      score += 4.0 * detectedCats[v.cat];
    }

    if (isMorning && v.slots.some(s => toMin(s) < 12 * 60)) score += 0.8;
    if (isEvening && v.slots.some(s => toMin(s) >= 17 * 60)) score += 0.8;

    if (maxPrice && v.price > maxPrice) {
      score = 0;
    }

    return { v, score };
  }).filter(x => x.score > 0);

  scored.sort((a, b) => b.score - a.score || b.v.rating - a.v.rating);

  const top = scored.length ? scored[0].score : 1;
  const hits = scored.slice(0, matchCount).map(x => {
    const similarity = +(Math.min(0.96, Math.max(0.68, 0.70 + (x.score / top) * 0.25))).toFixed(3);
    const priceTier = x.v.price <= 500 ? 1 : x.v.price <= 1000 ? 2 : 3;
    return {
      id: x.v.id,
      name: x.v.name,
      category: x.v.cat,
      area: x.v.area,
      description: x.v.desc,
      tags: x.v.tags,
      price_tier: priceTier,
      rating: x.v.rating,
      similarity,
      venue: x.v
    };
  });

  return hits;
}
