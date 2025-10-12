import requests
import time
from models.nlp_model import analyze_text

CHECK_INTERVAL = 300  # seconds between API checks (5 minutes)
LIMIT = 10

def stream_disaster_events():
    seen_events = set()  # Keep track of events we've already printed

    print("🌍 Streaming disaster-related events via NASA EONET (live)...\n")

    while True:
        try:
            url = "https://eonet.gsfc.nasa.gov/api/v3/events"
            response = requests.get(url)
            data = response.json()

            new_count = 0
            for event in data["events"]:
                if new_count >= LIMIT:
                    break

                event_id = event["id"]
                if event_id in seen_events:
                    continue  # Skip events we've already shown

                title = event["title"]
                categories = ", ".join([cat["title"] for cat in event["categories"]])
                print(f"\nEvent: {title}")
                print(f"Categories: {categories}")

                # Analyze the title using your NLP model
                result = analyze_text(title)
                print("Analysis:", result)

                seen_events.add(event_id)
                new_count += 1

            print(f"\n⏳ Waiting {CHECK_INTERVAL} seconds for new events...\n")
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print("❌ Error fetching events:", e)
            print("⏳ Retrying in 60 seconds...\n")
            time.sleep(60)

if __name__ == "__main__":
    stream_disaster_events()
