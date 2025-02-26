"""
schemas.py - Defines Pydantic schemas for request validation and responses.
"""

from pydantic import BaseModel
from typing import Optional

# Schema for creating a Habit (Request Body)
class HabitCreate(BaseModel):
    name: str
    description: str
    frequency: str

# Schema for Updating a Habit (PUT Request)
class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[str] = None

# Schema for Returning a Habit (Response)
class HabitResponse(BaseModel):
    id: int
    name: str
    description: str
    frequency: str
    streak: int
    completed_today: bool

    class Config:
        orm_mode = True # Enables SQLAlchemy compatibility (conversion from SQLAlchemy to Pydantic)