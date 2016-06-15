"""
flashcards.commands.cards
~~~~~~~~~~~~~~~~~~~

Contains the commands and subcommands related to the cards resource.
"""
import click

from flashcards import storage
from flashcards.cards import StudyCard


@click.group('cards')
def cards_group():
    """Command related to StudyCard objects """
    pass


@click.command('add')
@click.option('--question', prompt='Question')
@click.option('--answer', prompt='Answer')
def add(question, answer):
    """ Add a studycard to the currently selected studyset. """

    # Load the currently selected studyset
    try:
        studyset = storage.load_selected_studyset()

        # Create the card and add it to the studyset
        card = StudyCard(question, answer)
        studyset.add(card)

        # Update the studyset by overwriting the old information.
        storage.store_studyset(studyset)

        click.echo('Card added to the studyset !')

    except IOError:
        click.echo('There is no studyset currently selected. '
                   'Select a studyset to add a card.')


cards_group.add_command(add)
