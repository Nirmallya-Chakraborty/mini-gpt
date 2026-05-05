import requests

# Ollama runs as a service in docker-compose
OLLAMA_URL = "http://host.docker.internal:11434"

MODEL = "llama3"  # change if needed

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