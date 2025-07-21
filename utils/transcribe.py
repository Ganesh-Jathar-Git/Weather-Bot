import whisper

model = whisper.load_model("medium")  # Can be change to "small" or "large"

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path, language="ja")
    return result["text"].strip()

