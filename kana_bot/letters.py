class JLetters(object):
    """
    A class to provide Kana (Japanese letters).
    """

    # TODO : Add diacritics
    HIRAGANA_LETTERS = {
        "vowel": "あいうえお",
        "k": "かきくけこ",
        "s": "さしすせそ",
        "t": "たちつてと",
        "n": "なにぬねの",
        "h": "はひふへほ",
        "m": "まみむめも",
        "y": "やいゆえよ",  # It's actually only やゆよ
        "r": "らりるれろ",
        "w": "わいうえを",  # It's actually only わを
        "nn": "ん"
    }
    KATAKANA_LETTERS = {
        "vowel": "アイウエオ",
        "k": "カキクケコ",
        "s": "サシスセソ",
        "t": "タチツテト",
        "n": "ナニヌネノ",
        "h": "ハヒフヘホ",
        "m": "マミムメモ",
        "y": "ヤイユエヨ",  # It's actually only ヤユヨ
        "r": "ラリルレロ",
        "w": "ワイウエヲ",  # It's actually only ワヲ
        "nn": "ン"
    }
    vowel = "aiueo"
    japanese_consonant = "kstnhmyrwn"  # TODO : Add other consonant 

    def _get_char_by_vowel(self, letters: str, vowel: str):
        idx = {
            "a": 0,
            "i": 1,
            "u": 2,
            "e": 3,
            "o": 4
        }

        return letters[idx[vowel]]


    def get_jletter(self, romaji: str, kana_type="HIRAGANA") -> str:
        """
        This function will get the Japanese characters based on romaji.
        
        Parameters
        ----------
        romaji : str
            A string that written in alphabet.
        kana_type : {"HIRAGANA", "KATAKANA"}, default "HIRAGANA"
            Kana type to specify what letter user wants.

        Returns
        -------
        str
            The letter user wants.
        """

        letters: dict
        if kana_type == "HIRAGANA":
            letters = self.HIRAGANA_LETTERS
        elif kana_type == "KATAKANA":
            letters = self.KATAKANA_LETTERS
        else:
            raise Exception("Unrecognized `kana_type`. Should be only 'HIRAGANA' or 'KATAKANA'.")

        if len(romaji) == 1:
            if romaji in self.vowel:
                return self._get_char_by_vowel(letters["vowel"], romaji)
        
        # TODO
        return None


# For testing purpose
if __name__ == "__main__":
    jletters = JLetters()
    print(jletters.get_jletter("a"))  # will prints あ
    print(jletters.get_jletter("a", "TEST"))  # will raises an error
