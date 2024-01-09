class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # appending infinity to ensure that target can be greater than any element in nums
        nums.append(float('inf'))
        # initializing pointers for binary search
        left, right = 0, len(nums) - 1
        # binary search loop
        while(left < right):
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        # the final 'left' position is the insertion point of the target
        return left
        