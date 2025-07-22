## 🗾 Japanese Voice Weather Chatbot
This is a voice-enabled chatbot that listens to Japanese speech, fetches real-time weather data, and generates smart, AI-powered suggestions to enhance the user experience.

## 🚀 Features
- 🎙️ Japanese voice input using microphone
- 🗣️ Real-time speech-to-text transcription using Whisper  
- ☁️ Real-time weather info using WeatherAPI  
- 🤖 AI-generated suggestions using IBM WatsonX (Llama 3-3-70B)
- 🌐 Web-based UI using Gradio

## ⚙️ Environment Variables

Before running, create a .env file or export the following variables in your terminal:

Set the following environment variables:
   - `WEATHER_API_KEY=your_weatherapi_key`
   - `IBM_API_KEY=your_ibm_api_key`
   - `IBM_PROJECT_ID=your_ibm_project_id`
   - `MODEL_ID=your_model_id`
   - `URL=your_model_endpoint_url`   

## 🧪 Setup
1.Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2.Install dependencies:   
```bash
pip install -r requirements.txt
```

3.Run the app:
```bash
python app.py
```

## 🎯 Example Use Cases (based on weather and AI suggestions)  
🌤️ Travel recommendations: Suggests nearby places to visit based on the weather  
👗 Fashion tips: Recommends clothing appropriate for today’s temperature and rain conditions  
🎵 Mood-based music: Suggests playlists matching the weather (e.g., chill music on rainy days)  
🏃‍♂️ Outdoor activity advice: Recommends safe times or gear for exercise or farming  
🚫 Rain alerts: Warns users to carry an umbrella or delay travel  

# 📝 Notes  
1. Works best with a stable internet connection and a good quality mic.  
2. Outputs AI suggestions based on current weather and location.  
