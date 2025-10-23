import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def summarize_text(transcript):
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = "models/gemini-2.5-flash" # Use a valid model from your list
    url = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent?key={api_key}"
    prompt = f"Summarize this meeting transcript into key decisions and action items. Transcript: {transcript}"
    headers = {"Content-Type": "application/json"}  # No Authorization header
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    summary_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    lines = summary_text.split('\n')
    summary = "\n".join([line for line in lines if not line.startswith('-')])
    actions = "\n".join([line for line in lines if line.startswith('-')])
    return summary, actions
