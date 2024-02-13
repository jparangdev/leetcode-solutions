from typing import List

class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid_index = start + (end - start) // 2
            if nums[mid_index] < target:
                start = mid_index + 1
            elif nums[mid_index] > target:
                end = mid_index
            else:
                return mid_index
        return start
