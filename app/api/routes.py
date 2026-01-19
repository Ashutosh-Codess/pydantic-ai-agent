from fastapi import APIRouter
from app.agent.career_agent import ask_ai
from app.schemas.request import AskRequest

router = APIRouter()

@router.post("/ask")
async def ask(req: AskRequest):
    return await ask_ai(req)
