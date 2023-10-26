# greedy problem O(n) time complexity, O(1) space complexity
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # does a solution exist?
        if sum(gas) < sum(cost):
            return -1
        
        total, res = 0, 0
        # iterate through array
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            # postion doesnt work
            if total < 0:
                # reset total
                total = 0
                res = i + 1
        return res