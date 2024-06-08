class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        
        # variable to keep running sum of elements in nums
        total = 0

        # iterate through the list with both index (i) and element (n)
        for i, n in enumerate(nums):
            # update the running total
            total += n
            # compute the remainder of the total divided by k
            r = total % k
            
            # if the remainder has not been seen before, store the index
            if r not in remainder:
                remainder[r] = i
            # if the remainder has been seen before and the subarray length is at least 2
            elif i - remainder[r] > 1:
                # A valid subarray is found, return True
                return True
                
        # if no valid subarray is found, return False
        return False
