from typing import List, Optional

from core.entities import Todo
from core.interfaces import TodoRepository


class CreateTodo:
    """Use case for creating new todo items.

    This class encapsulates the logic for adding a new todo item to the repository.
    """

    def __init__(self, todo_repo: TodoRepository):
        """Initialize the CreateTodo use case.

        Parameters
        ----------
        todo_repo : TodoRepository
            The repository interface for interacting with todo items.
        """
        self.todo_repo = todo_repo

    def execute(self, title: str, description: Optional[str] = None) -> Todo:
        """Execute the create todo operation.

        Parameters
        ----------
        title : str
            The title of the new todo item.
        description : Optional[str], optional
            An optional description for the new todo item, by default None.

        Returns
        -------
        Todo
            The newly created todo item.
        """
        todo = Todo(title=title, description=description)
        return self.todo_repo.create(todo)


class GetAllTodos:
    """Use case for retrieving all todo items.

    This class encapsulates the logic for fetching all todo items from the repository.
    """

    def __init__(self, todo_repo: TodoRepository):
        """Initialize the GetAllTodos use case.

        Parameters
        ----------
        todo_repo : TodoRepository
            The repository interface for interacting with todo items.
        """
        self.todo_repo = todo_repo

    def execute(self) -> List[Todo]:
        """Execute the get all todos operation.

        Returns
        -------
        List[Todo]
            A list of all todo items.
        """
        return self.todo_repo.get_all()


class GetTodoById:
    """Use case for retrieving a single todo item by ID.

    This class encapsulates the logic for fetching a specific todo item from the
    repository using its unique identifier.
    """

    def __init__(self, todo_repo: TodoRepository):
        """Initialize the GetTodoById use case.

        Parameters
        ----------
        todo_repo : TodoRepository
            The repository interface for interacting with todo items.
        """
        self.todo_repo = todo_repo

    def execute(self, todo_id: str) -> Optional[Todo]:
        """Execute the get todo by ID operation.

        Parameters
        ----------
        todo_id : str
            The ID of the todo item to retrieve.

        Returns
        -------
        Optional[Todo]
            The retrieved todo item, or None if not found.
        """
        return self.todo_repo.get_by_id(todo_id)


class UpdateTodo:
    """Use case for updating an existing todo item.

    This class encapsulates the logic for modifying an existing todo item in the
    repository.
    """

    def __init__(self, todo_repo: TodoRepository):
        """Initialize the UpdateTodo use case.

        Parameters
        ----------
        todo_repo : TodoRepository
            The repository interface for interacting with todo items.
        """
        self.todo_repo = todo_repo

    def execute(
        self,
        todo_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> Todo:
        """Execute the update todo operation.

        Parameters
        ----------
        todo_id : str
            The ID of the todo item to update.
        title : Optional[str], optional
            The new title for the todo item, by default None.
        description : Optional[str], optional
            The new description for the todo item, by default None.
        completed : Optional[bool], optional
            Boolean to mark the todo item as completed or not completed, by default None.

        Returns
        -------
        Todo
            The updated todo item.

        Raises
        ------
        ValueError
            If the todo item with the given ID is not found.
        """
        todo = self.todo_repo.get_by_id(todo_id)
        if not todo:
            raise ValueError(f"Todo with ID {todo_id} not found.")

        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed

        return self.todo_repo.update(todo)


class DeleteTodo:
    """Use case for deleting a todo item.

    This class encapsulates the logic for removing a todo item from the repository.
    """

    def __init__(self, todo_repo: TodoRepository):
        """Initialize the DeleteTodo use case.

        Parameters
        ----------
        todo_repo : TodoRepository
            The repository interface for interacting with todo items.
        """
        self.todo_repo = todo_repo

    def execute(self, todo_id: str) -> None:
        """Execute the delete todo operation.

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
        self.todo_repo.delete(todo_id)
