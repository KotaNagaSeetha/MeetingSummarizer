import whisper

model = whisper.load_model("base")  # You may use "small" or "medium" if you prefer

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']
