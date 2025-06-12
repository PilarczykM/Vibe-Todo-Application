from datetime import datetime
from typing import List, Optional

import pytest

from core.entities import Todo
from core.repository import InMemoryTodoRepository
from core.use_cases import CreateTodo, DeleteTodo, GetAllTodos, GetTodoById, UpdateTodo


# Tests for core/entities.py
def test_todo_creation():
    todo = Todo(title="Test Todo")
    assert todo.title == "Test Todo"
    assert not todo.completed
    assert todo.description is None
    assert isinstance(todo.id, str)
    assert isinstance(todo.created_at, datetime)


def test_todo_creation_with_description():
    todo = Todo(title="Test Todo", description="This is a test description")
    assert todo.description == "This is a test description"


# Tests for core/repository.py
@pytest.fixture
def in_memory_repo():
    return InMemoryTodoRepository()


def test_create_todo(in_memory_repo):
    todo = Todo(title="Buy groceries")
    created_todo = in_memory_repo.create(todo)
    assert created_todo.id in in_memory_repo.todos
    assert in_memory_repo.get_by_id(created_todo.id) == todo


def test_get_all_todos(in_memory_repo):
    todo1 = Todo(title="Task 1")
    todo2 = Todo(title="Task 2")
    in_memory_repo.create(todo1)
    in_memory_repo.create(todo2)
    todos = in_memory_repo.get_all()
    assert len(todos) == 2
    assert todo1 in todos and todo2 in todos


def test_get_by_id(in_memory_repo):
    todo = Todo(title="Specific Task")
    in_memory_repo.create(todo)
    retrieved_todo = in_memory_repo.get_by_id(todo.id)
    assert retrieved_todo == todo


def test_get_by_id_not_found(in_memory_repo):
    assert in_memory_repo.get_by_id("non-existent-id") is None


def test_update_todo(in_memory_repo):
    todo = Todo(title="Old Title")
    in_memory_repo.create(todo)
    todo.title = "New Title"
    updated_todo = in_memory_repo.update(todo)
    assert updated_todo.title == "New Title"
    assert in_memory_repo.get_by_id(todo.id).title == "New Title"


def test_update_todo_not_found(in_memory_repo):
    todo = Todo(id="non-existent-id", title="Test")
    with pytest.raises(ValueError, match="Todo with ID non-existent-id not found."):
        in_memory_repo.update(todo)


def test_delete_todo(in_memory_repo):
    todo = Todo(title="Task to delete")
    in_memory_repo.create(todo)
    in_memory_repo.delete(todo.id)
    assert in_memory_repo.get_by_id(todo.id) is None


def test_delete_todo_not_found(in_memory_repo):
    with pytest.raises(ValueError, match="Todo with ID non-existent-id not found."):
        in_memory_repo.delete("non-existent-id")


# Tests for core/use_cases.py
# Using a simple mock for TodoRepository for use case tests
class MockTodoRepository:
    def __init__(self):
        self.todos = {}

    def create(self, todo: Todo) -> Todo:
        self.todos[todo.id] = todo
        return todo

    def get_all(self) -> List[Todo]:
        return list(self.todos.values())

    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        return self.todos.get(todo_id)

    def update(self, todo: Todo) -> Todo:
        if todo.id not in self.todos:
            raise ValueError("Todo not found")
        self.todos[todo.id] = todo
        return todo

    def delete(self, todo_id: str) -> None:
        if todo_id not in self.todos:
            raise ValueError("Todo not found")
        del self.todos[todo_id]


@pytest.fixture
def mock_repo():
    return MockTodoRepository()


def test_create_todo_use_case(mock_repo):
    create_todo = CreateTodo(todo_repo=mock_repo)
    todo = create_todo.execute(title="New Task", description="Details")
    assert todo.title == "New Task"
    assert mock_repo.get_by_id(todo.id) == todo


def test_get_all_todos_use_case(mock_repo):
    mock_repo.create(Todo(title="Task 1"))
    mock_repo.create(Todo(title="Task 2"))
    get_all_todos = GetAllTodos(todo_repo=mock_repo)
    todos = get_all_todos.execute()
    assert len(todos) == 2


def test_get_todo_by_id_use_case(mock_repo):
    todo = mock_repo.create(Todo(title="Find Me"))
    get_todo_by_id = GetTodoById(todo_repo=mock_repo)
    found_todo = get_todo_by_id.execute(todo.id)
    assert found_todo == todo


def test_get_todo_by_id_use_case_not_found(mock_repo):
    get_todo_by_id = GetTodoById(todo_repo=mock_repo)
    found_todo = get_todo_by_id.execute("non-existent")
    assert found_todo is None


def test_update_todo_use_case(mock_repo):
    todo = mock_repo.create(Todo(title="Original", completed=False))
    update_todo = UpdateTodo(todo_repo=mock_repo)
    updated_todo = update_todo.execute(todo.id, title="Updated Title", completed=True)
    assert updated_todo.title == "Updated Title"
    assert updated_todo.completed is True
    assert mock_repo.get_by_id(todo.id).title == "Updated Title"


def test_update_todo_use_case_not_found(mock_repo):
    update_todo = UpdateTodo(todo_repo=mock_repo)
    with pytest.raises(ValueError, match="Todo with ID non-existent-id not found."):
        update_todo.execute("non-existent-id", title="Test")


def test_delete_todo_use_case(mock_repo):
    todo = mock_repo.create(Todo(title="Delete Me"))
    delete_todo = DeleteTodo(todo_repo=mock_repo)
    delete_todo.execute(todo.id)
    assert mock_repo.get_by_id(todo.id) is None


def test_delete_todo_use_case_not_found(mock_repo):
    delete_todo = DeleteTodo(todo_repo=mock_repo)
    with pytest.raises(ValueError, match="Todo not found"):
        delete_todo.execute("non-existent-id")
