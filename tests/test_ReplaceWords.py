import unittest
from solutions.medium.ReplaceWords import ReplaceWords


class ReplaceWordsTest(unittest.TestCase):
    def setUp(self):
        self.replaceWords = ReplaceWords()

    def test_replaceWords_1(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        result = "the cat was rat by the bat"
        self.assertEqual(result, self.replaceWords.replaceWords(dictionary, sentence))

    def test_replaceWords_2(self):
        dictionary = ["a", "b", "c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        result = "a a b c"
        self.assertEqual(result, self.replaceWords.replaceWords(dictionary, sentence))

    def test_replaceWords_3(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aa"
        result = "a a a a a a"
        self.assertEqual(result, self.replaceWords.replaceWords(dictionary, sentence))

    def test_replaceWords_4(self):
        dictionary = ["cat", "catt", "catting"]
        sentence = "the cattings were going on"
        result = "the cat were going on"
        self.assertEqual(result, self.replaceWords.replaceWords(dictionary, sentence))

    def test_replaceWords_5(self):
        dictionary = ["c", "cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        result = "the c was rat by the bat"
        self.assertEqual(result, self.replaceWords.replaceWords(dictionary, sentence))


if __name__ == '__main__':
    unittest.main()