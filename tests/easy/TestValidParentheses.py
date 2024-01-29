import unittest

from solutions.easy.ValidParentheses import ValidParentheses


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.instance = ValidParentheses()

    def test(self):
        cases = [
            ("()", True),
            ("(){}[]", True),
            ("(]", False),
            ("]", False),
            ("){", False)
            # Add more test cases if needed
        ]
        for case, expected in cases:
            with self.subTest(case=case):
                self.assertEqual(self.instance.isValid(case), expected)

