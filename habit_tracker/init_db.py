"""
init_db.py - Initialize the database and creates tables.
"""

from database import engine, Base
import habit_tracker.models

# Create database tables from models
Base.metadata.create_all(bind=engine)

print("Database initialized successfully!")