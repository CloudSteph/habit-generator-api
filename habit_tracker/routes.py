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

# 1) Endpoint to create a new habit.
@router.post("/habits/", response_model=schemas.HabitResponse)
def create_habit(habit_data: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.create_habit(db, habit_data)

# 2) Endpoint to retrieve all habits.
@router.get("/habits/", response_model=list[schemas.HabitResponse])
def get_habits(db: Session = Depends(get_db)):
    return crud.get_habits(db)

# 3) Endpoint to retrieve a random habit based on priority logic.
@router.get("/habits/random")
def get_random_habit(db: Session = Depends(get_db)):
    habit = crud.get_random_habit(db)
    if habit is None:
        raise HTTPException(status_code=404, detail="No habits found")
    return habit

# 4) Endpoint to reset 'completed_today' for all habits.
@router.post("/habits/reset")
def reset_habits(db: Session = Depends(get_db)):
    crud.reset_completed_today(db)
    return {"message": "All habits reset for the new day!"}

# 5) Endpoint to mark a habit as completed.
@router.patch("/habits/{habit_id}/complete", response_model=schemas.HabitResponse)
def complete_habit(habit_id: int, db: Session = Depends(get_db)):
    return crud.complete_habit(db, habit_id)

# 6) Endpoint to retrieve a specific habit by ID
@router.get("/habits/{habit_id}", response_model=schemas.HabitResponse)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = crud.get_habit(db, habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

# 7) Endpoint to update an existing habit.
@router.put("/habits/{habit_id}", response_model=schemas.HabitResponse)
def update_habit(habit_id: int, habit_data: schemas.HabitCreate, db: Session = Depends(get_db)):
    habit = crud.update_habit(db, habit_id, habit_data)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

# 8) Endpoint to delete a habit.
@router.delete("/habits/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = crud.delete_habit(db, habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted successfully"}