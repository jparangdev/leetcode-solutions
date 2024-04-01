from typing import Optional, List


class AssignCookies:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        for i in g:
            for j in s:
                if i <= j:
                    result = result+1
                    s.remove(j)
                    break
        return result




        
