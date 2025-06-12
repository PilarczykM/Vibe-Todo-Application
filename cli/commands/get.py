import click
from rich.console import Console

from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.command()
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
