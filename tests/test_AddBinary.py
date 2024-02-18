import unittest
from solutions.easy.AddBinary import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_addBinary(self):
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")
        self.assertEqual(self.solution.addBinary("0", "0"), "0")
        self.assertEqual(self.solution.addBinary("1", "1"), "10")
        self.assertEqual(self.solution.addBinary("1111", "1"), "10000")


if __name__ == '__main__':
    unittest.main()
