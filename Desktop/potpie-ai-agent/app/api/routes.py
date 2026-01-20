from fastapi import APIRouter
from app.schemas.request import AskRequest
from app.agent.career_agent import ask_ai

router = APIRouter()

@router.post("/ask", tags=["AI"])
async def ask(req: AskRequest):
    return {"answer": await ask_ai(req.question)}
