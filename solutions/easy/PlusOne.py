from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            sum += digits[i] * 10 ** (len(digits) - i - 1)
        return [int(digit) for digit in str(sum + 1)]
