import { Router } from 'express';
import { runChatTurn } from '../services/rag/chatAgent';

export const chatRouter = Router();

// POST /chat or POST /api/chat
chatRouter.post('/', async (req, res) => {
  const { userId, city, message, text, q, history } = req.body;
  const userMsg = message || text || q;

  if (!userMsg) {
    return res.status(400).json({ error: 'Message is required' });
  }

  try {
    const result = await runChatTurn(
      userId || 'usr_guest',
      city || 'BLR',
      userMsg,
      history || []
    );
    res.json(result);
  } catch (err: any) {
    console.error('[chat] Error processing turn:', err);
    res.status(500).json({ error: err.message || 'Failed to process chat' });
  }
});
