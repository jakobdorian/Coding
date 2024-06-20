class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort the positions array to facilitate the distance calculations
        position.sort()
        
        # helper function to check if it's possible to place m balls
        # with at least 'min_dis' distance apart
        def helper(min_dis):
            count = 1  # start by placing the first ball at the first position
            last_pos = position[0]

            # iterate through the sorted positions to place the rest of the balls
            for i in range(1, len(position)):
                # check if the current position is at least 'min_dis' away from the last placed ball
                if position[i] - last_pos >= min_dis:
                    count += 1  
                    last_pos = position[i] 
                    if count == m:  # if all m balls are placed successfully
                        return True
            return False  
        
        # binary search range
        left, right = 1, position[-1] - position[0]
        res = 0  # variable to store the result of the maximum minimum distance

        # binary search to find the maximum minimum distance
        while left <= right:
            mid = (left + right) // 2  # calculate the middle value of the current range
            if helper(mid):  # check if it's possible to place balls with 'mid' distance
                res = mid
                left = mid + 1  # try for a larger distance
            else:
                right = mid - 1  # try for a smaller distance
        
        return res  # return the maximum minimum distance found
        