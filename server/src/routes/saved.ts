import { Router } from 'express';
import { store } from '../services/store';

export const savedRouter = Router();

// GET /api/saved?email=user@example.com
savedRouter.get('/', (req, res) => {
  const email = (req.query.email as string)?.trim().toLowerCase();
  if (!email) return res.json({ saved: [] });
  res.json({ saved: store.saved[email] || [] });
});

// POST /api/saved/toggle
savedRouter.post('/toggle', (req, res) => {
  const { email, venueId } = req.body;
  if (!email || !venueId) {
    return res.status(400).json({ error: 'Email and venueId are required.' });
  }

  const cleanEmail = String(email).trim().toLowerCase();
  const list = store.saved[cleanEmail] || [];
  const exists = list.includes(venueId);

  let updatedList: string[];
  if (exists) {
    updatedList = list.filter(id => id !== venueId);
  } else {
    updatedList = [...list, venueId];
  }

  store.saved[cleanEmail] = updatedList;
  store.save();

  res.json({
    saved: !exists,
    venueIds: updatedList
  });
});
