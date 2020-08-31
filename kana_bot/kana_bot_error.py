class ConsonantError(Exception):
    """Raises when users violate consonant when calling function."""

    pass


class EmptyRomajiError(Exception):
    """Raises when user input an empty string for romaji variable."""

    pass


class KanaTypeError(Exception):
    """Raises when Kana type is not one of HIRAGANA and KATAKANA."""

    pass


class LetterNotFoundError(Exception):
    """Raises when there is no Japanase letter with user-typed romaji."""

    pass


class RomajiLengthError(Exception):
    """Raises when input is more than three characters."""

    pass