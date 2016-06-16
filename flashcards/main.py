"""
flashcards.main
~~~~~~~~~~~~~~~~~~~

Main entry point of the application.
Contain commands and sub-commands grouping logic.
"""
import os

import click

from flashcards import storage
from flashcards import study
from flashcards.commands import sets as sets_commands
from flashcards.commands import cards as cards_commands


@click.group()
def cli():
    """
    Command line application that focus on creating decks of flashcards
    quickly and easily.
    """
    # Verify that the storage directory is present.
    storage.verify_storage_dir_integrity()
    pass


@click.command('status')
def status_cmd():
    """
    Show status of the application.

    Displaying the currently selected studyset.
        - studyset title
        - studyset description
        - number of cards
    """
    try:
        studyset = storage.load_selected_studyset()

        click.echo('Currently selected studyset: %s \n' % studyset.title)
        click.echo('[NUMBER OF CARDS]: %s \n' % len(studyset))
        click.echo('[DESCRIPTION]:')
        click.echo(studyset.description + '\n')

    except IOError:
        click.echo('No studyset currently selected.')


@click.command('study')
@click.argument('studyset')
@click.option('-m', '--mode', default=None)
def study_cmd(studyset, mode):
    """
    Start a study session.

    Study the studyset passed via the studyset argument.
    """
    studyset_path = os.path.join(storage.studyset_storage_path(), studyset)
    studyset = storage.load_studyset(studyset_path).load()

    studysession = study.get_study_session_template(mode)
    studysession.start(studyset)


# Add the subcommands to this main entry point.
cli.add_command(status_cmd)
cli.add_command(study_cmd)
cli.add_command(sets_commands.sets_group)
cli.add_command(cards_commands.cards_group)
