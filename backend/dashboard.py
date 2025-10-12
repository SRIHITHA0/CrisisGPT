import gradio as gr
from backend.models.nlp_model import analyze_text
from backend.models.cv_model import analyze_image


def crisis_dashboard(text_input, image_input):
    # Run text and image analysis
    text_result = analyze_text(text_input)
    image_result = analyze_image(image_input)
    
    # Color code urgency
    urgency_color = {
        "high": "red",
        "medium": "orange",
        "low": "green"
    }.get(text_result["urgency"], "gray")
    
    # Prepare summary
    summary = (
        f"**🧠 Detected Type:** {text_result['type'].capitalize()}  \n"
        f"**⚠️ Urgency:** <span style='color:{urgency_color}'>{text_result['urgency'].upper()}</span>  \n"
        f"**📝 Message:** {text_result['text_analysis']}"
    )
    
    # Image info
    detected_objects = [f"{d['label']} ({d['confidence']:.2f})" for d in image_result["detections"]]
    image_summary = " | ".join(detected_objects)
    
    return summary, image_result["image_path"], f"**Detected Objects:** {image_summary}"

# Gradio Interface
demo = gr.Interface(
    fn=crisis_dashboard,
    inputs=[
        gr.Textbox(label="Disaster Report Text", placeholder="e.g. Severe flood in coastal city — immediate evacuation required!"),
        gr.Image(label="Disaster Image")
    ],
    outputs=[
        gr.Markdown(label="Text Analysis Summary"),
        gr.Image(label="Analyzed Image"),
        gr.Markdown(label="Image Detection Summary")
    ],
    title="🌍 CrisisGPT Dashboard",
    description="AI-powered disaster detection combining text + image analysis."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
