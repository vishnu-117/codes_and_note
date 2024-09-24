Step 1.Initialize Alembic:
alembic init alembic

Step 2.Edit alembic.ini:
Change the sqlalchemy.url to match your SQLALCHEMY_DATABASE_URI from config.py.
sqlalchemy.url = sqlite:///./test.db

Step 3.Generate the Initial Migration:
alembic revision --autogenerate -m "Initial migration"

Step 4.Apply the Migration:
alembic upgrade head

Step 5: Running the App
uvicorn app.main:app --reload


Summary of Routes:
POST /tasks/: Create a new task.
GET /tasks/: Get all tasks.
GET /tasks/{task_id}: Get a specific task by ID.
PUT /tasks/{task_id}: Update task status (complete or incomplete).
DELETE /tasks/{task_id}: Delete a task by ID.