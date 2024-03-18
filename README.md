# FastAPI REST API

## Description
This project is a FastAPI REST API that provides endpoints for interacting with a database.
We utilized Aerich for migration and Tortoise-ORM for data manipulation.

## Requirements

- Mysql
- Python
- Docker

## Installation
1. Clone the repository: `git clone https://github.com/s3kiro23/fastapi-todo-project.git`
2. Create your .env by copy .env.development
3. Build the project with Docker: `docker-compose -f docker-compose.dev.yaml up -d`

## Usage
Create your bearer token first.
Methods only available with valid token in headers.

- Use this commands if you plan to update models : 
  - Init migration with Aerich: `aerich init -t db_config.ORM`
  - Init connection between app & db: `aerich init-db`
  - Create migration: `aerich migrate`
  - Update schema: `aerich upgrade`

- API endpoints:
  - `/auth/token`: POST create a token and return it.
  - `/api/v1/`: GET all todos list.
  - `/api/v1/`: POST create a todo.
  - `/api/v1/{todo_id}/`: GET a todo details.
  - `/api/v1/{todo_id}/`: PUT updata an existing todo.
  - `/api/v1/{todo_id}/`: DELETE a todo in db.

- URL availables:
  - `/docs/`: Swagger page to test api.
  - `/redoc/`: Redoc api doc.
