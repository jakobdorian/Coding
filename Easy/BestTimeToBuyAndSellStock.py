# O(n) solution as we only scan the array once with two pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers: p1 for buying and p2 for selling
        p1 = 0
        p2 = 1
        # maximum profit
        res = 0
        
        while p2 < len(prices):
            # profitable transaction
            if prices[p1] < prices[p2]:
                profit = prices[p2] - prices[p1]
                res = max(res, profit)
            # not a profitable transaction
            else:
                p1 = p2
            p2 += 1
        return res