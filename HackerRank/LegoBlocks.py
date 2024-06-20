def legoBlocks(n, m):
    MOD = 1000000007  # the modulus to prevent integer overflow and ensure results fit within standard integer limits.
    
    # a list to store the number of ways to fill a row of width i.
    row_ways = [0] * (m+1)
    row_ways[0] = 1  # there is one way to fill a row of width 0 (using no blocks).
    
    # calculate the number of ways to fill a row of each width from 1 to m.
    for i in range(1, m + 1):
        row_ways[i] = row_ways[i - 1]  # add ways to fill the row by adding a block of width 1.
        if i >= 2:
            row_ways[i] += row_ways[i - 2]  # add ways to fill the row by adding a block of width 2.
        if i >= 3:
            row_ways[i] += row_ways[i - 3]  # add ways to fill the row by adding a block of width 3.
        if i >= 4:
            row_ways[i] += row_ways[i - 4]  # add ways to fill the row by adding a block of width 4.
        row_ways[i] %= MOD  # apply modulus to keep the value within integer limits.
    
    # calculate the total number of ways to build each column of width i with n rows.
    total_ways = [pow(row_ways[i], n, MOD) for i in range(m+1)]
    
    # initialize a list to store the number of valid ways to build a wall of width i.
    res = [0] * (m+1)
    res[0] = 1  # there is one way to build a wall of width 0 (using no blocks).
    
    # calculate the number of valid ways to build a wall of each width from 1 to m.
    for i in range(1, m+1):
        res[i] = total_ways[i]  # start with the total number of ways to build the column.
        for k in range(1, i):
            # subbtract the invalid ways where the wall would be split into two parts.
            res[i] -= res[k] * total_ways[i - k]
            res[i] %= MOD  # apply modulus to keep the value within integer limits.
    
    return res[m]  # return the number of valid ways to build a wall of width m.
