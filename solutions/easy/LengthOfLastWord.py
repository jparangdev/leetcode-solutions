class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        array = s.split()
        return len(array[-1])
