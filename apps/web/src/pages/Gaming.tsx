import React, { useState, useEffect } from 'react';
import { Venue } from '../data/venues';
import { getVenues } from '../lib/api';
import { VenueCard } from '../components/VenueCard';
import { VenueModal } from '../components/VenueModal';

export default function Gaming() {
  const [venues, setVenues] = useState<Venue[]>([]);
  const [activeVenue, setActiveVenue] = useState<Venue | null>(null);

  useEffect(() => {
    getVenues(undefined, 'gaming').then(setVenues);
  }, []);

  return (
    <div style={{ maxWidth: 1280, margin: '0 auto', padding: '24px 20px 80px' }}>
      <div style={{ marginBottom: 28 }}>
        <h1 style={{ fontSize: '2rem', fontWeight: 800, margin: '0 0 8px 0', color: 'var(--text)' }}>
          🎮 Gaming & Board Game Cafes
        </h1>
        <p style={{ color: 'var(--text-secondary)', margin: 0 }}>
          E-sports lounges, VR simulators, and cozy board game cafes with 1,000+ titles
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
