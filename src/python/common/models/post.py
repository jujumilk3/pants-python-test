from datetime import datetime

from pydantic import BaseModel, Field

from utils import utcnow


class CallMessage(BaseModel):
    timestamp: datetime = Field(default_factory=utcnow)
    command: str
    body: str
