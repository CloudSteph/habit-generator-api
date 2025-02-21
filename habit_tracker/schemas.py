"""
schemas.py - Defines Pydantic schemas for request validation and responses.
"""

from pydantic import BaseModel
from typing import Optional

class HabitBase(BaseModel):
    """
    Base schema defining common fields for a habit.
    """
    name: str
    description: Optional[str] = None
    frequency: str # e.g., "daily", "weekly"

class HabitCreate(HabitBase):
    """
    Schema for creating a new habit.
    """
    pass # Inherits fields from HabitBase

class HabitResponse(HabitBase):
    """
    Schema for returning a habit response.
    """
    id: int
    streak: int
    completed_today: bool

    class Config:
        orm_mode = True # Enables SQLAlchemy compatibility