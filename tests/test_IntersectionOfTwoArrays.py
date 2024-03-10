import unittest
from typing import List
from solutions.easy.IntersectionOfTwoArrays import IntersectionOfTwoArrays


class TestIntersectionOfTwoArrays(unittest.TestCase):

    def setUp(self):
        self.intersect_obj = IntersectionOfTwoArrays()

    def test_intersection_empty(self):
        self.assertEqual(self.intersect_obj.intersection([], []), [])

    def test_intersection_single_element(self):
        self.assertEqual(self.intersect_obj.intersection([1], [1]), [1])

    def test_intersection_no_intersection(self):
        self.assertEqual(self.intersect_obj.intersection([1, 2, 3], [4, 5, 6]), [])

    def test_intersection_multiple_occurrences(self):
        self.assertEqual(self.intersect_obj.intersection([1, 2, 2, 3], [2, 2, 3, 4]), [2, 3])

    def test_intersection_generic_case(self):
        self.assertEqual(self.intersect_obj.intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])


if __name__ == "__main__":
    unittest.main()
