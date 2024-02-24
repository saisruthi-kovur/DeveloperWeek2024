import json
import random
from datetime import datetime, timedelta

# Define basic parameters for the data generation
NUM_EVENTS = 1000  # Total number of events to generate
START_DATE = datetime(2023, 1, 1)  # Start date for events
DAYS_SPAN = 90  # Span of days over which events are generated

# Potential values for different event types
pages = ["/home", "/products", "/contact", "/about"]
products = [str(i) for i in range(1, 101)]  # Simulate 100 different product IDs
feedback_texts = ["Love it!", "Could be better.", "Fantastic product.", "Not what I expected."]
sign_ups = ["User"+str(i) for i in range(1, 201)]  # Simulate 200 different user names

def generate_event(timestamp):
    event_type = random.choice(["pageView", "click", "feedback", "signUp"])
    event = {"timestamp": timestamp.isoformat()}

    if event_type == "pageView":
        event.update({"eventType": "pageView", "url": random.choice(pages)})
    elif event_type == "click":
        event.update({"eventType": "click", "url": "/product/" + random.choice(products)})
    elif event_type == "feedback":
        event.update({"eventType": "feedback", "text": random.choice(feedback_texts)})
    elif event_type == "signUp":
        event.update({"eventType": "signUp", "userName": random.choice(sign_ups)})

    return event

def generate_sample_data(filename="sampleData.jsonl"):
    with open(filename, 'w') as file:
        for _ in range(NUM_EVENTS):
            days_offset = random.randrange(DAYS_SPAN)
            timestamp = START_DATE + timedelta(days=days_offset)
            event = generate_event(timestamp)
            file.write(json.dumps(event) + '\n')

generate_sample_data()
