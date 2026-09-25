import Anthropic from '@anthropic-ai/sdk';
import { retrieveRelevantVenues, RetrievedVenue } from './retrieve';
import { store, Venue, slotPrice, newRef, todayISO, toISO, fromISO, toMin } from '../store';

let anthropicClient: Anthropic | null = null;
if (process.env.ANTHROPIC_API_KEY) {
  try {
    anthropicClient = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  } catch (e) {
    console.warn('[chatAgent] Failed to init Anthropic client:', e);
  }
}

const bookVenueTool = {
  name: 'book_venue',
  description: 'Create a real booking for a venue slot on behalf of the user.',
  input_schema: {
    type: 'object' as const,
    properties: {
      venue_id: { type: 'string' },
      slot_id: { type: 'string' },
      date: { type: 'string' },
      party_size: { type: 'number' },
    },
    required: ['venue_id', 'slot_id'],
  },
};

function dayLabel(iso: string): string {
  const t = todayISO();
  if (iso === t) return 'today';
  const d = new Date();
  d.setDate(d.getDate() + 1);
  if (iso === toISO(d)) return 'tomorrow';
  const x = fromISO(iso);
  const WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const MO = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return `${WD[x.getDay()]} ${x.getDate()} ${MO[x.getMonth()]}`;
}

