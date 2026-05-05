import requests

#OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
MODEL_NAME = "tinyllama"

def generate_response(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response from model")

    except Exception as e:
        return f"Error from Ollama: {str(e)}"