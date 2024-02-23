import unittest
from solutions.easy.ClimbingStairs import ClimbingStairs


class TestClimbStairs(unittest.TestCase):

    def setUp(self):
        self.climber = ClimbingStairs()

    def test_climbStairs_1(self):
        self.assertEqual(self.climber.climbStairs(1), 1)

    def test_climbStairs_2(self):
        self.assertEqual(self.climber.climbStairs(2), 2)

    def test_climbStairs_3(self):
        self.assertEqual(self.climber.climbStairs(3), 3)

    def test_climbStairs_4(self):
        self.assertEqual(self.climber.climbStairs(4), 5)

    def test_climbStairs_5(self):
        self.assertEqual(self.climber.climbStairs(5), 8)


if __name__ == '__main__':
    unittest.main()
