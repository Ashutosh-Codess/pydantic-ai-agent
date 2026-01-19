from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Assistant")

app.include_router(router)
