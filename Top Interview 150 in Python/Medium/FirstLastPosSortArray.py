class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the leftmost and rightmost occurrences of the target using binary search
        left = self.binary(nums, target, True)
        right = self.binary(nums, target, False)
        # return the result as a list [leftmost, rightmost]
        return [left, right]

    def binary(self, nums, target, leftBias):
        # binary search function to find leftmost or rightmost occurrence
        # leftBias: True for leftmost, False for rightmost
        left, right = 0, len(nums) - 1
        res = -1  # initialize result to -1, indicating target not found
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                # target found, update result and adjust search range based on leftBias
                res = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return res

# Time complexity: O(log n) - Binary search is used to find leftmost and rightmost occurrences.
# Space complexity: O(1) - Constant space is used for variables.
