from pydantic import BaseModel
from typing import List, Dict, Optional

class Plan(BaseModel):
    name: str
    allowed_apis: List[str]

class Permission(BaseModel):
    plan_name: str
    api_names: List[str]

class Subscription(BaseModel):
    user_id: str
    plan_name: str

class UsageLog(BaseModel):
    user_id: str
    api_name: str
    count: int = 0

class User(BaseModel):
    id: str
    role: str  # "admin" or "customer"
