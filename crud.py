"""
crud.py - Handles database operations (CRUD) for habits.
"""

import random
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

def get_random_habits(db: Session):
    """
    Retrieves a random habit, prioritizing habits that:
    - Have not been completed today.
    - Appear more frequently.
    """

    # Fetch all habits
    habits = db.query(Habit).all()

    # If there are no habits, return None
    if not habits:
        return None
    
    # Filter habits that have NOT been completed today
    available_habits = [habit for habit in habits if not habit.completed_today]

    # If all habits are completed today, allow selection from all habits
    if not available_habits:
        available_habits = habits

    # Weighting logic: Higher weight for lower streaks and higher frequency
    weighted_habits = []
    for habit in available_habits:
        weight = max(1, 5 - habit.streak) # Prioritize habits with lower streaks

        if habit.frequency == "daily":
            weight *= 3 # Daily habits appear more frequently
        elif habit.frequency == "weekly":
            weight *= 2 # weekly habits have medium priority
        
        weighted_habits.extend([habit] * weight) # Add habit multiple times for weighting 

    # Randomly select one habit based on weight
    return random.choice(weighted_habits)