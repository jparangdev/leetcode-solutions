import unittest

from solutions.easy.LongestCommonPrefix import LongestCommonPrefix


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.instance = LongestCommonPrefix()

    def test(self):
        cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["a"], "a"),
        ]
        for case, expected in cases:
            with self.subTest(case=case):
                self.assertEqual(self.instance.longestCommonPrefix(case), expected)
