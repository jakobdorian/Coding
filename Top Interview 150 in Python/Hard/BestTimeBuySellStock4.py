class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        # if there are no prices or only one price, there is no profit
        if n <= 1:
            return 0

        # if the allowed number of transactions is greater than or equal to the maximum possible transactions,
        # we can just perform as many transactions as possible to maximize profit
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # dynamic programming table initialization with all elements set to 0
        dp = [[0] * n for _ in range(k + 1)]

        # loop through all possible transactions
        for i in range(1, k + 1):
            # max_diff to track the maximum difference between current price and previous prices
            max_diff = -prices[0]
            for j in range(1, n):
                # the maximum profit at j-th day with at most i transactions is either:
                # 1. the maximum profit without any transaction on j-th day, same as the profit of previous day (dp[i][j-1])
                # 2. the maximum profit that can be obtained by completing a transaction on j-th day, 
                #    i.e., price[j] + maximum profit on (j-1)th day - cost of buying stock on j-th day (max_diff)
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                
                # update max_diff to track the maximum difference for the next iteration
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
                
        # maximum profit after k transactions is stored in the last cell of the dynamic programming table
        return dp[k][n - 1]
