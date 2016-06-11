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
    storage.create_study_set_file(study_set)
    click.echo('Study set created !')


@click.command('select')
@click.argument('studyset')
def select(studyset):
    studyset_path = os.path.join(storage.studyset_storage_path(), studyset)
    print studyset_path


sets_group.add_command(new)
sets_group.add_command(select)
