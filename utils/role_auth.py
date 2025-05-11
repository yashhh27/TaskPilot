from fastapi import HTTPException, Request

# Simulated user roles for demo
USER_ROLES = {
    "admin123": "admin",
    "user456": "customer"
}

def get_role(user_id: str):
    return USER_ROLES.get(user_id, "customer")

def require_admin(user_id: str):
    if get_role(user_id) != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
