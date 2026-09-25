import React, { useState, useEffect } from 'react';
import { Venue } from '../data/venues';
import { getVenues } from '../lib/api';
import { VenueCard } from '../components/VenueCard';
import { VenueModal } from '../components/VenueModal';

export default function Sports() {
  const [venues, setVenues] = useState<Venue[]>([]);
  const [activeVenue, setActiveVenue] = useState<Venue | null>(null);

  useEffect(() => {
    getVenues(undefined, 'sports').then(setVenues);
  }, []);

  return (
    <div style={{ maxWidth: 1280, margin: '0 auto', padding: '24px 20px 80px' }}>
      <div style={{ marginBottom: 28 }}>
        <h1 style={{ fontSize: '2rem', fontWeight: 800, margin: '0 0 8px 0', color: 'var(--text)' }}>
          🏸 Sports Courts & Football Turfs
        </h1>
        <p style={{ color: 'var(--text-secondary)', margin: 0 }}>
          Indoor wooden badminton courts, floodlit 5v5 artificial pitches, and cricket nets
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: 24 }}>
        {venues.map((v) => (
          <VenueCard key={v.id} venue={v} onSelect={(venue) => setActiveVenue(venue)} />
        ))}
      </div>

      <VenueModal venue={activeVenue} onClose={() => setActiveVenue(null)} />
    </div>
  );
}
