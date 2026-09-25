import { Request, Response, NextFunction } from 'express';
import { supabase } from '../config/db';

// Verifies the Supabase-issued JWT sent from the frontend (phone/OTP or partner/admin login).
export async function requireAuth(req: Request, res: Response, next: NextFunction) {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (!token) return res.status(401).json({ error: 'Missing auth token' });

  const { data, error } = await supabase.auth.getUser(token);
  if (error || !data.user) return res.status(401).json({ error: 'Invalid session' });

  (req as any).user = data.user;
  next();
}
