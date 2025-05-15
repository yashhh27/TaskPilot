
 TaskPilot – AI-Powered Goal Decomposer with Usage Access Management

TaskPilot is a FastAPI-based project that uses **Ollama (LLaMA3)** to decompose user goals into subtasks, assign priorities, and recommend learning resources. It also includes access management features like plans, usage tracking, and protected APIs.

---

 Features

AI Assistant (LLM Integration)
- Accepts a user goal (e.g., "Prepare for Python Interview")
- Calls **Ollama (LLaMA3)** using HTTPX async client
- Parses JSON response with subtasks, priorities, and resources
- Auto-saves subtasks to a user’s task list

 Access Management System
- Create subscription plans with allowed APIs
- Subscribe users to plans
- Protect APIs using access control and usage logs

Task Management
- Create, read, update, delete (CRUD) tasks
- Batch create tasks from AI subtasks

---

 Project Structure

```
.
├── main.py
├── routers/
│   ├── ai.py              # AI goal decomposition endpoint
│   ├── plans.py           # Create plans
│   ├── subscriptions.py   # Subscribe users
│   ├── access.py          # Access control
│   └── tasks.py           # Task management APIs
├── utils/
│   └── ai_client.py       # Async function to connect with Ollama
└── schemas/
    └── models.py          # Pydantic models
```

---

 How to Run the Project

 Prerequisites

- Python 3.10 or higher
- Ollama (local LLM server)

 1. Clone the Repository

```bash
git clone https://github.com/yourusername/taskpilot.git
cd taskpilot
```

 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn httpx pydantic
```

 4. Start Ollama (if not running)

```bash
ollama run llama3
```

Verify it's running:

```bash
curl http://localhost:11434
# Should return: "Ollama is running"
```

 5. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Visit Swagger UI at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

 Example Test (Postman / Swagger)

Endpoint:

```
POST /api/ai/decompose-task?user_id=ashok123
```

 Body (JSON):

```json
{
  "goal": "prepare for Python interview"
}
```

 Response:

```json
{
  "rewritten": "...",
  "subtasks": [
    {
      "task": "...",
      "priority": "High",
      "details": [...],
      "resources": { "books": [...], "web": [...] }
    }
  ]
}
```

---

 Dependencies (requirements.txt)

```text
fastapi
uvicorn
httpx
pydantic
```

---

 Note on Ollama Models

You must have LLaMA3 model installed:

```bash
ollama pull llama3
```

---

 Future Improvements

- Add authentication for users
- MongoDB or SQLite storage for tasks
- Enhance AI response validation
