from typing import Optional

import click
from rich.console import Console

from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.command()
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
