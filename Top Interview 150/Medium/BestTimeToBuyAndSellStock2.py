# this is a classic sliding window problem
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit
        res = 0
        # a single pointer to scan array, skip the first element
        for i in range(1, len(prices)):
            # if the price at the current index is > then previous = profit
            if prices[i] > prices[i - 1]:
                res += (prices[i] - prices[i - 1])
        return res