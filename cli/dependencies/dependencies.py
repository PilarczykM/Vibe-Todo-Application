from rich.console import Console

from core.json_repository import JsonTodoRepository
from core.use_cases import CreateTodo, DeleteTodo, GetAllTodos, GetTodoById, UpdateTodo

console = Console()

class CLIDependencies:
    def __init__(self):
        self.repo = JsonTodoRepository()
        self.create_todo = CreateTodo(todo_repo=self.repo)
        self.get_all_todos = GetAllTodos(todo_repo=self.repo)
        self.get_todo_by_id = GetTodoById(todo_repo=self.repo)
        self.update_todo = UpdateTodo(todo_repo=self.repo)
        self.delete_todo = DeleteTodo(todo_repo=self.repo) 