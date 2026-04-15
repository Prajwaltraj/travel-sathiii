import requests
import json
from gtts import gTTS
import uuid
import os

def get_ai_response(user_query, context):
    """Calls local Ollama instance (defaulting to llama3 or mistral)"""
    url = "http://localhost:11434/api/generate"
    
    prompt = f"""
    You are Travel-Sathi, a helpful travel assistant.
    Use the following context to answer the user query.
    Context: {context}
    User: {user_query}
    Assistant:"""

    payload = {
        "model": "llama3", # Ensure you have run 'ollama pull llama3'
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        return response.json().get("response", "I'm sorry, I couldn't process that.")
    except Exception as e:
        return f"Connection Error: {str(e)}"

def generate_voice(text):
    """Generates an audio file and returns the filename"""
    filename = f"speech_{uuid.uuid4().hex[:8]}.mp3"
    filepath = os.path.join("static", filename)
    
    tts = gTTS(text=text, lang='en')
    tts.save(filepath)
    
    return filename