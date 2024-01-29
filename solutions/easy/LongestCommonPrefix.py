from typing import List

class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result
        for length in range(1, len(strs[0])+1):
            if self.all_startwith_prieix(strs, strs[0][:length]):
                result = strs[0][:length]
        return result

    def all_startwith_prieix(self, list, prefix):
        return all(string.startswith(prefix) for string in list)