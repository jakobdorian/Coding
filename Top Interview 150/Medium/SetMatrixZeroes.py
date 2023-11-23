# O(1) sol
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        isZero = False

        # determine which rows/cols need to be zero
        for r in range(rows):
            for c in range(cols):
                # if val is zero
                if matrix[r][c] == 0:
                    # set the first row in this col to zero
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        isZero = True

        # fill in zeros, skip first row and col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # check if the origin of the matrix is 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
       # do we need to zero out the first row?
        if isZero:
            for c in range(cols):
                matrix[0][c] = 0
