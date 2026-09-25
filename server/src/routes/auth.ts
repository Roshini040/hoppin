import { Router } from 'express';
import { store, User } from '../services/store';

export const authRouter = Router();

function hashPw(pw: string): string {
  return Buffer.from(pw).toString('base64');
}

// POST /api/auth/signup
authRouter.post('/signup', (req, res) => {
  const { name, email, password } = req.body;
  if (!email || !password || !name) {
    return res.status(400).json({ error: 'Name, email, and password are required.' });
  }

  const cleanEmail = String(email).trim().toLowerCase();
  if (store.users[cleanEmail]) {
    return res.status(400).json({ error: 'An account with that email already exists. Sign in instead.' });
  }

  if (password.length < 6) {
    return res.status(400).json({ error: 'Password must be at least 6 characters.' });
  }

  const user: User = {
    id: `usr_${Date.now()}_${Math.floor(Math.random() * 1000)}`,
    email: cleanEmail,
    name: String(name).trim(),
    passwordHash: hashPw(password),
    createdAt: Date.now()
  };

  store.users[cleanEmail] = user;
  store.save();

  const token = `tok_${user.id}_${Date.now()}`;
  res.json({
    token,
    user: { id: user.id, name: user.name, email: user.email }
  });
});

// POST /api/auth/login
authRouter.post('/login', (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required.' });
  }

  const cleanEmail = String(email).trim().toLowerCase();
  const user = store.users[cleanEmail];
  if (!user || user.passwordHash !== hashPw(password)) {
    return res.status(401).json({ error: 'Invalid email or password.' });
  }

  const token = `tok_${user.id}_${Date.now()}`;
  res.json({
    token,
    user: { id: user.id, name: user.name, email: user.email }
  });
});

// POST /api/auth/guest
authRouter.post('/guest', (req, res) => {
  const guestEmail = 'guest@hoppin.demo';
  let user = store.users[guestEmail];
  if (!user) {
    user = {
      id: 'usr_guest',
      email: guestEmail,
      name: 'Guest',
      passwordHash: hashPw('guest-demo'),
      createdAt: Date.now()
    };
    store.users[guestEmail] = user;
    store.save();
  }

  const token = `tok_${user.id}_guest`;
  res.json({
    token,
    user: { id: user.id, name: user.name, email: user.email }
  });
});

// GET /api/auth/me
authRouter.get('/me', (req, res) => {
  const authHeader = req.headers.authorization;
  const emailQuery = req.query.email as string | undefined;

  let email = emailQuery ? String(emailQuery).toLowerCase() : undefined;
  if (!email && authHeader && authHeader.startsWith('Bearer ')) {
    const token = authHeader.slice(7);
    // Find matching user
    const found = Object.values(store.users).find(u => token.includes(u.id));
    if (found) email = found.email;
  }

  if (!email || !store.users[email]) {
    return res.status(401).json({ error: 'Not authenticated' });
  }

  const user = store.users[email];
  res.json({
    user: { id: user.id, name: user.name, email: user.email }
  });
});
