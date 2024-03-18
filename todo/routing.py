from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends
from .schemas import TodoGet, TodoPost, TodoPut
from .models import Todo
from auth.services import verify_token

router = APIRouter(prefix="/api/v1", tags=["Todos"])


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
