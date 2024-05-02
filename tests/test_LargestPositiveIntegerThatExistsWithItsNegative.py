import unittest
from solutions.easy.LargestPositiveIntegerThatExistsWithItsNegative import LargestPositiveIntegerThatExistsWithItsNegative

class TestFindMaxK(unittest.TestCase):
    
    def setUp(self):
        self.largest_positive_integer = LargestPositiveIntegerThatExistsWithItsNegative()
    
    def test_empty_list(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([]), -1)
        
    def test_all_positive_number(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([1, 2, 3, 4, 5]), -1)
        
    def test_all_negative_number(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([-1, -2, -3, -4, -5]), -1)
        
    def test_matching_positive_and_negative(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([-1, -2, -3, 1, 2, 3]), 3)

    def test_no_matching_positive_and_negative(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([-1, -2, -3, 4, 5, 6]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(self.largest_positive_integer.findMaxK([-1, 2, -3, 1, -2, 3]), 3)
        
if __name__ == '__main__':
    unittest.main()