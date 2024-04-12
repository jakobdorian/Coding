class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # a deque to store coordinates of rotten oranges
        q = deque()
        # variables to track time and count of fresh oranges
        time, fresh = 0, 0
        # get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # define possible directions to check neighboring cells
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # if the cell contains a fresh orange, increment the count of fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                # if the cell contains a rotten orange, add its coordinates to the deque
                if grid[r][c] == 2:
                    q.append([r,c])

        # continue processing while there are rotten oranges and fresh oranges remaining
        while q and fresh > 0:
            # process each rotten orange in the queue
            for i in range(len(q)):
                # get coordinates of a rotten orange from the queue
                r, c = q.popleft()
                # check neighboring cells in all directions
                for dr, dc in directions:
                    # calculate coordinates of neighboring cell
                    row, col = dr + r, dc + c
                    # if neighboring cell is out of bounds or already rotten, skip
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    # mark the neighboring fresh orange as rotten
                    grid[row][col] = 2
                    # add coordinates of the newly rotten orange to the queue
                    q.append([row,col])
                    # decrement the count of fresh oranges
                    fresh -= 1
            # increment the time as each minute passes
            time += 1

        # if all oranges have been rotten, return the time taken
        if fresh == 0:
            return time
        # if there are still fresh oranges remaining, return -1 indicating impossibility
        else:
            return -1
