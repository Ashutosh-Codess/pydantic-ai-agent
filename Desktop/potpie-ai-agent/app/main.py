from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Assistant API",
    version="2.0.0",
    description="Question-only AI endpoint"
)

app.include_router(router)
