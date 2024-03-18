from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends
from .models import User
from auth.services import verify_token
from .schemas import UserOut, UserIn
from passlib.hash import bcrypt


router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(verify_token)],
)


# @router.get("/users/me", status_code=status.HTTP_200_OK)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user


@router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=UserOut
)
async def create_user(user: UserIn):
    user_obj = User(
        username=user.username,
        email=user.email,
        password_hash=bcrypt.hash(user.password_hash),
    )
    await user_obj.save()
    return await UserOut.from_tortoise_orm(user_obj)


@router.get("/delete", status_code=status.HTTP_200_OK)
async def delete_user():
    return "User deleted"


@router.get("/update", status_code=status.HTTP_200_OK)
async def update_user():
    return ""


# Path: auth/routing.py
