from dotenv import dotenv_values
from typing import List

values = dotenv_values()


class Config:
    DB_CONNECTION: str = values["DB_CONNECTION"]
    DB_MODELS: List[str] = ["todo.models", "auth.models"]
    SECRET_KEY: str = values["SECRET_KEY"]
