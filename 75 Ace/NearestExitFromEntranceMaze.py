class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # get the dimensions of the maze
        rows = len(maze)
        cols = len(maze[0])

        # mark the entrance in the maze
        sx, sy = entrance
        maze[sx][sy] = "s"

        # mark exits on the edges of the maze
        for x in range(rows):
            if maze[x][0] == ".":
                maze[x][0] = "e"
            if maze[x][-1] == ".":
                maze[x][-1] = "e"
        for y in range(cols):
            if maze[0][y] == ".":
                maze[0][y] = "e"
            if maze[-1][y] == ".":
                maze[-1][y] = "e"

        # define possible movement directions
        directions = [(0,1), (1,0), (-1,0), (0, -1)]
        # initialize visited array to keep track of visited cells
        visited = [[False] * cols for _ in range(rows)]
        # initialize a queue for BFS traversal
        q = deque()

        # start BFS from the entrance
        q.append((0, sx, sy))
        visited[sx][sy] = True

        # BFS traversal
        while len(q) > 0:
            d, x, y = q.popleft()  # get current position and distance
            for dx, dy in directions:  # explore adjacent cells
                nx, ny = x + dx, y + dy
                # check if the next cell is within the maze and not visited
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # if the next cell is empty, mark it as visited and add to the queue
                    if maze[nx][ny] == ".":
                        visited[nx][ny] = True
                        q.append((d+1, nx, ny))
                    # if the next cell is an exit, return the distance
                    elif maze[nx][ny] == "e":
                        return d + 1
        # if there is no reachable exit, return -1
        return -1
