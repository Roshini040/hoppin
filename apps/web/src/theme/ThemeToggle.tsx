import React, { useEffect, useState } from 'react';

export function ThemeToggle({ showLabel = false }: { showLabel?: boolean }) {
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {
    const saved = localStorage.getItem('theme');
    if (saved === 'light' || saved === 'dark') return saved;
    return 'dark'; // default to Grail signature dark aesthetic
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggle = () => {
    setTheme((t) => (t === 'dark' ? 'light' : 'dark'));
  };

  return (
    <button
      onClick={toggle}
      title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
      aria-label="Toggle theme"
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 6,
        padding: showLabel ? '8px 16px' : '8px 12px',
        borderRadius: 'var(--radius-pill)',
        background: 'var(--bg-glass)',
        border: '1px solid var(--border-glass)',
        color: 'var(--text-primary)',
        fontFamily: 'var(--font-mono)',
        fontSize: '11px',
        letterSpacing: '0.1em',
        cursor: 'pointer',
        transition: 'all 0.2s cubic-bezier(0.22, 1, 0.36, 1)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        boxShadow: 'var(--shadow-card)',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.borderColor = 'var(--grail-lilac)';
        e.currentTarget.style.transform = 'scale(1.04)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.borderColor = 'var(--border-glass)';
        e.currentTarget.style.transform = 'scale(1)';
      }}
    >
      <span style={{ fontSize: '13px' }}>{theme === 'dark' ? '☀️' : '🌙'}</span>
      {showLabel && <span>{theme === 'dark' ? 'LIGHT' : 'DARK'}</span>}
    </button>
  );
}
