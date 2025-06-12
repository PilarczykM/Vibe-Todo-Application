from fastapi import Depends

from core.interfaces import TodoRepository
from core.repository import InMemoryTodoRepository
from core.use_cases import CreateTodo, DeleteTodo, GetAllTodos, GetTodoById, UpdateTodo

in_memory_repo_instance = InMemoryTodoRepository()


def get_todo_repository() -> TodoRepository:
    return in_memory_repo_instance


def get_create_todo_use_case(
    repo: TodoRepository = Depends(get_todo_repository),
) -> CreateTodo:
    return CreateTodo(todo_repo=repo)


def get_get_all_todos_use_case(
    repo: TodoRepository = Depends(get_todo_repository),
) -> GetAllTodos:
    return GetAllTodos(todo_repo=repo)


def get_get_todo_by_id_use_case(
    repo: TodoRepository = Depends(get_todo_repository),
) -> GetTodoById:
    return GetTodoById(todo_repo=repo)


def get_update_todo_use_case(
    repo: TodoRepository = Depends(get_todo_repository),
) -> UpdateTodo:
    return UpdateTodo(todo_repo=repo)


def get_delete_todo_use_case(
    repo: TodoRepository = Depends(get_todo_repository),
) -> DeleteTodo:
    return DeleteTodo(todo_repo=repo)
