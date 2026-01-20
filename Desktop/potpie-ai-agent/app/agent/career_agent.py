import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

model = OpenAIChatModel(
    model_name="mistralai/mistral-7b-instruct"
)

agent = Agent(model)

async def ask_ai(question: str) -> str:
    result = await agent.run(question)
    return result.output
