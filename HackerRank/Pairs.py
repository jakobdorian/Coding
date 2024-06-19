def pairs(k, arr):
    res = 0
    # convert the list to a set for O(1) average-time complexity membership tests
    numbers = set(arr)
    
    # iterate through each number in the list
    for num in arr:
        # check if the current number plus k exists in the set
        if (num + k) in numbers:
            # if it does, increment the result counter
            res += 1
    
    # return the total count of such pairs
    return res
