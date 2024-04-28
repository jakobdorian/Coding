class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # get the lengths of the input texts
        n, m = len(text1), len(text2)

        # DP table with dimensions (n+1) x (m+1) filled with zeros
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # iterate through each character in text1
        for r in range(1, n + 1):
            # iterate through each character in text2
            for c in range(1, m + 1):
                # if the characters at current positions match
                if text1[r-1] == text2[c-1]:
                    # increment the value in the DP table diagonally by 1
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    # if the characters don't match, take the maximum of the values above and to the left
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        # return the value at the bottom-right corner of the DP table
        return dp[-1][-1]
