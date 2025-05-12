from fastapi import APIRouter
from pydantic import BaseModel
import json
from utils.ai_client import decompose_goal_with_ollama
import re
router = APIRouter()

class GoalRequest(BaseModel):
    goal: str



@router.post("/ai/decompose-task")
def handle_ai_task_decomposition(request: GoalRequest):
    response_text = decompose_goal_with_ollama(request.goal)

    try:
        # Extract first JSON-like block
        match = re.search(r'\{[\s\S]+\}', response_text)

        if not match:
            return {
                "error": "Could not extract JSON block from AI response.",
                "raw_response": response_text
            }

        extracted_json = match.group(0)

        # Replace any smart quotes or formatting issues
        extracted_json = extracted_json.replace("“", "\"").replace("”", "\"")

        result = json.loads(extracted_json)
        return result

    except Exception as e:
        return {
            "error": f"Parsing failed: {str(e)}",
            "raw_response": response_text
        }

    
