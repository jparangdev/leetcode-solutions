import unittest

from solutions.easy.LomanToInteger import LomanToInteger


class TestLomanToInteger(unittest.TestCase):
    def setUp(self):
        self.instance = LomanToInteger()

    def test(self):
        cases = [
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            # Add more test cases if needed
        ]
        for case, expected in cases:
            with self.subTest(case=case):
                self.assertEqual(self.instance.romanToInt(case), expected)

