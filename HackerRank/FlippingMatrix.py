def flippingMatrix(matrix):
    # find the size of the quadrant
    n = len(matrix) // 2
    
    # initialize result to store the sum of maximum elements from quadrants
    res = 0
    
    # loop through each element in the top-left quadrant of the matrix
    for i in range(n):
        for j in range(n):
            # Elements in the corresponding quadrants
            topleft = matrix[i][j]
            topright = matrix[i][2 * n - 1 - j]
            bottomleft = matrix[2 * n - 1 - i][j]
            bottomright = matrix[2 * n - 1 - i][2 * n - 1 - j]
            
            # add the maximum of the four corresponding elements to the result
            res += max(topleft, topright, bottomleft, bottomright)
    
    # return the final computed result
    return res
