class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""       # store the longest palindrome found so far
        resLen = 0     # store the length of the longest palindrome found so far

        # O(n^2)
        for i in range(len(s)):
            left, right = i, i
            # expand around the current character (odd length palindrome)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            # expand around the gap between the current and the next character (even length palindrome)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return res
