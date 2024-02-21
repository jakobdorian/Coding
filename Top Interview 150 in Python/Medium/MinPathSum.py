class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # determine the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # 2D list to store intermediate results
        res = [[float("inf")] * (cols + 1) for r in range(rows + 1)]
        
        # set the initial value for the bottom-right cell
        res[rows-1][cols] = 0

        # iterate through the grid starting from the bottom-right cell
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # calculate the minimum path sum for each cell
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
                
        # return the minimum path sum starting from the top-left cell
        return res[0][0]
