# Project Tasks: Python Todo Application

Based on the `PRD.md` document, here's a breakdown of tasks to be completed, ordered for sequential development.

## Phase 1: Project Setup and Core Logic (Clean Architecture Foundation)

1.  **Project Structure Creation**
    *   Create the main project directories: `core`, `web`, `cli`, and `tests`.
    *   Initialize `__init__.py` files within each directory to make them Python packages.

2.  **Define Core Entities (`core/entities.py`)**
    *   Create a `Todo` dataclass or Pydantic model with `id`, `title`, `description` (optional), `completed` (boolean), and `created_at` (timestamp).
    *   Ensure type annotations are used for all fields.

3.  **Define Core Repository Interface (`core/interfaces.py`)**
    *   Create an abstract base class (ABC) for a `TodoRepository`.
    *   Define abstract methods for CRUD operations: `create`, `get_all`, `get_by_id`, `update`, `delete`.
    *   Include method signatures with type hints for parameters and return values.

4.  **Implement In-Memory Repository (`core/repository.py`)**
    *   Create a concrete implementation of `TodoRepository` that stores `Todo` items in an in-memory data structure (e.g., a dictionary or list).
    *   Implement UUID generation for `id`s for new todo items.
    *   Implement logic for each CRUD operation.

5.  **Implement Core Use Cases (`core/use_cases.py`)**
    *   Define classes/functions for core business logic operations that interact with the `TodoRepository`.
    *   Examples: `CreateTodo`, `GetAllTodos`, `GetTodoById`, `UpdateTodo`, `DeleteTodo`.
    *   Use dependency injection (e.g., constructor injection) to pass the `TodoRepository` instance to these use cases.
    *   Ensure all use cases are type-annotated.

6.  **Unit Tests for Core Logic (`tests/test_core.py`)**
    *   Write unit tests for the `core/entities.py`, `core/repository.py`, and `core/use_cases.py`.
    *   Use a testing framework (e.g., `pytest`).
    *   Mock the repository interface when testing use cases to isolate the business logic.

## Phase 2: Web Interface (FastAPI)

7.  **Web Data Models (`web/models.py`)**
    *   Define Pydantic models for request and response bodies specific to the FastAPI interface (e.g., `TodoCreate`, `TodoUpdate`, `TodoResponse`).
    *   Map these models to the `core.entities.Todo` model.

8.  **FastAPI Application Setup (`web/main.py`)**
    *   Initialize the FastAPI application.
    *   Set up dependency injection for the `TodoRepository` and use cases.
    *   Define API endpoints for CRUD operations (e.g., `/todos`, `/todos/{id}`).
    *   Implement endpoint logic that calls the appropriate core use cases.
    *   Include error handling for common scenarios (e.g., 404 for not found).

## Phase 3: CLI Interface (Click and Rich)

9.  **CLI Commands Setup (`cli/main.py`)**
    *   Initialize the Click application.
    *   Define top-level commands (e.g., `todo add`, `todo list`, `todo update`, `todo delete`).
    *   Set up dependency injection for the `TodoRepository` and use cases, similar to the web interface.

10. **Implement CLI Operations (`cli/commands.py`)**
    *   Implement the logic for each CLI command.
    *   Parse command-line arguments and options.
    *   Call the appropriate core use cases.
    *   Use Rich for structured and colored output (e.g., success messages, error messages, formatted todo lists).

## Phase 4: Documentation and Final Touches

11. **Update `README.md`**
    *   Add instructions on how to install dependencies, run the web application, and use the CLI commands.
    *   Include examples for both interfaces.

12. **Create `requirements.txt`**
    *   List all Python dependencies with their versions (FastAPI, Uvicorn, Click, Rich, Pydantic, pytest).

13. **Review and Refine**
    *   Review code for adherence to clean architecture principles and type annotations.
    *   Ensure functional equivalence between web and CLI interfaces.
    *   Perform basic integration testing. 