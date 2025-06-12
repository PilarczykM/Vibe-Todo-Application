from typing import Optional

import click
from rich.console import Console
from rich.table import Table

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


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.group()
def cli():
    """A simple Todo CLI application."""
    pass


@cli.command()
@click.argument("title")
@click.option("--description", "-d", help="Description of the todo item.")
@pass_dependencies
def add(dependencies: CLIDependencies, title: str, description: Optional[str]):
    """Add a new todo item."""
    try:
        todo = dependencies.create_todo.execute(title=title, description=description)
        console.print(f"[green]Todo added:[/green] ID=[cyan]{todo.id}[/cyan], Title='{todo.title}'")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")


@cli.command()
@pass_dependencies
def list(dependencies: CLIDependencies):
    """List all todo items."""
    todos = dependencies.get_all_todos.execute()
    if not todos:
        console.print("[yellow]No todo items found.[/yellow]")
        return

    table = Table(title="Todo List")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white", justify="left")
    table.add_column("Completed", style="green")
    table.add_column("Created At", style="blue", no_wrap=True)

    for todo in todos:
        completed_status = "[green]✔[/green]" if todo.completed else "[red]✘[/red]"
        table.add_row(
            todo.id,
            todo.title,
            todo.description if todo.description else "",
            completed_status,
            todo.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        )
    console.print(table)


@cli.command()
@click.argument("todo_id")
@pass_dependencies
def get(dependencies: CLIDependencies, todo_id: str):
    """Get a specific todo item by ID."""
    todo = dependencies.get_todo_by_id.execute(todo_id)
    if todo:
        console.print("[green]Todo Found:[/green]")
        console.print(f"  [bold]ID:[/bold] [cyan]{todo.id}[/cyan]")
        console.print(f"  [bold]Title:[/bold] {todo.title}")
        console.print(f"  [bold]Description:[/bold] {todo.description if todo.description else 'N/A'}")
        console.print(f"  [bold]Completed:[/bold] {'[green]Yes[/green]' if todo.completed else '[red]No[/red]'}")
        console.print(f"  [bold]Created At:[/bold] [blue]{todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}[/blue]")
    else:
        console.print(f"[red]Error:[/red] Todo with ID [cyan]{todo_id}[/cyan] not found.")


@cli.command()
@click.argument("todo_id")
@click.option("--title", "-t", help="New title for the todo item.")
@click.option("--description", "-d", help="New description for the todo item.")
@click.option("--completed/--not-completed", "-c/-n", default=None, help="Mark todo as completed or not completed.")
@pass_dependencies
def update(
    dependencies: CLIDependencies,
    todo_id: str,
    title: Optional[str],
    description: Optional[str],
    completed: Optional[bool],
):
    """Update an existing todo item."""
    if not any([title, description, completed]):
        console.print(
            "[yellow]No update parameters provided. "
            "Use --title, --description, or --completed/--not-completed.[/yellow]"
        )
        return
    try:
        updated_todo = dependencies.update_todo.execute(
            todo_id=todo_id, title=title, description=description, completed=completed
        )
        console.print(f"[green]Todo updated:[/green] ID=[cyan]{updated_todo.id}[/cyan], Title='{updated_todo.title}'")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")


@cli.command()
@click.argument("todo_id")
@pass_dependencies
def delete(dependencies: CLIDependencies, todo_id: str):
    """Delete a todo item by ID."""
    try:
        dependencies.delete_todo.execute(todo_id)
        console.print(f"[green]Todo with ID [cyan]{todo_id}[/cyan] deleted successfully.[/green]")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    cli()
