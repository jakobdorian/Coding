class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check if the grid is empty
        if not grid:
            return 0
        
        # get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # BFS function to explore connected "1"s
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # define the directions to explore (up, down, left, right)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # explore neighboring cells
                for dr, dc in directions:
                    # calculate the new coordinates
                    nr, nc = row + dr, col + dc
                    # check if the new coordinates are within the grid and the cell is unvisited and contains "1"
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        # enqueue the new cell and mark it as visited
                        q.append((nr, nc))
                        visited.add((nr, nc))

        # iterate through all cells in the grid
        for r in range(rows):
            for c in range(cols):
                # check if the current cell contains "1" and is unvisited
                if grid[r][c] == "1" and (r, c) not in visited:
                    # explore the connected "1"s using BFS and increment the island count
                    bfs(r, c)
                    islands += 1
        
        # return the total number of islands
        return islands
        