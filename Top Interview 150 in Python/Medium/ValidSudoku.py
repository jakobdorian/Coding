class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashsets
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        cells = collections.defaultdict(set)

        # iterate over entire grid
        for r in range(9):
            for c in range(9):
                # is this position empty?, if so skip
                if board[r][c] == ".":
                    continue
                # is this a duplicate?
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in cells[(r // 3, c // 3)]):
                    return False
                # if valid, update hashsets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                cells[(r // 3, c // 3)].add(board[r][c])
        return True
