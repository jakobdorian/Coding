class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            # use bitwise XOR operation to find the single number
            res = n ^ res
        return res
        