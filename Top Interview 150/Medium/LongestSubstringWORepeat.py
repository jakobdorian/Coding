class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        p1 = 0
        res = 0
        for p2 in range(len(s)):
            # is the curr char a dulp?
            while s[p2] in charSet:
                charSet.remove(s[p1])
                # slide window
                p1 += 1
            charSet.add(s[p2])
            res = max(res, p2 - p1 + 1)
        return res
        