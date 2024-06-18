def minimumBribes(q):
    res = 0
    
    # traverse the queue from the end to the start
    for i in range(len(q)-1, -1, -1):
        # check if the current position is too chaotic
        # q[i] - (i + 1) gives the number of positions q[i] has moved forward
        if q[i] - (i + 1) > 2:
            # If any person has moved more than 2 positions forward, print "Too chaotic" and return
            print("Too chaotic")
            return
    
        # count how many times q[i] has been bribed
        # Wwe need to check positions from max(0, q[i] - 2) to i-1
        # this is because a person can only move up to 2 positions ahead, so we only need to check 2 positions behind the current position
        for j in range(max(0, q[i] - 2), i):
            # if a person at position j has a higher number than q[i], it means q[i] has been bribed
            if q[j] > q[i]:
                # Increment the bribe count
                res += 1
    
    # print the total number of bribes
    print(res)
