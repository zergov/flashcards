"""
flashcards.commands.cards
~~~~~~~~~~~~~~~~~~~

Contains the commands and subcommands related to the cards resource.
"""
import os
import tempfile
from subprocess import call

import click

from flashcards import storage
from flashcards.cards import StudyCard


@click.group('cards')
def cards_group():
    """Command related to StudyCard objects """
    pass


@click.command('add')
@click.option('-q', '--question', default=None)
@click.option('-a', '--answer', default=None)
@click.option('-e', 'editormode', flag_value=True, default=False)
def add(question, answer, editormode):
    """ Add a studycard to the currently selected studyset. """
    try:
        studyset = storage.load_selected_studyset()

        if question is None:
            question = _ask_for_question(editormode)

        if answer is None:
            answer = _ask_for_answer(editormode)

        # Create the card and add it to the studyset
        studyset.add(StudyCard(question, answer))
        # Update the studyset by overwriting the old information.
        storage.store_studyset(studyset)
        click.echo('Card added to the studyset !')

    except IOError:
        click.echo('There is no studyset currently selected. '
                   'Select a studyset to add a card.')


def _ask_for_question(editor_mode=False):
    """
    Prompt the user for a question.
    """
    return click.prompt('Question') if not editor_mode else prompt_via_editor()


def _ask_for_answer(editor_mode=False):
    """
    Prompt the user for an answer.
    """
    return click.prompt('Answer') if not editor_mode else prompt_via_editor()


def prompt_via_editor():
    """
    Open a temp file in an editor and return the input from the user.

    :returns: the input str from the user.
    """
    editor = os.environ.get('EDITOR', 'vim')
    data = ""

    with tempfile.NamedTemporaryFile(suffix='.tmp') as f:
        f.flush()
        call([editor, f.name])

        f.seek(0)
        data = f.read()

    return data

cards_group.add_command(add)
