from fastapi import FastAPI
from routers import ai
from routers import plans
from routers import subscriptions
from routers import access
from routers import usage

from routers import subscriptions, access



app = FastAPI(
    title="TaskPilot X",
    description="AI-enhanced productivity backend with FastAPI",
    version="1.0.0"
)

# Register routers
app.include_router(ai.router, prefix="/api", tags=["AI Features"])
app.include_router(plans.router, prefix="/api", tags=["Plans"])
app.include_router(subscriptions.router, prefix="/api", tags=["Subscriptions"])
app.include_router(access.router, prefix="/api", tags=["Access"])
app.include_router(usage.router, prefix="/api", tags=["Usage"])

app.include_router(subscriptions.router, prefix="/api", tags=["Subscriptions"])
app.include_router(access.router, prefix="/api", tags=["Access"])


