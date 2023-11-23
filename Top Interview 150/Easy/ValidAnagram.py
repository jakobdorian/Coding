class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        # hashmaps to count the chars in both strings
        countS, countT = {}, {}
        # build hashmap
        for i in range(len(s)):
            # count the number of times a certain char is seen
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # iterate through hashmaps
        for ch in countS:
            if countS[ch] != countT.get(ch, 0):
                return False
        return True
        