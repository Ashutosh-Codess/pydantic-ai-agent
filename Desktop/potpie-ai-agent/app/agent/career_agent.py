from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

model = OpenAIChatModel(
    model_name="mistralai/mistral-7b-instruct",
    provider="openrouter"
)

agent = Agent(
    model=model,
    system_prompt="Answer directly. No templates. No formatting."
)

async def ask_ai(question: str) -> str:
    result = await agent.run(question)
    return result.output
