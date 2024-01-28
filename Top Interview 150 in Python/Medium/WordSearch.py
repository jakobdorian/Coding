class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get the number of rows and columns in the board
        rows = len(board)
        cols = len(board[0])
        # set to keep track of visited cells
        path = set()
        # dfs search
        def dfs(r, c, i):
            # base case: if the entire word is found
            if i == len(word):
                return True
            # check for out-of-bounds or mismatch conditions
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or word[i] != board[r][c] or (r, c) in path):
                return False
            # mark the current cell as visited
            path.add((r, c))
            # explore adjacent cells in all four directions
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            # backtrack: remove the current cell from the visited set
            path.remove((r, c))
            return res
        # iterate through all cells in the board
        for r in range(rows):
            for c in range(cols):
                # if the word is found starting from the current cell, return True
                if dfs(r, c, 0):
                    return True
        # if the word is not found starting from any cell, return False
        return False
