from fastapi import APIRouter, HTTPException
from app.schemas.request import AskRequest
from app.agent.career_agent import ask_ai

router = APIRouter()

@router.post("/ask")
async def ask(req: AskRequest):
    try:
        answer = await ask_ai(req.query)
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
