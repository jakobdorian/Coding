class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # add a zero at the end to handle the case when reaching the top of the stairs.
        cost.append(0)

        # traverse the list backwards to find the minimum cost for each step.
        for i in range(len(cost) - 3, -1, -1):
            # at each step, update the cost to reach that step by adding the minimum cost of
            # taking one or two steps from the current step.
            cost[i] += min(cost[i + 1], cost[i + 2])

        # return the minimum cost of reaching the top, considering starting from either the
        # first or the second step.
        return min(cost[0], cost[1])
