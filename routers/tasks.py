from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

router = APIRouter()

# In-memory task store: user_id -> List[Task]
TASKS_DB = {}

class Task(BaseModel):
    id: str
    user_id: str
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "Medium"  # High, Medium, Low
    status: Optional[str] = "Pending"   # Pending, Done

# ✅ Create Task
@router.post("/tasks/{user_id}", response_model=Task)
def create_task(user_id: str, task: Task):
    task.id = str(uuid.uuid4())
    task.user_id = user_id
    if user_id not in TASKS_DB:
        TASKS_DB[user_id] = []
    TASKS_DB[user_id].append(task)
    return task

# ✅ Get All Tasks for User
@router.get("/tasks/{user_id}", response_model=List[Task])
def get_tasks(user_id: str):
    return TASKS_DB.get(user_id, [])

# ✅ Update a Task
@router.put("/tasks/{user_id}/{task_id}", response_model=Task)
def update_task(user_id: str, task_id: str, updated: Task):
    tasks = TASKS_DB.get(user_id, [])
    for i, t in enumerate(tasks):
        if t.id == task_id:
            updated.id = task_id
            updated.user_id = user_id
            TASKS_DB[user_id][i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")

# ✅ Delete a Task
@router.delete("/tasks/{user_id}/{task_id}")
def delete_task(user_id: str, task_id: str):
    tasks = TASKS_DB.get(user_id, [])
    for i, t in enumerate(tasks):
        if t.id == task_id:
            del TASKS_DB[user_id][i]
            return {"msg": f"Task {task_id} deleted."}
    raise HTTPException(status_code=404, detail="Task not found")
