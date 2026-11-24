from pydantic import BaseModel
from typing import List


class AgentResponse(BaseModel):
    status: str
    message: str
    tasks: List[str] = []
    document: str = ""
    llm_used: str = ""
    execution_time: float = 0.0