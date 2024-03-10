from typing import List


class IntersectionOfTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i in nums1 :
            if i not in dict:
                dict[i] = 1
        for i in nums2 :
            if i in dict:
                dict[i] += 1
        return [key for key, value in dict.items() if value > 1]

