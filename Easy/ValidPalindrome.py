class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for ch in s:
            # is the current char alphanumeric?
            if ch.isalnum():
                # add it to result
                res += ch.lower()
        return res == res[::-1]
