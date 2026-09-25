// Local, open-source embeddings -- no external API call, no API key.
// Model runs in-process via @xenova/transformers (ONNX runtime under the hood).
import { pipeline } from '@xenova/transformers';

let embedder: any = null;

async function getEmbedder() {
  if (!embedder) {
    embedder = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2');
  }
  return embedder;
}

// Returns a 384-dim vector, matching the `embedding vector(384)` column in Postgres.
export async function embedText(text: string): Promise<number[]> {
  const model = await getEmbedder();
  const output = await model(text, { pooling: 'mean', normalize: true });
  return Array.from(output.data as Float32Array);
}
