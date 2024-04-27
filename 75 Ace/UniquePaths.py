# o(n*m) time complexity
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # a list representing a row with all values set to 1,
        # since there is only one way to reach each cell in the first row.
        row = [1] * n 
        
        # iterate through each row, starting from the second row.
        for i in range(m - 1):
            # create a new row with all values initially set to 1.
            newRow = [1] * n
            
            # calculate the number of unique paths for each cell in the current row.
            # starting from the second to last column and moving towards the first column.
            for j in range(n - 2, -1 , -1):
                # the number of unique paths to reach a cell is the sum of the paths
                # from the cell to its right and the cell below it in the previous row.
                newRow[j] = newRow[j + 1] + row[j]
            
            # update the current row with the newly calculated values for the next iteration.
            row = newRow
        
        # return the number of unique paths to reach the bottom-right cell (0,0).
        return row[0]
