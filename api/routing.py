import token
from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends
from .schemas import TodoGet, TodoPost, TodoPut
from .models import Todo, Token
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt
from settings.config import Config
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/v1", tags=["Todos"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = Config.SECRET_KEY
ALGORITHM = "HS256"


async def verify_token(token: str = Depends(oauth2_scheme)):
    token_exists = await Token.filter(token=token).exists()
    if not token_exists:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


@router.post(
    "/token", status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_token)]
)
async def generate_token():
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=30)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    await Token.create(token=encoded_jwt)
    return {"access_token": encoded_jwt, "token_type": "bearer"}


@router.get("/", dependencies=[Depends(verify_token)])
async def all_todos():
    return await TodoGet.from_queryset(Todo.all())


@router.post(
    "/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_token)]
)
async def create(body: TodoPost):
    data = body.model_dump(exclude_unset=True)
    todo_obj = await Todo.create(**data)
    return await TodoGet.from_tortoise_orm(todo_obj)


@router.put(
    "/{todo_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(verify_token)]
)
async def update(todo_id: str, body: TodoPut):
    todo_exists = await Todo.filter(id=todo_id).exists()
    if not todo_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    data = body.model_dump(exclude_unset=True)
    await Todo.filter(id=todo_id).update(**data)
    return "Update successful"


@router.delete(
    "/{todo_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(verify_token)]
)
async def delete(todo_id: str):
    todo_exists = await Todo.filter(id=todo_id).exists()
    if not todo_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    await Todo.filter(id=todo_id).delete()
    return "Todo deleted"
