"""
flashcards.study
~~~~~~~~~~~~~~~~~~~

Contain the StudySession logic.
This module should host the class that subclasses BaseStudySession.
"""
import random

import click


class BaseStudySession(object):
    """
    Basic Object that encapsulate a Study session.
    This object cycle through an iterator of StudyCard.

    The algorithm sequence stays the same, each iteration of cards follows this
    pattern:

        1) Show the question
        2) Wait for user input
        3) Show the answer
        4) Wait for user input
    """
    def start(self, cards):
        """
        Start a StudySession with the iterator of cards given.

        :param cards: cards iterator.
        """
        self.question_num = len(cards)
        self.question_count = 1  # starts at 1 for display convenience

        for card in cards:
            click.clear()
            self.show_question(card.question)
            self.show_answer(card.answer)

    def show_question(self, question):
        """
        Display the current question to the user.

        :param question: the question to display
        """
        header = '[QUESTION %s / %s]' % (self.question_count, self.question_num)
        click.echo(header)
        click.echo('\n' + question + '\n')
        click.pause('...')

    def show_answer(self, answer):
        """
        Display the answer to the question.

        :param answer: the answer
        """
        self.question_count += 1
        click.echo('\n' + answer + '\n')
        click.pause('Press any key to show next question')


class ShuffledStudySession(BaseStudySession):
    """
    StudySession that shuffles the cards before iterating on them.
    """

    def start(self, cards):
        """
        Start a studySession with the iterator of cards given.
        The cards are shuffled before beeing displayed.

        :param cards: cards iterator.
        """
        # Shuffle the given cards iterator
        cards_list = list(cards)
        random.shuffle(cards_list)

        super(ShuffledStudySession, self).start(cards_list)


# Association of Study session modes to the respective class instance.
STUDY_MODES = {'linear': BaseStudySession,
               'shuffled': ShuffledStudySession}


def get_study_session_template(sessionMode):
    """
    Depending on the sessionMode input entered by the user,
    return the appropriate instance of BaseStudySession.

    :param sessionMode: the desired study mode (default to 'linear')

    :returns: instance of BaseStudySession
    """

    if sessionMode not in STUDY_MODES:
        return BaseStudySession()
    else:
        return STUDY_MODES[sessionMode]()
