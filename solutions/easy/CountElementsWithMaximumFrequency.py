from typing import List


class CountElementsWithMaximumFrequency:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        max_frequency = max(num_counts.values())
        max_frequency_elements = [num for num, count in num_counts.items() if count == max_frequency]

        return len(max_frequency_elements) * max_frequency
