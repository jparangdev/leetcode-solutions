import unittest

from solutions.TwoSum import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.instance = TwoSum()

    def test_two_sum(self):
        cases = [
            ({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
            ({"nums": [3, 2, 4], "target": 6}, [1, 2]),
            ({"nums": [3, 3], "target": 6}, [0, 1]),
            # Add more test cases if needed
        ]
        for case, expected in cases:
            with self.subTest(case=case):
                self.assertEqual(self.instance.twoSum(**case), expected)

