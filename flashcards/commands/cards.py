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
@click.option('-e', 'editormode', flag_value=True, default=False)
def add(editormode):
    """ Add a studycard to the currently selected studyset. """
    try:
        studyset = storage.load_selected_studyset()

        question = _ask_for_question(editormode)
        answer = _ask_for_answer(editormode)

        # Create the card and add it to the studyset
        # Update the studyset by overwriting the old information.
        studyset.add(StudyCard(question, answer))
        storage.store_studyset(studyset)

        click.echo('Card added to the studyset !')

    except IOError:
        click.echo('There is no studyset currently selected. '
                   'Select a studyset to add a card.')


def _ask_for_question(editor_mode=False):
    """
    Prompt the user for a question.
    """
    if editor_mode:
        message = "\n# Write your question."
        return prompt_via_editor('TMP_QUESTION_', message)
    else:
        return click.prompt('Question')


def _ask_for_answer(editor_mode=False):
    """
    Prompt the user for an answer.
    """
    if editor_mode:
        message = "\n# Write your answer."
        return prompt_via_editor('TMP_ANSWER_', message)
    else:
        return click.prompt('Answer')


def prompt_via_editor(filename, init_message=None):
    """
    Open a temp file in an editor and return the input from the user.

    :param init_message: an initial message to write in the editor.

    :returns: the input str from the user.
    """
    editor = os.environ.get('EDITOR', 'vim')
    filecontent = ""

    with tempfile.NamedTemporaryFile(prefix=filename, suffix='.tmp') as f:
        # write initial message
        if init_message is not None:
            f.write(init_message)

        f.flush()
        call([editor, f.name])  # call the editor to open this file.

        f.seek(0)
        filecontent = f.read()

    return _remove_lines_starting_with(filecontent, '#')


def _remove_lines_starting_with(string, start_char):
    """
    Utility function that removes line starting with the given character in the
    provided str.

    :param data: the str to remove lines.
    :param start_char: the character to look for at the begining of a line.

    :returns: the string without the lines starting with start_char.
    """
    data = ""
    for line in string.split('\n'):
        if not line.startswith(start_char):
            data += line + '\n'

    return data

cards_group.add_command(add)
