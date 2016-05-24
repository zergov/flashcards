class StudyCard(object):
    """
    Class representing a question card.

    A question card is simple card containing a Question and an Answer.
    """

    def __init__(self, question, answer):
        """
        Creates a Question card containing a question and an answer to the
        question.

        :param question: The question of the card.
        :param answer: The answer to the question.
        """
        self._question = question
        self._answer = answer

    @property
    def question(self):
        """
        Get the question of the card.

        :returns: The question of the card.
        """
        return self._question

    @question.setter
    def question(self, value):
        """
        Set a new value for the question of this card

        :param new_question: The new question

        :raises TypeError: If the question is not of type str
        """
        if isinstance(value, basestring):
            self._question = value
        else:
            raise TypeError('Question should be of type str')

    @property
    def answer(self):
        """
        Get the answer for the question

        :returns: The answer to the question.
        """
        return self._answer

    @answer.setter
    def answer(self, value):
        """
        Set a new value for the question of this card

        :param new_question: The new question

        :raises BadQuestionErr: If the question is not of type str
        """
        if isinstance(value, basestring):
            self._answer = value
        else:
            raise TypeError('Answer should be of type str')


