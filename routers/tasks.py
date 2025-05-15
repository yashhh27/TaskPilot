# ✅ Task CRUD API for TaskPilot (with auto-save support)
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import uuid
import requests

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

# ✅ Batch Create from AI Subtasks
@router.post("/tasks/{user_id}/batch", response_model=List[Task])
def batch_create_tasks(user_id: str, tasks: List[Task]):
    if user_id not in TASKS_DB:
        TASKS_DB[user_id] = []
    for task in tasks:
        task.id = str(uuid.uuid4())
        task.user_id = user_id
        TASKS_DB[user_id].append(task)
    return TASKS_DB[user_id][-len(tasks):]  # Return only the added ones

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

# ✅ Delete All Tasks (for testing)
@router.delete("/tasks/{user_id}")
def clear_tasks(user_id: str):
    TASKS_DB[user_id] = []
    return {"msg": f"All tasks for user {user_id} cleared."}

# ✅ Hook: Convert AI subtasks to Task model
@router.post("/tasks/convert-ai-subtasks/{user_id}")
def convert_ai_to_tasks(user_id: str, subtasks: List[dict]):
    converted_tasks = []
    for item in subtasks:
        converted_tasks.append(Task(
            id="",
            user_id=user_id,
            title=item.get("task", "Untitled Task"),
            description="; ".join(item.get("details", [])),
            priority=item.get("priority", "Medium"),
            status="Pending"
        ))
    return batch_create_tasks(user_id, converted_tasks)
