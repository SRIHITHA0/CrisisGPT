# cv_model.py
from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO("yolov8n.pt")  # can later fine-tune on disaster images

def analyze_image(image_path):
    """
    Analyzes the given image and returns disaster-related detections.
    """
    results = model(image_path)
    labels = results[0].names

    output = []
    for box in results[0].boxes:
        cls = int(box.cls)
        conf = float(box.conf)
        name = labels[cls]
        output.append({
            "label": name,
            "confidence": round(conf, 2)
        })

    return {
        "image_path": image_path,
        "detections": output
    }

if __name__ == "__main__":
    test_image = "images/default.jpg"  # Replace with your test image
    print(analyze_image(test_image))
