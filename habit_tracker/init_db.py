"""
init_db.py - Initialize the database and creates tables.
"""

from habit_tracker.database import engine, Base
from habit_tracker import models

def initialize_database():
    print("Using database at: data/habits.db")
    # Create database tables from models
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()