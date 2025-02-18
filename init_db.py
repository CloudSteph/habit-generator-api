"""
init_db.py - Initialize the database and creates tables.
"""

from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

print("Database initialized successfully!")