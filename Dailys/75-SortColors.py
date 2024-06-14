class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1  
        i = 0  

        # helper function to swap elements at index i and j
        def helper(i, j):
            temp = nums[i]  
            nums[i] = nums[j] 
            nums[j] = temp  

        # iterate through the list until the current index pointer passes the right boundary
        while i <= right:
            if nums[i] == 0:  
                helper(left, i) 
                left += 1  

            elif nums[i] == 2:  
                helper(i, right)  
                right -= 1
                # decrement the current index to re-evaluate the swapped element
                i -= 1

            # move the current index pointer one step to the right
            i += 1
            