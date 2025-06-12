import json
from datetime import datetime
from typing import List, Optional

from core.entities import Todo
from core.interfaces import TodoRepository


class JsonTodoRepository(TodoRepository):
    """A Todo repository implementation that stores data in a JSON file.

    This repository handles serialization and deserialization of Todo objects
    to and from a specified JSON file, ensuring data persistence.
    """

    def __init__(self, file_path: str = "todos.json"):
        """Initialize the JSON todo repository.

        Parameters
        ----------
        file_path : str, optional
            The path to the JSON file where todos will be stored, by default
            "todos.json".
        """
        self.file_path = file_path
        self.todos = self._load_todos()

    def _load_todos(self) -> dict[str, Todo]:
        """Load todo items from the JSON file.

        If the file does not exist or is empty, an empty dictionary is returned.

        Returns
        -------
        dict[str, Todo]
            A dictionary of todo items, keyed by their IDs.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                todos = {
                    item["id"]: Todo(
                        id=item["id"],
                        title=item["title"],
                        description=item["description"],
                        completed=item["completed"],
                        created_at=datetime.fromisoformat(item["created_at"]),
                    )
                    for item in data
                }
                return todos
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_todos(self) -> None:
        """Save current todo items to the JSON file.

        This method serializes the dictionary of Todo objects into a JSON
        array and writes it to the specified file path.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            data = [
                {
                    "id": str(todo.id),
                    "title": todo.title,
                    "description": todo.description,
                    "completed": todo.completed,
                    "created_at": todo.created_at.isoformat(),
                }
                for todo in self.todos.values()
            ]
            json.dump(data, f, indent=4, ensure_ascii=False)

    def create(self, todo: Todo) -> Todo:
        """Create a new todo item in the repository.

        Parameters
        ----------
        todo : Todo
            The todo item to be created.

        Returns
        -------
        Todo
            The created todo item.
        """
        self.todos[str(todo.id)] = todo
        self._save_todos()
        return todo

    def get_all(self) -> List[Todo]:
        """Retrieve all todo items from the repository.

        Returns
        -------
        List[Todo]
            A list of all todo items.
        """
        return list(self.todos.values())

    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        """Retrieve a specific todo item by its ID.

        Parameters
        ----------
        todo_id : str
            The ID of the todo item to retrieve.

        Returns
        -------
        Optional[Todo]
            The retrieved todo item, or None if not found.
        """
        return self.todos.get(todo_id)

    def update(self, todo: Todo) -> Todo:
        """Update an existing todo item in the repository.

        Parameters
        ----------
        todo : Todo
            The todo item with updated information.

        Returns
        -------
        Todo
            The updated todo item.
        """
        if str(todo.id) not in self.todos:
            raise ValueError(f"Todo with ID {todo.id} not found.")
        self.todos[str(todo.id)] = todo
        self._save_todos()
        return todo

    def delete(self, todo_id: str) -> None:
        """Delete a todo item from the repository by its ID.

        Parameters
        ----------
        todo_id : str
            The ID of the todo item to delete.

        Returns
        -------
        None
        """
        if todo_id not in self.todos:
            raise ValueError(f"Todo with ID {todo_id} not found.")
        del self.todos[todo_id]
        self._save_todos()
