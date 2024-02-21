import unittest

from solutions.easy.SqrtX import SqrtX

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = SqrtX()

    def test_mySqrt(self):
        self.assertEqual(self.solution.mySqrt(4), 2)
        self.assertEqual(self.solution.mySqrt(8), 2)
        self.assertEqual(self.solution.mySqrt(16), 4)
        self.assertEqual(self.solution.mySqrt(0), 0)
        self.assertEqual(self.solution.mySqrt(1), 1)
        self.assertEqual(self.solution.mySqrt(2), 1)


if __name__ == "__main__":
    unittest.main()
