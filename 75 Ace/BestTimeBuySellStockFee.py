class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # profit and position variables
        profit, pos = 0, -prices[0]

        # loop through prices starting from the second element
        for i in range(1, len(prices)):
            # update position variable to store maximum between current position and previous profit - current price
            pos = max(pos, profit - prices[i])
            # update profit variable to store maximum between previous profit and (previous profit + current price - fee)
            profit = max(profit, pos + prices[i] - fee)

        # return maximum profit
        return profit
