"""
database.py - Handles the database connection setup using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (SQLite  file-based database)
DATABASE_URL = "sqlite:///./habits.db"

# Create a session engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for our models
Base = declarative_base()