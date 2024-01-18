class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <= 2:
            return n
        # variables to store the previous two results
        p1 = 1
        p2 = 2
        res = 0
        # calculate the number of ways to climb to the current step
        for i in range(2, n):
            res = p1 + p2
            p1 = p2
            p2 = res
        # return the result for climbing n steps
        return res
        