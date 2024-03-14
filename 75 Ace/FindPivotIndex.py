class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total sum of all elements in the given list
        total = sum(nums)
        # initialize the left sum as 0
        left = 0
        
        # iterate through each element in the list
        for i in range(len(nums)):
            # calculate the right sum as the total sum minus the current element and the left sum
            right = total - nums[i] - left
            
            # check if the left sum is equal to the right sum
            if left == right:
                # if so, return the current index as the pivot index
                return i
            
            # increment the left sum by the current element
            left += nums[i]
        
        # if no pivot index is found, return -1
        return -1
