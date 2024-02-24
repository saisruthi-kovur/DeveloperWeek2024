import { query } from "./_generated/server";

export const getRecentEvents = query(async ({ db }) => {
  return await db.query("events")
                 .order("timestamp", "desc")
                 .limit(10)
                 .collect();
});
