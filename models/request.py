from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    request: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="User Request"
    )