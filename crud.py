"""
crud.py - Handles database operations (CRUD) for habits.
"""

from sqlalchemy.orm import Session
from models import Habit
from schemas import HabitCreate

def create_habit(db: Session, habit_data: HabitCreate):
    """
    Creates a new habit and saves it to the database.
    """
    new_habit = Habit(
        name=habit_data.name,
        description=habit_data.description,
        frequency=habit_data.frequency,
        streak=0, # New habits start with a 0 streak
        completed_today=False
    )
    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)
    return new_habit

def get_habits(db: Session):
    """
    Retrieves all habits from the database.
    """
    return db.query(Habit).all()

def get_habit(db: Session, habit_id: int):
    """
    Retrieves a specific habit by ID.
    """
    return db.query(Habit).filter(Habit.id == habit_id).first()

def update_habit(db: Session, habit_id: int, habit_data: HabitCreate):
    """
    Updates a habit's details.
    """
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        habit.name = habit_data.name
        habit.description = habit_data.description
        habit.frequency = habit_data.frequency
        db.commit()
        db.refresh(habit)
    return habit

def delete_habit(db: Session, habit_id: int):
    """
    Deletes a habit from the database.
    """
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        db.delete(habit)
        db.commit()
    return habit