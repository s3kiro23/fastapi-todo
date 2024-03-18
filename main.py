from fastapi import FastAPI
from todo.routing import router as todo_router
from auth.routing import router as auth_router
from user.routing import router as user_router
from tortoise.contrib.fastapi import register_tortoise
from settings.config import Config

app = FastAPI()
app.include_router(todo_router)
app.include_router(auth_router)
app.include_router(user_router)

register_tortoise(
    app,
    db_url=Config.DB_CONNECTION,
    modules={"models": Config.DB_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def health_check():
    return "Bienvenue sur l'API FastAPI pour gérer vos tâches !"
