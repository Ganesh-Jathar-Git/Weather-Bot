import openai
import os

# Set your OpenAI API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIWhisperWrapper:
    def __init__(self, model_name="whisper-1"):
        self.model_name = model_name

    def transcribe(self, audio_path, language="ja"):
        with open(audio_path, "rb") as f:
            response = client.audio.transcriptions.create(
                model=self.model_name,
                file=f,
                language=language
            )
        return {"text": response.text}

# Use same function as before
model = OpenAIWhisperWrapper()

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path, language="ja")
    return result["text"].strip()

