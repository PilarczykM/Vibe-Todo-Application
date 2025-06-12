import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Todo:
    """Represents a single todo item.

    Attributes
    ----------
    title : str
        The title of the todo item.
    id : str
        A unique identifier for the todo item, generated automatically.
    description : Optional[str], optional
        An optional description for the todo item, by default None.
    completed : bool, optional
        Indicates whether the todo item is completed, by default False.
    created_at : datetime, optional
        The timestamp when the todo item was created, generated automatically.
    """

    title: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
