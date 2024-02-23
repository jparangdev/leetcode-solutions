# file: test_PlusOne.py
import unittest
from solutions.easy.PlusOne import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plus_one_single_digit(self):
        self.assertEqual(self.solution.plusOne([1]), [2])
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_plus_one_multiple_digits(self):
        self.assertEqual(self.solution.plusOne([1, 0]), [1, 1])
        self.assertEqual(self.solution.plusOne([9, 9]), [1, 0, 0])
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_plus_one_edge_cases(self):
        self.assertEqual(self.solution.plusOne([0]), [1])
        self.assertEqual(self.solution.plusOne([1, 0, 0, 0, 0, 0, 0, 0, 9]), [1, 0, 0, 0, 0, 0, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
