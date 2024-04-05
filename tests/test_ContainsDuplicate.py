import unittest
from solutions.easy.ContainsDuplicate import ContainsDuplicate


class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        self.containsDuplicate = ContainsDuplicate()

    def test_containsDuplicate_with_duplicates(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(self.containsDuplicate.containsDuplicate(nums))

    def test_containsDuplicate_without_duplicates(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.containsDuplicate.containsDuplicate(nums))

    def test_containsDuplicate_with_empty_input(self):
        nums = []
        self.assertFalse(self.containsDuplicate.containsDuplicate(nums))


if __name__ == '__main__':
    unittest.main()
