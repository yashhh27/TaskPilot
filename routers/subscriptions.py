from fastapi import APIRouter, HTTPException
from models.schemas import Subscription
from routers.plans import PLANS
from utils.role_auth import require_admin

router = APIRouter()

# Simulated DB
USER_SUBSCRIPTIONS = {}

@router.post("/subscribe/{user_id}")
def subscribe_user(user_id: str, subscription: Subscription):
    require_admin(subscription.user_id)  # Only admin can assign plans

    if subscription.plan_name not in PLANS:
        raise HTTPException(status_code=404, detail="Plan not found")

    USER_SUBSCRIPTIONS[user_id] = subscription.plan_name
    return {
        "msg": f"User '{user_id}' subscribed to plan '{subscription.plan_name}'"
    }
