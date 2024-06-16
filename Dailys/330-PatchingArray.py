class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # pointer and counters
        i, res, upto = 0, 0, 0
        N = len(nums)
        
        # continue until we can form all numbers up to n
        while upto < n:
            # if the current number in nums is within the range of numbers we can form
            # (upto + 1), use it to extend the range
            if i < N and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                # if the current number in nums is not within the range,
                # add a patch (which is upto + 1) to extend the range
                res += 1
                upto += (upto + 1)
                
        # return the total number of patches added
        return res
