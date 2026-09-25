import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

// Creates a Stripe PaymentIntent for a booking. The client confirms it with
// Stripe.js using the returned client_secret -- card details never touch our server.
export async function createPaymentIntent(bookingId: string, amount: number) {
  const intent = await stripe.paymentIntents.create({
    amount: Math.round(amount * 100), // paise
    currency: 'inr',
    metadata: { bookingId },
    automatic_payment_methods: { enabled: true }, // enables UPI, cards, wallets
  });
  return intent;
}
