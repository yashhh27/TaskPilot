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

@router.put("/plans/{plan_name}")
def update_plan(plan_name: str, updated_plan: Plan, user_id: str):
    require_admin(user_id)
    if plan_name not in PLANS:
        raise HTTPException(status_code=404, detail="Plan not found")
    PLANS[plan_name] = updated_plan
    return {"msg": f"Plan '{plan_name}' updated"}

@router.delete("/plans/{plan_name}")
def delete_plan(plan_name: str, user_id: str):
    require_admin(user_id)
    if plan_name not in PLANS:
        raise HTTPException(status_code=404, detail="Plan not found")
    del PLANS[plan_name]
    return {"msg": f"Plan '{plan_name}' deleted"}
