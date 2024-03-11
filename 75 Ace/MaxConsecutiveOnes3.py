class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left pointer and result variable
        left = 0
        res = 0

        # iterate through the array using a sliding window technique
        for right, n in enumerate(nums):
            # decrement k by 1 if the current element is 0 (1-n)
            k -= (1-n)
            # if k becomes negative, increment k by 1 if the left pointer element is 0
            # and move the left pointer to the right
            if k < 0:
                k += (1 - nums[left])
                left += 1
            # update the result with the maximum length of the current substring
            res = max(res, right - left + 1)
        
        # return the maximum length of substring with at most k zeros
        return res
