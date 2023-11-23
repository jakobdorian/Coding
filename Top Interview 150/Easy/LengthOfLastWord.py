class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = len(s) - 1
        res = 0
        # get rid of white spaces, decrement pointer
        while s[temp] == ' ':
            temp -= 1
        # count the length of the current word
        while temp >= 0 and s[temp] != ' ':
            res += 1
            temp -= 1
        return res
