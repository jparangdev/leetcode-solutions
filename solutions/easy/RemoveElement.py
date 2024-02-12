class RemoveElement:
    def removeElement(self, nums, val):
        while val not in nums:
            nums.remove(val)
        return len(nums)