-- Users (consumers) -- Supabase Auth handles the actual auth.users table;
-- this extends it with app-specific profile data.
create table public.users (
  id uuid primary key references auth.users(id) on delete cascade,
  phone text unique,
  name text,
  email text,
  city text check (city in ('Bengaluru', 'Chennai')),
  created_at timestamptz default now()
);

-- Venue owners / partners
create table public.partner_users (
  id uuid primary key references auth.users(id) on delete cascade,
  business_name text not null,
  payout_account jsonb,
  created_at timestamptz default now()
);

-- Admin/staff
create table public.admin_users (
  id uuid primary key references auth.users(id) on delete cascade,
  role text not null default 'staff' check (role in ('staff', 'superadmin')),
  created_at timestamptz default now()
);

-- Venues (restaurants, pubs, gaming, sports courts -- one table, category field)
create table public.venues (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid references public.partner_users(id),
  name text not null,
  category text not null check (category in ('restaurant', 'pub', 'gaming', 'sports', 'gym', 'club')),
  -- 'club' = recurring group activities (running/jogging/cycling meetups) rather than a fixed-table venue
  city text not null check (city in ('Bengaluru', 'Chennai')),
  area text not null,
  description text,
  tags text[] default '{}',            -- cuisine type / sport type / amenities
  price_tier smallint check (price_tier between 1 and 3),
  rating numeric(2,1) default 0,
  review_count int default 0,
  photos text[] default '{}',
  is_live boolean default false,
  created_at timestamptz default now()
);

-- Bookable inventory: a table, a court, or a gaming station, with its own time slots
create table public.slots (
  id uuid primary key default gen_random_uuid(),
  venue_id uuid references public.venues(id) on delete cascade,
  label text not null,                  -- "Table 4", "Court 2", "Station 7", "6 AM Run", "HIIT Class"
  capacity int default 1,               -- 1 for a table/court, N for a class or group run
  booked_count int default 0,           -- how many people/parties have joined so far
  date date not null,
  start_time time not null,
  end_time time not null,
  price numeric(10,2) not null,
  check (booked_count <= capacity)
);

-- Bookings
create table public.bookings (
  id text primary key,                  -- e.g. HOP-4821-BLR
  user_id uuid references public.users(id),
  venue_id uuid references public.venues(id),
  slot_id uuid references public.slots(id),
  party_size int,
  status text default 'upcoming' check (status in ('upcoming', 'past', 'cancelled')),
  total_amount numeric(10,2) not null,
  created_at timestamptz default now()
  -- no unique(slot_id) here anymore: a slot can hold multiple bookings (e.g. a run club
  -- session, capacity 20). bookingService.ts checks booked_count + party_size <= capacity
  -- before every insert, which is what actually prevents overbooking now.
);

-- Payments (Stripe)
create table public.payments (
  id uuid primary key default gen_random_uuid(),
  booking_id text references public.bookings(id),
  stripe_payment_intent_id text unique,
  amount numeric(10,2) not null,
  currency text default 'inr',
  status text default 'pending' check (status in ('pending', 'succeeded', 'failed', 'refunded')),
  created_at timestamptz default now()
);

-- Reviews
create table public.reviews (
  id uuid primary key default gen_random_uuid(),
  venue_id uuid references public.venues(id),
  user_id uuid references public.users(id),
  rating smallint check (rating between 1 and 5),
  text text,
  created_at timestamptz default now()
);
