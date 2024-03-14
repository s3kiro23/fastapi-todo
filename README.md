# FastAPI REST API

## Description
This project is a FastAPI REST API that provides endpoints for interacting with a database.

## Requirements

Mysql
Python

## Installation
1. Clone the repository: `git clone https://github.com/s3kiro23/fastapi-todo-project.git`
2. Install venv: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate`
4. Upgrade pip: `python -m pip install --upgrade pip`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Create your .env then copy .env.development
6. Set up the database: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Usage
Create your bearer token first.
Method only available with valid token in headers.

- API endpoints:
  - `/api/v1/`: GET all todos list.
  - `/api/v1/`: POST create a todo.
  - `/api/v1/{todo_id}/`: GET a todo details.
  - `/api/v1/{todo_id}/`: PUT updata an existing todo.
  - `/api/v1/{todo_id}/`: DELETE a todo in db.
  - `/api/token`: POST create a token and return it.

- URL availables:
  - `api/docs/`: Swagger page to test api.
  - `api/redoc/`: Redoc api doc.