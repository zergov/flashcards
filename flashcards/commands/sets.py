import click

from flashcards import storage


@click.group('sets')
def sets():
    """Command related to the StudySet object """
    pass


@click.command('new')
@click.option('--title', prompt='Title of the study set')
@click.option('--desc', prompt='Description for the study set (optional)')
def new(title, desc):
    """Create a new study set. """

    print 'creating study set: %s' % title


sets.add_command(new)
