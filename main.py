from fastapi import FastAPI
from pydantic import BaseModel
import os
import httpx

app = FastAPI()

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=AskResponse)
async def ask_ai(req: AskRequest):
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    # Safety check
    if not OPENAI_BASE_URL or not OPENROUTER_API_KEY:
        return {"answer": "ERROR: OpenRouter environment variables not set"}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Potpie AI Agent"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": req.query}
        ]
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            f"{OPENAI_BASE_URL}/chat/completions",
            headers=headers,
            json=payload
        )

    if response.status_code != 200:
        return {"answer": f"OpenRouter error: {response.text}"}

    data = response.json()
    return {"answer": data["choices"][0]["message"]["content"]}
