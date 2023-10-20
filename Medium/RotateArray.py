# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1) solution
        k = k % len(nums)
        p1 = 0
        p2 = len(nums) - 1
        # reverse array
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 = p1 + 1
            p2 = p2 - 1
        # reverse the 1st k elements
        p1 = 0
        p2 = k - 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 = p1 + 1
            p2 = p2 - 1
        # reverse the remaining portion of array
        p1 = k
        p2 = len(nums) - 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 = p1 + 1
            p2 = p2 - 1