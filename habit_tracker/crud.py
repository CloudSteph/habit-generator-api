"""
crud.py - Handles database operations (CRUD) for habits.
"""

from sqlalchemy.orm import Session
from habit_tracker.models import Habit
from habit_tracker.schemas import HabitCreate, HabitUpdate, HabitResponse
from datetime import datetime, timedelta
import random

# Creates a new habit and saves it to the database.
def create_habit(db: Session, habit_data: HabitCreate):
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

# Retrieves all habits from the database.
def get_habits(db: Session):
    return db.query(Habit).all()

# Retrieves a specific habit by ID.
def get_habit(db: Session, habit_id: int):
    return db.query(Habit).filter(Habit.id == habit_id).first()

# Retrieves a random habit based on streak priority
def get_random_habit(db: Session):
    habits = db.query(Habit).filter(Habit.completed_today == False).all()

    print(f"Available habits before filtering: {db.query(Habit).all()}")
    print(f"Available habits after filtering (completed_today=False): {habits}")

    # If there are no habits, return None
    if not habits:
        print("No available habits!")
        return None
    
    # Weight habits by streak (higher streak = higher selection chance)
    weighted_habits = [habit for habit in habits for _ in range(habit.streak + 1)]

    selected_habit = random.choice(weighted_habits)
    print(f"Selected habit: {selected_habit}")
    return selected_habit

# Mark a habit as completed
def complete_habit(db: Session, habit_id: int):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if not habit:
        return None
    
    habit.completed_today = True
    habit.streak += 1 # Increase streak on completion
    db.commit()
    db.refresh(habit)
    return habit

# Update a habit (PUT request)
def update_habit(db: Session, habit_id: int, habit_update: HabitUpdate):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if not habit:
        return None
    
    habit.name = habit_update.name or habit.name
    habit.description = habit_update.description or habit.description
    habit.frequency = habit_update.frequency or habit.frequency

    db.commit()
    db.refresh(habit)
    return habit

# Deletes a habit from the database.
def delete_habit(db: Session, habit_id: int):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        db.delete(habit)
        db.commit()
    return habit

# Reset 'completed_today' for all habits every midnight
def reset_completed_today(db: Session):
    try:
        db.query(Habit).update({"completed_today": False})
        db.commit()
        return {"message": "All habits have been reset."}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}