import React from 'react';
import { BrowserRouter, Routes, Route, NavLink, Link } from 'react-router-dom';
import { ThemeToggle } from './theme/ThemeToggle';
import Discover from './pages/Discover';
import Restaurants from './pages/Restaurants';
import Gaming from './pages/Gaming';
import Sports from './pages/Sports';
import VenueDetail from './pages/VenueDetail';
import Booking from './pages/Booking';
import Payment from './pages/Payment';
import Confirmation from './pages/Confirmation';
import MyBookings from './pages/MyBookings';
import Profile from './pages/Profile';
import Chat from './pages/Chat';

export default function App() {
  return (
    <BrowserRouter>
      {/* Top Navigation Bar (Responsive Web + Mobile) */}
      <header
        style={{
          position: 'sticky',
          top: 0,
          zIndex: 1000,
          padding: '14px 20px',
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            maxWidth: 1240,
            margin: '0 auto',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 12,
          }}
        >
          {/* Editorial Brand Logo */}
          <Link
            to="/"
            style={{
              pointerEvents: 'auto',
              display: 'flex',
              alignItems: 'baseline',
              gap: 8,
              textDecoration: 'none',
              background: 'var(--nav-bg)',
              backdropFilter: 'blur(20px)',
              WebkitBackdropFilter: 'blur(20px)',
              padding: '9px 18px',
              borderRadius: 'var(--radius-pill)',
              border: '1px solid var(--border-glass)',
              boxShadow: 'var(--shadow-card)',
              transition: 'border-color 0.2s',
            }}
          >
            <span
              style={{
                fontFamily: 'var(--font-serif)',
                fontSize: '1.4rem',
                fontWeight: 400,
                letterSpacing: '0.04em',
                textTransform: 'uppercase',
                color: 'var(--text-primary)',
              }}
            >
              HOPPIN
            </span>
            <span
              style={{
                width: 6,
                height: 6,
                borderRadius: '50%',
                background: 'var(--grail-gold)',
                display: 'inline-block',
                boxShadow: '0 0 8px var(--grail-gold)',
              }}
            />
            <span
              style={{
                fontFamily: 'var(--font-mono)',
                fontSize: '10px',
                color: 'var(--text-tertiary)',
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
                marginLeft: 4,
              }}
            >
              67 VENUES
            </span>
          </Link>

          {/* Desktop Center Navigation Pill (Hidden on Mobile via CSS) */}
          <nav
            className="desktop-nav"
            style={{
              pointerEvents: 'auto',
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              background: 'var(--nav-bg)',
              backdropFilter: 'blur(24px)',
              WebkitBackdropFilter: 'blur(24px)',
              padding: '4px 6px',
              borderRadius: 'var(--radius-pill)',
              border: '1px solid var(--border-glass)',
              boxShadow: 'var(--shadow-grail)',
            }}
          >
            {[
              { to: '/', label: 'DISCOVER' },
              { to: '/sports', label: 'SPORTS' },
              { to: '/restaurants', label: 'DINING' },
              { to: '/gaming', label: 'GAMING' },
            ].map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.to === '/'}
                style={({ isActive }) => ({
                  padding: '8px 18px',
                  borderRadius: 'var(--radius-pill)',
                  fontSize: '11px',
                  fontFamily: 'var(--font-mono)',
                  letterSpacing: '0.12em',
                  fontWeight: 600,
                  color: isActive ? 'var(--grail-lilac-dark)' : 'var(--text-secondary)',
                  background: isActive ? 'var(--grail-lilac)' : 'transparent',
                  boxShadow: isActive ? 'var(--shadow-pill)' : 'none',
                  textDecoration: 'none',
                  transition: 'all 0.25s cubic-bezier(0.22, 1, 0.36, 1)',
                })}
              >
                {item.label}
              </NavLink>
            ))}
          </nav>

          {/* Right Actions: AI Assistant Pill + Theme Toggle */}
          <div
            style={{
              pointerEvents: 'auto',
              display: 'flex',
              alignItems: 'center',
              gap: 10,
            }}
          >
            <NavLink
              to="/chat"
              className="desktop-chat-pill"
              style={({ isActive }) => ({
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                padding: '9px 18px',
                borderRadius: 'var(--radius-pill)',
                fontSize: '11px',
                fontFamily: 'var(--font-mono)',
                fontWeight: 700,
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
                textDecoration: 'none',
                background: isActive ? 'var(--grail-lilac)' : 'var(--nav-bg)',
                color: isActive ? 'var(--grail-lilac-dark)' : 'var(--text-primary)',
                border: '1px solid var(--border-glass)',
                backdropFilter: 'blur(20px)',
                WebkitBackdropFilter: 'blur(20px)',
                boxShadow: isActive ? 'var(--shadow-pill)' : 'var(--shadow-card)',
                transition: 'all 0.25s cubic-bezier(0.22, 1, 0.36, 1)',
              })}
            >
              <span
                style={{
                  width: 7,
                  height: 7,
                  borderRadius: '50%',
                  background: 'var(--grail-gold)',
                  boxShadow: '0 0 10px var(--grail-gold)',
                }}
              />
              <span>AI CONCIERGE</span>
            </NavLink>

            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main style={{ minHeight: 'calc(100vh - 160px)', paddingBottom: '70px' }}>
        <Routes>
          <Route path="/" element={<Discover />} />
          <Route path="/restaurants" element={<Restaurants />} />
          <Route path="/gaming" element={<Gaming />} />
          <Route path="/sports" element={<Sports />} />
          <Route path="/venue/:id" element={<VenueDetail />} />
          <Route path="/booking/:slotId" element={<Booking />} />
          <Route path="/payment/:bookingId" element={<Payment />} />
          <Route path="/confirmation/:bookingId" element={<Confirmation />} />
          <Route path="/bookings" element={<MyBookings />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/chat" element={<Chat />} />
        </Routes>
      </main>

      {/* Mobile Bottom Navigation Bar (Visible only on phone screens < 768px) */}
      <nav
        className="mobile-bottom-nav"
        style={{
          position: 'fixed',
          bottom: 12,
          left: 12,
          right: 12,
          zIndex: 1000,
          background: 'var(--nav-bg)',
          backdropFilter: 'blur(24px)',
          WebkitBackdropFilter: 'blur(24px)',
          border: '1px solid var(--border-glass)',
          borderRadius: 'var(--radius-pill)',
          padding: '6px 8px',
          display: 'none',
          justifyContent: 'space-around',
          alignItems: 'center',
          boxShadow: 'var(--shadow-grail)',
        }}
      >
        {[
          { to: '/', icon: '✦', label: 'Explore' },
          { to: '/sports', icon: '🏸', label: 'Sports' },
          { to: '/restaurants', icon: '🍽️', label: 'Dining' },
          { to: '/gaming', icon: '🎮', label: 'Gaming' },
          { to: '/chat', icon: '💬', label: 'AI Chat' },
        ].map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            style={({ isActive }) => ({
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 2,
              padding: '6px 12px',
              borderRadius: 'var(--radius-pill)',
              textDecoration: 'none',
              background: isActive ? 'var(--grail-lilac)' : 'transparent',
              color: isActive ? 'var(--grail-lilac-dark)' : 'var(--text-secondary)',
              transition: 'all 0.2s',
            })}
          >
            <span style={{ fontSize: '14px' }}>{item.icon}</span>
            <span style={{ fontFamily: 'var(--font-mono)', fontSize: '9px', fontWeight: 600, letterSpacing: '0.04em' }}>
              {item.label}
            </span>
          </NavLink>
        ))}
      </nav>

      {/* Responsive Inline CSS for Mobile Breakpoints */}
      <style>{`
        @media (max-width: 768px) {
          .desktop-nav {
            display: none !important;
          }
          .desktop-chat-pill {
            display: none !important;
          }
          .mobile-bottom-nav {
            display: flex !important;
          }
        }
      `}</style>
    </BrowserRouter>
  );
}
