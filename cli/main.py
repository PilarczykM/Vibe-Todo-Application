import click
from rich.console import Console

from cli.commands.add import add
from cli.commands.delete import delete
from cli.commands.get import get
from cli.commands.list import list
from cli.commands.update import update
from cli.dependencies.dependencies import CLIDependencies

console = Console()


pass_dependencies = click.make_pass_decorator(CLIDependencies, ensure=True)


@click.group()
def cli():
    """A simple Todo CLI application."""
    pass


cli.add_command(add)
cli.add_command(list)
cli.add_command(get)
cli.add_command(update)
cli.add_command(delete)


if __name__ == "__main__":
    cli()
