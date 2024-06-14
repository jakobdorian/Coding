def lonelyinteger(a):
    res = 0
    
    for num in a:
        res ^= num

    return res
