import requests
import httpx



OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"
async def call_ollama(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        return res.json().get("response", "(No response)")

def decompose_goal_with_ollama(goal: str):
    prompt = f"""
    The user goal is: "{goal}"

    1. Rewrite it professionally.
    2. Break it into 3–6 prioritized subtasks (High, Medium, Low).
    3. For each subtask, provide 2–3 key points to learn/do.
    4. Recommend a few resources (books, articles, websites) per subtask.

    Respond in JSON format like this:

    {{
      "rewritten": "...",
      "subtasks": [
        {{
          "task": "...",
          "priority": "High",
          "details": ["...", "..."],
          "resources": {{
            "books": ["..."],
            "web": ["..."],
            "papers": []
          }}
        }}
      ]
    }}
    """

    try:
        res = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        return res.json().get("response", "(No response)")
    except Exception as e:
        print("🛑 Ollama Error:", e)
        return "(Mock) Could not process task"