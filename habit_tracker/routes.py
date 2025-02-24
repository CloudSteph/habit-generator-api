"""
routes.py - Defines FastAPI routes for handling habit operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from habit_tracker.database import SessionLocal
import habit_tracker.crud as crud
import habit_tracker.schemas as schemas

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/habits/random")
def get_random_habit(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a random habit based on priority logic.
    """
    habit = crud.get_random_habit(db)
    if habit is None:
        raise HTTPException(status_code=404, detail="No habits found")
    return habit

@router.post("/habits/reset")
def reset_habits(db: Session = Depends(get_db)):
    """
    Endpoint to reset 'completed_today' for all habits.
    """
    crud.reset_completed_today(db)
    return {"message": "All habits reset for the new day!"}

@router.post("/habits/", response_model=schemas.HabitResponse)
def create_habit(habit_data: schemas.HabitCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new habit.
    """
    return crud.create_habit(db, habit_data)

@router.get("/habits/", response_model=list[schemas.HabitResponse])
def get_habits(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all habits.
    """
    return crud.get_habits(db)

@router.get("/habits/{habit_id}", response_model=schemas.HabitResponse)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a specific habit by ID
    """
    habit = crud.get_habit(db, habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@router.put("/habits/{habit_id}", response_model=schemas.HabitResponse)
def update_habit(habit_id: int, habit_data: schemas.HabitCreate, db: Session = Depends(get_db)):
    """
    Endpoint to update an existing habit.
    """
    habit = crud.update_habit(db, habit_id, habit_data)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@router.delete("/habits/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a habit.
    """
    habit = crud.delete_habit(db, habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted successfully"}