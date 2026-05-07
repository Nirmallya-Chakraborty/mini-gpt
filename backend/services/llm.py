import requests

OLLAMA_URL = "http://ollama:11434/api/generate"

MODEL = "llama3.2:1b"  # better lightweight option

def generate_response(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response from model")

    except Exception as e:
        return f"Error: {str(e)}"