class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, row, col):
            allSame = True
            # nested loops to check if all elements in the subgrid are the same
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row+i][col+j]:
                        allSame = False
            # if all elements are the same, create a leaf node
            if allSame:
                return Node(grid[row][col], True)
            # if not all elements are the same, divide the subgrid into four quadrants
            n = n // 2
            topLeft = dfs(n, row, col)
            topRight = dfs(n, row, col + n)
            bottomLeft = dfs(n, row + n, col)
            bottomRight = dfs(n, row + n, col + n)
            # create a non-leaf node with the four quadrant nodes
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        # start the depth-first search with the entire grid
        return dfs(len(grid), 0, 0)
