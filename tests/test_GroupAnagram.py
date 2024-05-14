import unittest
from typing import List
from solutions.medium.GroupAnagram import GroupAnagram


class TestGroupAnagram(unittest.TestCase):

    def test_group_anagrams(self):
        group_anagram = GroupAnagram()

        test_case1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(group_anagram.groupAnagrams(test_case1), expected_output1)

        test_case2 = [""]
        expected_output2 = [[""]]
        self.assertEqual(group_anagram.groupAnagrams(test_case2), expected_output2)

        test_case3 = ["a"]
        expected_output3 = [["a"]]
        self.assertEqual(group_anagram.groupAnagrams(test_case3), expected_output3)


if __name__ == "__main__":
    unittest.main()
