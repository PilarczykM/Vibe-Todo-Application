from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    id: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
