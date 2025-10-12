from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

NASA_API_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"

@app.route("/")
def home():
    return jsonify({"message": "🌍 CrisisGPT Backend Running with NASA Data!"})

@app.route("/disasters", methods=["GET"])
def get_disasters():
    """
    Fetch events from NASA EONET API and return JSON for frontend.
    """
    try:
        response = requests.get(NASA_API_URL)
        data = response.json()

        events = []
        for event in data.get("events", []):
            if event.get("geometry"):
                latest_geo = event["geometry"][-1]
                coords = latest_geo["coordinates"]
                title = event["title"]
                category = event["categories"][0]["title"]
                events.append({
                    "id": event["id"],
                    "title": title,
                    "category": category,
                    "coordinates": coords
                })

        return jsonify({"events": events})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
