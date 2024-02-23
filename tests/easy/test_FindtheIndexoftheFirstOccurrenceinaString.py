import unittest
from solutions.easy.FindtheIndexoftheFirstOccurrenceinaString import FindtheIndexoftheFirstOccurrenceinaString


class TestFindtheIndexoftheFirstOccurrenceinaString(unittest.TestCase):
    def setUp(self):
        self.find_index = FindtheIndexoftheFirstOccurrenceinaString()

    def test_strStr_empty_needle(self):
        self.assertEqual(self.find_index.strStr("sadbutsad", "sad"), 0)

    def test_strStr_needle_in_haystack(self):
        self.assertEqual(self.find_index.strStr("hello", "ll"), 2)

    def test_strStr_needle_not_in_haystack(self):
        self.assertEqual(self.find_index.strStr("leetcode", "leeto"), -1)

    def test_strStr_haystack_and_needle_are_empty(self):
        self.assertEqual(self.find_index.strStr("", ""), 0)


if __name__ == '__main__':
    unittest.main()
