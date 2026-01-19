from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

# Pydantic-AI automatically reads:
# OPENAI_API_KEY or OPENROUTER_API_KEY from environment
# NO api_key or base_url should be passed

model = OpenAIChatModel(
    model_name="mistralai/mistral-7b-instruct"
)

agent = Agent(
    model=model,
    system_prompt="You are a helpful AI assistant. Answer clearly and concisely."
)

async def ask_ai(req):
    result = await agent.run(req.query)
    return {"answer": result.output}
