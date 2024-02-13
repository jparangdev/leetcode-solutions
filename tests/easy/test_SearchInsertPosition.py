import unittest
from solutions.easy.SearchInsertPosition import SearchInsertPosition


class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.sip = SearchInsertPosition()

    def test_search_insert_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected_result = 2
        result = self.sip.searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_search_insert_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected_result = 1
        result = self.sip.searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_search_insert_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected_result = 4
        result = self.sip.searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_search_insert_4(self):
        nums = [1, 3, 5, 6]
        target = 0
        expected_result = 0
        result = self.sip.searchInsert(nums, target)
        self.assertEqual(result, expected_result)

    def test_search_insert_5(self):
        nums = [1]
        target = 0
        expected_result = 0
        result = self.sip.searchInsert(nums, target)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
