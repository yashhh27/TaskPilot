from fastapi import APIRouter
from pydantic import BaseModel
from utils.ai_client import ask_gpt

router = APIRouter()

class RewriteInput(BaseModel):
    task: str

class LearningPlanInput(BaseModel):
    skills: list[str]
    duration_days: int

@router.post("/ai/rewrite")
async def rewrite_task(data: RewriteInput):
    prompt = f"Rewrite this task to sound more clear and professional: {data.task}"
    response = await ask_gpt(prompt)
    return {"rewritten_task": response}

@router.post("/ai/learning-plan")
async def generate_learning_plan(data: LearningPlanInput):
    prompt = (
        f"I want to learn {', '.join(data.skills)} in {data.duration_days} days. "
        "Break it down into weekly learning goals and time allocation."
    )
    response = await ask_gpt(prompt)
    return {"learning_plan": response}
