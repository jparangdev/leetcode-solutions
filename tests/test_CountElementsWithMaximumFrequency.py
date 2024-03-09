import unittest
from typing import List
from solutions.easy.CountElementsWithMaximumFrequency import CountElementsWithMaximumFrequency


class TestCountElementsWithMaximumFrequency(unittest.TestCase):
    def setUp(self):
        self.sol = CountElementsWithMaximumFrequency()

    def test_max_frequency_number(self):
        self.assertEqual(self.sol.maxFrequencyElements([1,2,2,3,1,4]), 4)

    def test_max_frequency_number_same_count(self):
        self.assertEqual(self.sol.maxFrequencyElements([1, 1, 2, 2]), 4)

    def test_max_frequency_single_element(self):
        self.assertEqual(self.sol.maxFrequencyElements([5]), 1)

    def test_max_frequency_number_negative(self):
        self.assertEqual(self.sol.maxFrequencyElements([-1, -1, -2, -2, -2, -3, -3, -3]), 6)


if __name__ == "__main__":
    unittest.main()
