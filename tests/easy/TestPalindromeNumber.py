import unittest

from solutions.easy.PalindromeNumber import PalindromeNumber


class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.instance = PalindromeNumber()

    def test(self):
        cases = [
            (121, True),
            (-121, False),
            (10, False),
            # Add more test cases if needed
        ]
        for case, expected in cases:
            with self.subTest(case=case):
                self.assertEqual(self.instance.isPalindrome(case), expected)

