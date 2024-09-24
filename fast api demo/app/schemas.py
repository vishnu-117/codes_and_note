# app/schemas.py
from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    is_completed: bool

    class Config:
        orm_mode = True
