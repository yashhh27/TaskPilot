from fastapi import APIRouter
from typing import Dict

router = APIRouter()

# In-memory usage tracker
USAGE_LOG: Dict[str, Dict[str, int]] = {}

@router.post("/log-usage/{user_id}/{api_name}")
def log_usage(user_id: str, api_name: str):
    if user_id not in USAGE_LOG:
        USAGE_LOG[user_id] = {}

    USAGE_LOG[user_id][api_name] = USAGE_LOG[user_id].get(api_name, 0) + 1
    return {"msg": f"Logged usage for {user_id} on {api_name}"}

@router.get("/usage/{user_id}")
def get_usage(user_id: str):
    return {
        "user_id": user_id,
        "usage": USAGE_LOG.get(user_id, {})
    }
