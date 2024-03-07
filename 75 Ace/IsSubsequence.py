class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # pointers for both strings s and t
        i = 0
        j = 0
        
        # iterate through each character of s and t simultaneously
        while i < len(s) and j < len(t):
            # if characters at current positions match, move pointer for s to next position
            if s[i] == t[j]:
                i += 1
            # move pointer for t to next position regardless
            j += 1
        
        # if all characters of s are found in t in the same order, return True
        if i == len(s):
            return True
        # otherwise, return False
        else:
            return False
