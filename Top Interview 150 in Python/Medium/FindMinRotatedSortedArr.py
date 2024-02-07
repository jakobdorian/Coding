class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left pointer to the start of the list and right pointer to the end of the list
        left, right = 0, len(nums) - 1

        # binary search loop
        while left < right:
            # calculate the middle index
            mid = (left + right) // 2
            # if the value at the middle index is greater than the value at the right pointer,
            # the minimum element must be in the right half of the list.
            if nums[mid] > nums[right]:
                left = mid + 1
            # otherwise, the minimum element must be in the left half of the list.
            else:
                right = mid
        # when the loop breaks, left and right pointers will converge to the minimum element.
        # return the value at the left pointer, which is the minimum element.
        return nums[left]

# Time complexity: O(log n) - Binary search halves the search space in each iteration.
# Space complexity: O(1) - Constant space, no extra data structures are used.
