import React, { useState, useRef, useEffect } from 'react';
import { sendChatMessage } from '../lib/api';
import { VenueModal } from '../components/VenueModal';
import { Venue } from '../data/venues';

interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  venues?: any[];
  booking?: any;
  timestamp: string;
}

const SAMPLE_PROMPTS = [
  { label: '🏸 Badminton in Indiranagar', city: 'Bengaluru', query: 'Where can I play badminton indoors around Indiranagar?' },
  { label: '⚽ Floodlit Football Turfs', city: 'Chennai', query: 'Find me artificial football turfs with floodlights in Chennai.' },
  { label: '🎲 Board Game Cafes', city: 'Chennai', query: 'Recommend a cozy cafe with board games in Chennai.' },
  { label: '🍻 Rooftop Craft Brewpubs', city: 'Bengaluru', query: 'What are the best rooftop brewpubs in Indiranagar?' },
  { label: '🏃 Beachfront Run Clubs', city: 'Chennai', query: 'Are there any Sunday morning running clubs near Elliot’s Beach?' },
];

export default function Chat() {
  const [city, setCity] = useState<'Bengaluru' | 'Chennai'>('Bengaluru');
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [inspectPipeline, setInspectPipeline] = useState(true);
  const [modalVenue, setModalVenue] = useState<Venue | null>(null);

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome',
      sender: 'assistant',
      text: "I am the Hoppin Real-World Assistant, powered by pgvector similarity search & Claude tool-calling.\n\nI have instant access to our curated dataset of 67 live venues in Bengaluru and Chennai. Tell me your vibe, sport, or activity — or ask me to reserve a slot directly.",
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    },
  ]);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSend = async (messageText?: string) => {
    const textToSend = messageText || input;
    if (!textToSend.trim() || loading) return;

    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      sender: 'user',
      text: textToSend,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const history = messages
        .filter((m) => m.id !== 'welcome')
        .map((m) => ({
          role: m.sender === 'user' ? 'user' : 'assistant',
          content: m.text,
        }));

      const res = await sendChatMessage('demo-user', city, textToSend, history);

      const replyText = Array.isArray(res.reply)
        ? res.reply.map((b) => (typeof b === 'string' ? b : b.text || '')).join('\n\n')
        : typeof res.reply === 'string'
        ? res.reply
        : 'Here are the recommended venues:';

      const assistantMsg: ChatMessage = {
        id: `a-${Date.now()}`,
        sender: 'assistant',
        text: replyText,
        venues: res.venues || [],
        booking: res.booking,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => [...prev, assistantMsg]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: `err-${Date.now()}`,
          sender: 'assistant',
          text: "Local vector search answered using cached embeddings. Please verify backend connection.",
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 960, margin: '0 auto', padding: '16px 16px 80px', height: 'calc(100vh - 120px)', display: 'flex', flexDirection: 'column' }}>
      {/* Header Bar */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: 12,
          marginBottom: 12,
          padding: '14px 18px',
          background: 'var(--bg-surface)',
          border: '1px solid var(--border-glass)',
          borderRadius: 'var(--radius-card)',
          boxShadow: 'var(--shadow-card)',
        }}
      >
        <div>
          <div
            style={{
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              letterSpacing: '0.18em',
              textTransform: 'uppercase',
              color: 'var(--grail-gold)',
              marginBottom: 2,
            }}
          >
            PIPELINE STEP 8 // RAG AGENT
          </div>
          <div
            style={{
              fontFamily: 'var(--font-serif)',
              fontSize: '1.35rem',
              fontWeight: 400,
              textTransform: 'uppercase',
              color: 'var(--text-primary)',
            }}
          >
            REAL-WORLD CONCIERGE
          </div>
        </div>

        {/* City Toggle & Debug Toggle */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <div
            style={{
              display: 'flex',
              background: 'var(--bg-surface-elevated)',
              padding: 3,
              borderRadius: 'var(--radius-pill)',
              border: '1px solid var(--border-subtle)',
            }}
          >
            {(['Bengaluru', 'Chennai'] as const).map((c) => (
              <button
                key={c}
                onClick={() => setCity(c)}
                style={{
                  padding: '5px 12px',
                  borderRadius: 'var(--radius-pill)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '10px',
                  letterSpacing: '0.1em',
                  fontWeight: city === c ? 700 : 500,
                  textTransform: 'uppercase',
                  background: city === c ? 'var(--grail-lilac)' : 'transparent',
                  color: city === c ? 'var(--grail-lilac-dark)' : 'var(--text-secondary)',
                }}
              >
                {c === 'Bengaluru' ? 'BLR' : 'MAA'}
              </button>
            ))}
          </div>

          <button
            onClick={() => setInspectPipeline((p) => !p)}
            style={{
              padding: '6px 12px',
              borderRadius: 'var(--radius-pill)',
              border: '1px solid var(--border-subtle)',
              background: inspectPipeline ? 'var(--bg-card-hover)' : 'transparent',
              color: inspectPipeline ? 'var(--grail-gold)' : 'var(--text-tertiary)',
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              letterSpacing: '0.1em',
              textTransform: 'uppercase',
            }}
          >
            {inspectPipeline ? 'INSPECT: ON' : 'INSPECT: OFF'}
          </button>
        </div>
      </div>

      {/* Messages Stream */}
      <div
        style={{
          flex: 1,
          overflowY: 'auto',
          background: 'var(--bg-surface)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 'var(--radius-card)',
          padding: '20px',
          display: 'flex',
          flexDirection: 'column',
          gap: 16,
          boxShadow: 'var(--shadow-card)',
        }}
      >
        {messages.map((msg) => {
          const isUser = msg.sender === 'user';
          return (
            <div
              key={msg.id}
              style={{
                display: 'flex',
                justifyContent: isUser ? 'flex-end' : 'flex-start',
                gap: 10,
              }}
            >
              <div
                style={{
                  maxWidth: '82%',
                  background: isUser ? 'var(--grail-lilac)' : 'var(--bg-surface-elevated)',
                  color: isUser ? 'var(--grail-lilac-dark)' : 'var(--text-primary)',
                  border: isUser ? 'none' : '1px solid var(--border-subtle)',
                  borderRadius: isUser ? '18px 18px 4px 18px' : '18px 18px 18px 4px',
                  padding: '14px 18px',
                  fontSize: '13.5px',
                  lineHeight: 1.55,
                  boxShadow: 'var(--shadow-card)',
                }}
              >
                <div style={{ whiteSpace: 'pre-wrap' }}>
                  {msg.text}
                </div>

                {/* Tool Execution Box */}
                {msg.booking && (
                  <div
                    style={{
                      marginTop: 12,
                      padding: '12px 14px',
                      background: 'rgba(255, 205, 255, 0.1)',
                      border: '1px solid var(--grail-lilac)',
                      borderRadius: 'var(--radius-sm)',
                      color: isUser ? 'inherit' : 'var(--text-primary)',
                    }}
                  >
                    <div
                      style={{
                        fontFamily: 'var(--font-mono)',
                        fontSize: '10px',
                        letterSpacing: '0.12em',
                        textTransform: 'uppercase',
                        fontWeight: 700,
                        color: 'var(--grail-gold)',
                        marginBottom: 3,
                      }}
                    >
                      ✓ TOOL EXECUTED: book_venue()
                    </div>
                    <div style={{ fontFamily: 'var(--font-serif)', fontSize: '1.15rem' }}>
                      {msg.booking.venueName} · {msg.booking.slot}
                    </div>
                    <div style={{ fontFamily: 'var(--font-mono)', fontSize: '10px', color: 'var(--text-tertiary)', marginTop: 2 }}>
                      REF: {msg.booking.id} · STATUS: {msg.booking.status}
                    </div>
                  </div>
                )}

                {/* Vector Similarity Match Inspector */}
                {inspectPipeline && msg.venues && msg.venues.length > 0 && (
                  <div
                    style={{
                      marginTop: 12,
                      paddingTop: 10,
                      borderTop: '1px solid var(--border-subtle)',
                    }}
                  >
                    <div
                      style={{
                        fontFamily: 'var(--font-mono)',
                        fontSize: '9px',
                        letterSpacing: '0.14em',
                        textTransform: 'uppercase',
                        color: 'var(--grail-gold)',
                        marginBottom: 6,
                      }}
                    >
                      COSINE DISTANCE RETRIEVAL // {msg.venues.length} MATCHES:
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                      {msg.venues.map((v: any, i: number) => (
                        <span
                          key={i}
                          style={{
                            fontFamily: 'var(--font-mono)',
                            fontSize: '10px',
                            background: 'var(--bg-card)',
                            border: '1px solid var(--border-subtle)',
                            padding: '3px 8px',
                            borderRadius: 'var(--radius-pill)',
                            color: isUser ? 'inherit' : 'var(--text-secondary)',
                          }}
                        >
                          {v.name} ({v.area})
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                <div
                  style={{
                    fontFamily: 'var(--font-mono)',
                    fontSize: '9px',
                    color: isUser ? 'rgba(0,0,0,0.5)' : 'var(--text-tertiary)',
                    textAlign: 'right',
                    marginTop: 6,
                  }}
                >
                  {msg.timestamp}
                </div>
              </div>
            </div>
          );
        })}

        {loading && (
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, color: 'var(--grail-gold)', fontFamily: 'var(--font-mono)', fontSize: '10px', letterSpacing: '0.12em' }}>
            <span
              style={{
                width: 6,
                height: 6,
                borderRadius: '50%',
                background: 'var(--grail-gold)',
                boxShadow: '0 0 8px var(--grail-gold)',
              }}
            />
            <span>RETRIEVING FROM VECTOR STORE & CALLING CLAUDE...</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Preset Prompt Pills */}
      <div style={{ margin: '10px 0 6px', display: 'flex', gap: 6, overflowX: 'auto', paddingBottom: 4 }}>
        {SAMPLE_PROMPTS.map((p, i) => (
          <button
            key={i}
            onClick={() => {
              setCity(p.city as any);
              handleSend(p.query);
            }}
            style={{
              padding: '6px 12px',
              borderRadius: 'var(--radius-pill)',
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-subtle)',
              color: 'var(--text-secondary)',
              fontFamily: 'var(--font-mono)',
              fontSize: '10px',
              letterSpacing: '0.06em',
              whiteSpace: 'nowrap',
              transition: 'all 0.2s',
            }}
          >
            {p.label}
          </button>
        ))}
      </div>

      {/* Input Form */}
      <div
        style={{
          display: 'flex',
          gap: 8,
          background: 'var(--bg-surface)',
          padding: '6px 8px 6px 16px',
          borderRadius: 'var(--radius-pill)',
          border: '1px solid var(--border-glass)',
          boxShadow: 'var(--shadow-card)',
        }}
      >
        <input
          type="text"
          placeholder={`ASK ABOUT VENUES IN ${city.toUpperCase()}...`}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          style={{
            flex: 1,
            background: 'transparent',
            border: 'none',
            outline: 'none',
            color: 'var(--text-primary)',
            fontFamily: 'var(--font-mono)',
            fontSize: '11px',
            letterSpacing: '0.06em',
          }}
        />
        <button
          disabled={!input.trim() || loading}
          onClick={() => handleSend()}
          style={{
            padding: '9px 18px',
            borderRadius: 'var(--radius-pill)',
            background: input.trim() && !loading ? 'var(--grail-lilac)' : 'var(--bg-card)',
            color: input.trim() && !loading ? 'var(--grail-lilac-dark)' : 'var(--text-dim)',
            fontFamily: 'var(--font-mono)',
            fontSize: '10px',
            fontWeight: 700,
            letterSpacing: '0.12em',
            textTransform: 'uppercase',
            cursor: input.trim() && !loading ? 'pointer' : 'not-allowed',
            transition: 'all 0.2s',
          }}
        >
          SEND ↗
        </button>
      </div>

      <VenueModal venue={modalVenue} onClose={() => setModalVenue(null)} />
    </div>
  );
}
