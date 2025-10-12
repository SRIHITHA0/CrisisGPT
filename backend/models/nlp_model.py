# models/nlp_model.py
from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")

DISASTER_KEYWORDS = {
    "flood": ["flood", "inundation", "overflow"],
    "wildfire": ["fire", "bushfire", "forest fire"],
    "earthquake": ["quake", "tremor", "seismic"],
    "storm": ["storm", "cyclone", "hurricane", "typhoon"],
    "volcano": ["eruption", "lava", "volcano"],
    "drought": ["drought", "dry spell"],
}

def analyze_text(text):
    try:
        result = classifier(text[:512])[0]
        label = result['label']
        score = round(result['score'], 3)

        detected = None
        lower_text = text.lower()
        for disaster, keywords in DISASTER_KEYWORDS.items():
            if any(word in lower_text for word in keywords):
                detected = disaster
                break

        return {
            "text": text,
            "category": detected if detected else "unknown",
            "model_label": label,
            "confidence": score
        }

    except Exception as e:
        return {"error": str(e)}
