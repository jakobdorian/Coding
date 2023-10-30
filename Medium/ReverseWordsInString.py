class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string, reverse the string, then join them back up with a space
        return " ".join(reversed(s.split()))
        