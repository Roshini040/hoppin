-- Open-source vector search for the RAG chatbot
create extension if not exists vector;

alter table public.venues add column embedding vector(384); -- matches all-MiniLM-L6-v2 output size

-- Similarity search function, called from server/src/services/rag/retrieve.ts
create or replace function match_venues (
  query_embedding vector(384),
  match_city text,
  match_count int default 5
)
returns table (
  id uuid,
  name text,
  category text,
  area text,
  description text,
  tags text[],
  price_tier smallint,
  rating numeric,
  similarity float
)
language sql stable
as $$
  select
    v.id, v.name, v.category, v.area, v.description, v.tags, v.price_tier, v.rating,
    1 - (v.embedding <=> query_embedding) as similarity
  from public.venues v
  where v.city = match_city and v.is_live = true
  order by v.embedding <=> query_embedding
  limit match_count;
$$;

create index on public.venues using ivfflat (embedding vector_cosine_ops) with (lists = 100);
