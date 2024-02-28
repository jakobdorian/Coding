class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # cache to store already computed values
        cache = {}

        # helper function to recursively find maximal square
        def helper(r,c):
            # base case: if index is out of bounds, return 0
            if r >= rows or c >= cols:
                return 0
            
            # if value is not computed before, calculate it
            if (r,c) not in cache:
                # recursively compute values down, right, and diagonal
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diagonal = helper(r + 1, c + 1)

                # value for the current position in cache
                cache[(r,c)] = 0
                
                # if current position has '1', compute maximal square
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,right,diagonal)

            # return the value stored in cache for the current position
            return cache[(r,c)]

        # start recursion from the top-left corner of the matrix
        helper(0, 0)
        
        # return the area of the maximal square found
        return max(cache.values()) ** 2
