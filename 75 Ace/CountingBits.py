class Solution:
    def countBits(self, n: int) -> List[int]:
        # array dp to store the count of set bits for each number from 0 to n.
        dp = [0] * (n+1)
        
        # initialize offset to 1 for the first element.
        offset = 1

        # loop through the numbers from 1 to n.
        for i in range(1, n+1):
            # if i is a power of 2, update the offset.
            if offset * 2 == i:
                offset = i
            
            # calculate the count of set bits for the current number using previously computed values.
            dp[i] = 1 + dp[i - offset]
        
        # return the array containing the count of set bits for each number from 0 to n.
        return dp
