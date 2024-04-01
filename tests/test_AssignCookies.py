import unittest
from solutions.easy.AssignCookies import AssignCookies


class TestAssignCookies(unittest.TestCase):
    def setUp(self):
        self.sol = AssignCookies()

    def test_find_content_children(self):
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], [1, 1]), 1)
        self.assertEqual(self.sol.findContentChildren([1, 2], [1, 2, 3]), 2)
        self.assertEqual(self.sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]), 2)
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], []), 0)
        self.assertEqual(self.sol.findContentChildren([], [1, 2, 3]), 0)

    def tearDown(self):
        self.sol = None


if __name__ == '__main__':
    unittest.main()
