import click

from flashcards.commands import sets as sets_commands


@click.group()
def cli():
    """ Main entry point of the application """
    pass


cli.add_command(sets_commands.sets_group)
