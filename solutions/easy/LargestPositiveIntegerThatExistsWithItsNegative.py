from typing import List


class LargestPositiveIntegerThatExistsWithItsNegative:
    def findMaxK(self, nums: List[int]) -> int:
        result = -1
        nums.sort()
        if len(nums) == 0:
            return result
        if nums[-1] < 0:
            return result

        dic = {}
        for num in nums:
            if num <= 0:
                dic[num*-1] = num
            else:
                if num in dic:
                    if result < num:
                        result = num
        return result

