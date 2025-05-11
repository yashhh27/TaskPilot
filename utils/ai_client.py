import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3:8b"

async def ask_gpt(prompt: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"Rewrite this task to sound professional: {prompt}",
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "(Mock Response) No text generated.")
    except Exception as e:
        print("🛑 Ollama Error:", e)
        return f"(Mock Response) {prompt}"
