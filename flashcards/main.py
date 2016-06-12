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


@click.command('status')
def status():
    """
    Show status of the application.

    Displaying the currently selected studyset.
        - studyset title
        - studyset description
        - number of cards
    """
    studyset = storage.load_selected_studyset()
    data = (studyset.title, len(studyset._cards))
    click.echo('Currently using studyset: %s (%s cards)\n' % data)
    click.echo('Description: \n%s' % studyset.description)


# Add the subcommands to this main entry point.
cli.add_command(status)
cli.add_command(sets_commands.sets_group)
cli.add_command(cards_commands.cards_group)
