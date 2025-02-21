"""
main.py - FastAPI entry point.
"""
import os
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal
import crud
from routes import router
import logging
from datetime import datetime, timedelta

# Configure logging to write to a file
logging.basicConfig(
    filename="reset_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def cleanup_old_logs():
    """
    Deletes log entries older than 30 days to prevent excessive file size growth
    """
    log_file = "reset_log.txt"
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            lines = file.readlines()
        
        # Keep only logs from the last 30 days
        cutoff_date = datetime.now() - timedelta(days=30)
        new_lines = []

        for line in lines:
            try:
                log_date_str = line.split(" - ")[0] #Extract timestamp
                log_date = datetime.strptime(log_date_str, "%Y-%m-%d %H:%M:%S")

                # Keep log only if it's within the last 30 days
                if log_date >= cutoff_date:
                    new_lines.append(line)
            except ValueError as e:
                logging.warning(f"Skipping invalid log entry: {line.strip()} - Error: {e}")
                
        # Overwrite the file with only recent logs
        with open(log_file, "w") as file:
            file.writelines(new_lines)

        logging.info("Deleted logs older than 30 days")

# Call cleanup function before logging new resets
cleanup_old_logs()

# Initalize FastAPI app
app = FastAPI(
    title="Randomized Habit Generator API",
    description="An API to track and manage habits with random selection and automation.",
    version="1.0.0"
)

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