from typing import List


class GroupAnagram:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            key = tuple(sorted(str))
            if key in map:
                map[key].append(str)
            else:
                map[key] = [str]
        return list(map.values())