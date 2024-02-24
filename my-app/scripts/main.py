import os
from dotenv import load_dotenv
from convex import ConvexClient
# Import the AI data processing function
from ai_data_processing import process_event_data

def fetch_recent_events():
    load_dotenv(".env.local")
    client = ConvexClient(os.getenv("CONVEX_URL"))
    recent_events = client.query("events:getRecentEvents")
    return recent_events

def main():
    events = fetch_recent_events()
    # Process the events with the AI data processing module
    processed_events = process_event_data(events)
    # Now you can print the processed events or do something else with them
    print(processed_events)

if __name__ == "__main__":
    main()