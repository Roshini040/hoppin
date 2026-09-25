import React, { useEffect, useState, useMemo } from 'react';
import { Venue, Slot } from '../data/venues';
import { getVenues } from '../lib/api';
import { VenueCard } from '../components/VenueCard';
import { VenueModal } from '../components/VenueModal';
import { Link } from 'react-router-dom';

const CATEGORIES = [
  { id: 'all', label: 'ALL EXPERIENCES', count: 67 },
  { id: 'sports', label: 'SPORTS & TURFS', count: 18 },
  { id: 'gym', label: 'FITNESS & GYMS', count: 12 },
  { id: 'pub', label: 'PUBS & BREWS', count: 13 },
  { id: 'restaurant', label: 'DINING & CAFES', count: 7 },
  { id: 'gaming', label: 'GAMING & ARCADES', count: 9 },
  { id: 'club', label: 'CLUBS & RUNS', count: 8 },
];

export default function Discover() {
  const [venues, setVenues] = useState<Venue[]>([]);
  const [selectedCity, setSelectedCity] = useState<'All' | 'Bengaluru' | 'Chennai'>('All');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [sortBy, setSortBy] = useState<'rating' | 'reviews' | 'price'>('rating');
  const [activeVenue, setActiveVenue] = useState<Venue | null>(null);
  const [loading, setLoading] = useState(true);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    getVenues(
      selectedCity === 'All' ? undefined : selectedCity,
      selectedCategory === 'all' ? undefined : selectedCategory,
      searchQuery
    )
      .then((data) => {
        if (isMounted) {
          setVenues(data);
          setLoading(false);
        }
      })
      .catch(() => {
        if (isMounted) setLoading(false);
      });

    return () => {
      isMounted = false;
    };
  }, [selectedCity, selectedCategory, searchQuery]);

  const sortedVenues = useMemo(() => {
    return [...venues].sort((a, b) => {
      if (sortBy === 'rating') return b.rating - a.rating;
      if (sortBy === 'reviews') return b.reviewCount - a.reviewCount;
      if (sortBy === 'price') return a.priceTier - b.priceTier;
      return 0;
    });
  }, [venues, sortBy]);

  const handleBookSlot = (venue: Venue, slot: Slot) => {
    setToastMessage(`Reserved ${venue.name} for ${slot.time}`);
    setTimeout(() => setToastMessage(null), 4000);
  };

  return (
    <div style={{ maxWidth: 1240, margin: '0 auto', padding: '16px 20px 80px' }}>
      {/* Toast Notification */}
      {toastMessage && (
        <div
          style={{
            position: 'fixed',
            bottom: 80,
            right: 24,
            background: 'var(--grail-lilac)',
            color: 'var(--grail-lilac-dark)',
            padding: '12px 20px',
            borderRadius: 'var(--radius-pill)',
            boxShadow: 'var(--shadow-grail)',
            zIndex: 3000,
            fontFamily: 'var(--font-mono)',
            fontSize: '11px',
            fontWeight: 700,
            letterSpacing: '0.08em',
            textTransform: 'uppercase',
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}
        >
          <span>✓</span>
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Hero Section */}
      <section style={{ padding: '36px 0 32px', position: 'relative' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 16 }}>
          <span
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              fontWeight: 600,
              letterSpacing: '0.22em',
              textTransform: 'uppercase',
              color: 'var(--grail-gold)',
            }}
          >
            REAL-WORLD VENUES // NO SCREEN-ONLY LOCK-IN
          </span>
          <span style={{ color: 'var(--text-tertiary)' }}>·</span>
          <span
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              letterSpacing: '0.12em',
              textTransform: 'uppercase',
              color: 'var(--text-tertiary)',
            }}
          >
            67 VENUES
          </span>
        </div>

        <h1
          style={{
            fontFamily: 'var(--font-serif)',
            fontSize: 'clamp(2.4rem, 6.2vw, 5.2rem)',
            fontWeight: 300,
            textTransform: 'uppercase',
            letterSpacing: '-0.02em',
            lineHeight: 0.95,
            color: 'var(--text-primary)',
            margin: '0 0 20px 0',
            maxWidth: 920,
          }}
        >
          DISCOVER REAL PLACES. <br />
          <em style={{ fontStyle: 'italic', color: 'var(--grail-gold)', fontWeight: 300 }}>
            STEP OUT INTO THE CITY.
          </em>
        </h1>

        <p
          style={{
            maxWidth: 580,
            fontSize: '14px',
            lineHeight: 1.55,
            color: 'var(--text-secondary)',
            margin: '0 0 28px 0',
          }}
        >
          67 curated venues across Bengaluru and Chennai. Badminton courts, football turfs, craft brewpubs, and board game cafes — with AI vector booking.
        </p>

        {/* Grail Stat / Pillar Tiles */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
            gap: 10,
            marginBottom: 32,
          }}
        >
          {[
            { stat: 'STRENGTH', subtitle: '18 Courts & Turfs', desc: 'Badminton & football' },
            { stat: 'CHARISMA', subtitle: '13 Taprooms', desc: 'Craft brews & rooftops' },
            { stat: 'INTELLECT', subtitle: '9 Board Cafes', desc: '1,300+ titles & VR' },
            { stat: 'ENDURANCE', subtitle: '12 Gyms & Runs', desc: 'Beach runs & boxes' },
          ].map((card, i) => (
            <div
              key={i}
              style={{
                background: 'var(--bg-surface)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-sm)',
                padding: '14px 16px',
                boxShadow: 'var(--shadow-card)',
              }}
            >
              <div
                style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: '9px',
                  letterSpacing: '0.18em',
                  textTransform: 'uppercase',
                  color: 'var(--grail-gold)',
                  marginBottom: 3,
                }}
              >
                {card.stat}
              </div>
              <div style={{ fontFamily: 'var(--font-serif)', fontSize: '1.15rem', fontWeight: 400, color: 'var(--text-primary)', marginBottom: 2 }}>
                {card.subtitle}
              </div>
              <div style={{ fontSize: '10px', color: 'var(--text-tertiary)' }}>
                {card.desc}
              </div>
            </div>
          ))}
        </div>

        {/* Filter Controls Bar */}
        <div
          style={{
            display: 'flex',
            flexWrap: 'wrap',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 12,
            paddingTop: 14,
            borderTop: '1px solid var(--border-subtle)',
          }}
        >
          {/* City Capsule Toggle */}
          <div
            style={{
              display: 'flex',
              background: 'var(--bg-surface)',
              padding: 3,
              borderRadius: 'var(--radius-pill)',
              border: '1px solid var(--border-glass)',
            }}
          >
            {(['All', 'Bengaluru', 'Chennai'] as const).map((city) => (
              <button
                key={city}
                onClick={() => setSelectedCity(city)}
                style={{
                  padding: '7px 15px',
                  borderRadius: 'var(--radius-pill)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '10px',
                  letterSpacing: '0.1em',
                  fontWeight: selectedCity === city ? 700 : 500,
                  textTransform: 'uppercase',
                  background: selectedCity === city ? 'var(--grail-lilac)' : 'transparent',
                  color: selectedCity === city ? 'var(--grail-lilac-dark)' : 'var(--text-secondary)',
                  boxShadow: selectedCity === city ? 'var(--shadow-pill)' : 'none',
                  transition: 'all 0.2s',
                }}
              >
                {city === 'All' ? 'ALL (67)' : city === 'Bengaluru' ? 'BLR (29)' : 'MAA (38)'}
              </button>
            ))}
          </div>

          {/* Search Input */}
          <div style={{ flex: 1, minWidth: 220, position: 'relative' }}>
            <span
              style={{
                position: 'absolute',
                left: 14,
                top: '50%',
                transform: 'translateY(-50%)',
                color: 'var(--text-tertiary)',
                fontSize: '11px',
                fontFamily: 'var(--font-mono)',
              }}
            >
              //
            </span>
            <input
              type="text"
              placeholder="SEARCH INDIRANAGAR, TURF, ADYAR, BOARD GAMES..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 14px 10px 32px',
                background: 'var(--input-bg)',
                border: '1px solid var(--input-border)',
                borderRadius: 'var(--radius-pill)',
                color: 'var(--text-primary)',
                fontFamily: 'var(--font-mono)',
                fontSize: '11px',
                letterSpacing: '0.06em',
                outline: 'none',
                transition: 'border-color 0.2s',
              }}
              onFocus={(e) => (e.target.style.borderColor = 'var(--grail-gold)')}
              onBlur={(e) => (e.target.style.borderColor = 'var(--input-border)')}
            />
          </div>

          {/* Sort Dropdown */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value as any)}
              style={{
                padding: '8px 14px',
                background: 'var(--bg-surface)',
                border: '1px solid var(--border-glass)',
                borderRadius: 'var(--radius-pill)',
                color: 'var(--text-primary)',
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                letterSpacing: '0.08em',
                outline: 'none',
                cursor: 'pointer',
              }}
            >
              <option value="rating">RATING (HIGH)</option>
              <option value="reviews">REVIEWS (MOST)</option>
              <option value="price">PRICE (LOW-HIGH)</option>
            </select>
          </div>
        </div>

        {/* Category Pills Bar */}
        <div
          style={{
            display: 'flex',
            gap: 6,
            overflowX: 'auto',
            paddingTop: 14,
            paddingBottom: 4,
          }}
        >
          {CATEGORIES.map((cat) => {
            const isActive = selectedCategory === cat.id;
            return (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                style={{
                  padding: '6px 14px',
                  borderRadius: 'var(--radius-pill)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '10px',
                  letterSpacing: '0.08em',
                  fontWeight: isActive ? 700 : 500,
                  whiteSpace: 'nowrap',
                  background: isActive ? 'var(--grail-lilac)' : 'var(--bg-surface)',
                  color: isActive ? 'var(--grail-lilac-dark)' : 'var(--text-secondary)',
                  border: isActive ? '1px solid var(--grail-lilac)' : '1px solid var(--border-subtle)',
                  boxShadow: isActive ? 'var(--shadow-pill)' : 'none',
                  transition: 'all 0.2s',
                }}
              >
                {cat.label}
              </button>
            );
          })}
        </div>
      </section>

      {/* Venues Grid */}
      <section style={{ marginTop: 20 }}>
        {loading ? (
          <div style={{ textAlign: 'center', padding: '80px 0', color: 'var(--text-tertiary)', fontFamily: 'var(--font-mono)', fontSize: '11px', letterSpacing: '0.18em' }}>
            // LOADING VENUES...
          </div>
        ) : sortedVenues.length === 0 ? (
          <div
            style={{
              textAlign: 'center',
              padding: '80px 20px',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-card)',
              background: 'var(--bg-surface)',
            }}
          >
            <div style={{ fontFamily: 'var(--font-serif)', fontSize: '1.8rem', color: 'var(--text-primary)', marginBottom: 8 }}>
              NO VENUES FOUND
            </div>
            <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginBottom: 20 }}>
              Try adjusting your search query or city filter.
            </p>
            <button
              onClick={() => {
                setSelectedCity('All');
                setSelectedCategory('all');
                setSearchQuery('');
              }}
              style={{
                padding: '9px 20px',
                borderRadius: 'var(--radius-pill)',
                background: 'var(--grail-lilac)',
                color: 'var(--grail-lilac-dark)',
                fontFamily: 'var(--font-mono)',
                fontSize: '11px',
                fontWeight: 700,
                letterSpacing: '0.12em',
              }}
            >
              RESET FILTERS
            </button>
          </div>
        ) : (
          <>
            <div
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
                color: 'var(--text-tertiary)',
                marginBottom: 16,
              }}
            >
              SHOWING {sortedVenues.length} REAL VENUES
              {selectedCity !== 'All' ? ` IN ${selectedCity.toUpperCase()}` : ''}
            </div>

            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(310px, 1fr))',
                gap: 24,
              }}
            >
              {sortedVenues.map((v) => (
                <VenueCard key={v.id} venue={v} onSelect={(venue) => setActiveVenue(venue)} />
              ))}
            </div>
          </>
        )}
      </section>

      {/* Floating Bottom Pill Widget for Desktop */}
      <div className="desktop-pill-banner">
        <Link
          to="/chat"
          style={{
            position: 'fixed',
            bottom: 24,
            left: '50%',
            transform: 'translateX(-50%)',
            zIndex: 900,
            background: 'var(--nav-bg)',
            backdropFilter: 'blur(20px)',
            WebkitBackdropFilter: 'blur(20px)',
            border: '1px solid var(--border-glass)',
            borderRadius: 'var(--radius-pill)',
            padding: '7px 10px 7px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            boxShadow: 'var(--shadow-grail)',
            textDecoration: 'none',
            color: 'var(--text-primary)',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span
              style={{
                width: 7,
                height: 7,
                borderRadius: '50%',
                background: 'var(--grail-emerald)',
                boxShadow: '0 0 8px var(--grail-emerald)',
              }}
            />
            <span
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '11px',
                letterSpacing: '0.1em',
                textTransform: 'uppercase',
              }}
            >
              Step 8 Vector RAG Active
            </span>
          </div>

          <span
            style={{
              background: 'var(--grail-lilac)',
              color: 'var(--grail-lilac-dark)',
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              fontWeight: 700,
              letterSpacing: '0.12em',
              padding: '6px 14px',
              borderRadius: 'var(--radius-pill)',
              textTransform: 'uppercase',
            }}
          >
            Ask AI Concierge ↗
          </span>
        </Link>
      </div>

      <style>{`
        @media (max-width: 768px) {
          .desktop-pill-banner {
            display: none !important;
          }
        }
      `}</style>

      <VenueModal venue={activeVenue} onClose={() => setActiveVenue(null)} onBookSlot={handleBookSlot} />
    </div>
  );
}
