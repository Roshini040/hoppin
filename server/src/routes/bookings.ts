import { Router } from 'express';
import { store, Booking, slotPrice, newRef, toMin, fromISO, todayISO } from '../services/store';

export const bookingsRouter = Router();

const FEE = 30;

function isPast(b: Booking): boolean {
  try {
    const slotTime = toMin(b.slot);
    const dateObj = fromISO(b.iso);
    const bookingTimeMs = dateObj.getTime() + slotTime * 60 * 1000;
    return bookingTimeMs < Date.now();
  } catch {
    return false;
  }
}

// GET /api/bookings?email=user@example.com
bookingsRouter.get('/', (req, res) => {
  const email = (req.query.email as string)?.trim().toLowerCase();
  if (!email) {
    return res.json({ upcoming: [], past: [], stats: { upcoming: 0, past: 0, saved: 0, spent: 0 } });
  }

  const userBookings = store.bookings.filter(b => b.userEmail === email && b.status !== 'cancelled');

  const upcoming = userBookings.filter(b => !isPast(b));
  const past = userBookings.filter(b => isPast(b));
  const savedCount = (store.saved[email] || []).length;
  const spent = userBookings.reduce((sum, b) => sum + (b.total || 0), 0);

  res.json({
    bookings: userBookings,
    upcoming,
    past,
    stats: {
      upcoming: upcoming.length,
      past: past.length,
      saved: savedCount,
      spent
    }
  });
});

// POST /api/bookings
bookingsRouter.post('/', (req, res) => {
  try {
    const { venueId, iso, slot, partySize, promoCode, userEmail, userName, card, disc } = req.body;

    if (!venueId || !iso || !slot) {
      return res.status(400).json({ error: 'Venue, date, and slot are required.' });
    }

    const email = (userEmail || 'guest@hoppin.demo').trim().toLowerCase();
    const venue = store.getVenue(venueId);
    if (!venue) {
      return res.status(404).json({ error: 'Venue not found.' });
    }

    // Check availability
    const avail = store.getSlotAvailability(venue, iso, slot, email);
    if (avail.state === 'yours') {
      return res.status(400).json({ error: 'You have already booked this slot.' });
    }
    if (avail.state === 'full') {
      return res.status(400).json({ error: 'This slot is already fully booked.' });
    }
    if (avail.state === 'past') {
      return res.status(400).json({ error: 'This slot has already passed.' });
    }

    const basePrice = slotPrice(venue, slot);
    let discount = Number(disc || 0);

    // Validate promo code if provided
    if (promoCode) {
      const code = String(promoCode).trim().toUpperCase();
      if (code === 'HOPPIN20') discount = Math.round(basePrice * 0.2);
      else if (code === 'FIRST50') discount = 50;
      else if (code === 'CREW100') discount = 100;
    }

    const total = Math.max(0, basePrice + FEE - discount);
    const ref = newRef();
    const last4 = card ? String(card).replace(/\D/g, '').slice(-4) : '4242';

    const booking: Booking = {
      id: ref,
      ref,
      userEmail: email,
      userName: userName || store.users[email]?.name || 'Guest',
      venueId: venue.id,
      venueName: venue.name,
      cityName: venue.cityName,
      area: venue.area,
      iso,
      slot,
      partySize: Number(partySize) || 1,
      price: basePrice,
      fee: FEE,
      disc: discount,
      total,
      status: 'upcoming',
      createdAt: Date.now(),
      last4
    };

    store.bookings.unshift(booking);
    store.save();

    console.log(`[bookings] Created booking ${ref} for ${email} at ${venue.name} (${iso} ${slot})`);
    res.json({ success: true, booking, ref });
  } catch (err: any) {
    res.status(500).json({ error: err.message || 'Failed to create booking' });
  }
});

// POST /api/bookings/:ref/reschedule
bookingsRouter.post('/:ref/reschedule', (req, res) => {
  const { ref } = req.params;
  const { iso, slot } = req.body;

  const booking = store.bookings.find(b => b.ref === ref);
  if (!booking) {
    return res.status(404).json({ error: 'Booking not found.' });
  }

  const venue = store.getVenue(booking.venueId);
  if (!venue) {
    return res.status(404).json({ error: 'Venue not found.' });
  }

  const avail = store.getSlotAvailability(venue, iso, slot, booking.userEmail);
  if (avail.state === 'full' || avail.state === 'past') {
    return res.status(400).json({ error: 'Selected slot is not available for reschedule.' });
  }

  booking.iso = iso;
  booking.slot = slot;
  store.save();

  console.log(`[bookings] Rescheduled booking ${ref} to ${iso} ${slot}`);
  res.json({ success: true, booking });
});

// POST /api/bookings/:ref/cancel or DELETE /api/bookings/:ref
const handleCancel = (req: any, res: any) => {
  const { ref } = req.params;
  const booking = store.bookings.find(b => b.ref === ref);
  if (!booking) {
    return res.status(404).json({ error: 'Booking not found.' });
  }

  booking.status = 'cancelled';
  store.save();

  console.log(`[bookings] Cancelled booking ${ref}`);
  res.json({ success: true, message: 'Booking cancelled successfully.' });
};

bookingsRouter.post('/:ref/cancel', handleCancel);
bookingsRouter.delete('/:ref', handleCancel);

// POST /api/bookings/:ref/rate
bookingsRouter.post('/:ref/rate', (req, res) => {
  const { ref } = req.params;
  const { rating, comment } = req.body;
  const rateNum = Number(rating);

  if (!rateNum || rateNum < 1 || rateNum > 5) {
    return res.status(400).json({ error: 'Rating must be between 1 and 5 stars.' });
  }

  const booking = store.bookings.find(b => b.ref === ref);
  if (!booking) {
    return res.status(404).json({ error: 'Booking not found.' });
  }

  booking.rating = rateNum;
  store.reviews[ref] = rateNum;
  store.save();

  console.log(`[bookings] Rated booking ${ref} with ${rateNum} stars`);
  res.json({ success: true, rating: rateNum });
});
