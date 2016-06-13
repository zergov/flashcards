"""
flashcards.commands.sets
~~~~~~~~~~~~~~~~~~~

Contains the commands and subcommands related to the sets resource.
"""


import os
import click

from flashcards import sets
from flashcards import storage


@click.group('sets')
def sets_group():
    """Command related to the StudySet object """
    pass


@click.command('new')
@click.option('--title', prompt='Title of the study set')
@click.option('--desc', prompt='Description for the study set (optional)')
def new(title, desc):
    """
    Create a new study set.

    User supplies a title and a description.
    If this study set does not exist, it is created.
    """
    study_set = sets.StudySet(title, desc)
    filepath = storage.create_studyset_file(study_set)

    # automatically select this studyset
    storage.link_selected_studyset(filepath)
    click.echo('Study set created !')


@click.command('select')
@click.argument('studyset')
def select(studyset):
    studyset_path = os.path.join(storage.studyset_storage_path(), studyset)
    storage.link_selected_studyset(studyset_path)
    studyset_obj = storage.load_studyset(studyset_path).load()
    click.echo('Selected studyset: %s' % studyset_obj.title)
    click.echo('Next created cards will be automatically added '
               'to this studyset.')


sets_group.add_command(new)
sets_group.add_command(select)
