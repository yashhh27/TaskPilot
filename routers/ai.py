from fastapi import APIRouter
from pydantic import BaseModel
from utils.ai_client import ask_gpt

router = APIRouter()

class TaskRequest(BaseModel):
    task: str

@router.post("/ai/rewrite")
async def rewrite_task(request: TaskRequest):
    rewritten = await ask_gpt(request.task)
    return {"rewritten_task": rewritten}
