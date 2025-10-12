import os
import random

BASE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "images")

DISASTER_IMAGES = {
    "flood": os.path.join(BASE_IMAGE_PATH, "floods"),
    "wildfire": os.path.join(BASE_IMAGE_PATH, "wildfires"),
    "earthquake": os.path.join(BASE_IMAGE_PATH, "earthquakes"),
    "storm": os.path.join(BASE_IMAGE_PATH, "storms"),
}

def get_random_image(disaster_type):
    """Return a random image path for a disaster type."""
    folder = DISASTER_IMAGES.get(disaster_type)
    if not folder or not os.path.exists(folder):
        return None
    images = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith((".jpg", ".png"))]
    if not images:
        return None
    return random.choice(images)
