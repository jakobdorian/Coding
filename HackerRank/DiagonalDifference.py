def diagonalDifference(arr):
    # calculate the size of the array
    n = len(arr)
    
    # initialize sums for primary and secondary diagonals
    primary  = 0
    secondary = 0
    
    # loop through each row of the square matrix
    for i in range(n):
        # add the element from the primary diagonal (left to right)
        primary += arr[i][i]
        # add the element from the secondary diagonal (right to left)
        secondary += arr[i][n - 1 - i]
    
    # return the absolute difference between the sums of the diagonals
    return abs(primary - secondary)
