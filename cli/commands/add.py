from typing import Optional

import click
from rich.console import Console

from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.command()
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
