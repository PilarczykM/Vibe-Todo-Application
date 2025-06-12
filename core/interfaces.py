from abc import ABC, abstractmethod
from typing import List, Optional

from core.entities import Todo


class TodoRepository(ABC):
    """Abstract base class for a Todo repository.

    This interface defines the contract for any class that wishes to act as a
    repository for `Todo` objects, ensuring consistent CRUD operations.
    """

    @abstractmethod
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
        pass

    @abstractmethod
    def get_all(self) -> List[Todo]:
        """Retrieve all todo items from the repository.

        Returns
        -------
        List[Todo]
            A list of all todo items.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass
