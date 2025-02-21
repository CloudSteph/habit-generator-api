"""
models.py - Defines the Habit model for the database.
"""

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Habit(Base):
    """
    Habit model representing a user's habit with tracking information.
    """
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True) # Unique ID for each habit
    name = Column(String, nullable=False) # Habit name
    description = Column(String, nullable=True) # Optional habit description
    frequency = Column(String, nullable=False) # e.g., "daily" or "weekly" etc.
    streak = Column(Integer, default=0) # Number of consecutive completions
    completed_today = Column(Boolean, default=False) # Tracks daily completion