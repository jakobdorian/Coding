def countingSort(arr):
    res = [0] * 100
    
    # iterate over each number in the input array `arr`
    for num in arr:
        # increment the count of the number `num` in the result list `res`
        # this essentially counts the occurrence of each number in `arr`
        res[num] += 1
    
    # return the result list `res` which now contains the counts of each number
    return res
