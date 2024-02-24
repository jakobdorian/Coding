class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # check if the combined length of s1 and s2 is equal to s3, if not, it's impossible to interleave them
        if len(s1) + len(s2) != len(s3):
            return False

        # dynamic programming table with dimensions (len(s1) + 1) x (len(s2) + 1)
        dp = [[False] * (len(s2)+1) for i in range(len(s1) + 1)]

        # base case: set the bottom-right cell to True, indicating empty strings match an empty string
        dp[len(s1)][len(s2)] = True

        # iterate through the DP table backwards, filling it up based on the characters in s1, s2, and s3
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # check if current characters from s1 and s3 match and the cell below is True
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                # check if current characters from s2 and s3 match and the cell to the right is True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        # return whether the top-left cell is True, indicating s1 and s2 can be interleaved to form s3
        return dp[0][0]
