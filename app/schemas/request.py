from pydantic import BaseModel

class AskRequest(BaseModel):
    query: str | None = None
    topic: str | None = None
