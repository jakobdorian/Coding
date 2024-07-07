class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # iterate through each word in the list 'words'
        for w in words:
            # check if the word is a palindrome by comparing it to its reverse
            if w == w[::-1]:
                # if a palindrome is found, return the word
                return w
        # if no palindromes are found in the list, return an empty string
        return ""
