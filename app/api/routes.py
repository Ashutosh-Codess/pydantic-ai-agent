from fastapi import APIRouter, HTTPException
from app.schemas.request import AskRequest
from app.agent.career_agent import ask_ai

router = APIRouter()

@router.post("/ask")
async def ask(request: AskRequest):
    question = request.query or request.topic

    if not question:
        raise HTTPException(status_code=400, detail="Query missing")

    answer = await ask_ai(question)
    return {"answer": answer}
