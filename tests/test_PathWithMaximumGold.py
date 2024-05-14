import unittest
from typing import List
from solutions.medium.PathWithMaximumGold import PathWithMaximumGold


class TestPathWithMaximumGold(unittest.TestCase):
    def setUp(self):
        self.obj = PathWithMaximumGold()

    def test_getMaximumGold_empty_grid(self):
        grid = [[]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 0)

    def test_getMaximumGold_single_cell_grid(self):
        grid = [[5]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 5)

    def test_getMaximumGold_single_row_multiple_cells(self):
        grid = [[1, 0, 7, 0, 0]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 7)

    def test_getMaximumGold_single_column_multiple_rows(self):
        grid = [[3], [0], [8], [2]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 10)

    def test_getMaximumGold_multiple_rows_columns_with_zero_cells(self):
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 24)

    def test_getMaximumGold_multiple_rows_columns_case_1(self):
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        result = self.obj.getMaximumGold(grid)
        self.assertEqual(result, 28)


if __name__ == '__main__':
    unittest.main()
