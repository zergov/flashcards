import click

from flashcards import storage
from flashcards.commands import sets as sets_commands
from flashcards.commands import cards as cards_commands


@click.group()
def cli():
    """ Main entry point of the application """

    # Verify that the storage directory is present.
    storage.verify_storage_dir_integrity()
    pass


# Add the subcommands to this main entry point.
cli.add_command(sets_commands.sets_group)
cli.add_command(cards_commands.cards_group)
