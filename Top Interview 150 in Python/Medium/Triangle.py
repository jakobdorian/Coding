class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # store the cumulative minimum path sum from bottom to top
        dp = [0] * (len(triangle)+1)
        # iterate through each row of the triangle from bottom to top
        for row in triangle[::-1]:
            # iterate through each element in the current row
            for i, n in enumerate(row):
                # update `dp[i]` with the minimum sum path from the current row to the bottom
                dp[i] = n + min(dp[i], dp[i+1])
        # return the minimum sum path starting from the top of the triangle
        return dp[0]
