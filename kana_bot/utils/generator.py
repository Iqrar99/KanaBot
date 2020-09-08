import random
from .kana_bot_error import KanaTypeError
from .letters import JLetters


class QuizGenerator(object):
    """Class to generate questions for quiz."""
    jletters = JLetters()
    QUESTION_LIMIT = 20  # the number of question to be displayed
    question_counter = 0
    question_list = []
    answer_list = []
    user_answer_list = []
    result = []
    score = 0

    def __init__(self, kana_type: str, quiz_type: int):
        self.kana_type = kana_type
        self.quiz_type = quiz_type
        self.question_counter = 0
        self.question_list = []
        self.answer_list = []
        self.user_answer_list = []
        self.result = []
        self.score = 0

        if kana_type == "HIRAGANA":
            if quiz_type == 1:
                self.create_hiragana_quiz1()
            else:
                self.create_hiragana_quiz2()

        elif kana_type == "KATAKANA":
            if quiz_type == 1:
                self.create_katakana_quiz1()
            else:
                self.create_katakana_quiz2()

        else:
            raise KanaTypeError(
                "Unrecognized `kana_type`. Should be only 'HIRAGANA' or 'KATAKANA'. " +
                f"Got '{kana_type}' instead.")

    def create_hiragana_quiz1(self):
        """Hiragana to Romaji quiz."""

        all_letters = self.jletters.get_all_hiragana()
        taken = set()  # avoid taking the same letter for the questions
        while len(taken) != self.QUESTION_LIMIT:
            letter = random.choice(all_letters)
            if letter not in taken:
                taken.add(letter)

        self.question_list = list(taken)
        for i in range(self.QUESTION_LIMIT):
            answer = self.jletters.get_romaji(self.question_list[i])
            self.answer_list.append(answer)

    def create_hiragana_quiz2(self):
        """Romaji to Hiragana"""

        pass

    def create_katakana_quiz1(self):
        """Katakana to Romaji"""

        pass

    def create_katakana_quiz2(self):
        """Romaji to Katakana"""

        pass

    def get_score(self) -> int:
        for r in self.result:
            self.score += 10 if r else 0

        return self.score

    def increase_counter(self):
        self.question_counter += 1

    def get_counter(self) -> int:
        return self.question_counter

    def get_question(self, idx: int) -> str:
        return self.question_list[idx]

    def add_user_answer(self, answer: str):
        self.user_answer_list.append(answer)

    def get_user_answer(self, idx: int) -> str:
        return self.user_answer_list[idx]

    def get_true_answer(self, idx: int) -> str:
        return self.answer_list[idx]

    def add_result(self, result: bool):
        self.result.append(result)

    def get_result(self, idx: int) -> bool:
        return self.result[idx]


if __name__ == '__main__':
    g = QuizGenerator("HIRAGANA", 1)
    print(g.question_list)
    print(g.answer_list)
