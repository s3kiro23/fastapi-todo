from .models import User
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, Field

UserOut = pydantic_model_creator(User, name="UserOut")


class User(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
    is_verified: bool
    verified_at: str
    disabled: bool
    created_at: str
    updated_at: str


class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=100)
    password_hash: str = Field(min_length=12, max_length=100)
