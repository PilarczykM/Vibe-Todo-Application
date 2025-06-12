# Python Todo Application

This is a Python-based Todo application featuring both a web interface (using FastAPI) and a command-line interface (CLI) using Click and Rich. It's designed following clean architecture principles, emphasizing modularity, testability, and a clear separation of concerns.

## Features

- **Core Logic**: Shared business logic for CRUD (Create, Read, Update, Delete) operations on todo items.
- **Web Interface**: RESTful API for managing todos using FastAPI.
- **CLI Interface**: Command-line tools for managing todos using Click and Rich for enhanced output.
- **In-Memory Storage**: Data is stored in memory, allowing for easy extensibility to other databases in the future.
- **Type-Annotated**: All code is type-annotated for better readability and maintainability.
- **Unit Tests**: Basic unit tests for the core business logic.

## Project Structure

- `core/`: Contains the core business logic, entities (Todo), interfaces (TodoRepository), and use cases.
- `web/`: Contains the FastAPI application, including API endpoints and web-specific models.
- `cli/`: Contains the Click CLI application and its commands.
- `tests/`: Contains unit tests for the core logic.

## Setup and Installation

1.  **Clone the repository (if not already done):**
    ```bash
    git clone <repository-url>
    cd todo-app
    ```

2.  **Create a virtual environment and activate it:**

    **Install dependencies:**
    ```bash
    uv sync
    ```

## Running the Application

### Web Interface (FastAPI)

To run the FastAPI web application, use Uvicorn:

```bash
uv run uvicorn web.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### CLI Interface (Click)

To use the CLI, run commands from the project root:

#### Add a new todo:
```bash
uv run python -m cli.main add "Buy groceries" -d "Milk, eggs, bread"
```

#### List all todos:
```bash
uv run python -m cli.main list
```

#### Get a specific todo by ID:
(Replace `<todo_id>` with an actual ID from the list command output)
```bash
uv run python -m cli.main get <todo_id>
```

#### Update a todo:
```bash
uv run python -m cli.main update <todo_id> --title "Buy organic groceries" --completed
uv run python -m cli.main update <todo_id> --not-completed
```

#### Delete a todo:
```bash
uv run python -m cli.main delete <todo_id>
```

## Running Tests

To run the unit tests for the core logic, make sure you have `pytest` installed (included in `requirements.txt`) and run:

```bash
uv run pytest tests/
```
