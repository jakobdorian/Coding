class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # variables to store global and current maximum and minimum sums
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        # iterate through the array to find maximum and minimum sums
        for n in nums:
            # update current maximum and minimum sums
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            # update total sum
            total += n
            # update global maximum and minimum sums
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        # check if the global maximum sum is greater than 0
        if globalMax > 0:
            # return the maximum of either the global maximum sum or the difference between
            # total sum and global minimum sum
            return max(globalMax, total - globalMin)
        else:
            # if global maximum sum is non-positive, return the global maximum sum
            return globalMax
            