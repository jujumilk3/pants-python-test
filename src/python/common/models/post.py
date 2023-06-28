from datetime import datetime

from pydantic import BaseModel, Field

from utils import utcnow


class Post(BaseModel):
    title: str = Field(..., min_length=1, description="Post title")
    content: str = Field(..., min_length=1, description="Post content")
