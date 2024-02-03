class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # num of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        # pointers for binary search in rows
        top, bot = 0, rows - 1
        # binary search to find the row where the target might exist
        while top <= bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        # if the target is not within the possible rows, return false
        if not (top <= bot):
            return False
        # binary search in the selected row for the target
        row = (top+bot) // 2
        left, right = 0, cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        # if the target is not found in the selected row, return false
        return False
