class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0  
        empty = 0  
        
        # continue the process as long as there are full bottles to drink
        while numBottles > 0:
            res += numBottles  # drink all the full bottles and add to the result
            empty += numBottles  # all drunk bottles become empty
            
            # exchange empty bottles for full bottles
            numBottles = empty // numExchange  # get the number of full bottles after exchanging
            empty = empty % numExchange  # update the number of remaining empty bottles
        # return the total number of bottles drunk
        return res
