import unittest
from solutions.easy.ValidPalindrome import ValidPalindrome


class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.validPalindrome = ValidPalindrome()

    def tearDown(self):
        del self.validPalindrome

    def test_isPalindrome_lowercase(self):
        result = self.validPalindrome.isPalindrome("madam")
        self.assertEqual(result, True)

    def test_isPalindrome_uppercase(self):
        result = self.validPalindrome.isPalindrome("MADAM")
        self.assertEqual(result, True)

    def test_isPalindrome_mixedcase(self):
        result = self.validPalindrome.isPalindrome("MadAm")
        self.assertEqual(result, True)

    def test_isPalindrome_nonalpha(self):
        result = self.validPalindrome.isPalindrome("m#ad2a--m")
        self.assertEqual(result, False  )

    def test_isPalindrome_notpalindrome(self):
        result = self.validPalindrome.isPalindrome("hello")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
