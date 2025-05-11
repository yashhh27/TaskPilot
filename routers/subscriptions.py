from fastapi import APIRouter, HTTPException
from models.schemas import Subscription
from utils.role_auth import require_admin
from routers.plans import PLANS

router = APIRouter()

# Simulated database
USER_SUBSCRIPTIONS = {}

@router.post("/subscribe/{user_id}")
def subscribe_user(user_id: str, subscription: Subscription):
    require_admin(subscription.user_id)  # Only admins can subscribe users

    if subscription.plan_name not in PLANS:
        raise HTTPException(status_code=404, detail="Plan not found")

    USER_SUBSCRIPTIONS[user_id] = subscription.plan_name
    return {"msg": f"User '{user_id}' subscribed to plan '{subscription.plan_name}'"}
