# O(n) sol
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        # compare each character of s and t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False
            