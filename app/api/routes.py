from fastapi import APIRouter
from app.schemas.request import CareerRequest
from app.agent.career_agent import career_agent

router = APIRouter()

@router.post("/career")
async def career_advice(data: CareerRequest):
    result = await career_agent.run(data.query)
    return {"response": result.data}
