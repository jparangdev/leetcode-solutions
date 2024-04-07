import unittest
from solutions.easy.ValidAnagram import ValidAnagram


class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.validator = ValidAnagram()

    def test_isAnagram_same_chars_different_order(self):
        self.assertTrue(self.validator.isAnagram("anagram", "nagaram"))

    def test_isAnagram_same_chars_same_order(self):
        self.assertTrue(self.validator.isAnagram("python", "python"))

    def test_isAnagram_different_chars(self):
        self.assertFalse(self.validator.isAnagram("hello", "world"))

    def test_isAnagram_empty_strings(self):
        self.assertTrue(self.validator.isAnagram("", ""))

    def test_isAnagram_one_empty_string(self):
        self.assertFalse(self.validator.isAnagram("", "nonempty"))

    def test_isAnagram_case_sensitive_identical(self):
        self.assertTrue(self.validator.isAnagram("Python", "Python"))

    def test_isAnagram_case_sensitive_not_identical(self):
        self.assertFalse(self.validator.isAnagram("Python", "python"))

    def test_isAnagram_with_numbers(self):
        self.assertTrue(self.validator.isAnagram("123", "321"))

    def test_isAnagram_special_chars(self):
        self.assertTrue(self.validator.isAnagram("!@#", "#!@"))


if __name__ == '__main__':
    unittest.main()
