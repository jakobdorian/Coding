class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            # use bitwise xor operation to find single num
            res = n ^ res
        return res
        