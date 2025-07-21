import gradio as gr
from utils.weather import get_weather
from utils.transcribe import transcribe_audio
from utils.chat import generate_suggestion
from utils.chat import extract_city 

def process_input(audio):
    # Transcribe audio to Japanese text
    text = transcribe_audio(audio)
    
    # Extract city name from transcript using WatsonX
    city = extract_city(text)
    
    # Get weather info using extracted city
    weather = get_weather(city)
    
    # Generate suggestion using WatsonX AI Model
    suggestion = generate_suggestion(text, weather)
    
    # Final output
    return f"""
    🏙️ **検出された都市**
    {city}

    🌤️ **天気情報**  
    {weather}

    🤖 **生成AIからの提案**  
    {suggestion}
    """

demo = gr.Interface(
    fn=process_input,
    inputs = gr.Audio(type="filepath", label="日本語で話してください"),
    outputs="text",
    title="⛅ AI天気アシスタント",
    description="🎙️ 日本語で話しかけるだけで、AIがあなたの都市を認識し、現在の天気とスマートなアドバイスをお届けします.",
    allow_flagging="never" 
)

if __name__ == "__main__":
    demo.launch()
