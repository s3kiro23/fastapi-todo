from .models import User
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, Field
from datetime import datetime

UserOut = pydantic_model_creator(User, name="UserOut")


class User(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
    is_verified: bool
    verified_at: datetime
    disabled: bool
    created_at: datetime
    updated_at: datetime

    @property
    def created_at(self) -> str:
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')  # format as you need

    @property
    def updated_at(self) -> str:
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')  # format as you need
    
    @property
    def verified_at(self) -> str:
        return self.verified_at.strftime('%Y-%m-%d %H:%M:%S')  # format as you need


class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=100)
    password_hash: str = Field(min_length=12, max_length=100)
