class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # dictionary to store vowels for efficient lookup
        vowel = {'a', 'e', 'i', 'o', 'u'}

        left = 0  # left pointer for the sliding window
        count = 0  # counter for vowels in the current window
        res = 0  # result variable to store the maximum count of vowels

        # iterate over the string using a sliding window approach
        for right in range(len(s)):
            # increment count if the current character is a vowel
            count += 1 if s[right] in vowel else 0
            # if the window size exceeds k, move the left pointer and update the count
            if right - left + 1 > k:
                count -= 1 if s[left] in vowel else 0 
                left += 1
            # update the result with the maximum count of vowels encountered
            res = max(res, count)
            
        return res  # return the maximum count of vowels within any contiguous substring of length k
