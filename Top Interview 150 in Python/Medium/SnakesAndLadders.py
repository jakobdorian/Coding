class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()  # reversing the board for easier traversal

        # helper function to convert square number to row and column indices
        def helper(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()  # queue for BFS traversal
        q.append([1, 0])  # starting from square 1 with 0 moves
        visited = set()  # set to keep track of visited squares

        while q:
            square, moves = q.popleft()
            # roll the dice (try all possible outcomes)
            for i in range(1, 7):
                nextSquare = square + i
                r, c = helper(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]  # if there's a snake or ladder, move accordingly
                if nextSquare == length * length:
                    return moves + 1  # reached the last square, return the total moves
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])  # add the next square to the queue with updated moves
        # if the end is not reached, return -1 indicating it's not possib
        return -1
