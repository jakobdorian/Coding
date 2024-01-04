class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get the dimensions of the board
        height = len(board)
        width = len(board[0])

        # check if the board is empty
        if not board:
            return 0
        
        # helper function to perform depth-first search and mark 'O' connected to border as 'C'
        def helper(r, c):
            if 0 <= r < height and 0 <= c < width and board[r][c] == 'O':
                board[r][c] = 'C'
                helper(r-1, c)
                helper(r+1, c)
                helper(r, c-1)
                helper(r, c+1)
        
        # mark 'O' connected to the top and bottom borders as 'C'
        for r in [0, height-1]:
            for c in range(width):
                helper(r, c)
        
        # mark 'O' connected to the left and right borders as 'C'
        for c in [0, width-1]:
            for r in range(height):
                helper(r, c)
        
        # update the board based on the marked cells ('C', 'O', 'X')
        for r in range(height):
            for c in range(width):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                    