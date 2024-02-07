import unittest

from solutions.easy.RemoveDuplicatesfromSortedArray import removeDuplicatesfromSortedArray


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.remover = removeDuplicatesfromSortedArray()

    def test_duplicates_removed(self):
        nums = [1, 1, 2]
        expected_length = 2
        self.assertEqual(self.remover.removeDuplicates(nums), expected_length)

        nums = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4]
        expected_length = 5
        self.assertEqual(self.remover.removeDuplicates(nums), expected_length)


if __name__ == '__main__':
    unittest.main()