def gridChallenge(grid):
    # sort each row of the grid alphabetically and store it in a new list 'sorted_g'
    sorted_g = [''.join(sorted(row)) for row in grid]
    
    # iterate over each column in the sorted rows
    for col in range(len(sorted_g[0])):
        # iterate over each row starting from the second row
        for row in range(1, len(sorted_g)):
            # compare the current element with the element in the previous row
            if sorted_g[row][col] < sorted_g[row-1][col]:
                # if any element in the current row is less than the element in the previous row,
                # return "NO" indicating that the columns are not sorted alphabetically
                return "NO"
    # if all columns are sorted alphabetically, return "YES"
    return "YES"
