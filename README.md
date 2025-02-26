# Randomized Habit Generator API
## 📌 Overview
The **Randomized Habit Generator API** built with FastAPI is desgined to help users build consistent habits by tracking progress, selecting habits based on streak priority, and resetting completed habits daily. It encourages routine adherence by increasing the likelihood of selecting frequently completed habits while maintaining an element of randomness.

---

## ⭐️ Features
- **Habit CRUD Operations**: Create, retrieve, update, and delete habits.
- **Record Completions**: Mark a habit as completed for the current day.
- **Streak Tracking**: Track the current streak (number of consecutive days) for each habit.
- **Random Habit Selection**: Fetch a random habit from your list of habits.
- **Interactive API Docs**: FastAPI provides an interactive Swagger UI at /docs and OpenAPI JSON at /openapi.json and ReDoc at /redoc

---

## 🛠️ Technologies Used (Tech Stack)
- Python: Used to develop the backend logic
- FastAPI: Web framework for building APIs quickly, used for creating RESTful API endpoints.
- SQLite: Lightweight database used for storing habit data
- APScheduler: A scheduling library used for automating the daily habit reset
- SQLAlchemy: An ORM (Object Relational Mapper) used for database interactions.
- Pydantic: Used for data validation and parsing for API request and response models.

---

## Acknowledgements

- **[FastAPI Documentation](https://fastapi.tiangolo.com/#example-upgrade)** for providing a comprehensive guide to building APIs.
- **[SQLite Documentation](https://www.sqlite.org/docs.html)** for database management insights.
- **[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)** ORM for handling database interactions
- **[APScheduler](https://pypi.org/project/APScheduler/)** for guidance on scheduling tasks
- **[Python](https://www.w3schools.com/python/default.asp)**
- **[Pydantic](https://docs.pydantic.dev/latest/)** for simplifying data validation and serialization in FastAPI

---

## ⚙️ Setup & Installation 

**1. Clone the Repository and Navigate into project folder**
```
$ git clone https://github.com/CloudSteph/habit-generator-api.git
$ cd habit-generator-api
```

**2. Create a Virtual Environment**
```
$ python -m venv api_env
$ source api_env/bin/activate
```

**3. Install Dependencies:**
```
$ pip install -r requirements.txt
```
Install all required Python packages using pip. This will install FastAPI, Uvicorn, and any other libraries the project needs.

**4. Initialize the Database**
```
$ python habit_tracker.init_db.py
```

**5. Start the FastAPI Server**
```
$ uvicorn main:app --reload
```
This will start the server at http://127.0.0.1:8000/ (reload flag is useful during development).

**6. Usage: Open API Documentation**
Once the server is running, you can interact with the API using either the interactive docs or an API client which FastAPI automatically generates:

- Swagger UI: Open your web browser and navigate to http://127.0.0.1:8000/docs and you'll see the Swagger UI where all endpoints are documented. You can send requests to the API directly from this interface. For example, you can try creating a new habit or fetching all habits without writing any code.
- ReDoc: Alternatively, visit http://127.0.0.1:8000/redoc for a nicely formatted documentation of the API (read-only documentation).
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json is a machine-readable description of the FastAPI application.
- Postman or cURL: Use requests for instance:
```
$ curl -X GET "http://127.0.0.1:8000/habits"
```

---

# 📁 Project Structure
```
habit-generator-api/ 
│── main.py      	        # FastAPI entry point 
│── api_env/       	        # Virtual environment 
│── data/
│ ├── habits.db             # SQLite database storage for habits
│── habit_tracker/          # Core API logic
│ ├── __init__.py 	    
│ ├── crud.py               # CRUD operations
│ ├── database.py           # Database connection
│ ├── init_db.py            # Initializes the database 
│ ├── models.py             # SQLAlchemy Models
│ ├── routes.py             # FastAPI Endpoints
│ ├── schemas.py            # Pydantic Models for Validation
│ ├── scheduled_reset.py    # Automated habit resets
│── logs/
│ ├── reset_log.txt         # Log files
│── .gitignore              # Ignore files
│── requirements.txt        # Lists Python dependencies required 
│── README.md 		        # Project documentation
```
---

## API Endpoints
The order of endpoints below are important because FastAPI processes them sequentially. Specific routes (like /habits/random) should come before dynamic routes (like /habits/{id}), otherwise, FastAPI may misinterpret random as well.

![img5.png](projects_images/img5.png)

## API Documentation

**1️⃣ Create a New Habit**
- Method: POST
- Endpoint: /habits/
- Description: Adds a new habit to the database.
Example Request (JSON BODY):
![img.png](projects_images/img.png)

**2️⃣ Get All Habits**
- Method: GET
- Endpoint: /habits/
- Description: Retrieves a list of all habits.
Example Response:
![img1.png](projects_images/img1.png)

**3️⃣ Get a Random Habit**
- Method: GET
- Endpoint: /habits/random
- Description: Returns a randomly selected habit, prioritizing habits with higher streaks.
Example Response:
![img2.png](projects_images/img2.png)

**4️⃣ Reset All Habits at Midnight**
- Method: POST
- Endpoint: /habits/reset
- Description: Resets all habits by setting completed_today to false at midnight.
Example Response:
![img3.png](projects_images/img3.png)

**5️⃣ Mark Habit completed**
- Method: PATCH
- Endpoint: /habits/{habit_id}/complete
- Description: Mark a habit as completed for today.
Example Response:
![img8.png](projects_images/img8.png)

**6️⃣ Retrieve a specific Habit**
- Method: GET
- Endpoint: /habits/{habit_id}
- Description: Retrieve a specific habit by id
![img9.png](projects_images/img9/png)

**7️⃣ Update an existing Habit**
- Method: PUT
- Endpoint: /habits/{habit_id}
- Description: Update a specific habit by id
![img10.png](projects_images/img10.png)

**8️⃣ Delete a habit**
- Method: DELETE
- Endpoint: /habits/{habit_id}
- Description: Deletes a specific habit by id
![img11.png](projects_images/img11.png)

---

## FastAPI Documentation (Screenshots)

**FastAPI UI (Swagger): 127.0.0.1:8000/docs**
![img6.png](projects_images/img6.png)

**OpenAPI JSON: 127.0.0.1:8000/openapi.json**
![img7.png](projects_images/img7.png)

---

## Testing in Postman
Since everything is set up locally, I tested the API using Postman by:
1. **Manually  entering API endpoints** like http://127.0.0.1:8000/habits/.
2. **Sending GET, POST, PUT, PATCH** requests to validate responses.
3. Checking the behavior of random habit selection and habit reset as well as other behaviors.

---

## Future Improvements
- Add unit tests

---

## 👩🏻‍💻 Author

Created by Stephanie Liew 🚀

---

## LICENSE

This project is licensed under the [MIT License](LICENSE.md).
