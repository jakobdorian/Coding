class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Create a counter to keep track of the occurrences of each number in the list
        count = Counter(nums)
        res = 0 

        # loop through a range of numbers from 0 to the sum of the length of nums and the maximum number in nums
        for i in range(0, len(nums) + max(nums)):
             # if the current number appears more than once, calc extra occurences
            if count[i] > 1: 
                extra = count[i] - 1
                # move the extra occurrences to the next number
                count[i+1] += extra  
                # add the extra occurrences to the result count
                res += extra 

        return res
