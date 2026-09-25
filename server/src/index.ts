import express from 'express';
import cors from 'cors';
import { venuesRouter } from './routes/venues';
import { bookingsRouter } from './routes/bookings';
import { chatRouter } from './routes/chat';
import { authRouter } from './routes/auth';
import { promosRouter } from './routes/promos';
import { savedRouter } from './routes/saved';
import { clubsRouter } from './routes/clubs';
import { adminRouter } from './routes/admin';
import { store } from './services/store';

const app = express();

app.use(cors({
  origin: true,
  credentials: true
}));

app.use(express.json());

// Request logger
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString().split('T')[1].slice(0, 8)}] ${req.method} ${req.url}`);
  next();
});

// Health checks
app.get('/health', (req, res) => res.json({ status: 'ok', venues: store.venues.length }));
app.get('/api/health', (req, res) => res.json({ status: 'ok', venues: store.venues.length }));

// Mount routes at /api/
app.use('/api/venues', venuesRouter);
app.use('/api/bookings', bookingsRouter);
app.use('/api/chat', chatRouter);
app.use('/api/auth', authRouter);
app.use('/api/promos', promosRouter);
app.use('/api/saved', savedRouter);
app.use('/api/clubs', clubsRouter);
app.use('/api/admin', adminRouter);

// Also mount at root for backward compatibility with existing clients
app.use('/venues', venuesRouter);
app.use('/bookings', bookingsRouter);
app.use('/chat', chatRouter);
app.use('/auth', authRouter);
app.use('/promos', promosRouter);
app.use('/saved', savedRouter);
app.use('/clubs', clubsRouter);
app.use('/admin', adminRouter);

// Global error handler
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error('[server error]', err);
  res.status(500).json({ error: err?.message || 'Internal server error' });
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`===============================================`);
  console.log(`✨ Hoppin API running on http://localhost:${port}`);
  console.log(`📍 67 Venues ready (Bengaluru 29, Chennai 38)`);
  console.log(`Endpoints: /api/venues, /api/bookings, /api/chat, /api/auth, /api/promos, /api/saved`);
  console.log(`===============================================`);
});
