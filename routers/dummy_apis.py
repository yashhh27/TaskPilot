from fastapi import APIRouter, HTTPException
from routers.access import check_api_access
from routers.usage import USAGE_LOG
from routers.plans import PLANS
from routers.subscriptions import USER_SUBSCRIPTIONS
router = APIRouter()

def log_usage(user_id: str, api_name: str):
    if user_id not in USAGE_LOG:
        USAGE_LOG[user_id] = {}
    USAGE_LOG[user_id][api_name] = USAGE_LOG[user_id].get(api_name, 0) + 1

def require_api_access(user_id: str, api_name: str):
    plan_name = USER_SUBSCRIPTIONS.get(user_id)
    if not plan_name:
        raise HTTPException(status_code=403, detail="User not subscribed")

    plan = PLANS.get(plan_name)
    if not plan or api_name not in plan.allowed_apis:
        raise HTTPException(status_code=403, detail="Access denied")

    # Limit enforcement
    user_usage = USAGE_LOG.get(user_id, {}).get(api_name, 0)
    if user_usage >= plan.usage_limit:
        raise HTTPException(status_code=429, detail="Usage limit exceeded")

    # Log usage
    if user_id not in USAGE_LOG:
        USAGE_LOG[user_id] = {}
    USAGE_LOG[user_id][api_name] = user_usage + 1

@router.get("/api1")
def api1(user_id: str):
    require_api_access(user_id, "api1")
    return {"message": "API 1 response"}

@router.get("/api2")
def api2(user_id: str):
    require_api_access(user_id, "api2")
    return {"message": "API 2 response"}

@router.get("/api3")
def api3(user_id: str):
    require_api_access(user_id, "api3")
    return {"message": "API 3 response"}

@router.get("/api4")
def api4(user_id: str):
    require_api_access(user_id, "api4")
    return {"message": "API 4 response"}

@router.get("/api5")
def api5(user_id: str):
    require_api_access(user_id, "api5")
    return {"message": "API 5 response"}

@router.get("/api6")
def api6(user_id: str):
    require_api_access(user_id, "api6")
    return {"message": "API 6 response"}
