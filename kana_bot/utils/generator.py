from .kana_bot_error import KanaTypeError


class QuizGenerator(object):
    """Class to generate questions for quiz."""

    def __init__(self, kana_type: str, quiz_type: int):
        self.kana_type = kana_type
        self.quiz_type = quiz_type
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
        pass

    def create_hiragana_quiz2(self):
        pass

    def create_katakana_quiz1(self):
        pass

    def create_katakana_quiz2(self):
        pass
