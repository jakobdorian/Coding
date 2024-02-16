class Solution:
    def rob(self, nums: List[int]) -> int:
        # variables to track the maximum amount robbed in two consecutive houses
        rob1, rob2 = 0, 0
        
        # iterate through the list of house values
        for n in nums:
            # calculate the maximum amount that can be robbed considering the current house and the amount robbed in the previous two houses
            temp = max(n + rob1, rob2)
            # update the variables to track the amount robbed in the previous two houses
            rob1 = rob2
            rob2 = temp
        # return the maximum amount that can be robbed
        return rob2
