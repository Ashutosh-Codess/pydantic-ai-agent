from fastapi import APIRouter
from app.schemas.request import AskRequest
from app.agent.career_agent import ask_ai

router = APIRouter()

@router.post("/ask")
async def ask(request: AskRequest):
    response = await ask_ai(request.query)
    return {"response": response}
