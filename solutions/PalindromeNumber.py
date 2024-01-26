class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_num = str(x)
        reversed_str_num = str_num[::-1]
        return str_num == reversed_str_num
