def superDigit(n, k):
    # calculate the initial sum of digits of n and multiply by k
    res = sum((int(d) for d in str(n))) * k
    
    # reduce res to a single-digit number by repeatedly summing its digits
    while res >= 10:
        res = sum((int(d) for d in str(res)))

    # return the resulting single-digit number
    return res