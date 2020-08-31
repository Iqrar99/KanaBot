class JLetters(object):
    """
    A class to provide Kana (Japanese letters).
    """

    HIRAGANA_LETTERS = {
        "vowel": "あいうえお",
        "k": "かきくけこ",
        "g": "がぎぐげご",
        "s": "さしすせそ",
        "z": "ざじずぜぞ",
        "t": "たちつてと",
        "d": "だぢづでど",
        "n": "なにぬねの",
        "h": "はひふへほ",
        "b": "ばびぶべぼ",
        "p": "ぱぴぷぺぽ",
        "m": "まみむめも",
        "y": "やいゆえよ",  # It's actually only やゆよ
        "r": "らりるれろ",
        "w": "わいうえを",  # It's actually only わを
        "nn": "ん"
    }
    KATAKANA_LETTERS = {
        "vowel": "アイウエオ",
        "k": "カキクケコ",
        "g": "ガギグゲゴ",
        "s": "サシスセソ",
        "z": "ザジズゼゾ",
        "t": "タチツテト",
        "d": "ダヂヅデド",
        "n": "ナニヌネノ",
        "h": "ハヒフヘホ",
        "b": "バビブベボ",
        "p": "パピプペポ",
        "m": "マミムメモ",
        "y": "ヤイユエヨ",  # It's actually only ヤユヨ
        "r": "ラリルレロ",
        "w": "ワイウエヲ",  # It's actually only ワヲ
        "nn": "ン"
    }
    vowel = "aiueo"
    japanese_consonant = "kgsztdnhbpmyrwn" 

    def _get_char_by_vowel(self, letters: str, vowel: str):
        """
        This function will grab a specific letter based on the vowel.
        
        Parameters
        ----------
        letters : str
            Some letters that need to be picked one of them.
        vowel : str
            Vowel target.

        Returns
        -------
        str
            The Japanese letter user wants.
        """

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
        This function will get a Japanese character based on romaji.
        
        Parameters
        ----------
        romaji : str
            A string that written in alphabet.
        kana_type : {"HIRAGANA", "KATAKANA"}, default "HIRAGANA"
            Kana type to specify what letter user wants.

        Returns
        -------
        str
            The Japanese letter user wants.
        """

        if romaji == "":
            raise Exception("Can not accept empty string.")

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
            elif romaji == "n":
                return letters["nn"]
            else:
                raise Exception("Letter can not be found. Please type your romaji correctly.")
        
        elif len(romaji) == 2:
            if romaji == "nn":
                return letters[romaji]

            consonant = romaji[0]
            vowel = romaji[1]
            if consonant in self.vowel:
                raise Exception("First character should be consonant.")
            elif consonant not in self.japanese_consonant:
                raise Exception("The consonant is not used in Kana.")
            else:
                return self._get_char_by_vowel(letters[consonant], vowel)

        elif len(romaji) == 3:  # will handle special cases like  shi, chi, and tsu
            three_chars_romaji = {
                "shi": self._get_char_by_vowel(letters["s"], "i"),
                "chi": self._get_char_by_vowel(letters["t"], "i"),
                "tsu": self._get_char_by_vowel(letters["t"], "u")
            }

            if romaji in three_chars_romaji:
                return three_chars_romaji[romaji]
            else:
                return Exception("Unrecognized romaji. Please type romaji correctly.")

        else:
            raise Exception("Romaji for one Japanese letter should not exceed three chars.")



# For testing purpose
if __name__ == "__main__":
    jletters = JLetters()
    print(jletters.get_jletter("a"))  # will prints あ
    print(jletters.get_jletter("ka"))  # will prints か
    print(jletters.get_jletter("tsu", "KATAKANA"))  # will prints ツ
    print(jletters.get_jletter("tu", "KATAKANA"))  # will prints ツ

