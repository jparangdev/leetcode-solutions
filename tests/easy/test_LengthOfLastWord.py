import unittest

# Assuming that LengthOfLastWord.py is placed in the solutions/easy directory.
from solutions.easy.LengthOfLastWord import LengthOfLastWord


class TestLengthOfLastWord(unittest.TestCase):

    def setUp(self):
        self.instance = LengthOfLastWord()

    def test_length_of_last_word_with_single_word(self):
        self.assertEqual(self.instance.lengthOfLastWord("Hello"), 5)

    def test_length_of_last_word_with_multiple_words(self):
        self.assertEqual(self.instance.lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_length_of_last_word_with_spaces_at_the_end(self):
        self.assertEqual(self.instance.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_length_of_last_word_with_empty_string(self):
        self.assertEqual(self.instance.lengthOfLastWord(""), 0)


if __name__ == "__main__":
    unittest.main()
