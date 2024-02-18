class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        # base case: zero coins needed to make up amount 0
        dp[0] = 0

        # iterate through each amount from 1 to the target amount
        # and update the minimum number of coins needed to make up that amount
        for i in range(len(dp)):
            for c in coins:
                # check if the current coin can contribute to making up the current amount
                if i - c >= 0:
                    # update dp[i] with the minimum of its current value and the value
                    # obtained by adding one coin (coin c) to the amount (i - c)
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        # if dp[-1] is still infinity, it means it's impossible to make up the amount
        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]

# Time complexity: O(n * m), where n is the target amount and m is the number of coins
# Space complexity: O(n), where n is the target amount
