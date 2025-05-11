from fastapi import FastAPI

from routers import plans
from routers import subscriptions, access, usage, dummy_apis, ai


app = FastAPI(
    title="TaskPilot X",
    description="AI-enhanced productivity backend with FastAPI",
    version="1.0.0"
)

# Register routers

app.include_router(plans.router, prefix="/api", tags=["Plans"])
app.include_router(subscriptions.router, prefix="/api", tags=["Subscriptions"])
app.include_router(access.router, prefix="/api", tags=["Access"])
app.include_router(usage.router, prefix="/api", tags=["Usage"])
app.include_router(dummy_apis.router, prefix="/api", tags=["Protected APIs"])
app.include_router(ai.router, prefix="/api", tags=["AI Features"])
