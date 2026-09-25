-- Social layer: in-app 1:1 and group chat, so planning a run/booking never needs
-- WhatsApp. Kept deliberately simple (like WhatsApp/Instagram DMs), not a full chat
-- platform: one conversations table handles both 1:1 and group by just having 2+
-- participants, and it's the same UI either way.

create table public.conversations (
  id uuid primary key default gen_random_uuid(),
  is_group boolean default false,
  name text,                              -- only used for groups, e.g. "Saturday Run Club"
  venue_id uuid references public.venues(id), -- optional: auto-created group per club/session
  created_at timestamptz default now()
);

create table public.conversation_participants (
  conversation_id uuid references public.conversations(id) on delete cascade,
  user_id uuid references public.users(id) on delete cascade,
  joined_at timestamptz default now(),
  primary key (conversation_id, user_id)
);

create table public.messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references public.conversations(id) on delete cascade,
  sender_id uuid references public.users(id),
  body text not null,
  created_at timestamptz default now()
);

-- Rewards / gamification: stars for booking, streaks for showing up, badges for
-- milestones ("5 run club sessions", "tried all 4 categories"). Simple point ledger
-- rather than a single mutable balance, so history/audit is never lost.
create table public.point_events (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.users(id),
  points int not null,                    -- positive = earned, negative = redeemed
  reason text not null,                   -- 'booking_completed', 'streak_bonus', 'badge_unlocked', etc.
  booking_id text references public.bookings(id),
  created_at timestamptz default now()
);

create table public.badges (
  id uuid primary key default gen_random_uuid(),
  code text unique not null,              -- 'first_booking', 'five_run_sessions', 'category_explorer'
  name text not null,
  description text,
  icon text                               -- emoji or icon name, keep it simple
);

create table public.user_badges (
  user_id uuid references public.users(id),
  badge_id uuid references public.badges(id),
  earned_at timestamptz default now(),
  primary key (user_id, badge_id)
);

-- A user's current point balance, computed from the ledger -- always accurate,
-- never drifts out of sync with individual point_events rows.
create or replace function user_point_balance(uid uuid)
returns int language sql stable as $$
  select coalesce(sum(points), 0) from public.point_events where user_id = uid;
$$;
