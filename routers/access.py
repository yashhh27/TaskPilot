from fastapi import APIRouter, HTTPException
from routers.subscriptions import USER_SUBSCRIPTIONS
from routers.plans import PLANS

router = APIRouter()

@router.get("/access/{user_id}/{api_name}")
def check_api_access(user_id: str, api_name: str):
    plan_name = USER_SUBSCRIPTIONS.get(user_id)
    if not plan_name:
        raise HTTPException(status_code=404, detail="User not subscribed to any plan")

    plan = PLANS.get(plan_name)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    if api_name not in plan.allowed_apis:
        return {"access": False, "reason": f"'{api_name}' not allowed in plan '{plan_name}'"}

    return {"access": True, "plan": plan_name}
