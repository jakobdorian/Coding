class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        # run rotation
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                # save topleft val
                topLeft = matrix[top][left + i]
                # move bottomleft to topleft
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottomright to bottomleft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move topright to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # move topleft to topright
                matrix[top + i][right] = topLeft
            # update pointers
            left += 1
            right -= 1
