from fastapi.routing import APIRouter
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from .models import Token
from user.schemas import UserOut

from jose import jwt
from settings.config import Config
from datetime import datetime, timedelta
from .services import authenticated_user

router = APIRouter(
    prefix="/auth", tags=["Auth"], responses={404: {"description": "Not found"}}
)

SECRET_KEY = Config.SECRET_KEY
ALGORITHM = "HS256"


@router.post("/token", status_code=status.HTTP_201_CREATED)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticated_user(form_data.username, form_data.password)

    if not user:
        return {"error": "Invalid credentials"}

    data = await UserOut.from_tortoise_orm(user)
    user_obj = data.model_dump(exclude_unset=True)
    encoded_jwt = jwt.encode(user_obj, SECRET_KEY, algorithm=ALGORITHM)
    await Token.create(token=encoded_jwt)
    return {"access_token": encoded_jwt, "token_type": "bearer"}


@router.post("/refresh", status_code=status.HTTP_201_CREATED)
async def refresh_token():
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=30)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    await Token.filter().delete()
    await Token.create(token=encoded_jwt)
    return {"access_token": encoded_jwt, "token_type": "bearer"}
