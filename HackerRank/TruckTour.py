def truckTour(petrolpumps):
    # get the number of petrol pumps
    n = len(petrolpumps)
    current_petrol, total_petrol, total_distance = 0, 0, 0
    res = 0
    
    # iterate through each petrol pump
    for i in range(n):
        # get the petrol and distance for the current pump
        petrol, distance = petrolpumps[i]
        
        # add the petrol and distance to the total values
        total_petrol += petrol
        total_distance += distance
        
        # update the current petrol by adding the petrol from the pump and subtracting the distance to the next pump
        current_petrol += petrol - distance
        
        # if current petrol is less than 0, we cannot start from the previous pumps
        if current_petrol < 0:
            # move the starting index to the next pump
            res = i + 1
            # reset the current petrol
            current_petrol = 0
    
    # check if the total petrol is enough to cover the total distance
    if total_petrol >= total_distance:
        # if yes, return the starting pump index
        return res
    else:
        # if not, return -1 indicating no solution
        return -1
