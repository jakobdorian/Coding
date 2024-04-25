class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # iterate through houses
        for n in nums:
            # calc the max amount that can be robbed from current house
            temp = max(n + rob1, rob2)
            # update variables
            rob1 = rob2
            rob2 = temp
        # return max amount
        return rob2
