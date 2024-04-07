class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for j in t:
            if j not in map:
                return False
            else:
                map[j] -= 1
        for val in map.values():
            if val != 0:
                return False
        return True

    # best solution
    # sorted_s = sorted(s)
    # sorted_t = sorted(t)
    # return sorted_s == sorted_t
