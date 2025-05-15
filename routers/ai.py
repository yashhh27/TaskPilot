from fastapi import APIRouter, Query
from pydantic import BaseModel
import requests, re, json, ast
from utils.ai_client import call_ollama  # Async function to connect to Ollama

router = APIRouter()

class GoalRequest(BaseModel):
    goal: str

@router.post("/ai/decompose-task")
async def decompose_task_route(data: GoalRequest, user_id: str = Query(...)):
    """
    Accepts a user goal and user_id, returns a structured task breakdown.
    Uses Ollama to generate tasks. Auto-saves to user's task list.
    """
    # 🔮 Prompt for Ollama
    prompt = f"""
    The user goal is: "{data.goal}"

    1. Rewrite it professionally.
    2. Break it into 3–6 prioritized subtasks (High, Medium, Low).
    3. For each subtask, provide 2–3 key points to learn/do.
    4. Recommend 2–3 resources (books, websites, papers).

    Respond in valid JSON like this:

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

    # 🤖 Ask LLM via Ollama
    response_text = await call_ollama(prompt)

    # 🧠 Extract JSON from Ollama output
    match = re.search(r'\{[\s\S]+\}', response_text)
    if not match:
        return {"error": "AI response could not be parsed.", "raw_response": response_text}

    extracted_json = match.group(0).replace("“", '"').replace("”", '"')

    # 🧪 Try JSON decode
    try:
        parsed = json.loads(extracted_json)
    except:
        try:
            parsed = ast.literal_eval(extracted_json)
        except Exception as e:
            return {
                "error": f"AI response parsing failed: {str(e)}",
                "raw_response": response_text
            }

    # 💾 Save subtasks to backend
    save_url = f"http://localhost:8000/api/tasks/convert-ai-subtasks/{user_id}"
    try:
        requests.post(save_url, json=parsed.get("subtasks", []))
    except Exception as e:
        return {"error": "Failed to save tasks", "details": str(e)}

    return parsed
