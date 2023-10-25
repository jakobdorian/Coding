# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# O(1) solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result array
        res = [1] * (len(nums))
        pre, post = 1, 1
        # add prefixs to result array
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        # go through the array backwards
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= post
            post *= nums[i]
        return res
