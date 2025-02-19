"""
main.py - FastAPI entry point.
"""

from fastapi import FastAPI
import routes

# Initalize FastAPI app
app = FastAPI(title="Randomized Habit Generator API")

# Include habit routes
app.include_router(routes.router)

@app.get("/")
def home():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the Randomized Habit Generator API!"}