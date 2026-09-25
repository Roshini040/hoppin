import React from 'react';
import { Venue } from '../data/venues';

interface VenueCardProps {
  venue: Venue;
  onSelect?: (venue: Venue) => void;
}

export function VenueCard({ venue, onSelect }: VenueCardProps) {
  return (
    <div
      onClick={() => onSelect?.(venue)}
      style={{
        background: 'var(--bg-surface)',
        border: '1px solid var(--border-subtle)',
        borderRadius: 'var(--radius-card)',
        overflow: 'hidden',
        cursor: 'pointer',
        transition: 'all 0.3s cubic-bezier(0.22, 1, 0.36, 1)',
        display: 'flex',
        flexDirection: 'column',
        position: 'relative',
        boxShadow: 'var(--shadow-card)',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = 'translateY(-5px)';
        e.currentTarget.style.borderColor = 'var(--border-active)';
        e.currentTarget.style.boxShadow = 'var(--shadow-grail)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = 'translateY(0)';
        e.currentTarget.style.borderColor = 'var(--border-subtle)';
        e.currentTarget.style.boxShadow = 'var(--shadow-card)';
      }}
    >
      {/* Image Container with Scrim */}
      <div style={{ position: 'relative', width: '100%', height: '210px', overflow: 'hidden' }}>
        <img
          src={venue.photo}
          alt={venue.name}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transition: 'transform 0.5s ease',
          }}
          loading="lazy"
        />
        {/* Subtle Dark Bottom Fade for Text Contrast */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: 'linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.65) 100%)',
          }}
        />

        {/* Top Badges */}
        <div
          style={{
            position: 'absolute',
            top: 12,
            left: 12,
            right: 12,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <div
            style={{
              background: 'rgba(0, 0, 0, 0.72)',
              backdropFilter: 'blur(12px)',
              padding: '4px 12px',
              borderRadius: 'var(--radius-pill)',
              fontSize: '10px',
              fontFamily: 'var(--font-mono)',
              fontWeight: 700,
              letterSpacing: '0.14em',
              textTransform: 'uppercase',
              color: 'var(--grail-lilac-soft)',
              border: '1px solid rgba(255, 255, 255, 0.15)',
            }}
          >
            {venue.category}
          </div>

          <div
            style={{
              background: 'rgba(0, 0, 0, 0.72)',
              backdropFilter: 'blur(12px)',
              padding: '4px 10px',
              borderRadius: 'var(--radius-pill)',
              fontSize: '11px',
              fontFamily: 'var(--font-mono)',
              fontWeight: 700,
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              border: '1px solid rgba(255, 255, 255, 0.15)',
            }}
          >
            <span style={{ color: 'var(--grail-gold)' }}>★</span>
            <span>{venue.rating}</span>
          </div>
        </div>

        {/* Location & Price on Image Footer */}
        <div
          style={{
            position: 'absolute',
            bottom: 12,
            left: 14,
            right: 14,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-end',
          }}
        >
          <span
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '11px',
              color: '#f0f0f5',
              letterSpacing: '0.1em',
              textTransform: 'uppercase',
              fontWeight: 500,
              textShadow: '0 1px 3px rgba(0,0,0,0.8)',
            }}
          >
            {venue.city} · {venue.area}
          </span>
          <span
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '12px',
              fontWeight: 800,
              color: 'var(--grail-gold)',
              letterSpacing: '0.1em',
              textShadow: '0 1px 3px rgba(0,0,0,0.8)',
            }}
          >
            {'₹'.repeat(venue.priceTier)}
          </span>
        </div>
      </div>

      {/* Card Content Body */}
      <div style={{ padding: '18px 20px 20px', display: 'flex', flexDirection: 'column', flex: 1 }}>
        <h3
          style={{
            margin: '0 0 6px 0',
            fontFamily: 'var(--font-serif)',
            fontSize: '1.4rem',
            fontWeight: 400,
            color: 'var(--text-primary)',
            lineHeight: 1.15,
            letterSpacing: '-0.01em',
          }}
        >
          {venue.name}
        </h3>

        <p
          style={{
            margin: '0 0 14px 0',
            fontSize: '13px',
            lineHeight: 1.5,
            color: 'var(--text-secondary)',
            display: '-webkit-box',
            WebkitLineClamp: 2,
            WebkitBoxOrient: 'vertical',
            overflow: 'hidden',
          }}
        >
          {venue.description}
        </p>

        {/* Tags */}
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 16, marginTop: 'auto' }}>
          {venue.tags.slice(0, 3).map((tag, idx) => (
            <span
              key={idx}
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                color: 'var(--text-tertiary)',
                background: 'var(--bg-card)',
                border: '1px solid var(--border-subtle)',
                padding: '3px 9px',
                borderRadius: 'var(--radius-pill)',
                letterSpacing: '0.04em',
              }}
            >
              {tag}
            </span>
          ))}
        </div>

        {/* Action Button */}
        <button
          onClick={(e) => {
            e.stopPropagation();
            onSelect?.(venue);
          }}
          style={{
            width: '100%',
            padding: '11px 16px',
            borderRadius: 'var(--radius-pill)',
            border: '1px solid var(--border-glass)',
            background: 'var(--bg-card)',
            color: 'var(--text-primary)',
            fontFamily: 'var(--font-mono)',
            fontSize: '11px',
            fontWeight: 600,
            letterSpacing: '0.14em',
            textTransform: 'uppercase',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 8,
            transition: 'all 0.25s cubic-bezier(0.22, 1, 0.36, 1)',
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.background = 'var(--grail-lilac)';
            e.currentTarget.style.color = 'var(--grail-lilac-dark)';
            e.currentTarget.style.borderColor = 'var(--grail-lilac)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.background = 'var(--bg-card)';
            e.currentTarget.style.color = 'var(--text-primary)';
            e.currentTarget.style.borderColor = 'var(--border-glass)';
          }}
        >
          <span>VIEW SLOTS & RESERVE</span>
          <span style={{ fontSize: '13px' }}>↗</span>
        </button>
      </div>
    </div>
  );
}
