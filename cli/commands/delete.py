import click
from rich.console import Console

from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.command()
@click.argument("todo_id")
@pass_dependencies
def delete(dependencies: CLIDependencies, todo_id: str):
    """Delete a todo item by ID."""
    try:
        dependencies.delete_todo.execute(todo_id)
        console.print(f"[green]Todo with ID [cyan]{todo_id}[/cyan] deleted successfully.[/green]")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
