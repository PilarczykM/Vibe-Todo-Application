from fastapi import APIRouter, Depends, HTTPException

from core.use_cases import CreateTodo, DeleteTodo, GetAllTodos, GetTodoById, UpdateTodo
from web.dependencies.dependencies import (
    get_create_todo_use_case,
    get_delete_todo_use_case,
    get_get_all_todos_use_case,
    get_get_todo_by_id_use_case,
    get_update_todo_use_case,
)
from web.schemas.models import TodoCreate, TodoResponse, TodoUpdate

router = APIRouter()


@router.post("/todos/", response_model=TodoResponse, status_code=201)
def create_todo_endpoint(todo_create: TodoCreate, create_todo: CreateTodo = Depends(get_create_todo_use_case)):
    todo = create_todo.execute(title=todo_create.title, description=todo_create.description)
    return TodoResponse.model_validate(todo)


@router.get("/todos/")
def get_all_todos_endpoint(
    get_all_todos: GetAllTodos = Depends(get_get_all_todos_use_case),
):
    todos = get_all_todos.execute()
    return [TodoResponse.model_validate(todo) for todo in todos]


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo_by_id_endpoint(todo_id: str, get_todo_by_id: GetTodoById = Depends(get_get_todo_by_id_use_case)):
    todo = get_todo_by_id.execute(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponse.model_validate(todo)


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo_endpoint(
    todo_id: str,
    todo_update: TodoUpdate,
    update_todo: UpdateTodo = Depends(get_update_todo_use_case),
):
    try:
        todo = update_todo.execute(
            todo_id=todo_id,
            title=todo_update.title,
            description=todo_update.description,
            completed=todo_update.completed,
        )
        return TodoResponse.model_validate(todo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo_endpoint(todo_id: str, delete_todo: DeleteTodo = Depends(get_delete_todo_use_case)):
    try:
        delete_todo.execute(todo_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Todo deleted successfully"}
