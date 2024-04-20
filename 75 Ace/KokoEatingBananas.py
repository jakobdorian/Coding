class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        # set the result to the maximum possible speed initially
        res = right

        # binary search loop
        while left <= right:
            # calculate the mid value of the search space
            k = (left + right) // 2
            # total hours taken to eat all piles
            hours = 0
            # calculate total hours taken with current eating speed
            for p in piles:
                hours += math.ceil(p / k)
            
            # check if the total hours taken is less than or equal to given hours
            if hours <= h:
                # update result with current eating speed and move towards left
                res = min(res, k)
                right = k - 1
            else:
                # move towards right
                left = k + 1

        # return the minimum eating speed that satisfies the given hours
        return res
        