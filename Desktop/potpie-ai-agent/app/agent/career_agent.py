from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatModel(
    model_name="mistralai/mistral-7b-instruct",
    provider=provider
)

agent = Agent(
    model=model,
    system_prompt="You are a helpful AI study assistant. Answer any question clearly."
)

async def ask_ai(question: str) -> str:
    result = await agent.run(question)
    return result.output
