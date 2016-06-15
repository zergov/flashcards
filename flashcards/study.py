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
    Object that encapsulate a Study session. This object cycle through
    an iterator of StudyCard.
    """
    def start(self, cards):
        """
        Start a StudySession with the iterator of cards given.

        :param cards: cards iterator.
        """
        for card in cards:
            click.clear()
            self.show_question(card.question)
            self.show_answer(card.answer)

    def show_question(self, question):
        """
        Display the current question to the user.

        :param question: the question to display
        """
        click.echo('\n' + question + '\n')
        click.pause('...')

    def show_answer(self, answer):
        """
        Display the answer to the question.

        :param answer: the answer
        """
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
