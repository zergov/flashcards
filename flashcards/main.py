import click

from flashcards import storage
from flashcards.commands import sets as sets_commands


@click.group()
def cli():
    """ Main entry point of the application """

    # Verify that the storage directory is present.
    storage.verify_storage_dir_integrity()
    pass


cli.add_command(sets_commands.sets_group)
