# O(m*n), O(1) sol
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # keep looping until pointers meet
        while left < right and top < bottom:
            # get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            # update top, shift top down by one
            top += 1
            # get every i in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            # shift right to the left
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # get every i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            # update bottom
            bottom -= 1
            
            # get every i in left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # update left
            left += 1
        return res
