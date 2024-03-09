from typing import List


class MinimumCommonValue:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        dup = set1 & set2
        if not dup:
            return -1
        return min(dup)