import { supabase } from '../config/db';

interface BookVenueInput {
  venue_id: string;
  slot_id: string;
  party_size?: number;
}

// Works for both kinds of slot: a 1-capacity table/court (party_size must fit in 1 spot),
// and a group slot like a gym class or run-club session (capacity N, many separate
// bookings can share it as long as the total headcount stays under capacity).
// The check() constraint on slots.booked_count in migration 0001 is the last line of
// defense against a race condition; this check is what gives a clean error message.
export async function createBooking(userId: string, input: BookVenueInput) {
  const { data: slot } = await supabase.from('slots').select('*').eq('id', input.slot_id).single();
  if (!slot) throw new Error('Slot not found');

  const partySize = input.party_size ?? 1;
  if (slot.booked_count + partySize > slot.capacity) {
    throw new Error('Not enough spots left in this slot');
  }

  const bookingId = `HOP-${Math.floor(1000 + Math.random() * 9000)}-BLR`;

  const { data, error } = await supabase.from('bookings').insert({
    id: bookingId,
    user_id: userId,
    venue_id: input.venue_id,
    slot_id: input.slot_id,
    party_size: partySize,
    total_amount: slot.price,
  }).select().single();

  if (error) throw new Error('Could not create booking -- please try again.');

  const { error: slotError } = await supabase
    .from('slots')
    .update({ booked_count: slot.booked_count + partySize })
    .eq('id', input.slot_id)
    .eq('booked_count', slot.booked_count); // optimistic lock: fails if someone else booked in between

  if (slotError) {
    await supabase.from('bookings').delete().eq('id', bookingId); // roll back
    throw new Error('This slot filled up just now -- please pick another.');
  }

  return data;
}
