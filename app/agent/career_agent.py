import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    model_name="gpt-3.5-turbo",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

career_agent = Agent(
    model=model,
    system_prompt=(
        "You are a professional AI career advisor. "
        "Give clear, practical, step-by-step career guidance."
    )
)
