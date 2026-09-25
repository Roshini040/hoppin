import { Router } from 'express';

export const promosRouter = Router();

const PROMOS: Record<string, { desc: string; calculate: (amount: number) => number }> = {
  HOPPIN20: {
    desc: '20% off on all bookings',
    calculate: (amt) => Math.round(amt * 0.2)
  },
  FIRST50: {
    desc: '₹50 off for first-time explorer',
    calculate: (amt) => Math.min(50, amt)
  },
  CREW100: {
    desc: '₹100 off when booking with a crew',
    calculate: (amt) => Math.min(100, amt)
  }
};

// POST /api/promos/apply
promosRouter.post('/apply', (req, res) => {
  const { code, amount } = req.body;
  if (!code) {
    return res.status(400).json({ valid: false, error: 'Promo code is required.' });
  }

  const cleanCode = String(code).trim().toUpperCase();
  const promo = PROMOS[cleanCode];
  if (!promo) {
    return res.status(400).json({ valid: false, error: 'That promo code is not valid.' });
  }

  const baseAmount = Number(amount || 0);
  const discount = promo.calculate(baseAmount);
  const newTotal = Math.max(0, baseAmount - discount);

  res.json({
    valid: true,
    code: cleanCode,
    description: promo.desc,
    discount,
    total: newTotal
  });
});
