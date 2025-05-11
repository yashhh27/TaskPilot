from fastapi import APIRouter, HTTPException
from routers.access import check_api_access
from routers.usage import USAGE_LOG

router = APIRouter()

def log_usage(user_id: str, api_name: str):
    if user_id not in USAGE_LOG:
        USAGE_LOG[user_id] = {}
    USAGE_LOG[user_id][api_name] = USAGE_LOG[user_id].get(api_name, 0) + 1

def require_api_access(user_id: str, api_name: str):
    access = check_api_access(user_id, api_name)
    if not access.get("access"):
        raise HTTPException(status_code=403, detail="Access denied")
    log_usage(user_id, api_name)

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
