import os
import requests

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://192.168.1.185:11434")
MODEL_NAME = "llama3.2:1b"

def generate_response(prompt: str) -> str:
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response from model")

    except Exception as e:
        return f"Error from Ollama: {str(e)}"