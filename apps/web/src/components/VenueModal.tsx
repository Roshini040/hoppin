import React, { useState } from 'react';
import { Venue, Slot } from '../data/venues';

interface VenueModalProps {
  venue: Venue | null;
  onClose: () => void;
  onBookSlot?: (venue: Venue, slot: Slot) => void;
}

export function VenueModal({ venue, onClose, onBookSlot }: VenueModalProps) {
  const [selectedSlot, setSelectedSlot] = useState<Slot | null>(null);
  const [booked, setBooked] = useState(false);

  if (!venue) return null;

  const handleBooking = () => {
    if (selectedSlot) {
      setBooked(true);
      onBookSlot?.(venue, selectedSlot);
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 2000,
        padding: '16px',
      }}
      onClick={onClose}
    >
      <div
        className="modal-container"
        style={{
          background: 'var(--bg-surface)',
          borderRadius: 'var(--radius-modal)',
          border: '1px solid var(--border-glass)',
          width: '100%',
          maxWidth: 620,
          maxHeight: '90vh',
          overflowY: 'auto',
          boxShadow: 'var(--shadow-grail)',
          position: 'relative',
          color: 'var(--text-primary)',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Mobile Drag Handle */}
        <div
          style={{
            width: 40,
            height: 4,
            borderRadius: 2,
            background: 'var(--border-glass)',
            margin: '10px auto 0',
            display: 'none',
          }}
          className="mobile-handle"
        />

        {/* Header Hero Image */}
        <div style={{ position: 'relative', width: '100%', height: 240 }}>
          <img
            src={venue.photo}
            alt={venue.name}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background: 'linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.85) 100%)',
            }}
          />

          <button
            onClick={onClose}
            aria-label="Close modal"
            style={{
              position: 'absolute',
              top: 14,
              right: 14,
              width: 36,
              height: 36,
              borderRadius: '50%',
              background: 'rgba(0, 0, 0, 0.65)',
              backdropFilter: 'blur(12px)',
              color: '#ffffff',
              fontSize: '1rem',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              cursor: 'pointer',
            }}
          >
            ✕
          </button>

          <div
            style={{
              position: 'absolute',
              bottom: 16,
              left: 20,
              display: 'flex',
              gap: 8,
            }}
          >
            <span
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
                padding: '4px 12px',
                borderRadius: 'var(--radius-pill)',
                background: 'var(--grail-lilac)',
                color: 'var(--grail-lilac-dark)',
                fontWeight: 700,
              }}
            >
              {venue.category}
            </span>
            <span
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
                padding: '4px 12px',
                borderRadius: 'var(--radius-pill)',
                background: 'rgba(0, 0, 0, 0.65)',
                backdropFilter: 'blur(10px)',
                color: '#ffffff',
                border: '1px solid rgba(255, 255, 255, 0.2)',
                fontWeight: 600,
              }}
            >
              {venue.city}
            </span>
          </div>
        </div>

        {/* Modal Body */}
        <div style={{ padding: '24px 26px 30px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 16, marginBottom: 8 }}>
            <h2
              style={{
                margin: 0,
                fontFamily: 'var(--font-serif)',
                fontSize: '1.85rem',
                fontWeight: 400,
                letterSpacing: '-0.01em',
                color: 'var(--text-primary)',
                lineHeight: 1.15,
              }}
            >
              {venue.name}
            </h2>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 4,
                background: 'rgba(201, 162, 74, 0.12)',
                color: 'var(--grail-gold)',
                border: '1px solid rgba(201, 162, 74, 0.3)',
                padding: '4px 10px',
                borderRadius: 'var(--radius-pill)',
                fontFamily: 'var(--font-mono)',
                fontSize: '12px',
                fontWeight: 700,
                flexShrink: 0,
              }}
            >
              <span>★</span>
              <span>{venue.rating}</span>
            </div>
          </div>

          <div
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '11px',
              color: 'var(--text-tertiary)',
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
              marginBottom: 14,
              display: 'flex',
              gap: 8,
              alignItems: 'center',
            }}
          >
            <span>{venue.area}</span>
            <span>·</span>
            <span>{venue.reviewCount} REVIEWS</span>
            <span>·</span>
            <span style={{ color: 'var(--grail-gold)', fontWeight: 700 }}>{'₹'.repeat(venue.priceTier)}</span>
          </div>

          <p
            style={{
              margin: '0 0 18px 0',
              fontSize: '14px',
              lineHeight: 1.55,
              color: 'var(--text-secondary)',
            }}
          >
            {venue.description}
          </p>

          {/* Tags */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 24 }}>
            {venue.tags.map((tag, idx) => (
              <span
                key={idx}
                style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: '10px',
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-subtle)',
                  color: 'var(--text-tertiary)',
                  padding: '3px 10px',
                  borderRadius: 'var(--radius-pill)',
                }}
              >
                #{tag}
              </span>
            ))}
          </div>

          {/* Booking Slots */}
          <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 20 }}>
            <div
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '11px',
                letterSpacing: '0.16em',
                textTransform: 'uppercase',
                color: 'var(--grail-gold)',
                marginBottom: 12,
                fontWeight: 600,
              }}
            >
              Available Booking Slots
            </div>

            {booked ? (
              <div
                style={{
                  background: 'rgba(255, 205, 255, 0.1)',
                  border: '1px solid var(--grail-lilac)',
                  borderRadius: 'var(--radius-sm)',
                  padding: 20,
                  textAlign: 'center',
                }}
              >
                <div style={{ fontFamily: 'var(--font-serif)', fontSize: '1.6rem', color: 'var(--text-primary)', marginBottom: 4 }}>
                  SLOT RESERVED
                </div>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '12px', color: 'var(--grail-gold)', letterSpacing: '0.08em' }}>
                  {selectedSlot?.time} · ₹{selectedSlot?.price}
                </div>
                <div style={{ fontSize: '13px', color: 'var(--text-secondary)', marginTop: 6 }}>
                  Booking confirmed! Ready for your visit.
                </div>
              </div>
            ) : (
              <>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(160px, 1fr))', gap: 10, marginBottom: 20 }}>
                  {venue.slots.map((slot) => {
                    const isSelected = selectedSlot?.id === slot.id;
                    return (
                      <button
                        key={slot.id}
                        disabled={!slot.available}
                        onClick={() => setSelectedSlot(slot)}
                        style={{
                          padding: '12px 14px',
                          borderRadius: 'var(--radius-sm)',
                          border: isSelected
                            ? '1px solid var(--grail-lilac)'
                            : '1px solid var(--border-subtle)',
                          background: isSelected
                            ? 'var(--grail-lilac-soft)'
                            : slot.available
                            ? 'var(--bg-card)'
                            : 'transparent',
                          color: isSelected ? '#221826' : 'var(--text-primary)',
                          cursor: slot.available ? 'pointer' : 'not-allowed',
                          opacity: slot.available ? 1 : 0.35,
                          textAlign: 'left',
                          transition: 'all 0.2s',
                        }}
                      >
                        <div
                          style={{
                            fontFamily: 'var(--font-mono)',
                            fontSize: '11px',
                            fontWeight: 600,
                          }}
                        >
                          {slot.time}
                        </div>
                        <div
                          style={{
                            fontFamily: 'var(--font-mono)',
                            fontSize: '12px',
                            fontWeight: 700,
                            color: isSelected ? '#221826' : 'var(--grail-gold)',
                            marginTop: 4,
                          }}
                        >
                          ₹{slot.price}
                        </div>
                      </button>
                    );
                  })}
                </div>

                <div style={{ display: 'flex', gap: 10 }}>
                  <button
                    onClick={onClose}
                    style={{
                      flex: 1,
                      padding: '12px 16px',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      color: 'var(--text-secondary)',
                      borderRadius: 'var(--radius-pill)',
                      fontFamily: 'var(--font-mono)',
                      fontSize: '11px',
                      letterSpacing: '0.12em',
                      textTransform: 'uppercase',
                    }}
                  >
                    CLOSE
                  </button>

                  <button
                    disabled={!selectedSlot}
                    onClick={handleBooking}
                    style={{
                      flex: 2,
                      padding: '12px 20px',
                      background: selectedSlot ? 'var(--grail-lilac)' : 'var(--bg-card)',
                      color: selectedSlot ? 'var(--grail-lilac-dark)' : 'var(--text-dim)',
                      borderRadius: 'var(--radius-pill)',
                      fontFamily: 'var(--font-mono)',
                      fontSize: '11px',
                      fontWeight: 700,
                      letterSpacing: '0.14em',
                      textTransform: 'uppercase',
                      cursor: selectedSlot ? 'pointer' : 'not-allowed',
                      boxShadow: selectedSlot ? 'var(--shadow-pill)' : 'none',
                      transition: 'all 0.2s',
                    }}
                  >
                    {selectedSlot ? `RESERVE (₹${selectedSlot.price})` : 'CHOOSE A TIME'}
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      <style>{`
        @media (max-width: 768px) {
          .modal-container {
            border-bottom-left-radius: 0 !important;
            border-bottom-right-radius: 0 !important;
            max-height: 85vh !important;
            margin-top: auto;
          }
          .mobile-handle {
            display: block !important;
          }
        }
      `}</style>
    </div>
  );
}
