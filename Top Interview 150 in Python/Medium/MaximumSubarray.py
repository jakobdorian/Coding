class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize variables to store the maximum subarray sum and current subarray sum.
        res = float('-inf')  
        curr = 0 
        for n in nums:
            # update current subarray sum by choosing either to continue with the existing subarray or start a new one.
            curr = max(curr + n, n)
            # update the maximum subarray sum by comparing with the current subarray sum.
            res = max(res, curr)
        # return the maximum subarray sum.
        return res
        