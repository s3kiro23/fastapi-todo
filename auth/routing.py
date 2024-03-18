from fastapi.routing import APIRouter
from fastapi import status
from .models import Token

from jose import jwt
from settings.config import Config
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = Config.SECRET_KEY
ALGORITHM = "HS256"


@router.post("/token", status_code=status.HTTP_201_CREATED)
async def generate_token():
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=30)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    await Token.create(token=encoded_jwt)
    return {"access_token": encoded_jwt, "token_type": "bearer"}
