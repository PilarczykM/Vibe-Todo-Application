import click
from rich.console import Console
from rich.table import Table

from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.command()
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
