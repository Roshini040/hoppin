// Run once after seeding, and again whenever a venue is created/updated.
// Builds the text blob for each venue and stores its embedding for RAG search.
import { supabase } from '../src/config/db';
import { embedText } from '../src/services/rag/embed';

async function main() {
  const { data: venues, error } = await supabase.from('venues').select('*');
  if (error) throw error;

  for (const venue of venues) {
    const text = [venue.name, venue.category, venue.area, venue.description, (venue.tags || []).join(', ')]
      .filter(Boolean)
      .join('. ');

    const embedding = await embedText(text);
    await supabase.from('venues').update({ embedding }).eq('id', venue.id);
    console.log(`Embedded: ${venue.name}`);
  }
}

main();
