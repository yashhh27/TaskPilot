from pydantic import BaseModel
from typing import List, Dict, Optional

# ✅ Cloud Access Management Schemas
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

# ✅ TaskPilot Schemas (AI To-do + Task Assistant)
class TaskResource(BaseModel):
    books: Optional[List[str]] = []
    web: Optional[List[str]] = []
    papers: Optional[List[str]] = []

class AITaskCreate(BaseModel):
    task: str
    priority: str
    details: List[str]
    resources: TaskResource

class TaskCreate(BaseModel):
    user_id: str
    title: str
    description: str
    priority: Optional[str] = "Medium"
    status: Optional[str] = "Pending"  # Status could be: Pending, In Progress, Completed

class Task(TaskCreate):
    id: int
