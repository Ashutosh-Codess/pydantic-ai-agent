from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Potpie AI Career Agent",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)
