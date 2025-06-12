from typing import Dict, List, Optional

from core.entities import Todo
from core.interfaces import TodoRepository


class InMemoryTodoRepository(TodoRepository):
    """In-memory implementation of the TodoRepository.

    This repository stores todo items in a dictionary, providing a simple
    in-memory data store for the application. It implements the `TodoRepository`
    interface.
    """

    def __init__(self):
        """Initialize the in-memory todo repository.

        The todos are stored in a dictionary where keys are todo IDs and values
        are Todo objects.
        """
        self.todos: Dict[str, Todo] = {}

    def create(self, todo: Todo) -> Todo:
        """Create a new todo item in memory.

        Parameters
        ----------
        todo : Todo
            The todo item to be created.

        Returns
        -------
        Todo
            The created todo item.
        """
        self.todos[todo.id] = todo
        return todo

    def get_all(self) -> List[Todo]:
        """Retrieve all todo items from memory.

        Returns
        -------
        List[Todo]
            A list of all todo items.
        """
        return list(self.todos.values())

    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        """Retrieve a specific todo item by its ID from memory.

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
        """Update an existing todo item in memory.

        Parameters
        ----------
        todo : Todo
            The todo item with updated information.

        Returns
        -------
        Todo
            The updated todo item.

        Raises
        ------
        ValueError
            If the todo item with the given ID is not found.
        """
        if todo.id not in self.todos:
            raise ValueError(f"Todo with ID {todo.id} not found.")
        self.todos[todo.id] = todo
        return todo

    def delete(self, todo_id: str) -> None:
        """Delete a todo item from memory by its ID.

        Parameters
        ----------
        todo_id : str
            The ID of the todo item to delete.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the todo item with the given ID is not found.
        """
        if todo_id not in self.todos:
            raise ValueError(f"Todo with ID {todo_id} not found.")
        del self.todos[todo_id]
