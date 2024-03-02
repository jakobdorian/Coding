class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # the maximum number of candies among all kids.
        maxCandies = max(candies)
        
        # return a list indicating whether each kid can have the maximum number of candies 
        # if extraCandies were given to them.
        return [(curr + extraCandies >= maxCandies) for curr in candies]
