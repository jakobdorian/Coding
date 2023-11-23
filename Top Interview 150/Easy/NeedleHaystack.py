class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                # not a match
                if haystack[i + j] != needle[j]:
                    break
                # match found
                if j == len(needle) - 1:
                    return i
        # needle is not in haystack
        return -1