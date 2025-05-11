from fastapi import APIRouter, HTTPException
from models.schemas import Plan
from utils.role_auth import require_admin

router = APIRouter()
PLANS = {}

@router.post("/plans")
def create_plan(plan: Plan, user_id: str):
    require_admin(user_id)
    if plan.name in PLANS:
        raise HTTPException(status_code=400, detail="Plan already exists")
    PLANS[plan.name] = plan
    return {"msg": f"Plan '{plan.name}' created"}

@router.get("/plans")
def list_plans():
    return list(PLANS.values())
