class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # left pointer to track non-zero elements
        left = 0
        
        # iterate through the array with the right pointer
        for right in range(len(nums)):
            # if the element at the right pointer is non-zero
            if nums[right]:
                # swap the non-zero element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                # move the left pointer to the next position
                left += 1
        
        # return the modified array with non-zero elements moved to the front
        return nums
