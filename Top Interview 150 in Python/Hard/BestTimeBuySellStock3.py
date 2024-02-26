class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get the length of the prices list
        n = len(prices)
        
        # if there are no or only one price, return 0 as no profit can be made
        if n <= 1:
            return 0

        # list to store profits for each day
        profits = [0] * n
        
        # variables to track minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0
        
        # iterate through prices to calculate profits for each day
        for i in range(1, n):
            # update minimum price encountered so far
            min_price = min(min_price, prices[i])
            # update maximum profit if selling at current price is more profitable
            max_profit = max(max_profit, prices[i] - min_price)
            # store the maximum profit achievable up to the current day
            profits[i] = max_profit

        # variables to track maximum price and total maximum profit
        max_price = prices[n - 1]
        max_profit = 0
        total_max_profit = 0
        
        # iterate through prices in reverse to find the total maximum profit
        for i in range(n - 2, -1, -1):
            # update maximum price encountered so far
            max_price = max(max_price, prices[i])
            # update maximum profit if buying at current price is more profitable
            max_profit = max(max_profit, max_price - prices[i])
            # update total maximum profit considering the profit from previous days and the profit from selling at the current day
            total_max_profit = max(total_max_profit, max_profit + profits[i])
            
        # return the total maximum profit achievable
        return total_max_profit
