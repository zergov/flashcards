import click


class BaseStudySession(object):
    """
    Object that encapsulate a Study session. This object cycle through
    an iterator of StudyCard.
    """
    def start(self, cards):
        """
        Start a StudySession with the given study strategy.

        :param cards: cards itterator.
        :param study_strategy: an instance of StudyStrategy.
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
        print '\n'
        print question + '\n'
        click.pause('...')

    def show_answer(self, answer):
        """
        Display the answer to the question.

        :param answer: the answer
        """
        print '\n'
        print answer + '\n'
        click.pause('Press any key to show next question')
