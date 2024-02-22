class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # extracting dimensions of the grid
        n, m = len(obstacleGrid[0]), len(obstacleGrid)

        # 2D array to store number of unique paths
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # handling obstacles in the first row
        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
        
        # handling obstacles in the first column
        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
        
        # iterating through the grid to calculate unique paths
        for r in range(1, m):
            for c in range(1, n):
                # if obstacle found, continue to the next iteration
                if obstacleGrid[r][c] == 1:
                    continue
                # calculate unique paths by summing paths from top and left cells
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        # returning the number of unique paths to reach the bottom-right cell
        return dp[-1][-1]

# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m * n) for the dp array.
