import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    model_name="mistralai/mistral-7b-instruct",
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(model)

async def ask_ai(question: str) -> str:
    result = await agent.run(question)
    return result.output
