# Architecture

## System overview

```
apps/web (consumer)  ─┐
apps/partner          ├──►  server (Express API)  ──►  Supabase Postgres (+ pgvector)
apps/admin            ┘            │
                                    └──►  Stripe (payments)
                                    └──►  Claude API (chat generation, tool-calling)
```

## Open source notes

Everything is open source except two pieces that can't be, by nature of what they do:
- **Stripe** — moving real money requires a licensed, PCI-compliant processor. There's no
  open-source substitute for this; every production payments stack (even ones built on
  open-source frameworks) uses a processor like Stripe.
- **Claude API** — for chat quality/reliability. If you want a 100% open-source stack
  including the LLM, swap `chatAgent.ts` to call a self-hosted **Ollama** instance running
  an open model (e.g. Llama 3.1) instead of the Anthropic SDK — the RAG retrieval layer
  (pgvector + embeddings) stays identical either way, only the generation call changes.

Everything else — React, Express, Postgres, Supabase, pgvector, the embedding model
(`@xenova/transformers`, runs locally, no API key) — is open source.

## RAG chatbot design

The assistant doesn't just call an LLM cold — it retrieves real venue data first, so it
never hallucinates a restaurant that doesn't exist or a rating that isn't real.

**1. Ingestion (`server/scripts/ingestVenues.ts`, run on venue create/update)**
- Take each venue's name, category, cuisine/sport, area, description, and recent reviews
- Concatenate into one text blob
- Embed it locally with `@xenova/transformers` (`Xenova/all-MiniLM-L6-v2`, 384-dim, no API cost)
- Store the vector in `venues.embedding` (a `pgvector` column)

**2. Retrieval (`server/src/services/rag/retrieve.ts`)**
- User message comes in (e.g. "best pubs in Indiranagar")
- Embed the user's message with the same model
- Run a cosine-similarity search via the `match_venues` Postgres function (see migration 0002)
- Get back the top-k most relevant venues, with real ratings/prices/availability

**3. Generation (`server/src/services/rag/chatAgent.ts`)**
- Pass the retrieved venues as context to Claude, along with the conversation history
- Give Claude a `book_venue` tool it can call — so it can go from "book me a table for
  tonight" straight to creating a real booking via `bookingService.ts`, not just suggesting one
- Claude replies in natural language; if it called `book_venue`, the server executes the
  real booking and confirms it back in the same turn

This is the same pattern whether it's "find me a badminton court" or "find me South Indian
food" — one retrieval pipeline, one venues table, category is just a filter.

## Booking integrity

`supabase/migrations/0001_init_schema.sql` uses a unique constraint on
`(venue_id, slot_id, date, time)` in `bookings`, so two people can't double-book the same
table/court/station — the database rejects the second write rather than the app trying to
catch the race condition itself.
