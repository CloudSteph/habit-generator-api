"""
main.py - FastAPI entry point.
"""

from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal
import crud
from routes import router

# Initalize FastAPI app
app = FastAPI(title="Randomized Habit Generator API")

# Include habit routes from 'routes.py'
app.include_router(router)

# Initialize APScheduler()
scheduler = BackgroundScheduler()

def scheduled_reset():
    """
    Scheduled task to reset all habits every morning at 12:00 AM.
    """
    db = SessionLocal()
    try:
        crud.reset_completed_today(db)
        print("Habits reset for the new day!")
    except Exception as e:
        print(f"Error resetting habits: {e}")
    finally: db.close()

# Schedule the reset function to run daily at 12:00 AM
scheduler.add_job(scheduled_reset, "cron", hour=0, minute=0)
scheduler.start()

@app.get("/")
def home():
    """
    Root endpoint.
    """
    return {"message": "Habit Tracker API is running!"}