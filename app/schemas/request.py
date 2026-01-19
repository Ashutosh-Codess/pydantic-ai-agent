from pydantic import BaseModel

class CareerRequest(BaseModel):
    query: str
