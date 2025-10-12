# disaster_analyzer.py

from models.nlp_model import analyze_text
from models.cv_model import analyze_image

def analyze_disaster(text, image_path):
    # Analyze text
    text_result = analyze_text(text)
    
    # Analyze image
    image_result = analyze_image(image_path)
    
    # Combine results
    disaster_report = {
        "text_analysis": text_result,
        "image_analysis": image_result
    }
    
    return disaster_report

# Example usage
if __name__ == "__main__":
    sample_text = "Severe flood in coastal city — immediate evacuation required!"
    sample_image = "models/sample_disaster.jpg"  # Make sure path is correct
    report = analyze_disaster(sample_text, sample_image)
    print(report)
