import unittest
from typing import List
from solutions.easy.MinimumCommonValue import MinimumCommonValue


class TestMinimumCommonValue(unittest.TestCase):

    def setUp(self):
        self.mini_com_value = MinimumCommonValue()

    def test_get_common_when_common_values_exist(self):
        self.assertEqual(self.mini_com_value.getCommon([1, 2, 3, 4, 5], [2, 3, 6, 5, 7]), 2)

    def test_get_common_when_no_common_values_exist(self):
        self.assertEqual(self.mini_com_value.getCommon([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]),-1)

    def test_get_common_with_negative_integers(self):
        self.assertEqual(self.mini_com_value.getCommon([-1, -2, -3, -4, -5], [-2, -6, -5, -7, -8]), -5)

    def test_get_common_with_empty_lists(self):
        self.assertEqual(self.mini_com_value.getCommon([], []),-1)


if __name__ == "__main__":
    unittest.main()