export async function runChatTurn(
  userId: string,
  city: string,
  message: string,
  history: any[] = []
) {
  const low = message.toLowerCase().trim();

  // 1. Auto-detect city from user message if explicitly mentioned
  let targetCity = city;
  const hasBLR = /\b(bengaluru|bangalore|blr|indiranagar|koramangala|whitefield|cubbon)\b/i.test(low);
  const hasMAA = /\b(chennai|maa|adyar|besant|kilpauk|t\.?\s*nagar|mylapore|egmore|omr|velachery)\b/i.test(low);
  if (hasMAA && !hasBLR) targetCity = 'MAA';
  else if (hasBLR && !hasMAA) targetCity = 'BLR';

  // 2. Retrieve relevant venues using semantic scoring
  const venues = await retrieveRelevantVenues(message, targetCity, 4);

  // 3. If Claude API Key is provided, use Anthropic model
  if (anthropicClient) {
    try {
      const system = `You are the hoppin concierge, an expert guide for verified courts, taprooms, game cafes, gyms, and run clubs across Bengaluru and Chennai.
Recommend venues ONLY from the list below — never invent a venue, rating, or price that isn't in this list.
Always be concise, friendly, and practical. Highlight prices in ₹, ratings ★, and location. If the user wants to book, use the book_venue tool.

Available venues matching "${message}" in ${targetCity}:
${JSON.stringify(venues, null, 2)}`;

      const response = await anthropicClient.messages.create({
        model: 'claude-sonnet-4-6',
        max_tokens: 1000,
        system,
        messages: [...history, { role: 'user', content: message }],
        tools: [bookVenueTool],
      });

      const toolUse = response.content.find((b: any) => b.type === 'tool_use');
      const textBlock = response.content.find((b: any) => b.type === 'text');
      const text = textBlock ? textBlock.text : '';

      if (toolUse && toolUse.name === 'book_venue') {
        const input: any = toolUse.input;
        const v = store.getVenue(input.venue_id) || venues[0]?.venue;
        const targetVenue = v || store.venues[0];
        const dateIso = input.date || todayISO();
        const slot = input.slot_id || targetVenue.slots[0];
        const amt = slotPrice(targetVenue, slot);
        const ref = newRef();

        const toolObj = {
          name: 'book_venue',
          args: { venue_id: targetVenue.id, date: dateIso, slot },
          result: { status: 'held', ref, amount_inr: amt, expires_in: '10:00' },
          order: { venueId: targetVenue.id, iso: dateIso, slot, price: amt, ref }
        };

        return {
          reply: response.content,
          text,
          venues,
          hits: venues.map(v => v.id),
          tool: toolObj,
          trace: {
            query: message,
            hits: venues.map(v => ({ v: v.venue || v, d: +(1 - v.similarity).toFixed(3) })),
            tool: true
          }
        };
      }

      return {
        reply: response.content,
        text,
        venues,
        hits: venues.map(v => v.id),
        trace: {
          query: message,
          hits: venues.map(v => ({ v: v.venue || v, d: +(1 - v.similarity).toFixed(3) })),
          tool: false
        }
      };
    } catch (e) {
      console.warn('[chatAgent] Claude API call failed, falling back to enhanced local reasoning:', e);
    }
  }

  // 4. Enhanced local RAG reasoning
  const isGreeting = /^(hi|hello|hey|yo|namaste|vanakkam|good\s*(morning|evening|afternoon)|sup|start|help)\b/i.test(low);
  const isBooking = /\b(book|reserve|hold|grab|lock|schedule|pay)\b/i.test(low);
  const isPricing = /\b(price|pricing|cost|how much|fee|cheap|budget|rate)\b/i.test(low);
  const isTonight = /\b(tonight|today|now|evening|open tonight)\b/i.test(low);

  let replyText = '';
  let toolData: any = undefined;
  let hits = venues.map(v => v.id);

  if (isGreeting && !isBooking) {
    const cityName = targetCity === 'MAA' ? 'Chennai' : 'Bengaluru';
    replyText = `Hey there! 👋 I’m your **hoppin. AI Concierge**. I have real-time access to all 67 curated venues across **Bengaluru** and **Chennai** with live slots and instant UPI / card checkout.

Here are popular ways to explore:
• 🏸 **Badminton & Turfs:** *"Best floodlit turf in Indiranagar"* or *"Badminton in Chennai"*
• 🍺 **Craft Breweries:** *"Top rooftop craft beer taproom tonight"*
• 🎲 **Board Games:** *"Board game cafe with 1,000+ games"*
• 🏋️ **Fitness & Wellness:** *"Gym with pink salt sauna"*
• 🏃 **Social Run Clubs:** *"Sunrise run club near the beach"*

What would you like to explore or book today?`;
  } else if (isBooking && venues.length > 0) {
    const targetVenue = venues[0].venue || store.getVenue(venues[0].id) || store.venues[0];
    const nextSlot = store.nextOpen(targetVenue);
    const dateIso = nextSlot ? nextSlot.iso : todayISO();
    const slotTime = nextSlot ? nextSlot.slot : targetVenue.slots[0];
    const amt = slotPrice(targetVenue, slotTime);
    const ref = newRef();

    replyText = `🎯 Held <strong>${slotTime}</strong> on <strong>${dayLabel(dateIso)}</strong> at <strong>${targetVenue.name}</strong> (${targetVenue.area}) for <strong>₹${amt}</strong>.<br><br>Your hold is active for the next 10 minutes. Click below to pay via <strong>UPI (GPay / PhonePe / Paytm / QR)</strong> or Card and confirm your ticket instantly!`;

    toolData = {
      name: 'book_venue',
      args: { venue_id: targetVenue.id, date: dateIso, slot: slotTime },
      result: { status: 'held', ref, amount_inr: amt, expires_in: '10:00' },
      order: { venueId: targetVenue.id, iso: dateIso, slot: slotTime, price: amt, ref }
    };
  } else if (venues.length > 0) {
    const cityName = targetCity === 'MAA' ? 'Chennai' : 'Bengaluru';
    const first = venues[0];
    const firstVenue = first.venue || store.getVenue(first.id);
    const nextSlot = firstVenue ? store.nextOpen(firstVenue) : null;

    replyText = `Found **${venues.length} top verified spots** in ${cityName}:<br><br>`;

    // Spotlight primary match
    replyText += `🌟 **${first.name}** (${first.area}) — ★ ${first.rating.toFixed(1)}<br>`;
    replyText += `• **Rate:** from ₹${firstVenue?.price || 800}/hr<br>`;
    replyText += `• **Vibe:** ${firstVenue?.tags.slice(0, 3).join(' · ')}<br>`;
    if (nextSlot) {
      replyText += `• **Next Open Slot:** ${nextSlot.slot} (${dayLabel(nextSlot.iso)})<br>`;
    }
    replyText += `<br>`;

    // Secondary matches
    if (venues.length > 1) {
      replyText += `**Other great options:**<br>`;
      for (const h of venues.slice(1)) {
        const vObj = h.venue || store.getVenue(h.id);
        replyText += `• **${h.name}** (${h.area}) — ★ ${h.rating.toFixed(1)} · ₹${vObj?.price || 750}/hr<br>`;
      }
      replyText += `<br>`;
    }

    replyText += `💡 *Tip: Click any card below to see photos & pick your slot, or say **“book ${first.name.split(' ')[0]}”** to hold a spot immediately!*`;
  } else {
    replyText = `I couldn't find an exact match for that specific wording among the 67 venues on hoppin.

Try asking by:
• **Activity:** *badminton*, *football turf*, *craft beer*, *board games*, *crossfit*, *yoga*
• **Area:** *Indiranagar*, *Koramangala*, *Besant Nagar*, *Adyar*, *Kilpauk*, *Whitefield*
• **Filter:** *open tonight*, *under ₹800*, *outdoor courts*`;
  }

  const traceData = {
    query: message,
    hits: venues.map(v => ({ v: v.venue || v, d: +(1 - v.similarity).toFixed(3) })),
    tool: !!toolData
  };

  return {
    reply: [{ type: 'text', text: replyText }],
    text: replyText,
    venues,
    hits,
    tool: toolData,
    trace: traceData
  };
}
